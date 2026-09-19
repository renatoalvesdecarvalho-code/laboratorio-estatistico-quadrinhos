import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import minhastats as ms

# --------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# --------------------------------------------------

st.set_page_config(
    page_title="Laboratório Estatístico de Quadrinhos",
    page_icon="📊",
    layout="wide"
)

st.title("Laboratório Estatístico de Quadrinhos")

st.write(
    "Aplicação desenvolvida para explorar estatisticamente "
    "o dataset de quadrinhos utilizado no projeto."
)

# --------------------------------------------------
# CARREGAMENTO DOS DADOS
# --------------------------------------------------

@st.cache_data
def carregar_dados():
    return pd.read_csv("comic_books_10000_dataset.csv")


dados = carregar_dados()

st.success("Dataset carregado com sucesso!")

st.write("Quantidade de registros:", len(dados))
st.write("Quantidade de variáveis:", len(dados.columns))

# --------------------------------------------------
# VISUALIZAÇÃO DO DATASET
# --------------------------------------------------

st.header("Visualização dos dados")

st.dataframe(dados.head(20))

# --------------------------------------------------
# SELEÇÃO DA VARIÁVEL NUMÉRICA
# --------------------------------------------------

st.header("Estatística Descritiva")

colunas_numericas = dados.select_dtypes(include="number").columns.tolist()

variavel = st.selectbox(
    "Escolha uma variável numérica:",
    colunas_numericas
)

valores = dados[variavel].dropna().tolist()

# --------------------------------------------------
# MEDIDAS ESTATÍSTICAS
# --------------------------------------------------

st.subheader(f"Análise da variável: {variavel}")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Média",
        f"{ms.media(valores):.2f}"
    )

    st.metric(
        "Mediana",
        f"{ms.mediana(valores):.2f}"
    )

with col2:
    st.metric(
        "Desvio padrão",
        f"{ms.desvio_padrao_amostral(valores):.2f}"
    )

    st.metric(
        "Variância",
        f"{ms.variancia_amostral(valores):.2f}"
    )

with col3:
    minimo = min(valores)
    maximo = max(valores)

    st.metric(
        "Mínimo",
        f"{minimo:.2f}"
    )

    st.metric(
        "Máximo",
        f"{maximo:.2f}"
    )

# --------------------------------------------------
# QUARTIS
# --------------------------------------------------

q1 = ms.percentil(valores, 25)
q2 = ms.percentil(valores, 50)
q3 = ms.percentil(valores, 75)

st.subheader("Quartis")

st.write("Q1 (25%):", round(q1, 2))
st.write("Q2 (50%):", round(q2, 2))
st.write("Q3 (75%):", round(q3, 2))

# --------------------------------------------------
# DETECÇÃO DE OUTLIERS PELO IQR
# --------------------------------------------------

iqr = q3 - q1

limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

outliers = [
    valor
    for valor in valores
    if valor < limite_inferior or valor > limite_superior
]

st.subheader("Detecção de Outliers")

st.write("IQR:", round(iqr, 2))
st.write("Limite inferior:", round(limite_inferior, 2))
st.write("Limite superior:", round(limite_superior, 2))
st.write("Quantidade de outliers:", len(outliers))

# ---------------------------------------------
# TABELA DE FREQUÊNCIAS
# ---------------------------------------------

st.subheader("Tabela de Frequências")

# Agrupamento dos dados em classes
quantidade_classes = 10

frequencias, limites_classes = np.histogram(
    valores,
    bins=quantidade_classes
)

total_valores = len(valores)

tabela_frequencias = []

for i in range(quantidade_classes):
    limite_inferior_classe = limites_classes[i]
    limite_superior_classe = limites_classes[i + 1]

    frequencia_absoluta = int(frequencias[i])
    frequencia_relativa = (
        frequencia_absoluta / total_valores
    ) * 100

    tabela_frequencias.append({
        "Classe": (
            f"{limite_inferior_classe:.2f} "
            f"a {limite_superior_classe:.2f}"
        ),
        "Frequência absoluta": frequencia_absoluta,
        "Frequência relativa (%)": round(
            frequencia_relativa, 2
        )
    })

