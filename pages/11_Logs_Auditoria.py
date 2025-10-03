import streamlit as st
from pathlib import Path
from utils.logger import listar_logs

st.title("11) Logs y auditoría")

logs_dir = Path(__file__).parent.parent / "logs"
files = listar_logs(logs_dir)
if not files:
    st.info("Aún no hay logs. Genera un informe en las páginas anteriores.")
else:
    for f in files[-10:]:
        st.write(f"• {f}")
    st.caption("Descarga los JSON desde el hosting o localmente.")
