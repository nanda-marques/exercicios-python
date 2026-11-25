import streamlit as st
import pandas as pd

def app():
    st.title("Gráficos")

    df = pd.DataFrame({"Dia":[1, 2, 3, 4], "Vendas":[10, 20, 30, 15]})

    st.line_chart(df["Vendas"])
    st.bar_chart(df["Vendas"])