"""
SOLUCIONES - Variables y Tipos de Datos
Ejecuta desde raiz: python scripts/runner.py 1 2 [ejercicio] -s
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print(">> SOLUCION 1: Presentacion personal")
    print("-" * 40)
    print("nombre = input('Tu nombre: ')")
    print("edad = input('Tu edad: ')")
    print("ciudad = input('Tu ciudad: ')")
    print("print(f'Hola, soy {nombre}, tengo {edad} anos y vivo en {ciudad}')")
    print()
    print("Explicacion: input() pide datos al usuario.")
    print("Las f-strings (f'...{var}...') insertan variables en texto.")


def solucion_2():
    print(">> SOLUCION 2: Edad en dias")
    print("-" * 40)
    print("edad_str = input('Cuantos anos tienes? ')")
    print("edad = int(edad_str)")
    print("dias = edad * 365")
    print("print(f'Has vivido aproximadamente {dias} dias')")
    print()
    print("Explicacion: Convertimos el string a int con int(),")
    print("multiplicamos por 365 y mostramos el resultado.")


def solucion_3():
    print(">> SOLUCION 3: Detector de tipos")
    print("-" * 40)
    print("v1 = input('Valor 1: ')")
    print("v2 = input('Valor 2: ')")
    print("v3 = input('Valor 3: ')")
    print("print(f'{v1} es de tipo {type(v1)}')")
    print("print(f'{v2} es de tipo {type(v2)}')")
    print("print(f'{v3} es de tipo {type(v3)}')")
    print()
    print("Explicacion: input() SIEMPRE devuelve str. type()")
    print("muestra el tipo exacto de cada valor.")


if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
    else:
        for i, sol in enumerate(soluciones, 1):
            print(f"  {i}. {sol.__doc__}")
