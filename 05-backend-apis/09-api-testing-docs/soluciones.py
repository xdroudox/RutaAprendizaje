"""
SOLUCIONES - API Testing y Documentacion
Ejecuta desde raiz: python scripts/runner.py 5 9 1 -s
"""
import sys
import json
import http.client
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Construir request GET con http.client"""
    host = "jsonplaceholder.typicode.com"
    ruta = "/posts/1"
    conn = http.client.HTTPSConnection(host, timeout=5)
    conn.request("GET", ruta)
    resp = conn.getresponse()
    print(f"Status: {resp.status} {resp.reason}")
    body = resp.read().decode()
    print(f"Body: {body}")
    conn.close()

def ejercicio_2():
    """Validar status code y body de una response"""
    import json
    conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com", timeout=5)
    conn.request("GET", "/posts/1")
    resp = conn.getresponse()
    status = resp.status
    body = resp.read().decode()
    conn.close()
    assert status == 200, f"Status code esperado 200, obtenido {status}"
    print(f"Status code 200: OK")
    datos = json.loads(body)
    campos = ["id", "title", "body"]
    for campo in campos:
        if campo in datos:
            print(f"  Campo '{campo}': {datos[campo]}")
        else:
            print(f"  Campo '{campo}': FALTANTE")
    print("Validacion completada.")

def ejercicio_3():
    """Escribir documentacion OpenAPI simple (dict)"""
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
    print(json.dumps(openapi_doc, indent=2, ensure_ascii=False))

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
