import plotly.express as px
import pandas as pd

def criar_grafico_estados(df):
    """Gera um gráfico de barras com o volume de sinistros por estado."""
    df_agrupado = df['estado'].value_counts().reset_index()
    df_agrupado.columns = ['Estado', 'Quantidade']
    
    fig = px.bar(
        df_agrupado, 
        x='Estado', 
        y='Quantidade', 
        title='Volume de Sinistros por Estado',
        color='Quantidade',
        color_continuous_scale='Blues',
        text_auto=True
    )
    fig.update_layout(xaxis_title="", yaxis_title="Quantidade", showlegend=False)
    return fig

def criar_grafico_gravidade(df):
    """Gera um gráfico de rosca com o prejuízo por gravidade."""
    df_agrupado = df.groupby('gravidade')['valor_prejuizo'].sum().reset_index()
    
    fig = px.pie(
        df_agrupado, 
        values='valor_prejuizo', 
        names='gravidade', 
        title='Prejuízo Total por Gravidade',
        hole=0.4, # Isso transforma a pizza em uma rosca (donut)
        color_discrete_sequence=["#2563EB"]
    )
    return fig

def criar_grafico_tipo_sinistro(df):
    """Gera um gráfico de barras com o volume de sinistros por tipo."""
    # CORREÇÃO AQUI: Mudamos 'tipo_sinistro' para 'tipo_acidente'
    df_agrupado = df['tipo_acidente'].value_counts().reset_index()
    df_agrupado.columns = ['Tipo de Sinistro', 'Quantidade']
    
    fig = px.bar(
        df_agrupado, 
        x='Tipo de Sinistro', 
        y='Quantidade', 
        title='Volume de Sinistros por Tipo',
        color='Quantidade',
        color_continuous_scale='Blues',
        text_auto=True
    )
    fig.update_layout(xaxis_title="", yaxis_title="Quantidade", showlegend=False)
    return fig


def criar_grafico_evolucao_mensal(df):

    df = df.copy()

    df["data_abertura"] = pd.to_datetime(
        df["data_abertura"],
        errors="coerce"
    )

    df = df.dropna(subset=["data_abertura"])

    df["mes"] = (
        df["data_abertura"]
        .dt.to_period("M")
        .astype(str)
    )

    dados = (
        df.groupby("mes")
        .size()
        .reset_index(name="quantidade")
    )

    fig = px.line(
        dados,
        x="mes",
        y="quantidade",
        markers=True,
        text="quantidade",
        labels={
            "mes": "Mês",
            "quantidade": "Quantidade de Sinistros"
        }
    )

    fig.update_traces(
        textposition="top center"
    )

    fig.update_layout(
        height=400,
        xaxis_title="",
        yaxis_title="Quantidade",
        margin=dict(
            l=20,
            r=20,
            t=40,
            b=20
        )
    )

    return fig
