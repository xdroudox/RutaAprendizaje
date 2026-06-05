"""
SOLUCIONES - Recursion
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
    print("SOLUCION - Ejercicio 1: Factorial recursivo")
    print("=" * 50)
    print()
    print("```python")
    print("def factorial(n):")
    print("    if n <= 1:")
    print("        return 1")
    print("    return n * factorial(n - 1)")
    print("```")
    print()
    print("Desglose de factorial(5):")
    print("  return 5 * factorial(4)")
    print("       = 5 * (4 * factorial(3))")
    print("       = 5 * (4 * (3 * factorial(2)))")
    print("       = 5 * (4 * (3 * (2 * factorial(1))))")
    print("       = 5 * (4 * (3 * (2 * 1)))")
    print("       = 5 * (4 * (3 * 2))")
    print("       = 5 * (4 * 6)")
    print("       = 5 * 24")
    print("       = 120")
    print()
    print("Componentes de una funcion recursiva:")
    print("1. Caso base: if n <= 1: return 1")
    print("2. Llamada recursiva: factorial(n-1)")
    print("3. Progreso: cada llamada reduce n en 1")

def solucion_2():
    print("=" * 50)
    print("SOLUCION - Ejercicio 2: Fibonacci recursivo")
    print("=" * 50)
    print()
    print("```python")
    print("def fibonacci(n):")
    print("    if n <= 1:")
    print("        return n")
    print("    return fibonacci(n - 1) + fibonacci(n - 2)")
    print("```")
    print()
    print("Problema: esta implementacion es O(2^n).")
    print("Para n=40, hay ~330 MILLONES de llamadas recursivas.")
    print()
    print("Version optimizada con MEMOIZACION:")
    print()
    print("```python")
    print("def fibonacci_memo(n, memo={}):")
    print("    if n in memo:")
    print("        return memo[n]")
    print("    if n <= 1:")
    print("        return n")
    print("    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)")
    print("    return memo[n]")
    print("```")
    print()
    print("Version ITERATIVA (aun mejor, O(n)):")
    print()
    print("```python")
    print("def fibonacci_iter(n):")
    print("    a, b = 0, 1")
    print("    for _ in range(n):")
    print("        a, b = b, a + b")
    print("    return a")
    print("```")
    print()
    print("Leccion importante:")
    print("La recursion no siempre es la mejor opcion.")
    print("Evaluar si la recursion es realmente necesaria.")

def solucion_3():
    print("=" * 50)
    print("SOLUCION - Ejercicio 3: Torres de Hanoi")
    print("=" * 50)
    print()
    print("```python")
    print("def hanoi(n, origen, destino, auxiliar):")
    print("    if n == 1:")
    print("        print(f'Mover disco 1 de {origen} a {destino}')")
    print("        return")
    print("    hanoi(n - 1, origen, auxiliar, destino)")
    print("    print(f'Mover disco {n} de {origen} a {destino}')")
    print("    hanoi(n - 1, auxiliar, destino, origen)")
    print("```")
    print()
    print("Leyenda:")
    print("Las Torres de Hanoi es un problema clasico de recursion.")
    print("Cuenta la leyenda que monjes en un templo indio mueven")
    print("64 discos de oro y cuando terminen, el mundo se acabara.")
    print()
    print("Para 64 discos: 2^64 - 1 = 18,446,744,073,709,551,615 movimientos.")
    print("A 1 movimiento por segundo, tomaria ~585 mil millones de anos!")
    print()
    print("Aplicaciones reales de recursion:")
    print("- Recorrido de arboles (sistemas de archivos)")
    print("- Algoritmos divide y venceras (merge sort, quick sort)")
    print("- Backtracking (laberintos, Sudoku, 8 reinas)")
    print("- Procesamiento de XML/JSON anidado")

def menu():
    while True:
        print()
        print("=" * 50)
        print("SOLUCIONES - Recursion")
        print("=" * 50)
        print("1. Factorial recursivo")
        print("2. Fibonacci recursivo")
        print("3. Torres de Hanoi")
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
