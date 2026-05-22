import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# =========================================
# TITULO
# =========================================

st.title("Proyecto KDD con Datos de Estudiantes")

st.markdown("## 📚 DATOS DE ESTUDIANTES")

st.write("""
Este proyecto aplica la metodología KDD
(Knowledge Discovery in Databases)
para analizar información académica
de estudiantes.
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
# VALIDAR ARCHIVOS
# =========================================

if archivo1 and archivo2:

    # Leer archivos
    df1 = pd.read_excel(archivo1)
    df2 = pd.read_excel(archivo2)

    # Unir datasets
    df = pd.concat([df1, df2], ignore_index=True)

    # =====================================
    # 1. SELECTION
    # =====================================

    st.header("1️⃣ SELECTION - Selección de Datos")

    st.write("Primeras filas del dataset")

    st.dataframe(df.head())

    st.write("Dimensiones del dataset")

    st.write(df.shape)

    # =====================================
    # 2. PREPROCESSING
    # =====================================

    st.header("2️⃣ PREPROCESSING - Limpieza de Datos")

    st.subheader("Valores nulos")

    st.write(df.isnull().sum())

    # Eliminar duplicados
    df = df.drop_duplicates()

    # Rellenar valores nulos
    df = df.fillna("Sin dato")

    st.success("Datos limpiados correctamente")

    # =====================================
    # 3. TRANSFORMATION
    # =====================================

    st.header("3️⃣ TRANSFORMATION - Transformación de Datos")

    st.write("Tipos de datos")

    st.write(df.dtypes)

    # Codificación de variables categóricas
    encoder = LabelEncoder()

    if "sexo" in df.columns:

        df["sexo_codificado"] = encoder.fit_transform(df["sexo"])

        st.subheader("Codificación de la variable sexo")

        st.dataframe(
            df[["sexo", "sexo_codificado"]].head()
        )

    # =====================================
    # 4. DATA MINING
    # =====================================

    st.header("4️⃣ DATA MINING - Análisis de Datos")

    columnas_numericas = df.select_dtypes(
        include=["int64", "float64"]
    ).columns

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

    # =====================================
    # 5. INTERPRETATION
    # =====================================

    st.header("5️⃣ INTERPRETATION - Interpretación")

    st.write("""
    ✅ Se identificaron las carreras con mayor número de estudiantes.

    ✅ Se analizaron variables académicas y demográficas.

    ✅ Se transformaron variables categóricas para facilitar el análisis.
    """)

    # =====================================
    # 6. KNOWLEDGE
    # =====================================

    st.header("6️⃣ KNOWLEDGE - Conocimiento Obtenido")

    st.success("Proceso KDD completado correctamente")

    st.write("""
    ### Conclusiones

    - Los datos fueron integrados y limpiados correctamente.
    - La metodología KDD permitió organizar el análisis de datos.
    - Se obtuvieron patrones relacionados con carreras y estudiantes.
    - Los gráficos facilitaron la interpretación de la información.
    """)