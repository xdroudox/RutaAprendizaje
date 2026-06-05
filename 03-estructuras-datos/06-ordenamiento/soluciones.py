"""
SOLUCIONES - Algoritmos de Ordenamiento
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
    print("SOLUCION - Ejercicio 1: Bubble Sort")
    print("=" * 50)
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
    print("        if not swapped:")
    print("            break")
    print("    return arr")
    print("```")
    print()
    print("Visualizacion del ordenamiento:")
    print("  [5, 3, 8, 1, 2]")
    print("  Pasada 1: [3, 5, 1, 2, 8]  (8 llega al final)")
    print("  Pasada 2: [3, 1, 2, 5, 8]  (5 llega a su lugar)")
    print("  Pasada 3: [1, 2, 3, 5, 8]  (ordenado, swapped=False -> break)")
    print()
    print("Complejidad: Mejor O(n), Peor O(n^2), Memoria O(1)")
    print("Es estable (mantiene orden relativo de elementos iguales).")

def solucion_2():
    print("=" * 50)
    print("SOLUCION - Ejercicio 2: Selection Sort")
    print("=" * 50)
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
    print("```")
    print()
    print("Visualizacion:")
    print("  [64, 25, 12, 22, 11]")
    print("  i=0: min_idx=4 -> [11, 25, 12, 22, 64]")
    print("  i=1: min_idx=2 -> [11, 12, 25, 22, 64]")
    print("  i=2: min_idx=3 -> [11, 12, 22, 25, 64]")
    print("  i=3: min_idx=3 -> [11, 12, 22, 25, 64]")
    print()
    print("Caracteristicas:")
    print("- Siempre O(n^2) independientemente de los datos")
    print("- Memoria: O(1)")
    print("- NO estable (puede cambiar orden de elementos iguales)")
    print("- Bueno para arrays pequenos")

def solucion_3():
    print("=" * 50)
    print("SOLUCION - Ejercicio 3: Merge Sort")
    print("=" * 50)
    print()
    print("```python")
    print("def merge_sort(arr):")
    print("    if len(arr) <= 1:")
    print("        return arr")
    print("    mid = len(arr) // 2")
    print("    left = merge_sort(arr[:mid])")
    print("    right = merge_sort(arr[mid:])")
    print("    return merge(left, right)")
    print()
    print("def merge(left, right):")
    print("    result = []")
    print("    i = j = 0")
    print("    while i < len(left) and j < len(right):")
    print("        if left[i] <= right[j]:")
    print("            result.append(left[i]); i += 1")
    print("        else:")
    print("            result.append(right[j]); j += 1")
    print("    result.extend(left[i:])")
    print("    result.extend(right[j:])")
    print("    return result")
    print("```")
    print()
    print("Visualizacion para [38, 27, 43, 3]:")
    print("  divide: [38, 27] | [43, 3]")
    print("  divide: [38] [27] | [43] [3]")
    print("  merge:  [27, 38] | [3, 43]")
    print("  merge:  [3, 27, 38, 43]")
    print()
    print("Caracteristicas:")
    print("- Divide y venceras: divide hasta nivel atomico")
    print("- Siempre O(n log n)")
    print("- Memoria: O(n) (necesita arrays auxiliares)")
    print("- Es estable")
    print("- Ideal para grandes volumenes de datos")

def menu():
    while True:
        print()
        print("=" * 50)
        print("SOLUCIONES - Algoritmos de Ordenamiento")
        print("=" * 50)
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Merge Sort")
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
