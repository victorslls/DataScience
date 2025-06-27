### Data Science

## 📌 Problema
Prever o salário com base em características como idade e experiência.

## 📊 Fonte dos Dados
Dataset fictício baseado em dados de RH.

## 🧹 Técnicas Utilizadas
- Limpeza e tratamento de dados (remoção de valores nulos)
- Codificação de variáveis categóricas
- Visualizações com Seaborn e Plotly
- Modelagem preditiva com Regressão Linear

## 📈 Resultados
- R²: 0.82
- RMSE: 1200

## 🚀 Como rodar o projeto
1. Clone este repositório  
2. Instale as dependências:  
   ```bash
   pip install -r requirements.txt

## 🚀 Como rodar o projeto jupter
    
    jupyter notebook


    Projeto de Previsão Salarial com Machine Learning

#### 🔍 Visão Geral do Projeto

   Este projeto tem como objetivo o desenvolvimento de um modelo preditivo capaz de estimar o salário de um profissional com base em variáveis como idade, experiência profissional e escolaridade. O estudo simula uma aplicação real em contextos de Recursos Humanos e análise de dados trabalhistas.

   📂 Fonte dos Dados

   O conjunto de dados utilizado é fictício, mas inspirado em dados reais de RH. Ele foi preparado para representar uma variedade de perfis profissionais, com colunas como:

   Idade

   Anos de experiência

   Escolaridade

   Setor de atuação

   Salário (variável alvo)

   O dataset pode ser acessado aqui

   📅 Etapas Realizadas

### 1. Carregamento dos Dados

   Leitura do dataset com pandas.read_csv().

   Análise inicial com .info(), .head() e .describe().

### 2. Limpeza e Tratamento

   Remoção de valores ausentes com dropna().

   Conversão de tipos e padronização de categorias.

### 3. Codificação de Variáveis Categóricas

   Label Encoding para escolaridade com LabelEncoder().

   One-Hot Encoding para o setor com pd.get_dummies().

#### 4. Análise Exploratória de Dados (EDA)

   Foram geradas visualizações com seaborn, matplotlib e plotly:

   Histogramas de idade e salário

   Boxplots salariais por setor

   Matriz de correlação entre variáveis numéricas

   Gráficos interativos para exploração dos dados

### 5. Modelagem

   Algoritmo: Regressão Linear com scikit-learn

   Divisão dos dados em treino e teste: train_test_split()

   Avaliação com:

   R² (coeficiente de determinação)

   RMSE (erro quadrático médio)

   📊 Resultados Obtidos

   R²: 0.82 (boa explicação da variância dos dados)

   RMSE: 1200 (erro médio nas previsões)

   Correlação Positiva: entre experiência e salário, indicando que profissionais com mais tempo de experiência tendem a ter salários mais altos.

   📈 Interpretação e Insights

   O modelo conseguiu captar relações importantes entre as variáveis.

   Setores como tecnologia e engenharia apresentaram salários médios mais altos.

   Escolaridade teve impacto relevante, mas menor que a experiência.

   A distribuição de salários mostrou concentração entre R$ 3.000 e R$ 7.000, com outliers acima disso.

   🚀 Conclusão e Possíveis Expansões

   O modelo é funcional e pode ser aplicado em sistemas de RH.

   A análise mostrou que variáveis como experiência são fortemente preditivas.

   🔹 Sugestões futuras:



🚧 Como rodar o projeto

### 1. Instale as dependências

   pip install -r requirements.txt

#### 2. Execute o Jupyter Notebook

   jupyter notebook

   Abra os notebooks eda.ipynb e modelagem.ipynb para acompanhar as etapas de análise exploratória e modelagem preditiva.

   🎓 Tecnologias Utilizadas

   Python 3

   Pandas / NumPy

   Scikit-learn

   Seaborn / Matplotlib / Plotly

   Jupyter Notebook

