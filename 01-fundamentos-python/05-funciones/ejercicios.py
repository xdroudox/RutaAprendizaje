"""
EJERCICIOS - Funciones
Ejecuta: python ejercicios.py [numero] [-p]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    print("=" * 50)
    print(">> EJERCICIO 1: Calculadora con funciones")
    print("=" * 50)
    print()
    print("Crea las siguientes funciones:")
    print("  - sumar(a, b): devuelve a + b")
    print("  - restar(a, b): devuelve a - b")
    print("  - multiplicar(a, b): devuelve a * b")
    print("  - dividir(a, b): devuelve a / b (o 'Error' si b es 0)")
    print()
    print("El programa debe pedir dos numeros y la operacion (+, -, *, /)")
    print("y mostrar el resultado usando las funciones.")
    print()
    print("PISTA: return devuelve el resultado. Usa if b == 0 para evitar")
    print("       la division entre cero.")
    print()
    print("Edita el archivo y escribe tu codigo:")
    print("# --- TU CODIGO AQUI ---")

def solucion_1():
    print("SOLUCION 1:")
    print()
    print("def sumar(a, b):")
    print("    return a + b")
    print("def restar(a, b):")
    print("    return a - b")
    print("def multiplicar(a, b):")
    print("    return a * b")
    print("def dividir(a, b):")
    print("    if b == 0:")
    print("        return 'Error: division entre cero'")
    print("    return a / b")
    print("num1 = float(input('Primer numero: '))")
    print("num2 = float(input('Segundo numero: '))")
    print("op = input('Operacion (+, -, *, /): ')")
    print("if op == '+':")
    print("    print(sumar(num1, num2))")
    print("elif op == '-':")
    print("    print(restar(num1, num2))")
    print("elif op == '*':")
    print("    print(multiplicar(num1, num2))")
    print("elif op == '/':")
    print("    print(dividir(num1, num2))")
    print("else:")
    print("    print('Operacion no valida')")
    print()
    print("Explicacion:")
    print("- def crea una funcion reutilizable")
    print("- return devuelve el valor calculado")
    print("- Cada funcion hace una sola operacion (responsabilidad unica)")

def ejercicio_2():
    print("=" * 50)
    print(">> EJERCICIO 2: Contador de vocales")
    print("=" * 50)
    print()
    print("Crea una funcion contar_vocales(texto, incluir_mayusculas=True)")
    print("que cuente cuantas vocales (a, e, i, o, u) tiene un texto.")
    print()
    print("- Si incluir_mayusculas es True, cuenta vocales en mayusculas")
    print("  y minusculas. Si es False, solo minusculas.")
    print("- La funcion debe devolver el numero total de vocales.")
    print()
    print("Pide al usuario un texto y muestra el resultado.")
    print()
    print("PISTA: Usa .lower() y recorre el texto con for.")
    print("       'aeiou' contiene las vocales a buscar.")
    print()
    print("Edita el archivo y escribe tu codigo:")
    print("# --- TU CODIGO AQUI ---")

def solucion_2():
    print("SOLUCION 2:")
    print()
    print("def contar_vocales(texto, incluir_mayusculas=True):")
    print("    vocales = 'aeiou'")
    print("    conteo = 0")
    print("    for letra in texto:")
    print("        if incluir_mayusculas:")
    print("            if letra.lower() in vocales:")
    print("                conteo += 1")
    print("        else:")
    print("            if letra in vocales:")
    print("                conteo += 1")
    print("    return conteo")
    print("texto = input('Ingresa un texto: ')")
    print("resultado = contar_vocales(texto)")
    print("print(f'El texto tiene {resultado} vocales')")
    print()
    print("Explicacion:")
    print("- incluir_mayusculas=True es un parametro con valor por defecto")
    print("- .lower() convierte a minusculas para comparar")
    print("- El ambito de conteo es local a la funcion (scope)")
    print("- return devuelve el resultado al programa principal")

def ejercicio_3():
    print("=" * 50)
    print(">> EJERCICIO 3: Ordenar con lambda")
    print("=" * 50)
    print()
    print("Pide al usuario 5 numeros enteros, guardalos en una lista")
    print("y muestralos ordenados de mayor a menor.")
    print()
    print("Usa la funcion sorted() con una funcion lambda como key.")
    print()
    print("Ejemplo:")
    print("  Ingresa 5 numeros:")
    print("  3, 7, 1, 9, 4")
    print("  Ordenados (mayor a menor): [9, 7, 4, 3, 1]")
    print()
    print("PISTA: sorted(lista, key=lambda x: -x) los ordena de mayor a menor.")
    print("       Usa un for con range(5) y append() para la lista.")
    print()
    print("Edita el archivo y escribe tu codigo:")
    print("# --- TU CODIGO AQUI ---")

def solucion_3():
    print("SOLUCION 3:")
    print()
    print("numeros = []")
    print("for i in range(5):")
    print("    n = int(input(f'Numero {i+1}: '))")
    print("    numeros.append(n)")
    print("ordenados = sorted(numeros, key=lambda x: -x)")
    print("print(f'Ordenados (mayor a menor): {ordenados}')")
    print()
    print("Explicacion:")
    print("- for con range(5) pide 5 numeros")
    print("- append() agrega cada numero a la lista")
    print("- sorted() ordena sin modificar la lista original")
    print("- key=lambda x: -x usa una funcion anonima para invertir el orden")

def menu():
    while True:
        print()
        print("=" * 50)
        print("MENU - Funciones")
        print("=" * 50)
        print("1. Calculadora con funciones")
        print("2. Contador de vocales")
        print("3. Ordenar con lambda")
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
                "Crea funciones con def. return para devolver. Valida b == 0 en dividir",
                "def contar_vocales(texto, incluir_mayusculas=True). for letra in texto",
                "sorted(lista, key=lambda x: -x). Usa append() para construir la lista"
            ]
            print(f"PISTA: {pistas[num - 1]}")
        else:
            [ejercicio_1, ejercicio_2, ejercicio_3][num - 1]()

if __name__ == "__main__":
    main()
