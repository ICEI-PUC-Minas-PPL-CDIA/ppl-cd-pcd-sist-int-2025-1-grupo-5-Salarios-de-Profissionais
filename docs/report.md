# Os fatores que influenciam os salários dos profissionais de dados no Brasil.

# Índice

* [Os fatores que influenciam os salários dos profissionais de dados no Brasil.](#os-fatores-que-influenciam-os-salários-dos-profissionais-de-dados-no-brasil)
    * [INTEGRANTES:](#integrantes)
    * [Professores:](#professores)
    * [Resumo](#resumo)
* [Introdução](#introdução)
* [Contextualização](#contextualização)
* [Problema](#problema)
* [Objetivo geral](#objetivo-geral)
* [Objetivos específicos](#objetivos-específicos)
* [Justificativas](#justificativas)
* [Público alvo](#público-alvo)
    * [Profissionais de Ciência de Dados e Tecnologia](#profissionais-de-ciência-de-dados-e-tecnologia)
    * [Profissionais em Transição de Carreira](#profissionais-em-transição-de-carreira)
    * [Recrutadores e Gestores de RH](#recrutadores-e-gestores-de-rh)
    * [Empresas e Tomadores de Decisão](#empresas-e-tomadores-de-decisão)
* [Análise exploratórida dos dados.](#análise-exploratórida-dos-dados)
    * [State of Data Brazil 2023](#state-of-data-brazil-2023)
    * [Dicionário de Dados](#dicionário-de-dados)
        * [State of Data Brazil 2023](#state-of-data-brazil-2023-1)
            * [Variáveis Gerais](#variáveis-gerais)
            * [Cargos (Binários)](#cargos-binários)
            * [Linguagens de Programação (Binários)](#linguagens-de-programação-binários)
            * [Ferramentas - Nuvem e Armazenamento (Binários)](#ferramentas---nuvem-e-armazenamento-binários)
            * [Ferramentas de BI (Binários)](#ferramentas-de-bi-binários)
    * [Tabela PIB 2021](#tabela-pib-2021)
    * [Tabela IDHM 2021](#tabela-idhm-2021)
* [Descrição de dados 📊](#descrição-de-dados-📊)
    * [State of Data](#state-of-data)
    * [Faixa Salarial](#faixa-salarial)
    * [Salário Médio (Coluna calculada baseada na coluna faixa salarial da tabela original)](#salário-médio-coluna-calculada-baseada-na-coluna-faixa-salarial-da-tabela-original)
    * [Média salárial por UF](#média-salarial-por-uf)
    * [Idade](#idade)
    * [Sexo ou Gênero](#sexo-ou-gênero)
    * [Raça ou Etnia](#raça-ou-etnia)
    * [Nível de Ensino](#nível-de-ensino)
    * [UF](#uf)
    * [Quantidade de profissionais de Dados relacionando Gêneros por Uf](#quantidade-de-profissionais-de-dados-relacionando-gêneros-por-uf)
    * [Distribuição da média salarial por gênero por UF](#distribuição-da-média-salarial-por-gênero-por-uf)
    * [Média salarial por Gênero](#média-salarial-por-gênero)
    * [Média salarial por Cor/Raça/Etnia](#média-salarial-por-corraçaetnia)
    * [Cargo Atual](#cargo-atual)
    * [Média salarial por Cargo na área de Ciência de Dados](#média-salarial-por-cargo-na-área-de-ciência-de-dados)
    * [Média salarial por Ferramenta/Plataforma Utilizada](#média-salarial-por-ferramenta-plataforma-utilizada)
    * [Média salarail por linguagem de programação Utilizada](#média-salarail-por-linguagem-de-programação-utilizada)
    * [Média salarial por setores de Atuação](#média-salarial-por-setores-de-atuação)
    * [Número de funcionários da empresa que trabalha](#número-de-funcionários-da-empresa-que-trabalha)
    * [Nível](#nível)
    * [Média salarial por Nivel de experiência.](#média-salarial-por-nivel-de-experiencia)
    * [Tempo de experiência na área de dados](#tempo-de-experiência-na-área-de-dados)
* [Base Auxiliares](#base-auxiliares)
    * [IDH 2021 por UF](#idh-2021-por-uf)
    * [PIB 2021 por UF](#pib-2021-por-uf)
* [🧪 Preparação dos dados](#🧪-preparação-dos-dados)
    * [1. Seleção dos Atributos para a Hipótese 1:](#1-seleção-dos-atributos-para-a-hipótese-1)
    * [2. Tratamento dos Valores Faltantes ou Omissos (NaN) Hipótese 1:](#2-tratamento-dos-valores-faltantes-ou-omissos-nan-hipótese-1)
        * [Remoção de Linhas](#remoção-de-linhas)
        * [Substituição por Zero](#substituição-por-zero)
    * [3. Tratamento dos Valores Inconsistentes Hipótese 1:](#3-tratamento-dos-valores-inconsistentes-hipótese-1)
        * [Remoção de Categorias Irrelevantes](#remoção-de-categorias-irrelevantes)
        * [Unificação de Categorias](#unificação-de-categorias)
        * [Agrupamento de Categorias Raras](#agrupamento-de-categorias-raras)
    * [4. Conversão de Dados e Engenharia de Atributos Hipótese 1:](#4-conversão-de-dados-e-engenharia-de-atributos-hipótese-1)
        * [Criação da Variável Alvo (`Salario_target`)](#criação-da-variável-alvo-salario_target)
        * [Codificação Ordinal](#codificação-ordinal)
        * [Engenharia de Features de Habilidades](#engenharia-de-features-de-habilidades)
        * [Discretização de Variável Numérica](#discretização-de-variável-numérica)
        * [Conversão para Formato Binário (One-Hot Encoding)](#conversão-para-formato-binário-one-hot-encoding)
    * [Observação dados IDH e PIB](#observação-dados-idh-e-pib)
        * [Produto Interno Bruto (PIB)](#produto-interno-bruto-pib)
        * [Índice de Desenvolvimento Humano (IDH)](#índice-de-desenvolvimento-humano-idh)
    * [1. Seleção dos Atributos para a Hipótese 3:](#1-seleção-dos-atributos-para-a-hipótese-3)
    * [2. Tratamento dos Valores Faltantes ou Omissos (NaN) Hipótese 3:](#2-tratamento-dos-valores-faltantes-ou-omissos-nan-hipótese-3)
    * [Preparação dos dados específica para Hipótese 4:](#preparação-dos-dados-específica-para-hipótese-4)
    * [Tratamento de Valores Ausentes](#tratamento-de-valores-ausentes)
    * [Codificação de Variáveis](#codificação-de-variáveis)
    * [Verificação de Qualidade](#verificação-de-qualidade)
    * [Seleção de Variáveis](#seleção-de-variáveis)
* [Indução de modelos 🧠](#indução-de-modelos-🧠)
    * [Hipótese 1 - É possível prever a faixa salarial de um profissional com base nos indicadores socioeconômicos (PIB e IDH) do estado onde ele trabalha?](#hipótese-1---é-possível-prever-a-faixa-salarial-de-um-profissional-com-base-nos-indicadores-socioeconômicos-pib-e-idh-do-estado-onde-ele-trabalha)
    * [Modelo 1](#modelo-1)
    * [Árvore de Decisão 🌳](#árvore-de-decisão-🌳)
        * [Justificativa da Escolha](#justificativa-da-escolha)
        * [Amostragem e Particionamento dos Dados](#amostragem-e-particionamento-dos-dados)
        * [Parâmetros do Modelo](#parâmetros-do-modelo)
        * [Trecho de Código](#trecho-de-código)
    * [Fluxo de Processamento](#fluxo-de-processamento)
* [Resultado 🎯](#resultado-🎯)
    * [Resultados obtidos com o Modelo 1: Árvore de Decisão](#resultados-obtidos-com-o-modelo-1-árvore-de-decisão)
        * [Matriz de Confusão](#matriz-de-confusão)
        * [Métricas de Performance (Precisão, Revocação e F-Measure)](#métricas-de-performance-precisão-revocação-e-f-measure)
    * [Interpretação do Modelo 1: Árvore de Decisão](#interpretação-do-modelo-1-árvore-de-decisão)
        * [Parâmetros do Modelo Obtido](#parâmetros-do-modelo-obtido)
        * [Regras de "Raciocínio" do Modelo](#regras-de-raciocínio-do-modelo)
        * [Importância das Features](#importância-das-features)
* [Modelo 2](#modelo-2)
* [Hipótese 1 - É possível prever a faixa salarial de um profissional com base nos indicadores socioeconômicos (PIB e IDH) do estado onde ele trabalha?](#hipótese-1---é-possível-prever-a-faixa-salarial-de-um-profissional-com-base-nos-indicadores-socioeconômicos-pib-e-idh-do-estado-onde-ele-trabalha-1)
* [K-Vizinhos Mais Próximos (KNN) ⚙️](#k-vizinhos-mais-próximos-knn-⚙️)
    * [Justificativa da Escolha](#justificativa-da-escolha-1)
    * [Fluxo de Processamento](#fluxo-de-processamento-1)
* [Resultado 🎯](#resultado-🎯-1)
    * [Resultados obtidos com o Modelo 2: K-Vizinhos Mais Próximos (KNN)](#resultados-obtidos-com-o-modelo-2-k-vizinhos-mais-próximos-knn)
        * [Matriz de Confusão](#matriz-de-confusão-1)
        * [Métricas de Performance (Precisão, Revocação e F-Measure)](#métricas-de-performance-precisão-revocação-e-f-measure-1)
    * [Interpretação do Modelo 2: K-Vizinhos Mais Próximos (KNN)](#interpretação-do-modelo-2-k-vizinhos-mais-próximos-knn)
        * [Parâmetros do Modelo Obtido](#parâmetros-do-modelo-obtido-1)
        * [Regras de "Raciocínio" do Modelo](#regras-de-raciocínio-do-modelo-1)
        * [Importância das Features](#importância-das-features-1)
* [Análise Comparativa dos Modelos](#análise-comparativa-dos-modelos)
    * [Hipótese 1](#hipótese-1)
    * [Comparativo de Modelos - Árvore de Decisão vs KNN](#comparativo-de-modelos---árvore-de-decisão-vs-knn)
    * [📊 Acurácia Geral](#📊-acurácia-geral)
    * [🔍 Comparativo por Classe](#🔍-comparativo-por-classe)
        * [Classe 1 (Faixa Inferior)](#classe-1-faixa-inferior)
        * [Classe 2 (Faixa Média)](#classe-2-faixa-média)
        * [Classe 3 (Faixa Superior)](#classe-3-faixa-superior)
    * [⚖️ Overfitting/Generalização](#⚖️-overfittinggeneralização)
    * [🏆 Observações](#🏆-observações)
        * [Similaridade de Performance](#similaridade-de-performance)
        * [Escolha do Modelo](#escolha-do-modelo)
    * [Cenários de Uso: Qual Modelo se Sairia Melhor?](#cenários-de-uso-qual-modelo-se-sairia-melhor)
        * [A Árvore de Decisão seria superior para...](#a-árvore-de-decisão-seria-superior-para)
        * [O KNN seria superior para...](#o-knn-seria-superior-para)
* [Conclusão 💡](#conclusão-💡)
* [Observações Pessoais DIEGO](#observações-pessoais-diego)
    * [Principais Resultados](#principais-resultados)
    * [Vantagens do Sistema](#vantagens-do-sistema)
    * [Limitações](#limitações)
    * [Melhorias Propostas](#melhorias-propostas)
    * [Observações Finais](#observações-finais)
* [Hipótese – Características demográficas e profissionais influenciam a faixa salarial?](#hipótese-–-características-demográficas-e-profissionais-influenciam-a-faixa-salarial)
* [Modelo 1 – XGBoost](#modelo-1-–-xgboost)
    * [Indução do Modelo 1](#indução-do-modelo-1)
    * [Parâmetros utilizados:](#parâmetros-utilizados)
* [Resultado Modelo 1](#resultado-modelo-1)
    * [Acurácia: 78,63% (Teste)](#acurácia-7863-teste)
    * [Acurácia: 85,40% (Treino)](#acurácia-8540-treino)
* [Modelo 2 – Random Forest](#modelo-2-–-random-forest)
    * [Indução do Modelo 2](#indução-do-modelo-2)
    * [Parâmetros utilizados:](#parâmetros-utilizados-1)
* [Resultado Modelo 2](#resultado-modelo-2)
    * [Acurácia: 74,54% (Teste)](#acurácia-7454-teste)
    * [Acurácia: 85,22% (Treino)](#acurácia-8522-treino)
* [Análise comparativa dos modelos](#análise-comparativa-dos-modelos)
    * [Forças e Fragilidades](#forças-e-fragilidades)
    * [Exemplos de uso ideal:](#exemplos-de-uso-ideal)
* [Hipótese 3 (Modelo)](#hipótese-3)
   * [Resumo dos Dados](#resumo-dos-dados)
   * [Modelo](#modelo)
     * [Divisão dos Dados](#divisao-dos-dados)
     * [Balanceamento dos Dados](#balanceamento-dos-dados)
     * [Modelo de Classificação](#modelo-de-classificacao)
* [Resultados do Modelo](#resultados-do-modelo)
* [Relatório de Classificação](#relatorio-de-classificacao)
* [Insights Principais](#insights-principais)
   * [Distribuição Salarial](#distribuicao-salarial)
   * [Linguagens Mais Impactantes no Salário](#linguagens-mais-impactantes-no-salario)
* [Interpretação dos Resultados](#interpretacao-dos-resultados)
* [Implicações para o Mercado](#implicacoes-para-o-mercado)
* [Conclusão](#conclusão)
    * [Implicações para o Mercado](#implicações-para-o-mercado)
    * [Próximos Passos Recomendados](#próximos-passos-recomendados)
    * [Perguntas Frequentes](#perguntas-frequentes)
* [REFERÊNCIAS](#referências)
* [APÊNDICES](#apêndices)

# Os fatores que influenciam os salários dos profissionais de dados no Brasil.

## INTEGRANTES:

Antonio Augusto Vieira Lopes Filho, aavlfilho@sga.pucminas.br

Diego Rodrigo Marinho Silva, diego.marinho@sga.pucminas.br

Ryan Junio de Oliveira, ryan.junio@sga.pucminas.br

Vinicius Bigonha Cancela Moraes de Melo Filho, vbcmmfilho@sga.pucminas.br  

---

Professores:

Prof. Hugo Bastos de Paula

Prof. Hayala Nepomuceno Curto

---

_Curso de Ciência de Dados, Unidade Praça da Liberdade_

_Instituto de Informática e Ciências Exatas – Pontifícia Universidade de Minas Gerais (PUC MINAS), Belo Horizonte – MG – Brasil_

---

**Resumo**. Este projeto propõe o desenvolvimento de um sistema inteligente para analisar como fatores como nível de formação, experiência profissional, porte da empresa, região de residência e domínio de tecnologias específicas influenciam os salários dos profissionais de dados no Brasil. Utilizando técnicas de aprendizado de máquina e análise estatística, o sistema processará dados de diversas fontes para identificar padrões e correlações entre essas variáveis e a remuneração. O objetivo é fornecer insights precisos que auxiliem profissionais e empresas a entenderem melhor os fatores que impactam os salários no setor de dados, contribuindo para decisões estratégicas de carreira e gestão de talentos. 

---


## Introdução

O mercado de dados no Brasil está em constante expansão, e diversos fatores influenciam a remuneração dos profissionais da área. Aspectos como nível de formação, experiência profissional, porte da empresa, localização geográfica e domínio de determinadas tecnologias podem impactar significativamente os salários. Compreender essas variáveis é essencial tanto para profissionais que buscam crescimento na carreira quanto para empresas que desejam atrair e reter talentos. Neste contexto, este projeto propõe o desenvolvimento de um sistema inteligente capaz de analisar e identificar padrões salariais no setor de dados, auxiliando na tomada de decisões estratégicas.

##    Contextualização

Nos últimos anos, a área de ciência de dados tem se consolidado como um dos segmentos mais promissores do mercado de trabalho, impulsionada pelo crescimento da transformação digital e pelo uso intensivo de dados nas tomadas de decisão empresariais. Com essa expansão, há um aumento na demanda por profissionais qualificados, o que torna relevante a análise dos fatores que influenciam a remuneração desses especialistas.
Nesse contexto, este projeto se insere na interseção entre inteligência artificial, análise de dados e mercado de trabalho, buscando compreender como diferentes características dos profissionais de dados impactam seus salários no Brasil. Para isso, o estudo utiliza um sistema inteligente capaz de processar grandes volumes de informações e identificar padrões relacionados a variáveis como nível de formação, experiência profissional, porte da empresa, localização geográfica e domínio de tecnologias específicas. Essa abordagem possibilita uma análise mais precisa e baseada em evidências sobre os determinantes salariais no setor.

##    Problema

O problema central deste projeto é entender quais características dos profissionais de dados no Brasil afetam de forma mais significativa seus salários. Essa questão é relevante tanto para trabalhadores que buscam otimizar suas trajetórias profissionais quanto para empresas que desejam estabelecer políticas salariais mais competitivas. O contexto da aplicação envolve o mercado de tecnologia e ciência de dados, abrangendo profissionais de diferentes perfis, desde iniciantes até especialistas, que atuam em empresas de diversos portes e segmentos. O estudo se baseia em dados reais, extraídos de fontes como o State of Data - BR 2023, para analisar padrões e tendências salariais no setor. 

##    Objetivo geral

Desenvolver um sistema inteligente para analisar o impacto de fatores como nível de formação, experiência profissional, porte da empresa, localização geográfica e conhecimento em tecnologias nos salários dos profissionais de dados no Brasil, utilizando dados extraídos do State of Data - BR 2023 e outras fontes complementares. 

##    Objetivos específicos

Analisar a relação entre nível de formação, experiência profissional e porte da empresa com a remuneração dos profissionais de dados no Brasil, utilizando técnicas de aprendizado de máquina e análise estatística.

Investigar o impacto da localização geográfica e do domínio de determinadas tecnologias no salário dos profissionais, identificando possíveis desigualdades regionais e valorização de habilidades específicas no mercado.

Desenvolver modelos preditivos capazes de estimar faixas salariais com base nos atributos dos profissionais, fornecendo insights para tomada de decisão sobre carreira e políticas salariais.

Implementar visualizações interativas e relatórios analíticos para facilitar a interpretação dos padrões identificados, tornando os resultados acessíveis para diferentes perfis de usuários.


##    Justificativas

A crescente demanda por profissionais de ciência de dados no Brasil, aliada às variações salariais influenciadas por múltiplos fatores, torna essencial a compreensão dos elementos que impactam a remuneração desses especialistas. Segundo o artigo "Carreira em Dados: conheça as principais áreas e como ingressar" (Alura, 2023), aspectos como nível de formação, experiência, porte da empresa, localização geográfica e domínio de tecnologias exercem influência direta sobre as oportunidades e os ganhos no setor. No entanto, ainda há uma lacuna na identificação quantitativa e preditiva desses fatores, dificultando a tomada de decisão tanto para profissionais que buscam progressão na carreira quanto para empresas que desejam formular políticas salariais competitivas.
Diante desse cenário, este projeto se justifica pela necessidade de um sistema inteligente capaz de analisar e prever os impactos desses fatores nos salários dos profissionais de dados no Brasil. Ao utilizar dados extraídos do State of Data - BR 2023 e outras fontes complementares, o sistema busca gerar insights estratégicos baseados em evidências, permitindo um entendimento mais profundo da valorização profissional no setor. Além disso, a implementação de modelos preditivos e visualizações interativas possibilita a democratização da informação, fornecendo subsídios para que profissionais façam escolhas informadas sobre suas carreiras e empresas ajustem suas políticas de remuneração de forma mais eficiente e equitativa.



##   Público alvo

A aplicação será utilizada por diferentes perfis de usuários que buscam compreender os fatores que influenciam os salários no setor de ciência de dados no Brasil. Esses usuários podem ter níveis variados de conhecimento sobre tecnologia e estatística, mas todos compartilham o interesse em tomar decisões informadas com base em dados. A seguir, são descritos os principais perfis de usuários:

**Profissionais de Ciência de Dados e Tecnologia**
**Perfil:** Engenheiros de dados, cientistas de dados, analistas de dados e desenvolvedores que desejam entender melhor o impacto de fatores como experiência, formação acadêmica e habilidades tecnológicas em seus salários. 
**Conhecimento prévio:** Alto conhecimento técnico em programação, estatística e machine learning. Familiaridade com análise de dados e interpretação de gráficos interativos. 
**Relação com a tecnologia:** Usuários experientes, que podem usar os resultados do sistema para planejar sua progressão de carreira e negociar salários.

**Profissionais em Transição de Carreira**
**Perfil:** Pessoas migrando para a área de dados, vindas de setores como engenharia, administração, marketing e finanças. 
**Conhecimento prévio:** Nível intermediário a básico em ciência de dados e estatística. Interesse em entender quais habilidades e qualificações são mais valorizadas no mercado. 
**Relação com a tecnologia:** Familiarizados com ferramentas básicas de análise de dados, mas podem necessitar de suporte na interpretação dos resultados. 

**Recrutadores e Gestores de RH**
**Perfil:** Profissionais de Recursos Humanos e gestores que contratam e definem políticas salariais para equipes de dados. 
**Conhecimento prévio:** Baixo conhecimento técnico sobre ciência de dados, mas familiaridade com tendências de mercado e estruturação de cargos e salários. 
**Relação com a tecnologia:** Usam a aplicação para comparar remunerações, identificar padrões e embasar decisões estratégicas de contratação. 

**Empresas e Tomadores de Decisão**
**Perfil:** Diretores e líderes de empresas de tecnologia e dados que desejam entender melhor a dinâmica salarial do setor para definir estratégias de retenção e contratação. 
**Conhecimento prévio:** Alto conhecimento sobre negócios e gestão, mas limitado em análise de dados e machine learning. 
**Relação com a tecnologia:** Buscam relatórios e insights claros para embasar decisões estratégicas. 

## Análise exploratórida dos dados.

**State of Data Brazil 2023**
A base de dados State of Data Brazil 2023 é rica em informações sobre profissionais no setor de dados no Brasil, abordando tanto características demográficas quanto aspectos profissionais e de experiência no mercado de trabalho.
 
## Dicionário de Dados

State of Data Brazil 2023

Variáveis Gerais

| Variável                          | Descrição                                                  | Tipo de Dado                              |
|-----------------------------------|------------------------------------------------------------|-------------------------------------------|
| Salario Médio                     | Média da faixa salarial mensal                             | Quantitativo - Contínuo                   |
| Nível                             | Nível de carreira (experiência, autonomia, responsabilidades) | Qualitativo - Ordinal                 |
| Número de Funcionários da Empresa | Faixa do número de funcionários da empresa                 | Qualitativo - Ordinal                     |
| Situação Atual de Trabalho        | Tipo de vínculo empregatício                               | Qualitativo - Nominal (Multivariado)      |
| Área de Formação                  | Área acadêmica do profissional                             | Qualitativo - Nominal (Multivariado)      |
| Estado de Origem                  | Estado originário do profissional                          | Qualitativo - Nominal (Multivariado)      |
| Mudou de Estado                   | Se mudou de estado                                         | Qualitativo - Nominal (Binário)           |
| PCD (Pessoa Com Deficiência)      | Se possui alguma deficiência                               | Qualitativo - Nominal (Binário)           |
| Estado onde Mora                  | Estado de residência atual                                 | Qualitativo - Nominal (Multivariado)      |
| UF onde Mora                      | Unidade Federativa da residência atual                     | Qualitativo - Nominal (Multivariado)      |
| Região onde Mora                  | Região do Brasil onde reside                               | Qualitativo - Nominal (Multivariado)      |
| Idade                             | Idade em anos                                              | Quantitativo - Discreto                   |
| Faixa de Idade                    | Faixa etária (ex: 22-24, 30-34)                            | Qualitativo - Ordinal                     |
| Gênero                            | Gênero (Masculino, Feminino, etc.)                         | Qualitativo - Nominal (Binário)           |
| Etnia/Cor/Raça                    | Etnia, cor ou raça do profissional                         | Qualitativo - Nominal (Multivalorado)     |
| Nível de Ensino                   | Nível de escolaridade                                      | Qualitativo - Ordinal                     |
| Faixa Salarial Mensal             | Intervalo de renda mensal                                  | Qualitativo - Ordinal                     |
| Experiência Profissional em Dados | Tempo de experiência em dados                              | Qualitativo - Ordinal                     |
| Cargo Atual                       | Cargo ocupado atualmente                                   | Qualitativo - Nominal (Multivariado)      |
| Tamanho da Empresa                | Porte da empresa                                           | Qualitativo - Ordinal                     |
| Modelo de Trabalho                | Regime de trabalho                                         | Qualitativo - Nominal (Multivariado)      |
| Setor da Empresa                  | Setor de atuação da empresa                                | Qualitativo - Nominal (Multivariado)      |

Cargos (Binários)

| Variável                          | Descrição | Tipo de Dado                        |
|-----------------------------------|-----------|-------------------------------------|
| Analytics_Engineer                | Cargo     | Qualitativo - Nominal (Binário)     |
| Data_Engineer                     | Cargo     | Qualitativo - Nominal (Binário)     |
| Data_Analyst                      | Cargo     | Qualitativo - Nominal (Binário)     |
| Data_Scientist                    | Cargo     | Qualitativo - Nominal (Binário)     |
| Database_Administrator            | Cargo     | Qualitativo - Nominal (Binário)     |
| Analista_de_Bussiness_Intelligence| Cargo     | Qualitativo - Nominal (Binário)     |
| Data_Architect                    | Cargo     | Qualitativo - Nominal (Binário)     |
| Data_Product_Manager              | Cargo     | Qualitativo - Nominal (Binário)     |
| Business_Analyst                  | Cargo     | Qualitativo - Nominal (Binário)     |

Linguagens de Programação (Binários)

| Variável                        | Tipo de Dado                        |
|---------------------------------|-------------------------------------|
| SQL                             | Qualitativo - Nominal (Binário)     |
| R                               | Qualitativo - Nominal (Binário)     |
| Python                          | Qualitativo - Nominal (Binário)     |
| C/C++/C#                        | Qualitativo - Nominal (Binário)     |
| .NET                            | Qualitativo - Nominal (Binário)     |
| Java                            | Qualitativo - Nominal (Binário)     |
| Julia                           | Qualitativo - Nominal (Binário)     |
| SAS                             | Qualitativo - Nominal (Binário)     |
| Visual Basic                    | Qualitativo - Nominal (Binário)     |
| Scala                           | Qualitativo - Nominal (Binário)     |
| MATLAB                          | Qualitativo - Nominal (Binário)     |
| Rust                            | Qualitativo - Nominal (Binário)     |
| PHP                             | Qualitativo - Nominal (Binário)     |
| JavaScript                      | Qualitativo - Nominal (Binário)     |
| Não utilizo nenhuma linguagem   | Qualitativo - Nominal (Binário)     |

Ferramentas - Nuvem e Armazenamento (Binários)

| Variável                | Tipo de Dado                        |
|-------------------------|-------------------------------------|
| Azure (Microsoft)       | Qualitativo - Nominal (Binário)     |
| Amazon Web Services     | Qualitativo - Nominal (Binário)     |
| Google Cloud (GCP)      | Qualitativo - Nominal (Binário)     |
| Oracle Cloud            | Qualitativo - Nominal (Binário)     |
| IBM                     | Qualitativo - Nominal (Binário)     |
| Servidores On Premise   | Qualitativo - Nominal (Binário)     |
| Cloud própria           | Qualitativo - Nominal (Binário)     |

Ferramentas de BI (Binários)

| Variável                              | Tipo de Dado                        |
|---------------------------------------|-------------------------------------|
| Microsoft Power BI                    | Qualitativo - Nominal (Binário)     |
| Qlik View/Qlik Sense                  | Qualitativo - Nominal (Binário)     |
| Tableau                               | Qualitativo - Nominal (Binário)     |
| Metabase                              | Qualitativo - Nominal (Binário)     |
| Superset                              | Qualitativo - Nominal (Binário)     |
| Redash                                | Qualitativo - Nominal (Binário)     |
| Looker                                | Qualitativo - Nominal (Binário)     |
| Looker Studio (Google Data Studio)    | Qualitativo - Nominal (Binário)     |
| Amazon Quicksight                     | Qualitativo - Nominal (Binário)     |
| Mode                                  | Qualitativo - Nominal (Binário)     |
| Alteryx                               | Qualitativo - Nominal (Binário)     |
| MicroStrategy                         | Qualitativo - Nominal (Binário)     |
| IBM Analytics/Cognos                  | Qualitativo - Nominal (Binário)     |
| SAP Business Objects/SAP Analytics     | Qualitativo - Nominal (Binário)     |
| Oracle Business Intelligence           | Qualitativo - Nominal (Binário)     |
| Salesforce/Einstein Analytics          | Qualitativo - Nominal (Binário)     |
| Birst                                 | Qualitativo - Nominal (Binário)     |
| SAS Visual Analytics                   | Qualitativo - Nominal (Binário)     |
| Grafana                               | Qualitativo - Nominal (Binário)     |
| TIBCO Spotfire                        | Qualitativo - Nominal (Binário)     |
| Pentaho                               | Qualitativo - Nominal (Binário)     |
| Fazemos todas as análises em planilhas | Qualitativo - Nominal (Binário)     |
| Não utilizo nenhuma ferramenta de BI   | Qualitativo - Nominal (Binário)     |

Para enriquecer a análise e testar a hipótese sobre a influência de indicadores socioeconômicos nos salários, o estudo foi complementado com as seguintes fontes de dados externas, ambas referentes ao ano de 2021.

Tabela PIB 2021

| Variável          | Tipo de Dado                | Descrição                                                         |
|-------------------|----------------------------|-------------------------------------------------------------------|
| UF                | Qualitativo - Nominal       | Sigla da Unidade da Federação (estados e Distrito Federal)        |
| PIB_2021_OR       | Quantitativo - Contínuo     | Valor do Produto Interno Bruto em 2021 (milhões de reais)         |
| Partic_Pib_Brasil | Quantitativo - Contínuo     | Participação percentual do estado no PIB nacional (0 a 1)         |

Tabela IDHM 2021

| Variável      | Tipo de Dado                | Descrição                                                         |
|---------------|----------------------------|-------------------------------------------------------------------|
| Ano           | Quantitativo - Discreto     | Ano de referência dos dados                                       |
| Uf            | Qualitativo - Nominal       | Sigla da Unidade da Federação                                     |
| Nome_Estado   | Qualitativo - Nominal       | Nome completo do estado brasileiro ou DF                          |
| IDHM          | Quantitativo - Contínuo     | Índice de Desenvolvimento Humano Municipal (0 a 1)                |
| IDHM_L        | Quantitativo - Contínuo     | Dimensão Longevidade do IDHM (0 a 1)                              |
| IDHM_E        | Quantitativo - Contínuo     | Dimensão Educação do IDHM (0 a 1)                                 |
| IDHM_R        | Quantitativo - Contínuo     | Dimensão Renda do IDHM (0 a 1)                                    |
| IDHMAD        | Quantitativo - Contínuo     | IDHM Ajustado à Desigualdade (0 a 1)                              |
| IDHMAD_L      | Quantitativo - Contínuo     | Dimensão Longevidade do IDHMAD (0 a 1)                            |
| IDHMAD_E      | Quantitativo - Contínuo     | Dimensão Educação do IDHMAD (0 a 1)                               |
| IDHMAD_R      | Quantitativo - Contínuo     | Dimensão Renda do IDHMAD (0 a 1)                                  |
| RDPC          | Quantitativo - Contínuo     | Renda Domiciliar per Capita (em R$)                               |
| GINI          | Quantitativo - Contínuo     | Índice de Gini (medida de desigualdade, 0 a 1)                    |
| THEIL         | Quantitativo - Contínuo     | Índice de Theil (medida de desigualdade, ≥ 0)                     |


##    Descrição de dados :bar_chart:

### State of Data

A base de dados **State of Data Brazil 2023** retrata o perfil dos profissionais de dados no Brasil, abordando aspectos como formação acadêmica, experiência profissional, faixa salarial, ferramentas utilizadas e desafios enfrentados no setor.

### Faixa Salarial

![Faixa_salarial](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/results/Distribui%C3%A7%C3%A3o%20Faixa%20Salarial.png)

### Salário Médio (Coluna calculada baseada na coluna faixa salarial da tabela original)
#### Obs.: Para fins de visualização, a Coluna salário médio foi criada.

- **Número de observações não nulas**: 4.651  
- **Média**: R$ 10.028,67  
- **Desvio padrão**: R$ 6.969,22  
- **Valor mínimo**: R$ 1.050,50  
- **Primeiro quartil (25%)**: R$ 5.000,50  
- **Mediana (50%)**: R$ 10.000,50  
- **Terceiro quartil (75%)**: R$ 14.000,50  
- **Valor máximo**: R$ 35.000,50
  
![Distribuição media salarial](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/results/Distribui%C3%A7%C3%A3o%20cont%C3%ADnua%20dos%20sal%C3%A1rios.png)
![Boxplot](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/results/Distribui%C3%A7%C3%A3o%20dos%20sal%C3%A1rios%20boxplot.png)

### Média salárial por UF

![Média salárial por UF](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/results/M%C3%A9dia%20salarial%20por%20UF.png)

 ### Idade
- **Número de observações não nulas**: 5.293  
- **Média**: 32,0 anos  
- **Desvio padrão**: 7,62  
- **Valor mínimo**: 18 anos  
- **Primeiro quartil (25%)**: 27 anos  
- **Mediana (50%)**: 30 anos  
- **Terceiro quartil (75%)**: 36 anos  
- **Valor máximo**: 73 anos
  
![Idade](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/results/HISTOGRAMA%20FAIXA%20DE%20IDADE.png)

### Sexo ou Gênero
- **Masculino**: 75,1% (3.975 respostas)  
- **Feminino**: 24,4% (1.293 respostas)  
- **Prefiro não informar**: 0,3% (16 respostas)  
- **Outros**: 0,2% (9 respostas)
  
![Sexo ou Gênero](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/results/Distribui%C3%A7%C3%A3o%20por%20Genero.png)

### Raça ou Etnia
- **Branca**: 64,5% (3.414 respostas)  
- **Parda**: 24,2% (1.281 respostas)  
- **Preta**: 7,3% (387 respostas)  
- **Prefiro não informar**: 0,6% (34 respostas)  
- **Outra**: 0,3% (18 respostas)
  
![Raça ou Etnia](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/results/Distribui%C3%A7%C3%A3o%20Racial%20Etnica%20dos%20Profissionais%20de%20Dados.png)

### Nível de Ensino
- **Doutorado ou PhD**: 34,3% (1.818 respostas)  
- **Graduação/Bacharelado**: 34,0% (1.798 respostas)  
- **Estudante de Graduação**: 12,8% (678 respostas)  
- **Pós-graduação**: 12,8% (676 respostas)  
- **Mestrado**: 4,0% (210 respostas)  
- **Não tenho graduação formal**: 2,0% (105 respostas)  
- **Prefiro não informar**: 0,2% (8 respostas)

![Nível de Ensino](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/results/Distribui%C3%A7%C3%A3o%20por%20n%C3%ADvel%20de%20ensino.png)

### UF
- **Indica os estados brasileiros onde os profissionais de dados estão localizados**.
  
![UF](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/results/Distribui%C3%A7%C3%A3o%20Geografica%20dos%20profissionais%20de%20Dados%20por%20UF.png)

### Quantidade de profissionais de Dados relacionando Gêneros por Uf

![Quantidade gerno uf](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/results/Quantidade%20de%20profissionais%20de%20dados%20por%20g%C3%AAnero%20em%20cada%20UF.png)

### Distribuição da média salarial por gênero por UF

![Distribuição da média salarial por gênero por UF](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/results/M%C3%A9dia%20salarial%20por%20g%C3%AAnero%20em%20cada%20UF.png)

### Média salarial por Gênero 

![Média salarial por Gênero](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/results/Compara%C3%A7%C3%A3o%20Salarial%20entre%20g%C3%AAneros.png)

### Média salarial por Cor/Raça/Etnia

![Média salarial por Cor/Raça/Etnia](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/results/Sal%C3%A1rio%20m%C3%A9dia%20por%20ra%C3%A7a%20etnia.png)

### Cargo Atual
- **Informa os cargos que os profissionais de dados ocupam**.
  
![Cargo Atual](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/results/Distribui%C3%A7%C3%A3o%20de%20Cargos%20na%20Area%20de%20dados.png)

### Média salarial por Cargo na área de Ciência de Dados

![Média salarial por Cargo na área de Ciência de Dados](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/results/M%C3%A9dia%20salarial%20por%20cargo%20em%20ciencia%20de%20dados.png)

### Média salarial por Ferramenta/Plataforma Utilizada

![Média salarial por Ferramenta/Plataforma Utilizada](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/results/M%C3%A9dia%20salarial%20por%20ferramenta%20plataforma%20utilizada.png)

### Média salarail por linguagem de programação Utilizada

![Média salarail por linguagem de programação Utilizada](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/results/M%C3%A9dia%20salarial%20por%20linguagem%20de%20programa%C3%A7%C3%A3o%20utilizada.png)

### Média salarial por setores de Atuação

![Média salarial por setores de Atuação](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/results/M%C3%A9dia%20salarial%20por%20setor%20de%20atua%C3%A7%C3%A3o.png)


### Número de funcionários da empresa que trabalha
- **Demonstra o número de funcionários da empresa onde o profissional de dados atua**.
  
![Número de funcionários da empresa que trabalha](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/results/Distribui%C3%A7%C3%A3o%20do%20tamanho%20das%20empresas.png)

### Nível
- **Mostra os níveis de experiência dos profissionais de dados (Júnior, Pleno, Sênior)**.
  
![Nível](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/results/Distribui%C3%A7%C3%A3o%20por%20n%C3%ADvel%20de%20experiencia.png)

### Média salarial por Nivel de experiência.

![Média salarial por Nivel de experiência](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/results/M%C3%A9dia%20salarial%20por%20N%C3%ADvel%20de%20experiencia.png)

### Tempo de experiência na área de dados
- **Apresenta o tempo de experiência dos profissionais agrupado por faixas**.
  
![Tempo de experiência na área de dados](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/results/Distribui%C3%A7%C3%A3o%20de%20tempo%20de%20experi%C3%AAncia%20em%20dados.png)


## Base Auxiliares

### IDH 2021 por UF
- **O grafico mostra o Indice de Desenvolvimento Humano dividido por Estado**.
  
![IDH 2021](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/results/IDH%20por%20Unidade%20Federativa.png)

- **Número de observações não nulas: 27** 
- **Média: 0.730148**
- **Desvio padrão: 0.039892**
- **Valor mínimo: 0.676000** 	
- **Primeiro quartil (25% dos dados estão abaixo deste valor):0.698500**
- **Mediana (segundo quartil, 50% dos dados estão abaixo): 0.728000**
- **Terceiro quartil (75% dos dados estão abaixo deste valor): 0.765500**
- **Valor máximo: R$ 0.814000**
      

### PIB 2021 por UF

![PIB 2021](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/results/Distribui%C3%A7%C3%A3o%20do%20PIB%20por%20estado.png)

- **Número de observações não nulas: 27** 
- **Média: 333.783.100.000,00**
- **Desvio padrão: 535.633.300.000,00**
- **Valor mínimo: 18.203.000.000,00**
- **Primeiro quartil (25% dos dados estão abaixo deste valor): 70.147.000.000,00**
- **Mediana (segundo quartil, 50% dos dados estão abaixo): 186.337.000.000,00**
- **Terceiro quartil (75% dos dados estão abaixo deste valor): 319.781.000.000,00**
- **Valor máximo: R$ 2.719.751.000.000,00**

# 🧪 Preparação dos dados

Considerando que o problema central deste projeto é entender quais características dos profissionais de dados no Brasil afetam de forma mais significativa seus salários, foram levantados algumas hipóteses que serão trabalhadas nesse projeto.

**Hipótese 1:** É possível prever a faixa salarial de um profissional com base nos indicadores socioeconômicos (PIB e IDH) do estado onde ele trabalha?

**Hipótese 2:** O setor de atuação e o tamanho da empresa (Número de funcionários) influenciam o salário? Com setores como finanças e grandes empresas oferecendo melhores remunerações?

**Hipótese 3:** A diversidade de linguagens de programação utilizadas e o domínio de tecnologias específicas como cloud e ferramentas de BI estão associados a salários mais altos?

**Hipótese 4:** Nível de formação acadêmica: Profissionais com pós-graduação, mestrado ou doutorado tendem a receber salários mais altos do que aqueles com apenas graduação?


A etapa de preparação dos dados foi fundamental para garantir a qualidade e a adequação das informações para a modelagem. O processo envolveu a limpeza, transformação e engenharia de novos atributos a partir do dataset *State of Data Brazil 2023*, *IDH 2021* e *PIB 2021*, com o objetivo de criar uma base de treino robusta para os algoritmos de classificação (*Árvore de Decisão* e *k-NN*). A preparação consistiu nos seguintes passos:

### 1. Seleção dos Atributos para a **Hipótese 1:**

Após um processo de limpeza e engenharia de features, foram selecionados os seguintes atributos para compor a base de dados final utilizada no treinamento dos modelos. A variável `Salario_target` foi definida como a variável alvo (target).

* **`IDHM`**: Índice de Desenvolvimento Humano Municipal do estado.
* **`PIB_2021_OR`**: Produto Interno Bruto do estado em 2021.
* **`Nível_1.0`, `Nível_2.0`, `Nível_3.0`**: Representação binária (One-Hot Encoding) do nível profissional (Júnior, Pleno, Sênior).
* **`Nivel_de_Ensino`**: Nível de escolaridade codificado numericamente de forma ordinal.
* **`Grupo_Ferramentas_Ordinal`**: Categoria ordinal que representa a quantidade de ferramentas de BI/Dados que o profissional utiliza (engenharia de features).
* **`Grupo_Linguagens_Ordinal`**: Categoria ordinal que representa a quantidade de linguagens de programação que o profissional utiliza (engenharia de features).
* **`Nivel_Experiencia_Ordinal`**: Nível de experiência na área de dados, codificado numericamente de forma ordinal.
* **`Microsoft PowerBI`**: Atributo binário indicando se o profissional utiliza (1) ou não (0) esta ferramenta.
* **`Salario_target` (Alvo)**: Faixa salarial do profissional, discretizada em três categorias ordinais (1: Baixo, 2: Médio, 3: Alto).

### 2. Tratamento dos Valores Faltantes ou Omissos (NaN) **Hipótese 1:**

O tratamento de valores ausentes foi realizado de duas maneiras principais:

### Remoção de Linhas
Para garantir a qualidade e a integridade da análise, as linhas que continham valores nulos na coluna alvo inicial (`Faixa_Salarial`) e na coluna de identificação geográfica (`Uf`) foram completamente removidas do dataset, pois eram essenciais para a modelagem. Este procedimento resultou na exclusão de um número reduzido de registros. Considerando o volume total de dados, a remoção representou uma fração mínima do conjunto, assegurando que a base de dados final mantivesse sua robustez e representatividade estatística sem prejuízo significativo para a análise.

### Substituição por Zero
Para as colunas binárias que representam o uso de tecnologias específicas (como `Python`, `SQL`, `Azure (Microsoft)`, `Google Cloud (GCP)` e `Microsoft PowerBI`), os valores `NaN` foram substituídos por `0`, para evitar perda de dados. A premissa adotada foi que a ausência de resposta nestes campos indicava a não utilização da respectiva tecnologia pelo profissional.

### 3. Tratamento dos Valores Inconsistentes **Hipótese 1:**

Para garantir a consistência e a relevância dos dados, foram aplicados os seguintes tratamentos:

### Remoção de Categorias Irrelevantes
* Na variável `Faixa_Salarial`, a categoria "de R$ 101/mês a R$ 2.000/mês" foi removida para focar em faixas salariais mais representativas do mercado de dados.
* No atributo `Nivel_de_Ensino`, as respostas "Não tenho graduação formal" e "Prefiro não informar" foram excluídas por não agregarem valor à análise ordinal de escolaridade.

### Unificação de Categorias
No atributo `Tempo_de_experiencia_na_area_de_dados`, a categoria "de 5 a 6 anos" foi unificada com "de 4 a 6 anos" para resolver sobreposições e padronizar as faixas de experiência.

### Agrupamento de Categorias Raras
Para o atributo `Setor`, as categorias com frequência inferior a 100 ocorrências foram agrupadas em uma única classe chamada "Outros_Setores". Esta técnica reduz a dimensionalidade e evita que os modelos sejam influenciados por categorias com pouca representatividade.

### 4. Conversão de Dados e Engenharia de Atributos **Hipótese 1:**

A transformação dos dados foi a etapa mais extensa, envolvendo a conversão de tipos e a criação de novos atributos (engenharia de features):

### Criação da Variável Alvo (`Salario_target`)
* As categorias textuais da `Faixa_Salarial` foram convertidas em um valor numérico contínuo (`Salario_medio`), utilizando o ponto médio de cada faixa.
* Em seguida, a coluna `Salario_medio` foi discretizada em três categorias ordinais (`1`, `2`, `3`) de igual frequência, utilizando a função `pd.qcut` (tercis). O resultado foi a variável alvo final, `Salario_target`.

### Codificação Ordinal
Atributos categóricos com uma ordem lógica intrínseca foram convertidos para valores numéricos sequenciais:
* `Nivel_de_Ensino`: Mapeado para uma escala de 1 (Estudante) a 4 (Mestrado/Doutorado).
* `Tempo_de_experiencia_na_area_de_dados`: Convertido para `Nivel_Experiencia_Ordinal` em uma escala de 1 (Iniciante) a 4 (Especialista).

### Engenharia de Features de Habilidades
* Foram criadas as colunas `total_linguagens` e `total_ferramentas`, que somam a quantidade de linguegens e ferramentas, respectivamente, que cada profissional declarou usar.
* Essas contagens foram então agrupadas em categorias textuais (`Grupo_Linguagens` e `Grupo_Ferramentas`), como "Nenhuma", "1", "2", "3 ou mais".
* Finalmente, essas novas categorias foram codificadas ordinalmente (`Grupo_Linguagens_Ordinal` e `Grupo_Ferramentas_Ordinal`).

### Discretização de Variável Numérica
* A coluna contínua `Idade` foi transformada em um atributo categórico ordinal (`Idade_Quartil`) com quatro grupos de tamanhos similares, utilizando `pd.qcut`.

### Conversão para Formato Binário (One-Hot Encoding)
* O atributo nominal `Nível` (Júnior, Pleno, Sênior) foi transformado em três colunas binárias (`Nível_1.0`, `Nível_2.0`, `Nível_3.0`), permitindo que o modelo trate cada nível como uma característica independente.
* O mesmo processo foi aplicado à coluna `Setor_Agrupado`, gerando múltiplas colunas binárias (`Setor_Tecnologia`, `Setor_Finanças ou Bancos`, etc.).

### Observação dados IDH e PIB 

Para enriquecer a análise e testar a hipótese sobre a influência de indicadores socioeconômicos nos salários, o estudo foi complementado com as seguintes fontes de dados externas, ambas referentes ao ano de 2021. Os dados referentes a Pib e IDH foram unidos a base de daos principal atravez da Coluna UF.

### Produto Interno Bruto (PIB)
- **Fonte**: [Contas Regionais de 2021 - IBGE](https://www.ibge.gov.br/estatisticas/economicas/contas-nacionais/9054-contas-regionais-do-brasil.html?edicao=38346).
- **Metodologia**: Foram utilizados os valores do PIB calculados pela **ótica da renda**, que considera remunerações, rendimentos e impostos.
- **Justificativa do Ano**: O uso de dados de 2021 foi necessário por serem os mais recentes disponíveis, visto que o IBGE está realizando a [atualização do ano-base do Sistema de Contas Nacionais](https://www.ibge.gov.br/novo-portal-destaques/37997-divulgacao-do-informativo-das-contas-nacionais-anuais.html), o que impactou o cronograma de novas divulgações.

### Índice de Desenvolvimento Humano (IDH)
- **Fonte**: [IPEA DATA](http://www.ipeadata.gov.br/Default.aspx).
- **Justificativa do Ano**: Utilizou-se a base de 2021 por ser a mais recente com dados consolidados por estado disponíveis na plataforma no momento da coleta.

### 1. Seleção dos Atributos para a **Hipótese 3:**

Uma vez que a hipótese 3 tem como objetivo verificar se a diversidade de ferramentas influencia positivamente no salário, foi necessário selecionar para nosso dataframe somente os atributos que continha as ferramentas. Tendo como variável alvo a Faixa Salarial.

```Python
colunas_codigo = ['P2_h', 'P4_d_1', 'P4_d_2', 'P4_d_3', 'P4_d_4', 'P4_d_5', 
                 'P4_d_6', 'P4_d_7', 'P4_d_8', 'P4_d_9', 'P4_d_10', 'P4_d_11', 
                 'P4_d_12', 'P4_d_13', 'P4_d_14', 'P4_d_15']

# Procurar strings que contêm os códigos desejados
colunas_selecionadas = []
for codigo in colunas_codigo:
    colunas_correspondentes = [col for col in df.columns if codigo in col]
    if colunas_correspondentes:
        colunas_selecionadas.extend(colunas_correspondentes)

# Criar o DataFrame com as colunas selecionadas
df_atributos_selecionados = df[colunas_selecionadas]

df_atributos_selecionados.columns
```

Por fim, foi realizado uma renomeação dos atributos para serem melhores trabalhados.
### 2. Tratamento dos Valores Faltantes ou Omissos (NaN) **Hipótese 3:**

O tratamento dos valores ausentes foi orientado pela análise da variável alvo. Observou-se que, para todos os casos em que 'faixa_salarial' apresentava valores NaN, não havia um '1' em nenhum dos atributos correspondentes às ferramentas. Consequentemente, esses dados não eram úteis para a análise e foram descartados do dataframe.

```Python
nulos_df = df_novo[df_novo['faixa_salarial'].isnull()]
print(nulos_df.describe())
```

|       |   sql |   scala |   matlab |   rust |   php |   javascript |   nao_utiliza_linguagem |     r |   python |   c_cpp_csharp |   dotnet |   java |   julia |   sas_stata |   vb_vba |
|-------|-------|---------|----------|--------|-------|--------------|-------------------------|-------|----------|---------------|---------|-------|--------|------------|---------|
| count | 540.0 |   540.0 |    540.0 |  540.0 | 540.0 |        540.0 |                   540.0 | 540.0 |    540.0 |         540.0 |   540.0 | 540.0 |  540.0 |      540.0 |   540.0 |
| mean  |   0.0 |     0.0 |      0.0 |    0.0 |   0.0 |          0.0 |                     0.0 |   0.0 |      0.0 |           0.0 |     0.0 |   0.0 |    0.0 |        0.0 |     0.0 |
| std   |   0.0 |     0.0 |      0.0 |    0.0 |   0.0 |          0.0 |                     0.0 |   0.0 |      0.0 |           0.0 |     0.0 |   0.0 |    0.0 |        0.0 |     0.0 |
| min   |   0.0 |     0.0 |      0.0 |    0.0 |   0.0 |          0.0 |                     0.0 |   0.0 |      0.0 |           0.0 |     0.0 |   0.0 |    0.0 |        0.0 |     0.0 |
| 25%   |   0.0 |     0.0 |      0.0 |    0.0 |   0.0 |          0.0 |                     0.0 |   0.0 |      0.0 |           0.0 |     0.0 |   0.0 |    0.0 |        0.0 |     0.0 |
| 50%   |   0.0 |     0.0 |      0.0 |    0.0 |   0.0 |          0.0 |                     0.0 |   0.0 |      0.0 |           0.0 |     0.0 |   0.0 |    0.0 |        0.0 |     0.0 |
| 75%   |   0.0 |     0.0 |      0.0 |    0.0 |   0.0 |          0.0 |                     0.0 |   0.0 |      0.0 |           0.0 |     0.0 |   0.0 |    0.0 |        0.0 |     0.0 |
| max   |   0.0 |     0.0 |      0.0 |    0.0 |   0.0 |          0.0 |                     0.0 |   0.0 |      0.0 |           0.0 |     0.0 |   0.0 |    0.0 |        0.0 |     0.0 |

```Python
# Remover linhas onde 'faixa_salarial' é nula
df_novo = df_novo.dropna(subset=['faixa_salarial'])
```
Com essa análise, verificamos a quantidade de valores nulos ou ausentes no dataframe e constatamos que não havia nenhum valor faltante em todos os atributos. No entanto, houve a perda de 540 registros no total.

## Preparação dos dados específica para **Hipótese 4:**
##  Tratamento de Valores Ausentes 

**Problema anterior:**  
Imputação inadequada usando apenas a moda

**Solução implementada:**  
Imputação inteligente baseada em salário e experiência:
- Lógica: Profissionais com salários e experiência similares tendem a ter formação similar
- Método:  
  - Para experiência: KNN Imputer com k=5 vizinhos mais próximos

## Codificação de Variáveis 

**Problema anterior:**  
Codificação ordinal forçando linearidade (1,2,3,4)

**Solução implementada:**  
Codificação dummy (one-hot encoding):
- Vantagem: Permite relações não-lineares entre níveis de formação
- Referência: Graduação (categoria omitida)

##  Verificação de Qualidade

- **Multicolinearidade:** VIF < 5 para todas as variáveis
- **Normalização:** Variáveis numéricas padronizadas (média=0, desvio=1)
- **Validação cruzada:** K-fold (k=5) para estimativas robustas

## Seleção de Variáveis

**Variável dependente:**  
- `Salario_Medio` (em R$)

**Variáveis independentes principais:**  
- `Nivel_de_Ensino` (Graduação, Pós-graduação, Mestrado, Doutorado)  
- `Tempo_de_experiencia_na_area_de_dados` (em anos)

**Variáveis de controle:**  
- `Setor` (categoria da empresa)  
- `PIB_2021_OR` (PIB do estado, normalizado)  
- `IDHM` (Índice de Desenvolvimento Humano Municipal, normalizado)

# Indução de modelos 🧠

## Hipótese 1 - É possível prever a faixa salarial de um profissional com base nos indicadores socioeconômicos (PIB e IDH) do estado onde ele trabalha?

---
# Modelo 1
---

## Árvore de Decisão 🌳  

### Justificativa da Escolha  

A Árvore de Decisão foi selecionada por três motivos principais:  

- **Interpretabilidade**: O modelo gera um conjunto de regras visuais que são fáceis de entender, permitindo extrair insights diretos sobre como o modelo toma suas decisões para classificar os salários.  
- **Importância de Atributos**: O algoritmo calcula nativamente a importância de cada variável (`feature_importance_`), o que ajuda a identificar quais características são mais determinantes para prever a faixa salarial.  
- **Flexibilidade**: Lida bem com relações não-lineares entre as variáveis e não exige que os dados de entrada sejam escalonados (normalizados).  

### Amostragem e Particionamento dos Dados  

Foi utilizado o método de particionamento simples (*Hold-Out*). O conjunto de dados foi dividido da seguinte forma, utilizando `random_state=42` para garantir a reprodutibilidade:  

- **75%** para o conjunto de **Treinamento**.  
- **25%** para o conjunto de **Teste**.  

### Parâmetros do Modelo  

O modelo (`DecisionTreeClassifier`) foi configurado com os seguintes hiperparâmetros:  

- `criterion='gini'`: Métrica utilizada para medir a qualidade de uma divisão, buscando criar os nós mais puros possíveis a cada ramificação da árvore.  
- `max_depth=5`: Define a profundidade máxima da árvore. Este parâmetro foi usado para controlar a complexidade e evitar que o modelo se ajustasse demais aos dados de treino (*overfitting*).  

Trecho de Código

```python
# Importação das bibliotecas necessárias
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# 1. Particionamento dos dados em treino (75%) e teste (25%)
X_treino, X_teste, y_treino, y_teste = train_test_split(
    base_treino.drop(columns=['Salario_target']), 
    base_treino['Salario_target'], 
    test_size=0.25, 
    random_state=42
)

# 2. Instanciação do modelo com os parâmetros definidos
modelo_arvore = DecisionTreeClassifier(criterion='gini', max_depth=5, random_state=42)

# 3. Treinamento do modelo utilizando os dados de treino
modelo_arvore.fit(X_treino, y_treino)

```

## Fluxo de Processamento

O processo para treinar e avaliar o modelo de Árvore de Decisão seguiu um fluxo linear com as seguintes etapas:

1. **Seleção de Dados**:  
   O processo inicia com o dataset `base_treino`, já limpo e com as _features_ selecionadas.

2. **Separação de Variáveis**:  
   O dataset é dividido em:
   - `X` (matriz de _features_)
   - `y` (vetor alvo, `Salario_target`)

3. **Particionamento (Hold-Out)**:  
   Os conjuntos `X` e `y` são divididos em:
   - **75%** para treinamento
   - **25%** para teste

4. **Instanciação e Treinamento**:  
   O modelo `DecisionTreeClassifier` é:
   - Instanciado com os parâmetros definidos (`max_depth=5`, `criterion='gini'`)
   - Treinado com os dados de treinamento (`X_treino`, `y_treino`)

5. **Predição e Avaliação**:  
   O modelo treinado é utilizado para:
   - Fazer previsões no conjunto de teste (`X_teste`)
   - Comparar resultados com os valores reais (`y_teste`) para calcular métricas de performance (ex: acurácia)

![Arvore de decisão](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/docs/imagens/Arvore%20de%20Decis%C3%A3o%20Classifica%C3%A7%C3%A3o%20salarial.png)

# Resultado 🎯

### Resultados obtidos com o Modelo 1: Árvore de Decisão

O modelo de Árvore de Decisão foi treinado e avaliado utilizando uma partição de 75% dos dados para treino e 25% para teste. As métricas de performance foram calculadas sobre o conjunto de teste, que o modelo nunca havia visto antes.

O modelo alcançou uma acurácia de **0.69 no treino e 0.67 no teste**. Para uma análise mais detalhada, os seguintes resultados foram gerados:

#### Matriz de Confusão
A matriz de confusão abaixo ilustra a performance do modelo para cada classe. A diagonal principal (em vermelho mais escuro) mostra a quantidade de previsões corretas para cada faixa salarial (1: Baixo, 2: Médio, 3: Alto). As outras células indicam onde ocorreram os erros de classificação.

![Matriz de Confusão Árvore de Decisão](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/docs/imagens/MATRIZ%20DE%20CONFUS%C3%83O%20ARVORE%20ULTIMA.png)

#### Métricas de Performance (Precisão, Revocação e F-Measure)
O relatório de classificação detalha a performance do modelo para cada classe individualmente:

- **Precisão (Precision):** Das vezes que o modelo previu uma classe, quantas ele acertou?  
- **Revocação (Recall):** De todos os exemplos de uma classe, quantos o modelo conseguiu encontrar?  
- **F1-Score:** Média harmônica entre precisão e revocação, oferecendo um balanço entre as duas.    

```python
Relatório de Classificação:
              precision    recall  f1-score   support

           1       0.77      0.71      0.74       384
           2       0.58      0.56      0.57       433
           3       0.66      0.76      0.71       325

    accuracy                           0.67      1142
   macro avg       0.67      0.68      0.67      1142
weighted avg       0.67      0.67      0.67      1142
````

| ✅ EXEMPLO DE SUCESSO         | ❌ EXEMPLO DE FALHA          |
|-------------------------------|-------------------------------|
| **Métrica** \| **Valor**      | **Métrica** \| **Valor**      |
| IDHM \| 0.806                 | IDHM \| 0.806                 |
| PIB_2021_OR \| 2719751.000    | PIB_2021_OR \| 2719751.000    |
| Nível_1.0 \| 0.000            | Nível_1.0 \| 0.000            |
| Nível_2.0 \| 0.000            | Nível_2.0 \| 1.000            |
| Nível_3.0 \| 1.000            | Nível_3.0 \| 0.000            |
| Nivel_de_Ensino \| 3.000      | Nivel_de_Ensino \| 3.000      |
| Grupo_Ferramentas_Ordinal \| 4.000 | Grupo_Ferramentas_Ordinal \| 4.000 |
| Grupo_Linguagens_Ordinal \| 3.000 | Grupo_Linguagens_Ordinal \| 2.000 |
| Nivel_Experiencia_Ordinal \| 3.000 | Nivel_Experiencia_Ordinal \| 3.000 |
| Microsoft PowerBI \| 1.000    | Microsoft PowerBI \| 1.000    |
| Nivel_Salarial_Real \| 2.000  | Nivel_Salarial_Real \| 1.000  |
| Nivel_Salarial_Previsto \| 2.000 | Nivel_Salarial_Previsto \| 2.000 |

### Interpretação do Modelo 1: Árvore de Decisão

#### Parâmetros do Modelo Obtido
O modelo foi construído com os seguintes hiperparâmetros para controlar sua complexidade:
- `criterion='gini'`: Métrica usada para medir a qualidade das divisões nos nós.  
- `max_depth=5`: Profundidade máxima da árvore, limitada a 5 níveis para evitar superajuste.  

#### Regras de "Raciocínio" do Modelo
A grande vantagem da Árvore de Decisão é que seu processo de "raciocínio" é totalmente transparente. As regras de decisão podem ser visualizadas diretamente na estrutura da árvore abaixo. Cada nó representa uma pergunta sobre uma variável (ex: "O `Nivel_Experiencia_Ordinal` é menor ou igual a 2.5?"), e cada ramo representa a resposta ("sim" ou "não"), guiando até uma classificação final em uma das folhas.


#### Importância das Features
O modelo nos permite ver quais atributos foram mais influentes para a tomada de decisão. A importância é medida pela capacidade de cada feature em reduzir a impureza (critério Gini) nos nós da árvore. Conforme o gráfico abaixo, as variáveis mais decisivas para prever a faixa salarial foram:

![Feature Importance arvore de decisão](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/docs/imagens/FEATURE%20IMPORTANTE%20ARVORE%20ULTIMA.png)


---
# Modelo 2 
---
## Hipótese 1 - É possível prever a faixa salarial de um profissional com base nos indicadores socioeconômicos (PIB e IDH) do estado onde ele trabalha?
## K-Vizinhos Mais Próximos (KNN) ⚙️

### Justificativa da Escolha

O KNN foi escolhido como um segundo modelo para comparação por suas características distintas:

- **Simplicidade**: É um algoritmo conceitualmente simples, servindo como um excelente modelo de baseline para avaliar a performance de outros algoritmos mais complexos.
- **Não-paramétrico**: O modelo não faz suposições sobre a distribuição dos dados, o que o torna flexível a diferentes tipos de distribuições.
- **Análise de Similaridade**: Por ser baseado em distância, é eficaz em encontrar padrões locais, classificando um novo dado com base na "vizinhança" mais similar a ele nos dados de treino.

Uma etapa crucial para o KNN foi a padronização dos dados com o StandardScaler, garantindo que todas as variáveis tivessem a mesma escala e contribuíssem de forma equilibrada para o cálculo das distâncias.
Amostragem e Particionamento dos Dados

Para este modelo, também foi utilizado o método Hold-Out, mas com uma divisão diferente para testar outra abordagem:

- **80%** para o conjunto de Treinamento.
- **20%** para o conjunto de Teste.

O random_state=42 foi mantido. Adicionalmente, na análise da performance do modelo, foi empregada a Validação Cruzada (Cross-Validation) com 5 partições (cv=5) na geração das curvas de aprendizado, para uma avaliação mais robusta.
Parâmetros do Modelo

O modelo (KNeighborsClassifier) foi configurado com o seguinte hiperparâmetro:

- n_neighbors=20: Define que o modelo irá consultar os 20 vizinhos mais próximos de um novo dado para decidir a qual classe ele pertence, com base na classe majoritária entre esses vizinhos.

Trecho de Código

```python
# Importação das bibliotecas necessárias
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# 1. Particionamento dos dados em treino (80%) e teste (20%)
X_train, X_test, y_train, y_test = train_test_split(
    base_treino.drop('Salario_target', axis=1), 
    base_treino['Salario_target'], 
    test_size=0.2, 
    random_state=42
)

# 2. Padronização (scaling) dos dados, essencial para o KNN
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. Instanciação do modelo com o parâmetro definido
knn = KNeighborsClassifier(n_neighbors=20)

# 4. Treinamento do modelo utilizando os dados de treino já padronizados
knn.fit(X_train_scaled, y_train)
```

## Fluxo de Processamento

O fluxo para o modelo KNN incluiu uma etapa de pré-processamento adicional, crucial para algoritmos baseados em distância:

1. **Seleção de Dados**:  
   O processo inicia com o mesmo dataset `base_treino`.
2. **Separação de Variáveis**:  
   O dataset é dividido em:
   - `X` (_features_)
   - `y` (alvo)
3. **Particionamento (Hold-Out)**:  
   Os dados são divididos em:
   - **80%** para treinamento
   - **20%** para teste
4. **Padronização (Scaling)**:  
   - O `StandardScaler` é ajustado apenas com os dados de treinamento (`X_train`)
   - Usado para transformar tanto o conjunto de treino quanto o de teste  
   *Garante que todas as features tenham a mesma escala, sem vazamento de informação do conjunto de teste*
5. **Instanciação e Treinamento**:  
   - Modelo `KNeighborsClassifier` (`n_neighbors=20`) é treinado
   - Utiliza dados de treinamento já padronizados (`X_train_scaled`, `y_train`)
6. **Predição e Avaliação**:  
   - Modelo faz previsões no conjunto de teste padronizado (`X_test_scaled`)
   - Resultados são avaliados em comparação com valores reais (`y_test`)

![Froteira de decisão do modelo knn](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/docs/imagens/Fronteiras%20de%20Decis%C3%A3o%20do%20Modelo%20KNN%20(k%3D20).png)


# Resultado 🎯

## Resultados obtidos com o Modelo 2: K-Vizinhos Mais Próximos (KNN)

O modelo KNN foi treinado com 80% dos dados e avaliado nos 20% restantes. Uma etapa crucial de pré-processamento foi a padronização (*scaling*) dos dados, garantindo que todas as features tivessem a mesma escala de valor.

A acurácia obtida pelo modelo no conjunto de teste foi de ** 0.71 no treino e 0.67 no teste**.

#### Matriz de Confusão
A matriz abaixo demonstra a performance do KNN. Assim como no modelo anterior, a diagonal principal representa os acertos.

![Matriz de Confusão KNN](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/docs/imagens/MATRIZ%20DE%20CONFUS%C3%83O%20KNN%20ULTIMA.png)

#### Métricas de Performance (Precisão, Revocação e F-Measure)
O relatório de classificação para o KNN é apresentado abaixo.


```python
Relatório de Classificação:
              precision    recall  f1-score   support

           1       0.78      0.72      0.75       310
           2       0.58      0.58      0.58       348
           3       0.66      0.72      0.69       255

    accuracy                           0.67       913
   macro avg       0.67      0.67      0.67       913
weighted avg       0.67      0.67      0.67       913

```
| ✅ EXEMPLO DE SUCESSO         | ❌ EXEMPLO DE FALHA          |
|-------------------------------|-------------------------------|
| **Métrica** \| **Valor**      | **Métrica** \| **Valor**      |
| IDHM \| 0.806                 | IDHM \| 0.806                 |
| PIB_2021_OR \| 2719751.000    | PIB_2021_OR \| 2719751.000    |
| Nível_1.0 \| 0.000            | Nível_1.0 \| 0.000            |
| Nível_2.0 \| 0.000            | Nível_2.0 \| 1.000            |
| Nível_3.0 \| 1.000            | Nível_3.0 \| 0.000            |
| Nivel_de_Ensino \| 3.000      | Nivel_de_Ensino \| 3.000      |
| Grupo_Ferramentas_Ordinal \| 4.000 | Grupo_Ferramentas_Ordinal \| 4.000 |
| Grupo_Linguagens_Ordinal \| 3.000 | Grupo_Linguagens_Ordinal \| 2.000 |
| Nivel_Experiencia_Ordinal \| 3.000 | Nivel_Experiencia_Ordinal \| 3.000 |
| Microsoft PowerBI \| 1.000    | Microsoft PowerBI \| 1.000    |
| Nivel_Salarial_Real \| 2.000  | Nivel_Salarial_Real \| 1.000  |
| Nivel_Salarial_Previsto \| 2.000 | Nivel_Salarial_Previsto \| 2.000 |

### Interpretação do Modelo 2: K-Vizinhos Mais Próximos (KNN)

#### Parâmetros do Modelo Obtido
O principal hiperparâmetro que define o comportamento do modelo é:
- `n_neighbors=20`: Indica que, para classificar um novo profissional, o algoritmo irá se basear na classe majoritária entre os seus 20 vizinhos mais próximos no conjunto de treino.

#### Regras de "Raciocínio" do Modelo
Diferente da Árvore de Decisão, o KNN é um algoritmo não-paramétrico e não gera um conjunto de regras explícitas. Seu "raciocínio" é baseado em similaridade por distância. Para classificar um novo profissional, o modelo:
1. Calcula a "distância" (similaridade) entre este novo ponto e todos os outros pontos no conjunto de treino.  
2. Identifica os 20 vizinhos mais próximos.  
3. Realiza uma "votação" e atribui a faixa salarial que for majoritária entre esses vizinhos.  

O diagrama de **Fronteiras de Decisão** é a melhor forma de visualizar o resultado desse processo de votação, mostrando os "territórios" que o modelo definiu para cada classe.

![Fronteiras de Decisão do KNN](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/docs/imagens/Fronteiras%20de%20Decis%C3%A3o%20do%20Modelo%20KNN%20(k%3D20).png)

#### Importância das Features
O KNN não possui um método direto para calcular a importância das features. Por isso, foi utilizada a técnica de **Permutation Importance**. Este método mede a importância de uma variável ao calcular o quanto a performance do modelo cai quando os valores dessa variável são embaralhados aleatoriamente. Uma queda maior na acurácia significa que o modelo depende mais daquela feature. As variáveis mais importantes segundo esta técnica foram...

![Permutation Importance KNN](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/docs/imagens/FEATURE%20IMPORTANTE%20KNN%20ULTIMA.png)
 
---
# Análise Comparativa dos Modelos

## Hipótese 1

### Comparativo de Modelos - Árvore de Decisão vs KNN

### 📊 Acurácia Geral

| Modelo            | Acurácia de Treino | Acurácia de Teste | Diferença |
|-------------------|-------------------|------------------|-----------|
| Árvore de Decisão | 0.69              | 0.67             | 0.02      |
| KNN               | 0.6738            | 0.6635           | 0.0103    |

> **Observação**: Ambos os modelos apresentam acurácias muito semelhantes, com a Árvore de Decisão tendo ligeira vantagem no treino.

### 🔍 Comparativo por Classe

### Classe 1 (Faixa Inferior)
- **KNN tem vantagem**:  
  ✅ Melhor em Precisão, Recall e F1-Score

### Classe 2 (Faixa Média)
- **Ponto fraco de ambos**:  
  ⚠️ Métricas mais baixas (dificuldade inerente aos dados)

### Classe 3 (Faixa Superior)
- **Árvore tem vantagem**:  
  📈 Recall 0.76 (vs 0.72 do KNN)  
  F1-Score 0.71 (vs 0.69 do KNN)

### ⚖️ Overfitting/Generalização

| Modelo            | Diferença Treino-Teste | Conclusão                     |
|-------------------|-----------------------|-------------------------------|
| Árvore de Decisão | 2%                    | Boa generalização             |
| KNN               | ~1%                   | Generalização excelente       |

> Ambos mostram capacidade adequada de generalização, com KNN ligeiramente mais estável.

### 🏆 Observações

### Similaridade de Performance
- Performance global muito similar nos dois modelos
- Nenhum "vencedor" claro pelas métricas globais

### Escolha do Modelo
| Critério                | Modelo Recomendado       |
|-------------------------|--------------------------|
| Interpretabilidade       | Árvore de Decisão 🌳     |
| Simplicidade/Robustez   | KNN ⚙️                  |

**Fatores decisivos**:
- Para RH/explicabilidade: Árvore de Decisão
- Para implementação simples: KNN

## Cenários de Uso: Qual Modelo se Sairia Melhor?

Imaginando cenários práticos, podemos extrapolar onde cada modelo brilharia:

### A Árvore de Decisão seria superior para...

1. **Uma Ferramenta de Análise para o RH:**  
   Imagine um painel onde um gestor de RH quer entender os principais fatores que influenciam os salários na empresa para criar um plano de cargos e salários mais justo. As regras claras da árvore (ex: "Doutorado é um forte indicador de salário alto, mas apenas se combinado com mais de 7 anos de experiência") seriam perfeitas para gerar insights acionáveis.

2. **Um Simulador de Salário em um Site de Carreiras:**  
   Um sistema que precisa dar uma estimativa salarial instantânea para milhares de usuários por dia. A velocidade de predição da árvore seria essencial para garantir uma boa experiência do usuário.

### O KNN seria superior para...

1. **Identificar Perfis de "Unicórnio":**  
   Suponha que existam pequenos grupos de profissionais com combinações muito atípicas de habilidades que resultam em salários altíssimos (ex: pouca experiência formal, mas domínio de tecnologias de nicho como Julia e Rust em um setor financeiro). A fronteira de decisão flexível do KNN seria mais apta a identificar esses "bolsões" de alta renda que as regras gerais de uma árvore poderiam ignorar.

2. **Uma Análise Exploratória Rápida:**  
   Se o objetivo fosse apenas ter uma primeira estimativa (baseline) da dificuldade do problema de classificação sem se aprofundar em regras, o KNN seria um ótimo ponto de partida pela sua simplicidade de implementação.
 
---

# Conclusão 💡

---

# Observações Pessoais DIEGO

Este trabalho desenvolveu um sistema inteligente para analisar os fatores que influenciam os salários dos profissionais de dados no Brasil. Utilizando técnicas de aprendizado de máquina e análise estatística, o sistema processou dados como:


- Escolaridade
- Experiência
- Porte da empresa
- Localização
- Conhecimentos técnicos
- Indicadores socioeconômicos (IDH e PIB dos estados brasileiros)

A solução automatizou a coleta, o tratamento e a modelagem dos dados, apresentando os resultados por meio de relatórios interativos e visualizações para facilitar a interpretação.


## Principais Resultados


O sistema identificou que:


- **Experiência profissional**
- **Domínio de tecnologias em alta demanda**

São os principais determinantes da remuneração na área de dados.


## Vantagens do Sistema


✔ **Tomada de decisão informada**  

Auxilia profissionais na negociação salarial e empresas na definição de faixas competitivas.

✔ **Transparência de mercado**  

Torna as práticas salariais do setor mais claras.

✔ **Escalabilidade**  

Pode incorporar novos dados para se manter atualizado.


## Limitações


✖ **Viés dos dados**  

A qualidade da análise depende da representatividade dos dados, podendo reforçar distorções existentes.

✖ **Simplificação da realidade**  

Fatores subjetivos (como soft skills e cultura organizacional) podem não ser totalmente capturados.

## Melhorias Propostas

1. **Ampliação das fontes de dados**

   Incluir informações de plataformas como LinkedIn, portais de emprego e pesquisas salariais.

2. **Inclusão de novas variáveis**  

   Incorporar fatores como:

   - Certificações
   - Idiomas
   - Soft skills

3. **Ferramenta de predição personalizada**  

   Desenvolver um sistema interativo para estimativa salarial baseada nos dados do usuário.

4. **Análise temporal**

   Implementar monitoramento da evolução salarial e demanda por tecnologias.

## Observações Finais

O sistema oferece insights valiosos, mas sua eficácia depende:

- Da qualidade dos dados
- Da consideração de aspectos não quantificáveis

Embora o modelo atual tenha limitações, as melhorias propostas podem aumentar sua precisão e utilidade para profissionais e empresas do setor.


---

# Hipótese  – Características demográficas e profissionais influenciam a faixa salarial?

A hipótese deste trabalho é que características demográficas e profissionais dos indivíduos (como idade, forma de trabalho, cargo atual, entre outras) influenciam significativamente a faixa salarial a que pertencem. Parte-se do pressuposto de que, ao treinar modelos supervisionados, será possível prever com acurácia satisfatória a categoria salarial de um indivíduo com base nesses atributos.

---

# Modelo 1 – XGBoost

O modelo XGBoost é um algoritmo de aprendizado de máquina baseado em árvores de decisão otimizadas por boosting. Utiliza aprendizado sequencial, onde cada nova árvore tenta corrigir os erros das anteriores.

## Indução do Modelo 1

- Dados foram divididos em 80% treino e 20% teste.
- Foi utilizada **validação cruzada com 3 folds**.
- Hiperparâmetros ajustados via `GridSearchCV`.

### Parâmetros utilizados:
- `learning_rate`: 0.1  
- `max_depth`: 5  
- `n_estimators`: 100  
- `subsample`: 1.0  
- `eval_metric`: mlogloss  
- `random_state`: 42  

---

## Resultado Modelo 1

### Acurácia: **78,63%** (Teste)
| Classe | Precisão | Revocação | F1-Score | Suporte |
| ------ | -------- | --------- | -------- | ------- |
| Alta   | 0.78     | 0.67      | 0.72     | 259     |
| Média  | 0.78     | 0.90      | 0.84     | 559     |
| Baixa  | 0.87     | 0.47      | 0.61     | 113     |


### Acurácia: **85,40%** (Treino)
| Classe | Precisão | Revocação | F1-Score | Suporte |
| ------ | -------- | --------- | -------- | ------- |
| Alta   | 0.84     | 0.79      | 0.81     | 1128    |
| Média  | 0.85     | 0.92      | 0.88     | 2201    |
| Baixa  | 0.96     | 0.67      | 0.79     | 391     |


- O modelo obteve ótimo desempenho nas faixas "Alta" e "Média", mas enfrentou **dificuldade na previsão da faixa "Baixa"**, reflexo do desbalanceamento de dados.

![Matriz de Confusão XGBoost](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/results/Matriz%20de%20Confus%C3%A3o%20(XGBoost).png)

![Importância das Variáveis XGBoost](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/results/Import%C3%A2ncia%20das%20Vari%C3%A1veis%20(XGBoost).png)

---

# Modelo 2 – Random Forest

Random Forest é um algoritmo baseado em múltiplas árvores de decisão treinadas em subconjuntos aleatórios dos dados e dos atributos, combinando os resultados por votação.

## Indução do Modelo 2

- Usou-se a **mesma divisão (80/20)**
- O uso de SMOTE ajudou, mas não resolveu completamente a sensibilidade à classe minoritária.
- Hiperparâmetros foram definidos manualmente.
- Não houve validação cruzada.

### Parâmetros utilizados:
- `random_state`: 42  
- `max_depth`: 7  
- `n_estimators`: 100
- `max_features`: 0.5
- `min_samples_leaf`: 5
- `class_weight`: 'balanced'

---

## Resultado Modelo 2

### Acurácia: **74,54%** (Teste)

| Classe | Precisão | Revocação | F1-Score | Suporte |
| ------ | -------- | --------- | -------- | ------- |
| Alta   | 0.65     | 0.82      | 0.72     | 259     |
| Média  | 0.83     | 0.74      | 0.78     | 559     |
| Baixa  | 0.65     | 0.62      | 0.64     | 113     |

### Acurácia: **85,22%** (Treino)

| Classe | Precisão | Revocação | F1-Score | Suporte |
| ------ | -------- | --------- | -------- | ------- |
| Alta   | 0.80     | 0.92      | 0.85     | 2201    |
| Média  | 0.84     | 0.71      | 0.77     | 2201    |
| Baixa  | 0.93     | 0.93      | 0.93     | 2201    |


- Apresentou desempenho geral **ligeiramente inferior ao XGBoost**, mas **melhorou marginalmente a precisão da classe "Baixa"**.
- A revocação da classe "Baixa", contudo, foi ainda menor, o que indica que poucos dos casos verdadeiramente pertencentes a essa classe foram reconhecidos como tal.

![Matriz de Confusão RF](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/results/Matriz%20de%20Confus%C3%A3o%20(Random%20Forest).png)

![Importância das Variáveis RF](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/results/Import%C3%A2ncia%20das%20Vari%C3%A1veis%20(Random%20Forest).png)

---

# Análise comparativa dos modelos

| Critério                   | XGBoost     | Random Forest |
|----------------------------|-------------|----------------|
| Acurácia                   | 78,63%      | 74,54%         |
| Precisão (Classe Baixa)   | 0.87        | 0.65           |
| Revocação (Classe Baixa)  | 0.47        | 0.62          |
| Interpretação              | Moderada    | Alta           |
| Velocidade de Treinamento | Média       | Alta           |
| Robustez ao Ruído         | Alta        | Alta           |

### Forças e Fragilidades

- **XGBoost**: Melhor performance, especialmente em dados desbalanceados; porém, menos interpretável.
- **Random Forest**: Maior explicabilidade e rapidez; ligeiramente menos eficaz em acurácia e revocação.

### Exemplos de uso ideal:
- **XGBoost**: Análise de crédito, detecção de fraude, aplicações com muitos dados.
- **Random Forest**: Ambientes que exigem explicabilidade, como RH, saúde e decisões operacionais.

---

### Conclusão

Os testes realizados confirmam a hipótese de que dados demográficos e profissionais influenciam a faixa salarial. Ambos os modelos alcançaram desempenho satisfatório, com o XGBoost ligeiramente superior em termos de acurácia geral.

Contudo, a dificuldade persistente de ambos os modelos em prever a faixa "Baixa" de forma eficaz mostra a necessidade de:
- Estratégias adicionais de balanceamento,
- Avaliação de outros algoritmos (como LightGBM, CatBoost, Redes Neurais),
- Análise mais profunda da distribuição e qualidade dos dados.

No contexto prático, a escolha entre XGBoost e Random Forest dependerá do equilíbrio entre performance e interpretabilidade exigido pela aplicação.

---

## Hipótese 3

Como dito anteriormente, a hipótese 3 tinha como objetivo analisar quais ferramentas, sobretudo linguagens de programação, tem influência direta ou indireta no salário do profissional de dados.

### Resumo dos Dados

Analisou dados provenientes da pesquisa que captura informações sobre os profissionais. Os dados incluem:

- Informações sobre faixas salariais dos profissionais
- Linguagens de programação utilizadas (SQL, Python, R, C/C++/C#, .NET, Java, Julia, SAS/Stata, VB/VBA, Scala, Matlab, Rust, PHP, JavaScript)
- Aproximadamente 5.000 registros de profissionais (baseado na soma das faixas salariais)

### Modelo

**Divisão dos Dados:**

O conjunto de dados foi dividido em 60% para treino e 40% para teste.

   ```python
   X_train, X_test, y_train, y_test = train_test_split(X_filtered, y_filtered, test_size=0.4, random_state=0)
   ```

**Balanceamento dos Dados:**

Aplicação do SMOTE para balancear as classes no conjunto de treinamento.

   ```python
   smote = SMOTE(random_state=0, sampling_strategy='auto', k_neighbors=5)
   X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)
   ```
**Modelo de Classificação:**
   - Utilização do `BalancedRandomForestClassifier` para lidar com o desbalanceamento dos dados.
   - Ajuste dos hiperparâmetros utilizando `GridSearchCV`.

   ```python
   param_grid = {
       'n_estimators': [50, 100, 200],
       'max_depth': [None, 10, 20, 30],
       'min_samples_split': [2, 5, 10],
       'min_samples_leaf': [1, 2, 4]
   }

   grid_search = GridSearchCV(estimator=BalancedRandomForestClassifier(random_state=42),
                              param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)
   grid_search.fit(X_train_resampled, y_train_resampled)
   ```

### Resultados do Modelo

- **Melhores Hiperparâmetros:** `{'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 50}`
- **Acurácia no Conjunto de Teste:** `0.5553`
- **Acurácia no Conjunto de Treinamento:** `0.6257`

### Relatório de Classificação

| Classe | Precisão | Recall | F1-score | Suporte |
|--------|----------|--------|----------|---------|
| Alto   | 0.26     | 0.63   | 0.37     | 181     |
| Baixo  | 0.35     | 0.45   | 0.39     | 354     |
| Médio  | 0.78     | 0.57   | 0.66     | 1354    |

- **Acurácia Geral:** `0.56`
- **Média Macro:** Precisão: `0.46`, Recall: `0.55`, F1-score: `0.47`
- **Média Ponderada:** Precisão: `0.65`, Recall: `0.56`, F1-score: `0.58`

### Insights Principais

#### Distribuição Salarial
A distribuição das faixas salariais mostra uma concentração nas faixas intermediárias:
- **Faixa mais comum**: R$ 8.001 a R$ 12.000/mês (1.026 profissionais)
- **Segunda mais comum**: R$ 4.001 a R$ 6.000/mês (745 profissionais)
- **Terceira mais comum**: R$ 12.001 a R$ 16.000/mês (650 profissionais)

#### Linguagens Mais Impactantes no Salário
Nossa análise de importância de features revelou quais linguagens têm maior correlação com as faixas salariais:

1. **SQL** - Importância de 26,4%
2. **Python** - Importância de 15,8% 
3. **Scala** - Importância de 7,5%
4. **VB/VBA** - Importância de 6,6% 
5. **R** - Importância de 6,5%

Interessantemente, "não utilizar nenhuma linguagem" aparece com uma importância significativa de 19,1%.

### Interpretação dos Resultados

- O modelo tem melhor precisão na identificação da faixa salarial "Médio" (78%)
- Desempenho mais fraco nas faixas "Alto" (26%) e "Baixo" (35%)

### Implicações para o Mercado

1. **Importância do SQL**: O domínio de SQL demonstra ser um diferencial significativo para a remuneração, sugerindo a contínua relevância de habilidades relacionadas a banco de dados.

2. **Python como ferramenta essencial**: Confirma-se a posição do Python como linguagem fundamental na área de dados.

3. **Valorização de habilidades específicas**: Linguagens como Scala, embora menos comuns, parecem associadas a salários mais elevados, possivelmente por sua aplicação em contextos especializados como Big Data.

### Conclusão

A análise revela padrões claros de distribuição salarial entre profissionais de dados no Brasil, com concentração nas faixas intermediárias de R$ 4.000 a R$ 16.000/mês. As habilidades técnicas, especialmente em SQL e Python, demonstram forte correlação com maiores faixas salariais.

O modelo preditivo desenvolvido, apesar de suas limitações (acurácia de 55,5%), oferece insights valiosos sobre quais competências técnicas podem influenciar positivamente a remuneração de profissionais da área.

---

## Conclusão
Os resultados obtidos neste trabalho confirmam a hipótese de que características demográficas e profissionais influenciam significativamente a faixa salarial dos indivíduos. Os modelos supervisionados treinados — XGBoost e Random Forest — demonstraram bom desempenho preditivo, com acurácia geral acima de 78%, sendo capazes de prever com razoável precisão a categoria salarial com base nos atributos fornecidos.

NOTA: O modelo foi treinado usando o nível dos funcionários (Júnior, Pleno, Sênior), entretanto, ao contrário das expectativas, a retirada desse atributo não impacta o modelo de forma a torná-lo ineficaz, a perda é mínima (cerca de 2 a 5%), o que representa uma robustez dos modelos.

### Implicações para o Mercado
Habilidades técnicas como diferencial salarial: Linguagens como SQL, Python e R apareceram entre as variáveis mais relevantes para a previsão salarial, reforçando a importância da qualificação técnica.

Perfil demográfico importa: Variáveis como nível de ensino, tempo de experiência e cargo atual tiveram impacto expressivo no modelo, indicando a relevância de aspectos não técnicos na composição salarial.

Desempenho desigual entre classes salariais: Ambos os modelos tiveram melhor desempenho na previsão de salários médios. As faixas "Baixa" e "Alta" ainda apresentam desafios preditivos, mesmo com uso de técnicas como SMOTE para balanceamento.

### Próximos Passos Recomendados
 Inclusão de novas variáveis: Incorporar dados como certificações técnicas, tipo de empresa, nível de liderança e porte da organização.

 Análise regionalizada: Explorar o impacto da localização geográfica (UFs, capitais vs. interior) nos salários.

 Estudo longitudinal: Acompanhar como o valor de determinadas competências varia ao longo do tempo no mercado de dados.

 Avaliação de modelos interpretáveis: Testar algoritmos como Explainable Boosting Machines (EBM) para aliar performance e transparência.

Perguntas Frequentes
-Por que o modelo erra mais nas faixas 'Alta' e 'Baixa'?
Essas faixas geralmente concentram perfis mais extremos e heterogêneos. No caso da faixa "Alta", podem incluir cargos executivos com trajetórias muito específicas; já a faixa "Baixa" pode abranger desde iniciantes até profissionais em transição de carreira.

-Por que utilizar SMOTE?
O SMOTE foi utilizado para equilibrar o número de amostras por classe no conjunto de treino, ajudando o modelo a aprender melhor os padrões das faixas menos representadas.

-Como interpretar a importância das features?
A importância atribuída a uma feature no modelo Random Forest indica o quanto ela contribui para a tomada de decisão do modelo. SQL, nível de ensino, tempo de experiência e nível do cargo estão entre as mais relevantes.

-O XGBoost é sempre melhor?
Não necessariamente. Apesar da maior acurácia, o XGBoost pode ser mais difícil de explicar para usuários não técnicos e mais custoso computacionalmente. A escolha depende do objetivo do projeto.


# APÊNDICES

[Código (Hipótese 1 - Modelo 1 e 2)](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/models/MODELOS_ArvoreDecis%C3%A3o_KNN_HIPOTESE%201.ipynb)

[Código (Hipótese 2 - Modelo 1)](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/models/modeloXGBoost.py)

[Código (Hipótese 2 - Modelo 2)](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/models/modeloRandomForest.py)

[Código (Hipótese 3)](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/assets/models/model_hip3.ipynb)

[Apresentação final](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/pdf%20slide.pdf)

[Vídeo da apresentação](https://github.com/ICEI-PUC-Minas-PPL-CDIA/ppl-cd-pcd-sist-int-2025-1-grupo-5-Salarios-de-Profissionais/blob/main/Quais%20Fatores%20Influenciam%20os%20Sal%C3%A1rios%20dos%20Profissionais%20de%20Dados%20no%20Brasil%202.mp4)




