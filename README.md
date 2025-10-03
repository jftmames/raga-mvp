# RAGA — MVP Sim (Streamlit, multipágina)

Demostrador con explicación simulada realista de todos los componentes:
Intake/Plan → Ontología → Policy-Gate → Recuperación → Composición → Argumentos → EEE → Observabilidad → Runbook → AI Act → Auditoría.

## Despliegue rápido (Streamlit Cloud)
1. Crea un repo en GitHub y sube este contenido.
2. En Streamlit Cloud, selecciona `streamlit_app.py` como Main file.
3. Python 3.10+. Sin secretos.

## Local
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```
