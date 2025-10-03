import streamlit as st
from pathlib import Path
from utils.policy_gate import PolicyGate
from utils.ontology import Ontologia
from utils.retrieval import retrieve

st.title("4) Recuperación (RAG)")

BASE = Path(__file__).parent.parent
pg = PolicyGate(BASE / "config" / "policy_gate.yaml")
onto = Ontologia(BASE / "config" / "ontology.json")

docs = []
for fid, fname in [("boe","boe_pymes.md"),("doue","doue_export.md"),("aicep","portugal_aicep.md"),("mx_hs","mexico_hs.md"),("stock","images_stock_policy.md"),("priv_db","priv_db_registro.md")]:
    p = BASE / "data" / "sources" / fname
    if p.exists():
        docs.append((fid, fname, p.read_text(encoding="utf-8")))

override = st.session_state.get("policy_override", {})
def permitido(fid):
    if fid in override:
        return False
    return pg.permitido(fid)

permitidos = [(fid,name,txt) for (fid,name,txt) in docs if permitido(fid)]
bloqueados = [(fid,name) for (fid,name,_) in docs if not permitido(fid)]
st.write({"permitidos": [n for _,n,_ in permitidos], "bloqueados": [n for _,n in bloqueados]})

intake = st.session_state.get("intake", {"producto":"Conservas vegetales","mercado":"México"})
consulta = f"{intake.get('producto')} en {intake.get('mercado')}: requisitos, HS, licencias y ferias"
consulta_reescrita = onto.reescribir_consulta(consulta)

k = st.slider("k (top documentos)", 1, 5, 3)
hits = retrieve(consulta_reescrita, permitidos, k=k)

st.subheader("Top-k resultados")
for i,(s,fid,name,content) in enumerate(hits, start=1):
    st.markdown(f"**{i}. {name}** [{fid}] — similitud {s:.2f}")
    st.code("\n".join(content.splitlines()[:5]))

st.session_state["hits"] = hits
