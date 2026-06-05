"""
EJERCICIOS - Operadores y Expresiones
Ejecuta: python ejercicios.py [numero] [-p]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    print("=" * 50)
    print(">> EJERCICIO 1: Calculadora de propinas")
    print("=" * 50)
    print()
    print("Pide al usuario el total de la cuenta y el porcentaje de propina.")
    print("Calcula y muestra:")
    print("  - Monto de la propina")
    print("  - Total a pagar (cuenta + propina)")
    print()
    print("Ejemplo:")
    print("  Total de cuenta: 100")
    print("  Porcentaje de propina: 15")
    print("  Propina: $15.0")
    print("  Total: $115.0")
    print()
    print("PISTA: Usa float() para convertir los inputs.")
    print("       propina = total * porcentaje / 100")
    print()
    print("Edita el archivo y escribe tu codigo:")
    print("# --- TU CODIGO AQUI ---")

def solucion_1():
    print("SOLUCION 1:")
    print()
    print("total = float(input('Total de la cuenta: '))")
    print("porcentaje = float(input('Porcentaje de propina: '))")
    print("propina = total * porcentaje / 100")
    print("total_pagar = total + propina")
    print("print(f'Propina: ${propina:.2f}')")
    print("print(f'Total a pagar: ${total_pagar:.2f}')")
    print()
    print("Explicacion:")
    print("- float() convierte el texto a numero decimal")
    print("- Calculamos propina como total * porcentaje / 100")
    print("- Sumamos al total original")
    print("- Usamos :.2f para mostrar 2 decimales")

def ejercicio_2():
    print("=" * 50)
    print(">> EJERCICIO 2: Comparador de numeros")
    print("=" * 50)
    print()
    print("Pide dos numeros al usuario y muestra:")
    print("  - Si son iguales o distintos")
    print("  - Cual es mayor (o si son iguales)")
    print("  - Si cada numero es par o impar (usa %)")
    print()
    print("Ejemplo:")
    print("  Numero 1: 7")
    print("  Numero 2: 4")
    print("  Son distintos")
    print("  7 es mayor que 4")
    print("  7 es impar")
    print("  4 es par")
    print()
    print("PISTA: Usa == para comparar, > para mayor,")
    print("       y % 2 == 0 para saber si es par.")
    print()
    print("Edita el archivo y escribe tu codigo:")
    print("# --- TU CODIGO AQUI ---")

def solucion_2():
    print("SOLUCION 2:")
    print()
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
    print()
    print("Explicacion:")
    print("- == compara igualdad, > compara mayor que")
    print("- % 2 == 0 verifica si un numero es par")
    print("- Los condicionales permiten mostrar mensajes diferentes")

def ejercicio_3():
    print("=" * 50)
    print(">> EJERCICIO 3: Sistema de acceso VIP")
    print("=" * 50)
    print()
    print("Pregunta al usuario:")
    print("  - Su edad")
    print("  - Si tiene boleto VIP (si/no)")
    print("  - Si esta en la lista de invitados (si/no)")
    print()
    print("Muestra:")
    print("  - ACCESO PERMITIDO si: edad >= 18 AND")
    print("    (tiene VIP OR esta en lista)")
    print("  - ACCESO DENEGADO en caso contrario")
    print("  - Mensaje extra si es menor de edad")
    print()
    print("PISTA: Convierte las respuestas si/no a booleanos.")
    print("       Usa and, or, not para combinar condiciones.")
    print()
    print("Edita el archivo y escribe tu codigo:")
    print("# --- TU CODIGO AQUI ---")

def solucion_3():
    print("SOLUCION 3:")
    print()
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
    print()
    print("Explicacion:")
    print("- .lower() normaliza la entrada a minusculas")
    print("- La condicion principal usa and y or combinados")
    print("- not invierte el valor booleano")

def menu():
    while True:
        print()
        print("=" * 50)
        print("MENU - Operadores y Expresiones")
        print("=" * 50)
        print("1. Calculadora de propinas")
        print("2. Comparador de numeros")
        print("3. Sistema de acceso VIP")
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
                "Usa float() para los inputs. propina = total * porcentaje / 100",
                "Usa == y > para comparar. n % 2 == 0 verifica si es par",
                "Convierte si/no a bool. Combina condiciones con and y or"
            ]
            print(f"PISTA: {pistas[num - 1]}")
        else:
            [ejercicio_1, ejercicio_2, ejercicio_3][num - 1]()

if __name__ == "__main__":
    main()
