"""
EJERCICIOS - Variables y Tipos de Datos
Ejecuta desde raiz: python scripts/runner.py 1 2 [ejercicio]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1():
    """Crea variables nombre, edad, ciudad y muestralas"""
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass


def ejercicio_2():
    """Pide edad en anos y muestra los dias vividos"""
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass


def ejercicio_3():
    """Pide 3 valores y muestra el tipo de cada uno con type()"""
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
