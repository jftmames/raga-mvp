import streamlit as st
from pathlib import Path
from utils.logger import listar_logs

st.title("11) Logs y auditoría")

# Banner global de incidentes
if st.session_state.get("global_alert"):
    st.error(st.session_state["global_alert"])

logs_dir = Path(__file__).parent.parent / "logs"
files = listar_logs(logs_dir)

if not files:
    st.info("Aún no hay logs. Genera un informe en las páginas anteriores (Recuperación → Composición) y vuelve aquí.")
else:
    st.markdown("### Últimos logs")
    for f in files[-20:]:
        st.write(f"• `{f}`")
    st.caption("Descarga los JSON desde el hosting o localmente para trazabilidad y auditoría.")

