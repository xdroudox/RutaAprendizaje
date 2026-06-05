"""
SOLUCIONES - Operadores y Expresiones
Ejecuta: python soluciones.py [numero]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    print("=" * 50)
    print("SOLUCION 1: Calculadora de propinas")
    print("=" * 50)
    print()
    print("Codigo:")
    print("```python")
    print("total = float(input('Total de la cuenta: '))")
    print("porcentaje = float(input('Porcentaje de propina: '))")
    print("propina = total * porcentaje / 100")
    print("total_pagar = total + propina")
    print("print(f'Propina: ${propina:.2f}')")
    print("print(f'Total a pagar: ${total_pagar:.2f}')")
    print("```")
    print()
    print("Explicacion:")
    print("- float() convierte la entrada del usuario a numero decimal")
    print("- La formula propina = total * porcentaje / 100 usa multiplicacion y division")
    print("- Sumamos la propina al total original con +")
    print("- {:.2f} en f-strings formatea el numero con 2 decimales")

def solucion_2():
    print("=" * 50)
    print("SOLUCION 2: Comparador de numeros")
    print("=" * 50)
    print()
    print("Codigo:")
    print("```python")
    print("num1 = int(input('Numero 1: '))")
    print("num2 = int(input('Numero 2: '))")
    print("if num1 == num2:")
    print("    print('Son iguales')")
    print("else:")
    print("    print('Son distintos')")
    print("    if num1 > num2:")
    print("        print(f'{num1} es mayor que {num2}')")
    print("    else:")
    print("        print(f'{num2} es mayor que {num1}')")
    print("if num1 % 2 == 0:")
    print("    print(f'{num1} es par')")
    print("else:")
    print("    print(f'{num1} es impar')")
    print("if num2 % 2 == 0:")
    print("    print(f'{num2} es par')")
    print("else:")
    print("    print(f'{num2} es impar')")
    print("```")
    print()
    print("Explicacion:")
    print("- == compara si dos valores son iguales")
    print("- > compara si un valor es mayor que otro")
    print("- El operador % da el resto de la division")
    print("- Si n % 2 == 0, el numero es par (divisible entre 2)")

def solucion_3():
    print("=" * 50)
    print("SOLUCION 3: Sistema de acceso VIP")
    print("=" * 50)
    print()
    print("Codigo:")
    print("```python")
    print("edad = int(input('Edad: '))")
    print("vip = input('Tiene boleto VIP? (si/no): ').lower() == 'si'")
    print("lista = input('Esta en la lista de invitados? (si/no): ').lower() == 'si'")
    print("if edad >= 18 and (vip or lista):")
    print("    print('ACCESO PERMITIDO')")
    print("elif edad < 18:")
    print("    print('ACCESO DENEGADO - Eres menor de edad')")
    print("else:")
    print("    print('ACCESO DENEGADO')")
    print("if not vip and not lista:")
    print("    print('Necesitas boleto VIP o estar en la lista')")
    print("```")
    print()
    print("Explicacion:")
    print("- .lower() convierte la entrada a minusculas para comparar facil")
    print("- Operadores logicos combinados: edad >= 18 AND (vip OR lista)")
    print("- not invierte el valor booleano (True -> False, False -> True)")
    print("- Los parentesis cambian la precedencia: (vip or lista) se evalua primero")

def menu():
    while True:
        print()
        print("=" * 50)
        print("SOLUCIONES - Operadores y Expresiones")
        print("=" * 50)
        print("1. Calculadora de propinas")
        print("2. Comparador de numeros")
        print("3. Sistema de acceso VIP")
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
