"""
EJERCICIOS - Pilas y Colas
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
# EJERCICIO 1: Implementar un Stack
# ============================================
def ejercicio_1():
    print("=" * 50)
    print(">> EJERCICIO 1: Implementar un Stack (Pila)")
    print("=" * 50)
    print()
    print("Crea una clase Stack usando una lista de Python.")
    print()
    print("  class Stack:")
    print("      def __init__(self)")
    print("      def push(self, item)     - Agrega al tope")
    print("      def pop(self)            - Quita y devuelve el tope")
    print("      def peek(self)           - Ve el tope sin quitarlo")
    print("      def is_empty(self)       - True si esta vacio")
    print("      def size(self)           - Numero de elementos")
    print()
    print("PISTA: En Python, append() y pop() ya funcionan como stack")
    print()
    print("Edita el archivo:")
    print("class Stack:")
    print("    # --- TU CODIGO AQUI ---")

def solucion_1():
    print("SOLUCION - Ejercicio 1")
    print()
    print("```python")
    print("class Stack:")
    print("    def __init__(self):")
    print("        self.items = []")
    print()
    print("    def push(self, item):")
    print("        self.items.append(item)")
    print()
    print("    def pop(self):")
    print("        if self.is_empty():")
    print("            return None")
    print("        return self.items.pop()")
    print()
    print("    def peek(self):")
    print("        if self.is_empty():")
    print("            return None")
    print("        return self.items[-1]")
    print()
    print("    def is_empty(self):")
    print("        return len(self.items) == 0")
    print()
    print("    def size(self):")
    print("        return len(self.items)")
    print()
    print("# Prueba")
    print("s = Stack()")
    print("s.push(1); s.push(2); s.push(3)")
    print("print(s.pop())   # 3")
    print("print(s.peek())  # 2")
    print("print(s.size())  # 2")
    print("```")
    print()
    print("Explicacion:")
    print("Python list ya soporta operaciones de stack con append/pop.")
    print("append agrega al final O(1), pop quita del final O(1).")

# ============================================
# EJERCICIO 2: Implementar una Queue
# ============================================
def ejercicio_2():
    print("=" * 50)
    print(">> EJERCICIO 2: Implementar una Queue (Cola)")
    print("=" * 50)
    print()
    print("Crea una clase Queue usando collections.deque.")
    print()
    print("  class Queue:")
    print("      def __init__(self)")
    print("      def enqueue(self, item)  - Agrega al final")
    print("      def dequeue(self)        - Quita del inicio")
    print("      def front(self)          - Ve el primero")
    print("      def is_empty(self)       - True si esta vacia")
    print("      def size(self)           - Numero de elementos")
    print()
    print("PISTA: deque tiene append() y popleft()")
    print()
    print("Edita el archivo:")
    print("from collections import deque")
    print()
    print("class Queue:")
    print("    # --- TU CODIGO AQUI ---")

def solucion_2():
    print("SOLUCION - Ejercicio 2")
    print()
    print("```python")
    print("from collections import deque")
    print()
    print("class Queue:")
    print("    def __init__(self):")
    print("        self.items = deque()")
    print()
    print("    def enqueue(self, item):")
    print("        self.items.append(item)")
    print()
    print("    def dequeue(self):")
    print("        if self.is_empty():")
    print("            return None")
    print("        return self.items.popleft()")
    print()
    print("    def front(self):")
    print("        if self.is_empty():")
    print("            return None")
    print("        return self.items[0]")
    print()
    print("    def is_empty(self):")
    print("        return len(self.items) == 0")
    print()
    print("    def size(self):")
    print("        return len(self.items)")
    print()
    print("# Prueba")
    print("q = Queue()")
    print("q.enqueue('a'); q.enqueue('b'); q.enqueue('c')")
    print("print(q.dequeue())  # a")
    print("print(q.front())    # b")
    print("```")
    print()
    print("Explicacion:")
    print("deque (double-ended queue) es optimo para queues.")
    print("append es O(1) y popleft tambien es O(1).")
    print("Usar list con pop(0) seria O(n) por el desplazamiento.")

# ============================================
# EJERCICIO 3: Parentesis balanceados
# ============================================
def ejercicio_3():
    print("=" * 50)
    print(">> EJERCICIO 3: Parentesis balanceados")
    print("=" * 50)
    print()
    print("Usa un Stack para verificar si los parentesis")
    print("en una cadena estan balanceados.")
    print()
    print("Caracteres: () [] {}")
    print()
    print("Ejemplos:")
    print("  '()'        -> Balanceado")
    print("  '([])'      -> Balanceado")
    print("  '{[()]}'    -> Balanceado")
    print("  '(}'        -> No balanceado")
    print("  '([)]'      -> No balanceado")
    print()
    print("PISTA: Apila los de apertura, desapila al encontrar cierre")
    print()
    print("Edita el archivo:")
    print("def is_balanced(s):")
    print("    # --- TU CODIGO AQUI ---")

def solucion_3():
    print("SOLUCION - Ejercicio 3")
    print()
    print("```python")
    print("def is_balanced(s):")
    print("    stack = []")
    print("    pairs = {')': '(', ']': '[', '}': '{'}")
    print()
    print("    for char in s:")
    print("        if char in '({[':")
    print("            stack.append(char)")
    print("        elif char in ')}]':")
    print("            if not stack or stack.pop() != pairs[char]:")
    print("                return False")
    print()
    print("    return len(stack) == 0")
    print()
    print("# Pruebas")
    print("print(is_balanced('()'))      # True")
    print("print(is_balanced('([])'))    # True")
    print("print(is_balanced('{[()]}'))  # True")
    print("print(is_balanced('(}'))      # False")
    print("print(is_balanced('([)]'))    # False")
    print("```")
    print()
    print("Explicacion:")
    print("1. Si es caracter de apertura, lo apilamos")
    print("2. Si es de cierre, verificamos que el tope del stack")
    print("   sea su par correspondiente")
    print("3. Al final, el stack debe estar vacio")
    print()
    print("Complejidad: O(n) tiempo, O(n) memoria")

# ============================================
# MENU PRINCIPAL
# ============================================
def menu():
    while True:
        print()
        print("=" * 50)
        print("MENU - Pilas y Colas")
        print("=" * 50)
        print("1. Implementar un Stack")
        print("2. Implementar una Queue")
        print("3. Parentesis balanceados")
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
                "append y pop hacen que una lista funcione como stack LIFO",
                "deque con append y popleft es ideal para queue FIFO",
                "Usa un diccionario para mapear cierre -> apertura"
            ]
            print(f"PISTA: {pistas[num - 1]}")
        else:
            [ejercicio_1, ejercicio_2, ejercicio_3][num - 1]()

if __name__ == "__main__":
    main()