df_frequencias = pd.DataFrame(tabela_frequencias)

st.dataframe(
    df_frequencias,
    use_container_width=True,
    hide_index=True
)

st.caption(
    "Os valores foram agrupados em 10 classes para facilitar "
    "a visualização da distribuição de frequências."
)

# --------------------------------------------------
# HISTOGRAMA
# --------------------------------------------------

st.subheader("Histograma")

fig, ax = plt.subplots()

ax.hist(valores, bins=20)

ax.set_title(f"Distribuição de {variavel}")
ax.set_xlabel(variavel)
ax.set_ylabel("Frequência")

st.pyplot(fig)

plt.close(fig)

# --------------------------------------------------
# BOXPLOT
# --------------------------------------------------

st.subheader("Boxplot")

fig, ax = plt.subplots()

ax.boxplot(valores, orientation="horizontal")

ax.set_title(f"Boxplot de {variavel}")
ax.set_xlabel(variavel)

st.pyplot(fig)

plt.close(fig)

# --------------------------------------------------
# INTERPRETAÇÃO AUTOMÁTICA
# --------------------------------------------------

st.subheader("Interpretação")

media = ms.media(valores)
mediana = ms.mediana(valores)

if media > mediana:
    st.write(
        "A média é maior que a mediana. "
        "Isso sugere uma distribuição com assimetria à direita."
    )

elif media < mediana:
    st.write(
        "A média é menor que a mediana. "
        "Isso sugere uma distribuição com assimetria à esquerda."
    )

else:
    st.write(
        "A média e a mediana são iguais ou muito próximas, "
        "sugerindo uma distribuição aproximadamente simétrica."
    )

if len(outliers) > 0:
    st.write(
        f"Foram identificados {len(outliers)} possíveis outliers "
        "pela regra do IQR."
    )
else:
    st.write(
        "Não foram identificados outliers pela regra do IQR."
    )

# ============================================================
# RESUMO AUTOMÁTICO DA ESTATÍSTICA DESCRITIVA
# ============================================================

st.subheader("Resumo da análise")

media_atual = ms.media(valores)
mediana_atual = ms.mediana(valores)
desvio_atual = ms.desvio_padrao_amostral(valores)
amplitude_atual = max(valores) - min(valores)

st.write(
    f"A variável **{variavel}** possui média de aproximadamente "
    f"**{media_atual:.2f}** e mediana de **{mediana_atual:.2f}**. "
    f"O desvio padrão é de aproximadamente **{desvio_atual:.2f}** "
    f"e a amplitude observada é de **{amplitude_atual:.2f}**."
)

if media_atual > mediana_atual:
    st.write(
        "Como a média é maior que a mediana, os dados apresentam "
        "indício de assimetria à direita."
    )
elif media_atual < mediana_atual:
    st.write(
        "Como a média é menor que a mediana, os dados apresentam "
        "indício de assimetria à esquerda."
    )
else:
    st.write(
        "Como a média e a mediana são iguais, os dados apresentam "
        "indício de maior simetria em torno do centro."
    )

if len(outliers) > 0:
    percentual_outliers = (len(outliers) / len(valores)) * 100

    st.write(
        f"Foram identificados **{len(outliers)} possíveis outliers**, "
        f"correspondendo a aproximadamente **{percentual_outliers:.2f}%** "
        "dos valores analisados, utilizando a regra do IQR."
    )
else:
    st.write(
        "Não foram identificados possíveis outliers pela regra do IQR."
    )
    # ============================================================
# ANÁLISE DE RELAÇÃO ENTRE DUAS VARIÁVEIS
# ============================================================

st.divider()
st.header("Relação entre duas variáveis")

