import streamlit as st

st.title("Manual de uso — RAGA (MVP)")
st.caption("Guía integrada: propósito, roles, flujo, puntos de interacción humana y cuándo entra la IA.")

# Banner global (si Runbook activó una alerta)
if st.session_state.get("global_alert"):
    st.error(st.session_state["global_alert"])

# Navegación del manual
secciones = [
    "1. Propósito y alcance",
    "2. Roles y responsabilidades (HITL)",
    "3. Requisitos e instalación",
    "4. Estructura del proyecto",
    "5. Flujo de trabajo (visión general)",
    "6. Uso paso a paso (demo guiada)",
    "7. Dónde consulta la IA (y bajo qué control)",
    "8. Observabilidad, SLO/SLA y costes",
    "9. Cumplimiento (Policy-Gate y AI Act)",
    "10. Mantenimiento y versionado",
    "11. Glosario rápido",
]
section = st.sidebar.radio("Secciones del manual", secciones, index=0)

def h2(txt): st.subheader(txt)

# 1) Propósito
if section == "1. Propósito y alcance":
    h2("Propósito")
    st.write(
        "RAGA es un pipeline de informes legales/de negocio con trazabilidad y control de costes. "
        "No es un chat autónomo: **siempre hay una persona (PYME/consultor)** que guía las decisiones, "
        "y la IA se usa con límites claros (citas, umbrales de calidad y supervisión humana)."
    )
    h2("Qué resuelve")
    st.markdown(
        "- **Explicabilidad y evidencia**: respuestas con **citas** y **argumentación** (CEWR).\n"
        "- **Gobernanza**: **Policy-Gate** bloquea fuentes por licencia/PII/jurisdicción antes de buscar.\n"
        "- **Calidad**: evaluación **EEE** (heurística de demo) y bloqueo por umbral.\n"
        "- **Gestión**: **coste/latencia p50/p95** y degradación automática (Runbook)."
    )
    h2("Alcance del MVP")
    st.markdown(
        "- Varias piezas (RAG, CEWR, EEE) están **simuladas** para explicar el concepto, siempre con **persona al mando**.\n"
        "- En producción, ciertos pasos consultarán modelos de IA; aquí se indica **cuándo** y **cómo**."
    )

# 2) Roles (Human-in-the-Loop)
elif section == "2. Roles y responsabilidades (HITL)":
    h2("La persona guía; la IA asiste")
    st.markdown(
        "- **PYME/Consultor (humano)**: define objetivo, hipótesis y supuestos; ajusta fuentes permitidas; "
        "elige **rutas de entrada**; valida evidencias; decide sobre conclusiones; aprueba o bloquea la salida.\n"
        "- **Sistema (RAGA)**: orquesta el flujo; aplica Policy-Gate; recupera evidencia; propone borrador con **citas**; "
        "expone mapa de argumentos; calcula métricas y registra logs.\n"
        "- **IA (modelos)**: en producción, apoya en **generación con citas**, **extracción de argumentos** y **evaluación**; "
        "si la calidad cae bajo umbral, **no publica** sin revisión humana."
    )
    h2("Puntos de control humano")
    st.markdown(
        "1) **Intake y Plan** (obligatorio).  \n"
        "2) **Policy-Gate** (puede bloquear fuentes).  \n"
        "3) **Rutas de razonamiento** (ponderaciones y elección).  \n"
        "4) **Revisión de evidencias/citas** (Composición).  \n"
        "5) **Aprobación final** (si EEE/precision ≥ umbral; si no, revisión obligatoria)."
    )

# 3) Requisitos e instalación
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

