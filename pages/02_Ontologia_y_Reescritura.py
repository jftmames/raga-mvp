import streamlit as st
from pathlib import Path
from utils.ontology import Ontologia

st.title("2) Ontología y reescritura de consulta")

# Banner global de incidentes
if st.session_state.get("global_alert"):
    st.error(st.session_state["global_alert"])

onto = Ontologia(Path(__file__).parent.parent / "config" / "ontology.json")
intake = st.session_state.get("intake", {"producto":"Conservas vegetales","mercado":"México","supuestos":"B2B retail"})

consulta = f"{intake.get('producto','N/D')} en {intake.get('mercado','N/D')}: requisitos, HS, licencias y ferias"
consulta_reescrita = onto.reescribir_consulta(consulta)
etiquetas = onto.etiquetas(consulta_reescrita)

st.code(
    f"Original: {consulta}\nReescrita: {consulta_reescrita}\nEtiquetas: {', '.join(etiquetas)}",
    language="markdown"
)
st.write("La consulta reescrita y etiquetada mejora la recuperación y explica por qué se buscan ciertas fuentes.")