st.write(
    "Nesta seção é possível selecionar duas variáveis numéricas "
    "do dataset para analisar a relação existente entre elas."
)

variaveis_numericas = dados.select_dtypes(include="number").columns.tolist()

coluna_x = st.selectbox(
    "Selecione a variável X:",
    variaveis_numericas,
    index=0,
    key="variavel_x"
)

coluna_y = st.selectbox(
    "Selecione a variável Y:",
    variaveis_numericas,
    index=1 if len(variaveis_numericas) > 1 else 0,
    key="variavel_y"
)

if coluna_x == coluna_y:
    st.warning("Selecione duas variáveis diferentes para realizar a análise.")

else:
    x = dados[coluna_x].dropna()
    y = dados[coluna_y].dropna()

    dados_relacao = dados[[coluna_x, coluna_y]].dropna()

    x = dados_relacao[coluna_x].tolist()
    y = dados_relacao[coluna_y].tolist()

    st.subheader("Covariância e correlação")

    try:
        cov = ms.covariancia(x, y)
        corr = ms.correlacao_pearson(x, y)

        c1, c2 = st.columns(2)

        with c1:
            st.metric("Covariância", f"{cov:.4f}")

        with c2:
            st.metric("Correlação de Pearson", f"{corr:.4f}")

        if corr > 0.7:
            interpretacao = "Correlação positiva forte."
        elif corr > 0.3:
            interpretacao = "Correlação positiva moderada."
        elif corr > 0:
            interpretacao = "Correlação positiva fraca."
        elif corr < -0.7:
            interpretacao = "Correlação negativa forte."
        elif corr < -0.3:
            interpretacao = "Correlação negativa moderada."
        elif corr < 0:
            interpretacao = "Correlação negativa fraca."
        else:
            interpretacao = "Não foi identificada correlação linear."

        st.write("**Interpretação:**", interpretacao)

    except Exception as erro:
        st.error(f"Não foi possível calcular a relação: {erro}")

    # --------------------------------------------------------
    # GRÁFICO DE DISPERSÃO
    # --------------------------------------------------------

    st.subheader("Gráfico de dispersão")

    fig, ax = plt.subplots()

    ax.scatter(x, y, alpha=0.5)

    ax.set_xlabel(coluna_x)
    ax.set_ylabel(coluna_y)
    ax.set_title(f"{coluna_x} x {coluna_y}")

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)

    # --------------------------------------------------------
    # REGRESSÃO LINEAR
    # --------------------------------------------------------

    st.subheader("Regressão linear")

    try:
        intercepto, inclinacao, r2 = ms.regressao_linear(x, y)

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric("Intercepto", f"{intercepto:.4f}")

        with c2:
            st.metric("Inclinação", f"{inclinacao:.4f}")

        with c3:
            st.metric("R²", f"{r2:.4f}")

        st.write(
            f"**Equação da reta:** y = {intercepto:.4f} "
            f"+ ({inclinacao:.4f} × x)"
        )

        fig, ax = plt.subplots()

        ax.scatter(x, y, alpha=0.4)

        x_ordenado = sorted(x)

        y_previsto = [
            ms.prever(valor, intercepto, inclinacao)
            for valor in x_ordenado
        ]

        ax.plot(x_ordenado, y_previsto)

        ax.set_xlabel(coluna_x)
        ax.set_ylabel(coluna_y)
        ax.set_title("Regressão linear")

        plt.tight_layout()

        st.pyplot(fig)

        plt.close(fig)

    except Exception as erro:
        st.error(f"Não foi possível realizar a regressão linear: {erro}")

# ============================================================
# COMPLEMENTO DO MÓDULO 5 - PREDIÇÃO E INTERPRETAÇÃO
# ============================================================

st.subheader("Predição interativa")

st.write(
    "Informe um valor para a variável X e o modelo utilizará a "
    "equação da regressão linear para estimar o valor correspondente de Y."
)

