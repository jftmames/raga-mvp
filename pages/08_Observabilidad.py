import streamlit as st
import matplotlib.pyplot as plt
from utils.costs import generar_series

st.title("8) Observabilidad (€/tarea, latencia, %citas válidas)")

euros_p50 = generar_series(base=0.4, volatilidad=0.05)
euros_p95 = generar_series(base=0.9, volatilidad=0.08)
latencia = generar_series(base=2.0, volatilidad=0.4)
citas_validas = [min(100, max(85, 95 + int((i%5)-2))) for i in range(30)]

def plot_line(vals, title, ylabel):
    fig, ax = plt.subplots()
    ax.plot(list(range(1,len(vals)+1)), vals)
    ax.set_title(title); ax.set_xlabel("Días"); ax.set_ylabel(ylabel)
    st.pyplot(fig)

plot_line(euros_p50, "Coste p50 (€)", "€")
plot_line(euros_p95, "Coste p95 (€)", "€")
plot_line(latencia, "Latencia (s)", "s")
plot_line(citas_validas, "% citas válidas", "%")
st.caption("En producción: series desde logs; alertas por umbral.")
