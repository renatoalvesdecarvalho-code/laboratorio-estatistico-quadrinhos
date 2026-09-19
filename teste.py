import pandas as pd

dados = pd.read_csv("comic_books_10000_dataset.csv")

print("Tamanho do dataset:", dados.shape)
print("Colunas:", dados.columns.tolist())

print("Tipos das colunas:")
print(dados.dtypes)

print("Colunas numéricas:")
print(dados.select_dtypes(include="number").columns.tolist())

print(dados[["Release Year", "Page Count", "Rating (out of 10)", "Volume Count"]].isnull().sum())

print(dados["Release Year"].min(), dados["Release Year"].max())

print(dados["Page Count"].min(), dados["Page Count"].max())

print(dados["Rating (out of 10)"].min(), dados["Rating (out of 10)"].max())

print(dados["Volume Count"].min(), dados["Volume Count"].max())

print(dados["Genre"].unique())

print(dados["Format"].unique())

print(dados["Format"].value_counts())

print(dados["Format"].value_counts().head(1))

print(dados["Country of Origin"].value_counts())

print(dados["Country of Origin"].value_counts().head(1))

print(dados["Page Count"].mean())

print(dados["Page Count"].median())

print(dados["Rating (out of 10)"].mean())

print(dados["Rating (out of 10)"].median())

print(dados["Volume Count"].mean())

print(dados["Volume Count"].median())

print(dados["Release Year"].mean())

print(dados["Release Year"].median())

print(dados["Rating (out of 10)"].std())

print(dados["Page Count"].std())

print(dados["Genre"].value_counts().head(10))

print(dados["Studio/Publisher"].value_counts().head(10))

print(dados["Age Rating"].value_counts())

print(dados["Language"].value_counts())

print(dados["Status"].value_counts())

print(dados["Awards"].value_counts().head(10))

print(dados.nlargest(10, "Rating (out of 10)")[["Title", "Rating (out of 10)"]])

print(dados.nlargest(10, "Page Count")[["Title", "Page Count"]])

print(dados.nlargest(10, "Volume Count")[["Title", "Volume Count"]])

print(dados.groupby("Format")["Rating (out of 10)"].mean().sort_values(ascending=False))

print(dados.groupby("Country of Origin")["Rating (out of 10)"].mean().sort_values(ascending=False).head(10))

print(dados.groupby("Country of Origin")["Page Count"].mean().sort_values(ascending=False).head(10))

print(dados.groupby("Release Year")["Rating (out of 10)"].mean().tail(10))

print(dados["Page Count"].corr(dados["Rating (out of 10)"]))

print(dados["Volume Count"].corr(dados["Rating (out of 10)"]))

print(dados["Release Year"].corr(dados["Rating (out of 10)"]))

import matplotlib.pyplot as plt
dados["Format"].value_counts().head(10).plot(kind="bar")
plt.title("10 formatos mais frequentes")
plt.xlabel("Formato")
plt.ylabel("Quantidade")
plt.xticks(rotation=45, ha="right")
plt.close()
# Gráfico 2 - Países de origem mais frequentes
dados["Country of Origin"].value_counts().head(10).plot(kind="bar")
plt.title("10 países de origem mais frequentes")
plt.xlabel("País")
plt.ylabel("Quantidade")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.close()

# Gráfico 3 - Média de avaliação por ano
dados.groupby("Release Year")["Rating (out of 10)"].mean().plot()
plt.title("Média de avaliação por ano")
plt.xlabel("Ano de lançamento")
plt.ylabel("Avaliação média")
plt.tight_layout()
plt.close()

# Gráfico 4 - Relação entre número de páginas e avaliação
dados.plot.scatter(x="Page Count", y="Rating (out of 10)")
plt.title("Número de páginas x avaliação")
plt.xlabel("Número de páginas")
plt.ylabel("Avaliação")
plt.tight_layout()
plt.close()
# ============================================================
# ANÁLISES COMPLEMENTARES
# ============================================================

print("\n--- RESUMO ESTATÍSTICO ---")
print(dados[["Release Year", "Page Count", "Rating (out of 10)", "Volume Count"]].describe())

print("\n--- 10 GÊNEROS MAIS FREQUENTES ---")
print(dados["Genre"].value_counts().head(10))

print("\n--- 10 IDIOMAS MAIS FREQUENTES ---")
print(dados["Language"].value_counts().head(10))

print("\n--- DISTRIBUIÇÃO POR FAIXA ETÁRIA ---")
print(dados["Age Rating"].value_counts())

print("\n--- DISTRIBUIÇÃO POR STATUS ---")
print(dados["Status"].value_counts())

print("\n--- 10 QUADRINHOS COM MAIOR AVALIAÇÃO ---")
print(
    dados.nlargest(10, "Rating (out of 10)")[
        ["Title", "Rating (out of 10)"]
    ]
)

