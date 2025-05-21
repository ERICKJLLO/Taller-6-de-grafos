from datos.ejercicio3_datos import grafo

def kruskal(grafo):
    parent = {}
    def find(u):
        
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    def union(u, v):
        pu, pv = find(u), find(v)
        if pu != pv:
            parent[pu] = pv
    
    edges = []

    for u in grafo:
        
        for v, w in grafo[u]:
            
            if (v, u, w) not in edges:
                edges.append((u, v, w))

    edges.sort(key=lambda x: x[2])

    for nodo in grafo:
        parent[nodo] = nodo
    mst = []
    total = 0