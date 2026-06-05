"""
SOLUCIONES - Funciones
Ejecuta desde raiz: python scripts/runner.py 1 5 [ejercicio] -s
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print(">> SOLUCION 1: Funcion suma")
    print("-" * 40)
    print("def sumar(a, b):")
    print("    return a + b")
    print()
    print("num1 = float(input('Ingresa el primer numero: '))")
    print("num2 = float(input('Ingresa el segundo numero: '))")
    print("resultado = sumar(num1, num2)")
    print("print(f'La suma es: {resultado}')")
    print()
    print("Explicacion: def define la funcion con dos parametros. return devuelve el resultado de la suma.")


def solucion_2():
    print(">> SOLUCION 2: Funcion promedio")
    print("-" * 40)
    print("def promedio(lista):")
    print("    return sum(lista) / len(lista)")
    print()
    print("numeros = [10, 20, 30, 40, 50]")
    print("print(f'El promedio es: {promedio(numeros)}')")
    print()
    print("Explicacion: sum() suma todos los elementos, len() da la cantidad. La funcion recibe una lista como parametro.")


def solucion_3():
    print(">> SOLUCION 3: Filtrar pares con lambda")
    print("-" * 40)
    print("numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
    print("pares = list(filter(lambda x: x % 2 == 0, numeros))")
    print("print(f'Numeros pares: {pares}')")
    print()
    print("Explicacion: filter() aplica la funcion lambda a cada elemento. La lambda devuelve True si x es par. list() convierte el filtro en lista.")


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
