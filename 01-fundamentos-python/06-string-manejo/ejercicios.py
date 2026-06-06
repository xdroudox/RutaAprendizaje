"""
EJERCICIOS - Manejo de Strings
Ejecuta desde raiz: python scripts/runner.py 1 6 [ejercicio]

Niveles:
  🟢 Ej 1: Mayusculas y minusculas (upper(), lower())
  🟡 Ej 2: Invertir palabra con slicing [::-1] y palindromo
  🔴 Ej 3: Contar vocales en una frase con for

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
    """🟢 Mayusculas y minusculas: pedir nombre y mostrar en ambos formatos"""
    if pista == 1:
        print("💡 Pista 1: Pide el nombre con input()")
        return
    elif pista == 2:
        print("💡 Pista 2: Usa upper() y lower() sobre el nombre:")
        print("  print(f'Mayusculas: {nombre.upper()}')")
        return
    elif pista == 3:
        print("💡 Pista 3: Estructura completa:")
        print("  nombre = input('Tu nombre: ')")
        print("  print(f'Mayusculas: {nombre.upper()}')")
        print("  print(f'Minusculas: {nombre.lower()}')")
        return

    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass


def ejercicio_2(pista=0):
    """🟡 Invertir palabra: pedir palabra, mostrarla invertida y verificar si es palindromo"""
    if pista == 1:
        print("💡 Pista 1: Para invertir: palabra[::-1]")
        print("  invertida = palabra[::-1]")
        return
    elif pista == 2:
        print("💡 Pista 2: Palindromo = se lee igual al derecho y al reves:")
        print("  if palabra == invertida: es palindromo")
        return
    elif pista == 3:
        print("💡 Pista 3: Estructura completa:")
        print("  palabra = input('Ingresa una palabra: ')")
        print("  invertida = palabra[::-1]")
        print("  print(f'Invertida: {invertida}')")
        print("  if palabra == invertida:")
        print("      print('Es palindromo!')")
        print("  else:")
        print("      print('No es palindromo')")
        return

    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass


def ejercicio_3(pista=0):
    """🔴 Contar vocales: pedir frase, contar a, e, i, o, u con for"""
    if pista == 1:
        print("💡 Pista 1: Convierte la frase a minusculas con .lower()")
        print("  Asi 'A' y 'a' cuentan como la misma vocal")
        return
    elif pista == 2:
        print("💡 Pista 2: Recorre cada letra con for:")
        print("  for letra in frase:")
        print("      if letra in 'aeiou':")
        print("          conteo += 1")
        return
    elif pista == 3:
        print("💡 Pista 3: Estructura completa:")
        print("  frase = input('Frase: ').lower()")
        print("  vocales = 'aeiou'")
        print("  conteo = 0")
        print("  for letra in frase:")
        print("      if letra in vocales:")
        print("          conteo += 1")
        print("  print(f'Vocales: {conteo}')")
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
        print("Ejecuta: python scripts/runner.py 1 6 [N]")
        print("Pistas:  python scripts/runner.py 1 6 N -p [1|2|3]")
