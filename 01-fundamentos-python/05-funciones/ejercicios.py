"""
EJERCICIOS - Funciones
Ejecuta desde raiz: python scripts/runner.py 1 5 [ejercicio]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1():
    """Funcion suma: crear una funcion que reciba 2 numeros y devuelva su suma"""
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass


def ejercicio_2():
    """Funcion promedio: crear una funcion que reciba una lista y devuelva el promedio"""
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass


def ejercicio_3():
    """Filtrar pares con lambda: usar filter() con una funcion lambda para obtener solo los pares de una lista"""
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
