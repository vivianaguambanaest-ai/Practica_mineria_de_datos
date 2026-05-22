import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt 
st.title("Metodologias para el proceso de Mineria de Datos")
st.write("Practica 1")
#Dataframe de productos
data = {
    "Producto": ["Laptop", "Smartphone", "Tablet", "Monitor", "Teclado"],
    "Precio": [1000, 500, 300, 200, 50],
    "Cantidad": [10, 20, 15, 5, 30]
}
df=pd.DataFrame(data)
st.subheader("DataFrame de Productos")
st.dataframe(df)
st.write("Graficas")
st.header("Gráfica de Precios de Productos")
fig, ax = plt.subplots()
ax.bar(df["Producto"], df["Precio"], color="blue")
ax.set_xlabel("Producto")
ax.set_title("Precios de Productos")
st.pyplot(fig)

st.header("Gráfica de Cantidad de Productos")

fig, ax = plt.subplots()
ax.bar(df["Producto"], df["Cantidad"], color="green")

ax.set_xlabel("Producto")
ax.set_ylabel("Cantidad")
ax.set_title("Cantidad de Productos")

st.pyplot(fig)
