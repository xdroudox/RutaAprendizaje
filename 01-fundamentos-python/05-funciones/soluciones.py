"""
SOLUCIONES - Funciones
Ejecuta: python soluciones.py [numero]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    print("=" * 50)
    print("SOLUCION 1: Calculadora con funciones")
    print("=" * 50)
    print()
    print("Codigo:")
    print("```python")
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
    print("```")
    print()
    print("Explicacion:")
    print("- def sumar(a, b): define una funcion con dos parametros")
    print("- return a + b calcula y devuelve el resultado")
    print("- La validacion en dividir evita errores de division entre cero")
    print("- Cada funcion encapsula una operacion especifica")

def solucion_2():
    print("=" * 50)
    print("SOLUCION 2: Contador de vocales")
    print("=" * 50)
    print()
    print("Codigo:")
    print("```python")
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
    print("```")
    print()
    print("Explicacion:")
    print("- incluir_mayusculas=True: parametro con valor por defecto")
    print("- Si es True, usamos .lower() para contar mayusculas tambien")
    print("- letra in vocales verifica si la letra esta en 'aeiou'")
    print("- El scope de conteo es local, no afecta al programa principal")

def solucion_3():
    print("=" * 50)
    print("SOLUCION 3: Ordenar con lambda")
    print("=" * 50)
    print()
    print("Codigo:")
    print("```python")
    print("numeros = []")
    print("for i in range(5):")
    print("    n = int(input(f'Numero {i+1}: '))")
    print("    numeros.append(n)")
    print("ordenados = sorted(numeros, key=lambda x: -x)")
    print("print(f'Ordenados (mayor a menor): {ordenados}')")
    print("```")
    print()
    print("Explicacion:")
    print("- Los numeros se guardan en una lista con append()")
    print("- sorted() devuelve una nueva lista ordenada")
    print("- key=lambda x: -x usa una funcion anonima que devuelve el negativo")
    print("- Al ordenar por -x, los numeros mas grandes (ej: 9 -> -9) van primero")
    print("- La lista original no se modifica")

def menu():
    while True:
        print()
        print("=" * 50)
        print("SOLUCIONES - Funciones")
        print("=" * 50)
        print("1. Calculadora con funciones")
        print("2. Contador de vocales")
        print("3. Ordenar con lambda")
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
