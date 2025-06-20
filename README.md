## Os fatores que influenciam os salários dos profissionais de dados no Brasil.

O projeto desenvolve um sistema inteligente para analisar os fatores que influenciam os salários dos profissionais de dados no Brasil. A solução utiliza técnicas de aprendizado de máquina e análise estatística para processar informações relacionadas ao nível de formação, experiência, porte da empresa, localização geográfica e conhecimento em tecnologias específicas. Com base nesses dados, o sistema identifica padrões e relações entre essas variáveis, permitindo uma avaliação precisa do impacto de cada fator na remuneração dos profissionais.
A aplicação integra múltiplas fontes de dados, realizando a coleta, processamento e modelagem de forma automatizada. O sistema apresenta insights visuais e relatórios interativos, facilitando a compreensão dos resultados por diferentes perfis de usuários. Além disso, ele é projetado para ser escalável e adaptável a novas bases de dados, permitindo atualizações contínuas conforme o mercado de trabalho evolui.

## Integrantes

* Antonio Augusto Vieira Lopes Filho
* Diego Rodrigo Marinho Silva
* Ryan Junio de Oliveira 
* Vinicius Bigonha Cancela Moraes de Melo Filho 

## Professor

Prof. Hugo Bastos de Paula

Prof. Hayala Nepomuceno Curto

## Instruções de utilização

Este projeto implementa modelos de machine learning para classificação salarial com base em características profissionais e demográficas. Abaixo estão as instruções para configurar e executar a aplicação.
Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

    Python 3.8 ou superior

    Gerenciador de pacotes pip

Instalação das Dependências

    Clone o repositório: https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais.git

Crie e ative um ambiente virtual (recomendado):

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

Instale as dependências:

pip install -r requirements.txt

Ou instale manualmente os pacotes necessários:

pip install pandas numpy scikit-learn matplotlib seaborn yellowbrick

Execução do Modelo

    Coloque seu arquivo de dados (state_idh_pib.csv) na pasta /content/ (ou ajuste o caminho no código)

    Execute o script principal: assets/models/MODELOS_ArvoreDecisão_KNN_HIPOTESE 1.ipynb

    O script realizará:

        Pré-processamento dos dados

        Treinamento dos modelos (Árvore de Decisão e KNN)

        Avaliação dos modelos

        Geração de visualizações

Estrutura do Código

O projeto contém os seguintes componentes principais:

    Pré-processamento:

        Tratamento de valores faltantes

        Codificação de variáveis categóricas

        Engenharia de features (agrupamento de salários, experiência, etc.)

    Modelos Implementados:

        Árvore de Decisão

        K-Vizinhos Mais Próximos (KNN)

    Avaliação:

        Métricas de acurácia

        Matrizes de confusão

        Importância das features

        Curvas de aprendizado

    Visualização:

        Gráficos de importância de features

        Árvores de decisão plotadas

        Fronteiras de decisão (para KNN)

Personalização

Para usar com seus próprios dados:

    Substitua state_idh_pib.csv por seu conjunto de dados

    Ajuste os nomes das colunas no código conforme necessário

    Modifique os parâmetros dos modelos na seção de configuração

Saídas Geradas

O script produzirá:

    Relatórios de classificação no console

    Gráficos salvos como imagens PNG

    Análise de exemplos de acertos e erros


## Histórico de versões

* 0.1.1
    * CHANGE: Atualização das documentacoes. Código permaneceu inalterado.
* 0.1.0
    * Indução do primeiro modelo do agente inteligente.
* 0.0.1
    * Trabalhando na preparação dos dados.

