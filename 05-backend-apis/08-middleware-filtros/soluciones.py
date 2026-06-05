"""
SOLUCIONES - Middleware y Filtros
Ejecuta desde raiz: python scripts/runner.py 5 8 1 -s
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Funcion middleware que logee requests"""
    def middleware(req):
        print(f"  [Middleware] Request: {req['method']} {req['path']}")
        return req
    request = {"method": "GET", "path": "/api/usuarios", "headers": {}}
    resultado = middleware(request)
    print(f"  Request procesado: {resultado}")

def ejercicio_2():
    """Middleware de autenticacion que revisa token"""
    def auth_middleware(req):
        auth = req["headers"].get("Authorization", "")
        if auth.startswith("Bearer "):
            token = auth[7:]
            print(f"  Token valido: {token[:20]}...")
            return req
        else:
            print("  Acceso denegado: Token no proporcionado")
            return None
    request = {"method": "GET", "path": "/api/usuarios", "headers": {"Authorization": "Bearer token_valido"}}
    resultado = auth_middleware(request)
    if resultado:
        print("  Request autorizado, continuando...")

def ejercicio_3():
    """Pipeline de middlewares"""
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

    request = {"method": "GET", "path": "/api/usuarios", "headers": {}}
    print("  --- Pipeline con request valido ---")
    run_pipeline(request, [logging_mw, auth_mw, cors_mw])
    print()
    request2 = {"method": "POST", "path": "/api/data", "headers": {}}
    print("  --- Pipeline sin token ---")
    run_pipeline(request2, [auth_mw, logging_mw])

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            print(f">> SOLUCION {num + 1}: {ejercicios[num].__doc__}")
            print("-" * 40)
            ejercicios[num]()
    else:
        print("SOLUCIONES:")
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
