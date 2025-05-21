import json

def contar_nodos_intermedios(grafo, inicio, objetivo):
    conteo = {}
    
    def dfs(nodo, camino):
    
        if nodo == objetivo:
            print("Ruta encontrada:", camino)
    
            for intermedio in camino[1:-1]:
                conteo[intermedio] = conteo.get(intermedio, 0) + 1
            return
    
        for vecino in grafo[nodo]:
    
            if vecino not in camino:
                dfs(vecino, camino + [vecino])
    
    dfs(inicio, [inicio])

    return conteo
                
if __name__ == "__main__":
    with open ("datos/ejercicio2_datos.json") as g:
        datos = json.load(g)
        grafo = datos["grafo"]
        inicio = datos["inicio"]
        objetivo = datos["objetivo"]
        resultado = contar_nodos_intermedios(grafo, inicio, objetivo)
        print(resultado)
