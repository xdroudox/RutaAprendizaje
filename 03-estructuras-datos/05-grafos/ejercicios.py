"""
EJERCICIOS - Grafos
Ejecuta: python ejercicios.py [numero] [-p]

Uso:
  python ejercicios.py      -> Menu interactivo
  python ejercicios.py 1    -> Ejercicio 1
  python ejercicios.py 1 -p -> Pista para ejercicio 1
  python ejercicios.py -s 1 -> Solucion del ejercicio 1
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# ============================================
# EJERCICIO 1: Implementar un Grafo
# ============================================
def ejercicio_1():
    print("=" * 50)
    print(">> EJERCICIO 1: Implementar un Grafo")
    print("=" * 50)
    print()
    print("Crea la clase Graph usando lista de adyacencia.")
    print()
    print("  class Graph:")
    print("      def __init__(self, directed=False)")
    print("      def add_edge(self, u, v)  - Agrega arista")
    print("      def print_graph(self)     - Muestra el grafo")
    print()
    print("El grafo debe soportar dirigido y no dirigido.")
    print()
    print("Ejemplo no dirigido:")
    print("  g = Graph()")
    print("  g.add_edge(1, 2)")
    print("  g.add_edge(1, 3)")
    print("  g.add_edge(2, 4)")
    print()
    print("  Resultado:")
    print("  1: [2, 3]")
    print("  2: [1, 4]")
    print("  3: [1]")
    print("  4: [2]")
    print()
    print("PISTA: Usa un diccionario {vertice: [vecinos]}")
    print()
    print("Edita el archivo:")
    print("class Graph:")
    print("    # --- TU CODIGO AQUI ---")

def solucion_1():
    print("SOLUCION - Ejercicio 1")
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
    print("    def print_graph(self):")
    print("        for vertex in self.graph:")
    print("            print(f'{vertex}: {self.graph[vertex]}')")
    print()
    print("# Prueba")
    print("g = Graph()")
    print("g.add_edge(1, 2)")
    print("g.add_edge(1, 3)")
    print("g.add_edge(2, 4)")
    print("g.print_graph()")
    print("```")
    print()
    print("Complejidad:")
    print("- add_edge: O(1) promedio")
    print("- print_graph: O(V+E) donde V=vertices, E=aristas")

# ============================================
# EJERCICIO 2: DFS traversal
# ============================================
def ejercicio_2():
    print("=" * 50)
    print(">> EJERCICIO 2: DFS (Depth-First Search)")
    print("=" * 50)
    print()
    print("Implementa DFS para el grafo no dirigido:")
    print()
    print("    1 --- 2")
    print("    |     |")
    print("    3 --- 4")
    print()
    print("  def dfs(graph, start, visited=None):")
    print()
    print("DFS desde el nodo 1 deberia visitar: 1, 2, 4, 3")
    print()
    print("PISTA: DFS usa recursion (o un stack explicito)")
    print()
    print("Edita el archivo:")
    print("def dfs(graph, start, visited=None):")
    print("    # --- TU CODIGO AQUI ---")

def solucion_2():
    print("SOLUCION - Ejercicio 2")
    print()
    print("```python")
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
    print("# Prueba con el grafo de ejemplo")
    print("g = Graph()")
    print("for u, v in [(1,2),(1,3),(2,4),(3,4)]:")
    print("    g.add_edge(u, v)")
    print("dfs(g.graph, 1)  # 1 2 4 3 (o 1 3 4 2)")
    print("```")
    print()
    print("Explicacion:")
    print("DFS explora en profundidad antes de retroceder.")
    print("Usa un set para evitar ciclos.")
    print("Complejidad: O(V+E) donde V=vertices, E=aristas.")
    print()
    print("Tambien se puede implementar con un stack explicito:")
    print("  def dfs_iterative(graph, start):")
    print("      visited = set()")
    print("      stack = [start]")
    print("      while stack:")
    print("          v = stack.pop()")
    print("          if v not in visited:")
    print("              visited.add(v)")
    print("              print(v, end=' ')")
    print("              stack.extend(graph[v])")

# ============================================
# EJERCICIO 3: BFS traversal
# ============================================
def ejercicio_3():
    print("=" * 50)
    print(">> EJERCICIO 3: BFS (Breadth-First Search)")
    print("=" * 50)
    print()
    print("Implementa BFS para el mismo grafo:")
    print()
    print("    1 --- 2")
    print("    |     |")
    print("    3 --- 4")
    print()
    print("  def bfs(graph, start):")
    print()
    print("BFS desde el nodo 1 deberia visitar: 1, 2, 3, 4")
    print()
    print("PISTA: BFS usa una cola (collections.deque)")
    print()
    print("Edita el archivo:")
    print("from collections import deque")
    print()
    print("def bfs(graph, start):")
    print("    # --- TU CODIGO AQUI ---")

def solucion_3():
    print("SOLUCION - Ejercicio 3")
    print()
    print("```python")
    print("from collections import deque")
    print()
    print("def bfs(graph, start):")
    print("    visited = set()")
    print("    queue = deque([start])")
    print("    visited.add(start)")
    print()
    print("    while queue:")
    print("        v = queue.popleft()")
    print("        print(v, end=' ')")
    print("        for neighbor in graph[v]:")
    print("            if neighbor not in visited:")
    print("                visited.add(neighbor)")
    print("                queue.append(neighbor)")
    print("    return visited")
    print()
    print("# Prueba")
    print("g = Graph()")
    print("for u, v in [(1,2),(1,3),(2,4),(3,4)]:")
    print("    g.add_edge(u, v)")
    print("bfs(g.graph, 1)  # 1 2 3 4")
    print("```")
    print()
    print("Comparacion DFS vs BFS:")
    print()
    print("  DFS: 1 2 4 3 (profundidad primero)")
    print("  BFS: 1 2 3 4 (niveles primero)")
    print()
    print("BFS encuentra la ruta mas corta en grafos no ponderados.")
    print("DFS usa menos memoria en arboles profundos.")
    print("Complejidad de ambos: O(V+E)")

# ============================================
# MENU PRINCIPAL
# ============================================
def menu():
    while True:
        print()
        print("=" * 50)
        print("MENU - Grafos")
        print("=" * 50)
        print("1. Implementar un Grafo")
        print("2. DFS traversal")
        print("3. BFS traversal")
        print("0. Salir")
        print()

        opcion = input("Selecciona un ejercicio: ")

        if opcion == "1":
            ejercicio_1()
            input("Presiona ENTER para continuar...")
        elif opcion == "2":
            ejercicio_2()
            input("Presiona ENTER para continuar...")
        elif opcion == "3":
            ejercicio_3()
            input("Presiona ENTER para continuar...")
        elif opcion == "0":
            print("Sigue practicando!")
            break
        else:
            print("Opcion invalida")

def main():
    args = sys.argv[1:]

    if not args:
        menu()
        return

    if "-s" in args:
        idx = args.index("-s")
        if idx + 1 < len(args) and args[idx + 1].isdigit():
            num = int(args[idx + 1])
            [solucion_1, solucion_2, solucion_3][num - 1]()
        return

    if args[0].isdigit():
        num = int(args[0])
        if "-p" in args:
            pistas = [
                "Usa un diccionario donde cada clave es un vertice y el valor es una lista de vecinos",
                "DFS recursivo: llama a dfs para cada vecino no visitado",
                "BFS iterativo: usa deque, popleft para sacar del frente"
            ]
            print(f"PISTA: {pistas[num - 1]}")
        else:
            [ejercicio_1, ejercicio_2, ejercicio_3][num - 1]()

if __name__ == "__main__":
    main()
