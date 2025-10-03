import yaml
from pathlib import Path

class PolicyGate:
    def __init__(self, cfg_path: Path):
        self.cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8"))
        self.permisos = {f["id"]: f for f in self.cfg.get("fuentes", [])}

    def permitido(self, fuente_id: str) -> bool:
        f = self.permisos.get(fuente_id)
        return bool(f and f.get("permitido", False))

    def describe(self, fuente_id: str) -> dict:
        return self.permisos.get(fuente_id, {})
