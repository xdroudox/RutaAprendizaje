"""
EJERCICIOS - Recursion
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
# EJERCICIO 1: Factorial recursivo
# ============================================
def ejercicio_1():
    print("=" * 50)
    print(">> EJERCICIO 1: Factorial recursivo")
    print("=" * 50)
    print()
    print("Implementa la funcion factorial(n) usando recursion.")
    print()
    print("Matematicamente:")
    print("  0! = 1")
    print("  n! = n * (n-1)!")
    print()
    print("Ejemplo:")
    print("  factorial(5) = 5 * 4 * 3 * 2 * 1 = 120")
    print()
    print("PISTA: Caso base n <= 1, retorna 1")
    print()
    print("Edita el archivo:")
    print("def factorial(n):")
    print("    # --- TU CODIGO AQUI ---")

def solucion_1():
    print("SOLUCION - Ejercicio 1")
    print()
    print("```python")
    print("def factorial(n):")
    print("    if n <= 1:")
    print("        return 1")
    print("    return n * factorial(n - 1)")
    print()
    print("for i in range(11):")
    print("    print(f'{i}! = {factorial(i)}')")
    print("```")
    print()
    print("Resultados:")
    print("  0! = 1")
    print("  1! = 1")
    print("  2! = 2")
    print("  3! = 6")
    print("  4! = 24")
    print("  5! = 120")
    print("  6! = 720")
    print("  7! = 5040")
    print("  8! = 40320")
    print("  9! = 362880")
    print("  10! = 3628800")
    print()
    print("Stack de llamadas para factorial(5):")
    print("  factorial(5) -> 5 * factorial(4)")
    print("    factorial(4) -> 4 * factorial(3)")
    print("      factorial(3) -> 3 * factorial(2)")
    print("        factorial(2) -> 2 * factorial(1)")
    print("          factorial(1) -> 1  (caso base)")
    print("        <- 2 * 1 = 2")
    print("      <- 3 * 2 = 6")
    print("    <- 4 * 6 = 24")
    print("  <- 5 * 24 = 120")

# ============================================
# EJERCICIO 2: Fibonacci recursivo
# ============================================
def ejercicio_2():
    print("=" * 50)
    print(">> EJERCICIO 2: Fibonacci recursivo")
    print("=" * 50)
    print()
    print("Implementa la funcion fibonacci(n) que devuelva")
    print("el n-esimo termino de la serie de Fibonacci.")
    print()
    print("Serie: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...")
    print()
    print("  fib(0) = 0")
    print("  fib(1) = 1")
    print("  fib(n) = fib(n-1) + fib(n-2)")
    print()
    print("Ejemplo:")
    print("  fibonacci(6) = 8")
    print()
    print("PISTA: Caso base: if n <= 1: return n")
    print()
    print("Edita el archivo:")
    print("def fibonacci(n):")
    print("    # --- TU CODIGO AQUI ---")

def solucion_2():
    print("SOLUCION - Ejercicio 2")
    print()
    print("```python")
    print("def fibonacci(n):")
    print("    if n <= 1:")
    print("        return n")
    print("    return fibonacci(n - 1) + fibonacci(n - 2)")
    print()
    print("for i in range(11):")
    print("    print(f'fib({i}) = {fibonacci(i)}')")
    print("```")
    print()
    print("Resultados:")
    print("  fib(0) = 0")
    print("  fib(1) = 1")
    print("  fib(2) = 1")
    print("  fib(3) = 2")
    print("  fib(4) = 3")
    print("  fib(5) = 5")
    print("  fib(6) = 8")
    print("  fib(7) = 13")
    print("  fib(8) = 21")
    print("  fib(9) = 34")
    print("  fib(10) = 55")
    print()
    print("Arbol de llamadas para fibonacci(5):")
    print("            fib(5)")
    print("           /      \\")
    print("       fib(4)     fib(3)")
    print("      /     \\    /    \\")
    print("  fib(3)  fib(2) fib(2) fib(1)")
    print("  /    \\   /  \\   /  \\")
    print("fib(2) fib(1) ... (muchas llamadas)")
    print()
    print("Complejidad: O(2^n) - MUY ineficiente.")
    print("Optimizacion: usa memoizacion o programacion dinamica.")
    print("fib(40) genera ~330 MILLONES de llamadas!")

# ============================================
# EJERCICIO 3: Torres de Hanoi
# ============================================
def ejercicio_3():
    print("=" * 50)
    print(">> EJERCICIO 3: Torres de Hanoi")
    print("=" * 50)
    print()
    print("Implementa la solucion recursiva para las Torres de Hanoi.")
    print()
    print("  def hanoi(n, origen, destino, auxiliar):")
    print()
    print("Reglas:")
    print("  - Solo puedes mover un disco a la vez")
    print("  - No puedes poner un disco grande sobre uno pequeno")
    print("  - Debes mover todos los discos de A a C")
    print()
    print("Ejemplo con 3 discos:")
    print("  hanoi(3, 'A', 'C', 'B')")
    print()
    print("PISTA: Mueve n-1 discos de origen a auxiliar,")
    print("       luego mueve el disco n de origen a destino,")
    print("       luego mueve n-1 discos de auxiliar a destino")
    print()
    print("Edita el archivo:")
    print("def hanoi(n, origen, destino, auxiliar):")
    print("    # --- TU CODIGO AQUI ---")

def solucion_3():
    print("SOLUCION - Ejercicio 3")
    print()
    print("```python")
    print("def hanoi(n, origen, destino, auxiliar):")
    print("    if n == 1:")
    print("        print(f'Mover disco 1 de {origen} a {destino}')")
    print("        return")
    print("    hanoi(n - 1, origen, auxiliar, destino)")
    print("    print(f'Mover disco {n} de {origen} a {destino}')")
    print("    hanoi(n - 1, auxiliar, destino, origen)")
    print()
    print("hanoi(3, 'A', 'C', 'B')")
    print("```")
    print()
    print("Salida:")
    print("  Mover disco 1 de A a C")
    print("  Mover disco 2 de A a B")
    print("  Mover disco 1 de C a B")
    print("  Mover disco 3 de A a C")
    print("  Mover disco 1 de B a A")
    print("  Mover disco 2 de B a C")
    print("  Mover disco 1 de A a C")
    print()
    print("Explicacion:")
    print("1. Mueve n-1 discos de origen a auxiliar (usando destino como apoyo)")
    print("2. Mueve el disco n de origen a destino")
    print("3. Mueve n-1 discos de auxiliar a destino (usando origen como apoyo)")
    print()
    print("Complejidad: O(2^n) - minimo numero de movimientos = 2^n - 1")
    print("Para 3 discos: 7 movimientos. Para 64 discos: 18 quintillones!")

# ============================================
# MENU PRINCIPAL
# ============================================
def menu():
    while True:
        print()
        print("=" * 50)
        print("MENU - Recursion")
        print("=" * 50)
        print("1. Factorial recursivo")
        print("2. Fibonacci recursivo")
        print("3. Torres de Hanoi")
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
                "Caso base: n <= 1 retorna 1. Caso recursivo: n * factorial(n-1)",
                "Caso base: n <= 1 retorna n. Caso recursivo: fib(n-1) + fib(n-2)",
                "Mueve n-1 discos a auxiliar, luego el grande a destino, luego n-1 de auxiliar a destino"
            ]
            print(f"PISTA: {pistas[num - 1]}")
        else:
            [ejercicio_1, ejercicio_2, ejercicio_3][num - 1]()

if __name__ == "__main__":
    main()
