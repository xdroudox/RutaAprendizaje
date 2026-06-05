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
    print("EJERCICIO 1: Subconsulta en WHERE")
    print("=" * 50)
    conn = get_db()
    conn.executescript("""
        CREATE TABLE empleados (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            salario REAL,
            departamento TEXT
        );
        INSERT INTO empleados VALUES
            (1, 'Ana', 45000, 'Ventas'),
            (2, 'Luis', 52000, 'TI'),
            (3, 'Maria', 48000, 'Ventas'),
            (4, 'Carlos', 55000, 'TI'),
            (5, 'Sofia', 39000, 'RH');
    """)
    print("Tabla 'empleados' con 5 registros.")
    print()
    print("TAREA: Escribe una consulta que muestre los empleados")
    print("con salario mayor al salario promedio.")
    print()
    print("PISTA: WHERE salario > (SELECT AVG(salario) FROM empleados)")

def ejercicio_2():
    print("=" * 50)
    print("EJERCICIO 2: Subconsulta en SELECT y CTE")
    print("=" * 50)
    conn = get_db()
    conn.executescript("""
        CREATE TABLE clientes (
            id INTEGER PRIMARY KEY,
            nombre TEXT
        );
        INSERT INTO clientes VALUES (1, 'Ana'), (2, 'Luis'), (3, 'Maria');
        CREATE TABLE pedidos (
            id INTEGER PRIMARY KEY,
            cliente_id INTEGER,
            total REAL
        );
        INSERT INTO pedidos VALUES (1, 1, 150), (2, 1, 75), (3, 2, 200), (4, 3, 50);
    """)
    print("Tablas: clientes (3) y pedidos (4)")
    print()
    print("TAREA: Escribe un SELECT con subconsulta que muestre")
    print("cada cliente y el numero total de pedidos que ha hecho.")
    print()
    print("PISTA: SELECT nombre, (SELECT COUNT(*) FROM pedidos WHERE ...) AS pedidos FROM clientes;")

def ejercicio_3():
    print("=" * 50)
    print("EJERCICIO 3: VIEW")
    print("=" * 50)
    conn = get_db()
    conn.executescript("""
        CREATE TABLE productos (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            categoria TEXT,
            precio REAL
        );
        INSERT INTO productos VALUES
            (1, 'Laptop', 'Electronica', 1200),
            (2, 'Mouse', 'Electronica', 25),
            (3, 'Camisa', 'Ropa', 35),
            (4, 'Pantalon', 'Ropa', 50),
            (5, 'Tablet', 'Electronica', 300);
    """)
    print("Tabla 'productos' con 5 registros.")
    print()
    print("TAREA: Crea una VIEW llamada 'productos_electronica'")
    print("que contenga solo los productos de categoria 'Electronica'")
    print("con precio mayor a 100. Luego consultala.")
    print()
    print("PISTA: CREATE VIEW ... AS SELECT ... WHERE ...;")

pistas = {
    "1": "SELECT * FROM empleados WHERE salario > (SELECT AVG(salario) FROM empleados);",
    "2": "SELECT nombre, (SELECT COUNT(*) FROM pedidos WHERE pedidos.cliente_id = clientes.id) AS total_pedidos FROM clientes;",
    "3": "CREATE VIEW productos_electronica AS SELECT * FROM productos WHERE categoria = 'Electronica' AND precio > 100;\nSELECT * FROM productos_electronica;"
}

def menu():
    print("=" * 50)
    print("SUBCONSULTAS Y VISTAS - EJERCICIOS")
    print("=" * 50)
    print("1 - Subconsulta en WHERE")
    print("2 - Subconsulta en SELECT")
    print("3 - VIEW")
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
