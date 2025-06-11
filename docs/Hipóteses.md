## [Preparação dos Dados] Hipótese 1: Correlação entre salário, PIB e IDHM

### 1. Tratamento de Valores Ausentes
**Objetivo:**  
Garantir qualidade dos dados removendo/tratando registros incompletos.

**Processo Realizado:**
- Remoção de registros sem PIB ou IDHM (variáveis centrais)
- Preenchimento de experiência desconhecida com moda ("1 a 2 anos")

**Lógica das Decisões:**
- Dados macroeconômicos (PIB/IDHM) não podem ser imputados
- Experiência preenchida com valor mais frequente para minimizar distorções

### 2. Transformação de Variáveis
**Objetivo:**  
Preparar dados para análise estatística com distribuições adequadas.

**Principais Transformações:**
a) **Logarítmica do Salário**  
   - Motivo: Corrigir assimetria e reduzir impacto de outliers
   - Benefícios: Relação mais linear com outras variáveis

b) **One-Hot Encoding**  
   - Categorias convertidas em colunas binárias (ex: Nível → Júnior/Pleno/Sênior)
   - `drop_first=True` para evitar multicolinearidade

c) **Normalização (PIB e IDHM)**  
   - Padronização para mesma escala (média=0, desvio=1)
   - Permite comparação direta de coeficientes

### 3. Engenharia de Features
**Objetivo:**  
Criar variáveis que capturem relações complexas.

**Features Criadas:**
a) **Interação PIB-IDHM**  
   - Captura efeito combinado desenvolvimento econômico e humano
   - Ex: Estados com alto PIB + baixo IDHM podem ter comportamento distinto

b) **Categorização por Região**  
   - Agrupamento por similaridade socioeconômica
   - Vantagens: Redução de ruído e identificação de padrões regionais

c) **Variáveis de Controle**  
   - Dummies para experiência e senioridade
   - Isolam efeito de PIB/IDHM controlando fatores individuais/organizacionais

### Fluxo Lógico
1. **Tratamento de dados faltantes** → Base limpa
2. **Transformação de variáveis** → Preparação para modelagem
3. **Criação de novas features** → Aprimoramento explicativo

**Princípios Orientadores:**  
✓ Interpretabilidade ✓ Preservação estatística ✓ Facilitar análise causal

## Hipótese 2: Como o tamanho da empresa e setor afetam o salário
### 1. Tratamento de Valores Ausentes
Objetivo:
Assegurar a qualidade e consistência dos dados, eliminando registros incompletos ou realizando o tratamento adequado para permitir a modelagem preditiva sem viés ou perda de performance.

Processo Realizado:

Preenchimento de valores ausentes na variável ‘Tempo_de_experiencia_na_area_de_dados’:
Para os casos em que essa variável estava ausente, foi realizada a imputação com a moda da variável — “de 1 a 2 anos” — com o objetivo de manter a consistência sem gerar distorções significativas nos resultados. Essa abordagem se justifica pela predominância desse valor na amostra.

### 2. Hipótese do Estudo
Hipótese:
O salário médio de profissionais da área de dados é influenciado por fatores como o porte da empresa, o setor de atuação, o cargo atual, o nível de ensino e o tempo de experiência na área (Os valores finais do resusltado dos modelos tiveram a adição de "Genero", "Cor/Raça/Etnia", "Nível" e "Nível_de_Ensino" como variáveis, e demonstraram maior precisão devido a isso).

### 3. Transformações e Pré-processamento dos Dados
Processo Realizado:

Mapeamento de categorias para valores numéricos:
As categorias de número de funcionários na empresa e tempo de experiência foram convertidas para valores médios representativos, permitindo sua utilização em modelos de regressão.

Conversão para valores numéricos e remoção de inconsistências:
Foi realizada a conversão dos campos categóricos mapeados para valores numéricos, sendo removidos os registros que ainda apresentavam erros ou valores ausentes após a transformação.

