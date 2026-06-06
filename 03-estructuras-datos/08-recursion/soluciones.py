"""
SOLUCIONES - Recursion
Ejecuta: python scripts/runner.py 3 8 [ejercicio] -s
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: Factorial recursivo")
    print("=" * 50)

    print("""
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
""")

    print("--- EXPLICACION ---")
    print("""
El factorial se define matematicamente como:
  n! = n × (n-1) × (n-2) × ... × 2 × 1
  0! = 1

Traza de factorial(5):
  factorial(5) → 5 * factorial(4)
    factorial(4) → 4 * factorial(3)
      factorial(3) → 3 * factorial(2)
        factorial(2) → 2 * factorial(1)
          factorial(1) → 1  (caso base)
        ← 2 * 1 = 2
      ← 3 * 2 = 6
    ← 4 * 6 = 24
  ← 5 * 24 = 120

Stack de llamadas (memoria):
  Cada llamada recursiva se apila en el CALL STACK.
  factorial(5) → factorial(4) → factorial(3) → factorial(2) → factorial(1)
  Luego se "desapilan" en orden inverso resolviendo las multiplicaciones.

Complejidad: O(n) tiempo, O(n) espacio (por el stack de llamadas).
""")


def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: Fibonacci recursivo")
    print("=" * 50)

    print("""
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
""")

    print("--- EXPLICACION ---")
    print("""
La serie de Fibonacci:
  fib(0) = 0
  fib(1) = 1
  fib(2) = 1
  fib(3) = 2
  fib(4) = 3
  fib(5) = 5
  fib(6) = 8
  fib(7) = 13

Arbol de llamadas para fib(5):
                         fib(5)
                       /        \
                  fib(4)        fib(3)
                 /      \      /     \
            fib(3)    fib(2) fib(2)  fib(1)
           /    \    /   \\ /   \\
       fib(2) fib(1) 1 1  1 1
       /    \\
      1      1

Total de llamadas para fib(n): aproximadamente 2^n
  fib(5) = 15 llamadas
  fib(10) = 177 llamadas
  fib(30) = ~2.6 MILLONES de llamadas

Por eso fibonacci recursivo SIN optimizar tiene O(2^n):
  - fib(40) ya tarda segundos
  - fib(50) tarda minutos/horas

Optimizacion: usar memoizacion o (mejor) iteracion.
""")


def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: Suma de digitos")
    print("=" * 50)

    print("""
def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)
""")

    print("--- EXPLICACION ---")
    print("""
Operadores clave:
  n % 10  → obtiene el ULTIMO digito
  n // 10 → elimina el ULTIMO digito

Traza de suma_digitos(1234):
  Paso 1: n=1234, n%10=4, n//10=123
    return 4 + suma_digitos(123)
  Paso 2: n=123, n%10=3, n//10=12
    return 3 + suma_digitos(12)
  Paso 3: n=12, n%10=2, n//10=1
    return 2 + suma_digitos(1)
  Paso 4: n=1 < 10  → return 1  (caso base)

  Resolviendo:
    suma_digitos(1) = 1
    suma_digitos(12) = 2 + 1 = 3
    suma_digitos(123) = 3 + 3 = 6
    suma_digitos(1234) = 4 + 6 = 10

Caso base: cuando n < 10, solo hay un digito, se devuelve n.

Complejidad: O(log n) — porque dividimos n entre 10 en cada paso.
Para n=1,000,000: solo 7 llamadas recursivas.
""")


if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
