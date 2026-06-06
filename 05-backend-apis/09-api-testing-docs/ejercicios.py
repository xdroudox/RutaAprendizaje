"""
EJERCICIOS - API Testing y Documentacion
Ejecuta desde raiz: python scripts/runner.py 5 9 [ejercicio]

Niveles:
  🟢 Ej 1: Request GET con http.client
  🟡 Ej 2: Validar status code y body
  🔴 Ej 3: Documentacion OpenAPI (dict)

Pistas: python scripts/runner.py 5 9 N -p [1|2|3]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1(pista=0):
    """🟢 Request GET con http.client"""
    print(">> 🟢 EJERCICIO 1: Request GET con http.client")
    print("-" * 50)

    host = "jsonplaceholder.typicode.com"
    ruta = "/posts/1"

    print(f"Host: {host}")
    print(f"Ruta: {ruta}")

    if pista == 1:
        print("\n💡 Pista 1: Conecta y haz GET:")
        print("  conn = http.client.HTTPSConnection(host, timeout=5)")
        print("  conn.request('GET', ruta)")
        print("  resp = conn.getresponse()")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  resp = conn.getresponse()")
        print("  print(f'Status: {resp.status} {resp.reason}')")
        print("  body = resp.read().decode()")
        print("  print(f'Body: {body}')")
        print("  conn.close()")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Salida esperada:")
        print("  Status: 200 OK")
        print("  Body: {")
        print('    "userId": 1,')
        print('    "id": 1,')
        print('    "title": "..."',)
        print('    "body": "..."')
        print("  }")
        return

    print("\nConectate via HTTPS a la API publica JSONPlaceholder")
    print("y haz un GET a /posts/1. Imprime status code y body.")
    print("\n# ==== ESCRIBE TU CODIGO AQUI ====")


def ejercicio_2(pista=0):
    """🟡 Validar status code y body"""
    print(">> 🟡 EJERCICIO 2: Validar status code y body")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1: Despues del GET, valida:")
        print("  assert resp.status == 200, f'Esperado 200, obtenido {resp.status}'")
        print("  print('Status code 200: OK')")
        return
    elif pista == 2:
        print("\n💡 Pista 2: Valida campos del body:")
        print("  datos = json.loads(body)")
        print("  campos = ['id', 'title', 'body']")
        print("  for campo in campos:")
        print("      if campo in datos:")
        print("          print(f'Campo {campo}: {datos[campo]}')")
        print("      else:")
        print("          print(f'Campo {campo}: FALTANTE')")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Salida esperada:")
        print("  Status code 200: OK")
        print("  Campo 'id': 1")
        print("  Campo 'title': ...")
        print("  Campo 'body': ...")
        print("  Validacion completada.")
        return

    print("Usando la respuesta del ejercicio 1, valida que:")
    print("  1. Status code sea 200")
    print("  2. El body JSON tenga los campos: id, title, body")
    print("\n# ==== ESCRIBE TU CODIGO AQUI ====")


def ejercicio_3(pista=0):
    """🔴 Documentacion OpenAPI (dict)"""
    print(">> 🔴 EJERCICIO 3: Documentacion OpenAPI")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1: Estructura basica OpenAPI:")
        print("  openapi_doc = {")
        print("      'openapi': '3.0.0',")
        print("      'info': {")
        print("          'title': '...',")
        print("          'version': '1.0.0',")
        print("          'description': '...'")
        print("      },")
        print("      'paths': {")
        print("          '/api/usuarios': {")
        print("              'get': { ... },")
        print("              'post': { ... }")
        print("          }")
        print("      },")
        print("      'components': {")
        print("          'schemas': { ... }")
        print("      }")
        print("  }")
        return
    elif pista == 2:
        print("\n💡 Pista 2: Schema del endpoint GET:")
        print("  'get': {")
        print("      'summary': 'Listar todos los usuarios',")
        print("      'responses': {")
        print("          '200': {")
        print("              'description': 'Lista de usuarios',")
        print("              'content': {")
        print("                  'application/json': {")
        print("                      'schema': {")
        print("                          'type': 'array',")
        print("                          'items': {'$ref': '#/components/schemas/Usuario'}")
        print("                      }")
        print("                  }")
        print("              }")
        print("          }")
        print("      }")
        print("  }")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Schemas en components:")
        print("  'Usuario': {")
        print("      'type': 'object',")
        print("      'properties': {")
        print("          'id': {'type': 'integer'},")
        print("          'nombre': {'type': 'string'},")
        print("          'email': {'type': 'string'}")
        print("      }")
        print("  },")
        print("  'UsuarioInput': {")
        print("      'type': 'object',")
        print("      'properties': {")
        print("          'nombre': {'type': 'string'},")
        print("          'email': {'type': 'string'}")
        print("      },")
        print("      'required': ['nombre', 'email']")
        print("  }")
        return

    print("Crea un diccionario con la estructura OpenAPI 3.0")
    print("para una API de usuarios con 2 endpoints:")
    print("  - GET /api/usuarios → lista de usuarios")
    print("  - POST /api/usuarios → crear usuario")
    print()
    print("Incluye: openapi version, info, paths, components/schemas.")
    print("Luego imprimelo con json.dumps(indent=2).")
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
