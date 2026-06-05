"""
SOLUCIONES - Arboles
Ejecuta: python scripts/runner.py 3 4 [ejercicio] -s
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    print(">> SOLUCION 1: NodoArbol y BST con insert")
    print("-" * 40)
    print("class NodoArbol:")
    print("    def __init__(self, valor):")
    print("        self.valor = valor")
    print("        self.izquierdo = None")
    print("        self.derecho = None")
    print()
    print("class BST:")
    print("    def __init__(self):")
    print("        self.raiz = None")
    print()
    print("    def insert(self, valor):")
    print("        if not self.raiz:")
    print("            self.raiz = NodoArbol(valor)")
    print("            return")
    print("        self._insert(self.raiz, valor)")
    print()
    print("    def _insert(self, nodo, valor):")
    print("        if valor < nodo.valor:")
    print("            if nodo.izquierdo:")
    print("                self._insert(nodo.izquierdo, valor)")
    print("            else:")
    print("                nodo.izquierdo = NodoArbol(valor)")
    print("        else:")
    print("            if nodo.derecho:")
    print("                self._insert(nodo.derecho, valor)")
    print("            else:")
    print("                nodo.derecho = NodoArbol(valor)")
    print()
    print("Explicacion: Valores menores van a la izquierda,")
    print("mayores o iguales van a la derecha.")

def solucion_2():
    print(">> SOLUCION 2: Recorrido inorder")
    print("-" * 40)
    print("def inorder(nodo):")
    print("    if nodo:")
    print("        inorder(nodo.izquierdo)")
    print("        print(nodo.valor, end=' ')")
    print("        inorder(nodo.derecho)")
    print()
    print("Uso:")
    print("bst = BST()")
    print("for v in [5, 3, 7, 2, 4, 6, 8]:")
    print("    bst.insert(v)")
    print("inorder(bst.raiz)  # 2 3 4 5 6 7 8")
    print()
    print("Explicacion: inorder visita izquierdo, raiz, derecho.")
    print("En un BST, esto devuelve los valores ordenados.")

def solucion_3():
    print(">> SOLUCION 3: Buscar en BST")
    print("-" * 40)
    print("def buscar(nodo, valor):")
    print("    if not nodo:")
    print("        return False")
    print("    if nodo.valor == valor:")
    print("        return True")
    print("    if valor < nodo.valor:")
    print("        return buscar(nodo.izquierdo, valor)")
    print("    else:")
    print("        return buscar(nodo.derecho, valor)")
    print()
    print("Explicacion: Aprovecha la propiedad del BST.")
    print("Comparamos con la raiz y decidimos que rama explorar.")
    print("Complejidad: O(log n) en promedio, O(n) en el peor caso.")

if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
