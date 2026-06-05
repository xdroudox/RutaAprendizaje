import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    print("=" * 50)
    print("EJERCICIO 1: Documento vs Relacional")
    print("=" * 50)
    print("Dado el siguiente documento tipo MongoDB:")
    print()
    print('{')
    print('  "_id": 1,')
    print('  "nombre": "Ana",')
    print('  "direccion": { "ciudad": "Madrid", "cp": "28001" },')
    print('  "pedidos": [')
    print('    { "producto": "Laptop", "total": 1200 },')
    print('    { "producto": "Mouse", "total": 25 }')
    print('  ]')
    print('}')
    print()
    print("TAREA: Disena las tablas SQL equivalentes para representar")
    print("esta misma informacion en una base relacional.")
    print()
    print("PISTA: Necesitas al menos 2 tablas (usuarios y pedidos).")

def ejercicio_2():
    print("=" * 50)
    print("EJERCICIO 2: Filtrar documentos con Python dicts")
    print("=" * 50)
    print("Lista de documentos (diccionarios Python):")
    print()
    usuarios = [
        {"_id": 1, "nombre": "Ana", "edad": 25, "ciudad": "Madrid"},
        {"_id": 2, "nombre": "Luis", "edad": 30, "ciudad": "Barcelona"},
        {"_id": 3, "nombre": "Maria", "edad": 22, "ciudad": "Madrid"},
        {"_id": 4, "nombre": "Carlos", "edad": 35, "ciudad": "Valencia"},
    ]
    for u in usuarios:
        print(f"  {u}")
    print()
    print("TAREA: Escribe codigo Python (como si fuera una consulta")
    print("MongoDB) para filtrar los usuarios mayores de 25 anos")
    print("que viven en Madrid.")
    print()
    print("PISTA: [u for u in usuarios if u['edad'] > 25 and u['ciudad'] == 'Madrid']")

def ejercicio_3():
    print("=" * 50)
    print("EJERCICIO 3: Cuando usar SQL vs NoSQL")
    print("=" * 50)
    escenarios = [
        ("A", "Sistema bancario con transferencias entre cuentas."),
        ("B", "Catalogo de productos con campos variables segun el tipo."),
        ("C", "Red social con posts, comentarios, likes y amigos."),
    ]
    for letra, desc in escenarios:
        print(f"{letra}. {desc}")
    print()
    print("TAREA: Para cada escenario, decide si usarias SQL o NoSQL")
    print("y explica brevemente por que.")
    print()
    print("PISTA: A->SQL (ACID), B->NoSQL (esquema flexible),")
    print("  C->depende, pero NoSQL funciona bien para datos anidados.")

pistas = {
    "1": "Tabla usuarios: id, nombre, direccion_ciudad, direccion_cp\nTabla pedidos: id, usuario_id, producto, total\nCon FOREIGN KEY de usuario_id a usuarios(id)",
    "2": "resultado = [u for u in usuarios if u['edad'] > 25 and u['ciudad'] == 'Madrid']",
    "3": "A: SQL (requiere ACID, transacciones atomicas)\nB: NoSQL (esquema flexible, productos con atributos variables)\nC: NoSQL (datos anidados, relaciones de grafo)"
}

def menu():
    print("=" * 50)
    print("NOSQL INTRO - EJERCICIOS")
    print("=" * 50)
    print("1 - Documento vs Relacional")
    print("2 - Filtrar documentos Python")
    print("3 - Cuando usar SQL vs NoSQL")
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
