import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    print("=" * 50)
    print("EJERCICIO 1: Middleware de logging")
    print("=" * 50)
    print()
    print("TAREA: Implementa una funcion logging_middleware(peticion)")
    print("que imprima la hora, el metodo y la ruta de la peticion,")
    print("y luego retorne None para continuar el pipeline.")
    print()
    print("La peticion es un diccionario:")
    print('  {"metodo": "GET", "ruta": "/api/usuarios", "headers": {}}')
    print()
    print("PISTA: import time; print(f'[{time.ctime()}] {peticion[\"metodo\"]} {peticion[\"ruta\"]}'); return None")

def ejercicio_2():
    print("=" * 50)
    print("EJERCICIO 2: Middleware de autenticacion")
    print("=" * 50)
    print()
    print("TAREA: Implementa auth_middleware(peticion) que:")
    print("  1. Verifique si existe el header 'Authorization'")
    print("  2. Si no existe, retorne {'status': 401, 'body': 'No autorizado'}")
    print("  3. Si existe pero no empieza con 'Bearer ', retorne 401")
    print("  4. Si existe y es valido, retorne None")
    print()
    print('PISTA: if "Authorization" not in peticion["headers"]: return {"status": 401, "body": "No autorizado"}')

def ejercicio_3():
    print("=" * 50)
    print("EJERCICIO 3: Pipeline de middlewares")
    print("=" * 50)
    print()
    print("TAREA: Implementa la funcion procesar_peticion(peticion) que")
    print("ejecute dos middlewares en orden:")
    print("  1. auth_middleware (del ejercicio 2)")
    print("  2. logging_middleware (del ejercicio 1)")
    print()
    print("Si un middleware retorna un dict (respuesta), deten el pipeline")
    print("y devuelve esa respuesta. Si todos retornan None, devuelve:")
    print('  {"status": 200, "body": "Recurso servido"}')
    print()
    print("Prueba con peticion CON y SIN token de autorizacion.")
    print()
    print("PISTA: for mw in [auth_middleware, logging_middleware]: resultado = mw(peticion); if resultado: return resultado")

pistas = {
    "1": "import time; def logging_middleware(p): print(f'[{time.ctime()}] {p[\"metodo\"]} {p[\"ruta\"]}'); return None",
    "2": "def auth_middleware(p): h = p['headers']; token = h.get('Authorization'); if not token: return {'status': 401, 'body': 'No autorizado'}; return None",
    "3": "def procesar_peticion(p): for mw in [auth_middleware, logging_middleware]: r = mw(p); if r: return r; return {'status': 200, 'body': 'Recurso servido'}"
}

def menu():
    print("=" * 50)
    print("MIDDLEWARE Y FILTROS - EJERCICIOS")
    print("=" * 50)
    print("1 - Middleware de logging")
    print("2 - Middleware de autenticacion")
    print("3 - Pipeline de middlewares")
    print()
    print("Usa: python ejercicios.py <numero>")
    print("     python ejercicios.py <numero> -p  (pista)")

def main():
    args = sys.argv[1:]
    if not args:
        menu()
        return
    num = args[0]
    mostrar_pista = "-p" in args
    if mostrar_pista and num in pistas:
        print("=== PISTA ===")
        print(pistas[num])
        print()
    if num == "1":
        ejercicio_1()
    elif num == "2":
        ejercicio_2()
    elif num == "3":
        ejercicio_3()
    else:
        print("Ejercicio no valido. Usa 1, 2 o 3.")

if __name__ == "__main__":
    main()
