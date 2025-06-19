"""Proyecto de ejemplo para crear un histograma interactivo con Streamlit y Plotly"""

import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

# Selector de color
color_option = st.selectbox(
    'Selecciona el color para los gráficos',
    ['blue', 'green', 'red', 'orange', 'purple', 'gray']
)

# Casillas de verificación
show_hist = st.checkbox('Mostrar histograma')
show_scatter = st.checkbox('Mostrar gráfico de dispersión')

# Histograma
if show_hist:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig_hist = px.histogram(car_data, x="odometer",
                            color_discrete_sequence=[color_option])
    st.plotly_chart(fig_hist, use_container_width=True)

# Gráfico de dispersión
if show_scatter:
    st.write('Creación de un gráfico de dispersión: precio vs. odómetro')
    fig_scatter = px.scatter(car_data, x="odometer", y="price",
                             title="Relación entre kilometraje y precio",
                             color_discrete_sequence=[color_option])
    st.plotly_chart(fig_scatter, use_container_width=True)
