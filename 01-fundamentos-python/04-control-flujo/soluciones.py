"""
SOLUCIONES - Control de Flujo
Ejecuta: python soluciones.py [numero]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    print("=" * 50)
    print("SOLUCION 1: Clasificador de notas")
    print("=" * 50)
    print()
    print("Codigo:")
    print("```python")
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
    print("```")
    print()
    print("Explicacion:")
    print("- Primero validamos que la nota este en rango (0-100)")
    print("- elif evalua condiciones de mayor a menor")
    print("- Si llega a else, es porque nota < 60, entonces F")
    print("- El orden importa: si ponemos nota >= 60 antes, nunca llegaria a F")

def solucion_2():
    print("=" * 50)
    print("SOLUCION 2: Tabla de multiplicar")
    print("=" * 50)
    print()
    print("Codigo:")
    print("```python")
    print("numero = int(input('Que tabla deseas ver? '))")
    print("for i in range(1, 11):")
    print("    resultado = numero * i")
    print("    print(f'{numero} x {i} = {resultado}')")
    print("```")
    print()
    print("Explicacion:")
    print("- for i in range(1, 11) itera sobre 1, 2, 3, ..., 10")
    print("- En cada iteracion, multiplicamos numero por i")
    print("- range(inicio, fin) genera numeros desde inicio hasta fin-1")

def solucion_3():
    print("=" * 50)
    print("SOLUCION 3: Adivina el numero")
    print("=" * 50)
    print()
    print("Codigo:")
    print("```python")
    print("import random")
    print("secreto = random.randint(1, 20)")
    print("intentos = 5")
    print("while intentos > 0:")
    print("    num = int(input('Adivina el numero (1-20): '))")
    print("    if num < 1 or num > 20:")
    print("        print('Fuera de rango')")
    print("        continue")
    print("    if num == secreto:")
    print("        print('Felicidades! Adivinaste!')")
    print("        break")
    print("    elif num > secreto:")
    print("        print('Muy alto')")
    print("    else:")
    print("        print('Muy bajo')")
    print("    intentos -= 1")
    print("if intentos == 0:")
    print("    print(f'Se acabaron los intentos. Era {secreto}')")
    print("```")
    print()
    print("Explicacion:")
    print("- random.randint(1, 20) genera un numero aleatorio entre 1 y 20")
    print("- while intentos > 0: repite mientras queden intentos")
    print("- continue salta a la siguiente iteracion sin gastar intento")
    print("- break sale del bucle cuando acierta")
    print("- intentos -= 1 reduce el contador (solo en fallos validos)")

def menu():
    while True:
        print()
        print("=" * 50)
        print("SOLUCIONES - Control de Flujo")
        print("=" * 50)
        print("1. Clasificador de notas")
        print("2. Tabla de multiplicar")
        print("3. Adivina el numero")
        print("0. Salir")
        print()
        opcion = input("Ver solucion: ")
        sols = {"1": solucion_1, "2": solucion_2, "3": solucion_3}
        if opcion in sols:
            sols[opcion]()
            input("ENTER para continuar...")
        elif opcion == "0":
            break

def main():
    args = sys.argv[1:]
    if args and args[0].isdigit():
        [solucion_1, solucion_2, solucion_3][int(args[0]) - 1]()
    else:
        menu()

if __name__ == "__main__":
    main()
