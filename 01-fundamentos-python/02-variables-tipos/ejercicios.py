"""
EJERCICIOS - Variables y Tipos de Datos
Ejecuta desde raiz: python scripts/runner.py 1 2 [ejercicio]

Niveles:
  🟢 Ej 1: Presentacion personal (variables + f-strings)
  🟡 Ej 2: Edad en dias (input + int + multiplicacion)
  🔴 Ej 3: Detector de tipos (type() con input)

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
    """🟢 Presentacion personal: crea variables nombre, edad, ciudad y muestralas"""
    if pista == 1:
        print("💡 Pista 1: Usa input() para pedir cada dato:")
        print("  nombre = input('Tu nombre: ')")
        print("  edad = input('Tu edad: ')")
        return
    elif pista == 2:
        print("💡 Pista 2: Para mostrar todo junto, usa f-string:")
        print("  print(f'Hola, me llamo {nombre}...')")
        return
    elif pista == 3:
        print("💡 Pista 3: Estructura completa:")
        print("  nombre = input('Tu nombre: ')")
        print("  edad = input('Tu edad: ')")
        print("  ciudad = input('Tu ciudad: ')")
        print("  print(f'Hola, me llamo {nombre}, tengo {edad} anos y vivo en {ciudad}')")
        return

    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass


def ejercicio_2(pista=0):
    """🟡 Edad en dias: pide edad en anos, calcula dias = edad * 365 y muestra"""
    if pista == 1:
        print("💡 Pista 1: input() devuelve texto. Conviertelo a int con int()")
        print("  edad = int(input('Cuantos anos tienes? '))")
        return
    elif pista == 2:
        print("💡 Pista 2: dias = edad * 365")
        print("  Muestra el resultado con print(f'...{dias}...')")
        return
    elif pista == 3:
        print("💡 Pista 3: Estructura completa:")
        print("  edad = int(input('Cuantos anos tienes? '))")
        print("  dias = edad * 365")
        print("  print(f'Has vivido aproximadamente {dias} dias')")
        return

    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass


def ejercicio_3(pista=0):
    """🔴 Detector de tipos: pide 3 valores y muestra type() de cada uno"""
    if pista == 1:
        print("💡 Pista 1: input() SIN convertir. Guardalo directo:")
        print("  v1 = input('Valor 1: ')")
        return
    elif pista == 2:
        print("💡 Pista 2: type(variable) te dice el tipo.")
        print("  print(f'{v1} es {type(v1)}')")
        return
    elif pista == 3:
        print("💡 Pista 3: Estructura completa:")
        print("  v1 = input('Valor 1: ')")
        print("  v2 = input('Valor 2: ')")
        print("  v3 = input('Valor 3: ')")
        print("  print(type(v1))")
        print("  print(type(v2))")
        print("  print(type(v3))")
        print("  Todos seran <class 'str'> porque input() siempre devuelve texto.")
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
        print("Ejecuta: python scripts/runner.py 1 2 [N]")
        print("Pistas:  python scripts/runner.py 1 2 N -p [1|2|3]")
