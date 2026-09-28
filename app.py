import streamlit as st
import pandas as pd

from src.graficos import (
    criar_grafico_estados,
    criar_grafico_gravidade,
    criar_grafico_tipo_sinistro,
    criar_grafico_evolucao_mensal
)

# Configuração da página
st.set_page_config(
    page_title="Dashboard de Sinistros",
    layout="wide"
)


# Carregamento dos dados
@st.cache_data
def carregar_dados():
    try:
        return pd.read_csv("sinistros_tratado.csv")
    except FileNotFoundError:
        return pd.read_csv("data/sinistros_tratado.csv")


df = carregar_dados()


# =========================================================
# TÍTULO
# =========================================================

st.title("🚗 Dashboard Inteligente de Sinistros")


# =========================================================
# FILTROS
# =========================================================

with st.sidebar:

    st.header("Filtros")

    estado = st.multiselect(
        "Estado",
        options=sorted(df["estado"].dropna().unique())
    )

    gravidade = st.multiselect(
        "Gravidade",
        options=sorted(df["gravidade"].dropna().unique())
    )


# =========================================================
# APLICAÇÃO DOS FILTROS
# =========================================================

df_filtrado = df.copy()

if estado:
    df_filtrado = df_filtrado[
        df_filtrado["estado"].isin(estado)
    ]

if gravidade:
    df_filtrado = df_filtrado[
        df_filtrado["gravidade"].isin(gravidade)
    ]


# =========================================================
# KPIs
# =========================================================

total_sinistros = df_filtrado.shape[0]

prejuizo_total = df_filtrado["valor_prejuizo"].sum()

tempo_medio = df_filtrado["tempo_resolucao_dias"].mean()

if total_sinistros > 0:
    percentual_finalizados = (
        df_filtrado[df_filtrado["status"] == "Finalizado"].shape[0]
        / total_sinistros
        * 100
    )
else:
    percentual_finalizados = 0


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "📄 Total de Sinistros",
        f"{total_sinistros}"
    )


with col2:
    st.metric(
        "💰 Prejuízo Total",
        f"R$ {prejuizo_total:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )


with col3:
    st.metric(
        "⏱ Tempo Médio",
        f"{tempo_medio:.1f} dias"
    )


with col4:
    st.metric(
        "✅ Percentual Finalizados",
        f"{percentual_finalizados:.2f}%"
    )


st.divider()


# =========================================================
# ANÁLISE TEMPORAL
# =========================================================

st.subheader("📈 Evolução dos Sinistros")

fig_evolucao = criar_grafico_evolucao_mensal(df_filtrado)

st.plotly_chart(
    fig_evolucao,
    use_container_width=True
)


# =========================================================
# ANÁLISE DETALHADA
# =========================================================

st.subheader("🔎 Análise Detalhada")


col_graf1, col_graf2 = st.columns(2)


with col_graf1:

    fig_estados = criar_grafico_estados(df_filtrado)

    st.plotly_chart(
        fig_estados,
        use_container_width=True
    )


with col_graf2:

    fig_gravidade = criar_grafico_gravidade(df_filtrado)

    st.plotly_chart(
        fig_gravidade,
        use_container_width=True
    )


# =========================================================
# TIPOS DE SINISTRO
# =========================================================

fig_tipo_sinistro = criar_grafico_tipo_sinistro(df_filtrado)

st.plotly_chart(
    fig_tipo_sinistro,
    use_container_width=True
)