# 4) Estructura del proyecto
elif section == "4. Estructura del proyecto":
    h2("Estructura")
    tree = (
        "root/\n"
        "├─ streamlit_app.py        # Lanzador; enlaza a Home en /pages\n"
        "├─ Home.py                 # Portada del tour\n"
        "├─ pages/                  # Páginas del pipeline (incluye Rutas y Síntesis)\n"
        "├─ config/                 # policy_gate.yaml, sla.yaml, ontology.json\n"
        "├─ utils/                  # policy_gate, ontology, retrieval, compose, eee, costs, logger\n"
        "├─ data/sources/           # Documentos demo\n"
        "└─ logs/                   # JSON de ejecuciones (trazabilidad)\n"
    )
    st.code(tree, language="text")
    h2("Convenciones clave")
    st.markdown(
        "- Tablas: `st.dataframe(..., width=\"stretch\")`.\n"
        "- Gráficos: render **inline** (data URI) para evitar ficheros temporales.\n"
        "- Estado: `st.session_state` para hits, coste, alertas (`global_alert`), ruta elegida, etc."
    )

# 5) Flujo de trabajo (visión general)
elif section == "5. Flujo de trabajo (visión general)":
    h2("Pipeline con control humano e IA acotada")
    st.markdown(
        "1) **Intake y Plan** — 🧑‍💼 Humano define objetivo/hipótesis/supuestos. *(Sin IA)*  \n"
        "1B) **Rutas de razonamiento** — 🧑‍💼 Humano pondera criterios y elige ruta. *(Sin IA)*  \n"
        "2) **Ontología y Reescritura** — Sistema etiqueta/re-escribe con reglas. *(Sin IA en MVP; IA opcional en prod)*  \n"
        "3) **Policy-Gate** — Bloqueo por licencias/PII/jurisdicción. 🧑‍💼 puede anular. *(Sin IA)*  \n"
        "4) **RAG** — Recuperación top-k sobre fuentes permitidas. *(MVP sin IA; en prod embeddings)*  \n"
        "5) **Composición** — Borrador con **citas**. *(MVP sin IA; en prod LLM con citas + plantillas)*  \n"
        "6) **CEWR** — Mapa Claim–Evidence–Warrant–Rebuttal. *(MVP simulado; en prod extracción IA)*  \n"
        "7) **EEE** — Métrica de calidad. *(MVP heurística; en prod rúbrica/IA + validación humana)*  \n"
        "8) **Observabilidad** — Coste/latencia, %citas válidas. *(Sin IA)*  \n"
        "9) **Runbook** — Incidentes y degradación; bloqueo si baja calidad. *(Sin IA)*  \n"
        "10) **Checklist** — Evidencias operativas. *(Sin IA)*  \n"
        "11) **Logs** — Trazabilidad/auditoría. *(Sin IA)*"
    )
    st.caption("Leyenda: 🧑‍💼 decisión humana; IA en producción con límites y revisión.")

# 6) Uso paso a paso (demo guiada)
elif section == "6. Uso paso a paso (demo guiada)":
    h2("Caso de demo: conservas → México (HITL en cada paso clave)")
    st.markdown(
        "- **1) Intake/Plan (🧑‍💼)**: completa producto, mercado y supuestos; guarda.  \n"
        "- **1B) Rutas (🧑‍💼)**: ajusta pesos, compara rutas y **elige** una; guarda experimentos.  \n"
        "- **2) Ontología**: revisa consulta original/reescrita y etiquetas (reglas).  \n"
        "- **3) Policy-Gate (🧑‍💼)**: bloquea `priv_db` y/o `stock` si procede; esto afectará a RAG.  \n"
        "- **4) RAG**: ajusta **k** (1–5); observa **snippets** y **coste estimado**.  \n"
        "- **5) Composición (🧑‍💼)**: abre expanders; revisa **citas** (popover); decide si falta evidencia.  \n"
        "- **6) CEWR**: verifica que las evidencias respalden la Claim; anota contraargumentos.  \n"
        "- **7) EEE (🧑‍💼)**: si la calidad no llega al umbral, **bloquea** y pide más evidencia.  \n"
        "- **8) Observabilidad**: verifica tarjeta conectada a la última búsqueda + series.  \n"
        "- **9) Runbook (🧑‍💼)**: simula incidente y observa el **banner global**; decide acción.  \n"
        "- **10A) Síntesis (🧑‍💼)**: combina ruta, EEE, evidencia y coste en un IVI; descarga recomendación."
    )

