"""
EJERCICIOS - Recursion
Ejecuta desde raiz: python scripts/runner.py 3 8 [ejercicio]

Niveles:
  🟢 Ej 1: Factorial recursivo
  🟡 Ej 2: Fibonacci recursivo
  🔴 Ej 3: Suma de digitos recursiva

Pistas: python scripts/runner.py 3 8 N -p [1|2|3]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1(pista=0):
    """🟢 Factorial recursivo"""
    print(">> 🟢 EJERCICIO 1: Factorial recursivo")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1:")
        print("  n! = n * (n-1)!")
        print("  0! = 1")
        print("  1! = 1")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  def factorial(n):")
        print("      if n <= 1: return 1  # Caso base")
        print("      return n * factorial(n - 1)  # Caso recursivo")
        return
    elif pista == 3:
        print("\n💡 Pista 3:")
        print("  factorial(5):")
        print("    5 * factorial(4)")
        print("    5 * (4 * factorial(3))")
        print("    5 * (4 * (3 * factorial(2)))")
        print("    5 * (4 * (3 * (2 * factorial(1))))")
        print("    5 * (4 * (3 * (2 * 1)))")
        return

    print("\nImplementa:")
    print("  def factorial(n):")
    print()
    print("  Entrada: n = 5")
    print("  Salida:  120")
    print()
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")


def ejercicio_2(pista=0):
    """🟡 Fibonacci recursivo"""
    print(">> 🟡 EJERCICIO 2: Fibonacci recursivo")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1:")
        print("  fib(0) = 0")
        print("  fib(1) = 1")
        print("  fib(n) = fib(n-1) + fib(n-2)")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  def fibonacci(n):")
        print("      if n <= 1: return n")
        print("      return fibonacci(n - 1) + fibonacci(n - 2)")
        return
    elif pista == 3:
        print("\n💡 Pista 3:")
        print("  fibonacci(5):")
        print("    = fib(4) + fib(3)")
        print("    = (fib(3) + fib(2)) + (fib(2) + fib(1))")
        print("    = ((fib(2) + fib(1)) + (fib(1) + fib(0))) + ((fib(1) + fib(0)) + 1)")
        print("    = ... = 5")
        return

    print("\nImplementa:")
    print("  def fibonacci(n):")
    print()
    print("  Serie: 0, 1, 1, 2, 3, 5, 8, 13...")
    print("  Entrada: n = 7 → Salida: 13")
    print()
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")


def ejercicio_3(pista=0):
    """🔴 Suma de digitos recursiva"""
    print(">> 🔴 EJERCICIO 3: Suma de digitos recursiva")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1:")
        print("  n % 10  → ultimo digito")
        print("  n // 10 → numero sin el ultimo digito")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  def suma_digitos(n):")
        print("      if n < 10: return n")
        print("      return n % 10 + suma_digitos(n // 10)")
        return
    elif pista == 3:
        print("\n💡 Pista 3:")
        print("  suma_digitos(1234):")
        print("    4 + suma_digitos(123)")
        print("    4 + (3 + suma_digitos(12))")
        print("    4 + (3 + (2 + suma_digitos(1)))")
        print("    4 + (3 + (2 + 1))")
        print("    = 10")
        return

    print("\nImplementa:")
    print("  def suma_digitos(n):")
    print()
    print("  Entrada: n = 1234")
    print("  Salida:  10 (1+2+3+4)")
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
