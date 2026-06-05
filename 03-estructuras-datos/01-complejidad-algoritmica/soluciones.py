"""
SOLUCIONES - Complejidad Algoritmica (Big O)
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
    print("SOLUCION - Ejercicio 1: Analisis de complejidad I")
    print("=" * 50)
    print()
    print("Fragmento A: O(n)")
    print("  Un solo bucle for que recorre todo el array de n elementos.")
    print("  El tiempo crece linealmente con el tamano de entrada.")
    print()
    print("Fragmento B: O(1)")
    print("  Acceder a un indice de array es tiempo constante.")
    print("  No importa si el array tiene 1 o 1,000,000 elementos.")
    print()
    print("Fragmento C: O(n^2)")
    print("  Dos bucles anidados. El bucle exterior corre n veces,")
    print("  el interior corre n-i-1 veces. Total ~ n*(n/2) = O(n^2).")
    print()
    print("Fragmento D: O(log n)")
    print("  En cada iteracion del while, el espacio de busqueda")
    print("  se divide a la mitad. Si n=16, solo necesitas 4 pasos.")
    print()
    print("Codigo de ejemplo:")
    print("  def suma(arr):            # O(n)")
    print("      total = 0")
    print("      for n in arr:")
    print("          total += n")
    print("      return total")

def solucion_2():
    print("=" * 50)
    print("SOLUCION - Ejercicio 2: Analisis de complejidad II")
    print("=" * 50)
    print()
    print("Funcion A: O(n^2)")
    print("  Dos bucles anidados sobre el mismo array de tamano n.")
    print("  n * n = n^2 operaciones.")
    print()
    print("Funcion B: O(n * m)")
    print("  Matriz de n filas y m columnas. n * m operaciones.")
    print("  Si es cuadrada (n=m), es O(n^2).")
    print()
    print("Funcion C: O(2^n)")
    print("  Fibonacci recursiva sin memoizacion.")
    print("  Cada llamada genera 2 llamadas mas. Arbol binario de altura n.")
    print("  El numero de llamadas totales es O(2^n).")
    print()
    print("Funcion D: O(n log n)")
    print("  Merge sort divide el array en mitades (log n niveles)")
    print("  y en cada nivel combina n elementos. n * log n = O(n log n).")
    print()
    print("Comparativa para n=10:")
    print("  O(n)     = 10 operaciones")
    print("  O(n^2)   = 100 operaciones")
    print("  O(2^n)   = 1024 operaciones")
    print("  O(n! )   = 3,628,800 operaciones")

def solucion_3():
    print("=" * 50)
    print("SOLUCION - Ejercicio 3: Ordenar por eficiencia")
    print("=" * 50)
    print()
    print("Orden correcto (de menor a mayor complejidad):")
    print()
    print("  1. O(1)     - Acceder a un indice de array")
    print("  2. O(log n) - Busqueda binaria")
    print("  3. O(n)     - Recorrer un array con un bucle")
    print("  4. O(n log n) - Merge sort")
    print("  5. O(n^2)   - Bubble sort")
    print()
    print("Jerarquia de Big O (mas eficiente a menos eficiente):")
    print("  O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n) < O(n!)")
    print()
    print("Ejemplo con n=1000:")
    print("  O(1)     = 1 operacion")
    print("  O(log n) = ~10 operaciones")
    print("  O(n)     = 1000 operaciones")
    print("  O(n log n) = ~10000 operaciones")
    print("  O(n^2)   = 1,000,000 operaciones")
    print()
    print("Dato importante:")
    print("Siempre busca el algoritmo mas eficiente que cumpla")
    print("con los requisitos. n log n suele ser suficiente para")
    print("la mayoria de los casos practicos.")

def menu():
    while True:
        print()
        print("=" * 50)
        print("SOLUCIONES - Complejidad Algoritmica")
        print("=" * 50)
        print("1. Analisis de complejidad I")
        print("2. Analisis de complejidad II")
        print("3. Ordenar por eficiencia")
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
