"""
SOLUCIONES - Protocolo HTTP
Ejecuta desde raiz: python scripts/runner.py 5 1 1 -s
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Crear una URL a partir de componentes"""
    scheme = "https"
    host = "api.ejemplo.com"
    path = "/usuarios"
    params = {"rol": "admin", "edad": "25"}
    query = "&".join(f"{k}={v}" for k, v in params.items())
    url = f"{scheme}://{host}{path}?{query}"
    print(f"URL construida: {url}")

def ejercicio_2():
    """Simular request HTTP como diccionario"""
    request = {
        "method": "POST",
        "path": "/api/usuarios",
        "headers": {
            "Content-Type": "application/json",
            "Authorization": "Bearer token123"
        },
        "body": '{"nombre": "Ana", "email": "ana@ejemplo.com"}'
    }
    print("Request HTTP:")
    for k, v in request.items():
        print(f"  {k}: {v}")

def ejercicio_3():
    """Parsear response HTTP desde string"""
    response_str = "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{\"id\": 1, \"nombre\": \"Ana\"}"
    linea_inicial, resto = response_str.split("\r\n", 1)
    partes = linea_inicial.split(" ")
    version = partes[0]
    status_code = int(partes[1])
    mensaje = partes[2]
    encabezados, body = resto.split("\r\n\r\n", 1)
    headers = {}
    for linea in encabezados.split("\r\n"):
        if ": " in linea:
            k, v = linea.split(": ", 1)
            headers[k] = v
    print(f"Status: {status_code} {mensaje}")
    print(f"Headers: {headers}")
    print(f"Body: {body}")

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
