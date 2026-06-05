"""
SOLUCIONES - Colecciones
Ejecuta: python soluciones.py [numero]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    print("=" * 50)
    print("SOLUCION 1: Lista de compras")
    print("=" * 50)
    print()
    print("Codigo:")
    print("```python")
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
    print("```")
    print()
    print("Explicacion:")
    print("- append() agrega elementos al final de la lista")
    print("- remove() elimina la primera ocurrencia del elemento")
    print("- 'in' verifica si un elemento pertenece a la lista")
    print("- enumerate() da el indice (empezando en 1) y el valor")

def solucion_2():
    print("=" * 50)
    print("SOLUCION 2: Agenda telefonica")
    print("=" * 50)
    print()
    print("Codigo:")
    print("```python")
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
    print("```")
    print()
    print("Explicacion:")
    print("- Los diccionarios guardan pares clave:valor")
    print("- agenda[nombre] = telefono agrega o actualiza")
    print("- get() busca sin lanzar error si no existe (devuelve None)")
    print("- items() permite iterar sobre todas las entradas")

def solucion_3():
    print("=" * 50)
    print("SOLUCION 3: Numeros unicos")
    print("=" * 50)
    print()
    print("Codigo:")
    print("```python")
    print("numeros = []")
    print("for i in range(10):")
    print("    n = int(input(f'Numero {i+1}: '))")
    print("    numeros.append(n)")
    print("unicos = set(numeros)")
    print("print(f'Numeros unicos: {sorted(unicos)}')")
    print("print(f'Cantidad de unicos: {len(unicos)}')")
    print("pares = [x for x in numeros if x % 2 == 0]")
    print("print(f'Numeros pares: {pares}')")
    print("```")
    print()
    print("Explicacion:")
    print("- set(numeros) elimina automaticamente los duplicados")
    print("- sorted() ordena el conjunto de menor a mayor")
    print("- len() cuenta los elementos del set")
    print("- La list comprehension [x for x in numeros if x % 2 == 0]")
    print("  crea una nueva lista solo con los pares")

def menu():
    while True:
        print()
        print("=" * 50)
        print("SOLUCIONES - Colecciones")
        print("=" * 50)
        print("1. Lista de compras")
        print("2. Agenda telefonica")
        print("3. Numeros unicos")
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
