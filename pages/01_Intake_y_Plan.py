import streamlit as st

st.title("1) Intake y Plan")
st.write("Define el caso y explicita objetivo, hipótesis y supuestos. Esto alimenta la trazabilidad y la evaluación (EEE).")

# Banner global de incidentes
if st.session_state.get("global_alert"):
    st.error(st.session_state["global_alert"])

# Usar una clave de formulario que NO colisione con session_state["intake"]
with st.form("intake_form"):
    col1, col2 = st.columns(2)
    with col1:
        caso = st.selectbox(
            "Tipo de tarea",
            ["Dossier país–producto", "Dictamen PI uso/licencia", "HS preliminar"]
        )
        producto = st.text_input("Producto", "Conservas vegetales")
        mercado = st.text_input("Mercado objetivo", "México")
    with col2:
        objetivo = st.text_area(
            "Objetivo",
            "Determinar requisitos y barreras para exportar conservas vegetales a México con SLA y costes controlados."
        )
        hipotesis = st.text_area(
            "Hipótesis",
            "La clasificación HS 2001.90 es aplicable y hay ferias relevantes para retail."
        )
        supuestos = st.text_area(
            "Supuestos",
            "B2B retail; venta online; marca existente en ES; assets con licencia adecuada."
        )
    submitted = st.form_submit_button("Guardar plan")

if submitted:
    st.session_state["intake"] = {
        "caso": caso,
        "producto": producto,
        "mercado": mercado,
        "objetivo": objetivo,
        "hipotesis": hipotesis,
        "supuestos": supuestos,
    }
    st.success("Plan guardado.")
    st.json(st.session_state["intake"])
else:
    if "intake" in st.session_state:
        st.info("Plan cargado desde la sesión actual.")
        st.json(st.session_state["intake"])
    else:
        st.info("Rellena y pulsa **Guardar plan**. Se usará en las siguientes páginas.")

