import sys
import http.client

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    print("=" * 50)
    print("SOLUCION 1: Identificar codigos por escenario")
    print("=" * 50)
    escenarios = [
        ("Un usuario intenta acceder a /admin sin estar autenticado", "401 Unauthorized"),
        ("Un recurso solicitado no existe en el servidor", "404 Not Found"),
        ("Una peticion POST crea un nuevo usuario exitosamente", "201 Created"),
        ("El servidor sufrio un error interno inesperado", "500 Internal Server Error"),
        ("Un cliente envio JSON con formato incorrecto", "400 Bad Request"),
        ("Un recurso fue movido permanentemente a otra URL", "301 Moved Permanently"),
    ]
    for i, (escenario, codigo) in enumerate(escenarios, 1):
        print(f"{i}. {escenario}")
        print(f"   Codigo: {codigo}")
        print()

def solucion_2():
    print("=" * 50)
    print("SOLUCION 2: Consultar codigos en httpbin")
    print("=" * 50)
    for codigo in [200, 301, 403, 500]:
        conn = http.client.HTTPSConnection("httpbin.org")
        conn.request("GET", f"/status/{codigo}")
        resp = conn.getresponse()
        print(f"{resp.status} {resp.reason}")
        conn.close()

def solucion_3():
    print("=" * 50)
    print("SOLUCION 3: Simular manejo de errores")
    print("=" * 50)
    mensajes = {
        200: "OK: Peticion exitosa",
        201: "CREATED: Recurso creado exitosamente",
        204: "NO CONTENT: Peticion exitosa sin contenido",
        301: "MOVED PERMANENTLY: Recurso movido permanentemente",
        400: "BAD REQUEST: Datos invalidos en la peticion",
        401: "UNAUTHORIZED: Autenticacion requerida",
        403: "FORBIDDEN: No tienes permisos para acceder",
        404: "NOT FOUND: Recurso no encontrado",
        500: "INTERNAL SERVER ERROR: Error interno del servidor",
        503: "SERVICE UNAVAILABLE: Servicio no disponible temporalmente",
    }
    print("Diccionario de codigos:")
    for codigo, mensaje in mensajes.items():
        print(f"  {codigo} -> {mensaje}")
    print()
    print("Funcion de ejemplo:")
    print("""
def manejar_respuesta(codigo):
    mensajes = {200: 'OK', 404: 'No encontrado', ...}
    if codigo in mensajes:
        print(mensajes[codigo])
    else:
        print('Codigo desconocido')
""")

def menu():
    print("SOLUCIONES - HTTP STATUS CODES")
    print("1 - Identificar codigos por escenario")
    print("2 - Consultar codigos en httpbin")
    print("3 - Simular manejo de errores")

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
