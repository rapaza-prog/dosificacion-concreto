import streamlit as st
from calculos.dosificacion import calcular_materiales

st.title("🧱 Dosificación de Concreto – RNE E.060")

st.subheader("Datos de la losa")
area = st.number_input("Área (m²)", min_value=1.0, value=100.0)
espesor = st.number_input("Espesor (m)", min_value=0.05, value=0.20)
fc = st.selectbox("Resistencia f'c (kg/cm²)", [175, 210, 245, 280])

volumen = area * espesor
st.write(f"📦 **Volumen de concreto:** {volumen:.2f} m³")

if st.button("Calcular dosificación"):
    try:
        resultados = calcular_materiales(volumen, fc)

        st.success("Resultados según RNE E.060")
        st.write(f"🪨 Cemento: **{resultados['cemento_bolsas']} bolsas**")
        st.write(f"🟡 Arena: **{resultados['arena_m3']} m³**")
        st.write(f"⚪ Grava: **{resultados['grava_m3']} m³**")
        st.write(f"💧 Agua: **{resultados['agua_litros']} L**")
        st.write(f"⚖️ Relación a/c: **{resultados['relacion_ac']}**")

        st.info("Dosificación estimada. No reemplaza diseño de mezcla de laboratorio.")
    except Exception as e:
        st.error(str(e))
