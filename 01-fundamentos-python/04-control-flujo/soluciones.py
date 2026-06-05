"""
SOLUCIONES - Control de Flujo
Ejecuta desde raiz: python scripts/runner.py 1 4 [ejercicio] -s
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print(">> SOLUCION 1: Clasificador de notas")
    print("-" * 40)
    print("nota = int(input('Ingresa la nota (0-100): '))")
    print("if nota < 0 or nota > 100:")
    print("    print('Nota invalida')")
    print("elif nota >= 90:")
    print("    print('Calificacion: A')")
    print("elif nota >= 80:")
    print("    print('Calificacion: B')")
    print("elif nota >= 70:")
    print("    print('Calificacion: C')")
    print("elif nota >= 60:")
    print("    print('Calificacion: D')")
    print("else:")
    print("    print('Calificacion: F')")
    print()
    print("Explicacion: Se evaluan condiciones en orden descendente. El primer elif que se cumpla ejecuta su bloque.")


def solucion_2():
    print(">> SOLUCION 2: Tabla de multiplicar")
    print("-" * 40)
    print("numero = int(input('Que tabla deseas ver? '))")
    print("for i in range(1, 11):")
    print("    print(f'{numero} x {i} = {numero * i}')")
    print()
    print("Explicacion: range(1, 11) genera numeros del 1 al 10. El bucle for itera sobre cada uno y multiplica.")


def solucion_3():
    print(">> SOLUCION 3: Adivina el numero")
    print("-" * 40)
    print("import random")
    print("secreto = random.randint(1, 20)")
    print("while True:")
    print("    num = int(input('Adivina el numero (1-20): '))")
    print("    if num == secreto:")
    print("        print('Felicidades! Adivinaste!')")
    print("        break")
    print("    elif num > secreto:")
    print("        print('Muy alto')")
    print("    else:")
    print("        print('Muy bajo')")
    print()
    print("Explicacion: random.randint genera el numero. while True se repite hasta que el usuario acierte. break sale del bucle.")


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
