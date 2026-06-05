"""
SOLUCIONES - Logica de Programacion
Ejecuta desde raiz: python scripts/runner.py 1 1 [ejercicio] -s
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print(">> SOLUCION 1: Preparar un sandwich")
    print("-" * 40)
    print('print("1. Abrir la nevera")')
    print('print("2. Sacar pan, jamon, queso y lechuga")')
    print('print("3. Colocar dos rebanadas de pan en un plato")')
    print('print("4. Agregar jamon, queso y lechuga")')
    print('print("5. Colocar la otra rebanada de pan encima")')
    print('print("6. Disfrutar del sandwich")')
    print()
    print("Explicacion: Cada paso del mundo real se traduce")
    print("a una instruccion print() en Python.")


def solucion_2():
    print(">> SOLUCION 2: Par o impar")
    print("-" * 40)
    print("numero = int(input('Ingresa un numero: '))")
    print("if numero % 2 == 0:")
    print("    print(f'{numero} es PAR')")
    print("else:")
    print("    print(f'{numero} es IMPAR')")
    print()
    print("Explicacion: El operador % devuelve el resto.")
    print("Si numero % 2 == 0, es divisible por 2 -> PAR.")


def solucion_3():
    print(">> SOLUCION 3: Mayor de 3 numeros")
    print("-" * 40)
    print("a = int(input('Numero 1: '))")
    print("b = int(input('Numero 2: '))")
    print("c = int(input('Numero 3: '))")
    print("if a >= b and a >= c:")
    print("    print(f'El mayor es {a}')")
    print("elif b >= a and b >= c:")
    print("    print(f'El mayor es {b}')")
    print("else:")
    print("    print(f'El mayor es {c}')")
    print()
    print("Explicacion: Comparamos cada numero contra los otros dos")
    print("para encontrar el maximo. Tambien se puede usar max().")


if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
    else:
        print("SOLUCIONES DISPONIBLES:")
        for i, sol in enumerate(soluciones, 1):
            print(f"  {i}. {sol.__doc__}")
