# Relatório — Laboratório Estatístico de Quadrinhos

## 1. Identificação

**Aluno:** Renato Alves Carvalho  
**Matrícula:** 72601667  
**Curso:** Ciência da Computação  
**Disciplina:** Matemática e Estatística para Computação  
**Modalidade:** Virtual - Campus Virtual  
**Período:** 2º semestre - EAD 2026  

---

## 2. Introdução

Este trabalho apresenta o desenvolvimento de um Laboratório Estatístico Interativo utilizando Python e Streamlit.

A proposta foi aplicar conceitos estudados na disciplina de Matemática e Estatística para Computação em um conjunto de dados real. Além da análise dos dados, parte importante do trabalho foi implementar manualmente as principais funções estatísticas, evitando o uso de funções prontas para realizar os cálculos principais.

A aplicação desenvolvida permite realizar análises descritivas, identificar possíveis outliers, estudar relações entre variáveis, realizar regressão linear e predições, executar simulações probabilísticas e comparar os dados observados com distribuições teóricas.

---

## 3. Dataset utilizado

Foi utilizado o dataset **Comic Books Dataset (10,000 entries)**, contendo informações relacionadas a histórias em quadrinhos.

O conjunto utilizado possui aproximadamente:

- 10.000 registros
- 17 variáveis
- variáveis numéricas e categóricas

O tema foi escolhido por permitir trabalhar diferentes tipos de informações, como ano de lançamento, quantidade de páginas e outras características das obras.

**Fonte original do dataset:**

https://www.kaggle.com/datasets/rudrakumargupta/comic-books-dataset-10000-entries

O arquivo utilizado no projeto foi:

`comic_books_10000_dataset.csv`

---

## 4. Tecnologias utilizadas

O projeto foi desenvolvido em Python.

As principais ferramentas e bibliotecas utilizadas foram:

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib

O Streamlit foi utilizado para construir a interface interativa. O Pandas foi utilizado principalmente para leitura e manipulação do conjunto de dados. NumPy foi utilizado como referência na validação dos cálculos e em partes auxiliares das simulações. Matplotlib foi utilizado para a construção dos gráficos.

Os principais cálculos estatísticos apresentados ao usuário foram implementados no módulo próprio `minhastats.py`.

---

## 5. Núcleo estatístico próprio

Foi criada a biblioteca `minhastats.py`, contendo implementações próprias das principais medidas estatísticas utilizadas no projeto.

Foram implementadas as seguintes funções:

- média
- mediana
- moda
- amplitude
- variância populacional
- variância amostral
- desvio padrão populacional
- desvio padrão amostral
- percentis
- quartis
- coeficiente de variação
- covariância
- correlação de Pearson
- regressão linear simples
- predição

### 5.1 Média

A média aritmética foi calculada pela soma dos valores dividida pela quantidade de observações.

**Fórmula:**

μ = (Σ xi) / n

onde:

- `xi` representa cada valor observado
- `n` representa a quantidade de valores

### 5.2 Mediana

A mediana foi obtida após ordenar os valores.

Quando a quantidade de elementos é ímpar, utiliza-se o elemento central. Quando é par, é calculada a média dos dois elementos centrais.

### 5.3 Moda

A moda corresponde ao valor ou aos valores que apresentam a maior frequência dentro do conjunto analisado.

### 5.4 Amplitude

A amplitude foi calculada pela diferença entre o maior e o menor valor.

**Fórmula:**

Amplitude = máximo - mínimo

### 5.5 Variância populacional

A variância populacional foi calculada pela fórmula:

σ² = Σ(xi - μ)² / n

Ela representa a dispersão dos valores em relação à média da população.

### 5.6 Variância amostral

Para a variância amostral foi utilizada a correção de Bessel:

s² = Σ(xi - x̄)² / (n - 1)

### 5.7 Desvio padrão

O desvio padrão corresponde à raiz quadrada da variância.

**Populacional:**

σ = √σ²

**Amostral:**

s = √s²

### 5.8 Percentis e quartis

Os percentis dividem os dados ordenados de acordo com determinada porcentagem da distribuição.

Os quartis utilizados foram:

- Q1 = percentil 25
- Q2 = percentil 50
- Q3 = percentil 75

Q2 também corresponde à mediana.

### 5.9 Coeficiente de variação

O coeficiente de variação foi calculado utilizando:

CV = (s / |x̄|) × 100

O resultado permite observar a dispersão relativa dos dados em relação à média.

