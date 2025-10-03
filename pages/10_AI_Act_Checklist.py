import streamlit as st

st.title("10) Checklist regulatorio (enfoque práctico)")

# Banner global de incidentes
if st.session_state.get("global_alert"):
    st.error(st.session_state["global_alert"])

st.caption("Marca los controles que tengas cubiertos. Esto no es asesoramiento legal, es una guía operativa para tu demo.")

secciones = {
    "Gestión de riesgos": ["Registro de riesgos por caso", "Mitigaciones documentadas", "Revisión trimestral"],
    "Gobernanza de datos": ["Fuentes con licencia", "Minimización de PII", "Política de retención"],
    "Transparencia": ["Citas visibles", "Descripción de límites", "Logs accesibles"],
    "Supervisión humana": ["Umbrales de bloqueo (EEE/precisión)", "Escalado a experto"],
    "Registro/Auditoría": ["Versionado de ontología/prompts", "Logs firmados"]
}

resultados = {}
total_checks = 0
checks_ok = 0

for sec, items in secciones.items():
    st.subheader(sec)
    cols = st.columns(len(items))
    for i, it in enumerate(items):
        key = f"check_{sec}_{i}"
        resultados[(sec, it)] = cols[i].checkbox(it, value=True, key=key)
        total_checks += 1
        checks_ok += 1 if resultados[(sec, it)] else 0

st.metric("Controles cumplidos", f"{checks_ok}/{total_checks}")
st.caption("Objetivo de demo: evidencias reutilizables por cliente y auditor (no sólo un checklist).")
