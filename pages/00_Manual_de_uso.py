import streamlit as st

st.title("Manual de uso — RAGA (MVP)")
st.caption("Guía integrada: propósito, uso por páginas, buenas prácticas y solución de problemas.")

# Banner global (si Runbook activó una alerta)
if st.session_state.get("global_alert"):
    st.error(st.session_state["global_alert"])

# Navegación del manual
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

def h2(txt): st.subheader(txt)

# 1
if section == "1. Propósito y alcance":
    h2("Propósito")
    st.write(
        "RAGA es un pipeline de informes legales/de negocio con trazabilidad y control de costes. "
        "No es un chat, es una línea de producción: Intake → Plan → Ontología → Policy-Gate → RAG → "
        "Composición → Argumentación (CEWR) → EEE → Observabilidad → Runbook → Auditoría."
    )
    h2("Qué resuelve")
    st.markdown(
        "- **Explicabilidad y evidencia**: respuestas con **citas** y **argumentación**.\n"
        "- **Gobernanza**: **Policy-Gate** bloquea fuentes por licencia/PII/jurisdicción.\n"
        "- **Calidad**: evaluación **EEE** (heurística de demo).\n"
        "- **Gestión**: **coste/latencia p50/p95** y degradación automática (Runbook)."
    )
    h2("Limitaciones del MVP")
    st.markdown(
        "- Recuperación y EEE simplificadas para demo.\n"
        "- Ontología mínima, fuentes de ejemplo.\n"
        "- Métricas y logs orientados a explicar concepto (no producción)."
    )

# 2
elif section == "2. Público objetivo":
    h2("Para quién")
    st.markdown(
        "- **Dirección y negocio**: coste, tiempos y garantías.\n"
        "- **Compliance / Jurídico**: trazabilidad, citas, revisión humana por umbral.\n"
        "- **Producto / Ingeniería**: arquitectura y puntos de extensión."
    )
    h2("Casos ilustrativos")
    st.markdown(
        "- **Dossier país–producto** (conservas → México).\n"
        "- **Dictamen PI** (uso/licencias; pros/contraargumentos).\n"
        "- **HS preliminar** (clasificación arancelaria con límites)."
    )

# 3
elif section == "3. Requisitos e instalación":
    h2("Requisitos")
    st.markdown(
        "- Python 3.10+.\n"
        "- Dependencias en `requirements.txt`.\n"
        "- Despliegue local (`streamlit run streamlit_app.py`) o Streamlit Cloud (Main file: `streamlit_app.py`)."
    )
    h2("Instalación rápida (local)")
    st.code(
        "python -m venv .venv && source .venv/bin/activate  # Windows: .venv\\Scripts\\activate\n"
        "pip install -r requirements.txt\n"
        "streamlit run streamlit_app.py",
        language="bash",
    )
    h2("Despliegue en Streamlit Cloud")
    st.markdown(
        "- Sube el repo a GitHub.\n"
        "- En Streamlit Cloud: selecciona el repo y `streamlit_app.py` como **Main file**."
    )

# 4
elif section == "4. Estructura del proyecto":
    h2("Estructura")
    tree = (
        "root/\n"
        "├─ streamlit_app.py        # Lanzador; enlaza a Home en /pages\n"
        "├─ Home.py                 # Portada del tour\n"
        "├─ pages/                  # Páginas del pipeline\n"
        "├─ config/                 # policy_gate.yaml, sla.yaml, ontology.json\n"
        "├─ utils/                  # policy_gate, ontology, retrieval, compose, eee, costs, logger\n"
        "├─ data/sources/           # Documentos demo\n"
        "└─ logs/                   # JSON de ejecuciones (trazabilidad)\n"
    )
    st.code(tree, language="text")
    h2("Convenciones clave")
    st.markdown(
        "- Tablas: `st.dataframe(..., width=\"stretch\")` (no `use_container_width`).\n"
        "- Gráficos: render **inline** (data URI) para evitar errores de ficheros temporales.\n"
        "- Estado: `st.session_state` para hits, coste, alertas (`global_alert`)."
    )

# 5
elif section == "5. Flujo de trabajo (visión general)":
    h2("Pipeline")
    st.markdown(
        "1) **Intake y Plan** → objetivo/hipótesis/supuestos.  \n"
        "2) **Ontología** → reescritura/etiquetado.  \n"
        "3) **Policy-Gate** → filtro licencias/PII/jurisdicción.  \n"
        "4) **RAG** → top-k con **snippets resaltados**.  \n"
        "5) **Composición** → informe con **citas**.  \n"
        "6) **CEWR** → mapa de **argumentos**.  \n"
        "7) **EEE** → calidad del razonamiento.  \n"
        "8) **Observabilidad** → €/tarea, latencia; coste **conectado** a la última consulta.  \n"
        "9) **Runbook** → incidentes y **degradación**; banner **global**.  \n"
        "10) **Checklist AI Act** → controles.  \n"
        "11) **Logs** → trazabilidad."
    )

