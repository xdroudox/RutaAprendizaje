"""
EJERCICIOS - Arboles
Ejecuta desde raiz: python scripts/runner.py 3 4 [ejercicio]

Niveles:
  🟢 Ej 1: NodoArbol y BST con insert
  🟡 Ej 2: Recorrido inorder
  🔴 Ej 3: Buscar en BST

Pistas: python scripts/runner.py 3 4 N -p [1|2|3]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1(pista=0):
    """🟢 BST con insert"""
    print(">> 🟢 EJERCICIO 1: BST con insert")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1:")
        print("  class NodoArbol:")
        print("      def __init__(self, valor):")
        print("          self.valor = valor")
        print("          self.izquierdo = None")
        print("          self.derecho = None")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  insert en BST:")
        print("    - Si no hay raiz, nuevo nodo es la raiz")
        print("    - Si no, llama a _insert recursivo")
        print("  _insert(nodo, valor):")
        print("    - Si valor < nodo.valor → izquierda")
        print("    - Si no → derecha")
        return
    elif pista == 3:
        print("\n💡 Pista 3:")
        print("  def insert(self, valor):")
        print("      if not self.raiz:")
        print("          self.raiz = NodoArbol(valor)")
        print("          return")
        print("      self._insert(self.raiz, valor)")
        print()
        print("  def _insert(self, nodo, valor):")
        print("      if valor < nodo.valor:")
        print("          if nodo.izquierdo:")
        print("              self._insert(nodo.izquierdo, valor)")
        print("          else:")
        print("              nodo.izquierdo = NodoArbol(valor)")
        print("      else:")
        print("          if nodo.derecho:")
        print("              self._insert(nodo.derecho, valor)")
        print("          else:")
        print("              nodo.derecho = NodoArbol(valor)")
        return

    print("\nImplementa:")
    print("  1. class NodoArbol (valor, izquierdo, derecho)")
    print("  2. class BST con:")
    print("     - __init__(): self.raiz = None")
    print("     - insert(valor): inserta respetando prop. BST")
    print()
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")


def ejercicio_2(pista=0):
    """🟡 Recorrido inorder"""
    print(">> 🟡 EJERCICIO 2: Recorrido inorder")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1:")
        print("  inorder visita: izquierdo → raiz → derecho")
        print("  def inorder(nodo):")
        print("      if nodo:")
        print("          inorder(nodo.izquierdo)")
        print("          print(nodo.valor, end=' ')")
        print("          inorder(nodo.derecho)")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  En un BST, inorder SIEMPRE imprime ordenado.")
        print("  Prueba con: bst = BST()")
        print("  for v in [5, 3, 7, 2, 4, 6, 8]: bst.insert(v)")
        print("  inorder(bst.raiz)  # 2 3 4 5 6 7 8")
        return
    elif pista == 3:
        print("\n💡 Pista 3:")
        print("  def inorder(nodo):")
        print("      if nodo:")
        print("          inorder(nodo.izquierdo)")
        print("          print(nodo.valor, end=' ')")
        print("          inorder(nodo.derecho)")
        return

    print("\nImplementa la funcion recursiva:")
    print("  def inorder(nodo):")
    print("      # visita: izquierdo, raiz, derecho")
    print()
    print("  Prueba con: 5, 3, 7, 2, 4, 6, 8")
    print("  Resultado esperado: 2 3 4 5 6 7 8")
    print()
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")


def ejercicio_3(pista=0):
    """🔴 Buscar en BST"""
    print(">> 🔴 EJERCICIO 3: Buscar en BST")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1:")
        print("  def buscar(nodo, valor):")
        print("      if not nodo: return False")
        print("      if nodo.valor == valor: return True")
        print("      # decidir que rama explorar segun valor")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  Si valor < nodo.valor → busca en izquierdo")
        print("  Si valor > nodo.valor → busca en derecho")
        print("  Esto descarta la MITAD del arbol en cada paso")
        return
    elif pista == 3:
        print("\n💡 Pista 3:")
        print("  def buscar(nodo, valor):")
        print("      if not nodo:")
        print("          return False")
        print("      if nodo.valor == valor:")
        print("          return True")
        print("      if valor < nodo.valor:")
        print("          return buscar(nodo.izquierdo, valor)")
        print("      else:")
        print("          return buscar(nodo.derecho, valor)")
        return

    print("\nImplementa:")
    print("  def buscar(nodo, valor) -> bool:")
    print()
    print("  Entrada: arbol con [5, 3, 7, 2, 4, 6, 8]")
    print("  buscar(raiz, 4) → True")
    print("  buscar(raiz, 9) → False")
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
