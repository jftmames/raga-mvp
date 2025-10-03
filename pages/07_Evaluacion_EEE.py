import streamlit as st
from utils.eee import puntuar_eee

st.title("7) Evaluación EEE (calidad del razonamiento)")

informe = st.session_state.get("informe","")
if not informe:
    st.info("Genera un informe primero.")
else:
    eee = puntuar_eee(informe)
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Explícitud", eee["expl"], "0–1")
    with c2: st.metric("Evidencia", eee["evid"], "0–3")
    with c3: st.metric("Examen", eee["exam"], "0–1")
    with c4: st.metric("EEE total", eee["eee"], "0–3")
    st.session_state["eee"] = eee
    st.caption("Heurística de demo. En campus: rúbrica validada y fiabilidad interevaluador.")
