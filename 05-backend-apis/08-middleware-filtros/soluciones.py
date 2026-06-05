import sys
import time

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def auth_middleware(peticion):
    token = peticion["headers"].get("Authorization")
    if not token:
        return {"status": 401, "body": "No autorizado"}
    if not token.startswith("Bearer "):
        return {"status": 401, "body": "Token invalido"}
    return None

def logging_middleware(peticion):
    print(f"[{time.ctime()}] {peticion['metodo']} {peticion['ruta']}")
    return None

def procesar_peticion(peticion):
    for mw in [auth_middleware, logging_middleware]:
        resultado = mw(peticion)
        if resultado:
            return resultado
    return {"status": 200, "body": "Recurso servido", "headers": {"Content-Type": "application/json"}}

def solucion_1():
    print("=" * 50)
    print("SOLUCION 1: Middleware de logging")
    print("=" * 50)
    peticion = {"metodo": "GET", "ruta": "/api/usuarios", "headers": {}}
    print("Peticion:", peticion)
    print()
    print("Ejecutando logging_middleware:")
    resultado = logging_middleware(peticion)
    print("Resultado:", resultado)
    print("(None significa que continua el pipeline)")

def solucion_2():
    print("=" * 50)
    print("SOLUCION 2: Middleware de autenticacion")
    print("=" * 50)
    casos = [
        {"metodo": "GET", "ruta": "/api/admin", "headers": {}},
        {"metodo": "GET", "ruta": "/api/admin", "headers": {"Authorization": "Bearer token123"}},
        {"metodo": "GET", "ruta": "/api/admin", "headers": {"Authorization": "Basic abc123"}},
    ]
    for i, caso in enumerate(casos, 1):
        print(f"Caso {i}: {caso}")
        resultado = auth_middleware(caso)
        print(f"  Resultado: {resultado}")
        print()

def solucion_3():
    print("=" * 50)
    print("SOLUCION 3: Pipeline de middlewares")
    print("=" * 50)
    peticion_con_token = {
        "metodo": "GET",
        "ruta": "/api/usuarios",
        "headers": {"Authorization": "Bearer token123"}
    }
    peticion_sin_token = {
        "metodo": "GET",
        "ruta": "/api/admin",
        "headers": {}
    }
    print("Caso 1 - Peticion con token:")
    resultado = procesar_peticion(peticion_con_token)
    print(f"  Respuesta final: {resultado}")
    print()
    print("Caso 2 - Peticion sin token:")
    resultado = procesar_peticion(peticion_sin_token)
    print(f"  Respuesta final: {resultado}")

def menu():
    print("SOLUCIONES - MIDDLEWARE Y FILTROS")
    print("1 - Middleware de logging")
    print("2 - Middleware de autenticacion")
    print("3 - Pipeline de middlewares")

def main():
    args = sys.argv[1:]
    if not args:
        menu()
        return
    num = args[0]
    if num == "1":
        solucion_1()
    elif num == "2":
        solucion_2()
    elif num == "3":
        solucion_3()
    else:
        print("Solucion no valida. Usa 1, 2 o 3.")

if __name__ == "__main__":
    main()
