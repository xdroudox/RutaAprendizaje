"""
SOLUCIONES - Grafos
Ejecuta: python scripts/runner.py 3 5 [ejercicio] -s
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: Grafo con diccionario de adyacencia")
    print("=" * 50)

    print("""
class Grafo:
    def __init__(self):
        self.adyacencia = {}

    def agregar_nodo(self, nodo):
        if nodo not in self.adyacencia:
            self.adyacencia[nodo] = []

    def agregar_arista(self, a, b):
        self.agregar_nodo(a)
        self.agregar_nodo(b)
        self.adyacencia[a].append(b)
        self.adyacencia[b].append(a)  # No dirigido

    def mostrar(self):
        for nodo, vecinos in self.adyacencia.items():
            print(f"{nodo}: {vecinos}")
""")

    print("--- EXPLICACION ---")
    print("""
- La lista de adyacencia es un diccionario donde cada clave
  es un nodo y su valor es una LISTA de nodos vecinos.
- agregar_nodo(): si el nodo no existe, lo crea con lista vacia.
- agregar_arista(): agrega arista BIDIRECCIONAL (grafo no dirigido).
  a → b Y b → a.
- mostrar(): itera sobre el diccionario formateando nodo: [vecinos].

Ejemplo:
  g = Grafo()
  g.agregar_arista("A", "B")
  g.agregar_arista("A", "C")
  g.agregar_arista("B", "D")
  g.mostrar()
  # A: ['B', 'C']
  # B: ['A', 'D']
  # C: ['A']
  # D: ['B']
""")


def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: DFS")
    print("=" * 50)

    print("""
def dfs(grafo, inicio, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(inicio)
    print(inicio, end=' ')
    for vecino in grafo.adyacencia[inicio]:
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)
""")

    print("--- EXPLICACION ---")
    print("""
DFS explora en PROFUNDIDAD: va tan lejos como puede por cada
rama antes de retroceder (backtracking).

Funcionamiento:
  1. Marca el nodo actual como visitado y lo imprime.
  2. Para cada vecino NO visitado, llama recursivamente.

El parametro visitados=None con asignacion interna evita el
problema del mutables default argument en Python.

Visual con grafo:
    A - B - D - E
    |
    C

dfs(A): A B D E C

Orden de recursion:
  dfs(A) → marca A, vecinos [B, C]
    dfs(B) → marca B, vecinos [A, D]
      dfs(D) → marca D, vecinos [B, E]
        dfs(E) → marca E, vecinos [D]
      Vuelve de D, no quedan vecinos nuevos
    Vuelve de B, no quedan vecinos nuevos
    dfs(C) → marca C, vecinos [A]

Complejidad: O(V + E) donde V = vertices, E = aristas.
""")


def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: BFS")
    print("=" * 50)

    print("""
from collections import deque

def bfs(grafo, inicio):
    visitados = set()
    cola = deque([inicio])
    visitados.add(inicio)

    while cola:
        nodo = cola.popleft()
        print(nodo, end=' ')
        for vecino in grafo.adyacencia[nodo]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
""")

    print("--- EXPLICACION ---")
    print("""
BFS explora por NIVELES: primero todos los vecinos directos,
luego los vecinos de los vecinos, etc.

Usa una COLA (deque) en vez de recursion como DFS.

Paso a paso con grafo:
    A - B - D
    |
    C

bfs(A):
  cola = [A], visitados = {A}

  while cola:
    pop A → print(A), vecinos [B, C]
      B no visitado → visitados {A,B}, cola [B]
      C no visitado → visitados {A,B,C}, cola [B,C]

    pop B → print(B), vecinos [A, D]
      A visitado → saltar
      D no visitado → visitados {A,B,C,D}, cola [C,D]

    pop C → print(C), vecinos [A]
      A visitado → saltar

    pop D → print(D), vecinos [B]
      B visitado → saltar

  Resultado: A B C D

Diferencia clave DFS vs BFS:
  - DFS: A B D ... (profundidad primero)
  - BFS: A B C D (niveles primero)

Complejidad: O(V + E) tiempo, O(V) espacio (cola + visitados).
""")


if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
