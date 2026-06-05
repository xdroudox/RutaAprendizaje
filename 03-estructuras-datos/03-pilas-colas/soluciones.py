"""
SOLUCIONES - Pilas y Colas
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
    print("SOLUCION - Ejercicio 1: Implementar un Stack")
    print("=" * 50)
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
    print("        return None if self.is_empty() else self.items.pop()")
    print()
    print("    def peek(self):")
    print("        return None if self.is_empty() else self.items[-1]")
    print()
    print("    def is_empty(self):")
    print("        return len(self.items) == 0")
    print()
    print("    def size(self):")
    print("        return len(self.items)")
    print("```")
    print()
    print("Complejidad de todas las operaciones: O(1) amortizado.")
    print()
    print("Aplicaciones del Stack:")
    print("- Call stack de funciones")
    print("- Undo/Redo en editores")
    print("- Evaluacion de expresiones (notacion polaca)")
    print("- Navegacion forward/backward en browsers")

def solucion_2():
    print("=" * 50)
    print("SOLUCION - Ejercicio 2: Implementar una Queue")
    print("=" * 50)
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
    print("        return None if self.is_empty() else self.items.popleft()")
    print()
    print("    def front(self):")
    print("        return None if self.is_empty() else self.items[0]")
    print()
    print("    def is_empty(self):")
    print("        return len(self.items) == 0")
    print()
    print("    def size(self):")
    print("        return len(self.items)")
    print("```")
    print()
    print("Por que NO usar list para queues?")
    print("list.pop(0) requiere desplazar todos los elementos -> O(n)")
    print("deque.popleft() es O(1) porque usa una lista doblemente enlazada")
    print()
    print("Aplicaciones de Queue:")
    print("- Buffers (teclado, audio, video)")
    print("- Colas de impresion")
    print("- BFS en grafos")
    print("- Sistemas de tickets")

def solucion_3():
    print("=" * 50)
    print("SOLUCION - Ejercicio 3: Parentesis balanceados")
    print("=" * 50)
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
    print("```")
    print()
    print("Pruebas:")
    print("  is_balanced('()')        -> True")
    print("  is_balanced('([])')      -> True")
    print("  is_balanced('{[()]}')    -> True")
    print("  is_balanced('(')         -> False (stack no vacio)")
    print("  is_balanced(')')         -> False (stack vacio al cerrar)")
    print("  is_balanced('([)]')      -> False (orden incorrecto)")
    print()
    print("Complejidad: O(n) tiempo, O(n) espacio en el peor caso.")
    print()
    print("Este problema aparece en MUCHAS entrevistas tecnicas.")
    print("Es la aplicacion clasica del stack.")

def menu():
    while True:
        print()
        print("=" * 50)
        print("SOLUCIONES - Pilas y Colas")
        print("=" * 50)
        print("1. Implementar un Stack")
        print("2. Implementar una Queue")
        print("3. Parentesis balanceados")
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
