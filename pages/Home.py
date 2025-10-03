import streamlit as st

st.set_page_config(page_title="RAGA — MVP Simulado", page_icon="🌍", layout="wide")
st.title("RAGA — MVP Simulado (explicación realista de todos los componentes)")
st.caption("Tour: Intake → Plan → Ontología → Policy-Gate → Recuperación → Composición → Argumentos → EEE → Observabilidad → Runbook → AI Act → Auditoría")

st.markdown("""
### Qué vas a ver
- **Explicación guiada** de cada componente con datos simulados pero creíbles.
- **Controles de demo** para forzar fallos y activar **degradación** (modelo mediano, truncation, cache).
- **Métricas**: %citas válidas, EEE, coste p50/p95, SLA.
- **Trazabilidad**: cada ejecución genera un **log** descargable.
""")
