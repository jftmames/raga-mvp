import streamlit as st
from math import isfinite
from io import BytesIO
import base64
import matplotlib.pyplot as plt

st.title("1B) Rutas de razonamiento (decisiones PYME/consultor)")

# Banner global
if st.session_state.get("global_alert"):
    st.error(st.session_state["global_alert"])

# Intake mínimo
intake = st.session_state.get("intake")
if not intake:
    st.info("Primero completa **1) Intake y Plan** y vuelve aquí.")
    st.stop()

producto = intake.get("producto", "Producto")
mercado = intake.get("mercado", "Mercado")

st.markdown(
    f"**Caso**: {producto} → **{mercado}**. "
    "Ajusta los pesos según tus prioridades y compara rutas de entrada. "
    "El valor total combina tus pesos con los atributos de cada ruta (0–10)."
)

# === Pesos de decisión (0–5) ===
with st.expander("Pondera criterios (0–5)", expanded=True):
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        w_market   = st.slider("Atracción de mercado", 0, 5, 4)
        w_reg      = st.slider("Riesgo regulatorio (↓ mejor)", 0, 5, 3)
    with c2:
        w_dist     = st.slider("Distancia cultural (↓ mejor)", 0, 5, 3)
        w_cost     = st.slider("Coste de entrada (↓ mejor)", 0, 5, 3)
    with c3:
        w_time     = st.slider("Tiempo de validación (↓ mejor)", 0, 5, 4)
        w_digital  = st.slider("Madurez digital", 0, 5, 3)
    with c4:
        w_synergy  = st.slider("Sinergias logística/idioma", 0, 5, 4)
        w_other    = st.slider("Barreras arancel./técnicas (↓ mejor)", 0, 5, 3)

weights = {
    "market": w_market, "reg": w_reg, "dist": w_dist, "cost": w_cost,
    "time": w_time, "digital": w_digital, "synergy": w_synergy, "other": w_other
}

# === Definición de rutas (demo) ===
# Puntuaciones 0–10 por atributo. Las métricas "negativas" (reg/dist/cost/time/other) se invierten al calcular el valor.
rutas = [
    {
        "id": "UE_vecina",
        "nombre": "UE proximidad (Portugal/Francia)",
        "desc": "Entrada gradual a un mercado cercano cultural y regulatoriamente.",
        "scores": {"market": 6, "reg": 3, "dist": 2, "cost": 4, "time": 3, "digital": 6, "synergy": 8, "other": 3},
        "experimentos": [
            {"test": "Misión comercial + 5 reuniones B2B", "costo": 1200, "tiempo_sem": 3, "exito": "≥2 pilotos firmados"},
            {"test": "Listar en marketplace B2B UE", "costo": 300, "tiempo_sem": 2, "exito": "≥10 leads cualificados"}
        ],
        "pros": ["Baja distancia cultural/regulatoria", "Coste y tiempo de validación contenidos"],
        "contras": ["Tamaño de mercado incremental", "Precio medio UE puede ser exigente"]
    },
    {
        "id": "MX_partner",
        "nombre": f"{mercado} vía partner local",
        "desc": "Acuerdo con distribuidor/importador local para acelerar validación.",
        "scores": {"market": 8, "reg": 6, "dist": 7, "cost": 6, "time": 5, "digital": 7, "synergy": 5, "other": 6},
        "experimentos": [
            {"test": "Term sheet con 1 distribuidor", "costo": 0, "tiempo_sem": 2, "exito": "MVP retail en 1 cadena"},
            {"test": "Pilotaje con 2 retailers regionales", "costo": 800, "tiempo_sem": 4, "exito": "Rotación ≥80% stock"}
        ],
        "pros": ["Acceso acelerado a canales", "Aprendizaje local rápido"],
        "contras": ["Dependencia del partner", "Riesgo regulatorio/logístico mayor"]
    },
    {
        "id": "MX_directo",
        "nombre": f"{mercado} entrada directa B2B",
        "desc": "Estructura propia (agente/comercial) y registro directo.",
        "scores": {"market": 8, "reg": 7, "dist": 7, "cost": 7, "time": 7, "digital": 7, "synergy": 5, "other": 7},
        "experimentos": [
            {"test": "Agente comisionista 90 días", "costo": 2500, "tiempo_sem": 12, "exito": "≥3 cuentas ancla"},
            {"test": "Registro sanitario/etiquetado", "costo": 1500, "tiempo_sem": 10, "exito": "OK regulatorio sin observaciones graves"}
        ],
        "pros": ["Control total", "Valor capturado mayor a largo plazo"],
        "contras": ["CAPEX/OPEX inicial alto", "Time-to-market más largo"]
    },
    {
        "id": "UE_ecom",
        "nombre": "E-commerce transfronterizo UE",
        "desc": "Canal digital UE para test de demanda y pricing.",
        "scores": {"market": 5, "reg": 2, "dist": 2, "cost": 3, "time": 3, "digital": 8, "synergy": 7, "other": 2},
        "experimentos": [
            {"test": "Campaña performance 4 semanas", "costo": 600, "tiempo_sem": 4, "exito": "CAC ≤ objetivo y ≥200 ventas"},
            {"test": "A/B pricing/packaging", "costo": 200, "tiempo_sem": 3, "exito": "Elasticidad y margen objetivo"}
        ],
        "pros": ["Validación barata/rápida", "Datos de cliente inmediatos"],
        "contras": ["No sustituye canal físico", "Logística y devoluciones a vigilar"]
    }
]