### 5.10 Covariância

A covariância foi utilizada para analisar como duas variáveis variam conjuntamente.

Para a covariância amostral foi utilizada:

Cov(X,Y) = Σ[(xi - x̄)(yi - ȳ)] / (n - 1)

### 5.11 Correlação de Pearson

A correlação de Pearson foi calculada a partir da covariância e dos desvios padrão:

r = Cov(X,Y) / (sx × sy)

O coeficiente pode variar entre -1 e 1.

Valores próximos de 1 indicam associação linear positiva, valores próximos de -1 indicam associação linear negativa e valores próximos de zero indicam pouca associação linear.

---

## 6. Validação da biblioteca própria

Para verificar se as funções implementadas estavam produzindo resultados corretos, foi criado o arquivo `test_minhastats.py`.

Os resultados das funções próprias foram comparados com funções de referência do Python e do NumPy.

Foi adotada tolerância numérica de:

`1e-9`

Foram testados:

- média
- mediana
- moda
- amplitude
- variâncias
- desvios padrão
- percentis
- quartis
- coeficiente de variação
- covariância
- correlação de Pearson
- regressão linear
- predição

Ao executar os testes, todas as verificações foram concluídas com sucesso.

---

## 7. Estatística descritiva interativa

A aplicação permite selecionar uma variável numérica do dataset.

Após a seleção, são apresentadas medidas estatísticas como média, mediana, desvio padrão, variância, mínimo, máximo e quartis.

Também são apresentados gráficos para facilitar a análise da distribuição dos valores.

### Detecção de outliers

Para detectar possíveis valores discrepantes foi utilizada a regra do intervalo interquartil (IQR).

IQR = Q3 - Q1

Os limites são calculados por:

Limite inferior = Q1 - 1,5 × IQR

Limite superior = Q3 + 1,5 × IQR

Valores fora desses limites são identificados como possíveis outliers.

Na variável `Page Count`, por exemplo, foram encontrados 4 possíveis outliers pela regra do IQR.

![Estatística descritiva](imagens/01_estatistica_descritiva.png)

---

## 8. Lei dos Grandes Números

Foi desenvolvida uma simulação de Monte Carlo para demonstrar a Lei dos Grandes Números.

No experimento são realizados diversos lançamentos simulados de um dado.

O valor esperado teórico de um dado comum de seis faces é:

E(X) = 3,5

Conforme a quantidade de lançamentos aumenta, a média acumulada dos resultados tende a se aproximar desse valor teórico.

O experimento permite alterar a quantidade de lançamentos e observar essa convergência por meio de um gráfico.

---

## 9. Teorema Central do Limite

O Teorema Central do Limite foi demonstrado através da retirada repetida de amostras de uma variável do dataset.

O usuário pode selecionar:

- variável numérica
- tamanho de cada amostra
- número de repetições

Para cada amostra é calculada uma média.

Quando são realizadas muitas repetições, a distribuição dessas médias tende a apresentar um formato aproximadamente Normal, principalmente conforme o tamanho das amostras aumenta.

![Teorema Central do Limite](imagens/02_teorema_central_limite.png)

---

## 10. Distribuições teóricas

Foram realizadas comparações entre os dados observados e distribuições teóricas.

Foram utilizadas:

- Distribuição Normal
- Distribuição de Poisson

### 10.1 Distribuição Normal

Para a distribuição Normal, a média e o desvio padrão foram estimados a partir da variável escolhida.

A curva teórica foi sobreposta ao histograma dos dados, permitindo comparar visualmente o comportamento observado com o comportamento esperado de uma distribuição Normal.

A comparação visual permite verificar se o formato dos dados apresenta ou não características semelhantes às da distribuição teórica.

### 10.2 Distribuição de Poisson

Como segunda distribuição foi utilizada a distribuição de Poisson.

A variável `Page Count` foi utilizada por representar uma contagem inteira não negativa.

O parâmetro λ foi estimado a partir da média dos dados.

Na análise realizada:

λ ≈ 2232,8712

A comparação visual mostrou que os dados de quantidade de páginas possuem uma dispersão muito maior do que a região de maior concentração prevista pela distribuição de Poisson.

Por esse motivo, a distribuição de Poisson apresentou baixo ajuste visual aos dados observados.

Esse resultado também mostra que uma distribuição não deve ser escolhida somente porque uma variável possui valores numericamente compatíveis com o modelo. É necessário analisar as características dos dados e a qualidade do ajuste.

