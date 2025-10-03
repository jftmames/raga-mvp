import streamlit as st
from io import BytesIO
import base64

st.title("10A) Síntesis — Evaluación final de internacionalización (simulada)")

# Banner global
if st.session_state.get("global_alert"):
    st.error(st.session_state["global_alert"])

intake = st.session_state.get("intake")
ruta = st.session_state.get("ruta_seleccionada")
rutas_eval = st.session_state.get("rutas_eval", [])
experimentos = st.session_state.get("experimentos_sel", [])
eee = st.session_state.get("eee", {})
hits = st.session_state.get("hits", [])
cost = st.session_state.get("last_cost")

# Comprobaciones mínimas
if not intake:
    st.info("Falta **Intake**. Completa 1) Intake y Plan.")
    st.stop()
if not ruta:
    st.info("Falta **ruta seleccionada**. Configura 1B) Rutas de razonamiento.")
    st.stop()

# Bloques de contexto
st.subheader("Contexto")
st.markdown(f"- **Producto**: {intake.get('producto','N/D')}  \n- **Mercado**: {intake.get('mercado','N/D')}")
st.markdown(f"- **Objetivo**: {intake.get('objetivo','N/D')}  \n- **Supuestos**: {intake.get('supuestos','N/D')}")

st.subheader("Ruta seleccionada")
st.markdown(f"**{ruta['nombre']}** — valor de ruta **{ruta['valor']} / 100**")
st.caption(f"Pros: {', '.join(ruta.get('pros', []))} · Contras: {', '.join(ruta.get('contras', []))}")

# Métricas de calidad y evidencia
eee_total = float(eee.get("eee", 0.0)) if eee else 0.0
eee_norm = round((eee_total / 3.0) * 100, 1)  # 0–3 → 0–100
evid_norm = min(100.0, round(len(hits) * 33.3, 1)) if hits else 0.0  # 0 hits = 0; 3 hits ≈ 100

c1, c2, c3, c4 = st.columns(4)
with c1: st.metric("Valor de ruta", f"{ruta['valor']}/100")
with c2: st.metric("EEE (normalizado)", f"{eee_norm}/100")
with c3: st.metric("Evidencia (citas)", f"{evid_norm}/100")
with c4:
    if cost:
        st.metric("Coste estimado", f"€{cost['euros']}")
        st.caption(f"Tokens: {cost['tokens']} · Latencia: {cost['latencia_s']}s")
    else:
        st.metric("Coste estimado", "—")
        st.caption("Ejecuta 4) RAG para estimar coste/latencia.")

# Índice compuesto (simulado)
# Peso sugerido: 50% ruta, 30% EEE, 20% evidencia
ivi = round(0.5 * ruta["valor"] + 0.3 * eee_norm + 0.2 * evid_norm, 1)
st.subheader("Índice de Viabilidad Internacional (IVI)")
st.metric("IVI (0–100)", f"{ivi}")

# Recomendación textual (simulada)
def tramo(v):
    if v >= 80: return "ALTO"
    if v >= 60: return "MEDIO"
    return "BAJO"

st.subheader("Recomendación final (borrador)")
reco = []
reco.append(f"• **Recomendación**: avanzar con *{ruta['nombre']}* (valor {ruta['valor']}/100).")
reco.append(f"• **Calidad de razonamiento (EEE)**: {tramo(eee_norm)} ({eee_norm}/100).")
reco.append(f"• **Apoyo en evidencia**: {tramo(evid_norm)} ({evid_norm}/100) con {len(hits)} citas.")
if cost:
    reco.append(f"• **Coste/latencia estimados**: €{cost['euros']} y {cost['latencia_s']}s (objetivo SLA: dossier ≤120s).")
else:
    reco.append("• **Coste/latencia**: pendiente de estimación (ejecuta RAG).")

if experimentos:
    reco.append("• **Próximos pasos (experimentos seleccionados)**:")
    for i, e in enumerate(experimentos, start=1):
        reco.append(f"   {i}. {e['test']} — €{e['costo']} · {e['tiempo_sem']} sem · éxito: {e['exito']}")
else:
    reco.append("• **Próximos pasos**: selecciona experimentos en 1B) para un plan Lean medible.")

st.markdown("\n".join(reco))

# Descarga como Markdown
md_lines = [
    f"# Evaluación final — {intake.get('producto','N/D')} → {intake.get('mercado','N/D')}",
    f"**Ruta**: {ruta['nombre']} (valor {ruta['valor']}/100)",
    f"**IVI**: {ivi}/100",
    f"**EEE**: {eee_norm}/100 · **Evidencia**: {evid_norm}/100 · **Citas**: {len(hits)}",
]
if cost:
    md_lines.append(f"**Coste/latencia**: €{cost['euros']} · {cost['latencia_s']}s")
md_lines.append("\n## Experimentos")
if experimentos:
    for e in experimentos:
        md_lines.append(f"- {e['test']} — €{e['costo']} · {e['tiempo_sem']} sem · éxito: {e['exito']}")
else:
    md_lines.append("- (pendiente de selección)")

md = "\n".join(md_lines)
st.download_button("Descargar evaluación (Markdown)", data=md, file_name="Evaluacion_RAGA_MVP.md", mime="text/markdown")

st.caption("Este IVI es una simulación para demo. En producción: métricas reales, rúbricas validadas y fuentes oficiales.")
