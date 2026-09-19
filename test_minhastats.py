import math
import statistics

import numpy as np

import minhastats as ms


# ============================================================
# TESTES AUTOMATIZADOS DA BIBLIOTECA MINHASTATS
# ============================================================
#
# As funções implementadas em minhastats.py são comparadas
# com funções de referência do Python/NumPy.
#
# Tolerância numérica adotada:
# rel_tol = 1e-9
# abs_tol = 1e-9
#
# Essa tolerância permite pequenas diferenças decorrentes
# da representação de números de ponto flutuante.
# ============================================================

REL_TOL = 1e-9
ABS_TOL = 1e-9

dados = [10, 20, 30, 40, 50]
dados_moda = [10, 20, 20, 30, 40]
dados2 = [2, 4, 6, 8, 10]


def verificar(nome, obtido, esperado):
    """Compara dois resultados numéricos."""

    if math.isclose(
        obtido,
        esperado,
        rel_tol=REL_TOL,
        abs_tol=ABS_TOL
    ):
        print(f"[OK] {nome}")
    else:
        raise AssertionError(
            f"{nome}: obtido={obtido}, esperado={esperado}"
        )


print("=" * 60)
print("VALIDAÇÃO AUTOMATIZADA DA BIBLIOTECA MINHASTATS")
print("=" * 60)


# ============================================================
# MÉDIA
# ============================================================

verificar(
    "Média",
    ms.media(dados),
    np.mean(dados)
)


# ============================================================
# MEDIANA
# ============================================================

verificar(
    "Mediana",
    ms.mediana(dados),
    np.median(dados)
)


# ============================================================
# MODA
# ============================================================

moda_obtida = ms.moda(dados_moda)
moda_esperada = [statistics.mode(dados_moda)]

if moda_obtida == moda_esperada:
    print("[OK] Moda")
else:
    raise AssertionError(
        f"Moda: obtido={moda_obtida}, esperado={moda_esperada}"
    )


# ============================================================
# AMPLITUDE
# ============================================================

verificar(
    "Amplitude",
    ms.amplitude(dados),
    np.ptp(dados)
)


# ============================================================
# VARIÂNCIA POPULACIONAL
# ============================================================

verificar(
    "Variância populacional",
    ms.variancia_populacional(dados),
    np.var(dados, ddof=0)
)


# ============================================================
# VARIÂNCIA AMOSTRAL
# ============================================================

verificar(
    "Variância amostral",
    ms.variancia_amostral(dados),
    np.var(dados, ddof=1)
)


# ============================================================
# DESVIO PADRÃO POPULACIONAL
# ============================================================

verificar(
    "Desvio padrão populacional",
    ms.desvio_padrao_populacional(dados),
    np.std(dados, ddof=0)
)


# ============================================================
# DESVIO PADRÃO AMOSTRAL
# ============================================================

verificar(
    "Desvio padrão amostral",
    ms.desvio_padrao_amostral(dados),
    np.std(dados, ddof=1)
)


# ============================================================
# PERCENTIS
# ============================================================

for p in [25, 50, 75]:

    verificar(
        f"Percentil {p}",
        ms.percentil(dados, p),
        np.percentile(dados, p)
    )


# ============================================================
# QUARTIS
# ============================================================

q1, q2, q3 = ms.quartis(dados)

quartis_numpy = np.percentile(
    dados,
    [25, 50, 75]
)

verificar(
    "Quartil Q1",
    q1,
    quartis_numpy[0]
)

verificar(
    "Quartil Q2",
    q2,
    quartis_numpy[1]
)

verificar(
    "Quartil Q3",
    q3,
    quartis_numpy[2]
)


# ============================================================
# COEFICIENTE DE VARIAÇÃO
# ============================================================

cv_esperado = (
    np.std(dados, ddof=1)
    / abs(np.mean(dados))
) * 100

verificar(
    "Coeficiente de variação",
    ms.coeficiente_variacao(dados),
    cv_esperado
)


# ============================================================
# COVARIÂNCIA
# ============================================================

cov_numpy = np.cov(
    dados,
    dados2,
    ddof=1
)[0, 1]

verificar(
    "Covariância",
    ms.covariancia(dados, dados2),
    cov_numpy
)


# ============================================================
# CORRELAÇÃO DE PEARSON
# ============================================================

pearson_numpy = np.corrcoef(
    dados,
    dados2
)[0, 1]

verificar(
    "Correlação de Pearson",
    ms.correlacao_pearson(dados, dados2),
    pearson_numpy
)


# ============================================================
# REGRESSÃO LINEAR
# ============================================================

intercepto, inclinacao, r2 = ms.regressao_linear(
    dados,
    dados2
)

inclinacao_numpy, intercepto_numpy = np.polyfit(
    dados,
    dados2,
    1
)

r_numpy = np.corrcoef(
    dados,
    dados2
)[0, 1]

r2_numpy = r_numpy ** 2

verificar(
    "Regressão - intercepto",
    intercepto,
    intercepto_numpy
)

verificar(
    "Regressão - inclinação",
    inclinacao,
    inclinacao_numpy
)

verificar(
    "Regressão - R²",
    r2,
    r2_numpy
)


# ============================================================
# PREDIÇÃO
# ============================================================

x_predicao = 60

previsao_obtida = ms.prever(
    x_predicao,
    intercepto,
    inclinacao
)

previsao_esperada = (
    intercepto_numpy
    + inclinacao_numpy * x_predicao
)

verificar(
    "Predição",
    previsao_obtida,
    previsao_esperada
)


# ============================================================
# RESULTADO FINAL
# ============================================================

print()
print("=" * 60)
print("TODOS OS TESTES FORAM CONCLUÍDOS COM SUCESSO")
print("=" * 60)