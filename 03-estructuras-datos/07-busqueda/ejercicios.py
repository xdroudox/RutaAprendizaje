"""
EJERCICIOS - Algoritmos de Busqueda
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
# EJERCICIO 1: Busqueda Lineal
# ============================================
def ejercicio_1():
    print("=" * 50)
    print(">> EJERCICIO 1: Busqueda Lineal")
    print("=" * 50)
    print()
    print("Implementa la funcion linear_search que devuelva")
    print("el INDICE del elemento si existe, o -1 si no.")
    print()
    print("  def linear_search(arr, target):")
    print()
    print("Ejemplo:")
    print("  arr = [4, 2, 7, 1, 9]")
    print("  linear_search(arr, 7) -> 2")
    print("  linear_search(arr, 5) -> -1")
    print()
    print("PISTA: Recorre el array con un for y compara cada elemento")
    print()
    print("Edita el archivo:")
    print("def linear_search(arr, target):")
    print("    # --- TU CODIGO AQUI ---")

def solucion_1():
    print("SOLUCION - Ejercicio 1")
    print()
    print("```python")
    print("def linear_search(arr, target):")
    print("    for i in range(len(arr)):")
    print("        if arr[i] == target:")
    print("            return i")
    print("    return -1")
    print()
    print("# Prueba")
    print("arr = [4, 2, 7, 1, 9]")
    print("print(linear_search(arr, 7))  # 2")
    print("print(linear_search(arr, 5))  # -1")
    print("```")
    print()
    print("Explicacion:")
    print("Recorre el array elemento por elemento hasta encontrar")
    print("el objetivo. Si llega al final sin encontrarlo, devuelve -1.")
    print("Complejidad: O(n) - En el peor caso recorre todo el array.")

# ============================================
# EJERCICIO 2: Busqueda Binaria
# ============================================
def ejercicio_2():
    print("=" * 50)
    print(">> EJERCICIO 2: Busqueda Binaria")
    print("=" * 50)
    print()
    print("Implementa busqueda binaria de forma ITERATIVA.")
    print()
    print("  def binary_search(arr, target):")
    print()
    print("Requisito: el array debe estar ORDENADO.")
    print()
    print("Ejemplo:")
    print("  arr = [1, 3, 5, 7, 9, 11, 13]")
    print("  binary_search(arr, 7) -> 3")
    print("  binary_search(arr, 2) -> -1")
    print()
    print("PISTA: Usa dos punteros left=0 y right=len(arr)-1")
    print("       y ve actualizando mid = (left+right)//2")
    print()
    print("Edita el archivo:")
    print("def binary_search(arr, target):")
    print("    # --- TU CODIGO AQUI ---")

def solucion_2():
    print("SOLUCION - Ejercicio 2")
    print()
    print("```python")
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
    print("# Prueba")
    print("arr = [1, 3, 5, 7, 9, 11, 13]")
    print("print(binary_search(arr, 7))  # 3")
    print("print(binary_search(arr, 2))  # -1")
    print()
    print("# Version recursiva")
    print("def binary_search_rec(arr, target, left, right):")
    print("    if left > right:")
    print("        return -1")
    print("    mid = (left + right) // 2")
    print("    if arr[mid] == target:")
    print("        return mid")
    print("    elif arr[mid] < target:")
    print("        return binary_search_rec(arr, target, mid+1, right)")
    print("    return binary_search_rec(arr, target, left, mid-1)")
    print("```")
    print()
    print("Explicacion:")
    print("Divide el espacio de busqueda a la mitad en cada paso.")
    print("Para n=1,000,000, solo necesitas ~20 pasos (vs 1,000,000 lineal).")
    print("Complejidad: O(log n)")

# ============================================
# EJERCICIO 3: Hash Table
# ============================================
def ejercicio_3():
    print("=" * 50)
    print(">> EJERCICIO 3: Hash Table")
    print("=" * 50)
    print()
    print("Implementa una clase HashTable simple.")
    print()
    print("  class HashTable:")
    print("      def __init__(self, size=10)")
    print("      def _hash(self, key)       - Funcion hash")
    print("      def put(self, key, value)  - Insertar/actualizar")
    print("      def get(self, key)         - Obtener valor")
    print("      def delete(self, key)      - Eliminar clave")
    print()
    print("Usa listas para manejar colisiones (chaining).")
    print()
    print("PISTA: self.table = [[] for _ in range(size)]")
    print()
    print("Edita el archivo:")
    print("class HashTable:")
    print("    # --- TU CODIGO AQUI ---")

def solucion_3():
    print("SOLUCION - Ejercicio 3")
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
    print()
    print("# Prueba")
    print("ht = HashTable()")
    print("ht.put('juan', 25)")
    print("ht.put('maria', 30)")
    print("print(ht.get('juan'))    # 25")
    print("print(ht.get('pedro'))   # None")
    print("ht.delete('juan')")
    print("print(ht.get('juan'))    # None")
    print("```")
    print()
    print("Explicacion:")
    print("La funcion hash convierte la clave en un indice del array.")
    print("Colisiones: dos claves diferentes dan el mismo indice.")
    print("Solucion: chaining - cada bucket es una lista de pares (key, value).")
    print("Complejidad: O(1) promedio, O(n) peor caso (muchas colisiones).")

# ============================================
# MENU PRINCIPAL
# ============================================
def menu():
    while True:
        print()
        print("=" * 50)
        print("MENU - Algoritmos de Busqueda")
        print("=" * 50)
        print("1. Busqueda Lineal")
        print("2. Busqueda Binaria")
        print("3. Hash Table")
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
                "Un simple for loop que compara cada elemento",
                "left=0, right=n-1, mid=(left+right)//2, ajusta left/right segun la comparacion",
                "Usa hash(key) % size para el indice, y listas para manejar colisiones"
            ]
            print(f"PISTA: {pistas[num - 1]}")
        else:
            [ejercicio_1, ejercicio_2, ejercicio_3][num - 1]()

if __name__ == "__main__":
    main()