valor_x_predicao = st.number_input(
    f"Digite um valor para {coluna_x}:",
    value=float(ms.media(dados[coluna_x].dropna().tolist())),
    key="valor_x_predicao"
)

valor_y_previsto = ms.prever(
    valor_x_predicao,
    intercepto,
    inclinacao
)

st.success(
    f"Valor previsto de {coluna_y}: {valor_y_previsto:.4f}"
)


st.subheader("Interpretação da regressão")

if inclinacao > 0:
    st.write(
        f"O coeficiente angular é {inclinacao:.4f}. "
        f"Isso significa que, no modelo ajustado, para cada aumento "
        f"de 1 unidade em {coluna_x}, o valor previsto de "
        f"{coluna_y} aumenta aproximadamente {abs(inclinacao):.4f} unidades."
    )

elif inclinacao < 0:
    st.write(
        f"O coeficiente angular é {inclinacao:.4f}. "
        f"Isso significa que, no modelo ajustado, para cada aumento "
        f"de 1 unidade em {coluna_x}, o valor previsto de "
        f"{coluna_y} diminui aproximadamente {abs(inclinacao):.4f} unidades."
    )

else:
    st.write(
        "O coeficiente angular é igual a zero. Neste modelo, "
        "não foi identificada variação linear de Y associada ao aumento de X."
    )


st.write(
    f"O intercepto da reta é {intercepto:.4f}. Ele representa o valor "
    f"previsto de {coluna_y} quando {coluna_x} é igual a zero. "
    "Dependendo das variáveis analisadas, esse valor pode ter apenas "
    "significado matemático e não possuir interpretação prática."
)


st.write(
    f"O coeficiente de determinação R² é {r2:.4f}. "
    f"Isso indica que aproximadamente {r2 * 100:.2f}% da variação observada "
    f"em {coluna_y} é explicada pela relação linear com {coluna_x} "
    "dentro deste modelo."
)


st.warning(
    "Correlação não implica causalidade. Uma associação estatística entre "
    "duas variáveis não demonstra, por si só, que uma variável seja a causa "
    "das alterações observadas na outra."
)
# ============================================================
# MÓDULO 3 - PROBABILIDADE E SIMULAÇÃO
# ============================================================

st.divider()
st.header("Probabilidade e Simulação")

st.write(
    "Nesta seção são realizadas simulações de Monte Carlo para "
    "demonstrar a Lei dos Grandes Números e o Teorema Central do Limite."
)

# ============================================================
# LEI DOS GRANDES NÚMEROS
# ============================================================

st.subheader("Lei dos Grandes Números")

st.write(
    "A Lei dos Grandes Números mostra que, à medida que aumentamos "
    "a quantidade de observações de uma amostra, a média amostral "
    "tende a se aproximar da média esperada da população."
)

st.write(
    "Para demonstrar esse comportamento, será simulada uma sequência "
    "de lançamentos de um dado de seis faces."
)

numero_simulacoes = st.slider(
    "Quantidade de lançamentos do dado:",
    min_value=100,
    max_value=10000,
    value=5000,
    step=100
)

# Gerador com semente fixa para permitir reprodução do experimento
rng = np.random.default_rng(42)

lancamentos = rng.integers(
    1,
    7,
    size=numero_simulacoes
)

medias_acumuladas = []
soma_acumulada = 0

for i, valor in enumerate(lancamentos, start=1):
    soma_acumulada += valor
    medias_acumuladas.append(
        soma_acumulada / i
    )

media_teorica_dado = 3.5

st.write(
    f"Média obtida após **{numero_simulacoes} lançamentos**: "
    f"**{medias_acumuladas[-1]:.4f}**"
)

st.write(
    f"Média teórica esperada para um dado justo: "
    f"**{media_teorica_dado:.4f}**"
)

fig, ax = plt.subplots()