# 6
elif section == "6. Uso paso a paso (demo guiada)":
    h2("Caso de demo: conservas → México")
    st.markdown(
        "- **1) Intake/Plan**: completa producto, mercado y supuestos; guarda.  \n"
        "- **2) Ontología**: muestra consulta original/reescrita y etiquetas.  \n"
        "- **3) Policy-Gate**: bloquea `priv_db` y/o `stock`; impactará en RAG.  \n"
        "- **4) RAG**: ajusta **k** (1–5); observa **snippets resaltados** y **coste estimado**.  \n"
        "- **5) Composición**: revisa secciones (expanders) y **citas** en popover.  \n"
        "- **6) CEWR**: evidencias generan nodos dinámicos.  \n"
        "- **7) EEE**: muestra indicadores; en producción, rúbrica validada.  \n"
        "- **8) Observabilidad**: tarjeta conectada a la última búsqueda + series.  \n"
        "- **9) Runbook**: activa “EEE bajo umbral” y verifica el banner global.  \n"
        "- **10) Checklist**: marca controles para mostrar evidencia operativa.  \n"
        "- **11) Logs**: revisa los últimos JSON."
    )

# 7
elif section == "7. Buenas prácticas de presentación":
    h2("Consejos rápidos")
    st.markdown(
        "- Habla en **outcomes**: evidencia, costes, SLA, revisión humana.\n"
        "- Muestra **causa-efecto**: bloquea una fuente y enseña impacto en RAG/coste.\n"
        "- No prometas magia: el MVP **simula** piezas reemplazables en prod.\n"
        "- Cierra con valor: repetibilidad, trazabilidad, control de riesgo/coste."
    )
    h2("Tiempo sugerido")
    st.write("8–12 minutos para todo el tour. Si algo falla, pasa de página: la narrativa aguanta.")

# 8
elif section == "8. Observabilidad, SLO/SLA y costes":
    h2("Cómo leer las métricas")
    st.markdown(
        "- **Coste estimado** (RAG): impacto de **k** y fuentes permitidas.\n"
        "- **Series p50/p95**: latencia y € por tarea para capacidad/finanzas.\n"
        "- **Alertas**: si p95 sube, degradación (modelo/truncation/cache)."
    )
    h2("Reglas sugeridas")
    st.markdown(
        "- **SLA**: dossier ≤120 s; precisión normativa ≥95%; **EEE** ≥ 2.5 (si no, bloqueo).\n"
        "- **SLO**: p50/p95 € por caso; degradación si 3 días con p95 fuera."
    )

# 9
elif section == "9. Cumplimiento (Policy-Gate y AI Act)":
    h2("Policy-Gate")
    st.markdown(
        "- Filtro previo por **licencia/PII/jurisdicción**; lo bloqueado **no entra** a la búsqueda.\n"
        "- Mensajes visibles y logs para **auditoría**."
    )
    h2("Checklist AI Act (práctico)")
    st.markdown(
        "- Gestión de riesgos, gobernanza de datos, transparencia, supervisión humana, registro.\n"
        "- Objetivo: **evidencias operativas** (citas visibles, logs, versionado)."
    )

# 10
elif section == "10. Solución de problemas (FAQ técnico)":
    h2("Errores habituales y soluciones")
    st.markdown(
        "- **Page not found (`Home.py`)**: usa `st.page_link(\"pages/Home.py\", ...)`.\n"
        "- **Colisión `session_state`**: no reutilices keys de widgets (usa `intake_form`).\n"
        "- **Deprecation `use_container_width`**: `width=\"stretch\"`.\n"
        "- **PyArrow (`pii` bool/str)**: castea a texto en la tabla de `Policy_Gate.py`.\n"
        "- **MediaFileHandler (PNG faltante)**: gráficos **inline** (data URI) y `plt.close(fig)`."
    )
    h2("Dudas de demo")
    st.markdown(
        "- **Sin citas**: ajusta k; des-bloquea fuentes; regenera Composición.\n"
        "- **Alerta global**: desactívala en Runbook → “Ninguno”."
    )

# 11
elif section == "11. Mantenimiento y versionado":
    h2("Qué versionar")
    st.markdown(
        "- **Ontología y prompts**: versionado y deprecación.\n"
        "- **Policy-Gate**: cambios de licencias/PII logados.\n"
        "- **SLA/SLO**: umbrales por caso con registro de cambios.\n"
        "- **Fuentes**: altas/bajas con justificación y fecha."
    )
    h2("Escalado posterior")
    st.markdown(
        "- Sustituir `retrieval.py` por BM25/embeddings.\n"
        "- Reemplazar `eee.py` por rúbrica validada.\n"
        "- Conectar a BOE/DOUE reales y data warehouse de métricas."
    )

# 12
elif section == "12. Glosario rápido":
    h2("Términos clave")
    st.markdown(
        "- **Ontología**: conceptos/relaciones que guían la búsqueda.\n"
        "- **RAG**: recuperación de trozos relevantes antes de generar.\n"
        "- **CEWR**: mapa Claim–Evidence–Warrant–Rebuttal.\n"
        "- **EEE**: métrica didáctica de calidad del razonamiento.\n"
        "- **SLA/SLO**: compromisos externos/internos.\n"
        "- **Policy-Gate**: gate de licencias/PII/jurisdicción previo a uso de fuente.\n"
        "- **p50/p95**: mediana y “peor de los buenos”."
    )

