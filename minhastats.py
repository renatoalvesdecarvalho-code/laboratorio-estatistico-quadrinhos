# Biblioteca estatística própria
# Projeto: Laboratório Estatístico de Quadrinhos
# As funções abaixo implementam os cálculos sem utilizar
# funções estatísticas prontas de NumPy, Pandas ou statistics.


def _validar_dados(dados):
    """Verifica se a lista possui dados."""
    valores = list(dados)

    if len(valores) == 0:
        raise ValueError("A lista de dados não pode estar vazia.")

    return valores


def media(dados):
    """Calcula a média aritmética."""
    valores = _validar_dados(dados)

    soma = 0

    for valor in valores:
        soma += valor

    return soma / len(valores)


def mediana(dados):
    """Calcula a mediana."""
    valores = sorted(_validar_dados(dados))
    n = len(valores)

    meio = n // 2

    if n % 2 == 1:
        return valores[meio]

    return (valores[meio - 1] + valores[meio]) / 2


def moda(dados):
    """Calcula a moda. Retorna uma lista caso exista mais de uma."""
    valores = _validar_dados(dados)

    frequencias = {}

    for valor in valores:
        if valor in frequencias:
            frequencias[valor] += 1
        else:
            frequencias[valor] = 1

    maior_frequencia = max(frequencias.values())

    modas = []

    for valor, quantidade in frequencias.items():
        if quantidade == maior_frequencia:
            modas.append(valor)

    return modas


def amplitude(dados):
    """Calcula a amplitude total."""
    valores = _validar_dados(dados)

    menor = valores[0]
    maior = valores[0]

    for valor in valores:

        if valor < menor:
            menor = valor

        if valor > maior:
            maior = valor

    return maior - menor


def variancia_populacional(dados):
    """Calcula a variância populacional."""
    valores = _validar_dados(dados)

    m = media(valores)

    soma = 0

    for valor in valores:
        soma += (valor - m) ** 2

    return soma / len(valores)


def variancia_amostral(dados):
    """Calcula a variância amostral."""
    valores = _validar_dados(dados)

    if len(valores) < 2:
        raise ValueError(
            "A variância amostral exige pelo menos dois valores."
        )

    m = media(valores)

    soma = 0

    for valor in valores:
        soma += (valor - m) ** 2

    return soma / (len(valores) - 1)


def desvio_padrao_populacional(dados):
    """Calcula o desvio padrão populacional."""
    return variancia_populacional(dados) ** 0.5


def desvio_padrao_amostral(dados):
    """Calcula o desvio padrão amostral."""
    return variancia_amostral(dados) ** 0.5


def percentil(dados, p):
    """
    Calcula um percentil usando interpolação linear.

    p deve estar entre 0 e 100.
    """
    valores = sorted(_validar_dados(dados))

    if p < 0 or p > 100:
        raise ValueError("O percentil deve estar entre 0 e 100.")

    n = len(valores)

    if n == 1:
        return valores[0]

    posicao = (p / 100) * (n - 1)

    inferior = int(posicao)
    superior = inferior + 1

    if superior >= n:
        return valores[inferior]

    fracao = posicao - inferior

    return (
        valores[inferior]
        + fracao * (valores[superior] - valores[inferior])
    )


def quartis(dados):
    """Retorna primeiro, segundo e terceiro quartis."""
    q1 = percentil(dados, 25)
    q2 = percentil(dados, 50)
    q3 = percentil(dados, 75)

    return q1, q2, q3


def coeficiente_variacao(dados, amostral=True):
    """Calcula o coeficiente de variação em porcentagem."""
    valores = _validar_dados(dados)

    m = media(valores)

    if m == 0:
        raise ValueError(
            "Não é possível calcular o coeficiente de variação "
            "quando a média é zero."
        )

    if amostral:
        desvio = desvio_padrao_amostral(valores)
    else:
        desvio = desvio_padrao_populacional(valores)

    return (desvio / abs(m)) * 100


def covariancia(dados_x, dados_y, amostral=True):
    """Calcula a covariância entre duas variáveis."""
    x = _validar_dados(dados_x)
    y = _validar_dados(dados_y)

    if len(x) != len(y):
        raise ValueError(
            "As duas listas devem possuir o mesmo tamanho."
        )

    if amostral and len(x) < 2:
        raise ValueError(
            "A covariância amostral exige pelo menos dois pares."
        )

    media_x = media(x)
    media_y = media(y)

    soma = 0

    for i in range(len(x)):
        soma += (x[i] - media_x) * (y[i] - media_y)

    if amostral:
        return soma / (len(x) - 1)

    return soma / len(x)


def correlacao_pearson(dados_x, dados_y):
    """Calcula o coeficiente de correlação de Pearson."""
    x = _validar_dados(dados_x)
    y = _validar_dados(dados_y)

    if len(x) != len(y):
        raise ValueError(
            "As duas listas devem possuir o mesmo tamanho."
        )

    if len(x) < 2:
        raise ValueError(
            "A correlação exige pelo menos dois pares de valores."
        )

    media_x = media(x)
    media_y = media(y)

    soma_xy = 0
    soma_x2 = 0
    soma_y2 = 0

    for i in range(len(x)):

        diferenca_x = x[i] - media_x
        diferenca_y = y[i] - media_y

        soma_xy += diferenca_x * diferenca_y
        soma_x2 += diferenca_x ** 2
        soma_y2 += diferenca_y ** 2

    denominador = (soma_x2 * soma_y2) ** 0.5

    if denominador == 0:
        raise ValueError(
            "Não é possível calcular correlação "
            "quando uma variável não possui variação."
        )

    return soma_xy / denominador


# Regressão linear simples pelo método dos mínimos quadrados

def regressao_linear(dados_x, dados_y):
    """
    Calcula a regressão linear simples.

    Retorna:
    a = intercepto
    b = inclinação
    r2 = coeficiente de determinação
    """
    x = _validar_dados(dados_x)
    y = _validar_dados(dados_y)

    if len(x) != len(y):
        raise ValueError(
            "As duas listas devem possuir o mesmo tamanho."
        )

    if len(x) < 2:
        raise ValueError(
            "A regressão exige pelo menos dois pares de valores."
        )

    media_x = media(x)
    media_y = media(y)

    numerador = 0
    denominador = 0

    for i in range(len(x)):
        numerador += (x[i] - media_x) * (y[i] - media_y)
        denominador += (x[i] - media_x) ** 2

    if denominador == 0:
        raise ValueError(
            "Não é possível realizar regressão com X constante."
        )

    b = numerador / denominador
    a = media_y - b * media_x

    r = correlacao_pearson(x, y)
    r2 = r ** 2

    return a, b, r2


def prever(x, intercepto, inclinacao):
    """Realiza uma predição usando a equação da reta."""
    return intercepto + inclinacao * x