ax.plot(
    range(1, numero_simulacoes + 1),
    medias_acumuladas,
    label="Média acumulada"
)

ax.axhline(
    media_teorica_dado,
    linestyle="--",
    label="Média teórica = 3,5"
)

ax.set_title("Lei dos Grandes Números")
ax.set_xlabel("Número de lançamentos")
ax.set_ylabel("Média acumulada")
ax.legend()

st.pyplot(fig)

plt.close(fig)

st.info(
    "Observe que, conforme a quantidade de lançamentos aumenta, "
    "a média acumulada tende a se aproximar do valor teórico 3,5. "
    "Esse comportamento ilustra a Lei dos Grandes Números."
)


# ============================================================
# TEOREMA CENTRAL DO LIMITE
# ============================================================

st.subheader("Teorema Central do Limite")

st.write(
    "O Teorema Central do Limite estabelece que, sob condições "
    "adequadas, a distribuição das médias de muitas amostras "
    "independentes tende a apresentar formato aproximadamente normal "
    "quando o tamanho das amostras aumenta."
)

tamanho_amostra = st.slider(
    "Tamanho de cada amostra:",
    min_value=5,
    max_value=100,
    value=30,
    step=5
)

quantidade_amostras = st.slider(
    "Quantidade de amostras:",
    min_value=100,
    max_value=5000,
    value=1000,
    step=100
)

medias_amostrais = []

for _ in range(quantidade_amostras):

    amostra = rng.integers(
        1,
        7,
        size=tamanho_amostra
    )

    media_amostra = sum(amostra) / len(amostra)

    medias_amostrais.append(
        media_amostra
    )

media_das_medias = (
    sum(medias_amostrais)
    / len(medias_amostrais)
)

st.write(
    f"Média das **{quantidade_amostras} médias amostrais**: "
    f"**{media_das_medias:.4f}**"
)

st.write(
    f"Valor teórico esperado: "
    f"**{media_teorica_dado:.4f}**"
)

fig, ax = plt.subplots()

ax.hist(
    medias_amostrais,
    bins=30,
    edgecolor="black",
    alpha=0.7
)

ax.axvline(
    media_teorica_dado,
    linestyle="--",
    label="Média teórica = 3,5"
)

ax.set_title("Distribuição das Médias Amostrais")
ax.set_xlabel("Média da amostra")
ax.set_ylabel("Frequência")
ax.legend()

st.pyplot(fig)

plt.close(fig)

st.info(
    "Mesmo que os resultados individuais do dado tenham distribuição "
    "discreta, a distribuição das médias de muitas amostras tende a "
    "assumir um formato aproximadamente normal. Esse comportamento "
    "ilustra o Teorema Central do Limite."
)

# ------------------------------------------------------------
# TEOREMA CENTRAL DO LIMITE
# ------------------------------------------------------------

st.subheader("Teorema Central do Limite")

st.write(
    "O experimento abaixo retira várias amostras da variável escolhida "
    "e calcula a média de cada amostra. Com muitas repetições, a "
    "distribuição dessas médias tende a assumir formato aproximadamente "
    "Normal."
)

variavel_tcl = st.selectbox(
    "Escolha a variável numérica para o TCL:",
    colunas_numericas,
    key="variavel_tcl"
)

tamanho_amostra = st.slider(
    "Tamanho de cada amostra:",
    min_value=5,
    max_value=100,
    value=30,
    step=5,
key="tamanho_amostra_tcl_dataset"
)

numero_repeticoes = st.slider(
    "Número de repetições:",
    min_value=100,
    max_value=5000,
    value=1000,
    step=100
)

valores_tcl = dados[variavel_tcl].dropna().tolist()

medias_amostrais = []

for _ in range(numero_repeticoes):

    amostra = random.choices(
        valores_tcl,
        k=tamanho_amostra
    )

    media_amostra = ms.media(amostra)

    medias_amostrais.append(media_amostra)

fig, ax = plt.subplots()