print("\n--- 10 QUADRINHOS COM MAIOR NÚMERO DE PÁGINAS ---")
print(
    dados.nlargest(10, "Page Count")[
        ["Title", "Page Count"]
    ]
)

print("\n--- 10 QUADRINHOS COM MAIOR NÚMERO DE VOLUMES ---")
print(
    dados.nlargest(10, "Volume Count")[
        ["Title", "Volume Count"]
    ]
)
# ============================================================
# SALVANDO GRÁFICOS EM ARQUIVOS PNG
# ============================================================

# Gráfico 1 - 10 formatos mais frequentes
dados["Format"].value_counts().head(10).plot(kind="bar")
plt.title("10 formatos mais frequentes")
plt.xlabel("Formato")
plt.ylabel("Quantidade")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("grafico_formatos.png")
plt.close()

# Gráfico 2 - 10 países de origem mais frequentes
dados["Country of Origin"].value_counts().head(10).plot(kind="bar")
plt.title("10 países de origem mais frequentes")
plt.xlabel("País")
plt.ylabel("Quantidade")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("grafico_paises.png")
plt.close()

# Gráfico 3 - Média de avaliação por ano
dados.groupby("Release Year")["Rating (out of 10)"].mean().plot()
plt.title("Média de avaliação por ano")
plt.xlabel("Ano de lançamento")
plt.ylabel("Avaliação média")
plt.tight_layout()
plt.savefig("grafico_avaliacao_ano.png")
plt.close()

# Gráfico 4 - Número de páginas x avaliação
dados.plot.scatter(
    x="Page Count",
    y="Rating (out of 10)"
)
plt.title("Número de páginas x avaliação")
plt.xlabel("Número de páginas")
plt.ylabel("Avaliação")
plt.tight_layout()
plt.savefig("grafico_paginas_avaliacao.png")
plt.close()

print("\nGráficos salvos com sucesso!")
# ============================================================
# ANÁLISE DE RELAÇÕES ENTRE VARIÁVEIS
# ============================================================

print("\n--- CORRELAÇÕES ENTRE VARIÁVEIS NUMÉRICAS ---")

correlacoes = dados[
    ["Release Year", "Page Count", "Rating (out of 10)", "Volume Count"]
].corr()

print(correlacoes)

print("\n--- MÉDIA DE AVALIAÇÃO POR STATUS ---")
print(
    dados.groupby("Status")["Rating (out of 10)"]
    .mean()
    .sort_values(ascending=False)
)

print("\n--- MÉDIA DE AVALIAÇÃO POR FAIXA ETÁRIA ---")
print(
    dados.groupby("Age Rating")["Rating (out of 10)"]
    .mean()
    .sort_values(ascending=False)
)

print("\n--- 10 EDITORAS COM MAIOR MÉDIA DE AVALIAÇÃO ---")
print(
    dados.groupby("Studio/Publisher")["Rating (out of 10)"]
    .agg(["mean", "count"])
    .sort_values("mean", ascending=False)
    .head(10)
)

print("\n--- QUANTIDADE DE OBRAS POR ANO - ÚLTIMOS 10 ANOS ---")
print(
    dados["Release Year"]
    .value_counts()
    .sort_index()
    .tail(10)
)

print("\nAnálises de relações concluídas com sucesso!")
# ============================================================
# RESUMO FINAL DOS DADOS
# ============================================================

print("\n" + "=" * 60)
print("RESUMO FINAL DA ANÁLISE")
print("=" * 60)

print("\nQuantidade total de registros:")
print(len(dados))

print("\nQuantidade de gêneros diferentes:")
print(dados["Genre"].nunique())

print("\nQuantidade de formatos diferentes:")
print(dados["Format"].nunique())

print("\nFormato mais frequente:")
print(dados["Format"].value_counts().head(1))

print("\nPaís de origem mais frequente:")
print(dados["Country of Origin"].value_counts().head(1))

print("\nMédia de páginas:")
print(round(dados["Page Count"].mean(), 2))

print("\nMediana de páginas:")
print(dados["Page Count"].median())

print("\nAvaliação média:")
print(round(dados["Rating (out of 10)"].mean(), 2))

print("\nMediana das avaliações:")
print(dados["Rating (out of 10)"].median())

print("\nMédia do número de volumes:")
print(round(dados["Volume Count"].mean(), 2))

print("\nAno médio de lançamento:")
print(round(dados["Release Year"].mean(), 0))

print("\nQuadrinho com maior avaliação:")
print(
    dados.nlargest(1, "Rating (out of 10)")[
        ["Title", "Rating (out of 10)"]
    ]
)

print("\nQuadrinho com maior número de páginas:")
print(
    dados.nlargest(1, "Page Count")[
        ["Title", "Page Count"]
    ]
)

print("\nQuadrinho com maior número de volumes:")
print(
    dados.nlargest(1, "Volume Count")[
        ["Title", "Volume Count"]
    ]
)

print("\n" + "=" * 60)
print("ANÁLISE FINALIZADA COM SUCESSO")
print("=" * 60)