import json, re
from pathlib import Path

class Ontologia:
    def __init__(self, path: Path):
        self.data = json.loads(path.read_text(encoding="utf-8"))
        self.conceptos = self.data.get("conceptos", {})
        self.sinonimos = self.data.get("sinonimos", {})

    def reescribir_consulta(self, consulta: str) -> str:
        c = consulta
        for base, lst in self.sinonimos.items():
            for s in lst:
                c = re.sub(rf"\b{re.escape(s)}\b", base, c, flags=re.I)
        return c

    def etiquetas(self, consulta: str):
        etiquetas = set()
        lower = consulta.lower()
        for concepto, palabras in self.conceptos.items():
            if any(p in lower for p in palabras):
                etiquetas.add(concepto)
        return sorted(etiquetas)
