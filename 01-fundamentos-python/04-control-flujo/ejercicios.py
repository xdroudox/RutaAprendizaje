"""
EJERCICIOS - Control de Flujo
Ejecuta: python ejercicios.py [numero] [-p]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    print("=" * 50)
    print(">> EJERCICIO 1: Clasificador de notas")
    print("=" * 50)
    print()
    print("Pide una nota numerica del 0 al 100 y muestra la calificacion:")
    print("  - A: 90 a 100")
    print("  - B: 80 a 89")
    print("  - C: 70 a 79")
    print("  - D: 60 a 69")
    print("  - F: 0 a 59")
    print()
    print("Si la nota no esta entre 0 y 100, muestra 'Nota invalida'.")
    print()
    print("PISTA: Usa if, elif, else. Revisa primero si es valida.")
    print()
    print("Edita el archivo y escribe tu codigo:")
    print("# --- TU CODIGO AQUI ---")

def solucion_1():
    print("SOLUCION 1:")
    print()
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
    print()
    print("Explicacion:")
    print("- Validamos primero con if que la nota sea valida")
    print("- elif evalua condiciones en orden descendente")
    print("- else captura todo lo demas (nota < 60)")

def ejercicio_2():
    print("=" * 50)
    print(">> EJERCICIO 2: Tabla de multiplicar")
    print("=" * 50)
    print()
    print("Pide un numero al usuario y muestra su tabla de multiplicar")
    print("del 1 al 10 usando un bucle for y range().")
    print()
    print("Ejemplo para el numero 5:")
    print("  5 x 1 = 5")
    print("  5 x 2 = 10")
    print("  ...")
    print("  5 x 10 = 50")
    print()
    print("PISTA: range(1, 11) genera numeros del 1 al 10.")
    print("       Usa f-strings para formatear la salida.")
    print()
    print("Edita el archivo y escribe tu codigo:")
    print("# --- TU CODIGO AQUI ---")

def solucion_2():
    print("SOLUCION 2:")
    print()
    print("numero = int(input('Que tabla deseas ver? '))")
    print("for i in range(1, 11):")
    print("    resultado = numero * i")
    print("    print(f'{numero} x {i} = {resultado}')")
    print()
    print("Explicacion:")
    print("- range(1, 11) genera 1, 2, 3, ..., 10")
    print("- El bucle for itera 10 veces, i toma cada valor")
    print("- Multiplicamos numero * i y mostramos con f-string")

def ejercicio_3():
    print("=" * 50)
    print(">> EJERCICIO 3: Adivina el numero")
    print("=" * 50)
    print()
    print("El programa va a 'pensar' un numero aleatorio entre 1 y 20.")
    print("El usuario tiene 5 intentos para adivinarlo.")
    print()
    print("En cada intento:")
    print("  - Si acierta, muestra 'Felicidades!' y termina (break)")
    print("  - Si el numero es mayor, muestra 'Muy alto'")
    print("  - Si el numero es menor, muestra 'Muy bajo'")
    print("  - Si el numero no esta entre 1 y 20, muestra 'Fuera de rango'")
    print("    y continua (continue)")
    print("  - Si se agotan los intentos, muestra el numero correcto")
    print()
    print("PISTA: Usa random.randint(1, 20) y un while con contador.")
    print("       break para salir al acertar, continue para saltar.")
    print()
    print("Edita el archivo y escribe tu codigo:")
    print("# --- TU CODIGO AQUI ---")

def solucion_3():
    print("SOLUCION 3:")
    print()
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
    print()
    print("Explicacion:")
    print("- random.randint genera un numero aleatorio")
    print("- while se ejecuta mientras queden intentos")
    print("- continue salta el resto si el numero esta fuera de rango")
    print("- break termina el juego si acierta")
    print("- intentos -= 1 reduce el contador en cada fallo")

def menu():
    while True:
        print()
        print("=" * 50)
        print("MENU - Control de Flujo")
        print("=" * 50)
        print("1. Clasificador de notas")
        print("2. Tabla de multiplicar")
        print("3. Adivina el numero")
        print("0. Salir")
        print()
        opcion = input("Selecciona un ejercicio: ")
        if opcion == "1":
            ejercicio_1()
            input("ENTER para continuar...")
        elif opcion == "2":
            ejercicio_2()
            input("ENTER para continuar...")
        elif opcion == "3":
            ejercicio_3()
            input("ENTER para continuar...")
        elif opcion == "0":
            print("Sigue practicando!")
            break

def main():
    args = sys.argv[1:]
    if not args:
        menu()
        return
    if "-s" in args:
        idx = args.index("-s")
        if idx + 1 < len(args) and args[idx + 1].isdigit():
            [solucion_1, solucion_2, solucion_3][int(args[idx + 1]) - 1]()
        return
    if args[0].isdigit():
        num = int(args[0])
        if "-p" in args:
            pistas = [
                "Usa if/elif/else. Valida nota < 0 or nota > 100 primero",
                "for i in range(1, 11): y f-string para la salida",
                "random.randint(1,20). Usa while, break al acertar, continue si fuera de rango"
            ]
            print(f"PISTA: {pistas[num - 1]}")
        else:
            [ejercicio_1, ejercicio_2, ejercicio_3][num - 1]()

if __name__ == "__main__":
    main()
