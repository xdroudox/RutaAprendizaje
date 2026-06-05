"""
EJERCICIOS - REST APIs
Ejecuta desde raiz: python scripts/runner.py 5 4 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Disenar endpoints REST para un blog"""
    recursos = ["posts", "comments", "users"]
    # Para cada recurso, define el endpoint GET que lista todos
    # Ejemplo: GET /api/posts
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass

def ejercicio_2():
    """Mapear CRUD a metodos HTTP"""
    operaciones = [
        ("Obtener todos los posts", "GET", "/api/posts"),
        ("Crear un nuevo post", None, None),
        ("Obtener un post por ID", None, None),
        ("Actualizar un post completo", None, None),
        ("Eliminar un post", None, None),
        ("Crear un comentario en un post", None, None),
    ]
    for desc, metodo, ruta in operaciones:
        pass  # Completa los None con el metodo y ruta correctos
    # ==== ESCRIBE TU RESPUESTA AQUI ====

def ejercicio_3():
    """Identificar que endpoints son idempotentes"""
    endpoints = [
        ("GET /api/posts", None),
        ("POST /api/posts", None),
        ("PUT /api/posts/1", None),
        ("DELETE /api/posts/1", None),
        ("PATCH /api/posts/1", None),
    ]
    for endpoint, _ in endpoints:
        pass  # Marca True si es idempotente, False si no
    # ==== ESCRIBE TU RESPUESTA AQUI ====

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
