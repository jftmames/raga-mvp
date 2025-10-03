import streamlit as st
from pathlib import Path
from utils.policy_gate import PolicyGate
from utils.ontology import Ontologia
from utils.retrieval import retrieve
from utils.costs import estimar_coste_y_tiempo  # Importamos la función de costes

st.title("4) Recuperación (RAG)")
st.markdown("Se buscan los documentos más relevantes (`top-k`) en las fuentes **permitidas por el Policy-Gate**.")

# --- Carga de configuración y datos ---
BASE = Path(__file__).parent.parent
pg = PolicyGate(BASE / "config" / "policy_gate.yaml")
onto = Ontologia(BASE / "config" / "ontology.json")

docs = []
for fid, fname in [("boe","boe_pymes.md"),("doue","doue_export.md"),("aicep","portugal_aicep.md"),("mx_hs","mexico_hs.md"),("stock","images_stock_policy.md"),("priv_db","priv_db_registro.md")]:
    p = BASE / "data" / "sources" / fname
    if p.exists():
        docs.append((fid, fname, p.read_text(encoding="utf-8")))

# --- Aplicación del Policy-Gate con override de la sesión ---
override = st.session_state.get("policy_override", {})
def permitido(fid):
    # Si el fid está en el override, esa es la regla que manda
    if fid in override:
        return override[fid]
    # Si no, usamos la regla por defecto del PolicyGate
    return pg.permitido(fid)

permitidos = [(fid,name,txt) for (fid,name,txt) in docs if permitido(fid)]
bloqueados = [(fid,name,_) for (fid,name,_) in docs if not permitido(fid)]

# --- Feedback visual del Policy-Gate ---
st.info(f"Fuentes permitidas para la búsqueda: **{[n for _,n,_ in permitidos]}**")
if bloqueados:
    st.warning(f"Fuentes bloqueadas por el Policy-Gate: **{[n for _,n in bloqueados]}**")


# --- Parámetros de búsqueda y ejecución ---
intake = st.session_state.get("intake", {"producto":"Conservas vegetales","mercado":"México"})
consulta = f"{intake.get('producto')} en {intake.get('mercado')}: requisitos, HS, licencias y ferias"
consulta_reescrita = onto.reescribir_consulta(consulta)

st.subheader("Parámetros de la Búsqueda")
k = st.slider("k (número de documentos a recuperar)", 1, 5, 3, help="Ajustar 'k' impacta la cantidad de evidencia y el coste.")

if st.button("Ejecutar Recuperación"):
    hits = retrieve(consulta_reescrita, permitidos, k=k)
    st.session_state["hits"] = hits

    # --- Estimación y guardado de costes ---
    texto_total_len = sum(len(content) for _, _, _, content in hits)
    cost_info = estimar_coste_y_tiempo(texto_total_len)
    st.session_state["last_run_cost"] = cost_info # Guardamos para la página de Observabilidad

    st.success("Búsqueda completada.")
    st.metric("Coste estimado de esta operación", f"€ {cost_info['euros']:.2f}", help=f"Basado en {cost_info['tokens']} tokens y {cost_info['latencia_s']:.2f}s de latencia estimada.")


# --- Mostrar resultados ---
if "hits" in st.session_state:
    st.subheader("Top-k resultados")
    hits = st.session_state["hits"]
    if not hits:
        st.error("No se encontraron resultados en las fuentes permitidas.")
    else:
        for i, (s, fid, name, content) in enumerate(hits, start=1):
            with st.expander(f"**{i}. {name}** [{fid}] — Similitud: {s:.2f}"):
                # Mostramos un snippet del contenido
                st.code("\n".join(content.splitlines()[:10]), language="markdown")
