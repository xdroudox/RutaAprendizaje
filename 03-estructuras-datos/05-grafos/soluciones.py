"""
SOLUCIONES - Grafos
Ejecuta: python scripts/runner.py 3 5 [ejercicio] -s
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    print(">> SOLUCION 1: Grafo con diccionario de adyacencia")
    print("-" * 40)
    print("class Grafo:")
    print("    def __init__(self):")
    print("        self.adyacencia = {}")
    print()
    print("    def agregar_nodo(self, nodo):")
    print("        if nodo not in self.adyacencia:")
    print("            self.adyacencia[nodo] = []")
    print()
    print("    def agregar_arista(self, a, b):")
    print("        self.agregar_nodo(a)")
    print("        self.agregar_nodo(b)")
    print("        self.adyacencia[a].append(b)")
    print("        self.adyacencia[b].append(a)")
    print()
    print("    def mostrar(self):")
    print("        for nodo, vecinos in self.adyacencia.items():")
    print("            print(f'{nodo}: {vecinos}')")
    print()
    print("Explicacion: Usamos un diccionario donde cada clave es un nodo")
    print("y su valor es una lista de nodos vecinos (grafo no dirigido).")

def solucion_2():
    print(">> SOLUCION 2: DFS (Depth First Search)")
    print("-" * 40)
    print("def dfs(grafo, inicio, visitados=None):")
    print("    if visitados is None:")
    print("        visitados = set()")
    print("    visitados.add(inicio)")
    print("    print(inicio, end=' ')")
    print("    for vecino in grafo.adyacencia[inicio]:")
    print("        if vecino not in visitados:")
    print("            dfs(grafo, vecino, visitados)")
    print()
    print("Explicacion: DFS explora en profundidad usando recursion.")
    print("Va tan lejos como puede por cada rama antes de retroceder.")

def solucion_3():
    print(">> SOLUCION 3: BFS (Breadth First Search)")
    print("-" * 40)
    print("from collections import deque")
    print()
    print("def bfs(grafo, inicio):")
    print("    visitados = set()")
    print("    cola = deque([inicio])")
    print("    visitados.add(inicio)")
    print("    while cola:")
    print("        nodo = cola.popleft()")
    print("        print(nodo, end=' ')")
    print("        for vecino in grafo.adyacencia[nodo]:")
    print("            if vecino not in visitados:")
    print("                visitados.add(vecino)")
    print("                cola.append(vecino)")
    print()
    print("Explicacion: BFS explora por niveles usando una cola.")
    print("Primero visita todos los vecinos directos, luego los siguientes.")

if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
