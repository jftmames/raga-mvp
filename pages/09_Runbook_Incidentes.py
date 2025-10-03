import streamlit as st

st.title("9) Runbook e incidentes")
st.markdown("""
Un **Runbook** define acciones automáticas o manuales para responder a incidentes.
Aquí puedes simular un incidente para ver cómo reaccionaría el sistema,
por ejemplo, activando una **alerta global** y proponiendo una acción de mitigación.
""")

# --- Acciones definidas en el runbook ---
st.subheader("Acciones predefinidas")
st.markdown("""
- **Degradación automática**: si la latencia `p95` supera el umbral durante 3 días, el sistema pasa a usar un modelo de IA más pequeño, activa el truncado de contexto y una caché más agresiva.
- **Bloqueo de salida por calidad**: si la métrica `EEE` de un informe es inferior al umbral definido en el SLA (p.ej., 2.5), la salida se bloquea y se requiere revisión humana obligatoria.
- **Fallo de fuente de datos**: si una fuente clave (p.ej., base de datos privada) falla, se reintenta la conexión. Si persiste, se notifica al equipo de operaciones y se marcan las conclusiones del informe como "limitadas por falta de acceso a fuente X".
""")

# --- Simulador de incidentes ---
st.subheader("Simulador de Incidentes")
escenario = st.selectbox("Simular incidente", ["Ninguno","Latencia p95 fuera de rango","EEE bajo umbral","Fallo de fuente privada"])

# Limpiar la alerta si se selecciona "Ninguno"
if escenario == "Ninguno":
    if "global_alert" in st.session_state:
        st.session_state["global_alert"] = None
    st.success("Operación normal. No hay alertas activas.")
else:
    if st.button(f"Activar simulación de '{escenario}'"):
        if escenario == "Latencia p95 fuera de rango":
            st.session_state["global_alert"] = {
                "message": "Latencia p95 fuera de rango. Degradación automática activada.",
                "type": "warning",
                "icon": "⏱️"
            }
            st.warning("Acción recomendada: Activar degradación, notificar a ingeniería y revisar prompts recientes.")
        elif escenario == "EEE bajo umbral":
            st.session_state["global_alert"] = {
                "message": "Calidad EEE por debajo del umbral. Salida bloqueada.",
                "type": "error",
                "icon": "❗"
            }
            st.error("Acción recomendada: Bloquear la publicación del informe y asignarlo a un experto para revisión manual.")
        elif escenario == "Fallo de fuente privada":
            st.session_state["global_alert"] = {
                "message": "Fallo de conexión con fuente 'priv_db'. Usando fallback a fuentes públicas.",
                "type": "warning",
                "icon": "📦"
            }
            st.info("Acción recomendada: Marcar conclusiones como limitadas en el informe y registrar el fallo de la fuente en el log de auditoría.")

        st.success(f"Alerta global activada para '{escenario}'. Navega a otras páginas para ver el banner.")
        st.info("💡 Vuelve a seleccionar 'Ninguno' para desactivar la alerta.")

