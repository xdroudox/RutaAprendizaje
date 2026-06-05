"""
SOLUCIONES - Pilas y Colas
Ejecuta: python scripts/runner.py 3 3 [ejercicio] -s
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    print(">> SOLUCION 1: Stack con push/pop/peek")
    print("-" * 40)
    print("class Stack:")
    print("    def __init__(self):")
    print("        self.items = []")
    print()
    print("    def push(self, item):")
    print("        self.items.append(item)")
    print()
    print("    def pop(self):")
    print("        if not self.is_empty():")
    print("            return self.items.pop()")
    print("        return None")
    print()
    print("    def peek(self):")
    print("        if not self.is_empty():")
    print("            return self.items[-1]")
    print("        return None")
    print()
    print("    def is_empty(self):")
    print("        return len(self.items) == 0")
    print()
    print("    def size(self):")
    print("        return len(self.items)")
    print()
    print("Explicacion: LIFO - El ultimo en entrar es el primero en salir.")
    print("Internamente usamos una list de Python.")

def solucion_2():
    print(">> SOLUCION 2: Queue con enqueue/dequeue")
    print("-" * 40)
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
    print("        if not self.is_empty():")
    print("            return self.items.popleft()")
    print("        return None")
    print()
    print("    def front(self):")
    print("        if not self.is_empty():")
    print("            return self.items[0]")
    print("        return None")
    print()
    print("    def is_empty(self):")
    print("        return len(self.items) == 0")
    print()
    print("Explicacion: FIFO - El primero en entrar es el primero en salir.")
    print("Usamos deque de collections para eficiencia O(1) en ambos extremos.")

def solucion_3():
    print(">> SOLUCION 3: Parentesis balanceados con Stack")
    print("-" * 40)
    print("def parentesis_balanceados(expr):")
    print("    stack = Stack()")
    print("    pares = {')': '(', ']': '[', '}': '{'}")
    print("    for char in expr:")
    print("        if char in '([{':")
    print("            stack.push(char)")
    print("        elif char in ')]}':")
    print("            if stack.is_empty() or stack.pop() != pares[char]:")
    print("                return False")
    print("    return stack.is_empty()")
    print()
    print("Explicacion: Cada apertura se apila, cada cierre debe coincidir")
    print("con la ultima apertura. Si al final la pila esta vacia, OK.")

if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
