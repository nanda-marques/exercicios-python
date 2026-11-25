import streamlit as st

# módulos das páginas
import atividades.AE2.Aula06.meu_app.home as home
import atividades.AE2.Aula06.meu_app.analise as analise
import atividades.AE2.Aula06.meu_app.graficos as graficos
import atividades.AE2.Aula06.meu_app.sobre as sobre

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