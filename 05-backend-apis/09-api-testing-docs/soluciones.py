"""
SOLUCIONES - API Testing y Documentacion
Ejecuta: python scripts/runner.py 5 9 [ejercicio] -s
"""

import sys
import json
import http.client

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: Request GET con http.client")
    print("=" * 50)

    host = "jsonplaceholder.typicode.com"
    ruta = "/posts/1"

    print("--- CODIGO ---")
    print("conn = http.client.HTTPSConnection(host, timeout=5)")
    print("conn.request('GET', ruta)")
    print("resp = conn.getresponse()")
    print("print(f'Status: {resp.status} {resp.reason}')")
    print("print(f'Body: {resp.read().decode()}')")
    print("conn.close()")
    print()

    conn = http.client.HTTPSConnection(host, timeout=5)
    conn.request("GET", ruta)
    resp = conn.getresponse()
    body = resp.read().decode()

    print("--- RESULTADO ---")
    print(f"  Status: {resp.status} {resp.reason}")
    datos = json.loads(body)
    print(f"  Body: {json.dumps(datos, indent=2, ensure_ascii=False)}")
    conn.close()

    print()
    print("--- EXPLICACION ---")
    print("""
http.client es el modulo nativo de Python para HTTP.
Pasos para hacer un request GET:

  1. Crear conexion: HTTPSConnection(host, timeout)
  2. Enviar request: conn.request('GET', ruta)
  3. Obtener respuesta: resp = conn.getresponse()
  4. Leer body: resp.read().decode()
  5. Cerrar: conn.close()

En la practica se usa la libreria 'requests' (mas simple):
  import requests
  resp = requests.get('https://jsonplaceholder.typicode.com/posts/1')
  print(resp.status_code, resp.json())
""")


def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: Validar status code y body")
    print("=" * 50)

    host = "jsonplaceholder.typicode.com"
    ruta = "/posts/1"

    print("--- CODIGO ---")
    print("conn = http.client.HTTPSConnection(host, timeout=5)")
    print("conn.request('GET', ruta)")
    print("resp = conn.getresponse()")
    print("status = resp.status")
    print("body = resp.read().decode()")
    print("conn.close()")
    print("assert status == 200")
    print("datos = json.loads(body)")
    print("for campo in ['id', 'title', 'body']:")
    print("    print(f'{campo}: {datos.get(campo)}')")
    print()

    conn = http.client.HTTPSConnection(host, timeout=5)
    conn.request("GET", ruta)
    resp = conn.getresponse()
    status = resp.status
    body = resp.read().decode()
    conn.close()

    print("--- RESULTADO ---")
    if status == 200:
        print("  Status code 200: OK")
    else:
        print(f"  Status code: {status} (esperado 200)")

    datos = json.loads(body)
    campos = ["id", "title", "body"]
    for campo in campos:
        if campo in datos:
            print(f"  Campo '{campo}': {datos[campo]}")
        else:
            print(f"  Campo '{campo}': FALTANTE")
    print("  Validacion completada.")

    print()
    print("--- EXPLICACION ---")
    print("""
Validacion de respuestas API:

  1. Verificar status code (assert o if)
  2. Verificar estructura del body (campos esperados)
  3. Verificar tipos de datos (opcional)

En testing profesional se usan librerias como:
  - pytest + requests (Pruebas de API)
  - pydantic (validacion de schemas)
  - schemathesis (testing basado en OpenAPI)
""")


def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: Documentacion OpenAPI")
    print("=" * 50)

    openapi_doc = {
        "openapi": "3.0.0",
        "info": {
            "title": "API de Usuarios",
            "version": "1.0.0",
            "description": "API para gestionar usuarios"
        },
        "paths": {
            "/api/usuarios": {
                "get": {
                    "summary": "Listar todos los usuarios",
                    "responses": {
                        "200": {
                            "description": "Lista de usuarios",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "array",
                                        "items": {"$ref": "#/components/schemas/Usuario"}
                                    }
                                }
                            }
                        }
                    }
                },
                "post": {
                    "summary": "Crear un nuevo usuario",
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/UsuarioInput"}
                            }
                        }
                    },
                    "responses": {
                        "201": {"description": "Usuario creado exitosamente"},
                        "400": {"description": "Datos invalidos"}
                    }
                }
            }
        },
        "components": {
            "schemas": {
                "Usuario": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "nombre": {"type": "string"},
                        "email": {"type": "string"}
                    }
                },
                "UsuarioInput": {
                    "type": "object",
                    "properties": {
                        "nombre": {"type": "string"},
                        "email": {"type": "string"}
                    },
                    "required": ["nombre", "email"]
                }
            }
        }
    }

    print("--- RESULTADO ---")
    print(json.dumps(openapi_doc, indent=2, ensure_ascii=False))

    print()
    print("--- EXPLICACION ---")
    print("""
OpenAPI 3.0 estructura:

  openapi: version del estandar (3.0.0)
  info: metadatos de la API (titulo, version, descripcion)
  paths: endpoints disponibles con sus metodos
  components/schemas: definiciones reutilizables de datos

Cada path puede tener:
  - get, post, put, delete, patch, etc.
  - summary: descripcion breve
  - requestBody: schema de entrada (POST/PUT)
  - responses: codigos de respuesta con schemas

Ventajas de OpenAPI:
  - Generar documentacion visual (Swagger UI)
  - Generar clientes SDK automaticamente
  - Validar requests/responses automaticamente
  - Mantener la documentacion sincronizada con el codigo
""")


if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
