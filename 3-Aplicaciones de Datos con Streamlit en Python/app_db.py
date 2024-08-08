import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('mi_base_de_datos.db')

query_clientes = "SELECT * FROM clientes"
df_clientes = pd.read_sql(query_clientes, conn)
query_compras = "SELECT * FROM compras"
df_compras = pd.read_sql(query_compras, conn)

st.title('Búsqueda de información de compras')
st.write('Ingrese el ID de la compra a buscar:')
cod_compra = st.text_input(label='Código de compra')
if st.button('Buscar'):
    df_compra_filtrado = df_compras.loc[df_compras['id_compra'] == int(cod_compra)]
    if not df_compra_filtrado.empty:
        df_cliente_filtrado = df_clientes.loc[df_clientes['id_cliente'] == df_compra_filtrado.iloc[0]['id_cliente']]
        st.write(f"ID Compra: {df_compra_filtrado.iloc[0]['id_compra']}")
        st.write(f"Fecha compra: {df_compra_filtrado.iloc[0]['fecha_compra']}")
        st.write(f"ID Cliente: {df_cliente_filtrado.iloc[0]['id_cliente']}")
        st.write(f"Nombre Cliente: {df_cliente_filtrado.iloc[0]['nombre_cliente']}")
    else:
        st.warning('Código de compra no encontrado.')

st.write(df_compras)