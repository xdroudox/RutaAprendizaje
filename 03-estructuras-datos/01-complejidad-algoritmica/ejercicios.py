"""
EJERCICIOS - Complejidad Algoritmica (Big O)
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
# EJERCICIO 1: Analisis de complejidad I
# ============================================
def ejercicio_1():
    print("=" * 50)
    print(">> EJERCICIO 1: Analisis de complejidad I")
    print("=" * 50)
    print()
    print("Determina la complejidad Big O de cada fragmento:")
    print()
    print("Fragmento A:")
    print("  def suma(arr):")
    print("      total = 0")
    print("      for n in arr:")
    print("          total += n")
    print("      return total")
    print()
    print("Fragmento B:")
    print("  def get_first(arr):")
    print("      return arr[0]")
    print()
    print("Fragmento C:")
    print("  def bubble_sort(arr):")
    print("      n = len(arr)")
    print("      for i in range(n):")
    print("          for j in range(n-i-1):")
    print("              if arr[j] > arr[j+1]:")
    print("                  arr[j], arr[j+1] = arr[j+1], arr[j]")
    print()
    print("Fragmento D:")
    print("  def busqueda_binaria(arr, x):")
    print("      low, high = 0, len(arr)-1")
    print("      while low <= high:")
    print("          mid = (low+high)//2")
    print("          if arr[mid] == x: return mid")
    print("          elif arr[mid] < x: low = mid+1")
    print("          else: high = mid-1")
    print("      return -1")
    print()
    print("Escribe tus respuestas como comentarios:")
    print("# A: O(?)")
    print("# B: O(?)")
    print("# C: O(?)")
    print("# D: O(?)")

def solucion_1():
    print("SOLUCION - Ejercicio 1")
    print()
    print("Fragmento A: O(n) - Un solo bucle que recorre todo el array")
    print("Fragmento B: O(1) - Acceso directo por indice")
    print("Fragmento C: O(n^2) - Dos bucles anidados")
    print("Fragmento D: O(log n) - Divide el espacio a la mitad en cada paso")
    print()
    print("Explicacion:")
    print("- O(1): no importa el tamano, siempre el mismo numero de pasos")
    print("- O(n): crece proporcionalmente al tamano de entrada")
    print("- O(n^2): crece al cuadrado (bucles anidados)")
    print("- O(log n): se divide el problema a la mitad cada vez")

# ============================================
# EJERCICIO 2: Analisis de complejidad II
# ============================================
def ejercicio_2():
    print("=" * 50)
    print(">> EJERCICIO 2: Analisis de complejidad II")
    print("=" * 50)
    print()
    print("Determina la complejidad de estas funciones:")
    print()
    print("Funcion A:")
    print("  def print_pairs(arr):")
    print("      for i in arr:")
    print("          for j in arr:")
    print("              print(i, j)")
    print()
    print("Funcion B:")
    print("  def print_matrix(mat):")
    print("      for row in mat:")
    print("          for col in row:")
    print("              print(col)")
    print()
    print("Funcion C:")
    print("  def fibonacci_rec(n):")
    print("      if n <= 1: return n")
    print("      return fibonacci_rec(n-1) + fibonacci_rec(n-2)")
    print()
    print("Funcion D:")
    print("  def merge_sort(arr):")
    print("      if len(arr) <= 1: return arr")
    print("      mid = len(arr)//2")
    print("      left = merge_sort(arr[:mid])")
    print("      right = merge_sort(arr[mid:])")
    print("      return merge(left, right)")
    print()
    print("PISTA: Recuerda que bucles anidados se multiplican")
    print("       y recursion tiene su propia logica")
    print()
    print("# A: O(?)")
    print("# B: O(?)")
    print("# C: O(?)")
    print("# D: O(?)")

def solucion_2():
    print("SOLUCION - Ejercicio 2")
    print()
    print("Funcion A: O(n^2) - Bucle anidado sobre el mismo array")
    print("Funcion B: O(n*m) - Dos bucles, n filas * m columnas")
    print("Funcion C: O(2^n) - Fibonacci recursiva genera arbol binario")
    print("Funcion D: O(n log n) - Merge sort divide y conquista")
    print()
    print("Explicacion:")
    print("- O(n*m): cuando las dimensiones son diferentes")
    print("- O(2^n): exponencial, cada llamada genera 2 mas")
    print("- O(n log n): divide en mitades (log n) y mergea (n)")

# ============================================
# EJERCICIO 3: Ordenar por eficiencia
# ============================================
def ejercicio_3():
    print("=" * 50)
    print(">> EJERCICIO 3: Ordenar por eficiencia")
    print("=" * 50)
    print()
    print("Ordena las siguientes funciones de MENOR a MAYOR complejidad:")
    print()
    print("  1. Busqueda binaria")
    print("  2. Bubble sort")
    print("  3. Acceder a un indice de array")
    print("  4. Recorrer un array con un bucle")
    print("  5. Merge sort")
    print()
    print("PISTA: Ordenalas por Big O de menor a mayor")
    print()
    print("Escribe tu respuesta:")
    print("# Orden: ?, ?, ?, ?, ?")

def solucion_3():
    print("SOLUCION - Ejercicio 3")
    print()
    print("Orden correcto (menor a mayor):")
    print()
    print("  1. O(1)     -> Acceder a un indice de array")
    print("  2. O(log n) -> Busqueda binaria")
    print("  3. O(n)     -> Recorrer un array")
    print("  4. O(n log n) -> Merge sort")
    print("  5. O(n^2)   -> Bubble sort")
    print()
    print("Explicacion:")
    print("O(1) < O(log n) < O(n) < O(n log n) < O(n^2)")
    print("A medida que n crece, la diferencia se vuelve abismal.")
    print("Ejemplo para n=1,000,000:")
    print("  O(1) = 1 operacion")
    print("  O(log n) ~ 20 operaciones")
    print("  O(n) = 1,000,000 operaciones")
    print("  O(n log n) ~ 20,000,000 operaciones")
    print("  O(n^2) = 1,000,000,000,000 operaciones")

# ============================================
# MENU PRINCIPAL
# ============================================
def menu():
    while True:
        print()
        print("=" * 50)
        print("MENU - Complejidad Algoritmica")
        print("=" * 50)
        print("1. Analisis de complejidad I")
        print("2. Analisis de complejidad II")
        print("3. Ordenar por eficiencia")
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
                "Fijate en los bucles: 1 bucle = O(n), 2 anidados = O(n^2)",
                "La recursion fibonacci genera un arbol de llamadas",
                "Ordena por tasa de crecimiento: constante < log < lineal < n log n < cuadratico"
            ]
            print(f"PISTA: {pistas[num - 1]}")
        else:
            [ejercicio_1, ejercicio_2, ejercicio_3][num - 1]()

if __name__ == "__main__":
    main()
