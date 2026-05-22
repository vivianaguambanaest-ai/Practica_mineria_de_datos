import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# =========================================
# TITULO
# =========================================

st.title("Proyecto SEMMA con Datos de Estudiantes")

st.markdown("## 📚 DATOS DE ESTUDIANTES")

st.write("""
Este proyecto aplica la metodología SEMMA
para analizar información académica de estudiantes
correspondientes a dos períodos.
""")

# =========================================
# CARGA DE ARCHIVOS
# =========================================

archivo1 = st.file_uploader(
    "Subir archivo Excel 1",
    type=["xls", "xlsx"]
)

archivo2 = st.file_uploader(
    "Subir archivo Excel 2",
    type=["xls", "xlsx"]
)

# =========================================
# SI EXISTEN LOS DOS ARCHIVOS
# =========================================

if archivo1 and archivo2:

    # Leer archivos
    df1 = pd.read_excel(archivo1)
    df2 = pd.read_excel(archivo2)

    # Unir datasets
    df = pd.concat([df1, df2], ignore_index=True)

    # =====================================
    # 1. SAMPLE
    # =====================================

    st.header("1️⃣ SAMPLE - Recolección de Datos")

    st.write("Primeras filas del dataset")

    st.dataframe(df.head())

    st.write("Dimensiones del dataset")

    st.write(df.shape)

    # =====================================
    # 2. EXPLORE
    # =====================================

    st.header("2️⃣ EXPLORE - Exploración de Datos")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Tipos de datos")

        st.write(df.dtypes)

    with col2:

        st.subheader("Valores nulos")

        st.write(df.isnull().sum())

    st.subheader("Estadísticas descriptivas")

    st.write(df.describe())

    # =====================================
    # 3. MODIFY
    # =====================================

    st.header("3️⃣ MODIFY - Limpieza y Transformación")

    # Eliminar duplicados
    df = df.drop_duplicates()
    
    # Rellenar nulos en vez de eliminar todo
    df = df.fillna("Sin dato")

    st.success("Datos limpiados correctamente")

    st.write("Nueva dimensión del dataset")

    st.write(df.shape)

    # =====================================
    # 4. MODEL
    # =====================================

    st.header("4️⃣ MODEL - Visualización de Datos")

    columnas_numericas = df.select_dtypes(include="number").columns

    if len(columnas_numericas) > 0:

        columna = st.selectbox(
            "Selecciona una columna numérica",
            columnas_numericas
        )

        fig, ax = plt.subplots(figsize=(8,5))

        ax.hist(df[columna], bins=10)

        ax.set_title(f"Distribución de {columna}")

        st.pyplot(fig)

    # =====================================
    # GRAFICO DE CARRERAS
    # =====================================

    if "nombre_carrera" in df.columns:

        st.subheader("📊 Carreras con más estudiantes")

        fig3, ax3 = plt.subplots(figsize=(10,5))

        carreras = df["nombre_carrera"].value_counts().head(10)

        if not carreras.empty:

         carreras.plot(
         kind="bar",
         ax=ax3
         )

         st.pyplot(fig3)

        else:
         st.warning("No hay datos para mostrar")

    st.pyplot(fig3)

    # =====================================
    # 5. ASSESS
    # =====================================

    st.header("5️⃣ ASSESS - Evaluación")

    st.write("""
    ✅ Se cargaron correctamente los datos.

    ✅ Se realizó exploración y limpieza.

    ✅ Se analizaron variables académicas.

    ✅ Se visualizaron las carreras con más estudiantes.
    """)