import json
from pathlib import Path
from datetime import datetime

def guardar_log(dir_path: Path, payload: dict):
    dir_path.mkdir(parents=True, exist_ok=True)
    fname = f"log_{datetime.utcnow().strftime('%Y%m%dT%H%M%S')}.json"
    p = dir_path / fname
    p.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return str(p)

def listar_logs(dir_path: Path):
    return sorted([str(p) for p in dir_path.glob("log_*.json")])
