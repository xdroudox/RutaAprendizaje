import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    print("=" * 50)
    print("EJERCICIO 1: Disenar endpoints REST")
    print("=" * 50)
    print()
    print("TAREA: Para un sistema de biblioteca, disena los endpoints REST")
    print("adecuados para las siguientes operaciones:")
    print()
    print("  1. Obtener todos los libros")
    print("  2. Obtener un libro por ID")
    print("  3. Agregar un libro nuevo")
    print("  4. Actualizar toda la informacion de un libro")
    print("  5. Eliminar un libro")
    print("  6. Obtener todos los prestamos de un usuario")
    print()
    print("Escribe el metodo HTTP y la URL para cada operacion.")
    print()
    print("PISTA: GET /libros, GET /libros/{id}, POST /libros, ...")

def ejercicio_2():
    print("=" * 50)
    print("EJERCICIO 2: Determinar idempotencia")
    print("=" * 50)
    print()
    print("TAREA: Para cada operacion, indica si es idempotente (SI/NO)")
    print("y explica por que.")
    print()
    operaciones = [
        "GET /api/usuarios",
        "POST /api/usuarios",
        "PUT /api/usuarios/5",
        "DELETE /api/usuarios/5",
        "PATCH /api/usuarios/5",
        "GET /api/usuarios/5",
    ]
    for i, op in enumerate(operaciones, 1):
        print(f"  {i}. {op}")
    print()
    print("PISTA: PUT, DELETE y GET son idempotentes. POST no. PATCH depende.")

def ejercicio_3():
    print("=" * 50)
    print("EJERCICIO 3: Simular una API REST")
    print("=" * 50)
    print()
    print("TAREA: Completa la funcion manejar_peticion(metodo, ruta, datos)")
    print("que simula una API REST de productos.")
    print()
    productos = [
        {"id": 1, "nombre": "Laptop", "precio": 1200},
        {"id": 2, "nombre": "Mouse", "precio": 25},
    ]
    print("Productos iniciales:", productos)
    print()
    print("Implementa:")
    print("  GET /productos -> lista todos")
    print("  GET /productos/1 -> muestra producto con id=1")
    print("  POST /productos -> agrega nuevo producto (datos del cuerpo)")
    print("  DELETE /productos/1 -> elimina producto")
    print()
    print("PISTA: Usa condicionales para metodo y ruta.")

pistas = {
    "1": "GET /libros, GET /libros/{id}, POST /libros, PUT /libros/{id}, DELETE /libros/{id}, GET /usuarios/{id}/prestamos",
    "2": "1-SI (solo lectura), 2-NO (crea cada vez), 3-SI (mismo estado siempre), 4-SI (borrado afecta una vez), 5-PODRIA NO SER (depende de la implementacion), 6-SI (solo lectura)",
    "3": "if metodo == 'GET' and ruta == '/productos': print(productos); elif metodo == 'GET' and ruta.startswith('/productos/'): id = int(ruta.split('/')[2]); print([p for p in productos if p['id'] == id])"
}

def menu():
    print("=" * 50)
    print("REST APIS - EJERCICIOS")
    print("=" * 50)
    print("1 - Disenar endpoints REST")
    print("2 - Determinar idempotencia")
    print("3 - Simular una API REST")
    print()
    print("Usa: python ejercicios.py <numero>")
    print("     python ejercicios.py <numero> -p  (pista)")

def main():
    args = sys.argv[1:]
    if not args:
        menu()
        return
    num = args[0]
    mostrar_pista = "-p" in args
    if mostrar_pista and num in pistas:
        print("=== PISTA ===")
        print(pistas[num])
        print()
    if num == "1":
        ejercicio_1()
    elif num == "2":
        ejercicio_2()
    elif num == "3":
        ejercicio_3()
    else:
        print("Ejercicio no valido. Usa 1, 2 o 3.")

if __name__ == "__main__":
    main()
