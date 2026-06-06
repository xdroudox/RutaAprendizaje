"""
EJERCICIOS - Logica de Programacion
Ejecuta desde raiz: python scripts/runner.py 1 1 [ejercicio]

Niveles:
  🟢 Ej 1: Preparar un sandwich (secuencia de pasos con print)
  🟡 Ej 2: Par o impar (input + if/else + %)
  🔴 Ej 3: Mayor de 3 numeros (comparaciones sin max())

Pistas:
  python ejercicios.py N -p 1
  python ejercicios.py N -p 2
  python ejercicios.py N -p 3
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1(pista=0):
    """🟢 Preparar un sandwich: muestra los pasos con print(), uno por linea"""
    if pista == 1:
        print("💡 Pista 1: Cada paso es un print() diferente")
        print("  Ej: print('1. Abrir la nevera')")
        return
    elif pista == 2:
        print("💡 Pista 2: Necesitas al menos 4-5 pasos logicos")
        print("  1. Abrir la nevera")
        print("  2. Sacar ingredientes")
        print("  3. Armar el sandwich")
        print("  4. Servir")
        return
    elif pista == 3:
        print("💡 Pista 3: Usa print() para cada paso:")
        print("  print('1. ...')")
        print("  print('2. ...')")
        return

    # ==== ESCRIBE TU RESPUESTA AQUI ====
    print("  1. Abrir la nevera")
    print("  2. Sacar ingredientes")
    print("  3. Armar el sandwich")
    print("  4. Servir")


def ejercicio_2(pista=0):
    """🟡 Par o impar: pide un numero y muestra si es par o impar usando %"""
    if pista == 1:
        print("💡 Pista 1: Usa input() para pedir el numero e int() para convertirlo")
        print("  El operador % da el RESTO de una division")
        return
    elif pista == 2:
        print("💡 Pista 2: Si numero % 2 == 0, es PAR. Si no, es IMPAR.")
        print("  Usa if/else para mostrar el resultado")
        return
    elif pista == 3:
        print("💡 Pista 3: Estructura:")
        print("  num = int(input('Ingresa un numero: '))")
        print("  if num % 2 == 0:")
        print("      print('PAR')")
        print("  else:")
        print("      print('IMPAR')")
        return

    # ==== ESCRIBE TU RESPUESTA AQUI ====
    numero = int(input("Ingrese un numero: "))
    resultado = lambda x: "Par" if x % 2 == 0 else "Impar"
    print(f"El numero {numero} es ({resultado(numero)}) ")


def ejercicio_3(pista=0):
    """🔴 Mayor de 3 numeros: pide 3 numeros y muestra el mayor sin usar max()"""
    if pista == 1:
        print("💡 Pista 1: Pide los 3 numeros con input() y guardalos en a, b, c")
        return
    elif pista == 2:
        print("💡 Pista 2: Compara cada numero con los otros dos:")
        print("  if a >= b and a >= c: a es el mayor")
        print("  elif b >= a and b >= c: b es el mayor")
        print("  else: c es el mayor")
        return
    elif pista == 3:
        print("💡 Pista 3: Estructura completa:")
        print("  a = int(input('Num 1: '))")
        print("  b = int(input('Num 2: '))")
        print("  c = int(input('Num 3: '))")
        print("  if a >= b and a >= c:")
        print("      print(f'El mayor es {a}')")
        return

    # ==== ESCRIBE TU RESPUESTA AQUI ====
    num = []
    mayor = num[0]
    for i in range(3):
        numero = int(input("Ingrese un numero: "))
        num.append(numero)
    for n in num:
        if n > mayor:
            mayor = n
    print(f"Numero mayor ( {mayor} )")

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]

    # Parsear argumentos de forma segura
    pista = 0
    args = []
    i = 1
    while i < len(sys.argv):
        a = sys.argv[i]
        if a == "-s":
            i += 1
            continue
        if a == "-p":
            if i + 1 < len(sys.argv) and sys.argv[i + 1].isdigit():
                pista = int(sys.argv[i + 1])
            i += 2
            continue
        args.append(a)
        i += 1

    if len(args) > 0 and args[0].isdigit():
        num = int(args[0]) - 1
        if 0 <= num < len(ejercicios):
            niveles = ["🟢", "🟡", "🔴"]
            print(f">> {niveles[num]} EJERCICIO {num + 1}: {ejercicios[num].__doc__.strip()}")
            print("-" * 50)
            ejercicios[num](pista=pista)
        else:
            print(f"Ejercicio no encontrado. Valores: 1-{len(ejercicios)}")
    else:
        print("EJERCICIOS:")
        niveles = ["🟢", "🟡", "🔴"]
        for i, ej in enumerate(ejercicios, 1):
            doc = ej.__doc__.strip().split("\n")[0] if ej.__doc__ else "Sin descripcion"
            print(f"  {niveles[i-1]} {i}. {doc}")
        print()
        print("Ejecuta: python scripts/runner.py 1 1 [N]")
        print("Pistas:  python scripts/runner.py 1 1 N -p [1|2|3]")
