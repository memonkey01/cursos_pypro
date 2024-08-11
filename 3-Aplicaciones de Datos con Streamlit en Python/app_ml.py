import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

# Cargar conjunto de datos Iris
iris = datasets.load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
Y = pd.DataFrame(iris.target, columns=["class"])

# Sidebar para configuración del modelo
st.sidebar.header("Configuración del modelo")
n_neighbors = st.sidebar.number_input("Número de vecinos:", 1, 50, 5, 1)
model = KNeighborsClassifier(n_neighbors=n_neighbors)
model.fit(X, Y)


# Interfaz de usuario para selección de características
st.header("Clasificador de tipos de flores Iris")
st.write("Selecciona los valores de las siguientes características:")
selected_features = []
for feature_name in X.columns:
    value = st.sidebar.slider(feature_name, float(X[feature_name].min()), float(X[feature_name].max()))
    selected_features.append(value)


# Botón de predicción
if st.button("Predecir"):
    prediction = model.predict([selected_features])
    st.write("El tipo de flor es:", iris.target_names[prediction][0])