import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

productos = [
    {"id": 1, "nombre": "Laptop", "precio": 1200},
    {"id": 2, "nombre": "Mouse", "precio": 25},
]

def manejar_peticion(metodo, ruta, datos=None):
    if metodo == "GET" and ruta == "/productos":
        print("Listando productos:")
        for p in productos:
            print(f"  [{p['id']}] {p['nombre']} - ${p['precio']}")
    elif metodo == "GET" and ruta.startswith("/productos/"):
        pid = int(ruta.split("/")[2])
        prod = [p for p in productos if p["id"] == pid]
        if prod:
            p = prod[0]
            print(f"  [{p['id']}] {p['nombre']} - ${p['precio']}")
        else:
            print("  Producto no encontrado")
    elif metodo == "POST" and ruta == "/productos":
        if datos:
            nuevo_id = max(p["id"] for p in productos) + 1
            datos["id"] = nuevo_id
            productos.append(datos)
            print(f"  Producto creado con id={nuevo_id}")
    elif metodo == "DELETE" and ruta.startswith("/productos/"):
        pid = int(ruta.split("/")[2])
        global productos
        productos = [p for p in productos if p["id"] != pid]
        print(f"  Producto con id={pid} eliminado")
    else:
        print("  Ruta no encontrada")

def solucion_1():
    print("=" * 50)
    print("SOLUCION 1: Disenar endpoints REST")
    print("=" * 50)
    endpoints = [
        ("Obtener todos los libros", "GET", "/libros"),
        ("Obtener un libro por ID", "GET", "/libros/{id}"),
        ("Agregar un libro nuevo", "POST", "/libros"),
        ("Actualizar libro completo", "PUT", "/libros/{id}"),
        ("Eliminar un libro", "DELETE", "/libros/{id}"),
        ("Prestamos de un usuario", "GET", "/usuarios/{id}/prestamos"),
    ]
    for desc, metodo, url in endpoints:
        print(f"  {metodo:6s} {url:25s} -> {desc}")

def solucion_2():
    print("=" * 50)
    print("SOLUCION 2: Determinar idempotencia")
    print("=" * 50)
    resultados = [
        ("GET /api/usuarios", "SI", "Solo lectura, no modifica estado"),
        ("POST /api/usuarios", "NO", "Crea un nuevo recurso cada vez"),
        ("PUT /api/usuarios/5", "SI", "Mismo cuerpo produce mismo estado final"),
        ("DELETE /api/usuarios/5", "SI", "Tras borrar, el estado es el mismo"),
        ("PATCH /api/usuarios/5", "NO", "Puede incrementar un contador, etc."),
        ("GET /api/usuarios/5", "SI", "Solo lectura, no modifica estado"),
    ]
    for op, idemp, razon in resultados:
        print(f"  {op:30s} | Idempotente: {idemp} | {razon}")

def solucion_3():
    print("=" * 50)
    print("SOLUCION 3: Simular una API REST")
    print("=" * 50)
    print("Probando la API REST simulada:")
    print()
    manejar_peticion("GET", "/productos")
    print()
    manejar_peticion("GET", "/productos/1")
    print()
    manejar_peticion("POST", "/productos", {"nombre": "Teclado", "precio": 45})
    print()
    manejar_peticion("GET", "/productos")
    print()
    manejar_peticion("DELETE", "/productos/1")
    print()
    manejar_peticion("GET", "/productos")

def menu():
    print("SOLUCIONES - REST APIS")
    print("1 - Disenar endpoints REST")
    print("2 - Determinar idempotencia")
    print("3 - Simular una API REST")

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
