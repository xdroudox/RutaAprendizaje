"""
EJERCICIOS - Middleware y Filtros
Ejecuta desde raiz: python scripts/runner.py 5 8 [ejercicio]

Niveles:
  🟢 Ej 1: Middleware de logging
  🟡 Ej 2: Middleware de autenticacion
  🔴 Ej 3: Pipeline de middlewares

Pistas: python scripts/runner.py 5 8 N -p [1|2|3]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1(pista=0):
    """🟢 Middleware de logging"""
    print(">> 🟢 EJERCICIO 1: Middleware de logging")
    print("-" * 50)

    request = {"method": "GET", "path": "/api/usuarios", "headers": {}}

    print(f"Request: {request}")

    if pista == 1:
        print("\n💡 Pista 1: Un middleware es una funcion que recibe y devuelve request:")
        print("  def middleware(req):")
        print("      print(f'[Middleware] Request: {req[\"method\"]} {req[\"path\"]}')")
        print("      return req")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  def log_middleware(req):")
        print("      print(f'[LOG] {req[\"method\"]} {req[\"path\"]}')")
        print("      return req")
        print()
        print("  resultado = log_middleware(request)")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Salida esperada:")
        print("  [LOG] GET /api/usuarios")
        print("  Request procesado: {'method': 'GET', 'path': '/api/usuarios', ...}")
        return

    print("\nCrea una funcion middleware que reciba el request,")
    print("imprima el metodo y la ruta, y devuelva el request.")
    print("\n# ==== ESCRIBE TU CODIGO AQUI ====")


def ejercicio_2(pista=0):
    """🟡 Middleware de autenticacion"""
    print(">> 🟡 EJERCICIO 2: Middleware de autenticacion")
    print("-" * 50)

    request = {"method": "GET", "path": "/api/usuarios", "headers": {"Authorization": "Bearer token_valido"}}

    print(f"Request: {request}")

    if pista == 1:
        print("\n💡 Pista 1: Verifica si el header Authorization existe:")
        print("  auth = req['headers'].get('Authorization', '')")
        print("  if auth.startswith('Bearer '):")
        print("      token = auth[7:]")
        print("      print(f'Token valido: {token}')")
        print("      return req")
        print("  else:")
        print("      print('Acceso denegado')")
        print("      return None")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  def auth_middleware(req):")
        print("      if 'Authorization' in req['headers']:")
        print("          print('Token presente')")
        print("          return req")
        print("      else:")
        print("          print('Acceso denegado')")
        print("          return None")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Salida esperada con token:")
        print("  Token valido: token_valido...")
        print("  Request autorizado, continuando...")
        return

    print("\nCrea un middleware que verifique que exista el header")
    print("Authorization. Si existe → continua (devuelve req),")
    print("si no existe → rechaza (devuelve None).")
    print("\n# ==== ESCRIBE TU CODIGO AQUI ====")


def ejercicio_3(pista=0):
    """🔴 Pipeline de middlewares"""
    print(">> 🔴 EJERCICIO 3: Pipeline de middlewares")
    print("-" * 50)

    def logging_mw(req):
        print(f"[LOG] {req['method']} {req['path']}")
        return req

    def auth_mw(req):
        if "Authorization" in req["headers"]:
            print("[AUTH] Token presente")
            return req
        else:
            print("[AUTH] Acceso denegado")
            return None

    print("Middlewares disponibles: logging_mw, auth_mw")

    if pista == 1:
        print("\n💡 Pista 1: La funcion run_pipeline ejecuta middlewares en orden:")
        print("  def run_pipeline(request, middlewares):")
        print("      for mw in middlewares:")
        print("          if request is None:")
        print("              print('Pipeline detenido')")
        print("              break")
        print("          request = mw(request)")
        print("      return request")
        return
    elif pista == 2:
        print("\n💡 Pista 2: Prueba con request valido e invalido:")
        print("  req_valido = {'method': 'GET', 'path': '/api/data', 'headers': {'Authorization': 'Bearer x'}}")
        print("  req_invalido = {'method': 'POST', 'path': '/api/data', 'headers': {}}")
        print("  run_pipeline(req_valido, [logging_mw, auth_mw])")
        print("  run_pipeline(req_invalido, [auth_mw])")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Salida esperada:")
        print("  Pipeline con request valido:")
        print("    [LOG] GET /api/data")
        print("    [AUTH] Token presente")
        print("  Pipeline sin token:")
        print("    [AUTH] Acceso denegado")
        print("    Pipeline detenido")
        return

    print("\nCrea una funcion run_pipeline(request, middlewares) que")
    print("ejecute cada middleware en orden. Si alguno devuelve None,")
    print("detiene el pipeline.")
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
