"""
EJERCICIOS - HTTP Status Codes
Ejecuta desde raiz: python scripts/runner.py 5 2 [ejercicio]

Niveles:
  🟢 Ej 1: Clasificar codigos HTTP en familias
  🟡 Ej 2: Elegir status code correcto segun escenario
  🔴 Ej 3: Manejar errores HTTP con if/elif

Pistas: python scripts/runner.py 5 2 N -p [1|2|3]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1(pista=0):
    """🟢 Clasificar codigos HTTP en familias"""
    print(">> 🟢 EJERCICIO 1: Clasificar codigos HTTP en familias")
    print("-" * 50)

    codigos = [100, 200, 201, 301, 400, 401, 403, 404, 500, 502, 503]

    print("Codigos a clasificar:")
    print(f"  {codigos}")

    if pista == 1:
        print("\n💡 Pista 1: Regla de clasificacion:")
        print("  < 200 → 1xx Informativo")
        print("  < 300 → 2xx Exito")
        print("  < 400 → 3xx Redireccion")
        print("  < 500 → 4xx Error Cliente")
        print("  >= 500 → 5xx Error Servidor")
        return
    elif pista == 2:
        print("\n💡 Pista 2: Estructura del codigo:")
        print("  for codigo in codigos:")
        print("      if codigo < 200:")
        print("          familia = '1xx Informativo'")
        print("      elif codigo < 300:")
        print("          ...")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Salida esperada:")
        print("  100 -> 1xx Informativo")
        print("  200 -> 2xx Exito")
        print("  201 -> 2xx Exito")
        print("  301 -> 3xx Redireccion")
        print("  400 -> 4xx Error Cliente")
        print("  401 -> 4xx Error Cliente")
        print("  403 -> 4xx Error Cliente")
        print("  404 -> 4xx Error Cliente")
        print("  500 -> 5xx Error Servidor")
        print("  502 -> 5xx Error Servidor")
        print("  503 -> 5xx Error Servidor")
        return

    print("\nClasifica cada codigo en su familia:")
    print("  < 200 → 1xx Informativo")
    print("  < 300 → 2xx Exito")
    print("  < 400 → 3xx Redireccion")
    print("  < 500 → 4xx Error Cliente")
    print("  >= 500 → 5xx Error Servidor")
    print("\n# ==== ESCRIBE TU CODIGO AQUI ====")


def ejercicio_2(pista=0):
    """🟡 Elegir status code correcto segun escenario"""
    print(">> 🟡 EJERCICIO 2: Elegir status code correcto")
    print("-" * 50)

    escenarios = [
        "Usuario crea un recurso nuevo exitosamente",
        "Cliente solicita un recurso que no existe",
        "El servidor tuvo un error interno",
        "Cliente no esta autenticado",
        "Recurso movido permanentemente a otra URL"
    ]

    print("Escenarios:")
    for i, esc in enumerate(escenarios, 1):
        print(f"  {i}. {esc}")

    if pista == 1:
        print("\n💡 Pista 1: Posibles codigos:")
        print("  201 Created")
        print("  301 Moved Permanently")
        print("  401 Unauthorized")
        print("  404 Not Found")
        print("  500 Internal Server Error")
        return
    elif pista == 2:
        print("\n💡 Pista 2: Relacion escenario-codigo:")
        print("  'recurso nuevo' → 201")
        print("  'no existe' → 404")
        print("  'error interno' → 500")
        print("  'no autenticado' → 401")
        print("  'movido permanentemente' → 301")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Estructura:")
        print("  escenarios = [")
        print("      ('descripcion', codigo),")
        print("      ...")
        print("  ]")
        print("  for desc, codigo in escenarios:")
        print("      print(f'[{codigo}] {desc}')")
        return

    print("\nAsigna el codigo HTTP correcto a cada escenario.")
    print("Usa una lista de tuplas (escenario, codigo).")
    print("\n# ==== ESCRIBE TU CODIGO AQUI ====")


def ejercicio_3(pista=0):
    """🔴 Manejar errores HTTP con if/elif"""
    print(">> 🔴 EJERCICIO 3: Manejar errores HTTP con if/elif")
    print("-" * 50)

    status_code = 404

    if pista == 1:
        print("\n💡 Pista 1: Posibles acciones segun codigo:")
        print("  200 → Procesar respuesta exitosa")
        print("  201 → Recurso creado")
        print("  301 → Redirigir")
        print("  400 → Revisar solicitud")
        print("  401 → Autenticarse")
        print("  403 → Acceso denegado")
        print("  404 → Recurso no encontrado")
        print("  500 → Error del servidor")
        return
    elif pista == 2:
        print("\n💡 Pista 2: Estructura:")
        print("  if status_code == 200:")
        print("      print('Procesando respuesta exitosa...')")
        print("  elif status_code == 201:")
        print("      print('Recurso creado exitosamente.')")
        print("  elif ...")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Con status_code = 404, debe imprimir:")
        print("  'Recurso no encontrado. Verifica la URL.'")
        print("  Prueba cambiando status_code a 200, 500, etc.")
        return

    print(f"Dado el codigo de estado: {status_code}")
    print("Usa if/elif para imprimir una accion:")
    print("  200 → Procesar respuesta exitosa")
    print("  201 → Recurso creado")
    print("  301 → Redirigir")
    print("  400 → Revisar solicitud")
    print("  401 → Autenticarse")
    print("  403 → Acceso denegado")
    print("  404 → Recurso no encontrado")
    print("  500 → Error del servidor")
    print("  otro → Codigo desconocido")
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
