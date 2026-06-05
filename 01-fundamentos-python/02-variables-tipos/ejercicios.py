"""
EJERCICIOS - Variables y Tipos de Datos
Ejecuta: python ejercicios.py [numero] [-p]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    print("=" * 50)
    print(">> EJERCICIO 1: Presentacion personal")
    print("=" * 50)
    print()
    print("Crea variables con tu nombre, edad, ciudad y profesion.")
    print("Luego imprimelas en una presentacion como:")
    print('  "Hola, me llamo [nombre], tengo [edad] anos,")
    print('   soy de [ciudad] y soy [profesion]"')
    print()
    print("PISTA: Usa input() para pedir los datos y f-strings")
    print("       para formatear la salida")
    print()
    print("Edita el archivo y completa la funcion:")
    print("# --- TU CODIGO AQUI ---")

def solucion_1():
    print("SOLUCION 1:")
    print()
    print("nombre = input('Como te llamas? ')")
    print("edad = input('Cuantos anos tienes? ')")
    print("ciudad = input('De donde eres? ')")
    print("profesion = input('Cual es tu profesion? ')")
    print('print(f"Hola, me llamo {nombre}, tengo {edad} anos,')
    print(f'       soy de {ciudad} y soy {profesion}")')
    print()
    print("Explicacion: input() siempre devuelve str. Con f-strings")
    print("podemos incrustar variables dentro del texto.")

def ejercicio_2():
    print("=" * 50)
    print(">> EJERCICIO 2: Calculadora de edad en dias")
    print("=" * 50)
    print()
    print("Pide la edad del usuario en anos y calcula")
    print("cuantos dias ha vivido (aproximadamente).")
    print()
    print("Ej: 25 anos -> 9125 dias (25 * 365)")
    print()
    print("PISTA: Convierte el input a int con int()")
    print()
    print("Edita el archivo y completa la funcion:")
    print("# --- TU CODIGO AQUI ---")

def solucion_2():
    print("SOLUCION 2:")
    print()
    print("edad_str = input('Cuantos anos tienes? ')")
    print("edad = int(edad_str)")
    print("dias = edad * 365")
    print(f'print("Has vivido aproximadamente {dias} dias")')
    print()
    print("Explicacion: Convertimos el string a int con int(),")
    print("multiplicamos por 365 y mostramos el resultado.")

def ejercicio_3():
    print("=" * 50)
    print(">> EJERCICIO 3: Type detective")
    print("=" * 50)
    print()
    print("Pide al usuario que ingrese 3 valores diferentes")
    print("y muestra de que TIPO es cada uno usando type().")
    print()
    print("Ejemplo:")
    print("  Ingresa algo: 42")
    print("  Eso es de tipo <class 'str'> (porque input()")
    print("  siempre devuelve texto!)")
    print()
    print("PISTA: input() SIEMPRE devuelve str. type() te")
    print("       dice el tipo exacto.")
    print()
    print("Edita el archivo y completa la funcion:")
    print("# --- TU CODIGO AQUI ---")

def solucion_3():
    print("SOLUCION 3:")
    print()
    print("v1 = input('Valor 1: ')")
    print("v2 = input('Valor 2: ')")
    print("v3 = input('Valor 3: ')")
    print("print(f'{v1} es de tipo {type(v1)}')")
    print("print(f'{v2} es de tipo {type(v2)}')")
    print("print(f'{v3} es de tipo {type(v3)}')")
    print()
    print("Explicacion: Todo lo que ingresa el usuario es str.")
    print("Incluso si escribe un numero, Python lo trata como")
    print("texto hasta que lo conviertas con int() o float().")

def menu():
    while True:
        print()
        print("=" * 50)
        print("MENU - Variables y Tipos de Datos")
        print("=" * 50)
        print("1. Presentacion personal")
        print("2. Calculadora de edad en dias")
        print("3. Type detective")
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
                "Usa input() para pedir datos y f-strings (f'...{var}...')",
                "Convierte a int con int(), multiplica por 365",
                "input() siempre devuelve str. type() revela el tipo exacto"
            ]
            print(f"PISTA: {pistas[num - 1]}")
        else:
            [ejercicio_1, ejercicio_2, ejercicio_3][num - 1]()

if __name__ == "__main__":
    main()
