import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Mi Primera Aplicación de Datos')

datafile = st.file_uploader('Cargar archivo CSV', type='csv')
if datafile:
    df = pd.read_csv(datafile)

if 'df' in locals():
    st.write(df)

    st.subheader('Visualizacione Básica de Bitcoin')
    # Grafico linea
    fig, axs = plt.subplots(figsize=(10, 8))
    df.set_index('Date')['Close'].plot(kind='line', ax=axs)

    st.pyplot(fig)
