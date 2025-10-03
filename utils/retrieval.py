from typing import List, Tuple

def _tokenize(text: str):
    return [t.lower() for t in text.replace("#"," ").replace("-"," ").replace(":"," ").split()]

def cosine_sim(a: dict, b: dict):
    inter = set(a) & set(b)
    num = sum(a[t]*b[t] for t in inter)
    den = (sum(v*v for v in a.values()) ** 0.5) * (sum(v*v for v in b.values()) ** 0.5)
    return num/den if den else 0.0

def vectorize(tokens: List[str]):
    tf = {}
    for t in tokens:
        tf[t] = tf.get(t, 0) + 1
    return tf

def retrieve(query: str, docs: List[Tuple[str, str, str]], k=5):
    qv = vectorize(_tokenize(query))
    scored = []
    for fuente_id, name, content in docs:
        dv = vectorize(_tokenize(content))
        s = cosine_sim(qv, dv)
        scored.append((s, fuente_id, name, content))
    scored.sort(reverse=True, key=lambda x: x[0])
    return scored[:k]
