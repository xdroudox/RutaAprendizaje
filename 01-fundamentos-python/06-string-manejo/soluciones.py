"""
SOLUCIONES - Manejo de Strings
Ejecuta desde raiz: python scripts/runner.py 1 6 [ejercicio] -s
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print(">> SOLUCION 1: Mayusculas y minusculas")
    print("-" * 40)
    print("nombre = input('Ingresa tu nombre: ')")
    print("print(f'En mayusculas: {nombre.upper()}')")
    print("print(f'En minusculas: {nombre.lower()}')")
    print()
    print("Explicacion: upper() convierte todo a mayusculas, lower() convierte todo a minusculas.")


def solucion_2():
    print(">> SOLUCION 2: Invertir palabra")
    print("-" * 40)
    print("palabra = input('Ingresa una palabra: ')")
    print("invertida = palabra[::-1]")
    print("print(f'Palabra invertida: {invertida}')")
    print()
    print("Explicacion: [::-1] invierte la cadena. El primer : indica inicio, el segundo : indica fin, -1 es el paso negativo (inverso).")


def solucion_3():
    print(">> SOLUCION 3: Contar vocales")
    print("-" * 40)
    print("frase = input('Ingresa una frase: ').lower()")
    print("vocales = 'aeiou'")
    print("conteo = 0")
    print("for letra in frase:")
    print("    if letra in vocales:")
    print("        conteo += 1")
    print("print(f'La frase tiene {conteo} vocales')")
    print()
    print("Explicacion: .lower() convierte a minusculas. Se recorre cada letra con for y se verifica si esta en 'aeiou'.")


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