# === Cálculo de valor por ruta ===
def valor_ruta(scores, weights):
    # Invertimos métricas "negativas"
    inv = {k: (10 - scores[k]) for k in ["reg", "dist", "cost", "time", "other"]}
    pos = {k: scores[k] for k in ["market", "digital", "synergy"]}
    val = (
        weights["market"]  * pos["market"]  +
        weights["digital"] * pos["digital"] +
        weights["synergy"] * pos["synergy"] +
        weights["reg"]     * inv["reg"]     +
        weights["dist"]    * inv["dist"]    +
        weights["cost"]    * inv["cost"]    +
        weights["time"]    * inv["time"]    +
        weights["other"]   * inv["other"]
    )
    max_val = sum(weights.values()) * 10 if sum(weights.values()) > 0 else 1
    score100 = round((val / max_val) * 100, 1)
    return score100

for r in rutas:
    r["valor"] = valor_ruta(r["scores"], weights)

# Orden y visualización
rutas_sorted = sorted(rutas, key=lambda x: x["valor"], reverse=True)
st.subheader("Ranking de rutas (valor normalizado 0–100)")
for r in rutas_sorted:
    st.markdown(f"**{r['nombre']}** — valor **{r['valor']}** · {r['desc']}")
    st.caption(f"Pros: {', '.join(r['pros'])} · Contras: {', '.join(r['contras'])}")

# Gráfico de barras inline (evita MediaFileHandler)
def show_bar_inline(labels, values, title="Valor por ruta (0–100)"):
    fig, ax = plt.subplots(figsize=(6, 3.2))
    ax.bar(labels, values)
    ax.set_ylim(0, 100)
    ax.set_title(title)
    for i, v in enumerate(values):
        ax.text(i, v + 2, f"{v}", ha="center", fontsize=9)
    buf = BytesIO(); fig.savefig(buf, format="png", bbox_inches="tight"); buf.seek(0)
    b64 = base64.b64encode(buf.read()).decode()
    st.markdown(f"<img src='data:image/png;base64,{b64}' style='width:100%;max-width:100%;'/>", unsafe_allow_html=True)
    plt.close(fig)

show_bar_inline([r["nombre"] for r in rutas_sorted], [r["valor"] for r in rutas_sorted])

# Selección y plan de experimentos
st.subheader("Selecciona tu ruta y define experimentos (Build–Measure–Learn)")
opciones = {r["nombre"]: r["id"] for r in rutas_sorted}
eleccion = st.radio("Ruta seleccionada", list(opciones.keys()))
ruta_sel = next(r for r in rutas_sorted if r["id"] == opciones[eleccion])

# Experimentos toggle
st.markdown(f"**Experimentos propuestos para {ruta_sel['nombre']}**")
checks = []
for i, exp in enumerate(ruta_sel["experimentos"], start=1):
    chk = st.checkbox(
        f"[{i}] {exp['test']} — coste €{exp['costo']} · {exp['tiempo_sem']} sem · éxito: {exp['exito']}",
        value=True
    )
    if chk:
        checks.append(exp)

# Guardar en sesión
if st.button("Guardar ruta y experimentos"):
    st.session_state["ruta_seleccionada"] = ruta_sel
    st.session_state["rutas_eval"] = rutas_sorted
    st.session_state["experimentos_sel"] = checks
    st.success("Ruta y experimentos guardados ✔️")

# Nota para la síntesis
st.caption("Tip: Al final, la página **Síntesis** combinará el valor de ruta con EEE, evidencia y coste para una recomendación integral.")
