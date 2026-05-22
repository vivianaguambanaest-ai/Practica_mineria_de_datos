import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# =========================================
# TITULO
# =========================================

st.title("Proyecto CRISP-DM con Datos de Estudiantes")

st.markdown("## 📚 DATOS DE ESTUDIANTES")

st.write("""
Este proyecto aplica la metodología CRISP-DM
para analizar información académica
de estudiantes de diferentes períodos.
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

    # Unir archivos
    df = pd.concat([df1, df2], ignore_index=True)

    # =====================================
    # 1. BUSINESS UNDERSTANDING
    # =====================================

    st.header("1️⃣ BUSINESS UNDERSTANDING")

    st.write("""
    El objetivo del proyecto es analizar
    información académica de estudiantes
    para identificar patrones relacionados
    con carreras, sexo, etnia y otros datos.
    """)

    # =====================================
    # 2. DATA UNDERSTANDING
    # =====================================

    st.header("2️⃣ DATA UNDERSTANDING")

    st.subheader("Vista general del dataset")

    st.dataframe(df.head())

    st.subheader("Dimensiones del dataset")

    st.write(df.shape)

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Tipos de datos")

        st.write(df.dtypes)

    with col2:

        st.subheader("Valores nulos")

        st.write(df.isnull().sum())

    # =====================================
    # 3. DATA PREPARATION
    # =====================================

    st.header("3️⃣ DATA PREPARATION")

    # Eliminar duplicados
    df = df.drop_duplicates()

    # Rellenar nulos
    df = df.fillna("Sin dato")

    st.success("Datos preparados correctamente")

    st.write("Nueva dimensión del dataset")

    st.write(df.shape)

    # Codificación
    encoder = LabelEncoder()

    if "sexo" in df.columns:

        df["sexo_codificado"] = encoder.fit_transform(df["sexo"])

        st.subheader("Codificación de sexo")

        st.dataframe(
            df[["sexo", "sexo_codificado"]].head()
        )

    # =====================================
    # 4. MODELING
    # =====================================

    st.header("4️⃣ MODELING")

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
    # GRAFICO CARRERAS
    # =====================================

    if "nombre_carrera" in df.columns:

        st.subheader("📊 Carreras con más estudiantes")

        fig2, ax2 = plt.subplots(figsize=(10,5))

        carreras = df["nombre_carrera"].value_counts().head(10)

        if not carreras.empty:

            carreras.plot(
                kind="bar",
                ax=ax2
            )

            st.pyplot(fig2)

    # =====================================
    # GRAFICO SEXO
    # =====================================

    if "sexo" in df.columns:

        st.subheader("📈 Distribución por sexo")

        fig3, ax3 = plt.subplots(figsize=(6,4))

        df["sexo"].value_counts().plot(
            kind="bar",
            ax=ax3
        )

        st.pyplot(fig3)

    # =====================================
    # 5. EVALUATION
    # =====================================

    st.header("5️⃣ EVALUATION")

    st.write("""
    ✅ Los datos fueron cargados y procesados correctamente.

    ✅ Se identificaron las carreras con mayor número de estudiantes.

    ✅ Se analizaron variables académicas y demográficas.

    ✅ Los gráficos facilitaron la interpretación de resultados.
    """)

    # =====================================
    # 6. DEPLOYMENT
    # =====================================

    st.header("6️⃣ DEPLOYMENT")

    st.success("Proyecto CRISP-DM completado correctamente")

    st.write("""
    ### Conclusiones

    - La metodología CRISP-DM permitió estructurar
      el análisis de datos académicos.

    - El uso de Streamlit facilitó la visualización
      interactiva de la información.

    - Los resultados obtenidos pueden apoyar
      procesos de análisis institucional.
    """)