"""
SOLUCIONES - REST APIs
Ejecuta: python scripts/runner.py 5 4 [ejercicio] -s
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: Disenar endpoints REST para un blog")
    print("=" * 50)

    endpoints = {
        "posts": {
            "listar": "GET /api/posts",
            "obtener": "GET /api/posts/{id}",
            "crear": "POST /api/posts",
            "actualizar": "PUT /api/posts/{id}",
            "eliminar": "DELETE /api/posts/{id}"
        },
        "comments": {
            "listar": "GET /api/posts/{postId}/comments",
            "obtener": "GET /api/comments/{id}",
            "crear": "POST /api/posts/{postId}/comments",
            "actualizar": "PUT /api/comments/{id}",
            "eliminar": "DELETE /api/comments/{id}"
        },
        "users": {
            "listar": "GET /api/users",
            "obtener": "GET /api/users/{id}",
            "crear": "POST /api/users",
            "actualizar": "PUT /api/users/{id}",
            "eliminar": "DELETE /api/users/{id}"
        }
    }

    print("--- RESULTADO ---")
    for recurso, ops in endpoints.items():
        print(f"\n{recurso.upper()}:")
        for nombre, endpoint in ops.items():
            print(f"  {nombre}: {endpoint}")

    print()
    print("--- EXPLICACION ---")
    print("""
Convenciones REST:
  - Nombres en plural: /api/posts, NO /api/post
  - Anidacion para relaciones: /api/posts/{id}/comments
  - {id} es un parametro de ruta (path parameter)
  - GET no tiene body, POST/PUT pueden tenerlo
  - DELETE tipicamente responde 204 No Content

Para comments anidados:
  POST /api/posts/{postId}/comments
  El postId se pasa en la URL, los datos del comment en el body
""")


def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: Mapear CRUD a metodos HTTP")
    print("=" * 50)

    operaciones = [
        ("Obtener todos los posts", "GET", "/api/posts"),
        ("Crear un nuevo post", "POST", "/api/posts"),
        ("Obtener un post por ID", "GET", "/api/posts/{id}"),
        ("Actualizar un post completo", "PUT", "/api/posts/{id}"),
        ("Eliminar un post", "DELETE", "/api/posts/{id}"),
        ("Crear un comentario en un post", "POST", "/api/posts/{id}/comments"),
    ]

    print("--- RESULTADO ---")
    for desc, metodo, ruta in operaciones:
        print(f"  {metodo:7s} {ruta:35s} -> {desc}")

    print()
    print("--- EXPLICACION ---")
    print("""
Mapeo CRUD a metodos HTTP:

  Operacion      | HTTP  | Idempotente | Body?
  Leer           | GET   | Si          | No
  Crear          | POST  | No          | Si
  Reemplazar     | PUT   | Si          | Si
  Eliminar       | DELETE| Si          | No

Para crear un comentario en un post:
  POST /api/posts/{id}/comments
  El parentesco se refleja en la URL anidada.
""")


def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: Identificar endpoints idempotentes")
    print("=" * 50)

    endpoints = [
        ("GET /api/posts", True, "Solo lectura, no modifica estado"),
        ("POST /api/posts", False, "Crea un nuevo recurso cada vez"),
        ("PUT /api/posts/1", True, "Reemplaza el recurso, mismo resultado siempre"),
        ("DELETE /api/posts/1", True, "Eliminar algo ya eliminado no cambia el estado final"),
        ("PATCH /api/posts/1", False, "Modificacion parcial, el resultado puede variar"),
    ]

    print("--- RESULTADO ---")
    for endpoint, idempotente, razon in endpoints:
        marca = "SI" if idempotente else "NO"
        print(f"  {endpoint:30s} -> Idempotente: {marca}")
        print(f"  {'':30s}   ({razon})")
        print()

    print("--- EXPLICACION ---")
    print("""
La idempotencia es clave para la seguridad en APIs:

  Si un cliente no recibe respuesta, puede reenviar el request
  solo si el metodo es idempotente.

  Ejemplo: Pago con tarjeta
    - POST /api/pagos NO es idempotente
    - Si el cliente reenvia el POST, se cobra 2 veces
    - Solucion: usar un idempotency-key en el header

  Metodos seguros (no modifican estado): GET, HEAD, OPTIONS
  Metodos idempotentes: GET, PUT, DELETE, HEAD, OPTIONS
  Metodos NO idempotentes: POST, PATCH
""")


if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
