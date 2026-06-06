"""
EJERCICIOS - Funciones
Ejecuta desde raiz: python scripts/runner.py 1 5 [ejercicio]

Niveles:
  🟢 Ej 1: Funcion suma (def + return basico)
  🟡 Ej 2: Funcion promedio (funcion con lista)
  🔴 Ej 3: Filtrar pares con lambda (filter + lambda)

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
    """🟢 Funcion suma: crear funcion que reciba 2 numeros y devuelva su suma"""
    if pista == 1:
        print("💡 Pista 1: Define la funcion con def:")
        print("  def sumar(a, b):")
        print("      return a + b")
        return
    elif pista == 2:
        print("💡 Pista 2: Despues de definir la funcion, pide los numeros:")
        print("  num1 = float(input('Primer numero: '))")
        print("  num2 = float(input('Segundo numero: '))")
        return
    elif pista == 3:
        print("💡 Pista 3: Llama a la funcion y muestra:")
        print("  resultado = sumar(num1, num2)")
        print("  print(f'La suma es: {resultado}')")
        return

    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass


def ejercicio_2(pista=0):
    """🟡 Funcion promedio: funcion que recibe una lista y devuelve el promedio"""
    if pista == 1:
        print("💡 Pista 1: La funcion recibe una lista:")
        print("  def promedio(lista):")
        print("      return sum(lista) / len(lista)")
        return
    elif pista == 2:
        print("💡 Pista 2: Fuera de la funcion, crea una lista:")
        print("  numeros = [10, 20, 30, 40, 50]")
        return
    elif pista == 3:
        print("💡 Pista 3: Llama a la funcion:")
        print("  resultado = promedio(numeros)")
        print("  print(f'El promedio es: {resultado}')")
        return

    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass


def ejercicio_3(pista=0):
    """🔴 Filtrar pares con lambda: filter() + lambda para obtener solo pares"""
    if pista == 1:
        print("💡 Pista 1: Crea una lista de numeros:")
        print("  numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
        return
    elif pista == 2:
        print("💡 Pista 2: filter() recibe una funcion y un iterable:")
        print("  pares = list(filter(lambda x: x % 2 == 0, numeros))")
        return
    elif pista == 3:
        print("💡 Pista 3: Codigo completo:")
        print("  numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
        print("  pares = list(filter(lambda x: x % 2 == 0, numeros))")
        print("  print(f'Pares: {pares}')")
        return

    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass


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
        print("Ejecuta: python scripts/runner.py 1 5 [N]")
        print("Pistas:  python scripts/runner.py 1 5 N -p [1|2|3]")
