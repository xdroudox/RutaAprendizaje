"""
EJERCICIOS - Complejidad Algoritmica
Ejecuta desde raiz: python scripts/runner.py 3 1 [ejercicio]

Niveles:
  🟢 Ej 1: Identificar Big O de funciones (O(1), O(n), O(n^2))
  🟡 Ej 2: Ordenar notaciones por eficiencia
  🔴 Ej 3: Calcular complejidad de nested loops

Pistas: python scripts/runner.py 3 1 N -p [1|2|3]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1(pista=0):
    """🟢 Identificar Big O de funciones"""
    print(">> 🟢 EJERCICIO 1: Identificar Big O de funciones")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1:")
        print("  - arr[0]: acceder a una posicion especifica NO depende del tamano")
        print("  - for x in arr: cuantas veces se ejecuta el print?")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  - arr[0] = operacion constante (1 paso siempre)")
        print("  - arr[len(arr)//2] = sigue siendo constante (calculo + acceso)")
        print("  - Bucles anidados vs bucle simple: diferencia clave")
        return
    elif pista == 3:
        print("\n💡 Pista 3:")
        print("  - Acceso por indice: O(1)")
        print("  - Un bucle simple: O(n)")
        print("  - Dos bucles anidados: O(n^2)")
        return

    print("\nIdentifica la complejidad de cada caso:")
    print("  A) arr[0]")
    print("  B) for x in arr: print(x)")
    print("  C) for i in arr: for j in arr: print(i, j)")
    print("  D) arr[len(arr)//2]")
    print()
    print("Responde con: O(1), O(n), o O(n^2)")
    print()
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")


def ejercicio_2(pista=0):
    """🟡 Ordenar por eficiencia"""
    print(">> 🟡 EJERCICIO 2: Ordenar notaciones por eficiencia")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1:")
        print("  Piensa en n = 1,000,000:")
        print("  - O(1) = 1 operacion")
        print("  - O(log n) ≈ 20 operaciones")
        print("  - O(n) = 1,000,000 operaciones")
        print("  - O(n!) = imposible")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  De mas eficiente a menos eficiente:")
        print("  ? < ? < ? < ? < ? < ? < ?")
        print("  Hint: Constante < Logaritmico < Lineal")
        return
    elif pista == 3:
        print("\n💡 Pista 3:")
        print("  Orden correcto:")
        print("  1) O(1)")
        print("  2) O(log n)")
        print("  3) O(n)")
        print("  4) O(n log n)")
        print("  5) O(n^2)")
        print("  6) O(2^n)")
        print("  7) O(n!)")
        return

    print("\nOrdena de MENOR a MAYOR crecimiento:")
    print("  O(n!), O(1), O(n^2), O(n), O(log n), O(2^n), O(n log n)")
    print()
    print("Escribe la secuencia ordenada (ej: O(1) < O(n) < ...)")
    print()
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")


def ejercicio_3(pista=0):
    """🔴 Calcular complejidad de nested loops"""
    print(">> 🔴 EJERCICIO 3: Calcular complejidad de nested loops")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1:")
        print("  Fragmento A: for i in range(n): for j in range(n) -> n * n")
        print("  Fragmento B: for i in range(n): for j in range(i): el bucle")
        print("  interno NO llega a n siempre. Promedia n/2.")
        print("  Fragmento C: for i in range(n): for j in range(m): n * m")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  - n * n = n^2")
        print("  - n * (n/2) = n^2/2, ignoramos constantes → n^2")
        print("  - n * m no se puede simplificar (son distintas)")
        return
    elif pista == 3:
        print("\n💡 Pista 3:")
        print("  A) O(n^2)")
        print("  B) O(n^2)")
        print("  C) O(n*m)")
        return

    print("\nCalcula la complejidad para cada fragmento:")
    print()
    print("  # Fragmento A")
    print("  for i in range(n):")
    print("      for j in range(n):")
    print("          print(i, j)")
    print()
    print("  # Fragmento B")
    print("  for i in range(n):")
    print("      for j in range(i):")
    print("          print(i, j)")
    print()
    print("  # Fragmento C")
    print("  for i in range(n):")
    print("      for j in range(m):")
    print("          print(i, j)")
    print()
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")


if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            pista = 0
            if "-p" in sys.argv:
                idx = sys.argv.index("-p")
                if idx + 1 < len(sys.argv) and sys.argv[idx + 1].isdigit():
                    pista = int(sys.argv[idx + 1])
            ejercicios[num](pista)
    else:
        print("EJERCICIOS:")
        for i, ej in enumerate(ejercicios, 1):
            doc = ej.__doc__ or ""
            print(f"  {i}. {doc}")
