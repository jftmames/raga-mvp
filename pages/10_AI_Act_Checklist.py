import streamlit as st

st.title("10) Checklist regulatorio (enfoque práctico)")

secciones = {
    "Gestión de riesgos": ["Registro de riesgos por caso", "Mitigaciones documentadas", "Revisión trimestral"],
    "Gobernanza de datos": ["Fuentes con licencia", "Minimización de PII", "Política de retención"],
    "Transparencia": ["Citas visibles", "Descripción de límites", "Logs accesibles"],
    "Supervisión humana": ["Umbrales de bloqueo (EEE/precisión)", "Escalado a experto"],
    "Registro/Auditoría": ["Versionado de ontología/prompts", "Logs firmados"]
}

resultados = {}
for sec, items in secciones.items():
    st.subheader(sec)
    cols = st.columns(len(items))
    for i, it in enumerate(items):
        resultados[(sec,it)] = cols[i].checkbox(it, value=True)

score = sum(1 for v in resultados.values() if v)
st.metric("Controles cumplidos", f"{score}/{len(resultados)}")
st.caption("Objetivo: evidencias reutilizables por cliente y auditor.")
