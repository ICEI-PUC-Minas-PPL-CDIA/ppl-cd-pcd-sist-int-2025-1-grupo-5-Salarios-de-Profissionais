import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar os dados
df = pd.read_csv("uniao_das_bases.csv")
df = df[df["Salario_Medio"].notnull() & df["Faixa_Salarial"].notnull()].copy()

# 2. Agrupar faixa salarial com base em quantis
quantis = df["Salario_Medio"].quantile([0.33, 0.66])
lim_baixa, lim_media = quantis[0.33], quantis[0.66]

def faixa_quantis(s):
    if s <= lim_baixa:
        return "Baixa"
    elif s <= lim_media:
        return "Média"
    else:
        return "Alta"

df["Faixa_Salarial_Quantis"] = df["Salario_Medio"].apply(faixa_quantis)

# 3. Selecionar colunas
cols = [
    "Idade", "Num_func_empresa_que_trabalha", "Setor", "Cargo_Atual", "Nivel_de_Ensino", "Nível",
    "Tempo_de_experiencia_na_area_de_dados", "Uf", "Genero", "Cor/Raça/Etnia",
    "Atual_forma_de_trabalho", "Situacao_atual_de_trabalho"
]
X = df[cols].copy()
y = df["Faixa_Salarial_Quantis"]

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

# 4. Treinar Random Forest
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)

# 5. Treinar XGBoost com hiperparâmetros otimizados
xgb = XGBClassifier(
    learning_rate=0.1,
    max_depth=5,
    n_estimators=100,
    subsample=1.0,
    use_label_encoder=False,
    eval_metric="mlogloss",
    random_state=42
)
xgb.fit(X_train, y_train)

# 6. Avaliar XGBoost
y_pred = xgb.predict(X_test)
print("Acurácia:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=le.classes_))
ConfusionMatrixDisplay.from_predictions(le.inverse_transform(y_test), le.inverse_transform(y_pred), cmap="Oranges").plot()

# 7. Gráfico das 15 variáveis mais importantes do XGBoost
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