"""
SOLUCIONES - Complejidad Algoritmica
Ejecuta: python scripts/runner.py 3 1 [ejercicio] -s
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    print(">> SOLUCION 1: Analisis de Big O")
    print("-" * 40)
    print("Fragmento A (suma): O(n) - Un solo bucle que recorre el array")
    print("Fragmento B (get_first): O(1) - Acceso directo por indice")
    print("Fragmento C (bubble_sort): O(n^2) - Dos bucles anidados")
    print("Fragmento D (busqueda_binaria): O(log n) - Divide espacio a la mitad")
    print()
    print("Explicacion:")
    print("- O(1): tiempo constante, no depende del tamano")
    print("- O(log n): divide el problema en cada paso")
    print("- O(n): lineal, crece proporcional a la entrada")
    print("- O(n^2): cuadratico, bucles anidados")

def solucion_2():
    print(">> SOLUCION 2: Ordenar por eficiencia")
    print("-" * 40)
    print("Orden correcto (menor a mayor):")
    print("  1. O(1)      - Acceder a indice de array")
    print("  2. O(log n)  - Busqueda binaria")
    print("  3. O(n)      - Recorrer array con un bucle")
    print("  4. O(n log n)- Merge sort")
    print("  5. O(n^2)    - Bubble sort")
    print("  6. O(2^n)    - Fibonacci recursivo")
    print("  7. O(n!)     - Permutaciones")
    print()
    print("Explicacion: A medida que n crece, la diferencia es abismal.")
    print("Ejemplo para n=1000: O(1)=1, O(log n)=10, O(n)=1000,")
    print("O(n log n)=10000, O(n^2)=1,000,000, O(2^n)=inmenso")

def solucion_3():
    print(">> SOLUCION 3: Nested loops")
    print("-" * 40)
    print("Ejemplo de nested loops y sus complejidades:")
    print()
    print("for i in range(n):           # O(n)")
    print("    for j in range(n):       # O(n)")

    print("    -> Complejidad: O(n^2)")
    print()
    print("for i in range(n):           # O(n)")
    print("    for j in range(i):       # O(i) promedio n/2")
    print("    -> Complejidad: O(n^2/2) = O(n^2)")
    print()
    print("for i in range(n):           # O(n)")
    print("    for j in range(m):       # O(m)")
    print("    -> Complejidad: O(n*m)")

if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
