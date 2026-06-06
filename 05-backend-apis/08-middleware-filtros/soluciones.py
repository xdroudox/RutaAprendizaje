"""
SOLUCIONES - Middleware y Filtros
Ejecuta: python scripts/runner.py 5 8 [ejercicio] -s
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: Middleware de logging")
    print("=" * 50)

    request = {"method": "GET", "path": "/api/usuarios", "headers": {}}

    print("--- CODIGO ---")
    print("def log_middleware(req):")
    print("    print(f'[LOG] {req[\"method\"]} {req[\"path\"]}')")
    print("    return req")
    print()

    def log_middleware(req):
        print(f"  [LOG] {req['method']} {req['path']}")
        return req

    resultado = log_middleware(request)

    print(f"  Request procesado: {resultado}")

    print()
    print("--- EXPLICACION ---")
    print("""
Un middleware de logging se ejecuta al principio del pipeline.
Su unica responsabilidad es registrar informacion sobre el request
y pasarlo al siguiente middleware.

En frameworks reales (Flask, Express, Spring):
  - No se devuelve el request explicitamente
  - Se llama a next() o se retorna para continuar
  - El framework maneja automaticamente el pipeline
""")


def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: Middleware de autenticacion")
    print("=" * 50)

    request = {"method": "GET", "path": "/api/usuarios", "headers": {"Authorization": "Bearer token_valido"}}

    print("--- CODIGO ---")
    print("def auth_middleware(req):")
    print("    auth = req['headers'].get('Authorization', '')")
    print("    if auth.startswith('Bearer '):")
    print("        token = auth[7:]")
    print("        print(f'Token valido: {token[:20]}...')")
    print("        return req")
    print("    else:")
    print("        print('Acceso denegado: Token no proporcionado')")
    print("        return None")
    print()

    def auth_middleware(req):
        auth = req["headers"].get("Authorization", "")
        if auth.startswith("Bearer "):
            token = auth[7:]
            print(f"  Token valido: {token[:20]}...")
            return req
        else:
            print("  Acceso denegado: Token no proporcionado")
            return None

    resultado = auth_middleware(request)
    if resultado:
        print("  Request autorizado, continuando...")

    print()
    print("--- EXPLICACION ---")
    print("""
El middleware de autenticacion puede:

  1. Dejar pasar (return req) → el siguiente middleware continua
  2. Rechazar (return None) → el pipeline se detiene
  3. Modificar el request (agregar datos del usuario) → enriquecer

En lugar de None, en frameworks reales se lanza una excepcion
HTTP (401 Unauthorized) que corta el pipeline inmediatamente.
""")


def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: Pipeline de middlewares")
    print("=" * 50)

    def logging_mw(req):
        print(f"  [LOG] {req['method']} {req['path']}")
        return req

    def auth_mw(req):
        if "Authorization" in req["headers"]:
            print("  [AUTH] Token presente")
            return req
        else:
            print("  [AUTH] Acceso denegado")
            return None

    def cors_mw(req):
        print("  [CORS] Headers CORS agregados")
        req["headers"]["Access-Control-Allow-Origin"] = "*"
        return req

    def run_pipeline(request, middlewares):
        print("  Iniciando pipeline...")
        for mw in middlewares:
            if request is None:
                print("  Pipeline detenido")
                break
            request = mw(request)
        if request:
            print("  Pipeline completado exitosamente")
        return request

    print("--- CODIGO ---")
    print("def run_pipeline(request, middlewares):")
    print("    for mw in middlewares:")
    print("        if request is None:")
    print("            break")
    print("        request = mw(request)")
    print("    return request")
    print()

    request = {"method": "GET", "path": "/api/usuarios", "headers": {}}
    print("  --- Pipeline con request valido ---")
    run_pipeline(request, [logging_mw, auth_mw, cors_mw])

    print()
    request2 = {"method": "POST", "path": "/api/data", "headers": {}}
    print("  --- Pipeline sin token ---")
    run_pipeline(request2, [auth_mw, logging_mw])

    print()
    print("--- EXPLICACION ---")
    print("""
El pipeline es una implementacion del patron Chain of Responsibility:

  Ventajas:
    - Separacion de responsabilidades (cada middleware hace 1 cosa)
    - Facil de extender (agregar/quitar middlewares)
    - Orden configurable (cambiar el orden en la lista)

  Orden tipico en produccion:
    1. Logger        (registrar todo)
    2. Rate Limiter  (proteger antes de procesar)
    3. Auth          (validar identidad)
    4. CORS          (permitir origenes)
    5. Parser        (procesar body)
    6. Handler       (logica de negocio)

  Si auth falla, el rate limiter ya registro la IP, el logger
  ya registro el intento, y el handler nunca se ejecuta.
""")


if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
