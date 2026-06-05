"""
SOLUCIONES - Colecciones
Ejecuta desde raiz: python scripts/runner.py 1 7 [ejercicio] -s
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print(">> SOLUCION 1: Lista de 5 numeros")
    print("-" * 40)
    print("numeros = [15, 22, 8, 31, 12]")
    print("suma = sum(numeros)")
    print("promedio = suma / len(numeros)")
    print("print(f'Lista: {numeros}')")
    print("print(f'Suma: {suma}')")
    print("print(f'Promedio: {promedio}')")
    print()
    print("Explicacion: sum() suma todos los elementos, len() da la cantidad. El promedio es suma / cantidad.")


def solucion_2():
    print(">> SOLUCION 2: Diccionario persona")
    print("-" * 40)
    print("persona = {")
    print("    'nombre': 'Carlos',")
    print("    'edad': 30,")
    print("    'ciudad': 'Bogota',")
    print("    'profesion': 'Ingeniero'")
    print("}")
    print("print(f'Nombre: {persona[\"nombre\"]}')")
    print("print(f'Edad: {persona[\"edad\"]}')")
    print("print(f'Ciudad: {persona[\"ciudad\"]}')")
    print("print(f'Profesion: {persona[\"profesion\"]}')")
    print()
    print("Explicacion: Los diccionarios guardan pares clave:valor. Se accede con diccionario[clave].")


def solucion_3():
    print(">> SOLUCION 3: List comprehension pares")
    print("-" * 40)
    print("pares = [x for x in range(1, 21) if x % 2 == 0]")
    print("print(f'Numeros pares del 1 al 20: {pares}')")
    print()
    print("Explicacion: [x for x in range(1, 21) if x % 2 == 0] genera una lista solo con los pares. range(1, 21) va del 1 al 20.")


if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
    else:
        print("SOLUCIONES:")
        for i, sol in enumerate(soluciones, 1):
            print(f"  {i}. {sol.__name__}")
