import streamlit as st
from calculos.dosificacion import calcular_materiales
from utils.conversiones import convertir_unidades, cargar_unidades
from calculos.volumen_losa import (
    volumen_losa_maciza,
    volumen_losa_aligerada
)



st.title("🧱 Dosificación de Concreto – RNE E.060")

st.subheader("Datos de la losa")
st.subheader("Tipo de losa")

tipo_losa = st.radio(
    "Selecciona el tipo de losa",
    ["Maciza", "Aligerada"]
)

st.subheader("Opciones de obra")


unidad = st.selectbox(
    "Selecciona la unidad que usas en obra",
    options=["lata", "balde", "cubo", "carretilla"],
    format_func=lambda x: x.capitalize()
)
usar_desperdicio = st.checkbox("Considerar factor de desperdicio")

desperdicio = 0
if usar_desperdicio:
    desperdicio = st.slider(
        "Porcentaje de desperdicio (%)",
        min_value=0,
        max_value=15,
        value=5
    )


st.subheader("Unidad de medición en obra")
area = st.number_input("Área (m²)", min_value=1.0, value=100.0, key="area")

if tipo_losa == "Maciza":
    espesor = st.number_input(
        "Espesor de losa (m)",
        min_value=0.10,
        value=0.20,
        key="espesor_maciza"
    )
else:
    espesor = st.selectbox(
        "Espesor total de losa aligerada (cm)",
        [20, 25],
        key="espesor_aligerada"
    )







#area = st.number_input("Área (m²)", min_value=1.0, value=100.0)
#espesor = st.number_input("Espesor (m)", min_value=0.05, value=0.20)
fc = st.selectbox("Resistencia f'c (kg/cm²)", [175, 210, 245, 280])


if tipo_losa == "Maciza":
    volumen = volumen_losa_maciza(area, espesor)
else:
    volumen = volumen_losa_aligerada(area, espesor)

st.write(f"📦 **Volumen de concreto:** {volumen:.2f} m³")

if st.button("Calcular dosificación"):
    try:
        resultados = calcular_materiales(volumen, fc, desperdicio)

        unidades = cargar_unidades()
        nombre_unidad = unidades[unidad]["nombre"]

        arena_unidades = convertir_unidades(resultados["arena_m3"], unidad)
        grava_unidades = convertir_unidades(resultados["grava_m3"], unidad) 

        st.success("Resultados según RNE E.060")

        st.markdown("### 📦 Materiales")

        st.write(f"🪨 **Cemento:** {resultados['cemento_bolsas']} bolsas")
        st.write(
        f"🟡 **Arena:** {resultados['arena_m3']} m³ "
        f"(≈ {arena_unidades} {nombre_unidad.lower()}s)"
        )

        st.write(f"💧 **Agua:** {resultados['agua_litros']} L")

        st.write(f"⚖️ **Relación a/c:** {resultados['relacion_ac']}")

        st.info(
        "Las conversiones a unidades de obra son aproximadas y "
        "se basan en prácticas comunes en el Perú."
        )

    except Exception as e:
        st.error(str(e))
if desperdicio > 0:
    st.warning(f"Incluye {desperdicio}% de desperdicio")