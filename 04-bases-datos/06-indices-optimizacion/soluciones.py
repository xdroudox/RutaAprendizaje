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
    print("SOLUCION 1: CREATE INDEX y EXPLAIN")
    print("=" * 50)
    conn = get_db()
    conn.executescript("""
        CREATE TABLE ventas (
            id INTEGER PRIMARY KEY,
            producto TEXT,
            cantidad INTEGER,
            total REAL
        );
        INSERT INTO ventas VALUES (1, 'Laptop', 2, 2400.00);
        INSERT INTO ventas VALUES (2, 'Mouse', 10, 250.00);
        INSERT INTO ventas VALUES (3, 'Monitor', 3, 900.00);
        INSERT INTO ventas VALUES (4, 'Laptop', 1, 1200.00);
        INSERT INTO ventas VALUES (5, 'Teclado', 5, 225.00);
    """)
    print("SIN INDICE:")
    cur = conn.execute("EXPLAIN QUERY PLAN SELECT * FROM ventas WHERE producto = 'Laptop';")
    for f in cur.fetchall():
        print(f["detail"])
    print()
    conn.execute("CREATE INDEX idx_producto ON ventas(producto);")
    print("CON INDICE:")
    cur = conn.execute("EXPLAIN QUERY PLAN SELECT * FROM ventas WHERE producto = 'Laptop';")
    for f in cur.fetchall():
        print(f["detail"])

def solucion_2():
    print("=" * 50)
    print("SOLUCION 2: Indices compuestos")
    print("=" * 50)
    conn = get_db()
    conn.executescript("""
        CREATE TABLE pedidos (
            id INTEGER PRIMARY KEY,
            cliente_id INTEGER,
            fecha TEXT,
            total REAL
        );
        INSERT INTO pedidos VALUES
            (1, 1, '2024-01-15', 150.00),
            (2, 1, '2024-02-10', 75.00),
            (3, 2, '2024-01-20', 200.00),
            (4, 3, '2024-03-05', 50.00);
    """)
    print("SIN INDICE compuesto:")
    cur = conn.execute("EXPLAIN QUERY PLAN SELECT * FROM pedidos WHERE cliente_id = 1 ORDER BY fecha;")
    for f in cur.fetchall():
        print(f["detail"])
    print()
    conn.execute("CREATE INDEX idx_cliente_fecha ON pedidos(cliente_id, fecha);")
    print("CON INDICE compuesto:")
    cur = conn.execute("EXPLAIN QUERY PLAN SELECT * FROM pedidos WHERE cliente_id = 1 ORDER BY fecha;")
    for f in cur.fetchall():
        print(f["detail"])

def solucion_3():
    print("=" * 50)
    print("SOLUCION 3: Cuando (no) indexar")
    print("=" * 50)
    print()
    print("1. Tabla 'usuarios' (1M filas), columna 'email' en WHERE.")
    print("   -> SI, definitivamente. Tabla grande y busqueda exacta.")
    print()
    print("2. Tabla 'configuracion' (10 filas), columna 'clave' en WHERE.")
    print("   -> NO, la tabla es demasiado pequena. Un indice anade")
    print("      overhead sin beneficio. El escaneo secuencial es casi")
    print("      instantaneo.")
    print()
    print("3. Columna 'activo' (solo 0 o 1) en tabla grande.")
    print("   -> NO, baja cardinalidad (solo 2 valores). Un indice no")
    print("      reduce significativamente el escaneo.")
    print()
    print("4. Columna 'fecha_creacion' con ORDER BY frecuente.")
    print("   -> SI, si la tabla es grande y se ordena frecuentemente.")
    print("      Ayuda tanto en filtros como en ordenamientos.")

def menu():
    print("SOLUCIONES - INDICES Y OPTIMIZACION")
    print("1 - CREATE INDEX y EXPLAIN")
    print("2 - Indices compuestos")
    print("3 - Cuando (no) indexar")

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
