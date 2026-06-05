import sys, sqlite3

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def get_db():
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    return conn

def mostrar_resultados(conn, query):
    try:
        cur = conn.execute(query)
        filas = cur.fetchall()
        if not filas:
            print("(Sin resultados)")
            return
        headers = [d[0] for d in cur.description]
        print(" | ".join(h for h in headers))
        print("-" * 40)
        for f in filas:
            print(" | ".join(str(f[h]) for h in headers))
    except Exception as e:
        print("ERROR:", e)

def solucion_1():
    print("=" * 50)
    print("SOLUCION 1: Subconsulta en WHERE")
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
    query = "SELECT * FROM empleados WHERE salario > (SELECT AVG(salario) FROM empleados);"
    print("Consulta ejecutada:")
    print(query)
    print()
    mostrar_resultados(conn, query)
    print()
    cur = conn.execute("SELECT AVG(salario) FROM empleados;")
    avg = cur.fetchone()[0]
    print(f"Salario promedio: {avg:.2f}")

def solucion_2():
    print("=" * 50)
    print("SOLUCION 2: Subconsulta en SELECT")
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
    query = """
        SELECT nombre,
            (SELECT COUNT(*) FROM pedidos WHERE pedidos.cliente_id = clientes.id) AS total_pedidos
        FROM clientes;
    """
    print("Consulta ejecutada:")
    print(query.strip())
    print()
    mostrar_resultados(conn, query)

def solucion_3():
    print("=" * 50)
    print("SOLUCION 3: VIEW")
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
        CREATE VIEW productos_electronica AS
            SELECT * FROM productos
            WHERE categoria = 'Electronica' AND precio > 100;
    """)
    query = "SELECT * FROM productos_electronica;"
    print("VIEW creada. Consulta ejecutada:")
    print(query)
    print()
    mostrar_resultados(conn, query)

def menu():
    print("SOLUCIONES - SUBCONSULTAS Y VISTAS")
    print("1 - Subconsulta en WHERE")
    print("2 - Subconsulta en SELECT")
    print("3 - VIEW")

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
