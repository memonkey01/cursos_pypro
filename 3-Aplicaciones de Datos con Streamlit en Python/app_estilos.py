import streamlit as st
from PIL import Image

# Encabezado personalizado
st.set_page_config(page_title="Mi Aplicación de Datos", page_icon=":bar_chart:", layout="wide")

# Título de la UI
st.title("Aplicación de Datos")

# Subtítulo de la UI
st.subheader("Diseño y personalización de la interfaz gráfica en Streamlit")

# Siderbar
logo_pypro = Image.open('assets/pypro_logo_plot.png')
with st.sidebar:
    st.image(logo_pypro)

    st.title("Menú de Opciones")

    # Agregar sección
    st.sidebar.header("Configuración")

    # Agregar slider
    edad = st.sidebar.slider("Seleccione su edad:", 0, 100, 30)

    # Agregar selección
    color = st.sidebar.selectbox("Seleccione su color favorito:", ["Rojo", "Azul", "Verde"])

    # Agregar botón
    st.sidebar.button("Procesar Datos")

# Mostrar datos
st.write("Su edad es de:", edad)
st.write("Su color favorito es:", color)