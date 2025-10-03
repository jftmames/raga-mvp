import streamlit as st, yaml
from pathlib import Path
from utils.policy_gate import PolicyGate

st.title("3) Policy-Gate (licencias, PII, jurisdicción)")

cfg_path = Path(__file__).parent.parent / "config" / "policy_gate.yaml"
pg = PolicyGate(cfg_path)
fuentes = pg.cfg.get("fuentes", [])

st.write("Reglas activas:")
st.dataframe(fuentes, use_container_width=True)

st.write("Simula un cambio: marca una fuente como no permitida (p.ej., 'stock') y observa su efecto en la recuperación.")
ids = [f["id"] for f in fuentes]
to_block = st.multiselect("Forzar bloqueo de:", ids, default=[])
if to_block:
    st.session_state["policy_override"] = {fid: False for fid in to_block}
    st.warning(f"Se bloquearon: {', '.join(to_block)} (simulado)")
else:
    st.session_state["policy_override"] = {}
