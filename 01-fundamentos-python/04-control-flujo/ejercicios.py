"""
EJERCICIOS - Control de Flujo
Ejecuta desde raiz: python scripts/runner.py 1 4 [ejercicio]

Niveles:
  🟢 Ej 1: Clasificador de notas (if/elif/else basico)
  🟡 Ej 2: Tabla de multiplicar formateada (for + condicional dentro del bucle)
  🔴 Ej 3: Juego adivinar con limite de intentos (while + condicional + random)

Pistas:
  python ejercicios.py N -p 1  (pista suave)
  python ejercicios.py N -p 2  (pista media)
  python ejercicios.py N -p 3  (pista fuerte)
"""

import sys
import random

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


# ---------------------------------------------------------------------------
# 🟢 EJERCICIO 1: Clasificador de notas (Basico)
# ---------------------------------------------------------------------------

def ejercicio_1(pista=0):
    """
    🟢 Clasificador de notas
    Pide una nota (0-100) y muestra la calificacion:
    A (90-100), B (80-89), C (70-79), D (60-69), F (<60)
    Valida que la nota este entre 0 y 100.
    """
    if pista == 1:
        print("💡 Pista 1: Usa input() para leer la nota y int() para convertirla a numero")
        print("  Ej: nota = int(input('Ingresa la nota: '))")
        return
    elif pista == 2:
        print("💡 Pista 2: Primero valida que 0 <= nota <= 100 con un if/else")
        print("  Si la nota no es valida, muestra 'Nota invalida'")
        print("  Si es valida, usa elif para cada rango, del mas alto al mas bajo")
        return
    elif pista == 3:
        print("💡 Pista 3: Estructura sugerida:")
        print("  if nota < 0 or nota > 100:")
        print("      print('Nota invalida')")
        print("  elif nota >= 90:")
        print("      print('A')")
        print("  elif nota >= 80:")
        print("      print('B')")
        print("  # ... y asi sucesivamente")
        return

    # ==== ESCRIBE TU RESPUESTA AQUI ====
    # 1. Pide la nota al usuario: nota = int(input("..."))
    # 2. Valida que este entre 0 y 100
    # 3. Clasifica con if/elif/else en orden descendente
    # 4. Muestra la calificacion
    pass


# ---------------------------------------------------------------------------
# 🟡 EJERCICIO 2: Tabla de multiplicar formateada (Intermedio)
# ---------------------------------------------------------------------------

def ejercicio_2(pista=0):
    """
    🟡 Tabla de multiplicar formateada
    Pide un numero y muestra su tabla del 1 al 10.
    Cada linea: "NUM x i = RESULTADO"
    Si el resultado es multiplo de 5, agrega " *" al final.
    """
    if pista == 1:
        print("💡 Pista 1: Usa un bucle for con range(1, 11) para generar 1 a 10")
        print("  Dentro del bucle, multiplica el numero ingresado por i")
        return
    elif pista == 2:
        print("💡 Pista 2: Para saber si es multiplo de 5, usa: resultado % 5 == 0")
        print("  Si es True, agrega ' *' al final de la linea")
        print("  Usa f-strings para formatear: f'{numero} x {i} = {resultado}'")
        return
    elif pista == 3:
        print("💡 Pista 3: Estructura sugerida:")
        print("  numero = int(input('Que tabla deseas ver? '))")
        print("  for i in range(1, 11):")
        print("      resultado = numero * i")
        print("      if resultado % 5 == 0:")
        print("          print(f'{numero} x {i} = {resultado} *')")
        print("      else:")
        print("          print(f'{numero} x {i} = {resultado}')")
        return

    # ==== ESCRIBE TU RESPUESTA AQUI ====
    # 1. Pide el numero: numero = int(input("..."))
    # 2. Bucle for de 1 a 10
    # 3. Dentro: calcula resultado = numero * i
    # 4. Si resultado % 5 == 0: muestra con " *" al final
    # 5. Si no: muestra normal
    pass


# ---------------------------------------------------------------------------
# 🔴 EJERCICIO 3: Juego de adivinar con limite de intentos (Avanzado)
# ---------------------------------------------------------------------------

def ejercicio_3(pista=0):
    """
    🔴 Juego de adivinar con limite de intentos
    El programa genera un numero aleatorio entre 1 y 20.
    El usuario tiene 5 intentos para adivinarlo.
    Pistas: "mayor" o "menor".
    Si falla los 5: muestra "Game over" y el numero.
    Al final: pregunta si quiere jugar de nuevo.
    """
    if pista == 1:
        print("💡 Pista 1: Usa random.randint(1, 20) para generar el numero secreto")
        print("  Usa una variable 'intentos = 5' que se reduzca en cada fallo")
        print("  El bucle principal: while intentos > 0:")
        return
    elif pista == 2:
        print("💡 Pista 2: Estructura del juego:")
        print("  - Dentro del while: pide un numero al usuario")
        print("  - Si acierta: print('Felicidades!') + break")
        print("  - Si falla: intentos -= 1, da pista mayor/menor")
        print("  - Si intentos == 0: muestra el numero secreto")
        print("  - Despues del while: pregunta si jugar de nuevo")
        return
    elif pista == 3:
        print("💡 Pista 3: Estructura sugerida:")
        print("  while True:")
        print("      secreto = random.randint(1, 20)")
        print("      intentos = 5")
        print("      while intentos > 0:")
        print("          num = int(input('Adivina (1-20): '))")
        print("          if num == secreto:")
        print("              print('Felicidades!')")
        print("              break")
        print("          else:")
        print("              intentos -= 1")
        print("              if num > secreto: print('Muy alto')")
        print("              else: print('Muy bajo')")
        print("      if intentos == 0: print(f'Game over! Era {secreto}')")
        print("      again = input('Jugar de nuevo? (s/n): ')")
        print("      if again != 's': break")
        return

    # ==== ESCRIBE TU RESPUESTA AQUI ====
    # 1. Bucle exterior: while True (para jugar de nuevo)
    # 2. Genera numero aleatorio: random.randint(1, 20)
    # 3. Inicializa intentos = 5
    # 4. Bucle interior: while intentos > 0
    #    - Pide numero
    #    - Si acierta: mensaje y break
    #    - Si falla: reduce intentos, da pista
    # 5. Si se acaban los intentos: mensaje game over
    # 6. Pregunta si quiere jugar de nuevo
    pass


# ---------------------------------------------------------------------------
# DISPATCHER
# ---------------------------------------------------------------------------

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
            # Mostrar nivel de dificultad
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
        print("Ejecuta: python scripts/runner.py 1 4 [N]")
        print("Pistas:  python scripts/runner.py 1 4 N -p [1|2|3]")
