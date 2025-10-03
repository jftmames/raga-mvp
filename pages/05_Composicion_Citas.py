import streamlit as st
from utils.compose import redactar_informe

st.title("5) Composición con citas (Generación)")

# Banner global de incidentes
if st.session_state.get("global_alert"):
    st.error(st.session_state["global_alert"])

hits = st.session_state.get("hits")
intake = st.session_state.get("intake")
if not hits or not intake:
    st.info("Primero pasa por Intake/Plan y Recuperación.")
else:
    informe = redactar_informe(intake.get("caso", "Caso"), intake, hits)
    st.session_state["informe"] = informe

    with st.expander("Resumen ejecutivo", expanded=True):
        # Todo lo anterior a "Evidencia citada"
        if "## Evidencia citada" in informe:
            st.markdown(informe.split("## Evidencia citada")[0])
        else:
            st.markdown(informe)

    with st.expander("Evidencia citada", expanded=True):
        for i, (s, fid, name, content) in enumerate(hits, start=1):
            with st.popover(f"Ver cita [{i}] {name} ({fid}) — similitud {s:.2f}"):
                st.code(content)

    with st.expander("Conclusiones", expanded=True):
        if "## Conclusiones iniciales" in informe:
            tail = informe.split("## Conclusiones iniciales")[-1]
            st.markdown("## Conclusiones iniciales" + tail)
        else:
            st.markdown("*(Sin conclusiones generadas)*")
