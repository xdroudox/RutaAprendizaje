"""
EJERCICIOS - Manejo de Strings
Ejecuta: python ejercicios.py [numero] [-p]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    print("=" * 50)
    print(">> EJERCICIO 1: Limpiador de texto")
    print("=" * 50)
    print()
    print("Pide al usuario una frase con espacios extras y")
    print("mayusculas/minusculas irregulares.")
    print()
    print("Limpiala aplicando:")
    print("  - Quitar espacios al inicio y final (strip)")
    print("  - Primera letra en mayuscula (capitalize)")
    print("  - El resto en minusculas")
    print()
    print("Ejemplo:")
    print("  '  hOLa MUNdo ' -> 'Hola mundo'")
    print()
    print("PISTA: strip() quita espacios, capitalize() pone la")
    print("       primera en mayuscula y el resto en minuscula.")
    print()
    print("Edita el archivo y escribe tu codigo:")
    print("# --- TU CODIGO AQUI ---")

def solucion_1():
    print("SOLUCION 1:")
    print()
    print("frase = input('Escribe una frase: ')")
    print("frase_limpia = frase.strip().capitalize()")
    print("print(f'Frase limpia: {frase_limpia}')")
    print()
    print("Explicacion:")
    print("- strip() elimina espacios al inicio y final")
    print("- capitalize() pone la primera letra mayuscula")
    print("  y el resto minusculas automaticamente")
    print("- Los metodos se pueden encadenar: .strip().capitalize()")

def ejercicio_2():
    print("=" * 50)
    print(">> EJERCICIO 2: Analizador de oraciones")
    print("=" * 50)
    print()
    print("Pide al usuario una oracion y muestra:")
    print("  - Numero de palabras en la oracion")
    print("  - Cada palabra en mayusculas (separadas por comas)")
    print("  - La oracion original con guiones en vez de espacios")
    print()
    print("Ejemplo:")
    print("  'Hola mundo desde Python'")
    print("  Palabras: 4")
    print("  En mayusculas: HOLA, MUNDO, DESDE, PYTHON")
    print("  Con guiones: Hola-mundo-desde-Python")
    print()
    print("PISTA: split() divide en palabras, upper() para mayusculas,")
    print("       join() une con guiones, replace() tambien funciona.")
    print()
    print("Edita el archivo y escribe tu codigo:")
    print("# --- TU CODIGO AQUI ---")

def solucion_2():
    print("SOLUCION 2:")
    print()
    print("oracion = input('Escribe una oracion: ')")
    print("palabras = oracion.split()")
    print("print(f'Numero de palabras: {len(palabras)}')")
    print("mayusculas = [p.upper() for p in palabras]")
    print("print(f'En mayusculas: {\", \".join(mayusculas)}')")
    print("print(f'Con guiones: {\"-\".join(palabras)}')")
    print()
    print("Explicacion:")
    print("- split() separa la oracion en palabras (por espacios)")
    print("- len() da la cantidad de palabras")
    print("- upper() convierte cada palabra a mayusculas")
    print("- join() une los elementos con el separador indicado")

def ejercicio_3():
    print("=" * 50)
    print(">> EJERCICIO 3: Formateador de factura")
    print("=" * 50)
    print()
    print("Pide al usuario:")
    print("  - Nombre del producto")
    print("  - Cantidad")
    print("  - Precio unitario")
    print()
    print("Muestra una factura formateada usando f-strings:")
    print("  Producto    Cantidad    Precio     Subtotal")
    print("  -----------------------------------------")
    print("  [nombre]    [cant]      [$precio]  [$total]")
    print("  -----------------------------------------")
    print("  TOTAL: $[suma]")
    print()
    print("Usa alineacion (< izquierda, > derecha) y 2 decimales.")
    print()
    print("PISTA: f'{variable:<10}' alinea a la izquierda en 10 espacios.")
    print("       f'{variable:.2f}' muestra 2 decimales.")
    print()
    print("Edita el archivo y escribe tu codigo:")
    print("# --- TU CODIGO AQUI ---")

def solucion_3():
    print("SOLUCION 3:")
    print()
    print("producto = input('Nombre del producto: ')")
    print("cantidad = int(input('Cantidad: '))")
    print("precio = float(input('Precio unitario: '))")
    print("subtotal = cantidad * precio")
    print("print(f'{\"Producto\":<12} {\"Cantidad\":<10} {\"Precio\":<10} {\"Subtotal\":<10}')")
    print("print('-' * 42)")
    print("print(f'{producto:<12} {cantidad:<10} ${precio:<7.2f} ${subtotal:<7.2f}')")
    print("print('-' * 42)")
    print("print(f'{\"TOTAL:\":<22} ${subtotal:.2f}')")
    print()
    print("Explicacion:")
    print("- f'{texto:<12}' alinea el texto a la izquierda en 12 espacios")
    print("- :.2f muestra el numero con 2 decimales")
    print("- Los encabezados se alinean para que coincidan con los datos")
    print("- Las lineas de guiones separan visualmente las secciones")

def menu():
    while True:
        print()
        print("=" * 50)
        print("MENU - Manejo de Strings")
        print("=" * 50)
        print("1. Limpiador de texto")
        print("2. Analizador de oraciones")
        print("3. Formateador de factura")
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
                "strip() quita espacios. capitalize() pone mayuscula inicial",
                "split() divide, upper() mayusculas, join() une con separador",
                "Usa f-strings con :<10 para alinear y :.2f para decimales"
            ]
            print(f"PISTA: {pistas[num - 1]}")
        else:
            [ejercicio_1, ejercicio_2, ejercicio_3][num - 1]()

if __name__ == "__main__":
    main()
