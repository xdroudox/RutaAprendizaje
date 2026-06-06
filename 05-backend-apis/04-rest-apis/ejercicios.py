"""
EJERCICIOS - REST APIs
Ejecuta desde raiz: python scripts/runner.py 5 4 [ejercicio]

Niveles:
  🟢 Ej 1: Disenar endpoints REST para un blog
  🟡 Ej 2: Mapear CRUD a metodos HTTP
  🔴 Ej 3: Identificar endpoints idempotentes

Pistas: python scripts/runner.py 5 4 N -p [1|2|3]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1(pista=0):
    """🟢 Disenar endpoints REST para un blog"""
    print(">> 🟢 EJERCICIO 1: Disenar endpoints REST para un blog")
    print("-" * 50)

    recursos = ["posts", "comments", "users"]

    print("Recursos del blog:")
    for r in recursos:
        print(f"  - {r}")

    if pista == 1:
        print("\n💡 Pista 1: Cada recurso necesita estos endpoints:")
        print("  GET /api/{recurso}     → listar todos")
        print("  GET /api/{recurso}/1   → obtener por ID")
        print("  POST /api/{recurso}    → crear")
        print("  PUT /api/{recurso}/1   → actualizar")
        print("  DELETE /api/{recurso}/1 → eliminar")
        print()
        print("  Para posts con comments anidados:")
        print("  GET /api/posts/1/comments")
        return
    elif pista == 2:
        print("\n💡 Pista 2: Estructura del diccionario:")
        print("  endpoints = {")
        print("      'posts': {")
        print("          'listar': 'GET /api/posts',")
        print("          'obtener': 'GET /api/posts/{id}',")
        print("          'crear': 'POST /api/posts',")
        print("          ...")
        print("      },")
        print("      ...")
        print("  }")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Endpoints esperados (parcial):")
        print("  POSTS:")
        print("    listar:     GET /api/posts")
        print("    obtener:    GET /api/posts/{id}")
        print("    crear:      POST /api/posts")
        print("    actualizar: PUT /api/posts/{id}")
        print("    eliminar:   DELETE /api/posts/{id}")
        print("  COMMENTS:")
        print("    listar:     GET /api/posts/{postId}/comments")
        print("    crear:      POST /api/posts/{postId}/comments")
        print("  USERS:")
        print("    ...")
        return

    print("\nDefine los endpoints REST para cada recurso del blog.")
    print("Para cada recurso: listar, obtener, crear, actualizar, eliminar.")
    print("Considera que comments estan anidados dentro de posts.")
    print("\n# ==== ESCRIBE TU CODIGO AQUI ====")


def ejercicio_2(pista=0):
    """🟡 Mapear CRUD a metodos HTTP"""
    print(">> 🟡 EJERCICIO 2: Mapear CRUD a metodos HTTP")
    print("-" * 50)

    operaciones = [
        ("Obtener todos los posts", "GET", "/api/posts"),
        ("Crear un nuevo post", None, None),
        ("Obtener un post por ID", None, None),
        ("Actualizar un post completo", None, None),
        ("Eliminar un post", None, None),
        ("Crear un comentario en un post", None, None),
    ]

    print("Completa los metodos y rutas faltantes:")
    for desc, metodo, ruta in operaciones:
        print(f"  {desc:45s} {str(metodo or '?'):7s} {str(ruta or '?'):30s}")

    if pista == 1:
        print("\n💡 Pista 1: Reglas de mapeo CRUD:")
        print("  Obtener todos → GET /api/posts")
        print("  Crear nuevo   → POST /api/posts")
        print("  Obtener por ID → GET /api/posts/{id}")
        print("  Actualizar    → PUT /api/posts/{id}")
        print("  Eliminar      → DELETE /api/posts/{id}")
        return
    elif pista == 2:
        print("\n💡 Pista 2: Para crear comentario en un post:")
        print("  POST /api/posts/{id}/comments")
        print("  (El comentario pertenece al post, por eso va anidado)")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Resultado completo:")
        print("  Obtener todos los posts          GET    /api/posts")
        print("  Crear un nuevo post              POST   /api/posts")
        print("  Obtener un post por ID           GET    /api/posts/{id}")
        print("  Actualizar un post completo      PUT    /api/posts/{id}")
        print("  Eliminar un post                 DELETE /api/posts/{id}")
        print("  Crear comentario en post         POST   /api/posts/{id}/comments")
        return

    print("\nAsigna el metodo HTTP y la ruta correcta a cada operacion.")
    print("Usa una lista de tuplas (descripcion, metodo, ruta).")
    print("\n# ==== ESCRIBE TU CODIGO AQUI ====")


def ejercicio_3(pista=0):
    """🔴 Identificar endpoints idempotentes"""
    print(">> 🔴 EJERCICIO 3: Identificar endpoints idempotentes")
    print("-" * 50)

    endpoints = [
        ("GET /api/posts", None),
        ("POST /api/posts", None),
        ("PUT /api/posts/1", None),
        ("DELETE /api/posts/1", None),
        ("PATCH /api/posts/1", None),
    ]

    print("Determina si cada endpoint es idempotente:")
    for endpoint, _ in endpoints:
        print(f"  {endpoint:30s} -> ?")

    if pista == 1:
        print("\n💡 Pista 1: Reglas de idempotencia:")
        print("  GET    → Si (solo lectura)")
        print("  PUT    → Si (reemplaza, mismo resultado siempre)")
        print("  DELETE → Si (eliminar algo ya eliminado no cambia nada)")
        print("  POST   → No (crea nuevo recurso cada vez)")
        print("  PATCH  → No (modificacion parcial, resultado puede variar)")
        return
    elif pista == 2:
        print("\n💡 Pista 2: Piensa en cada caso:")
        print("  GET /api/posts → haces GET 10 veces → mismo resultado")
        print("  POST /api/posts → haces POST 10 veces → 10 recursos nuevos")
        print("  PUT /api/posts/1 → haces PUT 10 veces → mismo estado final")
        print("  DELETE /api/posts/1 → 1ra vez elimina, 2da vez no hay nada que eliminar")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Resultado esperado:")
        print("  GET /api/posts         → Idempotente: SI  (solo lectura)")
        print("  POST /api/posts        → Idempotente: NO  (crea cada vez)")
        print("  PUT /api/posts/1       → Idempotente: SI  (reemplaza)")
        print("  DELETE /api/posts/1    → Idempotente: SI  (estado final es el mismo)")
        print("  PATCH /api/posts/1     → Idempotente: NO  (modifica parcialmente)")
        return

    print("\nPara cada endpoint, indica si es idempotente (True/False)")
    print("y explica brevemente por que.")
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
