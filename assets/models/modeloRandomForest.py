# Importar bibliotecas
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import cohen_kappa_score
from imblearn.over_sampling import SMOTE  

# 1. Carregamento e limpeza do dataset
df = pd.read_csv("uniao_das_bases.csv")

# Remover registros sem salario ou faixa salarial
df = df[df["Salario_Medio"].notnull() & df["Faixa_Salarial"].notnull()].copy()

# 2. Agrupamento de faixas salariais com base na semântica real da base
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

# Aplicar função personalizada
df["Faixa_Salarial_Agrupada"] = df["Faixa_Salarial"].apply(agrupa_faixas)

# 3. Seleção de colunas de entrada e target
cols = [
    "Idade", 
    "Num_func_empresa_que_trabalha", 
    "Setor", 
    "Cargo_Atual",
    "Nivel_de_Ensino", 
    "Tempo_de_experiencia_na_area_de_dados",
    "Uf", 
    "Genero", 
    "Cor/Raça/Etnia", 
    "Atual_forma_de_trabalho", 
    "Situacao_atual_de_trabalho", 
    "Python", 
    "R", 
    "SQL", 
    "Nível"
]
X = df[cols].copy()
y = df["Faixa_Salarial_Agrupada"].copy()

X[["Python", "SQL", "R"]] = X[["Python", "SQL", "R"]].fillna(0)

# 4. Preencher valores nulos com "Desconhecido" para categorias
for col in X.select_dtypes(include="object").columns:
    X[col].fillna("Desconhecido", inplace=True)

# 5. Codificação de variáveis categóricas (one-hot encoding) e padronização
X_encoded = pd.get_dummies(X, drop_first=True)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_encoded)

# 6. Codificar a variável alvo com LabelEncoder para simular ordinalidade
le = LabelEncoder()
y_encoded = le.fit_transform(y)  # Baixa = 0, Média = 1, Alta = 2

# 7. Separação em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.2, random_state=42)

# 8. Aplicar SMOTE para balancear as classes no conjunto de treino
smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

# 9. Treinar modelo Random Forest com dados balanceados
rf = RandomForestClassifier(random_state=42, max_depth = 7, n_estimators = 100, max_features=0.5, min_samples_leaf=5, class_weight='balanced')
rf.fit(X_train_res, y_train_res)

# 10. Previsão e avaliação
y_pred = rf.predict(X_test)

# Relatórios de performance
print("Acurácia:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=le.classes_))

# Matriz de confusão
ordem_desejada = ['Alta', 'Média', 'Baixa']
labels_ordinais = le.transform(ordem_desejada)
cm = confusion_matrix(y_test, y_pred, labels=labels_ordinais)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=ordem_desejada)
disp.plot(cmap="Oranges")
plt.title("Matriz de Confusão (Ordem Ordinal)")
plt.show()

# 11. Métrica adicional: Kappa Ponderado (Quadrático)
kappa_quadratico = cohen_kappa_score(y_test, y_pred, weights='quadratic')
print("Cohen's Quadratic Kappa:", kappa_quadratico)

# 12. Gráfico das 15 variáveis mais importantes
importances = rf.feature_importances_
indices = np.argsort(importances)[::-1][:15]
features = X_encoded.columns[indices]

plt.figure(figsize=(10, 6))
sns.barplot(x=importances[indices], y=features)
plt.title("Top 15 Variáveis Mais Importantes - Random Forest")
plt.xlabel("Importância")
plt.ylabel("Variável")
plt.tight_layout()
plt.show()

# Avaliar o desempenho no conjunto de treino (após o ajuste com SMOTE)
y_train_pred = rf.predict(X_train_res)
print("\n--- Desempenho no conjunto de TREINO ---")
print("Acurácia (treino):", accuracy_score(y_train_res, y_train_pred))
print(classification_report(y_train_res, y_train_pred, target_names=le.classes_))

# Comparação treino vs teste
acc_train = accuracy_score(y_train_res, y_train_pred)
acc_test = accuracy_score(y_test, y_pred)

results_rf = pd.DataFrame({
    "Conjunto": ["Treino", "Teste"],
    "Acurácia": [acc_train, acc_test]
})

plt.figure(figsize=(6, 4))
sns.barplot(data=results_rf, x="Conjunto", y="Acurácia", palette="Blues")
plt.ylim(0, 1)
plt.title("Acurácia Random Forest - Treino vs Teste")
plt.ylabel("Acurácia")
plt.tight_layout()
plt.show()
