"""
EJERCICIOS - Operadores y Expresiones
Ejecuta desde raiz: python scripts/runner.py 1 3 [ejercicio]

Niveles:
  🟢 Ej 1: Calculadora de propina (operadores aritmeticos)
  🟡 Ej 2: Ano bisiesto (and, or, %, combinacion de condiciones)
  🔴 Ej 3: Verificar triangulo (comparaciones multiples con and)

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
    """🟢 Calculadora de propina: pide total y %, muestra propina y total a pagar"""
    if pista == 1:
        print("💡 Pista 1: Usa float() para el total (puede tener decimales)")
        print("  total = float(input('Total de la cuenta: '))")
        return
    elif pista == 2:
        print("💡 Pista 2: Formulas:")
        print("  propina = total * porcentaje / 100")
        print("  total_pagar = total + propina")
        return
    elif pista == 3:
        print("💡 Pista 3: Estructura completa:")
        print("  total = float(input('Total: '))")
        print("  porcentaje = float(input('Porcentaje de propina: '))")
        print("  propina = total * porcentaje / 100")
        print("  print(f'Propina: ${propina:.2f}')")
        print("  print(f'Total: ${total + propina:.2f}')")
        return

    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass


def ejercicio_2(pista=0):
    """🟡 Ano bisiesto: determina si un ano es bisiesto segun la regla oficial"""
    if pista == 1:
        print("💡 Pista 1: Un ano es bisiesto si:")
        print("  - Es divisible entre 4")
        print("  - PERO no entre 100 (a menos que tambien sea entre 400)")
        return
    elif pista == 2:
        print("💡 Pista 2: La condicion completa:")
        print("  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):")
        return
    elif pista == 3:
        print("💡 Pista 3: Estructura completa:")
        print("  year = int(input('Ingresa un ano: '))")
        print("  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):")
        print("      print(f'{year} es bisiesto')")
        print("  else:")
        print("      print(f'{year} no es bisiesto')")
        return

    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass


def ejercicio_3(pista=0):
    """🔴 Verificar triangulo: 3 lados pueden formar un triangulo?"""
    if pista == 1:
        print("💡 Pista 1: Pide los 3 lados y guardalos como float")
        return
    elif pista == 2:
        print("💡 Pista 2: Condicion: la suma de 2 lados debe ser MAYOR que el tercero")
        print("  PARA TODAS las combinaciones posibles:")
        print("  a + b > c AND a + c > b AND b + c > a")
        return
    elif pista == 3:
        print("💡 Pista 3: Estructura completa:")
        print("  a = float(input('Lado 1: '))")
        print("  b = float(input('Lado 2: '))")
        print("  c = float(input('Lado 3: '))")
        print("  if a + b > c and a + c > b and b + c > a:")
        print("      print('Si forma triangulo')")
        print("  else:")
        print("      print('No forma triangulo')")
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
        print("Ejecuta: python scripts/runner.py 1 3 [N]")
        print("Pistas:  python scripts/runner.py 1 3 N -p [1|2|3]")
