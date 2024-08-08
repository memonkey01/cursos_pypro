import streamlit as st
import pandas as pd
import plotly.express as px
from faker import Faker
import random
from datetime import datetime, timedelta

# Generar datos dummy
def generate_dummy_data():
    fake = Faker()

    # Datos para clientes
    clientes = []
    for _ in range(100):
        clientes.append({
            'id_cliente': _ + 1,
            'nombre_cliente': fake.name(),
            'fecha_creacion': fake.date_between(start_date='-5y', end_date='today').strftime('%Y-%m-%d'),
            'tipo_cliente': random.choice(['Regular', 'Premium', 'VIP'])
        })

    # Datos para compras
    compras = []
    for _ in range(1000):
        compras.append({
            'id_compra': _ + 1,
            'id_cliente': random.choice(range(1, 101)),
            'nombre_item': fake.word(),
            'fecha_compra': fake.date_between(start_date='-5y', end_date='today').strftime('%Y-%m-%d'),
            'precio_venta': round(random.uniform(5.0, 500.0), 2),
            'descuento': round(random.uniform(0.0, 50.0), 2)
        })

    return pd.DataFrame(clientes), pd.DataFrame(compras)

# Crear los datos
clientes_df, compras_df = generate_dummy_data()

# Iniciar la aplicación de Streamlit
st.title("Aplicación Interactiva con Streamlit y Plotly")
st.write("Esta aplicación muestra datos ficticios de clientes y compras.")

# Mostrar los datos en tablas
st.header("Datos de Clientes")
st.dataframe(clientes_df)

st.header("Datos de Compras")
st.dataframe(compras_df)

# Seleccionar tipo de gráfico
st.header("Visualización de Datos")
chart_type = st.selectbox("Seleccione el tipo de gráfico", ["Barras", "Líneas", "Dispersión"])

# Filtrar datos por tipo de cliente
tipo_cliente = st.selectbox("Seleccione el tipo de cliente", clientes_df['tipo_cliente'].unique())

# Filtrar las compras según el tipo de cliente seleccionado
filtered_data = compras_df[compras_df['id_cliente'].isin(clientes_df[clientes_df['tipo_cliente'] == tipo_cliente]['id_cliente'])]

# Crear gráfico interactivo con Plotly
if chart_type == "Barras":
    fig = px.bar(filtered_data, x='fecha_compra', y='precio_venta', title=f'Compras de Clientes {tipo_cliente}')
elif chart_type == "Líneas":
    fig = px.line(filtered_data.groupby('fecha_compra').sum().reset_index(), x='fecha_compra', y='precio_venta', title=f'Compras de Clientes {tipo_cliente}')
elif chart_type == "Dispersión":
    fig = px.scatter(filtered_data, x='fecha_compra', y='precio_venta', title=f'Compras de Clientes {tipo_cliente}')

st.plotly_chart(fig)
