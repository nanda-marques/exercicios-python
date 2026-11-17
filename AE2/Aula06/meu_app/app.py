import streamlit as st

# módulos das páginas
import home
import analise
import graficos
import sobre

st.sidebar.title("Menu")
pagina = st.sidebar.selectbox("Escolha a página: ", ["Home", "Análise", "Gráficos", "Sobre"])

if pagina == "Home":
    home.app()

elif pagina == "Análise":
    analise.app()

elif pagina == "Gráficos":
    graficos.app()

elif pagina == "Sobre":
    sobre.app()