Codificação de variáveis categóricas (One-hot Encoding):
As variáveis categóricas restantes foram transformadas em variáveis binárias por meio do método de one-hot encoding, evitando ordenações implícitas e viabilizando o uso em modelos estatísticos.

### 4. Modelagem Preditiva
Modelos Utilizados:

=== Regressão Linear ===

Erro Absoluto Médio (MAE): 2.605,37

Coeficiente de Determinação (R²): 0,528

=== XGBoost Regressor ===

Erro Absoluto Médio (MAE): 2.766,00

Coeficiente de Determinação (R²): 0,478


=== Novo Modelo XGBoost ===
MAE: 2366.31
R²: 0.6030
Acurácia por Faixa: 37.86%
(Acurácia por faixa se refere ao fato de que embora o teste tenha sido feito com o salario médio das faixas, o correto seria o valor se encontrar dentro da faixa esperada, nesse caso, apenas %37,86 das vezes o valor previsto se encontra na faixa real, entretanto, o MAE diminui em comparação com os outros modelos testados e o R² aumentou)


(O teste abaixo foi feito considerando apenas as 2 variáveis pensadas inicialmente na hipótese)
=== Regressão Linear ===
MAE: 5323.6442419655605
R²: 0.01065716316951204

=== XGBoost ===
MAE: 5360.752834262643
R²: -0.0038376364030112686

Interpretação dos Resultados:
Os dois modelos apresentaram desempenhos comparáveis, com ligeira vantagem para a regressão linear em termos de erro médio e explicação da variância do salário. O valor de R² indica que aproximadamente 50% da variação nos salários pode ser explicada pelas variáveis incluídas no modelo, o que demonstra uma relação moderada.

A performance do modelo XGBoost, embora inferior, pode estar relacionada à ausência de ajustes finos em seus hiperparâmetros, ou ainda à predominância de relações lineares entre as variáveis.

O segundo teste foi feito usando apenas as variáveis: Número de funcionários da empresa e Setor da empresa. O modelo apresentou resultados que apontam um correlação mínima com o salário.

### 5. Considerações Finais
Os resultados obtidos sugerem que a hipótese é parcialmente confirmada. Variáveis como setor de atuação, porte da empresa, nível de ensino, cargo atual e tempo de experiência apresentam influência sobre a variável resposta (salário médio). No entanto, o modelo também indica que existem outros fatores não considerados neste estudo que podem impactar significativamente o salário dos profissionais da área de dados.

Próximos passos :

Incluir variáveis geográficas e socioeconômicas (PIB, IDHM, custo de vida). (Não houve essa adição, pois há outra hipótese que foca na influência de tais variáveis)

Analisar interações entre variáveis (ex.: setor * cargo).

Ajustar hiperparâmetros de modelos não-lineares como o XGBoost.

Testar modelos adicionais com maior capacidade de generalização.

## Hipótese 5: Associação entre Formação Acadêmica e Salário dos Profissionais de Dados (CORRIGIDA)

### 1. Definição da Hipótese

**Hipótese**: Profissionais com pós-graduação, mestrado ou doutorado tendem a estar **associados** a salários mais altos do que aqueles com apenas graduação, mesmo após controlar para experiência, setor, PIB/IDHM do estado e outras variáveis relevantes.

**Nota importante**: Este é um estudo observacional que identifica **associações**, não relações causais.

### 2. Preparação dos Dados

#### 2.1 Seleção de Variáveis
- **Variável dependente**: Salario_Medio (em R$)
- **Variáveis independentes principais**:
  - Nivel_de_Ensino (Graduação, Pós-graduação, Mestrado, Doutorado)
  - Tempo_de_experiencia_na_area_de_dados (em anos)
- **Variáveis de controle**:
  - Setor (categoria da empresa)
  - PIB_2021_OR (PIB do estado, normalizado)
  - IDHM (Índice de Desenvolvimento Humano Municipal, normalizado)

