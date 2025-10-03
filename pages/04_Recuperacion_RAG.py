import streamlit as st
from pathlib import Path
from utils.policy_gate import PolicyGate
from utils.ontology import Ontologia
from utils.retrieval import retrieve
from utils.costs import estimar_coste_y_tiempo

st.title("4) Recuperación (RAG)")

# Banner global de incidentes
if st.session_state.get("global_alert"):
    st.error(st.session_state["global_alert"])

BASE = Path(__file__).parent.parent
pg = PolicyGate(BASE / "config" / "policy_gate.yaml")
onto = Ontologia(BASE / "config" / "ontology.json")

# Aviso si policy bloqueó algo
if st.session_state.get("policy_msg"):
    st.warning("⚠️ " + st.session_state["policy_msg"])

# Cargar documentos de la demo
docs = []
for fid, fname in [
    ("boe", "boe_pymes.md"),
    ("doue", "doue_export.md"),
    ("aicep", "portugal_aicep.md"),
    ("mx_hs", "mexico_hs.md"),
    ("stock", "images_stock_policy.md"),
    ("priv_db", "priv_db_registro.md"),
]:
    p = BASE / "data" / "sources" / fname
    if p.exists():
        docs.append((fid, fname, p.read_text(encoding="utf-8")))

# Overrides de policy (bloqueos simulados)
override = st.session_state.get("policy_override", {})

def permitido(fid: str) -> bool:
    if fid in override:
        return False
    return pg.permitido(fid)

permitidos = [(fid, name, txt) for (fid, name, txt) in docs if permitido(fid)]
bloqueados = [(fid, name) for (fid, name, _) in docs if not permitido(fid)]

# Preparar consulta desde Intake
intake = st.session_state.get("intake", {"producto": "Conservas vegetales", "mercado": "México"})
consulta = f"{intake.get('producto')} en {intake.get('mercado')}: requisitos, HS, licencias y ferias"
consulta_reescrita = onto.reescribir_consulta(consulta)

# Utilidad para resaltar términos en snippets
def highlight(text: str, terms):
    import re
    def rep(m): return f"<mark>{m.group(0)}</mark>"
    for t in sorted({t for t in terms if t}, key=len, reverse=True):
        text = re.sub(rf"(?i){re.escape(t)}", rep, text)
    return text

k = st.slider("k (top documentos)", 1, 5, 3)
hits = retrieve(consulta_reescrita, permitidos, k=k)

st.subheader("Top-k resultados")
terms = [intake.get("producto", ""), intake.get("mercado", ""), "requisitos", "HS", "licencias", "ferias"]
for i, (s, fid, name, content) in enumerate(hits, start=1):
    st.markdown(f"**{i}. {name}** [{fid}] — similitud {s:.2f}")
    snippet = "\n".join(content.splitlines()[:5])
    st.markdown(highlight(snippet, terms), unsafe_allow_html=True)

# Coste estimado “online” (conecta con Observabilidad)
payload_len = sum(len(c) for *_, c in hits) + len(consulta_reescrita)
est = estimar_coste_y_tiempo(payload_len)
st.session_state["last_cost"] = est
st.info(f"💶 Coste estimado ahora: **€{est['euros']}** · Tokens: {est['tokens']} · Latencia: {est['latencia_s']}s")

# Guardar hits para siguientes pantallas
st.session_state["hits"] = hits

