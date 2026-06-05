"""
🔍 SOLUCIONES - Lógica de Programación
Ejecuta: python soluciones.py [número]

Uso:
  python soluciones.py    → Menú de soluciones
  python soluciones.py 1  → Solución del ejercicio 1
"""

import sys

def solucion_1():
    print("=" * 50)
    print("🔍 SOLUCIÓN - Ejercicio 1: Tu primer algoritmo")
    print("=" * 50)
    print()
    print("📝 Algoritmo para preparar un sándwich:")
    print()
    print("```python")
    print("# ALGORITMO: Preparar un sándwich 🥪")
    print('print("🧑‍🍳 Vamos a preparar un sándwich!")')
    print('print()')
    print("# Paso 1: Conseguir ingredientes")
    print('print("1. Abro la nevera...")')
    print('print("   - Pan 🍞")')
    print('print("   - Jamón 🥩")')
    print('print("   - Queso 🧀")')
    print('print("   - Lechuga 🥬")')
    print('print()')
    print("# Paso 2: Preparar la base")
    print('print("2. Pongo dos rebanadas de pan en el plato")')
    print('print()')
    print("# Paso 3: Armar el sándwich")
    print('print("3. Agrego jamón sobre el pan")')
    print('print("4. Agrego queso sobre el jamón")')
    print('print("5. Agrego lechuga sobre el queso")')
    print('print()')
    print("# Paso 4: Cerrar")
    print('print("6. Pongo la otra rebanada de pan encima")')
    print('print()')
    print("# Paso 5: Disfrutar")
    print('print("7. ¡A comer! 🥪✨")')
    print("```")
    print()
    print("📖 Explicación:")
    print("Cada acción del mundo real se convierte en una instrucción")
    print("de Python (print()). La secuencia ordenada de pasos es")
    print("exactamente eso: un ALGORITMO.")

def solucion_2():
    print("=" * 50)
    print("🔍 SOLUCIÓN - Ejercicio 2: Algoritmo del cajero")
    print("=" * 50)
    print()
    print("```python")
    print('monto = int(input("Ingresa el monto a retirar: "))')
    print("original = monto")
    print()
    print("billete_1000 = monto // 1000")
    print("monto = monto % 1000")
    print("billete_500 = monto // 500")
    print("monto = monto % 500")
    print("billete_200 = monto // 200")
    print("monto = monto % 200")
    print("billete_100 = monto // 100")
    print("monto = monto % 100")
    print("billete_50 = monto // 50")
    print()
    print('print(f"Para ${original} necesitas:")')
    print('print(f"  {billete_1000} billetes de $1000")')
    print('print(f"  {billete_500} billetes de $500")')
    print('print(f"  {billete_200} billetes de $200")')
    print('print(f"  {billete_100} billetes de $100")')
    print('print(f"  {billete_50} billetes de $50")')
    print("```")
    print()
    print("📖 Explicación:")
    print("Este es un algoritmo GREEDY (avaro): siempre usa la")
    print("denominación más grande posible primero. // da el")
    print("número de billetes, % da el residuo para continuar.")

def solucion_3():
    print("=" * 50)
    print("🔍 SOLUCIÓN - Ejercicio 3: Número par o impar")
    print("=" * 50)
    print()
    print("```python")
    print('numero = int(input("Ingresa un número entero: "))')
    print()
    print("if numero % 2 == 0:")
    print('    print(f"El número {numero} es PAR ✅")')
    print("else:")
    print('    print(f"El número {numero} es IMPAR ❌")')
    print("```")
    print()
    print("📖 Explicación:")
    print("El operador % (módulo) devuelve el RESTO de una división.")
    print("Si número % 2 == 0 → el número es divisible por 2 → es PAR.")
    print("Si número % 2 == 1 → NO es divisible por 2 → es IMPAR.")
    print()
    print("💡 Dato curioso: Esta es una de las operaciones más")
    print("usadas en programación. La verás en todos lados!")

def menu():
    while True:
        print()
        print("=" * 50)
        print("📋 SOLUCIONES - Lógica de Programación")
        print("=" * 50)
        print("1. Tu primer algoritmo")
        print("2. Algoritmo del cajero")
        print("3. Número par o impar")
        print("0. Salir")
        print()

        opcion = input("➜ Ver solución: ")

        soluciones = {"1": solucion_1, "2": solucion_2, "3": solucion_3}

        if opcion in soluciones:
            soluciones[opcion]()
            input("\nPresiona ENTER para continuar...")
        elif opcion == "0":
            print("👋 ¡Sigue así!")
            break
        else:
            print("❌ Opción inválida")

def main():
    args = sys.argv[1:]
    if args and args[0].isdigit():
        [solucion_1, solucion_2, solucion_3][int(args[0]) - 1]()
    else:
        menu()

if __name__ == "__main__":
    main()
