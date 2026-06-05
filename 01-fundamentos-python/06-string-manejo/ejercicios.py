"""
EJERCICIOS - Manejo de Strings
Ejecuta desde raiz: python scripts/runner.py 1 6 [ejercicio]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1():
    """Mayusculas y minusculas: pedir nombre y mostrarlo en mayusculas y minusculas"""
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass


def ejercicio_2():
    """Invertir palabra: pedir una palabra y mostrarla invertida usando slicing [::-1]"""
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass


def ejercicio_3():
    """Contar vocales: pedir una frase y contar cuantas vocales tiene recorriendola con for"""
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