#### 2.2 Tratamento de Valores Ausentes (CORRIGIDO)
- **Problema anterior**: Imputação inadequada usando apenas a moda
- **Solução implementada**: Imputação inteligente baseada em salário e experiência
- **Lógica**: Profissionais com salários e experiência similares tendem a ter formação similar
- **Para experiência**: KNN Imputer com k=5 vizinhos mais próximos

#### 2.3 Codificação de Variáveis (CORRIGIDA)
- **Problema anterior**: Codificação ordinal forçando linearidade (1,2,3,4)
- **Solução implementada**: Codificação dummy (one-hot encoding)
- **Vantagem**: Permite relações não-lineares entre níveis de formação
- **Referência**: Graduação (categoria omitida)

#### 2.4 Verificação de Qualidade
- **Multicolinearidade**: VIF < 5 para todas as variáveis
- **Normalização**: Variáveis numéricas padronizadas (média=0, desvio=1)
- **Validação cruzada**: K-fold (k=5) para estimativas robustas

### 3. Modelagem e Validação

#### 3.1 Divisão dos Dados
- **Conjunto de treino**: 80% dos dados (estratificado por quartis de salário)
- **Conjunto de teste**: 20% dos dados
- **Método**: Amostragem estratificada para manter distribuição original

#### 3.2 Modelos Implementados
1. **Regressão Linear Múltipla (OLS)**
   - R² = 0.611 (61,1% da variação explicada)
   - MAE = R$ 4.936
   - Validação cruzada: R² = 0.608 ± 0.023

2. **Random Forest (comparação)**
   - R² = 0.545
   - MAE = R$ 5.349
   - Validação cruzada: R² = 0.542 ± 0.031

### 4. Resultados

#### 4.1 Associações Identificadas
- **Experiência**: +R$ 4.961 por ano adicional
- **Setor Tecnologia**: +R$ 2.089 vs. setor de referência
- **Setor Financeiro**: +R$ 1.946 vs. setor de referência
- **PIB do estado**: +R$ 591 por desvio padrão
- **IDHM**: Associação positiva com salário

#### 4.2 Estatísticas Descritivas por Formação
| Nível | N | Média Salarial | Desvio Padrão | Mediana |
|-------|---|----------------|---------------|---------|
| Graduação | 1.798 | R$ 12.857 | R$ 8.420 | R$ 11.200 |
| Pós-graduação | 676 | R$ 17.205 | R$ 7.890 | R$ 16.800 |
| Mestrado | 210 | R$ 21.010 | R$ 9.340 | R$ 20.100 |
| Doutorado | 1.818 | R$ 27.574 | R$ 11.250 | R$ 26.400 |

### 5. Discussão e Interpretação

#### 5.1 Interpretação dos Resultados
- **Associação robusta**: Níveis mais altos de formação estão associados a salários maiores
- **Controle de confundidores**: Resultados controlam para experiência, setor e fatores regionais
- **Magnitude substancial**: Diferenças significativas entre níveis de formação

#### 5.2 Limitações Importantes
1. **Causalidade**: Este estudo é observacional e identifica **associações**, não relações causais
2. **Variáveis omitidas**: Fatores não observados (habilidades, networking, qualidade da instituição) podem influenciar tanto formação quanto salário
3. **Viés de seleção**: Profissionais que buscam maior formação podem ter características não observadas que também afetam o salário
4. **Efeito de sinalização**: Parte da associação pode ser devido ao valor da formação como "sinal" de competência
5. **Contexto temporal**: Resultados refletem o mercado brasileiro de dados em 2023

### 6. Conclusões

#### 6.1 Principais Achados
- **Associação positiva** entre nível de formação e salário
- **Experiência** é o fator mais importante (R$ 4.961/ano)
- **Setor** e **localização** também são relevantes
- **Modelo explica** 61% da variação salarial

