import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar e filtrar dados
df = pd.read_csv("uniao_das_bases.csv")
df = df[df["Salario_Medio"].notnull() & df["Faixa_Salarial"].notnull()].copy()

# 2. Agrupar faixa salarial usando quantis
quantis = df["Salario_Medio"].quantile([0.33, 0.66])
lim_baixa, lim_media = quantis[0.33], quantis[0.66]

def faixa_quantis(salario):
    if salario <= lim_baixa:
        return "Baixa"
    elif salario <= lim_media:
        return "Média"
    else:
        return "Alta"

df["Faixa_Salarial_Quantis"] = df["Salario_Medio"].apply(faixa_quantis)

# 3. Selecionar colunas de entrada
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
    "Situacao_atual_de_trabalho"
]
X = df[cols].copy()
y = df["Faixa_Salarial_Quantis"]

# 4. Preencher valores nulos
for col in X.select_dtypes(include="object").columns:
    X[col].fillna("Desconhecido", inplace=True)

# 5. Codificação e normalização
X_encoded = pd.get_dummies(X, drop_first=True)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_encoded)

# 6. Codificação da variável target
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# 7. Separar dados em treino/teste
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.2, random_state=42)

# 8. Treinar modelo Random Forest
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)

# 9. Avaliação
y_pred = rf.predict(X_test)
print("Acurácia:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=le.classes_))

ConfusionMatrixDisplay.from_predictions(le.inverse_transform(y_test), le.inverse_transform(y_pred), cmap="Greens").plot()

# 10. Gráfico das 15 variáveis mais importantes
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