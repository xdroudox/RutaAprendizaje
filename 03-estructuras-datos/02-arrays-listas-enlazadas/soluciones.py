"""
SOLUCIONES - Arrays y Listas Enlazadas
Ejecuta: python scripts/runner.py 3 2 [ejercicio] -s
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    print(">> SOLUCION 1: SinglyLinkedList con append y display")
    print("-" * 40)
    print("class Nodo:")
    print("    def __init__(self, dato):")
    print("        self.dato = dato")
    print("        self.siguiente = None")
    print()
    print("class SinglyLinkedList:")
    print("    def __init__(self):")
    print("        self.cabeza = None")
    print()
    print("    def append(self, dato):")
    print("        nuevo = Nodo(dato)")
    print("        if not self.cabeza:")
    print("            self.cabeza = nuevo")
    print("            return")
    print("        actual = self.cabeza")
    print("        while actual.siguiente:")
    print("            actual = actual.siguiente")
    print("        actual.siguiente = nuevo")
    print()
    print("    def display(self):")
    print("        actual = self.cabeza")
    print("        while actual:")
    print("            print(actual.dato, end=' -> ')")
    print("            actual = actual.siguiente")
    print("        print('None')")
    print()
    print("    def to_list(self):")
    print("        resultado = []")
    print("        actual = self.cabeza")
    print("        while actual:")
    print("            resultado.append(actual.dato)")
    print("            actual = actual.siguiente")
    print("        return resultado")

def solucion_2():
    print(">> SOLUCION 2: Eliminar duplicados de lista enlazada")
    print("-" * 40)
    print("def eliminar_duplicados(lista):")
    print("    if not lista.cabeza:")
    print("        return")
    print("    vistos = set()")
    print("    actual = lista.cabeza")
    print("    vistos.add(actual.dato)")
    print("    while actual.siguiente:")
    print("        if actual.siguiente.dato in vistos:")
    print("            actual.siguiente = actual.siguiente.siguiente")
    print("        else:")
    print("            vistos.add(actual.siguiente.dato)")
    print("            actual = actual.siguiente")
    print()
    print("Explicacion: Usamos un set para trackear valores vistos.")
    print("Si el siguiente nodo ya fue visto, lo saltamos.")

def solucion_3():
    print(">> SOLUCION 3: Revertir lista enlazada")
    print("-" * 40)
    print("def revertir(lista):")
    print("    anterior = None")
    print("    actual = lista.cabeza")
    print("    while actual:")
    print("        siguiente = actual.siguiente")
    print("        actual.siguiente = anterior")
    print("        anterior = actual")
    print("        actual = siguiente")
    print("    lista.cabeza = anterior")
    print()
    print("Explicacion: Recorremos la lista reasignando punteros.")
    print("En cada paso, invertimos el enlace del nodo actual")
    print("para que apunte al nodo anterior en vez del siguiente.")

if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
