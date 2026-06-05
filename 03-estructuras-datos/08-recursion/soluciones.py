"""
SOLUCIONES - Recursion
Ejecuta: python scripts/runner.py 3 8 [ejercicio] -s
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    print(">> SOLUCION 1: Factorial recursivo")
    print("-" * 40)
    print("def factorial(n):")
    print("    if n <= 1:")
    print("        return 1")
    print("    return n * factorial(n - 1)")
    print()
    print("Uso: factorial(5) -> 120")
    print()
    print("Explicacion: Caso base: n <= 1 retorna 1.")
    print("Caso recursivo: n * factorial(n-1).")
    print("La funcion se llama a si misma con n-1 hasta llegar al caso base.")

def solucion_2():
    print(">> SOLUCION 2: Fibonacci recursivo")
    print("-" * 40)
    print("def fibonacci(n):")
    print("    if n <= 1:")
    print("        return n")
    print("    return fibonacci(n - 1) + fibonacci(n - 2)")
    print()
    print("Uso: fibonacci(7) -> 13")
    print()
    print("Explicacion: Caso base: n=0 -> 0, n=1 -> 1.")
    print("Caso recursivo: suma de los dos anteriores.")
    print("Complejidad: O(2^n) sin memoizacion.")

def solucion_3():
    print(">> SOLUCION 3: Suma de digitos recursiva")
    print("-" * 40)
    print("def suma_digitos(n):")
    print("    if n < 10:")
    print("        return n")
    print("    return n % 10 + suma_digitos(n // 10)")
    print()
    print("Uso: suma_digitos(1234) -> 10")
    print()
    print("Explicacion: n % 10 da el ultimo digito,")
    print("n // 10 elimina el ultimo digito.")
    print("Caso base: cuando n < 10, retorna n.")

if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
