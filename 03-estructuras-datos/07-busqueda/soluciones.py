"""
SOLUCIONES - Busqueda
Ejecuta: python scripts/runner.py 3 7 [ejercicio] -s
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: Busqueda lineal")
    print("=" * 50)

    print("""
def busqueda_lineal(arr, objetivo):
    for i in range(len(arr)):
        if arr[i] == objetivo:
            return i
    return -1
""")

    print("--- EXPLICACION ---")
    print("""
La busqueda lineal es la mas simple: recorre el array desde el
indice 0 hasta el final comparando cada elemento.

- Si encuentra el objetivo, devuelve el INDICE (no el valor).
- Si termina el bucle sin encontrar, devuelve -1.

Ejemplo:
  arr = [4, 2, 7, 1, 9], objetivo = 7
  i=0: 4 != 7
  i=1: 2 != 7
  i=2: 7 == 7 → return 2

Complejidad: O(n)
  - Mejor caso: O(1) (el objetivo esta al inicio)
  - Peor caso: O(n) (el objetivo esta al final o no existe)
  - Promedio: O(n)

Ventaja: no requiere datos ordenados.
Desventaja: lenta para arrays grandes.
""")


def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: Busqueda binaria")
    print("=" * 50)

    print("""
def busqueda_binaria(arr, objetivo):
    bajo, alto = 0, len(arr) - 1

    while bajo <= alto:
        medio = (bajo + alto) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1

    return -1
""")

    print("--- EXPLICACION ---")
    print("""
Busca en [1, 3, 5, 7, 9, 11, 13] el valor 7:

Paso 1: bajo=0, alto=6, medio=3
  arr[3] = 7 == 7 → return 3 ✅

Busca el valor 6:
Paso 1: bajo=0, alto=6, medio=3
  arr[3] = 7 > 6 → alto = 2
Paso 2: bajo=0, alto=2, medio=1
  arr[1] = 3 < 6 → bajo = 2
Paso 3: bajo=2, alto=2, medio=2
  arr[2] = 5 < 6 → bajo = 3
Paso 4: bajo=3 > alto=2 → sale del while → return -1

Complejidad: O(log n)
  n=10: ~4 pasos  |  n=100: ~7 pasos  |  n=1M: ~20 pasos

Requisito: el array debe estar ORDENADO.
""")


def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: HashSet simple")
    print("=" * 50)

    print("""
class HashSet:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, valor):
        return hash(valor) % self.size

    def add(self, valor):
        idx = self._hash(valor)
        if valor not in self.buckets[idx]:
            self.buckets[idx].append(valor)

    def contains(self, valor):
        idx = self._hash(valor)
        return valor in self.buckets[idx]

    def remove(self, valor):
        idx = self._hash(valor)
        if valor in self.buckets[idx]:
            self.buckets[idx].remove(valor)
""")

    print("--- EXPLICACION ---")
    print("""
Estructura interna:
  buckets = [[], [], [], [], [], [], [], [], [], []]
              ^ bucket 0    ^ bucket 5

Funcionamiento:
  1. _hash(valor): usa hash() de Python y modulo para obtener
     un indice entre 0 y size-1.
  2. add(): calcula hash, si el valor NO esta en el bucket, lo agrega.
  3. contains(): calcula hash, verifica si esta en el bucket.
  4. remove(): calcula hash, si esta en el bucket, lo elimina.

Manejo de colisiones:
  Dos valores con el mismo hash van al MISMO bucket (lista).
  La busqueda dentro del bucket es O(k) donde k = items/bucket.

Ejemplo con size=3:
  hs = HashSet(3)
  hs.add(10)   # hash(10)%3 = 1 → bucket[1] = [10]
  hs.add(7)    # hash(7)%3 = 1 → bucket[1] = [10, 7]
  hs.add(3)    # hash(3)%3 = 0 → bucket[0] = [3]

  contains(7): hash(7)%3 = 1, 7 in [10, 7] → True

Complejidad PROMEDIO: O(1) para add, contains, remove
  (asumiendo buena distribucion del hash y pocas colisiones).
""")


if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
