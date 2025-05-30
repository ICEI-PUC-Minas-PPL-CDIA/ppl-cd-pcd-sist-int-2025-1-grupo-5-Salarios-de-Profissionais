import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

# Pré-processamento dos dados
df = pd.read_csv('dados_projeto.csv')

# 1. Tratamento de valores ausentes
df['Nivel_de_Ensino'].fillna('Pós-graduação', inplace=True)
df.dropna(subset=['Salario_Medio', 'Tempo_de_experiencia_na_area_de_dados', 
                 'PIB_2021_OR', 'IDHM'], inplace=True)

# 2. Codificação de variáveis categóricas
nivel_ensino_map = {
    'Graduação': 1,
    'Pós-graduação': 2,
    'Mestrado': 3,
    'Doutorado': 4
}
df['Nivel_de_Ensino'] = df['Nivel_de_Ensino'].map(nivel_ensino_map)

# 3. Engenharia de features
df['Formacao_X_Experiencia'] = df['Nivel_de_Ensino'] * df['Tempo_de_experiencia_na_area_de_dados']

# 4. One-hot encoding para setores
setores_dummies = pd.get_dummies(df['Setor'], prefix='Setor', drop_first=True)

# 5. Normalização de PIB e IDHM
scaler = StandardScaler()
df[['PIB_2021_OR_norm', 'IDHM_norm']] = scaler.fit_transform(df[['PIB_2021_OR', 'IDHM']])

# 6. Preparação da matriz de features
X = pd.concat([df[['Nivel_de_Ensino', 'Tempo_de_experiencia_na_area_de_dados',
                  'Formacao_X_Experiencia']],
              setores_dummies,
              df[['PIB_2021_OR_norm', 'IDHM_norm']]], axis=1)
y = df['Salario_Medio']

# 7. Divisão treino-teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 8. Modelagem OLS com statsmodels
X_train_sm = sm.add_constant(X_train)
modelo_ols = sm.OLS(y_train, X_train_sm).fit()

# 9. Resultados do modelo
print(modelo_ols.summary())

# 10. Visualização dos coeficientes
coeficientes = modelo_ols.params[1:4]
plt.figure(figsize=(10,6))
coeficientes.plot(kind='bar')
plt.title('Impacto das Variáveis Principais no Salário')
plt.ylabel('Coeficiente (R$)')
plt.xticks(rotation=45)
plt.show()

# 11. Análise de resíduos
residuos = modelo_ols.resid
plt.figure(figsize=(10,6))
sns.histplot(residuos, kde=True)
plt.title('Distribuição dos Resíduos')
plt.xlabel('Resíduos')
plt.show()
