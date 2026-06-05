"""
SOLUCIONES - Manejo de Strings
Ejecuta: python soluciones.py [numero]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    print("=" * 50)
    print("SOLUCION 1: Limpiador de texto")
    print("=" * 50)
    print()
    print("Codigo:")
    print("```python")
    print("frase = input('Escribe una frase: ')")
    print("frase_limpia = frase.strip().capitalize()")
    print("print(f'Frase limpia: {frase_limpia}')")
    print("```")
    print()
    print("Explicacion:")
    print("- strip() elimina espacios en blanco al inicio y final")
    print("- capitalize() convierte el primer caracter a mayuscula")
    print("  y el resto a minuscula automaticamente")
    print("- Los metodos se pueden encadenar: objeto.metodo1().metodo2()")

def solucion_2():
    print("=" * 50)
    print("SOLUCION 2: Analizador de oraciones")
    print("=" * 50)
    print()
    print("Codigo:")
    print("```python")
    print("oracion = input('Escribe una oracion: ')")
    print("palabras = oracion.split()")
    print("print(f'Numero de palabras: {len(palabras)}')")
    print("mayusculas = [p.upper() for p in palabras]")
    print("print(f'En mayusculas: {\", \".join(mayusculas)}')")
    print("print(f'Con guiones: {\"-\".join(palabras)}')")
    print("```")
    print()
    print("Explicacion:")
    print("- split() sin argumentos divide por espacios en blanco")
    print("- len() cuenta cuantos elementos tiene la lista")
    print("- upper() convierte cada palabra a mayusculas")
    print("- ', '.join() une con coma y espacio")
    print("- '-'.join() une con guion")

def solucion_3():
    print("=" * 50)
    print("SOLUCION 3: Formateador de factura")
    print("=" * 50)
    print()
    print("Codigo:")
    print("```python")
    print("producto = input('Nombre del producto: ')")
    print("cantidad = int(input('Cantidad: '))")
    print("precio = float(input('Precio unitario: '))")
    print("subtotal = cantidad * precio")
    print("print(f'{\"Producto\":<12} {\"Cantidad\":<10} {\"Precio\":<10} {\"Subtotal\":<10}')")
    print("print('-' * 42)")
    print("print(f'{producto:<12} {cantidad:<10} ${precio:<7.2f} ${subtotal:<7.2f}')")
    print("print('-' * 42)")
    print("print(f'{\"TOTAL:\":<22} ${subtotal:.2f}')")
    print("```")
    print()
    print("Explicacion:")
    print("- f'{variable:<12}' alinea el contenido a la izquierda en 12 caracteres")
    print("- {:<7.2f} alinea un numero con 2 decimales en 7 espacios")
    print("- Los literales como 'Producto' se escapan con llaves dobles")
    print("- Las lineas de guiones separan encabezados, datos y total")

def menu():
    while True:
        print()
        print("=" * 50)
        print("SOLUCIONES - Manejo de Strings")
        print("=" * 50)
        print("1. Limpiador de texto")
        print("2. Analizador de oraciones")
        print("3. Formateador de factura")
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
