"""
EJERCICIOS - Arboles
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
# EJERCICIO 1: Implementar BST
# ============================================
def ejercicio_1():
    print("=" * 50)
    print(">> EJERCICIO 1: Implementar un BST")
    print("=" * 50)
    print()
    print("Crea la clase BinarySearchTree con metodos insert y search.")
    print()
    print("  class Node:")
    print("      def __init__(self, value):")
    print("          self.value = value")
    print("          self.left = None")
    print("          self.right = None")
    print()
    print("  class BinarySearchTree:")
    print("      def __init__(self)")
    print("      def insert(self, value) - Inserta manteniendo propiedad BST")
    print("      def search(self, value) - Devuelve True/False")
    print()
    print("Propiedad BST: izquierda < raiz < derecha")
    print()
    print("PISTA: Si value < raiz, ve a la izquierda; si no, a la derecha")
    print()
    print("Edita el archivo:")
    print("class Node:")
    print("    # --- TU CODIGO AQUI ---")
    print()
    print("class BinarySearchTree:")
    print("    # --- TU CODIGO AQUI ---")

def solucion_1():
    print("SOLUCION - Ejercicio 1")
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
    print("        if not node:")
    print("            return False")
    print("        if node.value == value:")
    print("            return True")
    print("        if value < node.value:")
    print("            return self._search_rec(node.left, value)")
    print("        return self._search_rec(node.right, value)")
    print("```")
    print()
    print("Complejidad: O(log n) promedio, O(n) peor caso (arbol degenerado)")

# ============================================
# EJERCICIO 2: Recorridos del arbol
# ============================================
def ejercicio_2():
    print("=" * 50)
    print(">> EJERCICIO 2: Recorridos del arbol")
    print("=" * 50)
    print()
    print("Implementa las 3 funciones de recorrido para un BST:")
    print()
    print("  def inorder(node):     # izquierda, raiz, derecha")
    print("  def preorder(node):    # raiz, izquierda, derecha")
    print("  def postorder(node):   # izquierda, derecha, raiz")
    print()
    print("Para el arbol:")
    print("        10")
    print("       /  \\")
    print("      5    15")
    print("     / \\     \\")
    print("    3   7     20")
    print()
    print("Los resultados deben ser:")
    print("  inorder:   3, 5, 7, 10, 15, 20")
    print("  preorder:  10, 5, 3, 7, 15, 20")
    print("  postorder: 3, 7, 5, 20, 15, 10")
    print()
    print("PISTA: Cada funcion recibe un nodo y verifica si es None")
    print()
    print("Edita el archivo:")
    print("def inorder(node):")
    print("    # --- TU CODIGO AQUI ---")

def solucion_2():
    print("SOLUCION - Ejercicio 2")
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
    print()
    print("# Prueba")
    print("bst = BinarySearchTree()")
    print("for v in [10, 5, 15, 3, 7, 20]:")
    print("    bst.insert(v)")
    print("print('Inorder:'); inorder(bst.root)   # 3 5 7 10 15 20")
    print("print('Preorder:'); preorder(bst.root) # 10 5 3 7 15 20")
    print("print('Postorder:'); postorder(bst.root) # 3 7 5 20 15 10")
    print("```")
    print()
    print("Usos de cada recorrido:")
    print("- Inorder: devuelve valores ordenados en BST")
    print("- Preorder: usado para copiar/serializar arboles")
    print("- Postorder: usado para eliminar arboles (hojas primero)")

# ============================================
# EJERCICIO 3: Minimo y maximo en BST
# ============================================
def ejercicio_3():
    print("=" * 50)
    print(">> EJERCICIO 3: Minimo y maximo en BST")
    print("=" * 50)
    print()
    print("Implementa funciones para encontrar el valor minimo")
    print("y maximo en un arbol binario de busqueda.")
    print()
    print("  def find_min(root):")
    print("  def find_max(root):")
    print()
    print("Para el arbol:")
    print("        10")
    print("       /  \\")
    print("      5    15")
    print("     / \\     \\")
    print("    3   7     20")
    print()
    print("Minimo: 3")
    print("Maximo: 20")
    print()
    print("PISTA: En un BST, el minimo esta en la hoja mas izquierda")
    print()
    print("Edita el archivo:")
    print("def find_min(root):")
    print("    # --- TU CODIGO AQUI ---")
    print()
    print("def find_max(root):")
    print("    # --- TU CODIGO AQUI ---")

def solucion_3():
    print("SOLUCION - Ejercicio 3")
    print()
    print("```python")
    print("def find_min(root):")
    print("    if not root:")
    print("        return None")
    print("    current = root")
    print("    while current.left:")
    print("        current = current.left")
    print("    return current.value")
    print()
    print("def find_max(root):")
    print("    if not root:")
    print("        return None")
    print("    current = root")
    print("    while current.right:")
    print("        current = current.right")
    print("    return current.value")
    print()
    print("# Version recursiva")
    print("def find_min_rec(node):")
    print("    if not node:")
    print("        return None")
    print("    if not node.left:")
    print("        return node.value")
    print("    return find_min_rec(node.left)")
    print("```")
    print()
    print("Explicacion:")
    print("En un BST, el minimo siempre esta en la rama izquierda")
    print("mas profunda, y el maximo en la rama derecha mas profunda.")
    print("Propiedad del BST: todo hijo izquierdo < padre < hijo derecho.")
    print("Complejidad: O(h) donde h es la altura del arbol.")

# ============================================
# MENU PRINCIPAL
# ============================================
def menu():
    while True:
        print()
        print("=" * 50)
        print("MENU - Arboles")
        print("=" * 50)
        print("1. Implementar un BST")
        print("2. Recorridos del arbol")
        print("3. Minimo y maximo en BST")
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
                "Compara el valor con el nodo actual: menor ve a la izquierda, mayor a la derecha",
                "Inorder = izq-raiz-der, Preorder = raiz-izq-der, Postorder = izq-der-raiz",
                "En un BST, el minimo esta siempre a la izquierda"
            ]
            print(f"PISTA: {pistas[num - 1]}")
        else:
            [ejercicio_1, ejercicio_2, ejercicio_3][num - 1]()

if __name__ == "__main__":
    main()
