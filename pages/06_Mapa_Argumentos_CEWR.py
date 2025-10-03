import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx
import base64
from io import BytesIO

st.title("6) Mapa de argumentos (Claim–Evidence–Warrant–Rebuttal)")

def show_fig_inline(fig, alt="", width="100%"):
    """Renderiza la figura como <img> embebido (data URI) para evitar MediaFileHandler."""
    buf = BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    b64 = base64.b64encode(buf.read()).decode()
    st.markdown(
        f"<img alt='{alt}' src='data:image/png;base64,{b64}' style='width:{width};max-width:100%;'/>",
        unsafe_allow_html=True
    )
    plt.close(fig)

texto = st.session_state.get("informe", "")
if not texto:
    st.info("Genera un informe primero.")
else:
    # Grafo CEWR de ejemplo
    G = nx.DiGraph()
    G.add_node("Claim: Apto para exportar", kind="claim")
    G.add_node("Evidence: DOUE 1169/2011", kind="evidence")
    G.add_node("Evidence: BOE etiquetado", kind="evidence")
    G.add_node("Warrant: Cumpliendo requisitos", kind="warrant")
    G.add_node("Rebuttal: Arancel alto MX", kind="rebuttal")
    G.add_edges_from([
        ("Evidence: DOUE 1169/2011", "Claim: Apto para exportar"),
        ("Evidence: BOE etiquetado", "Claim: Apto para exportar"),
        ("Warrant: Cumpliendo requisitos", "Claim: Apto para exportar"),
        ("Rebuttal: Arancel alto MX", "Claim: Apto para exportar"),
    ])

    pos = nx.spring_layout(G, seed=7)
    fig, ax = plt.subplots(figsize=(7, 5))
    nx.draw_networkx_nodes(G, pos, ax=ax)
    nx.draw_networkx_edges(G, pos, ax=ax, arrows=True)
    nx.draw_networkx_labels(G, pos, ax=ax, font_size=9)
    ax.axis("off")

    show_fig_inline(fig, alt="Mapa CEWR", width="100%")
    st.caption("Esquema ilustrativo. En producción: extracción CEWR con enlaces a citas.")