ax.hist(
    medias_amostrais,
    bins=30,
    density=True
)

ax.set_xlabel("Média amostral")
ax.set_ylabel("Densidade")
ax.set_title("Teorema Central do Limite")

plt.tight_layout()

st.pyplot(fig)

plt.close(fig)

st.write(
    "**Média das médias amostrais:**",
    round(ms.media(medias_amostrais), 4)
)

st.write(
    "**Média da variável no dataset:**",
    round(ms.media(valores_tcl), 4)
)

st.info(
    "O histograma mostra a distribuição das médias obtidas nas "
    "amostras. Conforme o tamanho das amostras e o número de "
    "repetições aumentam, essa distribuição tende a se aproximar "
    "de uma distribuição Normal."
)

# ============================================================
# MÓDULO 4 - DISTRIBUIÇÕES TEÓRICAS
# ============================================================

st.divider()
st.header("Distribuições Teóricas")

st.write(
    "Nesta seção, uma distribuição teórica é comparada com os dados "
    "observados. O objetivo é verificar visualmente o quanto o comportamento "
    "dos dados se aproxima de um modelo probabilístico conhecido."
)

# ------------------------------------------------------------
# DISTRIBUIÇÃO NORMAL
# ------------------------------------------------------------

st.subheader("Distribuição Normal")

variavel_normal = st.selectbox(
    "Escolha uma variável numérica para comparar com a distribuição Normal:",
    colunas_numericas,
    key="variavel_normal"
)

valores_normal = dados[variavel_normal].dropna().tolist()

media_normal = ms.media(valores_normal)
desvio_normal = ms.desvio_padrao_populacional(valores_normal)

if desvio_normal > 0:

    import math

    x_min = min(valores_normal)
    x_max = max(valores_normal)

    quantidade_pontos = 300

    passo = (x_max - x_min) / (quantidade_pontos - 1)

    x_normal = [
        x_min + i * passo
        for i in range(quantidade_pontos)
    ]

    y_normal = []

    for x in x_normal:

        densidade = (
            1 / (desvio_normal * math.sqrt(2 * math.pi))
        ) * math.exp(
            -0.5 * ((x - media_normal) / desvio_normal) ** 2
        )

        y_normal.append(densidade)

    fig, ax = plt.subplots()

    ax.hist(
        valores_normal,
        bins=30,
        density=True,
        alpha=0.6,
        label="Dados observados"
    )

    ax.plot(
        x_normal,
        y_normal,
        linewidth=2,
        label="Distribuição Normal"
    )

    ax.set_xlabel(variavel_normal)
    ax.set_ylabel("Densidade")
    ax.set_title(
        f"Histograma de {variavel_normal} com curva Normal"
    )

    ax.legend()

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)

    st.write(
        f"**Média estimada:** {media_normal:.4f}"
    )

    st.write(
        f"**Desvio padrão estimado:** {desvio_normal:.4f}"
    )

    st.info(
        "A curva representa uma distribuição Normal com média e "
        "desvio padrão estimados a partir dos próprios dados. "
        "Quanto mais o formato do histograma acompanhar a curva, "
        "melhor é o ajuste visual à distribuição Normal."
    )

else:

    st.warning(
        "A variável escolhida possui desvio padrão igual a zero "
        "e não pode ser comparada com uma distribuição Normal."
    )


# ------------------------------------------------------------
# SEGUNDA DISTRIBUIÇÃO: POISSON
# ------------------------------------------------------------

st.subheader("Distribuição de Poisson")

st.write(
    "Como segunda distribuição teórica, utilizamos a distribuição de "
    "Poisson, adequada para representar contagens inteiras não negativas. "
    "Escolha uma variável que represente uma contagem para realizar "
    "a comparação."
)

# Para a distribuição de Poisson foi utilizada Page Count,
# pois representa uma variável quantitativa discreta de contagem.
variavel_poisson = "Page Count"

