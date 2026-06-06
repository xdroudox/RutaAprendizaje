"""
EJERCICIOS - Grafos
Ejecuta desde raiz: python scripts/runner.py 3 5 [ejercicio]

Niveles:
  🟢 Ej 1: Grafo con diccionario de adyacencia
  🟡 Ej 2: DFS (Depth First Search)
  🔴 Ej 3: BFS (Breadth First Search)

Pistas: python scripts/runner.py 3 5 N -p [1|2|3]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1(pista=0):
    """🟢 Grafo con diccionario de adyacencia"""
    print(">> 🟢 EJERCICIO 1: Grafo con diccionario de adyacencia")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1:")
        print("  self.adyacencia = {}  # diccionario nodo → lista")
        print("  agregar_nodo: if nodo not in self.adyacencia:")
        print("      self.adyacencia[nodo] = []")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  agregar_arista(a, b):")
        print("    1. agregar_nodo(a) y agregar_nodo(b)")
        print("    2. self.adyacencia[a].append(b)")
        print("    3. self.adyacencia[b].append(a)  # No dirigido")
        return
    elif pista == 3:
        print("\n💡 Pista 3:")
        print("  class Grafo:")
        print("      def __init__(self):")
        print("          self.adyacencia = {}")
        print("      def agregar_nodo(self, nodo):")
        print("          if nodo not in self.adyacencia:")
        print("              self.adyacencia[nodo] = []")
        print("      def agregar_arista(self, a, b):")
        print("          self.agregar_nodo(a)")
        print("          self.agregar_nodo(b)")
        print("          self.adyacencia[a].append(b)")
        print("          self.adyacencia[b].append(a)")
        print("      def mostrar(self):")
        print("          for n, v in self.adyacencia.items():")
        print("              print(f'{n}: {v}')")
        return

    print("\nImplementa:")
    print("  class Grafo:")
    print("    - __init__(): self.adyacencia = {}")
    print("    - agregar_nodo(nodo)")
    print("    - agregar_arista(a, b) — grafo NO dirigido")
    print("    - mostrar() — imprime nodo: [vecinos]")
    print()
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")


def ejercicio_2(pista=0):
    """🟡 DFS - Depth First Search"""
    print(">> 🟡 EJERCICIO 2: DFS (Depth First Search)")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1:")
        print("  DFS es recursivo:")
        print("  def dfs(grafo, inicio, visitados=None):")
        print("      if visitados is None: visitados = set()")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  def dfs(grafo, inicio, visitados=None):")
        print("      if visitados is None: visitados = set()")
        print("      visitados.add(inicio)")
        print("      print(inicio, end=' ')")
        print("      for vecino in grafo.adyacencia[inicio]:")
        print("          if vecino not in visitados:")
        print("              dfs(grafo, vecino, visitados)")
        return
    elif pista == 3:
        print("\n💡 Pista 3:")
        print("  Para el grafo:")
        print("    A: [B, C]")
        print("    B: [A, D]")
        print("    C: [A, D]")
        print("    D: [B, C]")
        print("  dfs(grafo, 'A') → A B D C")
        print("  (o A C D B, depende del orden de vecinos)")
        return

    print("\nImplementa:")
    print("  def dfs(grafo, inicio):")
    print()
    print("  Recorre el grafo en profundidad")
    print("  (usa recursion + set de visitados)")
    print()
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")


def ejercicio_3(pista=0):
    """🔴 BFS - Breadth First Search"""
    print(">> 🔴 EJERCICIO 3: BFS (Breadth First Search)")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1:")
        print("  BFS usa una COLA (from collections import deque):")
        print("  cola = deque([inicio])")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  def bfs(grafo, inicio):")
        print("      from collections import deque")
        print("      visitados = {inicio}")
        print("      cola = deque([inicio])")
        print("      while cola:")
        print("          nodo = cola.popleft()")
        print("          print(nodo, end=' ')")
        print("          for vecino in grafo.adyacencia[nodo]:")
        print("              if vecino not in visitados:")
        print("                  visitados.add(vecino)")
        print("                  cola.append(vecino)")
        return
    elif pista == 3:
        print("\n💡 Pista 3:")
        print("  BFS del grafo desde A:")
        print("    A: [B, C]")
        print("    B: [A, D]")
        print("    C: [A, D]")
        print("    D: [B, C]")
        print("  bfs(grafo, 'A') → A B C D")
        return

    print("\nImplementa:")
    print("  def bfs(grafo, inicio):")
    print()
    print("  Recorre el grafo por niveles (usa cola)")
    print("  from collections import deque")
    print()
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")


if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            pista = 0
            if "-p" in sys.argv:
                idx = sys.argv.index("-p")
                if idx + 1 < len(sys.argv) and sys.argv[idx + 1].isdigit():
                    pista = int(sys.argv[idx + 1])
            ejercicios[num](pista)
    else:
        print("EJERCICIOS:")
        for i, ej in enumerate(ejercicios, 1):
            doc = ej.__doc__ or ""
            print(f"  {i}. {doc}")
