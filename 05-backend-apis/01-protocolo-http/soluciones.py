"""
SOLUCIONES - Protocolo HTTP
Ejecuta: python scripts/runner.py 5 1 [ejercicio] -s
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: Construir URL desde componentes")
    print("=" * 50)

    scheme = "https"
    host = "api.ejemplo.com"
    path = "/usuarios"
    params = {"rol": "admin", "edad": "25"}

    print("--- CODIGO ---")
    print("query = '&'.join(f'{k}={v}' for k, v in params.items())")
    print("url = f'{scheme}://{host}{path}?{query}'")
    print()

    query = "&".join(f"{k}={v}" for k, v in params.items())
    url = f"{scheme}://{host}{path}?{query}"

    print("--- RESULTADO ---")
    print(f"  URL: {url}")

    print()
    print("--- EXPLICACION ---")
    print("""
La URL se compone de:
  scheme://host/path?query_string

El query_string se construye uniendo los parametros con '&':
  rol=admin&edad=25

Nota: En Python, urllib.parse.urlencode() hace esto automaticamente:
  from urllib.parse import urlencode
  query = urlencode(params)
""")


def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: Simular request HTTP como diccionario")
    print("=" * 50)

    print("--- CODIGO ---")
    print("request = {")
    print("    'method': 'POST',")
    print("    'path': '/api/usuarios',")
    print("    'headers': {")
    print("        'Content-Type': 'application/json',")
    print("        'Authorization': 'Bearer token123'")
    print("    },")
    print("    'body': '{\"nombre\": \"Ana\", \"email\": \"ana@ejemplo.com\"}'")
    print("}")
    print("for k, v in request.items():")
    print("    print(f'{k}: {v}')")
    print()

    request = {
        "method": "POST",
        "path": "/api/usuarios",
        "headers": {
            "Content-Type": "application/json",
            "Authorization": "Bearer token123"
        },
        "body": '{"nombre": "Ana", "email": "ana@ejemplo.com"}'
    }

    print("--- RESULTADO ---")
    for k, v in request.items():
        print(f"  {k}: {v}")

    print()
    print("--- EXPLICACION ---")
    print("""
Un request HTTP real se ve asi en la red:

  POST /api/usuarios HTTP/1.1
  Host: api.ejemplo.com
  Content-Type: application/json
  Authorization: Bearer token123

  {"nombre": "Ana", "email": "ana@ejemplo.com"}

En Python, podriamos enviarlo con:
  import http.client
  conn = http.client.HTTPSConnection('api.ejemplo.com')
  conn.request('POST', '/api/usuarios', body=request['body'], headers=request['headers'])
""")


def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: Parsear response HTTP desde string")
    print("=" * 50)

    response_str = "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{\"id\": 1, \"nombre\": \"Ana\"}"

    print("--- CODIGO ---")
    print("linea_inicial, resto = response_str.split('\\\\r\\\\n', 1)")
    print("partes = linea_inicial.split(' ')")
    print("version = partes[0]")
    print("status_code = int(partes[1])")
    print("mensaje = partes[2]")
    print("encabezados, body = resto.split('\\\\r\\\\n\\\\r\\\\n', 1)")
    print("headers = {}")
    print("for linea in encabezados.split('\\\\r\\\\n'):")
    print("    if ': ' in linea:")
    print("        k, v = linea.split(': ', 1)")
    print("        headers[k] = v")
    print()

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

    print("--- RESULTADO ---")
    print(f"  Version: {version}")
    print(f"  Status: {status_code} {mensaje}")
    print(f"  Headers: {headers}")
    print(f"  Body: {body}")

    print()
    print("--- EXPLICACION ---")
    print("""
Estructura de un response HTTP:

  HTTP/version STATUS_CODE MENSAJE  ← linea inicial
  Header1: valor1                    ← headers
  Header2: valor2
                                     ← linea vacia (\\r\\n)
  {"datos": "..."}                   ← body

El split con maxsplit=1 separa solo la primera ocurrencia:
  - \\r\\n separa linea inicial del resto
  - \\r\\n\\r\\n separa headers del body (doble salto de linea)

En la practica se usa la libreria requests:
  import requests
  resp = requests.get('https://api.ejemplo.com/usuarios')
  print(resp.status_code, resp.json())
""")


if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
