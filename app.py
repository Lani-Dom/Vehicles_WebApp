import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # Leer datos

# Encabezado
st.header('Aplicación web - Anuncios de ventas de autos')

# Botón para histograma
hist_button = st.button('Construir histograma')

# Si se hace clic en el botón
if hist_button: 
    st.write('Histograma para datos de anuncios de venta de coches (relación kilometraje y cantidad)')
    
    # Histograma
    fig = px.histogram(car_data, x="odometer") 

    # Despliegue
    st.plotly_chart(fig, use_container_width=True) 



# Botón para gráfico de dispersión
disp_button = st.button('Construir gráfico de dispersión') 

# Si se hace clic en el botón
if disp_button: 
    st.write('Gráfico de dispersión para datos de anuncios de venta de coches (relación kilometraje y precio)')
    
    # Gráfico de dispersión
    fig2 = px.scatter(car_data, x="odometer", y="price") 

    # Despliegue
    st.plotly_chart(fig2, use_container_width=True) 
