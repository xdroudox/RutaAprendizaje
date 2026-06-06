"""
SOLUCIONES - Arboles
Ejecuta: python scripts/runner.py 3 4 [ejercicio] -s
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: BST con insert")
    print("=" * 50)

    print("""
class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class BST:
    def __init__(self):
        self.raiz = None

    def insert(self, valor):
        if not self.raiz:
            self.raiz = NodoArbol(valor)
            return
        self._insert(self.raiz, valor)

    def _insert(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo:
                self._insert(nodo.izquierdo, valor)
            else:
                nodo.izquierdo = NodoArbol(valor)
        else:
            if nodo.derecho:
                self._insert(nodo.derecho, valor)
            else:
                nodo.derecho = NodoArbol(valor)
""")

    print("--- EXPLICACION ---")
    print("""
- NodoArbol: cada nodo tiene un valor y dos hijos (izquierdo/derecho).
- BST.insert():
  1. Si no hay raiz, el nuevo nodo ES la raiz.
  2. Si no, delega en _insert() recursivo.
- BST._insert():
  - Si valor < nodo.valor: va a la IZQUIERDA.
    - Si hay hijo izquierdo, sigue recursivamente.
    - Si no, inserta ahi.
  - Si valor >= nodo.valor: va a la DERECHA.
    - Misma logica.

Propiedad del BST:
  izquierda < raiz <= derecha

Insercion: [5, 3, 7, 2, 4]
  5 → raiz
  3 → izquierda de 5
  7 → derecha de 5
  2 → izquierda de 3
  4 → derecha de 3

Arbol resultante:
      5
     / \\
    3   7
   / \\
  2   4
""")


def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: Recorrido inorder")
    print("=" * 50)

    print("""
def inorder(nodo):
    if nodo:
        inorder(nodo.izquierdo)
        print(nodo.valor, end=' ')
        inorder(nodo.derecho)
""")

    print("--- EXPLICACION ---")
    print("""
El recorrido inorder visita en este orden:
  1. Subarbol IZQUIERDO (recursivamente)
  2. RAIZ (imprime el valor)
  3. Subarbol DERECHO (recursivamente)

En un BST, esto produce los valores en ORDEN ASCENDENTE.

Visual con arbol [5, 3, 7, 2, 4, 6, 8]:

      5
     / \\
    3   7
   / \\ / \\
  2  4 6  8

Paso a paso de inorder(5):
  1. inorder(3)
     1.1 inorder(2) → print(2)
     1.2 print(3)
     1.3 inorder(4) → print(4)
  2. print(5)
  3. inorder(7)
     3.1 inorder(6) → print(6)
     3.2 print(7)
     3.3 inorder(8) → print(8)

Resultado: 2 3 4 5 6 7 8
""")


def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: Buscar en BST")
    print("=" * 50)

    print("""
def buscar(nodo, valor):
    if not nodo:
        return False
    if nodo.valor == valor:
        return True
    if valor < nodo.valor:
        return buscar(nodo.izquierdo, valor)
    else:
        return buscar(nodo.derecho, valor)
""")

    print("--- EXPLICACION ---")
    print("""
La busqueda aprovecha la propiedad del BST para descartar
la MITAD del arbol en cada paso (similar a binary search).

Buscar 4 en [5, 3, 7, 2, 4, 6, 8]:

  Paso 1: nodo=5, 4<5 → izquierda
  Paso 2: nodo=3, 4>3 → derecha
  Paso 3: nodo=4, 4==4 → True! ✅

Buscar 9 en el mismo arbol:

  Paso 1: nodo=5, 9>5 → derecha
  Paso 2: nodo=7, 9>7 → derecha
  Paso 3: nodo=8, 9>8 → derecha
  Paso 4: nodo=None → False ❌

Complejidad:
  - Promedio (arbol balanceado): O(log n)
  - Peor caso (arbol inclinado): O(n)

   n | O(log n) | O(n)
  ---|----------|-----
  10 |    4     |  10
  100|    7     | 100
  1K |   10     |1000
  1M |   20     | 1M
""")


if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
