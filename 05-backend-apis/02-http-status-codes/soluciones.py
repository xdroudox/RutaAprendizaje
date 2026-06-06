"""
SOLUCIONES - HTTP Status Codes
Ejecuta: python scripts/runner.py 5 2 [ejercicio] -s
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: Clasificar codigos HTTP en familias")
    print("=" * 50)

    codigos = [100, 200, 201, 301, 400, 401, 403, 404, 500, 502, 503]

    print("--- CODIGO ---")
    print("for codigo in codigos:")
    print("    if codigo < 200:")
    print("        familia = '1xx Informativo'")
    print("    elif codigo < 300:")
    print("        familia = '2xx Exito'")
    print("    elif codigo < 400:")
    print("        familia = '3xx Redireccion'")
    print("    elif codigo < 500:")
    print("        familia = '4xx Error Cliente'")
    print("    else:")
    print("        familia = '5xx Error Servidor'")
    print("    print(f'{codigo} -> {familia}')")
    print()

    print("--- RESULTADO ---")
    for codigo in codigos:
        if codigo < 200:
            familia = "1xx Informativo"
        elif codigo < 300:
            familia = "2xx Exito"
        elif codigo < 400:
            familia = "3xx Redireccion"
        elif codigo < 500:
            familia = "4xx Error Cliente"
        else:
            familia = "5xx Error Servidor"
        print(f"  {codigo} -> {familia}")

    print()
    print("--- EXPLICACION ---")
    print("""
Los codigos HTTP se clasifican por su primer digito:

  1xx: Informacion (100-199)
  2xx: Exito (200-299)
  3xx: Redireccion (300-399)
  4xx: Error del cliente (400-499)
  5xx: Error del servidor (500-599)

Esta estructura permite manejar respuestas sin conocer
cada codigo individual: basta con mirar el rango.
""")


def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: Elegir status code correcto")
    print("=" * 50)

    print("--- CODIGO ---")
    print("escenarios = [")
    print("    ('Usuario crea un recurso nuevo exitosamente', 201),")
    print("    ('Cliente solicita un recurso que no existe', 404),")
    print("    ('El servidor tuvo un error interno', 500),")
    print("    ('Cliente no esta autenticado', 401),")
    print("    ('Recurso movido permanentemente a otra URL', 301),")
    print("]")
    print("for escenario, codigo in escenarios:")
    print("    print(f'[{codigo}] {escenario}')")
    print()

    escenarios = [
        ("Usuario crea un recurso nuevo exitosamente", 201),
        ("Cliente solicita un recurso que no existe", 404),
        ("El servidor tuvo un error interno", 500),
        ("Cliente no esta autenticado", 401),
        ("Recurso movido permanentemente a otra URL", 301),
    ]

    print("--- RESULTADO ---")
    for escenario, codigo in escenarios:
        print(f"  [{codigo}] {escenario}")

    print()
    print("--- EXPLICACION ---")
    print("""
Codigo HTTP para cada escenario:

  201 Created     → POST exitoso (recurso creado)
  404 Not Found   → El recurso solicitado no existe
  500 Internal    → Error inesperado del servidor
  401 Unauthorized → Falta autenticacion
  301 Moved       → El recurso cambio de URL permanentemente

Regla general:
  - El cliente usa 4xx cuando el error es del usuario
  - El servidor usa 5xx cuando el error es interno
  - 2xx para exito, 3xx para redirecciones
""")


def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: Manejar errores HTTP con if/elif")
    print("=" * 50)

    status_code = 404

    print("--- CODIGO ---")
    print("if status_code == 200:")
    print("    print('Procesando respuesta exitosa...')")
    print("elif status_code == 201:")
    print("    print('Recurso creado exitosamente.')")
    print("elif status_code == 301:")
    print("    print('Redirigiendo a la nueva URL...')")
    print("elif status_code == 400:")
    print("    print('Error en la solicitud. Revisa los parametros.')")
    print("elif status_code == 401:")
    print("    print('Autenticacion requerida. Inicia sesion.')")
    print("elif status_code == 403:")
    print("    print('Acceso denegado. No tienes permisos.')")
    print("elif status_code == 404:")
    print("    print('Recurso no encontrado. Verifica la URL.')")
    print("elif status_code == 500:")
    print("    print('Error interno del servidor. Intenta mas tarde.')")
    print("else:")
    print("    print(f'Codigo desconocido: {status_code}')")
    print()

    print("--- RESULTADO ---")
    if status_code == 200:
        print("  Procesando respuesta exitosa...")
    elif status_code == 201:
        print("  Recurso creado exitosamente.")
    elif status_code == 301:
        print("  Redirigiendo a la nueva URL...")
    elif status_code == 400:
        print("  Error en la solicitud. Revisa los parametros.")
    elif status_code == 401:
        print("  Autenticacion requerida. Inicia sesion.")
    elif status_code == 403:
        print("  Acceso denegado. No tienes permisos.")
    elif status_code == 404:
        print("  Recurso no encontrado. Verifica la URL.")
    elif status_code == 500:
        print("  Error interno del servidor. Intenta mas tarde.")
    else:
        print(f"  Codigo desconocido: {status_code}")

    print()
    print("--- EXPLICACION ---")
    print("""
En aplicaciones reales usamos un enfoque mas limpio
con un diccionario en lugar de if/elif largos:

  manejo = {
      200: lambda: print('OK'),
      201: lambda: print('Creado'),
      301: lambda: print('Redirigir'),
      400: lambda: print('Bad request'),
      401: lambda: print('No autenticado'),
      403: lambda: print('Prohibido'),
      404: lambda: print('No encontrado'),
      500: lambda: print('Error servidor'),
  }
  manejo.get(status_code, lambda: print(f'Desconocido: {status_code}'))()

Esto es mas facil de mantener y extender.
""")


if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
