"""
SOLUCIONES - JSON y XML
Ejecuta: python scripts/runner.py 5 3 [ejercicio] -s
"""

import sys
import json

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: Convertir dict a JSON con json.dumps()")
    print("=" * 50)

    usuario = {
        "id": 1,
        "nombre": "Ana",
        "email": "ana@ejemplo.com",
        "activo": True,
        "tags": ["admin", "user"]
    }

    print("--- CODIGO ---")
    print("json_str = json.dumps(usuario, indent=2, ensure_ascii=False)")
    print()

    json_str = json.dumps(usuario, indent=2, ensure_ascii=False)

    print("--- RESULTADO ---")
    print(json_str)

    print()
    print("--- EXPLICACION ---")
    print("""
json.dumps() convierte un objeto Python a string JSON:

  indent=2: Formatea con 2 espacios de indentacion
  ensure_ascii=False: Permite caracteres Unicode (acentos, ñ, etc.)

Conversion de tipos:
  Python  →  JSON
  dict    →  object  {...}
  list    →  array   [...]
  str     →  string  "..."
  int     →  number
  True    →  true
  None    →  null
""")


def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: Parsear JSON a dict con json.loads()")
    print("=" * 50)

    json_str = '{"id": 1, "nombre": "Ana", "email": "ana@ejemplo.com", "activo": true}'

    print("--- CODIGO ---")
    print("datos = json.loads(json_str)")
    print("print(f'Nombre: {datos[\"nombre\"]}')")
    print("print(f'Email: {datos[\"email\"]}')")
    print("print(f'Activo: {datos[\"activo\"]}')")
    print()

    datos = json.loads(json_str)

    print("--- RESULTADO ---")
    print(f"  Nombre: {datos['nombre']}")
    print(f"  Email: {datos['email']}")
    print(f"  Activo: {datos['activo']}")

    print()
    print("--- EXPLICACION ---")
    print("""
json.loads() convierte un string JSON a objeto Python:

  JSON     →  Python
  object   →  dict
  array    →  list
  string   →  str
  number   →  int/float
  true     →  True
  false    →  False
  null     →  None

Nota: JSON usa comillas dobles obligatoriamente y los
booleanos son en minuscula (true/false), no como en
Python (True/False).
""")


def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: Leer JSON de archivo y extraer datos")
    print("=" * 50)

    import os
    ruta = os.path.join(os.path.dirname(__file__), "datos.json")

    print("--- CODIGO ---")
    print("with open(ruta, 'r', encoding='utf-8') as f:")
    print("    datos = json.load(f)")
    print("print(json.dumps(datos, indent=2, ensure_ascii=False))")
    print()

    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as f:
            datos = json.load(f)

        print("--- RESULTADO ---")
        print(json.dumps(datos, indent=2, ensure_ascii=False))
        if isinstance(datos, list):
            print(f"\n  Total de registros: {len(datos)}")
    else:
        print("  Archivo datos.json no encontrado.")
        print("  Crealo con este contenido:")
        print()
        ejemplo = [
            {"id": 1, "nombre": "Ana", "email": "ana@email.com"},
            {"id": 2, "nombre": "Juan", "email": "juan@email.com"}
        ]
        print(json.dumps(ejemplo, indent=2, ensure_ascii=False))

    print()
    print("--- EXPLICACION ---")
    print("""
json.load() lee JSON directamente desde un archivo:

  with open('datos.json', 'r', encoding='utf-8') as f:
      datos = json.load(f)

Es equivalente a:
  with open('datos.json', 'r') as f:
      datos = json.loads(f.read())

Usos reales:
  - Leer configuraciones (config.json)
  - Cargar datos de prueba (seed data)
  - Leer respuestas de APIs guardadas en archivos
""")


if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