![Distribuição de Poisson](imagens/03_distribuicao_poisson.png)

---

## 11. Correlação e regressão linear

A aplicação permite selecionar duas variáveis numéricas para estudar a relação entre elas.

Foram implementados:

- covariância
- correlação de Pearson
- gráfico de dispersão
- regressão linear simples
- equação da reta
- coeficiente de determinação R²
- predição interativa

### 11.1 Regressão linear

A regressão linear simples foi implementada pelo método dos mínimos quadrados.

A equação utilizada possui a forma:

ŷ = a + bx

onde:

- `a` é o intercepto
- `b` é o coeficiente angular
- `x` é o valor da variável independente
- `ŷ` é o valor previsto

O coeficiente angular foi calculado por:

b = Σ[(xi - x̄)(yi - ȳ)] / Σ[(xi - x̄)²]

O intercepto foi calculado por:

a = ȳ - b x̄

### 11.2 Análise de Release Year e Page Count

Uma das análises realizadas utilizou:

X = `Release Year`

Y = `Page Count`

Os resultados encontrados foram aproximadamente:

- Covariância: 1873,7033
- Correlação de Pearson: 0,1349
- Intercepto: -66020,7783
- Coeficiente angular: 33,8644
- R²: 0,0182

A equação aproximada da regressão foi:

ŷ = -66020,7783 + 33,8644x

A correlação encontrada é positiva, porém fraca.

O R² de aproximadamente 0,0182 indica que cerca de 1,82% da variação observada na quantidade de páginas é explicada linearmente pelo ano de lançamento dentro deste conjunto de dados.

A aplicação também permite informar um valor de X e calcular automaticamente uma previsão para Y.

É importante destacar que correlação não implica causalidade. A existência de uma associação estatística não demonstra que uma variável seja responsável pelas alterações da outra.

![Correlação e regressão linear](imagens/04_regressao_linear.png)

---

## 12. Principais descobertas

Ao final das análises foram selecionadas três descobertas consideradas relevantes.

### 12.1 Lançamentos mais concentrados nos anos recentes

A variável `Release Year` apresentou média de aproximadamente 2015,50 e mediana de 2017.

Como a média ficou abaixo da mediana, foi observado indício de leve assimetria à esquerda.

Isso indica que o conjunto analisado apresenta maior concentração de registros em anos mais recentes, enquanto os registros mais antigos estendem a distribuição em direção aos anos anteriores.

### 12.2 Ano de lançamento explica pouco da quantidade de páginas

A correlação de Pearson entre `Release Year` e `Page Count` foi aproximadamente:

r = 0,1349

Esse resultado indica uma correlação linear positiva fraca.

O modelo de regressão apresentou:

R² ≈ 0,0182

Assim, apenas cerca de 1,82% da variação observada em `Page Count` é explicada linearmente pelo ano de lançamento nesse modelo.

Portanto, dentro deste dataset, obras mais recentes não apresentam uma relação linear forte com uma quantidade maior de páginas.

### 12.3 Quantidade de páginas apresenta grande dispersão

A variável `Page Count` apresentou:

- média aproximada: 2232,87
- mediana: 1571
- desvio padrão aproximado: 1866,72
- mínimo: 48
- máximo: 14.400

Esses valores mostram uma grande dispersão na quantidade de páginas das obras.

Essa característica também ficou evidente durante a comparação com a distribuição de Poisson, que apresentou baixo ajuste visual aos dados.

---

## 13. Conclusão

O desenvolvimento do Laboratório Estatístico permitiu aplicar na prática diferentes conteúdos estudados na disciplina.

Além de utilizar técnicas de estatística descritiva, foram implementadas manualmente funções para cálculo de medidas de posição, dispersão, correlação e regressão.

Os testes automatizados permitiram comparar as funções próprias com bibliotecas consolidadas, ajudando a verificar a corretude dos cálculos.

As simulações da Lei dos Grandes Números e do Teorema Central do Limite permitiram visualizar conceitos probabilísticos de forma prática.

A comparação com distribuições teóricas também mostrou que nem todo modelo probabilístico apresenta bom ajuste a qualquer conjunto de dados.

Por fim, a análise de correlação e regressão mostrou como duas variáveis podem apresentar associação estatística sem que isso signifique necessariamente uma relação de causa e efeito.

O projeto possibilitou reunir programação, matemática e estatística em uma única aplicação interativa.