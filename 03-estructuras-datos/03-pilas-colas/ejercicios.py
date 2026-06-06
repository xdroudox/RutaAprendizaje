"""
EJERCICIOS - Pilas y Colas
Ejecuta desde raiz: python scripts/runner.py 3 3 [ejercicio]

Niveles:
  🟢 Ej 1: Implementar Stack con list
  🟡 Ej 2: Implementar Queue con deque
  🔴 Ej 3: Verificar parentesis balanceados

Pistas: python scripts/runner.py 3 3 N -p [1|2|3]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1(pista=0):
    """🟢 Stack con push/pop/peek"""
    print(">> 🟢 EJERCICIO 1: Stack con push/pop/peek")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1:")
        print("  Internamente usa una list de Python:")
        print("  self.items = []")
        print("  push: self.items.append(item)")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  pop: self.items.pop()  # Quita el ULTIMO")
        print("  peek: self.items[-1]   # Ultimo elemento")
        print("  is_empty: len(self.items) == 0")
        print("  pop y peek deben verificar is_empty antes")
        return
    elif pista == 3:
        print("\n💡 Pista 3:")
        print("  class Stack:")
        print("      def __init__(self): self.items = []")
        print("      def push(self, item): self.items.append(item)")
        print("      def pop(self):")
        print("          return None if self.is_empty() else self.items.pop()")
        print("      def peek(self):")
        print("          return None if self.is_empty() else self.items[-1]")
        print("      def is_empty(self): return len(self.items) == 0")
        return

    print("\nCrea la clase Stack:")
    print("  - __init__(): self.items = []")
    print("  - push(item): agrega a la cima")
    print("  - pop(): quita y devuelve cima (None si vacio)")
    print("  - peek(): ve cima sin quitar (None si vacio)")
    print("  - is_empty(): True/False")
    print()
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")


def ejercicio_2(pista=0):
    """🟡 Queue con enqueue/dequeue"""
    print(">> 🟡 EJERCICIO 2: Queue con enqueue/dequeue")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1:")
        print("  Importa deque: from collections import deque")
        print("  self.items = deque()")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  enqueue: self.items.append(item)")
        print("  dequeue: self.items.popleft()   # ← O(1)")
        print("  front: self.items[0]")
        return
    elif pista == 3:
        print("\n💡 Pista 3:")
        print("  from collections import deque")
        print("  class Queue:")
        print("      def __init__(self): self.items = deque()")
        print("      def enqueue(self, item): self.items.append(item)")
        print("      def dequeue(self):")
        print("          return None if self.is_empty() else self.items.popleft()")
        print("      def front(self):")
        print("          return None if self.is_empty() else self.items[0]")
        print("      def is_empty(self): return len(self.items) == 0")
        return

    print("\nCrea la clase Queue:")
    print("  - Usa deque de collections (no list)")
    print("  - enqueue(item): agrega al final")
    print("  - dequeue(): quita y devuelve el primero (None si vacio)")
    print("  - front(): ve primero sin quitar (None si vacio)")
    print("  - is_empty(): True/False")
    print()
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")


def ejercicio_3(pista=0):
    """🔴 Parentesis balanceados con Stack"""
    print(">> 🔴 EJERCICIO 3: Verificar parentesis balanceados")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1:")
        print("  Recorre la expresion caracter por caracter:")
        print("  - Si es apertura ([{ → apila")
        print("  - Si es cierre )]} → verifica que coincida")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  Usa un diccionario de pares:")
        print("  pares = {')': '(', ']': '[', '}': '{'}")
        print("  Si el cierre no coincide con lo que hay en la cima → False")
        return
    elif pista == 3:
        print("\n💡 Pista 3:")
        print("  from collections import deque  # o tu clase Stack")
        print()
        print("  def esta_balanceada(expr):")
        print("      stack = []")
        print("      pares = {')': '(', ']': '[', '}': '{'}")
        print("      for c in expr:")
        print("          if c in '([{': stack.append(c)")
        print("          elif c in ')]}':")
        print("              if not stack or stack.pop() != pares[c]:")
        print("                  return False")
        print("      return len(stack) == 0")
        return

    print("\nImplementa:")
    print("  def esta_balanceada(expr):")
    print()
    print("  Entrada: '([])'   →  True")
    print("  Entrada: '([)]'   →  False")
    print("  Entrada: '{[]()}' →  True")
    print()
    print("Usa un Stack para rastrear las aperturas.")
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
