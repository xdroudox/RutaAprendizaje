"""
EJERCICIOS - Middleware y Filtros
Ejecuta desde raiz: python scripts/runner.py 5 8 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Funcion middleware que logee requests"""
    request = {"method": "GET", "path": "/api/usuarios", "headers": {}}
    # Crea una funcion middleware() que imprima el metodo y la ruta
    # y devuelva el request sin modificar
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass

def ejercicio_2():
    """Middleware de autenticacion que revisa token"""
    request = {"method": "GET", "path": "/api/usuarios", "headers": {"Authorization": "Bearer token_valido"}}
    # Crea un middleware que verifique que exista el header Authorization
    # Si no existe, imprime "Acceso denegado"
    # Si existe, imprime "Token valido" y continua
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass

def ejercicio_3():
    """Pipeline de middlewares"""
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

    # Crea una funcion run_pipeline(request, middlewares) que ejecute
    # cada middleware en orden. Si alguno devuelve None, detiene el pipeline.
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            print(f">> EJERCICIO {num + 1}: {ejercicios[num].__doc__}")
            print("-" * 40)
            ejercicios[num]()
    else:
        print("EJERCICIOS:")
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
