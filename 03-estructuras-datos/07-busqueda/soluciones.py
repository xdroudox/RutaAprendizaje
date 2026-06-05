"""
SOLUCIONES - Algoritmos de Busqueda
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
    print("SOLUCION - Ejercicio 1: Busqueda Lineal")
    print("=" * 50)
    print()
    print("```python")
    print("def linear_search(arr, target):")
    print("    for i in range(len(arr)):")
    print("        if arr[i] == target:")
    print("            return i")
    print("    return -1")
    print("```")
    print()
    print("Casos de prueba:")
    print("  arr = [4, 2, 7, 1, 9, 3]")
    print("  linear_search(arr, 7) -> 2  (encontrado en indice 2)")
    print("  linear_search(arr, 5) -> -1 (no encontrado)")
    print("  linear_search([], 1)  -> -1 (array vacio)")
    print()
    print("Complejidad: O(n)")
    print("  Mejor caso: O(1) - el elemento esta al inicio")
    print("  Peor caso: O(n) - el elemento esta al final o no existe")
    print()
    print("Usos: Arrays pequenos, datos desordenados,")
    print("      cuando solo necesitas buscar una vez.")

def solucion_2():
    print("=" * 50)
    print("SOLUCION - Ejercicio 2: Busqueda Binaria")
    print("=" * 50)
    print()
    print("```python")
    print("# Version iterativa")
    print("def binary_search(arr, target):")
    print("    left, right = 0, len(arr) - 1")
    print("    while left <= right:")
    print("        mid = (left + right) // 2")
    print("        if arr[mid] == target:")
    print("            return mid")
    print("        elif arr[mid] < target:")
    print("            left = mid + 1")
    print("        else:")
    print("            right = mid - 1")
    print("    return -1")
    print()
    print("# Version recursiva")
    print("def binary_search_rec(arr, target, left, right):")
    print("    if left > right:")
    print("        return -1")
    print("    mid = (left + right) // 2")
    print("    if arr[mid] == target:")
    print("        return mid")
    print("    if arr[mid] < target:")
    print("        return binary_search_rec(arr, target, mid+1, right)")
    print("    return binary_search_rec(arr, target, left, mid-1)")
    print("```")
    print()
    print("Visualizacion para arr=[1,3,5,7,9,11,13], target=7:")
    print("  left=0, right=6, mid=3 -> arr[3]=7, encontrado!")
    print()
    print("  Para target=2:")
    print("  left=0, right=6, mid=3 -> arr[3]=7 > 2, right=2")
    print("  left=0, right=2, mid=1 -> arr[1]=3 > 2, right=0")
    print("  left=0, right=0, mid=0 -> arr[0]=1 < 2, left=1")
    print("  left=1, right=0 -> left > right, return -1")
    print()
    print("Complejidad: O(log n)")
    print("  n=10 -> ~4 pasos maximo")
    print("  n=1000 -> ~10 pasos maximo")
    print("  n=1,000,000 -> ~20 pasos maximo")

def solucion_3():
    print("=" * 50)
    print("SOLUCION - Ejercicio 3: Hash Table")
    print("=" * 50)
    print()
    print("```python")
    print("class HashTable:")
    print("    def __init__(self, size=10):")
    print("        self.size = size")
    print("        self.table = [[] for _ in range(size)]")
    print()
    print("    def _hash(self, key):")
    print("        return hash(key) % self.size")
    print()
    print("    def put(self, key, value):")
    print("        idx = self._hash(key)")
    print("        for i, (k, v) in enumerate(self.table[idx]):")
    print("            if k == key:")
    print("                self.table[idx][i] = (key, value)")
    print("                return")
    print("        self.table[idx].append((key, value))")
    print()
    print("    def get(self, key):")
    print("        idx = self._hash(key)")
    print("        for k, v in self.table[idx]:")
    print("            if k == key:")
    print("                return v")
    print("        return None")
    print()
    print("    def delete(self, key):")
    print("        idx = self._hash(key)")
    print("        for i, (k, v) in enumerate(self.table[idx]):")
    print("            if k == key:")
    print("                del self.table[idx][i]")
    print("                return True")
    print("        return False")
    print("```")
    print()
    print("Explicacion del direccionamiento abierto con chaining:")
    print("  hash('juan') % 10 = 7 -> bucket[7] almacena ('juan', 25)")
    print("  Si 'luis' tambien da 7, se anade a la lista: [('juan',25), ('luis',30)]")
    print()
    print("Complejidad:")
    print("  Promedio: O(1) para put, get, delete")
    print("  Peor caso: O(n) si todas las claves tienen el mismo hash")
    print()
    print("Para mejorar: aumentar size, mejor funcion hash, rehashing.")

def menu():
    while True:
        print()
        print("=" * 50)
        print("SOLUCIONES - Algoritmos de Busqueda")
        print("=" * 50)
        print("1. Busqueda Lineal")
        print("2. Busqueda Binaria")
        print("3. Hash Table")
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
