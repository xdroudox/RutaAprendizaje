"""
EJERCICIOS - Arrays y Listas Enlazadas
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
# EJERCICIO 1: Lista Simplemente Enlazada
# ============================================
def ejercicio_1():
    print("=" * 50)
    print(">> EJERCICIO 1: Lista Simplemente Enlazada")
    print("=" * 50)
    print()
    print("Implementa una SinglyLinkedList con los siguientes metodos:")
    print()
    print("  class Node:")
    print("      def __init__(self, data):")
    print("          self.data = data")
    print("          self.next = None")
    print()
    print("  class SinglyLinkedList:")
    print("      def __init__(self)")
    print("      def insert(self, data)    - Agrega al final")
    print("      def delete(self, data)    - Elimina por valor")
    print("      def search(self, data)    - Busca y devuelve True/False")
    print("      def print_list(self)      - Muestra la lista")
    print()
    print("PISTA: Para insertar al final, recorre hasta el ultimo nodo")
    print()
    print("Edita el archivo y escribe tu codigo:")
    print("class Node:")
    print("    # --- TU CODIGO AQUI ---")
    print()
    print("class SinglyLinkedList:")
    print("    # --- TU CODIGO AQUI ---")

def solucion_1():
    print("SOLUCION - Ejercicio 1")
    print()
    print("```python")
    print("class Node:")
    print("    def __init__(self, data):")
    print("        self.data = data")
    print("        self.next = None")
    print()
    print("class SinglyLinkedList:")
    print("    def __init__(self):")
    print("        self.head = None")
    print()
    print("    def insert(self, data):")
    print("        new_node = Node(data)")
    print("        if not self.head:")
    print("            self.head = new_node")
    print("            return")
    print("        current = self.head")
    print("        while current.next:")
    print("            current = current.next")
    print("        current.next = new_node")
    print()
    print("    def delete(self, data):")
    print("        if not self.head:")
    print("            return")
    print("        if self.head.data == data:")
    print("            self.head = self.head.next")
    print("            return")
    print("        current = self.head")
    print("        while current.next:")
    print("            if current.next.data == data:")
    print("                current.next = current.next.next")
    print("                return")
    print("            current = current.next")
    print()
    print("    def search(self, data):")
    print("        current = self.head")
    print("        while current:")
    print("            if current.data == data:")
    print("                return True")
    print("            current = current.next")
    print("        return False")
    print()
    print("    def print_list(self):")
    print("        current = self.head")
    print("        while current:")
    print("            print(f'{current.data} -> ', end='')")
    print("            current = current.next")
    print("        print('None')")
    print("```")
    print()
    print("Explicacion:")
    print("Cada nodo tiene un puntero al siguiente. La lista mantiene")
    print("referencia solo al head. Insertar al final es O(n), pero")
    print("insertar al inicio seria O(1).")

# ============================================
# EJERCICIO 2: Lista Doblemente Enlazada
# ============================================
def ejercicio_2():
    print("=" * 50)
    print(">> EJERCICIO 2: Lista Doblemente Enlazada")
    print("=" * 50)
    print()
    print("Implementa una DoublyLinkedList:")
    print()
    print("  class Node:")
    print("      def __init__(self, data):")
    print("          self.data = data")
    print("          self.prev = None")
    print("          self.next = None")
    print()
    print("  class DoublyLinkedList:")
    print("      def append(self, data)     - Agrega al final")
    print("      def prepend(self, data)    - Agrega al inicio")
    print("      def print_forward(self)    - Muestra head -> tail")
    print("      def print_backward(self)   - Muestra tail -> head")
    print()
    print("PISTA: Manten referencia a head y tail")
    print()
    print("Edita el archivo:")
    print("# --- TU CODIGO AQUI ---")

def solucion_2():
    print("SOLUCION - Ejercicio 2")
    print()
    print("```python")
    print("class Node:")
    print("    def __init__(self, data):")
    print("        self.data = data")
    print("        self.prev = None")
    print("        self.next = None")
    print()
    print("class DoublyLinkedList:")
    print("    def __init__(self):")
    print("        self.head = None")
    print("        self.tail = None")
    print()
    print("    def append(self, data):")
    print("        new_node = Node(data)")
    print("        if not self.head:")
    print("            self.head = new_node")
    print("            self.tail = new_node")
    print("            return")
    print("        self.tail.next = new_node")
    print("        new_node.prev = self.tail")
    print("        self.tail = new_node")
    print()
    print("    def prepend(self, data):")
    print("        new_node = Node(data)")
    print("        if not self.head:")
    print("            self.head = new_node")
    print("            self.tail = new_node")
    print("            return")
    print("        self.head.prev = new_node")
    print("        new_node.next = self.head")
    print("        self.head = new_node")
    print()
    print("    def print_forward(self):")
    print("        current = self.head")
    print("        while current:")
    print("            print(f'{current.data} <-> ', end='')")
    print("            current = current.next")
    print("        print('None')")
    print()
    print("    def print_backward(self):")
    print("        current = self.tail")
    print("        while current:")
    print("            print(f'{current.data} <-> ', end='')")
    print("            current = current.prev")
    print("        print('None')")
    print("```")
    print()
    print("Explicacion:")
    print("Cada nodo tiene punteros al anterior y siguiente.")
    print("Con head y tail, insertar en ambos extremos es O(1).")
    print("print_backward recorre desde tail hacia atras con prev.")

# ============================================
# EJERCICIO 3: Invertir lista enlazada
# ============================================
def ejercicio_3():
    print("=" * 50)
    print(">> EJERCICIO 3: Invertir lista enlazada")
    print("=" * 50)
    print()
    print("Dada una SinglyLinkedList, implementa una funcion")
    print("para INVERTIRLA (reverse).")
    print()
    print("Ejemplo:")
    print("  1 -> 2 -> 3 -> None")
    print("  invertir -> 3 -> 2 -> 1 -> None")
    print()
    print("PISTA: Usa 3 punteros: prev, current, next")
    print()
    print("Edita el archivo:")
    print("def reverse_linked_list(head):")
    print("    # --- TU CODIGO AQUI ---")

def solucion_3():
    print("SOLUCION - Ejercicio 3")
    print()
    print("```python")
    print("def reverse_linked_list(head):")
    print("    prev = None")
    print("    current = head")
    print("    while current:")
    print("        next_node = current.next")
    print("        current.next = prev")
    print("        prev = current")
    print("        current = next_node")
    print("    return prev  # Nueva cabeza")
    print("```")
    print()
    print("Explicacion:")
    print("Usamos 3 punteros para no perder la referencia:")
    print("- prev: nodo anterior (inicia como None)")
    print("- current: nodo actual")
    print("- next_node: guarda el siguiente antes de romper la referencia")
    print()
    print("En cada paso, current.next apunta a prev, y avanzamos.")
    print("Al final, prev es la nueva cabeza de la lista invertida.")
    print("Complejidad: O(n) tiempo, O(1) memoria.")

# ============================================
# MENU PRINCIPAL
# ============================================
def menu():
    while True:
        print()
        print("=" * 50)
        print("MENU - Arrays y Listas Enlazadas")
        print("=" * 50)
        print("1. Lista Simplemente Enlazada")
        print("2. Lista Doblemente Enlazada")
        print("3. Invertir lista enlazada")
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
                "Para insertar al final, recorre hasta que current.next sea None",
                "Manten referencia a head y tail para insercion O(1) en extremos",
                "Guarda next antes de cambiar la referencia, o perderas el resto"
            ]
            print(f"PISTA: {pistas[num - 1]}")
        else:
            [ejercicio_1, ejercicio_2, ejercicio_3][num - 1]()

if __name__ == "__main__":
    main()