#### 6.2 Implicações Práticas
- **Para profissionais**: Formação adicional está associada a maiores salários, mas deve ser considerada junto com experiência
- **Para empregadores**: Múltiplos fatores além da formação influenciam produtividade
- **Para políticas**: Investimento em educação pode estar associado a melhores resultados no mercado

#### 6.3 Limitações e Cuidados
- **Não é causal**: Não podemos afirmar que formação causa maiores salários
- **Contexto específico**: Resultados válidos para o mercado brasileiro de dados em 2023
- **Fatores omitidos**: Muitas variáveis importantes não foram incluídas

### 7. Correções Implementadas

✅ **Dados reais** em vez de simulados  
✅ **Imputação inteligente** baseada em salário e experiência  
✅ **Codificação dummy** para evitar assumir linearidade  
✅ **Validação cruzada** para estimativas robustas  
✅ **Linguagem adequada** evitando interpretação causal  
✅ **Análise de limitações** e considerações metodológicas  
✅ **Comparação de modelos** para robustez  
✅ **Visualizações informativas** dos resultados  

### 8. Arquivos Corrigidos

- **Código**: `hipotese5_corrigida.py` (implementação completa com correções)
- **Visualizações**: 
  - `analise_exploratoria_corrigida.png`
  - `resultados_hipotese5_corrigida.png`
  - `distribuicao_salarial_corrigida.png`

---

**Versão**: 2.0 (Corrigida)  
**Data**: 11 de junho de 2025  
**Status**: ✅ Problemas críticos corrigidos
## [Preparação dos Dados] Hipótese 3

Inicialmente, para a preparação de dados para a Hipótese foi necessário determinar alguns pontos a respeito de um atributo criado anteriormente 'Salario_Medio'. Como visualizar, quais são seus valores únicos e a quantidade de respostas por valor. Os resultados respectivamente foram: 

Dados únicos: 14000.5,  7000.5,     nan,  5000.5, 10000.5, 22500.5,  1500.5, 3500.5, 18000.5,  2500.5, 27500.5, 35000.5,  1050.5;

| Salario_Medio | Quantidade |
|---------------|-----------:|
| 10000.50      |       1026 |
| 5000.50       |        745 |
| 14000.50      |        650 |
| 7000.50       |        637 |
| 3500.50       |        352 |
| 18000.50      |        328 |
| 2500.50       |        288 |
| 1500.50       |        215 |
| 22500.50      |        195 |
| 27500.50      |        128 |
| 35000.50      |         86 |
| 1050.50       |          1 |

Com isso, foi possível comparar qual linguagem está sendo utilizada nos maiores salários, fazendo uma comparação inicial entre Python x R. Foi plotado assim dois gráficos, um corresponde a média salarial por habilidade, contemplando R, Python ou outra. E, por fim, um gráfico de quantidade de profissionais por salário médio que utilizam as linguagens.


<img src="imagens/media_salarial_por_habilidade.png">

<img src="imagens/quantidade_profissionais_salario_python_r.png">

Podendo levantar algumas conclusões:
1. Há uma baixa adesão das duas linguagens de programação entre os salários médio de 1050,00 a 2500,50 reais;
2. Dessa forma, é possível observar que na medida em que o salário médio vai aumentando, percebe-se que o número de pessoas que trabalham com linguagem de programação é maior, especialmente em faixas como 5000,00 a 7000,50 reais;
3. A linguagem Python é mais comum que R entre as faixas salariais;
4. Há a presença de profisisonais que trabalham com ambas linguagens em todas as faixas, entretanto, não parece ser algo muito comum.

## Indução de modelos

### Modelo 1: Algoritmo


### Resultados obtidos com o modelo 1.

## Modelo para Hipótese 1 - "Dado o PIB e o IDH de uma região/país, um profissional de dados tem maior probabilidade de ter um salário acima ou abaixo de uma determinada faixa salarial para a área?"

