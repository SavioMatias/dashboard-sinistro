import pandas as pd


def calcular_kpis(df):
    """Calcula os principais KPIs do dashboard."""

    total_sinistros = df["id_sinistro"].nunique()

    prejuizo_total = df["valor_prejuizo"].sum()

    tempo_medio = df["tempo_resolucao_dias"].mean()

    percentual_finalizados = ((df["status"] == "Finalizado").mean() * 100
    )

    return {
        "total_sinistros": total_sinistros,
        "prejuizo_total": prejuizo_total,
        "tempo_medio": tempo_medio,
        "percentual_finalizados": percentual_finalizados,
    }