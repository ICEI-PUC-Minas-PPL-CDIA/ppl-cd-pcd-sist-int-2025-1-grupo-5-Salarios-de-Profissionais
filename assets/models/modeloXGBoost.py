# Importar bibliotecas
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay, cohen_kappa_score
import matplotlib.pyplot as plt
import seaborn as sns
from imblearn.over_sampling import SMOTE

# 1. Carregar os dados
df = pd.read_csv("uniao_das_bases.csv")
df = df[df["Salario_Medio"].notnull() & df["Faixa_Salarial"].notnull()].copy()

# 2. Agrupar faixa salarial com base semântica real

def agrupa_faixas(s):
    if s in [
        'Menos de R$ 1.000/mês',
        'de R$ 101/mês a R$ 2.000/mês',
        'de R$ 1.001/mês a R$ 2.000/mês',
        'de R$ 2.001/mês a R$ 3.000/mês'
    ]:
        return 'Baixa'
    elif s in [
        'de R$ 3.001/mês a R$ 4.000/mês',
        'de R$ 4.001/mês a R$ 6.000/mês',
        'de R$ 6.001/mês a R$ 8.000/mês',
        'de R$ 8.001/mês a R$ 12.000/mês'
    ]:
        return 'Média'
    else:
        return 'Alta'

# Aplicar agrupamento
df["Faixa_Salarial_Quantis"] = df["Faixa_Salarial"].apply(agrupa_faixas)

# 3. Selecionar colunas
cols = [
    "Idade", 
    "Num_func_empresa_que_trabalha", 
    "Setor", 
    "Cargo_Atual", 
    "Nivel_de_Ensino", 
    "Nível",
    "Tempo_de_experiencia_na_area_de_dados", 
    "Uf", 
    "Genero", 
    "Cor/Raça/Etnia",
    "Atual_forma_de_trabalho", 
    "Situacao_atual_de_trabalho",
    "Python",
    "SQL",
    "R"
]
X = df[cols].copy()
y = df["Faixa_Salarial_Quantis"]

X[["Python", "SQL", "R"]] = X[["Python", "SQL", "R"]].fillna(0) 

for col in X.select_dtypes(include="object").columns:
    X[col] = X[col].fillna("Desconhecido")

X = pd.get_dummies(X, drop_first=True)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Codificar y
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Treino/teste
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.2, random_state=42)

# Aplicar SMOTE
smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

# Treinar XGBoost com hiperparâmetros otimizados
xgb = XGBClassifier(
    learning_rate=0.1,
    max_depth=5,
    n_estimators=100,
    subsample=1.0,
    use_label_encoder=False,
    eval_metric="mlogloss",
    random_state=42
)
xgb.fit(X_train_res, y_train_res)

# Avaliar XGBoost
y_pred = xgb.predict(X_test)
print("Acurácia:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=le.classes_))
print("Cohen's Quadratic Kappa:", cohen_kappa_score(y_test, y_pred, weights='quadratic'))

# Matriz de confusão com ordem ordinal
ordem_desejada = ['Alta', 'Média', 'Baixa']
labels_ordinais = le.transform(ordem_desejada)
cm = confusion_matrix(y_test, y_pred, labels=labels_ordinais)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=ordem_desejada)
disp.plot(cmap="Oranges")
plt.title("Matriz de Confusão (Ordem Ordinal)")
plt.show()

# Gráfico das 15 variáveis mais importantes do XGBoost
importances = xgb.feature_importances_
indices = np.argsort(importances)[::-1][:15]
features = X.columns[indices]

plt.figure(figsize=(10, 6))
sns.barplot(x=importances[indices], y=features)
plt.title("Top 15 Variáveis Mais Importantes - XGBoost")
plt.xlabel("Importância")
plt.ylabel("Variável")
plt.tight_layout()
plt.show()

# Comparação de performance no treino e teste (XGBoost)
acc_xgb_train = xgb.score(X_train_res, y_train_res)
acc_xgb_test = xgb.score(X_test, y_test)

results_xgb = pd.DataFrame({
    "Conjunto": ["Treino", "Teste"],
    "Acurácia": [acc_xgb_train, acc_xgb_test]
})

plt.figure(figsize=(6, 4))
sns.barplot(data=results_xgb, x="Conjunto", y="Acurácia", palette="Oranges")
plt.ylim(0, 1)
plt.title("Acurácia XGBoost - Treino vs Teste")
plt.ylabel("Acurácia")
plt.tight_layout()
plt.show()
