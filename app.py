import streamlit as st
import pandas as pd
import plotly.express as px
car_data = pd.read_csv('vehicles_us.csv') 
hist_button = st.button('Construir histograma') 
if hist_button:
    st.write('Histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
dis_button = st.button('Construir diagrama de dispersion') 
if hist_button:
    st.write('Diagrama de dispersion para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)