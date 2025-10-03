import streamlit as st
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from utils.costs import generar_series

st.title("8) Observabilidad (€/tarea, latencia, %citas válidas)")

# Banner global de incidentes
if st.session_state.get("global_alert"):
    st.error(st.session_state["global_alert"])

# Métrica conectada a la última consulta
if st.session_state.get("last_cost"):
    est = st.session_state["last_cost"]
    st.metric("Coste estimado consulta actual", f"€{est['euros']}")
    st.caption(f"Tokens: {est['tokens']} · Latencia: {est['latencia_s']}s")

def show_fig_inline(fig, alt=""):
    buf = BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    b64 = base64.b64encode(buf.read()).decode()
    st.markdown(
        f"<img alt='{alt}' src='data:image/png;base64,{b64}' style='width:100%;max-width:100%;'/>",
        unsafe_allow_html=True,
    )
    plt.close(fig)

# Series simuladas
euros_p50 = generar_series(base=0.4, volatilidad=0.05)
euros_p95 = generar_series(base=0.9, volatilidad=0.08)
latencia  = generar_series(base=2.0, volatilidad=0.4)
citas_val = [min(100, max(85, 95 + int((i % 5) - 2))) for i in range(30)]

def plot_line(vals, title, ylabel, alt):
    fig, ax = plt.subplots()
    ax.plot(list(range(1, len(vals) + 1)), vals)
    ax.set_title(title)
    ax.set_xlabel("Días")
    ax.set_ylabel(ylabel)
    show_fig_inline(fig, alt=alt)

plot_line(euros_p50, "Coste p50 (€)", "€", alt="Coste p50")
plot_line(euros_p95, "Coste p95 (€)", "€", alt="Coste p95")
plot_line(latencia,  "Latencia (s)",  "s", alt="Latencia")
plot_line(citas_val, "% citas válidas", "%", alt="Citas válidas")

st.caption("En producción: series desde logs; alertas por umbral.")

