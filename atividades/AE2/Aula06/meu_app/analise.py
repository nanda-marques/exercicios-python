import streamlit as st
import pandas as pd

def app():
    st.title("Análise de Dados")
    st.write("Estatística e Tabelas")

    df = pd.DataFrame({"Produto":["A", "B", "C"], "Vendas":[100, 200, 150]})

    st.dataframe(df)
    st.write("Estatísticas: ")
    st.write(df.describe())