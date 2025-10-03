import streamlit as st

st.set_page_config(page_title="RAGA — MVP Sim", page_icon="🌍", layout="wide")

# Banner global de incidentes (si lo activa el Runbook)
if st.session_state.get("global_alert"):
    st.error(st.session_state["global_alert"])

st.write("Usa **Pages** para navegar por el MVP o entra a la portada del tour:")

# Importante: la ruta debe apuntar a la página dentro de /pages
st.page_link("pages/00_Home.py", label="Ir al Tour principal", icon="🏠")
