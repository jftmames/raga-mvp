def puntuar_eee(texto: str) -> dict:
    lower = texto.lower()
    expl = 1 if ("supuestos" in lower or "objetivo" in lower) else 0
    evid_count = texto.count("**[")
    evid = 3 if evid_count >= 3 else (2 if evid_count == 2 else (1 if evid_count == 1 else 0))
    exam = 1 if ("riesgo" in lower or "contraargument" in lower) else 0
    total = min(3, expl + evid + exam)
    return {"expl": expl, "evid": evid, "exam": exam, "eee": float(round(total,2))}
