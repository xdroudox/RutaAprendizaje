"""
SOLUCIONES - Busqueda
Ejecuta: python scripts/runner.py 3 7 [ejercicio] -s
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    print(">> SOLUCION 1: Busqueda lineal")
    print("-" * 40)
    print("def busqueda_lineal(arr, objetivo):")
    print("    for i in range(len(arr)):")
    print("        if arr[i] == objetivo:")
    print("            return i")
    print("    return -1")
    print()
    print("Explicacion: Recorre el array de principio a fin.")
    print("Complejidad: O(n) en el peor caso.")

def solucion_2():
    print(">> SOLUCION 2: Busqueda binaria")
    print("-" * 40)
    print("def busqueda_binaria(arr, objetivo):")
    print("    bajo, alto = 0, len(arr) - 1")
    print("    while bajo <= alto:")
    print("        medio = (bajo + alto) // 2")
    print("        if arr[medio] == objetivo:")
    print("            return medio")
    print("        elif arr[medio] < objetivo:")
    print("            bajo = medio + 1")
    print("        else:")
    print("            alto = medio - 1")
    print("    return -1")
    print()
    print("Explicacion: Requiere array ordenado. Divide el espacio")
    print("de busqueda a la mitad en cada paso. O(log n).")

def solucion_3():
    print(">> SOLUCION 3: HashSet simple")
    print("-" * 40)
    print("class HashSet:")
    print("    def __init__(self, size=10):")
    print("        self.size = size")
    print("        self.buckets = [[] for _ in range(size)]")
    print()
    print("    def _hash(self, valor):")
    print("        return hash(valor) % self.size")
    print()
    print("    def add(self, valor):")
    print("        idx = self._hash(valor)")
    print("        if valor not in self.buckets[idx]:")
    print("            self.buckets[idx].append(valor)")
    print()
    print("    def contains(self, valor):")
    print("        idx = self._hash(valor)")
    print("        return valor in self.buckets[idx]")
    print()
    print("    def remove(self, valor):")
    print("        idx = self._hash(valor)")
    print("        if valor in self.buckets[idx]:")
    print("            self.buckets[idx].remove(valor)")
    print()
    print("Explicacion: Usamos hash() de Python para obtener el indice")
    print("del bucket. Cada bucket es una lista (manejo de colisiones).")

if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
