"""
EJERCICIOS - NoSQL Intro
Ejecuta desde raiz: python scripts/runner.py 4 7 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Modela un documento MongoDB para un usuario usando un dict anidado"""
    print("Crea un diccionario que represente un documento MongoDB para un usuario")
    print("Incluye: nombre, email, direccion (calle, ciudad, pais), intereses (lista)")
    print()
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    # usuario = {
    #     "nombre": "Ana Garcia",
    #     "email": "ana@email.com",
    #     "direccion": {
    #         "calle": "Calle Mayor 10",
    #         "ciudad": "Madrid",
    #         "pais": "Espana"
    #     },
    #     "intereses": ["lectura", "viajes", "fotografia"]
    # }
    # import json
    # print(json.dumps(usuario, indent=2, ensure_ascii=False))
    pass

def ejercicio_2():
    """Convierte un esquema SQL normalizado a un documento NoSQL (dict)"""
    print("=== Esquema SQL normalizado ===")
    print("Tabla: clientes (id, nombre, ciudad)")
    print("Tabla: pedidos (id, cliente_id, producto, total)")
    print()
    print("Convierte los pedidos de un cliente a un unico documento NoSQL")
    print("donde los pedidos sean un array anidado dentro del cliente")
    print()
    datos_sql = {
        "clientes": [
            {"id": 1, "nombre": "Ana", "ciudad": "Madrid"},
            {"id": 2, "nombre": "Juan", "ciudad": "Barcelona"}
        ],
        "pedidos": [
            {"id": 1, "cliente_id": 1, "producto": "Laptop", "total": 999.99},
            {"id": 2, "cliente_id": 1, "producto": "Mouse", "total": 25.50},
            {"id": 3, "cliente_id": 2, "producto": "Teclado", "total": 45.00}
        ]
    }
    print("Datos SQL:", datos_sql)
    print()
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    # Crea un documento NoSQL donde cada cliente incluya sus pedidos como array anidado
    # documento = {
    #     "cliente": { "nombre": "...", "ciudad": "..." },
    #     "pedidos": [ { "producto": "...", "total": ... }, ... ]
    # }
    pass

def ejercicio_3():
    """Compara casos de uso: cuando usar SQL vs NoSQL"""
    import random
    casos = [
        "Sistema bancario con transferencias entre cuentas",
        "Catalogo de productos con estructura variable",
        "Red social con posts, likes y comentarios",
        "Sistema de facturacion con totales exactos",
        "Blog con articulos y multiples autores",
        "Analitica en tiempo real de eventos de usuario",
        "Sistema de reservas de vuelos con integridad estricta",
        "Almacenamiento de sesiones de usuario con TTL"
    ]
    print("=== Clasifica cada caso como SQL o NoSQL ===")
    print()
    for i, caso in enumerate(casos, 1):
        print(f"  {i}. {caso}")
    print()
    print("Para cada caso, escribe: 'SQL' o 'NoSQL' y explica brevemente por que")
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    # analisis = {
    #     1: ("SQL", "Requiere ACID para transferencias exactas"),
    #     2: ("NoSQL", "Estructura flexible para diferentes tipos de producto"),
    #     ...
    # }
    # for num, (tipo, razon) in analisis.items():
    #     print(f"  {num}. {tipo:6s} - {razon}")
    pass

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            print(f">> EJERCICIO {num + 1}: {ejercicios[num].__doc__}")
            print("-" * 40)
            ejercicios[num]()
    else:
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
