import streamlit as st

st.title("RAGA — Tour del pipeline")
st.caption("Intake → Plan → Ontología → Policy-Gate → RAG → Composición → CEWR → EEE → Observabilidad → Runbook → Auditoría")

# Banner global de incidentes
if st.session_state.get("global_alert"):
    st.error(st.session_state["global_alert"])

# Diagrama de flujo del pipeline (visual y didáctico)
st.graphviz_chart("""
digraph G {
  rankdir=LR;
  node [shape=box, style=rounded];
  Intake -> Plan -> Ontologia -> PolicyGate -> RAG -> Composicion -> CEWR -> EEE -> Observabilidad -> Runbook -> Auditoria;
}
""")

# Contexto del caso de demo + CTA claro
st.markdown("""
**Caso de demo:** exportación de *conservas vegetales* a **México**.  
Verás cómo cada componente afecta a **evidencia, costes y SLA** en tiempo real.
""")

st.page_link("pages/01_Intake_y_Plan.py", label="Iniciar tour ahora →", icon="▶️")
