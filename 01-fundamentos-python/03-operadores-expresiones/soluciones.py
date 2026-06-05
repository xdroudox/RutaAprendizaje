"""
SOLUCIONES - Operadores y Expresiones
Ejecuta desde raiz: python scripts/runner.py 1 3 [ejercicio] -s
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print(">> SOLUCION 1: Calculadora de propina")
    print("-" * 40)
    print("total = float(input('Total de la cuenta: '))")
    print("porcentaje = float(input('Porcentaje de propina: '))")
    print("propina = total * porcentaje / 100")
    print("total_pagar = total + propina")
    print("print(f'Propina: ${propina:.2f}')")
    print("print(f'Total a pagar: ${total_pagar:.2f}')")
    print()
    print("Explicacion: Se multiplica el total por el porcentaje y se divide entre 100. Luego se suma al total original.")


def solucion_2():
    print(">> SOLUCION 2: Ano bisiesto")
    print("-" * 40)
    print("year = int(input('Ingresa un ano: '))")
    print("if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):")
    print("    print(f'{year} es bisiesto')")
    print("else:")
    print("    print(f'{year} no es bisiesto')")
    print()
    print("Explicacion: Un ano es bisiesto si es divisible entre 4 pero no entre 100, o si es divisible entre 400.")


def solucion_3():
    print(">> SOLUCION 3: Verificar triangulo")
    print("-" * 40)
    print("a = float(input('Lado 1: '))")
    print("b = float(input('Lado 2: '))")
    print("c = float(input('Lado 3: '))")
    print("if a + b > c and a + c > b and b + c > a:")
    print("    print('Si puede formar un triangulo')")
    print("else:")
    print("    print('No puede formar un triangulo')")
    print()
    print("Explicacion: La suma de dos lados debe ser mayor que el tercero para todas las combinaciones.")


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