### **Modelo:** Árvore de Decisão

### Justificativa:
- **Justificativa: As faixas salariais são definidas por intervalos fixos (R1.001−R1.001−R4.000, R4.001−R4.001−R6.000, etc.), criando relações não-lineares entre variáveis econômicas (PIB, IHD) e o target.
- **Vantagem da Árvore: Modela naturalmente relações não-lineares através de divisões binárias sequenciais, identificando pontos de corte ótimos nos preditores.

### Processo Utilizado para Amostragem de Dados

1. **Pré-processamento Inicial**
A coluna **Nível Salarial**, que é o target, foi dividida em:

| Faixa Salarial | Intervalo de Valores    |
|:--------------:|:-----------------------:|
| Faixa 1        | R$1.001 - R$4.000       |
| Faixa 2        | R$4.001 - R$10.000      |
| Faixa 3        | R$10.001 - R$20.000     |
| Faixa 4        | R$20.001+               |

**Lista de Colunas utilizadas no treino e teste:**
- IDHM
- PIB_2021_OR  
- Faixa_Etaria
- Nivel_de_Ensino
- Nível
- Nivel_Salarial
- Python
- Tempo_de_experiencia_na_area_de_dados
- Todas as 27 colunas Uf (Obs.: Coluna Uf foi subdividida para receber valores binários).
   
| Etapa                     | Descrição                                                                                                                                 | Código Relacionado                                                                 |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| **Pré-processamento Inicial** | Preparação dos dados antes da modelagem, incluindo:<br>- Tratamento de valores faltantes<br>- Codificação de variáveis categóricas<br>- Normalização<br><br> `base_treino` pronta.* | `base_treino.drop(columns=['Nivel_Salarial'])`<br>        |
| **Divisão Treino-Teste**  | Separação dos dados em:<br>- Treino (75%)<br>- Teste (25%)<br><br>Com estratificação implícita e `random_state` para reprodutibilidade.  | `train_test_split(..., test_size=0.25, random_state=42)`                         |
| **Pós-processamento**     | Análise das previsões através de:<br>- Acurácia<br>- Matriz de confusão<br>- Relatório de classificação por faixa salarial               | `accuracy_score()`<br>`confusion_matrix()`<br>`classification_report()`          |
| **Descrição dos Parâmetros** | `DecisionTreeClassifier` configurado com:<br>- `criterion='gini'`: Mede a impureza dos splits<br>- `max_depth=4`: Limita profundidade para evitar overfitting<br>- `random_state=42`: Garante reprodutibilidade | `DecisionTreeClassifier(criterion='gini', max_depth=4, random_state=42)`        |

### Resultado

=== Métricas de Desempenho ===

### Acurácia: 0.62

### Matriz de confusão:

