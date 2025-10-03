import streamlit as st

st.title("9) Runbook e incidentes")

st.markdown("""
- **Degradación automática**: si p95 supera el umbral 3 días seguidos, pasar a modelo mediano + truncation + cache.
- **Bloqueo de salida**: si EEE < umbral, revisión humana obligatoria.
- **Fallo de retrieval**: reintento con expansión de consulta; si persiste, notificar y limitar conclusiones.
""")

escenario = st.selectbox("Simular incidente", ["Ninguno","p95 fuera de rango","EEE bajo umbral","Fallo de fuente privada"])
if escenario == "p95 fuera de rango":
    st.warning("Acción: activar degradación, notificar a ingeniería y revisar prompts.")
elif escenario == "EEE bajo umbral":
    st.error("Acción: bloquear salida y enviar a revisión de Compliance.")
elif escenario == "Fallo de fuente privada":
    st.info("Acción: fallback a fuentes públicas; marcar limitación en conclusiones y log.")
else:
    st.success("Operación normal.")
