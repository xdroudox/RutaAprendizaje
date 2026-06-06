"""
EJERCICIOS - Busqueda
Ejecuta desde raiz: python scripts/runner.py 3 7 [ejercicio]

Niveles:
  🟢 Ej 1: Busqueda lineal
  🟡 Ej 2: Busqueda binaria
  🔴 Ej 3: HashSet simple

Pistas: python scripts/runner.py 3 7 N -p [1|2|3]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1(pista=0):
    """🟢 Busqueda lineal"""
    print(">> 🟢 EJERCICIO 1: Busqueda lineal")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1:")
        print("  def busqueda_lineal(arr, objetivo):")
        print("      for i in range(len(arr)):")
        print("          if arr[i] == objetivo:")
        print("              return i")
        print("      return -1")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  - Recorre el array de principio a fin")
        print("  - Si encuentra el valor, devuelve su indice")
        print("  - Si termina el bucle sin encontrar, devuelve -1")
        return
    elif pista == 3:
        print("\n💡 Pista 3:")
        print("  Entrada: arr = [4, 2, 7, 1, 9], objetivo = 7")
        print("  Recorrido: arr[0]=4, arr[1]=2, arr[2]=7 → return 2")
        return

    print("\nImplementa:")
    print("  def busqueda_lineal(arr, objetivo) -> int:")
    print()
    print("  Entrada: [4, 2, 7, 1, 9], buscar 7")
    print("  Salida:  2 (indice donde esta 7)")
    print()
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")


def ejercicio_2(pista=0):
    """🟡 Busqueda binaria"""
    print(">> 🟡 EJERCICIO 2: Busqueda binaria")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1:")
        print("  bajo, alto = 0, len(arr) - 1")
        print("  while bajo <= alto:")
        print("      medio = (bajo + alto) // 2")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  if arr[medio] == objetivo: return medio")
        print("  if arr[medio] < objetivo: bajo = medio + 1")
        print("  else: alto = medio - 1")
        return
    elif pista == 3:
        print("\n💡 Pista 3:")
        print("  def busqueda_binaria(arr, objetivo):")
        print("      bajo, alto = 0, len(arr) - 1")
        print("      while bajo <= alto:")
        print("          medio = (bajo + alto) // 2")
        print("          if arr[medio] == objetivo:")
        print("              return medio")
        print("          elif arr[medio] < objetivo:")
        print("              bajo = medio + 1")
        print("          else:")
        print("              alto = medio - 1")
        print("      return -1")
        return

    print("\nImplementa:")
    print("  def busqueda_binaria(arr, objetivo) -> int:")
    print("      # arr esta ORDENADO (requisito)")
    print()
    print("  Entrada: [1, 3, 5, 7, 9, 11], buscar 7")
    print("  Salida:  3")
    print()
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")


def ejercicio_3(pista=0):
    """🔴 HashSet simple"""
    print(">> 🔴 EJERCICIO 3: HashSet simple")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1:")
        print("  class HashSet:")
        print("      def __init__(self, size=10):")
        print("          self.size = size")
        print("          self.buckets = [[] for _ in range(size)]")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  _hash: hash(valor) % self.size")
        print("  add: idx = _hash(valor); si no esta en bucket, agregar")
        print("  contains: idx = _hash; return valor in bucket")
        print("  remove: idx = _hash; si esta, bucket.remove(valor)")
        return
    elif pista == 3:
        print("\n💡 Pista 3:")
        print("  class HashSet:")
        print("      def __init__(self, size=10):")
        print("          self.size = size")
        print("          self.buckets = [[] for _ in range(size)]")
        print("      def _hash(self, valor):")
        print("          return hash(valor) % self.size")
        print("      def add(self, valor):")
        print("          idx = self._hash(valor)")
        print("          if valor not in self.buckets[idx]:")
        print("              self.buckets[idx].append(valor)")
        print("      def contains(self, valor):")
        print("          return valor in self.buckets[self._hash(valor)]")
        print("      def remove(self, valor):")
        print("          idx = self._hash(valor)")
        print("          if valor in self.buckets[idx]:")
        print("              self.buckets[idx].remove(valor)")
        return

    print("\nImplementa la clase HashSet:")
    print("  - __init__(size=10): self.buckets = [[] for _ in range(size)]")
    print("  - _hash(valor): funcion hash interna")
    print("  - add(valor): agrega si no existe")
    print("  - contains(valor): True/False")
    print("  - remove(valor): elimina si existe")
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
