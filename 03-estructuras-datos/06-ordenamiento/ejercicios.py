"""
EJERCICIOS - Algoritmos de Ordenamiento
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
# EJERCICIO 1: Bubble Sort
# ============================================
def ejercicio_1():
    print("=" * 50)
    print(">> EJERCICIO 1: Bubble Sort")
    print("=" * 50)
    print()
    print("Implementa bubble sort con una optimizacion:")
    print("detener el algoritmo si el array ya esta ordenado")
    print("(sin intercambios en una pasada completa).")
    print()
    print("  def bubble_sort(arr):")
    print()
    print("Ejemplo:")
    print("  [5, 3, 8, 1, 2] -> [1, 2, 3, 5, 8]")
    print()
    print("PISTA: Usa un flag 'swapped' que se reinicia en cada pasada")
    print()
    print("Edita el archivo:")
    print("def bubble_sort(arr):")
    print("    # --- TU CODIGO AQUI ---")

def solucion_1():
    print("SOLUCION - Ejercicio 1")
    print()
    print("```python")
    print("def bubble_sort(arr):")
    print("    n = len(arr)")
    print("    for i in range(n):")
    print("        swapped = False")
    print("        for j in range(0, n - i - 1):")
    print("            if arr[j] > arr[j + 1]:")
    print("                arr[j], arr[j + 1] = arr[j + 1], arr[j]")
    print("                swapped = True")
    print("        if not swapped:  # Ya ordenado")
    print("            break")
    print("    return arr")
    print()
    print("# Prueba")
    print("arr = [5, 3, 8, 1, 2]")
    print("print(bubble_sort(arr))  # [1, 2, 3, 5, 8]")
    print("```")
    print()
    print("Explicacion:")
    print("Cada pasada 'burbujea' el elemento mas grande al final.")
    print("Optimizacion: si no hay intercambios, el array ya esta ordenado.")
    print("Mejor caso: O(n), Peor caso: O(n^2), Memoria: O(1)")

# ============================================
# EJERCICIO 2: Selection Sort
# ============================================
def ejercicio_2():
    print("=" * 50)
    print(">> EJERCICIO 2: Selection Sort")
    print("=" * 50)
    print()
    print("Implementa selection sort.")
    print()
    print("  def selection_sort(arr):")
    print()
    print("En cada iteracion, encuentra el elemento minimo")
    print("y lo coloca en la posicion correcta.")
    print()
    print("Ejemplo:")
    print("  [5, 3, 8, 1, 2]")
    print("  Paso 1: min=1 -> [1, 3, 8, 5, 2]")
    print("  Paso 2: min=2 -> [1, 2, 8, 5, 3]")
    print("  ...")
    print()
    print("PISTA: Manten un indice 'min_idx' y actualizalo en el bucle interno")
    print()
    print("Edita el archivo:")
    print("def selection_sort(arr):")
    print("    # --- TU CODIGO AQUI ---")

def solucion_2():
    print("SOLUCION - Ejercicio 2")
    print()
    print("```python")
    print("def selection_sort(arr):")
    print("    n = len(arr)")
    print("    for i in range(n):")
    print("        min_idx = i")
    print("        for j in range(i + 1, n):")
    print("            if arr[j] < arr[min_idx]:")
    print("                min_idx = j")
    print("        arr[i], arr[min_idx] = arr[min_idx], arr[i]")
    print("    return arr")
    print()
    print("# Prueba")
    print("arr = [64, 25, 12, 22, 11]")
    print("print(selection_sort(arr))  # [11, 12, 22, 25, 64]")
    print("```")
    print()
    print("Explicacion:")
    print("Encuentra el minimo en la parte no ordenada y lo intercambia")
    print("con el primer elemento de la parte no ordenada.")
    print("Complejidad: O(n^2) siempre (incluso si ya esta ordenado).")
    print("Memoria: O(1)")

# ============================================
# EJERCICIO 3: Merge Sort
# ============================================
def ejercicio_3():
    print("=" * 50)
    print(">> EJERCICIO 3: Merge Sort")
    print("=" * 50)
    print()
    print("Implementa merge sort con su funcion auxiliar merge.")
    print()
    print("  def merge_sort(arr):")
    print("  def merge(left, right):")
    print()
    print("merge_sort divide el array en mitades recursivamente.")
    print("merge combina dos arrays ordenados en uno solo.")
    print()
    print("Ejemplo:")
    print("  [38, 27, 43, 3, 9, 82, 10]")
    print("  -> divide hasta tener elementos individuales")
    print("  -> mergea de vuelta en orden")
    print()
    print("PISTA: merge() usa dos indices i, j para comparar elementos")
    print()
    print("Edita el archivo:")
    print("def merge_sort(arr):")
    print("    # --- TU CODIGO AQUI ---")
    print()
    print("def merge(left, right):")
    print("    # --- TU CODIGO AQUI ---")

def solucion_3():
    print("SOLUCION - Ejercicio 3")
    print()
    print("```python")
    print("def merge_sort(arr):")
    print("    if len(arr) <= 1:")
    print("        return arr")
    print()
    print("    mid = len(arr) // 2")
    print("    left = merge_sort(arr[:mid])")
    print("    right = merge_sort(arr[mid:])")
    print("    return merge(left, right)")
    print()
    print("def merge(left, right):")
    print("    result = []")
    print("    i = j = 0")
    print()
    print("    while i < len(left) and j < len(right):")
    print("        if left[i] <= right[j]:")
    print("            result.append(left[i])")
    print("            i += 1")
    print("        else:")
    print("            result.append(right[j])")
    print("            j += 1")
    print()
    print("    result.extend(left[i:])")
    print("    result.extend(right[j:])")
    print("    return result")
    print()
    print("# Prueba")
    print("arr = [38, 27, 43, 3, 9, 82, 10]")
    print("print(merge_sort(arr))  # [3, 9, 10, 27, 38, 43, 82]")
    print("```")
    print()
    print("Explicacion:")
    print("Merge sort es un algoritmo 'divide y venceras'.")
    print("Divide hasta tener arrays de 1 elemento (ordenados por definicion).")
    print("Luego mergea combinando dos arrays ordenados.")
    print("Complejidad: O(n log n) siempre.")
    print("Memoria: O(n) - requiere espacio extra para los arrays.")

# ============================================
# MENU PRINCIPAL
# ============================================
def menu():
    while True:
        print()
        print("=" * 50)
        print("MENU - Algoritmos de Ordenamiento")
        print("=" * 50)
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Merge Sort")
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
                "Usa un flag swapped que se ponga False al inicio de cada pasada",
                "Encuentra el minimo en la parte no ordenada y lo intercambias",
                "Divide recursive hasta tener 1 elemento, luego mergea ordenando"
            ]
            print(f"PISTA: {pistas[num - 1]}")
        else:
            [ejercicio_1, ejercicio_2, ejercicio_3][num - 1]()

if __name__ == "__main__":
    main()
