"""
SOLUCIONES - Variables y Tipos de Datos
Ejecuta: python soluciones.py [numero]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    print("=" * 50)
    print("SOLUCION 1: Presentacion personal")
    print("=" * 50)
    print()
    print("Codigo:")
    print("```python")
    print("nombre = input('Como te llamas? ')")
    print("edad = input('Cuantos anos tienes? ')")
    print("ciudad = input('De donde eres? ')")
    print("profesion = input('Cual es tu profesion? ')")
    print("print()")
    print('print(f"Hola, me llamo {nombre}, tengo {edad} anos,")')
    print(f'print(f"soy de {ciudad} y soy {profesion}")')
    print("```")
    print()
    print("Explicacion:")
    print("- input() pide datos al usuario y los guarda en variables")
    print("- Las f-strings (f'...{var}...') incrustan variables en texto")
    print("- El resultado se ve limpio y formateado")

def solucion_2():
    print("=" * 50)
    print("SOLUCION 2: Calculadora de edad en dias")
    print("=" * 50)
    print()
    print("Codigo:")
    print("```python")
    print("edad_str = input('Cuantos anos tienes? ')")
    print("edad = int(edad_str)")
    print("dias = edad * 365")
    print('print(f"Has vivido aproximadamente {dias} dias")')
    print("```")
    print()
    print("Explicacion:")
    print("- input() devuelve str, necesitamos convertirlo a int")
    print("- int() convierte el texto a numero entero")
    print("- Multiplicamos edad * 365 para obtener los dias")

def solucion_3():
    print("=" * 50)
    print("SOLUCION 3: Type detective")
    print("=" * 50)
    print()
    print("Codigo:")
    print("```python")
    print("v1 = input('Valor 1: ')")
    print("v2 = input('Valor 2: ')")
    print("v3 = input('Valor 3: ')")
    print("print(f'{v1} es de tipo {type(v1)}')")
    print("print(f'{v2} es de tipo {type(v2)}')")
    print("print(f'{v3} es de tipo {type(v3)}')")
    print("```")
    print()
    print("Explicacion:")
    print("- type() revela el tipo de dato de cualquier variable")
    print("- Notaras que TODO lo de input() es <class 'str'>")
    print("- Incluso si escribes numeros, son strings hasta")
    print("  que los conviertas con int() o float()")

def menu():
    while True:
        print()
        print("=" * 50)
        print("SOLUCIONES - Variables y Tipos de Datos")
        print("=" * 50)
        print("1. Presentacion personal")
        print("2. Calculadora de edad en dias")
        print("3. Type detective")
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
