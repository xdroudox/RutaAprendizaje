"""
SOLUCIONES - Ordenamiento
Ejecuta: python scripts/runner.py 3 6 [ejercicio] -s
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: Bubble Sort")
    print("=" * 50)

    print("""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
""")

    print("--- EXPLICACION ---")
    print("""
Bubble sort compara pares adyacentes y los intercambia si estan
en orden incorrecto. El mayor elemento "flota" hacia el final.

Paso a paso con [5, 3, 8, 1]:

Pasada 1 (i=0):
  j=0: 5>3 → swap → [3, 5, 8, 1]
  j=1: 5<8 → no swap
  j=2: 8>1 → swap → [3, 5, 1, 8] ← 8 floto al final

Pasada 2 (i=1):
  j=0: 3<5 → no swap
  j=1: 5>1 → swap → [3, 1, 5, 8] ← 5 floto

Pasada 3 (i=2):
  j=0: 3>1 → swap → [1, 3, 5, 8] ← 3 floto

Resultado: [1, 3, 5, 8]

Complejidad: O(n^2) en peor y promedio, O(n) si ya esta ordenado.
""")


def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: Selection Sort")
    print("=" * 50)

    print("""
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
""")

    print("--- EXPLICACION ---")
    print("""
Selection sort encuentra el ELEMENTO MINIMO en cada pasada y lo
coloca en su posicion correcta.

Paso a paso con [64, 25, 12, 22, 11]:

Pasada 1: minimo entre indices 0-4 es 11 (idx 4)
  swap arr[0] con arr[4] → [11, 25, 12, 22, 64]

Pasada 2: minimo entre indices 1-4 es 12 (idx 2)
  swap arr[1] con arr[2] → [11, 12, 25, 22, 64]

Pasada 3: minimo entre indices 2-4 es 22 (idx 3)
  swap arr[2] con arr[3] → [11, 12, 22, 25, 64]

Pasada 4: minimo entre indices 3-4 es 25 (idx 3)
  swap arr[3] con arr[3] → [11, 12, 22, 25, 64]

Complejidad: SIEMPRE O(n^2) (incluso si ya esta ordenado).
Ventaja sobre bubble: hace menos intercambios (max n-1).
""")


def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: Merge Sort")
    print("=" * 50)

    print("""
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    resultado = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            resultado.append(left[i])
            i += 1
        else:
            resultado.append(right[j])
            j += 1
    resultado.extend(left[i:])
    resultado.extend(right[j:])
    return resultado
""")

    print("--- EXPLICACION ---")
    print("""
Merge Sort usa DIVIDE Y CONQUISTA:

1. DIVIDE: parte el array en mitades hasta tener 1 elemento.
2. CONQUISTA: fusiona las mitades ordenadamente.

Paso a paso con [38, 27, 43, 3]:

             [38, 27, 43, 3]
            /              \
      [38, 27]           [43, 3]
      /      \           /      \
    [38]    [27]       [43]    [3]
      \      /           \      /
    merge(27,38)       merge(3,43)
      \                  /
    merge([27,38], [3,43])
            |
         [3, 27, 38, 43]

Funcion merge(left, right):
  Compara el primer elemento de cada lista.
  Toma el menor y lo pone en resultado.
  Cuando una lista se vacia, copia el resto de la otra.

Complejidad: SIEMPRE O(n log n). Memoria: O(n) adicional.
Es un algoritmo ESTABLE (mantiene orden de elementos iguales).
""")


if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
