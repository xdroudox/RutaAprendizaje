import sys, sqlite3

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def get_db():
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    return conn

def ejercicio_1():
    print("=" * 50)
    print("EJERCICIO 1: Primera Forma Normal (1NF)")
    print("=" * 50)
    print("Tabla no normalizada (viola 1NF):")
    print("| orden_id | cliente | productos                |")
    print("|----------|---------|--------------------------|")
    print("| 1        | Ana     | Laptop, Mouse            |")
    print("| 2        | Luis    | Teclado                  |")
    print("| 3        | Maria   | Monitor, Laptop, Mouse   |")
    print()
    print("TAREA: Escribe CREATE TABLE para la version 1NF")
    print("donde cada producto este en una fila separada.")
    print("Crea tambien la tabla 'ordenes' con orden_id y cliente.")
    print()
    print("Ejecuta esta consulta:")
    print("  SELECT o.orden_id, o.cliente, d.producto")
    print("  FROM ordenes o JOIN detalle_orden d ON o.orden_id = d.orden_id;")
    print()
    print("PISTA: Usa dos tablas: ordenes(orden_id, cliente)")
    print("y detalle_orden(orden_id, producto)")

def ejercicio_2():
    print("=" * 50)
    print("EJERCICIO 2: Tercera Forma Normal (3NF)")
    print("=" * 50)
    print("Tabla no normalizada (viola 3NF):")
    print("| emp_id | nombre | dept_id | dept_nombre | dept_ciudad |")
    print("|--------|--------|---------|-------------|-------------|")
    print("| 1      | Ana    | D1      | Ventas      | Madrid      |")
    print("| 2      | Luis   | D2      | TI          | Barcelona   |")
    print("| 3      | Pedro  | D1      | Ventas      | Madrid      |")
    print()
    print("TAREA: disena dos tablas en 3NF separando empleados de departamentos.")
    print()
    print("PISTA: Crea 'departamentos' y 'empleados' con FK a departamentos.")

def ejercicio_3():
    print("=" * 50)
    print("EJERCICIO 3: Desnormalizacion")
    print("=" * 50)
    print("Tablas normalizadas:")
    print("pedidos(id, cliente_id, fecha)")
    print("clientes(id, nombre, email)")
    print()
    print("TAREA: disena una tabla desnormalizada 'pedidos_con_cliente'")
    print("que incluya el nombre del cliente directamente en la tabla")
    print("de pedidos para evitar JOINs frecuentes.")
    print()
    print("PISTA: CREATE TABLE pedidos_con_cliente (id INTEGER, cliente_id INTEGER,")
    print("  cliente_nombre TEXT, fecha TEXT);")

pistas = {
    "1": "CREATE TABLE ordenes (orden_id INTEGER PRIMARY KEY, cliente TEXT);\nCREATE TABLE detalle_orden (orden_id INTEGER, producto TEXT, FOREIGN KEY (orden_id) REFERENCES ordenes(orden_id));\nINSERT INTO ordenes VALUES (1,'Ana'),(2,'Luis'),(3,'Maria');\nINSERT INTO detalle_orden VALUES (1,'Laptop'),(1,'Mouse'),(2,'Teclado'),(3,'Monitor'),(3,'Laptop'),(3,'Mouse');",
    "2": "CREATE TABLE departamentos (dept_id TEXT PRIMARY KEY, nombre TEXT, ciudad TEXT);\nINSERT INTO departamentos VALUES ('D1','Ventas','Madrid'),('D2','TI','Barcelona');\nCREATE TABLE empleados (id INTEGER PRIMARY KEY, nombre TEXT, dept_id TEXT, FOREIGN KEY (dept_id) REFERENCES departamentos(dept_id));\nINSERT INTO empleados VALUES (1,'Ana','D1'),(2,'Luis','D2'),(3,'Pedro','D1');",
    "3": "CREATE TABLE pedidos_con_cliente (id INTEGER PRIMARY KEY, cliente_id INTEGER, cliente_nombre TEXT, fecha TEXT);\nINSERT INTO pedidos_con_cliente VALUES (1,1,'Ana','2024-01-15'),(2,2,'Luis','2024-01-16');"
}

def menu():
    print("=" * 50)
    print("NORMALIZACION - EJERCICIOS")
    print("=" * 50)
    print("1 - Primera Forma Normal (1NF)")
    print("2 - Tercera Forma Normal (3NF)")
    print("3 - Desnormalizacion")
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
