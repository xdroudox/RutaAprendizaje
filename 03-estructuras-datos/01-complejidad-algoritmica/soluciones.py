"""
SOLUCIONES - Complejidad Algoritmica
Ejecuta: python scripts/runner.py 3 1 [ejercicio] -s
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: Identificar Big O")
    print("=" * 50)

    print("""
A) arr[0] → O(1) — CONSTANTE
   Acceder a un indice especifico de un array NO depende del tamano.
   El calculo es: direccion_base + (indice * tamano_elemento).
   Siempre 1 operacion, sin importar si el array tiene 10 o 10 millones.

B) for x in arr: print(x) → O(n) — LINEAL
   Se ejecuta UNA vez por cada elemento del array.
   Si hay 10 elementos → 10 prints. Si hay 1000 → 1000 prints.
   Crece en proporcion DIRECTA al tamano de la entrada.

C) for i in arr: for j in arr: print(i, j) → O(n^2) — CUADRATICO
   Por cada elemento del array exterior, recorre TODO el array interior.
   n elementos * n elementos = n^2 operaciones.
   Para n=1000: 1,000,000 de operaciones.

D) arr[len(arr)//2] → O(1) — CONSTANTE
   Sigue siendo acceso directo por indice. len(arr) es O(1),
   la division es O(1), y el acceso es O(1).
""")


def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: Ordenar por eficiencia")
    print("=" * 50)

    print("""
Orden correcto (de MENOR a MAYOR crecimiento):

  1) O(1)       - Constante
  2) O(log n)   - Logaritmico
  3) O(n)       - Lineal
  4) O(n log n) - Log-lineal
  5) O(n^2)     - Cuadratico
  6) O(2^n)     - Exponencial
  7) O(n!)      - Factorial

Para n = 30:
  O(1)     = 1
  O(log n) = ~5
  O(n)     = 30
  O(n log n) = ~147
  O(n^2)   = 900
  O(2^n)   = ~1,000,000,000
  O(n!)    = ~2.65 * 10^32 (MAS que atomos en el universo)

Diferencia entre O(n log n) y O(n^2):
  Con n = 100,000:
    - O(n log n) ≈ 1,660,000 operaciones (~2 ms)
    - O(n^2) = 10,000,000,000 operaciones (~20 segundos)
""")


def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: Nested loops")
    print("=" * 50)

    print("""
FRAGMENTO A: O(n^2)

  for i in range(n):        # se ejecuta n veces
      for j in range(n):    # se ejecuta n veces por cada i
          print(i, j)       # total: n * n = n^2

  Explicacion: El bucle exterior da n vueltas, y por cada vuelta
  el bucle interior da n vueltas. Total = n * n = n^2.
  Para n=100: 10,000 iteraciones.

FRAGMENTO B: O(n^2)

  for i in range(n):        # se ejecuta n veces
      for j in range(i):    # se ejecuta i veces (0, 1, 2, ..., n-1)
          print(i, j)       # total: 0+1+2+...+(n-1) = n(n-1)/2

  Explicacion: No son n*n exactas, sino la suma de 1 a n:
  0 + 1 + 2 + ... + (n-1) = n(n-1)/2 = n^2/2 - n/2
  Ignoramos constantes y termino menor → O(n^2).

FRAGMENTO C: O(n*m)

  for i in range(n):        # se ejecuta n veces
      for j in range(m):    # se ejecuta m veces por cada i
          print(i, j)       # total: n * m

  Explicacion: n y m son independientes. No podemos simplificar
  porque no sabemos cual es mayor. La complejidad es O(n*m).
  Ejemplo: matriz de n filas y m columnas = O(n*m).
""")


if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
