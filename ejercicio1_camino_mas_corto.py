import json
import heapq

def dijkstra(grafo, origen, destino):
    
    heap = [(0, 1, origen, [origen])]
    visitados = set()
    
    while heap:
    
        costo, _, nodo, camino = heapq.heappop(heap)
    
        if nodo == destino:
            return camino, costo
    
        if nodo in visitados:
            continue
        visitados.add(nodo)

        for vecino, peso in grafo[nodo].items():
    
            if vecino not in visitados:
                heapq.heappush(heap, (costo + peso, len(camino) + 1, vecino, camino + [vecino]))
    
    return None, float('inf')

if __name__ == "__main__":
    with open("datos/ejercicio1_datos.json") as f:
        datos = json.load(f)
        grafo = datos["grafo"]
        origen = datos["origen"]
        destino = datos["destino"]
        camino, costo = dijkstra(grafo, origen, destino)
        print("camino mas corto:", camino)
        print("costo total:", costo)        