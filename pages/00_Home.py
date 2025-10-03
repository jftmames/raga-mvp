import streamlit as st

# --- Configuración de la página y helpers ---
st.set_page_config(page_title="RAGA — MVP Simulado", page_icon="🌍", layout="wide")

def h2(text):
    """Función helper para títulos h2 consistentes."""
    st.markdown(f"<h2>{text}</h2>", unsafe_allow_html=True)

# --- Banner de Alerta Global ---
# Este bloque revisa si hay una alerta en el estado de la sesión (definida en Runbook)
# y la muestra en la parte superior de la página. Debería añadirse al inicio
# de CADA archivo en la carpeta /pages para que la alerta sea visible globalmente.
if "global_alert" in st.session_state and st.session_state["global_alert"]:
    alert_info = st.session_state["global_alert"]
    st.toast(alert_info["message"], icon=alert_info.get("icon", "⚠️"))
    if alert_info["type"] == "warning":
        st.warning(f"**ALERTA GLOBAL:** {alert_info['message']}")
    elif alert_info["type"] == "error":
        st.error(f"**ALERTA CRÍTICA:** {alert_info['message']}")
    # Limpiamos la alerta para que no se muestre en la siguiente recarga si no es persistente
    # st.session_state["global_alert"] = None


# --- Barra Lateral de Navegación ---
st.sidebar.title("📘 Guía del Proyecto RAGA")
st.sidebar.markdown("Navega por las secciones para entender el propósito, la estructura y el flujo de trabajo del sistema.")

section = st.sidebar.radio(
    "Selecciona una sección:",
    [
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
    ],
    key="main_nav"
)

# --- Contenido Principal ---
st.title("RAGA — Simulación de un Pipeline de IA Gobernada")
st.caption(f"Mostrando sección: **{section}**")

# 1) Propósito y alcance
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
        "valida evidencias; decide sobre conclusiones; aprueba o bloquea la salida.\n"
        "- **Sistema (RAGA)**: orquesta el flujo; aplica Policy-Gate; recupera evidencia; propone borrador con **citas**; "
        "expone mapa de argumentos; calcula métricas y registra logs.\n"
        "- **IA (modelos)**: en producción, apoya en **generación con citas**, **extracción de argumentos** y **evaluación**; "
        "si la calidad cae bajo umbral, **no publica** sin revisión humana."
    )
    h2("Puntos de control humano")
    st.markdown(
        "1) **Intake y Plan** (obligatorio).  \n"
        "2) **Policy-Gate** (puede bloquear fuentes).  \n"
        "3) **Revisión de evidencias/citas** (Composición).  \n"
        "4) **Aprobación final** (si EEE/precision ≥ umbral; si no, revisión obligatoria)."
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
        "raga-mvp-sim-streamlit/\n"
        "├─ streamlit_app.py         # Lanzador; enlaza a Home en /pages\n"
        "├─ Home.py                  # Esta guía interactiva\n"
        "├─ pages/                   # Páginas del pipeline (01_Intake..., etc.)\n"
        "├─ config/                  # Ficheros de configuración (policy_gate.yaml, ...)\n"
        "├─ utils/                   # Lógica reutilizable (retrieval, compose, ...)\n"
        "├─ data/sources/            # Documentos de ejemplo (.md)\n"
        "└─ logs/                    # Logs de ejecución en formato JSON (trazabilidad)\n"
    )
    st.code(tree, language="bash")
    h2("Convenciones clave")
    st.markdown(
        "- **Estado entre páginas**: `st.session_state` se usa para pasar datos como el `intake`, los `hits` de la búsqueda, costes y alertas.\n"
        "- **Visualización**: Se priorizan componentes nativos de Streamlit para una demo limpia y rápida."
    )

# 5) Flujo de trabajo (visión general)
elif section == "5. Flujo de trabajo (visión general)":
    h2("Pipeline con control humano e IA acotada")
    st.graphviz_chart('''
        digraph {
            rankdir=TB;
            node [shape=box, style="rounded,filled", fillcolor=lightblue];
            
            subgraph cluster_human {
                label = "Control Humano (🧑‍💼)";
                style=filled;
                color=lightgrey;
                node [fillcolor=lightyellow];
                Intake [label="1. Intake y Plan"];
                PolicyGate [label="3. Policy-Gate (Revisión)"];
                Review [label="5. Revisión y Aprobación"];
            }

            subgraph cluster_system {
                label = "Sistema RAGA (⚙️)";
                style=filled;
                color=lightcyan;
                Ontology [label="2. Ontología y Reescritura"];
                RAG [label="4. Recuperación (RAG)"];
                Composition [label="5A. Composición (Borrador)"];
                CEWR [label="6. Mapa de Argumentos (CEWR)"];
                EEE [label="7. Evaluación (EEE)"];
                Observability [label="8. Observabilidad"];
                Logs [label="11. Logs de Auditoría"];
            }

            Intake -> Ontology -> PolicyGate -> RAG -> Composition -> Review;
            Composition -> CEWR [style=dashed];
            Review -> EEE;
            EEE -> Logs;
            RAG -> Observability [style=dashed];
        }
    ''')
    st.markdown(
        "1) **Intake y Plan** — 🧑‍💼 Humano define objetivo/hipótesis/supuestos. *(Sin IA)* \n"
        "2) **Ontología y Reescritura** — Sistema etiqueta/re-escribe con reglas. *(Sin IA en MVP; IA opcional en prod)* \n"
        "3) **Policy-Gate** — Bloqueo por licencias/PII/jurisdicción. 🧑‍💼 puede anular. *(Sin IA)* \n"
        "4) **RAG** — Recuperación top-k sobre fuentes permitidas. *(MVP sin IA; en prod embeddings)* \n"
        "5) **Composición** — Borrador con **citas**. *(MVP sin IA; en prod LLM con citas + plantillas)* \n"
        "6) **CEWR** — Mapa Claim–Evidence–Warrant–Rebuttal. *(MVP simulado; en prod extracción IA)* \n"
        "7) **EEE** — Métrica de calidad. *(MVP heurística; en prod rúbrica/IA + validación humana)* \n"
        "8) **Observabilidad** — Coste/latencia, %citas válidas. *(Sin IA)* \n"
        "9) **Runbook** — Incidentes y degradación; bloqueo si baja calidad. *(Sin IA)* \n"
        "10) **Checklist** — Evidencias operativas. *(Sin IA)* \n"
        "11) **Logs** — Trazabilidad/auditoría. *(Sin IA)*"
    )
    st.caption("Leyenda: 🧑‍💼 decisión humana; ⚙️ proceso automatizado/asistido.")

# ... (resto de las secciones del 6 al 11) ...
# El código para las demás secciones (6 a 11) se añadiría aquí,
# siguiendo el mismo patrón "elif section == ...".
# Por brevedad, se omite aquí pero la estructura es idéntica.

else:
    st.info("Selecciona una sección de la barra lateral para ver los detalles.")

