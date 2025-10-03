import streamlit as st
from pathlib import Path
from utils.policy_gate import PolicyGate

st.title("3) Policy-Gate (licencias, PII, jurisdicción)")
st.markdown("""
El **Policy-Gate** es un filtro de gobernanza que se aplica **antes** de la búsqueda.
Revisa las fuentes de datos contra un conjunto de reglas (licencia, PII, jurisdicción)
y solo permite que las fuentes autorizadas pasen a la siguiente fase.
El humano puede revisar y anular estas reglas para una búsqueda específica.
""")

cfg_path = Path(__file__).parent.parent / "config" / "policy_gate.yaml"
pg = PolicyGate(cfg_path)
fuentes = pg.cfg.get("fuentes", [])

st.subheader("Estado Actual de las Fuentes")

# --- Representación visual de las fuentes ---
cols = st.columns(len(fuentes))
for i, fuente in enumerate(fuentes):
    with cols[i]:
        permitido = fuente.get("permitido", False)
        emoji = "✅" if permitido else "❌"
        st.metric(
            label=f"{fuente['nombre']} ({fuente['id']})",
            value="Permitido" if permitido else "Bloqueado",
            help=f"Licencia: {fuente['licencia']} | PII: {fuente['pii']} | Jurisdicción: {fuente['jurisdiccion']}"
        )
        st.markdown(f"<div style='text-align: center; font-size: 24px;'>{emoji}</div>", unsafe_allow_html=True)


st.subheader("Simulación de Anulación Manual (Override)")
st.write("Simula un cambio: marca una fuente como no permitida para esta ejecución (p.ej., 'priv_db') y observa su efecto en la página de **Recuperación (RAG)**.")

ids = [f["id"] for f in fuentes]
# Restaurar el estado por defecto si no hay nada en session_state
if 'policy_override' not in st.session_state:
    st.session_state["policy_override"] = {}

# Usamos un multiselect para forzar el bloqueo
to_block = st.multiselect("Forzar bloqueo de:", ids, default=list(st.session_state.get("policy_override", {}).keys()))

if to_block:
    st.session_state["policy_override"] = {fid: False for fid in to_block}
    st.warning(f"Se bloquearon manualmente para esta sesión: **{', '.join(to_block)}**")
else:
    # Si se deseleccionan todos, se limpia el override
    if st.session_state["policy_override"]:
        st.session_state["policy_override"] = {}
        st.success("Anulación manual eliminada. Se usarán las reglas por defecto.")
