"""
SOLUCIONES - REST APIs
Ejecuta desde raiz: python scripts/runner.py 5 4 1 -s
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Disenar endpoints REST para un blog"""
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
            "crear": "POST /api/posts/{postId}/comments",
            "eliminar": "DELETE /api/comments/{id}"
        },
        "users": {
            "listar": "GET /api/users",
            "obtener": "GET /api/users/{id}",
            "crear": "POST /api/users",
            "actualizar": "PUT /api/users/{id}"
        }
    }
    for recurso, ops in endpoints.items():
        print(f"\n{recurso.upper()}:")
        for nombre, endpoint in ops.items():
            print(f"  {nombre}: {endpoint}")

def ejercicio_2():
    """Mapear CRUD a metodos HTTP"""
    operaciones = [
        ("Obtener todos los posts", "GET", "/api/posts"),
        ("Crear un nuevo post", "POST", "/api/posts"),
        ("Obtener un post por ID", "GET", "/api/posts/{id}"),
        ("Actualizar un post completo", "PUT", "/api/posts/{id}"),
        ("Eliminar un post", "DELETE", "/api/posts/{id}"),
        ("Crear un comentario en un post", "POST", "/api/posts/{id}/comments"),
    ]
    for desc, metodo, ruta in operaciones:
        print(f"  {metodo:6s} {ruta:30s} -> {desc}")

def ejercicio_3():
    """Identificar que endpoints son idempotentes"""
    endpoints = [
        ("GET /api/posts", True, "Solo lectura, no modifica estado"),
        ("POST /api/posts", False, "Crea un nuevo recurso cada vez"),
        ("PUT /api/posts/1", True, "Reemplaza el recurso, mismo resultado siempre"),
        ("DELETE /api/posts/1", True, "Eliminar algo ya eliminado no cambia el estado"),
        ("PATCH /api/posts/1", False, "Modificacion parcial, resultado puede variar"),
    ]
    for endpoint, idempotente, razon in endpoints:
        marca = "SI" if idempotente else "NO"
        print(f"  {endpoint:25s} -> Idempotente: {marca} ({razon})")

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
