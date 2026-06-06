"""
EJERCICIOS - Ordenamiento
Ejecuta desde raiz: python scripts/runner.py 3 6 [ejercicio]

Niveles:
  🟢 Ej 1: Bubble Sort
  🟡 Ej 2: Selection Sort
  🔴 Ej 3: Merge Sort

Pistas: python scripts/runner.py 3 6 N -p [1|2|3]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1(pista=0):
    """🟢 Bubble Sort"""
    print(">> 🟢 EJERCICIO 1: Bubble Sort")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1:")
        print("  Dos bucles anidados:")
        print("  for i in range(n):")
        print("      for j in range(n - i - 1):")
        print("          if arr[j] > arr[j+1]: intercambiar")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  n - i - 1: en cada pasada, el ultimo elemento")
        print("  ya esta en su posicion correcta.")
        return
    elif pista == 3:
        print("\n💡 Pista 3:")
        print("  def bubble_sort(arr):")
        print("      n = len(arr)")
        print("      for i in range(n):")
        print("          for j in range(n - i - 1):")
        print("              if arr[j] > arr[j + 1]:")
        print("                  arr[j], arr[j+1] = arr[j+1], arr[j]")
        print("      return arr")
        return

    print("\nImplementa:")
    print("  def bubble_sort(arr):")
    print("      # Dos bucles anidados, comparar e intercambiar")
    print()
    print("  Entrada: [64, 34, 25, 12, 22, 11, 90]")
    print("  Salida:  [11, 12, 22, 25, 34, 64, 90]")
    print()
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")


def ejercicio_2(pista=0):
    """🟡 Selection Sort"""
    print(">> 🟡 EJERCICIO 2: Selection Sort")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1:")
        print("  for i in range(n):  # posicion actual")
        print("      min_idx = i")
        print("      for j in range(i + 1, n):")
        print("          if arr[j] < arr[min_idx]:")
        print("              min_idx = j")
        print("      # intercambiar arr[i] con arr[min_idx]")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  Selection sort: encuentra el MINIMO en cada pasada")
        print("  y lo coloca en la posicion i.")
        return
    elif pista == 3:
        print("\n💡 Pista 3:")
        print("  def selection_sort(arr):")
        print("      n = len(arr)")
        print("      for i in range(n):")
        print("          min_idx = i")
        print("          for j in range(i + 1, n):")
        print("              if arr[j] < arr[min_idx]:")
        print("                  min_idx = j")
        print("          arr[i], arr[min_idx] = arr[min_idx], arr[i]")
        print("      return arr")
        return

    print("\nImplementa:")
    print("  def selection_sort(arr):")
    print("      # En cada pasada, busca el minimo y lo coloca")
    print()
    print("  Entrada: [64, 25, 12, 22, 11]")
    print("  Salida:  [11, 12, 22, 25, 64]")
    print()
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")


def ejercicio_3(pista=0):
    """🔴 Merge Sort"""
    print(">> 🔴 EJERCICIO 3: Merge Sort")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1:")
        print("  merge_sort(arr): caso base len <= 1")
        print("  mid = len(arr) // 2")
        print("  left = merge_sort(arr[:mid])")
        print("  right = merge_sort(arr[mid:])")
        print("  return merge(left, right)")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  merge(left, right):")
        print("    resultado = []")
        print("    i = j = 0")
        print("    while i < len(left) and j < len(right):")
        print("        if left[i] <= right[j]:")
        print("            resultado.append(left[i]); i += 1")
        print("        else:")
        print("            resultado.append(right[j]); j += 1")
        print("    resultado.extend(left[i:])")
        print("    resultado.extend(right[j:])")
        print("    return resultado")
        return
    elif pista == 3:
        print("\n💡 Pista 3:")
        print("  def merge_sort(arr):")
        print("      if len(arr) <= 1: return arr")
        print("      mid = len(arr) // 2")
        print("      return merge(merge_sort(arr[:mid]),")
        print("                     merge_sort(arr[mid:]))")
        return

    print("\nImplementa:")
    print("  def merge_sort(arr):   # Divide")
    print("  def merge(left, right): # Fusiona")
    print()
    print("  Entrada: [38, 27, 43, 3, 9, 82, 10]")
    print("  Salida:  [3, 9, 10, 27, 38, 43, 82]")
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
