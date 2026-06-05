"""
EJERCICIOS - Colecciones
Ejecuta desde raiz: python scripts/runner.py 1 7 [ejercicio]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1():
    """Lista de 5 numeros: crear una lista, mostrar la suma y el promedio de sus elementos"""
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass


def ejercicio_2():
    """Diccionario persona: crear un diccionario con datos de una persona y acceder a sus claves"""
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass


def ejercicio_3():
    """List comprehension pares: generar una lista con los numeros pares del 1 al 20 usando list comprehension"""
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass


if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            print(f">> EJERCICIO {num + 1}: {ejercicios[num].__doc__}")
            print("-" * 40)
            ejercicios[num]()
    else:
        print("EJERCICIOS:")
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
