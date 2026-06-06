"""
EJERCICIOS - JSON y XML
Ejecuta desde raiz: python scripts/runner.py 5 3 [ejercicio]

Niveles:
  🟢 Ej 1: Convertir dict a JSON con json.dumps()
  🟡 Ej 2: Parsear JSON a dict con json.loads()
  🔴 Ej 3: Leer JSON de archivo y extraer datos

Pistas: python scripts/runner.py 5 3 N -p [1|2|3]
"""

import sys
import json

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1(pista=0):
    """🟢 Convertir dict a JSON con json.dumps()"""
    print(">> 🟢 EJERCICIO 1: Convertir dict a JSON")
    print("-" * 50)

    usuario = {
        "id": 1,
        "nombre": "Ana",
        "email": "ana@ejemplo.com",
        "activo": True,
        "tags": ["admin", "user"]
    }

    print(f"Diccionario original: {usuario}")

    if pista == 1:
        print("\n💡 Pista 1: Usa json.dumps() con indentacion:")
        print("  json_str = json.dumps(usuario, indent=2, ensure_ascii=False)")
        return
    elif pista == 2:
        print("\n💡 Pista 2: Parametros utiles de dumps():")
        print("  indent=N -> formatea con N espacios de indentacion")
        print("  ensure_ascii=False -> permite caracteres acentuados")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Salida esperada:")
        print('  {')
        print('    "id": 1,')
        print('    "nombre": "Ana",')
        print('    "email": "ana@ejemplo.com",')
        print('    "activo": true,')
        print('    "tags": [')
        print('      "admin",')
        print('      "user"')
        print('    ]')
        print('  }')
        print("  Nota: True → true, los strings usan comillas dobles")
        return

    print("\nConvierte el diccionario a string JSON con formato legible.")
    print("Usa json.dumps() con indent=2 y ensure_ascii=False.")
    print("\n# ==== ESCRIBE TU CODIGO AQUI ====")


def ejercicio_2(pista=0):
    """🟡 Parsear JSON a dict con json.loads()"""
    print(">> 🟡 EJERCICIO 2: Parsear JSON a dict")
    print("-" * 50)

    json_str = '{"id": 1, "nombre": "Ana", "email": "ana@ejemplo.com", "activo": true}'

    print(f"String JSON: {json_str}")

    if pista == 1:
        print("\n💡 Pista 1: Usa json.loads() para convertir el string a dict:")
        print("  datos = json.loads(json_str)")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  datos = json.loads(json_str)")
        print("  print(f'Nombre: {datos[\"nombre\"]}')")
        print("  print(f'Email: {datos[\"email\"]}')")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Salida esperada:")
        print("  Nombre: Ana")
        print("  Email: ana@ejemplo.com")
        print("  Activo: True")
        return

    print("\nConvierte el string JSON a diccionario e imprime nombre y email.")
    print("\n# ==== ESCRIBE TU CODIGO AQUI ====")


def ejercicio_3(pista=0):
    """🔴 Leer JSON de archivo y extraer datos"""
    print(">> 🔴 EJERCICIO 3: Leer JSON de archivo")
    print("-" * 50)

    import os
    ruta = os.path.join(os.path.dirname(__file__), "datos.json")
    print(f"Buscando archivo: {ruta}")

    if pista == 1:
        print("\n💡 Pista 1: Usa json.load() para leer archivos:")
        print("  with open(ruta, 'r', encoding='utf-8') as f:")
        print("      datos = json.load(f)")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  if os.path.exists(ruta):")
        print("      with open(ruta, 'r', encoding='utf-8') as f:")
        print("          datos = json.load(f)")
        print("      print(json.dumps(datos, indent=2, ensure_ascii=False))")
        print("  else:")
        print("      print(f'Archivo no encontrado: {ruta}')")
        return
    elif pista == 3:
        print("\n💡 Pista 3: El archivo datos.json debe contener:")
        print("  [")
        print("    { \"id\": 1, \"nombre\": \"Ana\", \"email\": \"ana@email.com\" },")
        print("    { \"id\": 2, \"nombre\": \"Juan\", \"email\": \"juan@email.com\" }")
        print("  ]")
        print("  Crea este archivo en el directorio del modulo si no existe.")
        return

    print("\nLee el archivo datos.json usando json.load() y muestra su contenido.")
    print("Verifica que el archivo exista antes de intentar leerlo.")
    print("\n# ==== ESCRIBE TU CODIGO AQUI ====")


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
