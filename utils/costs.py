import random

def estimar_coste_y_tiempo(texto_len: int):
    tokens = max(120, int(texto_len/4))
    euros = round((tokens/1000)*0.5 + (tokens/1000)*1.5, 2)
    lat = round(random.uniform(1.1, 3.5), 2)
    return {"tokens": tokens, "euros": euros, "latencia_s": lat}

def generar_series(n=30, base=0.5, volatilidad=0.1):
    vals = []
    v = base
    for _ in range(n):
        v = max(0, v + random.uniform(-volatilidad, volatilidad))
        vals.append(round(v, 3))
    return vals
