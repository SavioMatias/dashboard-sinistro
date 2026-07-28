import streamlit as st

st.set_page_config (
    page_title="Dashboard Inteligente de Sinistros",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Dashboard Inteligente de Sinistros")

st.write("Projeto desenvolvido por Sávio Matias")

st.markdown("---")

st.subheader("Bem-vindo!")

st.write(
    """
    Este dashboard tem como objetivo acompanhar indicadores
    relacionados aos sinistros da frota, auxiliando gestores
    na tomada de decisão.
    """
)