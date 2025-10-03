import streamlit as st
from utils.compose import redactar_informe

st.title("5) Composición con citas (Generación)")

hits = st.session_state.get("hits")
intake = st.session_state.get("intake")
if not hits or not intake:
    st.info("Primero pasa por Intake/Plan y Recuperación.")
else:
    informe = redactar_informe(intake.get("caso","Caso"), intake, hits)
    st.session_state["informe"] = informe
    st.markdown(informe)
