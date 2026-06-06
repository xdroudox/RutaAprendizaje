"""
EJERCICIOS - Colecciones
Ejecuta desde raiz: python scripts/runner.py 1 7 [ejercicio]

Niveles:
  🟢 Ej 1: Operaciones con listas (append, insert, pop, len)
  🟡 Ej 2: Agenda telefonica (diccionarios + menu con bucle)
  🔴 Ej 3: Analizador de texto (frecuencia de palabras con dict)

Pistas:
  python ejercicios.py N -p 1
  python ejercicios.py N -p 2
  python ejercicios.py N -p 3
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


# ---------------------------------------------------------------------------
# 🟢 EJERCICIO 1: Operaciones con listas
# ---------------------------------------------------------------------------

def ejercicio_1(pista=0):
    """
    🟢 Operaciones con listas
    Crea una lista vacia. Agrega 1-5 con append(), inserta 0 al inicio,
    elimina el ultimo con pop(). Muestra la lista final y su longitud.
    """
    if pista == 1:
        print("💡 Pista 1: Empieza con lista_vacia = []")
        print("  append(1), append(2)... hasta append(5)")
        return
    elif pista == 2:
        print("💡 Pista 2: Despues de tener [1, 2, 3, 4, 5]:")
        print("  lista.insert(0, 0) → [0, 1, 2, 3, 4, 5]")
        print("  lista.pop() → elimina el 5 → [0, 1, 2, 3, 4]")
        return
    elif pista == 3:
        print("💡 Pista 3: Estructura completa:")
        print("  nums = []")
        print("  for i in range(1, 6):")
        print("      nums.append(i)")
        print("  nums.insert(0, 0)")
        print("  nums.pop()")
        print("  print('Lista:', nums)")
        print("  print('Longitud:', len(nums))")
        return

    # ==== ESCRIBE TU RESPUESTA AQUI ====
    # 1. Crea una lista vacia
    # 2. Agrega los numeros 1 al 5 con append()
    # 3. Inserta 0 al principio con insert(0, 0)
    # 4. Elimina el ultimo elemento con pop()
    # 5. Muestra la lista y su longitud
    pass


# ---------------------------------------------------------------------------
# 🟡 EJERCICIO 2: Agenda telefonica
# ---------------------------------------------------------------------------

def ejercicio_2(pista=0):
    """
    🟡 Agenda telefonica
    Menu interactivo: 1) Agregar contacto, 2) Buscar telefono,
    3) Mostrar todos, 4) Salir. Usa un diccionario.
    """
    if pista == 1:
        print("💡 Pista 1: Crea un diccionario vacio: agenda = {}")
        print("  Usa un while True para el menu.")
        print("  Muestra opciones con print() y lee con input().")
        return
    elif pista == 2:
        print("💡 Pista 2: Estructura del menu:")
        print("  while True:")
        print("      print('1. Agregar 2. Buscar 3. Mostrar 4. Salir')")
        print("      opcion = input('Elige: ')")
        print("      if opcion == '1': ...")
        print("      elif opcion == '2': ...")
        print("      elif opcion == '4': break")
        return
    elif pista == 3:
        print("💡 Pista 3: Para cada opcion:")
        print("  1. nombre = input('Nombre: '); telefono = input('Telefono: ')")
        print("     agenda[nombre] = telefono")
        print("  2. nombre = input('Buscar: '); print(agenda.get(nombre, 'No encontrado'))")
        print("  3. for nombre, telefono in agenda.items():")
        print("       print(f'{nombre}: {telefono}')")
        return

    # ==== ESCRIBE TU RESPUESTA AQUI ====
    # 1. Crea agenda = {}
    # 2. while True con menu de opciones
    # 3. Opcion 1: agrega contacto (clave = nombre, valor = telefono)
    # 4. Opcion 2: busca por nombre (usa .get() para evitar error)
    # 5. Opcion 3: recorre con .items() y muestra todos
    # 6. Opcion 4: break
    pass


# ---------------------------------------------------------------------------
# 🔴 EJERCICIO 3: Analizador de texto
# ---------------------------------------------------------------------------

def ejercicio_3(pista=0):
    """
    🔴 Analizador de texto
    Pide una frase. Muestra:
    - Total de caracteres
    - Cantidad de palabras
    - Frecuencia de cada palabra
    - Palabra mas larga
    """
    if pista == 1:
        print("💡 Pista 1: Divide la frase con .split() para obtener palabras")
        print("  Total caracteres: len(frase) (con espacios)")
        print("  Cantidad palabras: len(palabras)")
        return
    elif pista == 2:
        print("💡 Pista 2: Para la frecuencia:")
        print("  frecuencia = {}")
        print("  for palabra in palabras:")
        print("      if palabra in frecuencia:")
        print("          frecuencia[palabra] += 1")
        print("      else:")
        print("          frecuencia[palabra] = 1")
        print("  Para palabra mas larga: max(palabras, key=len)")
        return
    elif pista == 3:
        print("💡 Pista 3: Estructura completa:")
        print("  frase = input('Ingresa una frase: ')")
        print("  palabras = frase.split()")
        print("  print(f'Caracteres: {len(frase)}')")
        print("  print(f'Palabras: {len(palabras)}')")
        print("  frec = {}")
        print("  for p in palabras:")
        print("      frec[p] = frec.get(p, 0) + 1")
        print("  print('Frecuencias:')")
        print("  for p, c in frec.items():")
        print("      print(f'  {p}: {c}')")
        print("  print(f'Mas larga: {max(palabras, key=len)}')")
        return

    # ==== ESCRIBE TU RESPUESTA AQUI ====
    # 1. Pide la frase
    # 2. Divide en palabras con .split()
    # 3. Muestra total de caracteres y cantidad de palabras
    # 4. Crea un diccionario de frecuencias
    # 5. Encuentra la palabra mas larga con max(..., key=len)
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
        print("Ejecuta: python scripts/runner.py 1 7 [N]")
        print("Pistas:  python scripts/runner.py 1 7 N -p [1|2|3]")