![Sem título](https://github.com/user-attachments/assets/ab46043f-a25b-45d1-9da4-2f6a01bd8680)

![Sem título](https://github.com/user-attachments/assets/fcef2718-2f12-45d6-9bd4-9bd3339da894)

## Análise da Matriz de Confusão

| Métrica               | Classe 1 | Classe 2 | Classe 3 | Classe 4 |
|-----------------------|---------|---------|---------|---------|
| **Acertos**           | 99      | 191     | 281     | 0       |
| **Erros principais**  | 97 → Classe 2 | 40 → Classe 1, 64 → Classe 3 | 97 → Classe 2 | 100% → Classe 3 |
| **Taxa de acerto**    | 48.5%   | 63.7%   | 73.2%   | 0%      |

## Principais Problemas Identificados:

1. **Falha crítica na Classe 4**:
   - 100% dos casos classificados erroneamente como Classe 3
   - Possível causa: Desbalanceamento extremo ou falta de padrões discriminativos

2. **Alta confusão entre Classes 1-2**:
   - 97 casos da Classe 1 classificados como 2
   - 40 casos da Classe 2 classificados como 1
   - Sugere sobreposição de características entre estas classes

3. **Melhor desempenho na Classe 3**:
   - 73.2% de acurácia (melhor entre todas)
   - Ainda apresenta 97 erros classificados como Classe 2

4. **Conclusão**:

- **Limitações do Modelo de Árvore de Decisão**:
  - Desempenho comprometido devido a:
    - **Dados desbalanceados** (natureza não-uniforme das classes)
    - **Sobreposição de características** entre classes
  - Problemas específicos identificados:
    - **Falha crítica na Classe 4**:
      - 100% de erro de classificação
      - Possível causa: sub-representação nos dados de treino
    - **Alta confusão entre Classes 1-2**:
      - Limites de decisão inadequados para separar classes similares
    - **Desempenho mediano na Classe 3**:
      - Acurácia de 73.2% (melhor entre as classes)
      - Ainda com 97 erros significativos
  - Conclusão:
    - Estrutura de decisão binária hierárquica mostrou-se:
      - Pouco eficaz para múltiplas classes
      - Limitada para variáveis altamente interdependentes

	
## Árvore de Decisão: [Hipótese] Quais ferramentas influenciam no salário médio?

### Abordagem Metodológica

Para prever os salários médios dos profissionais de dados, foi construído um modelo de regressão baseado em árvore de decisão. Este modelo inicial foi desenvolvido com o objetivo de identificar os fatores mais relevantes que influenciam os salários na área de dados.

### Conjunto de dados e variáveis

O modelo utilizou as seguintes variáveis como preditoras:
- **Localização geográfica**: UF onde o profissional reside (variável categórica)
- **Conhecimento técnico**: Domínio de linguagens específicas como SQL e Python
- **Perfil de habilidades técnicas**: Uso de linguagens estatísticas para análise de dados, linguagens web, empresariais e de sistema
- **Ausência de habilidades em programação**: Indicador de não utilização de linguagens de programação

A variável alvo foi o `salario_medio`, caracterizando um problema de regressão.

### Processamento e construção do modelo

O pipeline de modelagem incluiu:
1. **Pré-processamento dos dados**:
   - Codificação one-hot para variáveis categóricas (UF)
   - Passagem direta das variáveis numéricas
   
2. **Algoritmo de modelagem**:
   - Árvore de Decisão para Regressão
   - Parâmetro de profundidade máxima = 5 para evitar overfitting

3. **Validação**:
   - Divisão dos dados em conjuntos de treino (80%) e teste (20%)

## Resultados Principais

### Importância das características

Analisando a importância das features no modelo, identificamos os principais fatores que influenciam os salários:

| Feature | Importância |
|---------|------------|
| Não utiliza linguagem de programação | 27.93% |
| Conhecimento em SQL | 18.74% |
| Conhecimento em Python | 17.65% |
| Residência em local não identificado (NI) | 13.31% |
| Residência em São Paulo (SP) | 10.99% |
| Uso de linguagens empresariais | 6.42% |
| Uso de linguagens estatísticas para análise de dados | 1.96% |
| Residência no Distrito Federal (DF) | 1.08% |
| Residência em Pernambuco (PE) | 0.57% |
| Residência na Bahia (BA) | 0.54% |

### Insights preliminares

1. **Impacto negativo da falta de programação**: A característica mais importante foi "não utiliza linguagem de programação", sugerindo que este fator tem forte correlação com os salários (provavelmente negativa)

2. **Relevância das habilidades técnicas**: SQL e Python destacam-se como as linguagens mais valorizadas no mercado, representando juntas cerca de 36% da importância no modelo

3. **Fator geográfico**: A localização geográfica tem peso significativo, com destaque para profissionais em São Paulo

4. **Especialização técnica**: Linguagens empresariais e estatísticas também influenciam os salários, embora com menor impacto que as linguagens principais
