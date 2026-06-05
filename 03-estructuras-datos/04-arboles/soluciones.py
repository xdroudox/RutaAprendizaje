"""
SOLUCIONES - Arboles
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
    print("SOLUCION - Ejercicio 1: Implementar un BST")
    print("=" * 50)
    print()
    print("```python")
    print("class Node:")
    print("    def __init__(self, value):")
    print("        self.value = value")
    print("        self.left = None")
    print("        self.right = None")
    print()
    print("class BinarySearchTree:")
    print("    def __init__(self):")
    print("        self.root = None")
    print()
    print("    def insert(self, value):")
    print("        if not self.root:")
    print("            self.root = Node(value)")
    print("            return")
    print("        self._insert_rec(self.root, value)")
    print()
    print("    def _insert_rec(self, node, value):")
    print("        if value < node.value:")
    print("            if not node.left:")
    print("                node.left = Node(value)")
    print("            else:")
    print("                self._insert_rec(node.left, value)")
    print("        else:")
    print("            if not node.right:")
    print("                node.right = Node(value)")
    print("            else:")
    print("                self._insert_rec(node.right, value)")
    print()
    print("    def search(self, value):")
    print("        return self._search_rec(self.root, value)")
    print()
    print("    def _search_rec(self, node, value):")
    print("        if not node: return False")
    print("        if node.value == value: return True")
    print("        if value < node.value:")
    print("            return self._search_rec(node.left, value)")
    print("        return self._search_rec(node.right, value)")
    print()
    print("# Prueba")
    print("bst = BinarySearchTree()")
    print("for v in [10, 5, 15, 3, 7, 20]: bst.insert(v)")
    print("print(bst.search(7))   # True")
    print("print(bst.search(99))  # False")
    print("```")
    print()
    print("Complejidad: O(log n) en promedio, O(n) en peor caso.")
    print("Esto depende de la altura del arbol.")

def solucion_2():
    print("=" * 50)
    print("SOLUCION - Ejercicio 2: Recorridos del arbol")
    print("=" * 50)
    print()
    print("```python")
    print("def inorder(node):")
    print("    if node:")
    print("        inorder(node.left)")
    print("        print(node.value, end=' ')")
    print("        inorder(node.right)")
    print()
    print("def preorder(node):")
    print("    if node:")
    print("        print(node.value, end=' ')")
    print("        preorder(node.left)")
    print("        preorder(node.right)")
    print()
    print("def postorder(node):")
    print("    if node:")
    print("        postorder(node.left)")
    print("        postorder(node.right)")
    print("        print(node.value, end=' ')")
    print("```")
    print()
    print("Resultados para el arbol de ejemplo:")
    print()
    print("        10")
    print("       /  \\")
    print("      5    15")
    print("     / \\     \\")
    print("    3   7     20")
    print()
    print("  inorder:   3 5 7 10 15 20  (ordenado!)")
    print("  preorder:  10 5 3 7 15 20")
    print("  postorder: 3 7 5 20 15 10")
    print()
    print("Aplicaciones:")
    print("- Inorder: BST -> valores ordenados")
    print("- Preorder: serializar arbol para reconstruccion")
    print("- Postorder: eliminar nodos de hoja a raiz")

def solucion_3():
    print("=" * 50)
    print("SOLUCION - Ejercicio 3: Minimo y maximo en BST")
    print("=" * 50)
    print()
    print("```python")
    print("def find_min(root):")
    print("    if not root: return None")
    print("    current = root")
    print("    while current.left:")
    print("        current = current.left")
    print("    return current.value")
    print()
    print("def find_max(root):")
    print("    if not root: return None")
    print("    current = root")
    print("    while current.right:")
    print("        current = current.right")
    print("    return current.value")
    print()
    print("# Prueba")
    print("bst = BinarySearchTree()")
    print("for v in [10, 5, 15, 3, 7, 20]: bst.insert(v)")
    print("print(find_min(bst.root))  # 3")
    print("print(find_max(bst.root))  # 20")
    print("```")
    print()
    print("Version recursiva:")
    print("  def find_min_rec(node):")
    print("      if not node: return None")
    print("      if not node.left: return node.value")
    print("      return find_min_rec(node.left)")
    print()
    print("Complejidad: O(h) donde h es la altura del arbol.")
    print("En un arbol balanceado: O(log n).")
    print("En un arbol degenerado (lista enlazada): O(n).")

def menu():
    while True:
        print()
        print("=" * 50)
        print("SOLUCIONES - Arboles")
        print("=" * 50)
        print("1. Implementar un BST")
        print("2. Recorridos del arbol")
        print("3. Minimo y maximo en BST")
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
