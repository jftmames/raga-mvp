import streamlit as st
import pandas as pd
from pathlib import Path
from utils.policy_gate import PolicyGate

st.title("3) Policy-Gate (licencias, PII, jurisdicción)")

cfg_path = Path(__file__).parent.parent / "config" / "policy_gate.yaml"
pg = PolicyGate(cfg_path)
fuentes = pg.cfg.get("fuentes", [])

# 🔧 Normalizar a DataFrame y forzar 'pii' a texto (evita ArrowInvalid por mezcla bool/str)
df = pd.DataFrame(fuentes)
if "pii" in df.columns:
    df["pii"] = df["pii"].map({True: "sí", False: "no"}).astype(str)

st.write("Reglas activas:")
st.dataframe(df, width="stretch")  # ← sustituye use_container_width por width

# Simulación de bloqueos manuales (override)
ids = df["id"].tolist() if "id" in df.columns else [f.get("id") for f in fuentes]
to_block = st.multiselect("Forzar bloqueo de:", ids, default=[])
if to_block:
    st.session_state["policy_override"] = {fid: False for fid in to_block}
    st.warning(f"Se bloquearon: {', '.join(to_block)} (simulado)")
else:
    st.session_state["policy_override"] = {}

