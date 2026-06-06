"""
SOLUCIONES - Pilas y Colas
Ejecuta: python scripts/runner.py 3 3 [ejercicio] -s
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: Stack")
    print("=" * 50)

    print("""
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
""")

    print("--- EXPLICACION ---")
    print("""
- Internamente usamos una list de Python como almacenamiento.
- push(): append() agrega al FINAL de la lista (cima de la pila).
- pop(): pop() sin argumentos quita el ULTIMO elemento.
  Si la pila esta vacia, devolvemos None (evita error).
- peek(): items[-1] accede al ultimo elemento SIN quitarlo.
- is_empty(): verifica si la lista esta vacia.

Complejidad: TODAS las operaciones son O(1).

Ejemplo de uso:
  s = Stack()
  s.push(10)           # [10]
  s.push(20)           # [10, 20]
  s.push(30)           # [10, 20, 30]
  s.pop()              # 30, queda [10, 20]
  s.peek()             # 20
""")


def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: Queue")
    print("=" * 50)

    print("""
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        return None

    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0
""")

    print("--- EXPLICACION ---")
    print("""
- Usamos deque (double-ended queue) de collections en vez de list.
  ¿Por que? Porque list.pop(0) es O(n) — desplaza todos los elementos.
  deque.popleft() es O(1) — optimizado para ambos extremos.

- enqueue(): append agrega a la DERECHA del deque.
- dequeue(): popleft() quita de la IZQUIERDA del deque.
  O(1) gracias a deque.
- front(): items[0] accede al primer elemento sin quitarlo.

Ejemplo de uso:
  q = Queue()
  q.enqueue('A')       # deque(['A'])
  q.enqueue('B')       # deque(['A', 'B'])
  q.enqueue('C')       # deque(['A', 'B', 'C'])
  q.dequeue()          # 'A', queda deque(['B', 'C'])
  q.front()            # 'B'
""")


def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: Parentesis balanceados")
    print("=" * 50)

    print("""
def esta_balanceada(expr):
    stack = []
    pares = {')': '(', ']': '[', '}': '{'}

    for char in expr:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack.pop() != pares[char]:
                return False

    return len(stack) == 0
""")

    print("--- EXPLICACION ---")
    print("""
Funcionamiento paso a paso con '{[()]}':

  char | stack antes | accion          | stack despues
  -----|-------------|-----------------|---------------
  {    | []          | apilar          | ['{']
  [    | ['{']       | apilar          | ['{', '[']
  (    | ['{', '[']  | apilar          | ['{', '[', '(']
  )    | ['{', '[', '('] | cierre, pop() = '(' == pares[')']='(' ✓ | ['{', '[']
  ]    | ['{', '[']  | cierre, pop() = '[' == pares[']']='[' ✓ | ['{']
  }    | ['{']       | cierre, pop() = '{' == pares['}']='{' ✓ | []
  FIN  | []          | stack vacio → True ✓

Caso no balanceado '([)]':
  ( → apilar: ['(']
  [ → apilar: ['(', '[']
  ) → pop() = '[' pero pares[')'] = '('  → '[' != '(' → False

Complejidad: O(n) tiempo, O(n) espacio en el peor caso.
  n = longitud de la expresion.
""")


if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
