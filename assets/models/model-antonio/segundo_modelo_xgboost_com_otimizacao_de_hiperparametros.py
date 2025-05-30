import xgboost as xgb
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import GridSearchCV

# 1. Preparação dos dados para XGBoost
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)

# 2. Definição dos parâmetros iniciais
params = {
    'objective': 'reg:squarederror',
    'learning_rate': 0.1,
    'max_depth': 5,
    'subsample': 0.8,
    'colsample_bytree': 0.8,
    'n_estimators': 100
}

# 3. Otimização de hiperparâmetros
param_grid = {
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.1, 0.2],
    'subsample': [0.6, 0.8, 1.0],
    'colsample_bytree': [0.6, 0.8, 1.0]
}

grid_search = GridSearchCV(
    estimator=xgb.XGBRegressor(**params),
    param_grid=param_grid,
    cv=3,
    scoring='neg_mean_absolute_error',
    verbose=1
)

grid_search.fit(X_train, y_train)

# 4. Melhores parâmetros
best_params = grid_search.best_params_
print(f"Melhores parâmetros: {best_params}")

# 5. Modelo final com melhores parâmetros
modelo_xgb = xgb.XGBRegressor(**best_params)
modelo_xgb.fit(X_train, y_train)

# 6. Previsões e avaliação
y_pred = modelo_xgb.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nMAE: {mae:.2f}")
print(f"R²: {r2:.4f}")

# 7. Visualização da importância das features
plt.figure(figsize=(10,6))
xgb.plot_importance(modelo_xgb, max_num_features=10)
plt.title('Importância das Variáveis - XGBoost')
plt.show()

# 8. Análise de previsões vs valores reais
plt.figure(figsize=(10,6))
sns.scatterplot(x=y_test, y=y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--')
plt.xlabel('Valores Reais')
plt.ylabel('Previsões')
plt.title('Comparação entre Valores Reais e Previsões')
plt.show()
