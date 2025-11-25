import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")


fig, ax = plt.subplots()

col1,col2,col3 = st.columns([1,3,1])

col1.image("C:\\Users\\mandy\\OneDrive\\Desktop\\spyder\\logouprh.png",width=150)
col2.title("Datos de Covid - Variante Omicrón")
col3.image("C:\\Users\\mandy\\OneDrive\\Desktop\\spyder\\covid_1.png",width=150)

st.divider()

df_covid = pd.read_csv("https://raw.githubusercontent.com/elioramosweb/archivo_datos/main/datos_diarios-2022-03-22_10_20_15.csv",parse_dates=['date'])

nombres = list(df_covid.columns)[1:]

columna = st.sidebar.selectbox("Columna de interes", nombres)

suavizado = st.sidebar.checkbox("Suavizado")

tabla = st.sidebar.checkbox("Mostrar datos")

df_covid.plot(x="date",y=columna,
              ax=ax,
              xlabel="Fechas",
              ylabel=columna)

col1,col2 = st.columns(2)

if suavizado:
    ventana = st.sidebar.slider("Ventana de suavizado [dias]",1,15,7)
    df_rolling = df_covid[columna].rolling(ventana,center=True).mean()
    df_covid[columna+"_rolling"] = df_rolling
    df_covid.plot(x="date",y=columna+"_rolling",ax=ax)

if tabla:
    df_covid["date"] = df_covid["date"].dt.strftime("%d-%b-%Y")
    df_tabla = df_covid[["date",columna]]
    col2.write(df_tabla)

col1.pyplot(fig)

st.sidebar.divider()

st.sidebar.markdown("""Aplicación desarrollada por:<br><i>Amanda S. Ayala Cuadrado<br>
                    Comp3005<br>Universidad de Puerto Rico en Humacao</i>""",
                    unsafe_allow_html=True)
