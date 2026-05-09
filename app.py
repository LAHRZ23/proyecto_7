import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Leer datos
car_data = pd.read_csv('vehicles_us.csv')

# Título de la app
st.header('Análisis de vehículos')

st.write('Muestra de Datos de vehículos en U.S.A. 🚗')
st.dataframe(car_data.head(20))

# HISTOGRAMA

st.write('Kilometraje de vehículos 🚗')

hist_button = st.button('Construir histograma')

if hist_button:

    st.write('Distribución del kilometraje de los vehículos')

    fig_hist = go.Figure(
        data=[go.Histogram(x=car_data['odometer'])]
    )

    fig_hist.update_layout(
        title='Distribución del Odómetro',
        xaxis_title='Kilometraje',
        yaxis_title='Cantidad de vehículos'
    )

    st.plotly_chart(fig_hist, use_container_width=True)


# GRÁFICA DE DISPERSIÓN

st.write('Precio por Kilometraje 🌟 ✖️ 🚗')

build_scatter = st.button('Construir gráfica de dispersión')

if build_scatter:

    st.write('Relación entre Kilometraje y precio')

    fig_scatter = go.Figure(
        data=[go.Scatter(
            x=car_data['odometer'],
            y=car_data['price'],
            mode='markers',
            marker_color='red'
        )]
    )

    fig_scatter.update_layout(
        title='Odómetro vs Precio',
        xaxis_title='Kilometraje',
        yaxis_title='Precio'
    )

    st.plotly_chart(fig_scatter, use_container_width=True)

# BOXPLOT CONDICIÓN VS PRECIO

st.write('Condición por Precio💲 ✖️ 🚗')

build_boxplot = st.checkbox('Comparar condición y precio')

if build_boxplot:

    st.write('Relación entre la condición del vehículo y su precio')

    fig_box = go.Figure()

    fig_box.add_trace(
        go.Box(
            x=car_data['condition'],
            y=car_data['price'],
            marker_color='seagreen'
        )
    )

    fig_box.update_layout(
        title='Condición del vehículo vs Precio',
        xaxis_title='Condición',
        yaxis_title='Precio'
    )

    st.plotly_chart(fig_box, use_container_width=True)
