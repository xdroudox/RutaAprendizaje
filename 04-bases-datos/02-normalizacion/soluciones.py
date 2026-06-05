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
    print("SOLUCION 1: Primera Forma Normal (1NF)")
    print("=" * 50)
    conn = get_db()
    conn.executescript("""
        CREATE TABLE ordenes (
            orden_id INTEGER PRIMARY KEY,
            cliente TEXT
        );
        CREATE TABLE detalle_orden (
            orden_id INTEGER,
            producto TEXT,
            FOREIGN KEY (orden_id) REFERENCES ordenes(orden_id)
        );
        INSERT INTO ordenes VALUES (1, 'Ana'), (2, 'Luis'), (3, 'Maria');
        INSERT INTO detalle_orden VALUES
            (1, 'Laptop'), (1, 'Mouse'),
            (2, 'Teclado'),
            (3, 'Monitor'), (3, 'Laptop'), (3, 'Mouse');
    """)
    query = """
        SELECT o.orden_id, o.cliente, d.producto
        FROM ordenes o
        JOIN detalle_orden d ON o.orden_id = d.orden_id;
    """
    print("Consulta ejecutada:")
    print(query.strip())
    print()
    mostrar_resultados(conn, query)

def solucion_2():
    print("=" * 50)
    print("SOLUCION 2: Tercera Forma Normal (3NF)")
    print("=" * 50)
    conn = get_db()
    conn.executescript("""
        CREATE TABLE departamentos (
            dept_id TEXT PRIMARY KEY,
            nombre TEXT,
            ciudad TEXT
        );
        INSERT INTO departamentos VALUES
            ('D1', 'Ventas', 'Madrid'),
            ('D2', 'TI', 'Barcelona');
        CREATE TABLE empleados (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            dept_id TEXT,
            FOREIGN KEY (dept_id) REFERENCES departamentos(dept_id)
        );
        INSERT INTO empleados VALUES
            (1, 'Ana', 'D1'),
            (2, 'Luis', 'D2'),
            (3, 'Pedro', 'D1');
    """)
    query = """
        SELECT e.id, e.nombre, d.nombre AS dept_nombre, d.ciudad
        FROM empleados e
        JOIN departamentos d ON e.dept_id = d.dept_id;
    """
    print("Consulta ejecutada:")
    print(query.strip())
    print()
    mostrar_resultados(conn, query)

def solucion_3():
    print("=" * 50)
    print("SOLUCION 3: Desnormalizacion")
    print("=" * 50)
    conn = get_db()
    conn.executescript("""
        CREATE TABLE pedidos_con_cliente (
            id INTEGER PRIMARY KEY,
            cliente_id INTEGER,
            cliente_nombre TEXT,
            fecha TEXT
        );
        INSERT INTO pedidos_con_cliente VALUES
            (1, 1, 'Ana', '2024-01-15'),
            (2, 2, 'Luis', '2024-01-16'),
            (3, 1, 'Ana', '2024-01-17');
    """)
    query = "SELECT * FROM pedidos_con_cliente;"
    print("Consulta ejecutada:")
    print(query)
    print()
    mostrar_resultados(conn, query)
    print()
    print("Nota: Hay redundancia (Ana aparece varias veces) pero")
    print("evitamos JOINs en consultas frecuentes.")

def menu():
    print("SOLUCIONES - NORMALIZACION")
    print("1 - Primera Forma Normal (1NF)")
    print("2 - Tercera Forma Normal (3NF)")
    print("3 - Desnormalizacion")

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
