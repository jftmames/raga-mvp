from typing import List, Dict
from datetime import datetime

def redactar_informe(caso: str, intake: Dict, hits: List[tuple]):
    partes = []
    partes.append(f"# Informe — {caso}\n")
    partes.append("## Resumen ejecutivo\n")
    partes.append(f"- Producto: {intake.get('producto','N/D')}  ")
    partes.append(f"- Mercado: {intake.get('mercado','N/D')}  ")
    partes.append(f"- Supuestos: {intake.get('supuestos','N/D')}\n")
    partes.append("## Evidencia citada\n")
    for i,(s, fid, name, content) in enumerate(hits, start=1):
        snippet = "\n".join([l for l in content.strip().splitlines() if l][:3])
        partes.append(f"**[{i}] {name} ({fid})** — similitud {s:.2f}\n> {snippet}\n")
    partes.append("## Conclusiones iniciales\n")
    partes.append("- (Borrador) Requisitos y riesgos resumidos a partir de la evidencia citada.")
    partes.append("\n---\n")
    partes.append(f"_Generado: {datetime.utcnow().isoformat()}Z_")
    return "\n".join(partes)
