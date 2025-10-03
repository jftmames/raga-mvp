import streamlit as st

st.title("9) Runbook e incidentes")

# Banner global de incidentes (se actualiza al escoger el escenario)
if st.session_state.get("global_alert"):
    st.error(st.session_state["global_alert"])

st.markdown("""
- **Degradación automática**: si p95 supera el umbral 3 días seguidos, pasar a modelo mediano + truncation + cache.
- **Bloqueo de salida**: si EEE < umbral, revisión humana obligatoria.
- **Fallo de retrieval**: reintento con expansión de consulta; si persiste, notificar y limitar conclusiones.
""")

escenario = st.selectbox("Simular incidente", ["Ninguno","p95 fuera de rango","EEE bajo umbral","Fallo de fuente privada"])

if escenario == "p95 fuera de rango":
    st.session_state["global_alert"] = "🔴 ALERTA: p95 fuera de rango. Activar degradación y revisar prompts."
    st.warning("Acción: activar degradación, notificar a ingeniería y revisar prompts.")
elif escenario == "EEE bajo umbral":
    st.session_state["global_alert"] = "🔴 ALERTA: EEE bajo umbral. Salida bloqueada pendiente de revisión humana."
    st.error("Acción: bloquear salida y enviar a revisión de Compliance.")
elif escenario == "Fallo de fuente privada":
    st.session_state["global_alert"] = "🟠 Aviso: Fuente privada caída. Fallback a públicas; limitar conclusiones."
    st.info("Acción: fallback a fuentes públicas; marcar limitación en conclusiones y log.")
else:
    st.session_state.pop("global_alert", None)
    st.success("Operación normal (alerta desactivada).")

st.caption("La alerta aparecerá arriba en esta y otras páginas mientras esté activa.")
