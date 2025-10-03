import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx
from io import BytesIO
import base64

st.title("6) Mapa de argumentos (CEWR)")

# Banner global de incidentes
if st.session_state.get("global_alert"):
    st.error(st.session_state["global_alert"])

def show_fig_inline(fig):
    buf = BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    b64 = base64.b64encode(buf.read()).decode()
    st.markdown(
        f"<img src='data:image/png;base64,{b64}' style='width:100%;max-width:100%;'/>",
        unsafe_allow_html=True,
    )
    plt.close(fig)

hits = st.session_state.get("hits", [])
if not hits:
    st.info("Genera un informe primero.")
else:
    # CEWR dinámico (evidencias desde 'hits')
    G = nx.DiGraph()
    G.add_node("Claim: Apto para exportar", kind="claim")
    for i, (_s, fid, name, _content) in enumerate(hits, start=1):
        ev = f"Evidence [{i}]: {name}"
        G.add_node(ev, kind="evidence")
        G.add_edge(ev, "Claim: Apto para exportar")
    G.add_node("Warrant: Cumpliendo requisitos citados", kind="warrant")
    G.add_edge("Warrant: Cumpliendo requisitos citados", "Claim: Apto para exportar")
    G.add_node("Rebuttal: Aranceles/Registros adicionales", kind="rebuttal")
    G.add_edge("Rebuttal: Aranceles/Registros adicionales", "Claim: Apto para exportar")

    pos = nx.spring_layout(G, seed=7)
    fig, ax = plt.subplots(figsize=(8, 6))
    nx.draw_networkx_nodes(G, pos, ax=ax)
    nx.draw_networkx_edges(G, pos, ax=ax, arrows=True)
    nx.draw_networkx_labels(G, pos, ax=ax, font_size=9)
    ax.axis("off")
    show_fig_inline(fig)

    st.caption("Los nodos de evidencia se generan a partir de las citas reales de esta ejecución.")

