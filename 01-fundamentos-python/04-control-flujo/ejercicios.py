"""
EJERCICIOS - Control de Flujo
Ejecuta desde raiz: python scripts/runner.py 1 4 [ejercicio]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1():
    """Clasificar nota: pide nota 0-100 y muestra A (>=90), B (>=80), C (>=70), D (>=60), F (<60)"""
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass


def ejercicio_2():
    """Tabla de multiplicar: pide un numero y muestra su tabla del 1 al 10 usando for y range()"""
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass


def ejercicio_3():
    """Adivinar un numero: el programa genera un numero aleatorio y el usuario debe adivinarlo con pistas"""
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
