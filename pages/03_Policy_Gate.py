import streamlit as st
import pandas as pd
from pathlib import Path
from utils.policy_gate import PolicyGate

st.title("3) Policy-Gate (licencias, PII, jurisdicción)")

# Banner global de incidentes
if st.session_state.get("global_alert"):
    st.error(st.session_state["global_alert"])

cfg_path = Path(__file__).parent.parent / "config" / "policy_gate.yaml"
pg = PolicyGate(cfg_path)
fuentes = pg.cfg.get("fuentes", [])
df = pd.DataFrame(fuentes)

# Normalizar a texto para evitar ArrowInvalid (mezcla bool/str)
if "pii" in df.columns:
    df["pii"] = df["pii"].map({True: "sí", False: "no"}).astype(str)

st.subheader("Estado de fuentes")
for _, row in df.iterrows():
    estado = "🟢 Permitido" if row.get("permitido") else "🔴 Bloqueado"
    st.markdown(
        f"- **{row.get('nombre','?')}** (`{row.get('id','?')}`) — {estado} · "
        f"Licencia: `{row.get('licencia','?')}` · PII: `{row.get('pii','?')}`"
    )

ids = df["id"].tolist() if "id" in df.columns else []
to_block = st.multiselect("Forzar bloqueo de:", ids, default=[])
st.session_state["policy_override"] = {fid: False for fid in to_block} if to_block else {}
st.session_state["policy_msg"] = (
    f"Fuentes bloqueadas por policy: {', '.join(to_block)}" if to_block else ""
)

with st.expander("Ver tabla detallada"):
    st.dataframe(df, width="stretch")  # (en lugar de use_container_width)

