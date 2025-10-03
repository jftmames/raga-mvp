import streamlit as st

# Página de Manual de uso para el MVP RAGA
st.title("Manual de uso — RAGA (MVP)")

# Banner global si hay incidentes simulados
if st.session_state.get("global_alert"):
    st.error(st.session_state["global_alert"])

st.caption("Este manual explica el propósito, cómo usar cada página, buenas prácticas de demo, solución de problemas y mantenimiento.")

# Navegación lateral del manual
secciones = [
    "1. Propósito y alcance",
    "2. Público objetivo",
    "3. Requisitos e instalación",
    "4. Estructura del proyecto",
    "5. Flujo de trabajo (visión general)",
    "6. Uso paso a paso (demo guiada)",
    "7. Buenas prácticas de presentación",
    "8. Observabilidad, SLO/SLA y costes",
    "9. Cumplimiento (Policy-Gate y AI Act)",
    "10. Solución de problemas (FAQ técnico)",
    "11. Mantenimiento y versionado",
    "12. Glosario rápido",
]
section = st.sidebar.radio("Secciones del manual", secciones, index=0)

# Utilidades de render
def h2(txt): st.markdown(f"## {txt}")
def p(txt):  st.markdown(txt)

# Contenidos
if section == "1. Propósito y alcance":
    h2("Propósito")
    p("""
RAGA es un **pipeline de informes** legales/de negocio con trazabilidad y control de costes. Este MVP no es “un chat”, sino una **línea de producción**: Intake → Plan → Ontología → Policy-Gate → RAG → Composición → Argumentación (CEWR) → EEE → Observabilidad → Runbook → Auditoría.
    """)
    h2("Qué resuelve")
    p("""
- **Explicabilidad y evidencia**: respuestas basadas en **citas** y **argumentación**.
- **Gobernanza**: **Policy-Gate** que bloquea fuentes por licencia/PII/jurisdicción.
- **Calidad**: evaluación **EEE** (heurística de demo).
- **Gestión**: **coste/latencia p50/p95** y reglas de **degradación** (Runbook).
    """)
    h2("Limitaciones de MVP")
    p("""
- Recuperación y EEE son **simuladas**/simplificadas para demo.
- La ontología es mínima. Las fuentes son de ejemplo.
- Métricas y logs están orientados a explicar el concepto, no a producción.
    """)

elif section == "2. Público objetivo":
    h2("Para quién está pensado")
    p("""
- **Dirección y negocio**: ver coste, tiempos y garantías de calidad.
- **Compliance / Jurídico**: trazabilidad, citas, revisión humana forzada por umbral.
- **Producto / Ingeniería**: arquitectura y puntos de extensión (retrieval, rúbricas, fuentes).
    """)
    h2("Casos ilustrativos")
    p("""
- **Dossier país–producto** (ejemplo: conservas → México).
- **Dictamen PI** (uso/licencias con evidencia y contraargumentos).
- **HS preliminar** (clasificación arancelaria preliminar con limitaciones).
    """)

elif section == "3. Requisitos e instalación":
    h2("Requisitos")
    p("""
- Python 3.10+.
- Dependencias en `requirements.txt`.
- Despliegue local (`streamlit run streamlit_app.py`) o Streamlit Cloud (Main file: `streamlit_app.py`).
    """)
    h2("Instalación rápida (local)")
    p("""
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
streamlit run streamlit_app.py