# 7) Dónde consulta la IA (y bajo qué control)
elif section == "7. Dónde consulta la IA (y bajo qué control)":
    h2("Puntos de IA en producción (con persona al mando)")
    st.markdown(
        "- **Composición con citas**: el LLM redacta usando **únicamente** fragmentos recuperados; "
        "el humano revisa y puede devolver a RAG si faltan pruebas.\n"
        "- **CEWR (extracción de argumentos)**: el LLM propone Claim/Evidence/Warrant/Rebuttal **vinculados a citas**; "
        "el humano valida y añade contraargumentos.\n"
        "- **EEE (evaluación)**: el LLM puntúa según rúbrica; si **EEE < umbral**, la salida queda **bloqueada** hasta revisión humana.\n"
        "- **RAG (opcional)**: embeddings para recuperación semántica; aún así, **Policy-Gate** filtra y el humano decide **k**."
    )
    h2("Controles y salvaguardas")
    st.markdown(
        "- **Policy-Gate previo** a cualquier consulta/uso de fuente.\n"
        "- **Citas obligatorias** visibles en el informe (trazabilidad).\n"
        "- **Umbral de calidad** (EEE/precisión): si no se alcanza, **no se publica**.\n"
        "- **Supervisión humana** en Intake/Plan, Rutas, Composición y Síntesis final."
    )

# 8) Observabilidad
elif section == "8. Observabilidad, SLO/SLA y costes":
    h2("Cómo leer las métricas")
    st.markdown(
        "- **Coste estimado (RAG)**: impacto de **k** y fuentes permitidas.\n"
        "- **Series p50/p95**: latencia y € por tarea para capacidad/finanzas.\n"
        "- **Alertas (Runbook)**: si p95 sube, degradación (modelo/truncation/cache)."
    )
    h2("Reglas sugeridas")
    st.markdown(
        "- **SLA**: dossier ≤120 s; precisión normativa ≥95%; **EEE** ≥ 2.5 (si no, bloqueo y revisión).\n"
        "- **SLO**: p50/p95 € por caso; degradación si 3 días con p95 fuera."
    )

# 9) Cumplimiento
elif section == "9. Cumplimiento (Policy-Gate y AI Act)":
    h2("Policy-Gate")
    st.markdown(
        "- Filtro previo por **licencia/PII/jurisdicción**; lo bloqueado **no entra** a la búsqueda.\n"
        "- Mensajes visibles y logs para **auditoría** (quién, cuándo, qué se bloqueó)."
    )
    h2("Checklist AI Act (práctico)")
    st.markdown(
        "- Gestión de riesgos, gobernanza de datos, transparencia, supervisión humana, registro.\n"
        "- Evidencias operativas: citas visibles, logs, versionado de ontología/prompts, umbrales de bloqueo."
    )

# 10) Mantenimiento y versionado
elif section == "10. Mantenimiento y versionado":
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
        "- Reemplazar `eee.py` por rúbrica validada (con fiabilidad interevaluador).\n"
        "- Conectar a BOE/DOUE reales y data warehouse de métricas."
    )

# 11) Glosario
elif section == "11. Glosario rápido":
    h2("Términos clave")
    st.markdown(
        "- **Ontología**: conceptos/relaciones que guían la búsqueda.\n"
        "- **RAG**: recuperación de trozos relevantes antes de generar.\n"
        "- **CEWR**: mapa Claim–Evidence–Warrant–Rebuttal.\n"
        "- **EEE**: métrica de calidad del razonamiento.\n"
        "- **SLA/SLO**: compromisos externos/internos de servicio.\n"
        "- **Policy-Gate**: gate de licencias/PII/jurisdicción previo a uso de fuente.\n"
        "- **p50/p95**: mediana y “peor de los buenos”."
    )
