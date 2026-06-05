import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    print("=" * 50)
    print("SOLUCION 1: Documento vs Relacional")
    print("=" * 50)
    print("Modelo relacional equivalente:")
    print()
    print("Tabla: usuarios")
    print("| id | nombre | direccion_ciudad | direccion_cp |")
    print("|----|--------|------------------|--------------|")
    print("| 1  | Ana    | Madrid           | 28001        |")
    print()
    print("Tabla: pedidos")
    print("| id | usuario_id | producto | total |")
    print("|----|------------|----------|-------|")
    print("| 1  | 1          | Laptop   | 1200  |")
    print("| 2  | 1          | Mouse    | 25    |")
    print()
    print("En MongoDB los datos anidados van en un solo documento.")
    print("En SQL se separan en tablas normalizadas con JOINs.")

def solucion_2():
    print("=" * 50)
    print("SOLUCION 2: Filtrar documentos Python")
    print("=" * 50)
    usuarios = [
        {"_id": 1, "nombre": "Ana", "edad": 25, "ciudad": "Madrid"},
        {"_id": 2, "nombre": "Luis", "edad": 30, "ciudad": "Barcelona"},
        {"_id": 3, "nombre": "Maria", "edad": 22, "ciudad": "Madrid"},
        {"_id": 4, "nombre": "Carlos", "edad": 35, "ciudad": "Valencia"},
    ]
    query = [u for u in usuarios if u["edad"] > 25 and u["ciudad"] == "Madrid"]
    print("Consulta: usuarios donde edad > 25 AND ciudad = 'Madrid'")
    print()
    print("Resultado:")
    for u in query:
        print(f"  {u}")
    if not query:
        print("  (Sin resultados)")
    print()
    print("Equivalente SQL: SELECT * FROM usuarios WHERE edad > 25 AND ciudad = 'Madrid';")

def solucion_3():
    print("=" * 50)
    print("SOLUCION 3: Cuando usar SQL vs NoSQL")
    print("=" * 50)
    print()
    print("A. Sistema bancario con transferencias entre cuentas.")
    print("   -> SQL. Requiere ACID: atomicidad en transferencias,")
    print("      consistencia en saldos, aislamiento entre operaciones")
    print("      y durabilidad. Es el caso classico para SQL relacional.")
    print()
    print("B. Catalogo de productos con campos variables")
    print("   -> NoSQL. Cada tipo de producto tiene atributos distintos")
    print("      (ej. laptop tiene 'ram', camisa tiene 'talla').")
    print("      MongoDB permite documentos con esquema flexible.")
    print("      En SQL se necesitarian tablas EAV (entity-attribute-value)")
    print("      que son complejas de consultar.")
    print()
    print("C. Red social con posts, comentarios, likes y amigos.")
    print("   -> NoSQL (o hibrido). Los datos son jerarquicos:")
    print("      un post con sus comentarios anidados, un usuario con")
    print("      su lista de amigos. MongoDB modela esto naturalmente.")
    print("      SQL tambien funciona pero requiere mas JOINs.")

def menu():
    print("SOLUCIONES - NOSQL INTRO")
    print("1 - Documento vs Relacional")
    print("2 - Filtrar documentos Python")
    print("3 - Cuando usar SQL vs NoSQL")

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