st.write(
    "**Variável utilizada:** Page Count (quantidade de páginas)"
)

st.caption(
    "A variável foi definida especificamente para esta análise porque "
    "representa uma contagem discreta não negativa. Variáveis como "
    "Release Year não são adequadas para este modelo, pois representam "
    "anos e não contagens de ocorrências."
)

valores_poisson_originais = (
    dados[variavel_poisson]
    .dropna()
    .tolist()
)

valores_poisson = [
    int(round(valor))
    for valor in valores_poisson_originais
    if valor >= 0
]

if len(valores_poisson) > 0:

    lambda_poisson = ms.media(valores_poisson)

    valor_minimo = min(valores_poisson)
    valor_maximo = max(valores_poisson)

    # Evita gerar milhares de pontos quando a variável possui
    # valores extremos.
    limite_superior = min(
        valor_maximo,
        int(lambda_poisson + 4 * math.sqrt(lambda_poisson)) + 1
        if lambda_poisson > 0
        else valor_maximo
    )

    limite_superior = max(
        limite_superior,
        valor_minimo + 1
    )

    valores_k = list(
        range(
            max(0, valor_minimo),
            limite_superior + 1
        )
    )

    probabilidades_poisson = []

    for k in valores_k:

        try:
            probabilidade = (
                math.exp(-lambda_poisson)
                * (lambda_poisson ** k)
                / math.factorial(k)
            )
        except (OverflowError, ValueError):
            probabilidade = 0

        probabilidades_poisson.append(
            probabilidade
        )

    fig, ax = plt.subplots()

    ax.hist(
        valores_poisson,
        bins=30,
        density=True,
        alpha=0.6,
        label="Dados observados"
    )

    ax.plot(
        valores_k,
        probabilidades_poisson,
        marker="o",
        linewidth=2,
        label="Distribuição de Poisson"
    )

    ax.set_xlabel(variavel_poisson)
    ax.set_ylabel("Densidade / Probabilidade")
    ax.set_title(
        f"{variavel_poisson} comparada à distribuição de Poisson"
    )

    ax.legend()

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)

    st.write(
        f"**Parâmetro λ (lambda) estimado:** "
        f"{lambda_poisson:.4f}"
    )

    st.info(
        "Na distribuição de Poisson, o parâmetro λ representa a "
        "média esperada da contagem. A comparação do gráfico permite "
        "avaliar visualmente se os dados apresentam comportamento "
        "semelhante ao modelo de Poisson."
    )

    st.warning(
        "A escolha de uma distribuição teórica depende da natureza "
        "da variável. A presença da curva no gráfico não significa "
        "automaticamente que a distribuição seja um bom modelo para "
        "os dados; o ajuste deve ser interpretado visualmente e de "
        "acordo com o significado da variável."
    )

else:
    st.warning(
        "Não existem valores não negativos suficientes para realizar "
        "a comparação com a distribuição de Poisson."
    )


# ------------------------------------------------------------
# INTERPRETAÇÃO DO AJUSTE
# ------------------------------------------------------------

st.subheader("Interpretação do ajuste")

st.write(
    "Visualmente, a distribuição de Poisson apresenta baixo ajuste "
    "aos dados de quantidade de páginas. Os valores observados possuem "
    "grande dispersão e amplitude, enquanto a distribuição teórica de "
    "Poisson fica concentrada em uma região muito menor."
)

st.write(
    "Neste conjunto de dados, portanto, a distribuição de Poisson "
    "não representa adequadamente o comportamento da variável "
    "Page Count. Esse resultado também demonstra que uma distribuição "
    "teórica deve ser avaliada de acordo com as características dos "
    "dados, e não apenas aplicada por possuir uma variável numericamente "
    "compatível."
)


# ============================================================
# MÓDULO 6 - RELATÓRIO DE DESCOBERTAS
# ============================================================

st.divider()
st.header("Relatório de Descobertas")

