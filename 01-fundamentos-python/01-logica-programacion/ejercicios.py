"""
EJERCICIOS - Logica de Programacion
Ejecuta: python ejercicios.py [numero] [-p]

Uso:
  python ejercicios.py      -> Menu interactivo
  python ejercicios.py 1    -> Ejercicio 1
  python ejercicios.py 1 -p -> Pista para ejercicio 1
  python ejercicios.py -s 1 -> Solucion del ejercicio 1
"""

import sys

# Forzar UTF-8 en Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# ============================================
# EJERCICIO 1: Tu primer algoritmo
# ============================================
def ejercicio_1():
    print("=" * 50)
    print(">> EJERCICIO 1: Tu primer algoritmo")
    print("=" * 50)
    print()
    print("Crea un algoritmo (en espanol) para preparar un sandwich,")
    print("luego traducelo a codigo Python.")
    print()
    print("Instrucciones:")
    print("  1. Escribe los pasos como comentarios (#)")
    print("  2. Traduce cada paso a codigo Python")
    print("  3. Usa print() para mostrar cada accion")
    print()
    print("PISTA: Usa print() para describir cada paso")
    print()
    print("Edita este archivo y completa la funcion:")
    print("# --- TU CODIGO AQUI ---")

def solucion_1():
    print("🔍 SOLUCIÓN - Ejercicio 1")
    print()
    print("```python")
    print("# ALGORITMO: Preparar un sándwich")
    print("# 1. Conseguir ingredientes")
    print('print("1. Abro la nevera y saco: pan, jamón, queso, lechuga")')
    print("# 2. Preparar la base")
    print('print("2. Pongo dos rebanadas de pan en el plato")')
    print("# 3. Agregar ingredientes")
    print('print("3. Agrego jamón, queso y lechuga")')
    print("# 4. Cerrar el sándwich")
    print('print("4. Pongo la otra rebanada de pan encima")')
    print("# 5. Disfrutar")
    print('print("5. ¡A comer! 🥪")')
    print("```")
    print()
    print("📖 Explicación:")
    print("Cada paso del algoritmo se traduce a un print().")
    print("Los comentarios (#) documentan qué hace cada parte.")

# ============================================
# EJERCICIO 2: Algoritmo del cajero
# ============================================
def ejercicio_2():
    print("=" * 50)
    print("🎯 EJERCICIO 2: El algoritmo del cajero")
    print("=" * 50)
    print()
    print("Crea un algoritmo que calcule cuántos billetes de cada")
    print("denominación (1000, 500, 200, 100, 50) necesita un cajero")
    print("automático para dar un vuelto.")
    print()
    print("Ejemplo: 2750 → 2 de 1000, 1 de 500, 1 de 200, 0 de 100, 1 de 50")
    print()
    print("💡 PISTA: Usa división entera (//) y módulo (%)")
    print()
    print("✏️  Edita el archivo y escribe tu código:")
    print("# --- TU CÓDIGO AQUÍ ---")

def solucion_2():
    print("🔍 SOLUCIÓN - Ejercicio 2")
    print()
    print("```python")
    print("monto = 2750")
    print("billete_1000 = monto // 1000")
    print("monto = monto % 1000")
    print("billete_500 = monto // 500")
    print("monto = monto % 500")
    print("billete_200 = monto // 200")
    print("monto = monto % 200")
    print("billete_100 = monto // 100")
    print("monto = monto % 100")
    print("billete_50 = monto // 50")
    print('print(f"{billete_1000} de 1000, {billete_500} de 500,", end=" ")')
    print('print(f"{billete_200} de 200, {billete_100} de 100, {billete_50} de 50")')
    print("```")
    print()
    print("📖 Explicación:")
    print("// divide y devuelve la parte entera (cuántos billetes)")
    print("% devuelve el residuo (lo que falta por repartir)")
    print("Así sucesivamente hasta agotar el monto.")

# ============================================
# EJERCICIO 3: Número par o impar
# ============================================
def ejercicio_3():
    print("=" * 50)
    print("🎯 EJERCICIO 3: Número par o impar")
    print("=" * 50)
    print()
    print("Pide al usuario un número entero y determina si es par o impar.")
    print()
    print("💡 PISTA: Un número es par si n % 2 == 0")
    print()
    print("✏️  Edita el archivo y completa la función:")
    print("# --- TU CÓDIGO AQUÍ ---")

def solucion_3():
    print("🔍 SOLUCIÓN - Ejercicio 3")
    print()
    print("```python")
    print('numero = int(input("Ingresa un número: "))')
    print("if numero % 2 == 0:")
    print('    print(f"{numero} es PAR")')
    print("else:")
    print('    print(f"{numero} es IMPAR")')
    print("```")
    print()
    print("📖 Explicación:")
    print("El operador % devuelve el resto de la división.")
    print("Si al dividir por 2 el resto es 0, el número es par.")

# ============================================
# MENÚ PRINCIPAL
# ============================================
def menu():
    while True:
        print()
        print("=" * 50)
        print("📋 MENÚ - Lógica de Programación")
        print("=" * 50)
        print("1. Tu primer algoritmo")
        print("2. Algoritmo del cajero")
        print("3. Número par o impar")
        print("0. Salir")
        print()

        opcion = input("➜ Selecciona un ejercicio: ")

        if opcion == "1":
            ejercicio_1()
            input("\nPresiona ENTER para continuar...")
        elif opcion == "2":
            ejercicio_2()
            input("\nPresiona ENTER para continuar...")
        elif opcion == "3":
            ejercicio_3()
            input("\nPresiona ENTER para continuar...")
        elif opcion == "0":
            print("👋 ¡Sigue practicando!")
            break
        else:
            print("❌ Opción inválida")

def main():
    args = sys.argv[1:]

    if not args:
        menu()
        return

    if "-s" in args:
        idx = args.index("-s")
        if idx + 1 < len(args) and args[idx + 1].isdigit():
            num = int(args[idx + 1])
            [solucion_1, solucion_2, solucion_3][num - 1]()
        return

    if args[0].isdigit():
        num = int(args[0])
        if "-p" in args:
            pistas = [
                "Usa print() para cada paso del sándwich",
                "Usa // para división entera y % para el residuo",
                "Un número par: n % 2 == 0"
            ]
            print(f"💡 PISTA: {pistas[num - 1]}")
        else:
            [ejercicio_1, ejercicio_2, ejercicio_3][num - 1]()

if __name__ == "__main__":
    main()
