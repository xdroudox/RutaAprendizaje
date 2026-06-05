"""
EJERCICIOS - Colecciones
Ejecuta: python ejercicios.py [numero] [-p]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    print("=" * 50)
    print(">> EJERCICIO 1: Lista de compras")
    print("=" * 50)
    print()
    print("Crea un programa que administre una lista de compras:")
    print("  - El usuario puede agregar items (append)")
    print("  - Eliminar items por nombre (remove)")
    print("  - Ver la lista completa")
    print("  - Salir")
    print()
    print("Muestra un menu con opciones numeradas.")
    print("La lista se mantiene actualizada entre operaciones.")
    print()
    print("PISTA: Usa una lista vacia y un while True.")
    print("       append() agrega, remove() elimina.")
    print()
    print("Edita el archivo y escribe tu codigo:")
    print("# --- TU CODIGO AQUI ---")

def solucion_1():
    print("SOLUCION 1:")
    print()
    print("lista = []")
    print("while True:")
    print("    print('1. Agregar  2. Eliminar  3. Ver  0. Salir')")
    print("    op = input('Opcion: ')")
    print("    if op == '1':")
    print("        item = input('Item a agregar: ')")
    print("        lista.append(item)")
    print("        print(f'{item} agregado')")
    print("    elif op == '2':")
    print("        item = input('Item a eliminar: ')")
    print("        if item in lista:")
    print("            lista.remove(item)")
    print("            print(f'{item} eliminado')")
    print("        else:")
    print("            print('No encontrado')")
    print("    elif op == '3':")
    print("        if lista:")
    print("            for i, item in enumerate(lista, 1):")
    print("                print(f'{i}. {item}')")
    print("        else:")
    print("            print('Lista vacia')")
    print("    elif op == '0':")
    print("        break")
    print()
    print("Explicacion:")
    print("- append() agrega al final de la lista")
    print("- remove() elimina el primer elemento que coincida")
    print("- in verifica si un elemento existe en la lista")
    print("- enumerate() da indice y valor al iterar")

def ejercicio_2():
    print("=" * 50)
    print(">> EJERCICIO 2: Agenda telefonica")
    print("=" * 50)
    print()
    print("Crea una agenda que use un diccionario para guardar")
    print("contactos (nombre: telefono).")
    print()
    print("Funciones:")
    print("  - Agregar contacto (nombre y telefono)")
    print("  - Buscar contacto por nombre y mostrar su telefono")
    print("  - Listar todos los contactos")
    print("  - Salir")
    print()
    print("PISTA: agenda[nombre] = telefono para agregar.")
    print("       agenda.get(nombre) para buscar.")
    print()
    print("Edita el archivo y escribe tu codigo:")
    print("# --- TU CODIGO AQUI ---")

def solucion_2():
    print("SOLUCION 2:")
    print()
    print("agenda = {}")
    print("while True:")
    print("    print('1. Agregar  2. Buscar  3. Listar  0. Salir')")
    print("    op = input('Opcion: ')")
    print("    if op == '1':")
    print("        nombre = input('Nombre: ')")
    print("        telefono = input('Telefono: ')")
    print("        agenda[nombre] = telefono")
    print("        print('Contacto agregado')")
    print("    elif op == '2':")
    print("        nombre = input('Nombre a buscar: ')")
    print("        telefono = agenda.get(nombre)")
    print("        if telefono:")
    print("            print(f'{nombre}: {telefono}')")
    print("        else:")
    print("            print('Contacto no encontrado')")
    print("    elif op == '3':")
    print("        if agenda:")
    print("            for nombre, telefono in agenda.items():")
    print("                print(f'{nombre}: {telefono}')")
    print("        else:")
    print("            print('Agenda vacia')")
    print("    elif op == '0':")
    print("        break")
    print()
    print("Explicacion:")
    print("- agenda[nombre] = telefono agrega o actualiza")
    print("- get(nombre) devuelve el valor o None si no existe")
    print("- items() devuelve pares (clave, valor) para iterar")

def ejercicio_3():
    print("=" * 50)
    print(">> EJERCICIO 3: Numeros unicos")
    print("=" * 50)
    print()
    print("Pide al usuario 10 numeros enteros y guardalos en una lista.")
    print("Luego:")
    print("  - Muestra cuantos numeros son unicos (sin repetir)")
    print("    usando un set")
    print("  - Muestra los numeros unicos ordenados de menor a mayor")
    print("  - Usa una list comprehension para filtrar los numeros")
    print("    que son pares de la lista original")
    print()
    print("Ejemplo:")
    print("  Numeros: 3, 5, 3, 7, 5, 2, 8, 2, 9, 1")
    print("  Unicos: {1, 2, 3, 5, 7, 8, 9} (7 numeros)")
    print("  Pares: [2, 8, 2]")
    print()
    print("PISTA: set(lista) elimina duplicados.")
    print("       [x for x in lista if x % 2 == 0] filtra pares.")
    print()
    print("Edita el archivo y escribe tu codigo:")
    print("# --- TU CODIGO AQUI ---")

def solucion_3():
    print("SOLUCION 3:")
    print()
    print("numeros = []")
    print("for i in range(10):")
    print("    n = int(input(f'Numero {i+1}: '))")
    print("    numeros.append(n)")
    print("unicos = set(numeros)")
    print("print(f'Numeros unicos: {sorted(unicos)}')")
    print("print(f'Cantidad de unicos: {len(unicos)}')")
    print("pares = [x for x in numeros if x % 2 == 0]")
    print("print(f'Numeros pares: {pares}')")
    print()
    print("Explicacion:")
    print("- set(numeros) crea un conjunto sin duplicados")
    print("- sorted() ordena el set de menor a mayor")
    print("- len() cuenta cuantos elementos tiene el set")
    print("- [x for x in numeros if x % 2 == 0] es una list comprehension")
    print("  que filtra solo los numeros pares")

def menu():
    while True:
        print()
        print("=" * 50)
        print("MENU - Colecciones")
        print("=" * 50)
        print("1. Lista de compras")
        print("2. Agenda telefonica")
        print("3. Numeros unicos")
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
                "Lista vacia, while True, append(), remove(), 'in' para verificar existencia",
                "agenda = {}, agenda[nombre] = telefono, get() para buscar, items() para listar",
                "set(lista) elimina duplicados. sorted() ordena. List comprehension filtra"
            ]
            print(f"PISTA: {pistas[num - 1]}")
        else:
            [ejercicio_1, ejercicio_2, ejercicio_3][num - 1]()

if __name__ == "__main__":
    main()
