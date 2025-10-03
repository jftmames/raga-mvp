import streamlit as st

st.set_page_config(page_title="RAGA — MVP Sim", page_icon="🌍", layout="wide")
st.write("Usa **Pages** para navegar por el MVP o entra a la portada del tour:")

# Ojo: ruta relativa al entrypoint; debe apuntar a 'pages/Home.py'
st.page_link("pages/Home.py", label="Ir al Tour principal", icon="🏠")

