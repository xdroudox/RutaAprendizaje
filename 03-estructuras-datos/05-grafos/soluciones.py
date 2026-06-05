"""
SOLUCIONES - Grafos
Ejecuta: python soluciones.py [numero]

Uso:
  python soluciones.py    -> Menu de soluciones
  python soluciones.py 1  -> Solucion del ejercicio 1
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    print("=" * 50)
    print("SOLUCION - Ejercicio 1: Implementar un Grafo")
    print("=" * 50)
    print()
    print("```python")
    print("class Graph:")
    print("    def __init__(self, directed=False):")
    print("        self.graph = {}")
    print("        self.directed = directed")
    print()
    print("    def add_vertex(self, v):")
    print("        if v not in self.graph:")
    print("            self.graph[v] = []")
    print()
    print("    def add_edge(self, u, v):")
    print("        self.add_vertex(u)")
    print("        self.add_vertex(v)")
    print("        self.graph[u].append(v)")
    print("        if not self.directed:")
    print("            self.graph[v].append(u)")
    print()
    print("    def get_vertices(self):")
    print("        return list(self.graph.keys())")
    print()
    print("    def get_neighbors(self, v):")
    print("        return self.graph.get(v, [])")
    print()
    print("    def print_graph(self):")
    print("        for v in self.graph:")
    print("            print(f'{v}: {self.graph[v]}')")
    print("```")
    print()
    print("Ventajas de lista de adyacencia:")
    print("- Memoria eficiente: O(V+E)")
    print("- Iterar sobre vecinos de un vertice es rapido")
    print("- Agregar arista es O(1)")
    print()
    print("Matriz de adyacencia usa O(V^2) memoria,")
    print("pero verificar si existe una arista es O(1).")

def solucion_2():
    print("=" * 50)
    print("SOLUCION - Ejercicio 2: DFS traversal")
    print("=" * 50)
    print()
    print("```python")
    print("# Version recursiva")
    print("def dfs(graph, start, visited=None):")
    print("    if visited is None:")
    print("        visited = set()")
    print("    visited.add(start)")
    print("    print(start, end=' ')")
    print("    for neighbor in graph[start]:")
    print("        if neighbor not in visited:")
    print("            dfs(graph, neighbor, visited)")
    print("    return visited")
    print()
    print("# Version iterativa con stack")
    print("def dfs_iterative(graph, start):")
    print("    visited = set()")
    print("    stack = [start]")
    print("    while stack:")
    print("        v = stack.pop()")
    print("        if v not in visited:")
    print("            visited.add(v)")
    print("            print(v, end=' ')")
    print("            for neighbor in reversed(graph[v]):")
    print("                if neighbor not in visited:")
    print("                    stack.append(neighbor)")
    print("    return visited")
    print("```")
    print()
    print("Aplicaciones de DFS:")
    print("- Deteccion de ciclos en grafos")
    print("- Orden topologico")
    print("- Resolver laberintos")
    print("- Componentes conectados")
    print()
    print("Complejidad: O(V+E)")

def solucion_3():
    print("=" * 50)
    print("SOLUCION - Ejercicio 3: BFS traversal")
    print("=" * 50)
    print()
    print("```python")
    print("from collections import deque")
    print()
    print("def bfs(graph, start):")
    print("    visited = set()")
    print("    queue = deque([start])")
    print("    visited.add(start)")
    print("    while queue:")
    print("        v = queue.popleft()")
    print("        print(v, end=' ')")
    print("        for neighbor in graph[v]:")
    print("            if neighbor not in visited:")
    print("                visited.add(neighbor)")
    print("                queue.append(neighbor)")
    print("    return visited")
    print("```")
    print()
    print("Aplicaciones de BFS:")
    print("- Ruta mas corta en grafos no ponderados")
    print("- Web crawling")
    print("- Redes sociales (amigos en comun)")
    print("- GPS (rutas minimas)")
    print()
    print("Comparacion:")
    print("  BFS: 1 2 3 4 (por niveles, encuentra ruta mas corta)")
    print("  DFS: 1 2 4 3 (en profundidad, menos memoria)")
    print()
    print("Ambos: O(V+E) tiempo, O(V) memoria en el peor caso.")

def menu():
    while True:
        print()
        print("=" * 50)
        print("SOLUCIONES - Grafos")
        print("=" * 50)
        print("1. Implementar un Grafo")
        print("2. DFS traversal")
        print("3. BFS traversal")
        print("0. Salir")
        print()

        opcion = input("Ver solucion: ")

        soluciones = {"1": solucion_1, "2": solucion_2, "3": solucion_3}

        if opcion in soluciones:
            soluciones[opcion]()
            input("Presiona ENTER para continuar...")
        elif opcion == "0":
            print("Sigue asi!")
            break
        else:
            print("Opcion invalida")

def main():
    args = sys.argv[1:]
    if args and args[0].isdigit():
        [solucion_1, solucion_2, solucion_3][int(args[0]) - 1]()
    else:
        menu()

if __name__ == "__main__":
    main()
