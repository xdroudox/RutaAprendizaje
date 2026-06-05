"""
SOLUCIONES - Ordenamiento
Ejecuta: python scripts/runner.py 3 6 [ejercicio] -s
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    print(">> SOLUCION 1: Bubble Sort")
    print("-" * 40)
    print("def bubble_sort(arr):")
    print("    n = len(arr)")
    print("    for i in range(n):")
    print("        for j in range(n - i - 1):")
    print("            if arr[j] > arr[j + 1]:")
    print("                arr[j], arr[j + 1] = arr[j + 1], arr[j]")
    print("    return arr")
    print()
    print("Explicacion: Compara pares adyacentes y los intercambia")
    print("si estan en orden incorrecto. El mayor 'flota' al final.")
    print("Complejidad: O(n^2) en el peor caso.")

def solucion_2():
    print(">> SOLUCION 2: Selection Sort")
    print("-" * 40)
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
    print("Explicacion: En cada pasada, encuentra el minimo y lo coloca")
    print("en su posicion correcta. Complejidad: O(n^2).")

def solucion_3():
    print(">> SOLUCION 3: Merge Sort simplificado")
    print("-" * 40)
    print("def merge_sort(arr):")
    print("    if len(arr) <= 1:")
    print("        return arr")
    print("    mid = len(arr) // 2")
    print("    left = merge_sort(arr[:mid])")
    print("    right = merge_sort(arr[mid:])")
    print("    return merge(left, right)")
    print()
    print("def merge(left, right):")
    print("    resultado = []")
    print("    i = j = 0")
    print("    while i < len(left) and j < len(right):")
    print("        if left[i] <= right[j]:")
    print("            resultado.append(left[i])")
    print("            i += 1")
    print("        else:")
    print("            resultado.append(right[j])")
    print("            j += 1")
    print("    resultado.extend(left[i:])")
    print("    resultado.extend(right[j:])")
    print("    return resultado")
    print()
    print("Explicacion: Divide el array en mitades, ordena cada mitad")
    print("recursivamente y luego las fusiona. Complejidad: O(n log n).")

if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