st.write(
    "A partir das análises realizadas pelo laboratório estatístico, "
    "foram selecionadas três descobertas relevantes sobre o conjunto "
    "de dados de quadrinhos."
)

# ------------------------------------------------------------
# DESCOBERTA 1
# ------------------------------------------------------------

st.subheader("1. Os lançamentos estão mais concentrados nos anos recentes")

st.write(
    "A variável Release Year apresentou média de aproximadamente "
    "2015,50 e mediana de 2017. Como a média ficou abaixo da mediana, "
    "a análise descritiva indica uma leve assimetria à esquerda."
)

st.write(
    "Isso mostra que o conjunto de dados possui maior concentração "
    "de obras em anos mais recentes, enquanto os registros mais antigos "
    "estendem a distribuição em direção aos anos anteriores."
)


# ------------------------------------------------------------
# DESCOBERTA 2
# ------------------------------------------------------------

st.subheader(
    "2. Ano de lançamento explica pouco da quantidade de páginas"
)

st.write(
    "Na análise entre Release Year e Page Count, a correlação de "
    "Pearson encontrada foi aproximadamente 0,1349, indicando uma "
    "correlação linear positiva fraca."
)

st.write(
    "O modelo de regressão apresentou R² de aproximadamente 0,0182. "
    "Isso significa que apenas cerca de 1,82% da variação observada "
    "na quantidade de páginas é explicada linearmente pelo ano de "
    "lançamento neste conjunto de dados."
)

st.write(
    "Portanto, obras mais recentes não apresentam, neste dataset, "
    "uma relação linear forte com uma quantidade maior de páginas."
)


# ------------------------------------------------------------
# DESCOBERTA 3
# ------------------------------------------------------------

st.subheader(
    "3. A quantidade de páginas apresenta grande dispersão"
)

st.write(
    "A análise da variável Page Count revelou uma amplitude elevada, "
    "com presença de obras que possuem milhares de páginas e valores "
    "extremos que chegam a aproximadamente 14.400 páginas."
)

st.write(
    "Essa grande dispersão também ficou evidente na comparação com "
    "a distribuição de Poisson. Embora a média estimada tenha sido "
    "aproximadamente 2.232,87 páginas, a distribuição teórica ficou "
    "concentrada em uma região muito menor do que os dados observados."
)

st.write(
    "Visualmente, portanto, a distribuição de Poisson apresentou "
    "baixo ajuste à quantidade de páginas deste conjunto de dados."
)


st.info(
    "As descobertas apresentadas foram obtidas a partir das estatísticas "
    "e visualizações produzidas pelo próprio Laboratório Estatístico. "
    "As relações identificadas descrevem este conjunto de dados e não "
    "devem ser interpretadas automaticamente como relações de causa e efeito."
)

# ==========================================================
# CONCLUSÃO
# ==========================================================

st.divider()
st.header("Conclusão")

st.write(
    "A aplicação desenvolvida permite explorar o conjunto de dados de "
    "quadrinhos por meio de diferentes conceitos estatísticos. Foram "
    "utilizadas medidas de posição e dispersão, identificação de possíveis "
    "outliers, análise de correlação, regressão linear e predição."
)

st.write(
    "Também foram realizadas simulações relacionadas à Lei dos Grandes "
    "Números e ao Teorema Central do Limite, além da comparação dos dados "
    "com distribuições teóricas, como a distribuição Normal e a distribuição "
    "de Poisson."
)

st.write(
    "Os resultados mostram que diferentes técnicas estatísticas podem ser "
    "utilizadas para compreender o comportamento das variáveis do conjunto "
    "de dados e também demonstram que nem todo modelo probabilístico é "
    "adequado para qualquer tipo de variável."
)

st.write(
    "As principais funções estatísticas utilizadas nas análises foram "
    "implementadas no módulo próprio `minhastats.py`, permitindo aplicar "
    "na prática os conceitos estudados no projeto."
)