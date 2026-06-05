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
    print("SOLUCION 1: CREATE TABLE e INSERT")
    print("=" * 50)
    conn = get_db()
    conn.executescript("""
        CREATE TABLE productos (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            precio REAL,
            stock INTEGER
        );
        INSERT INTO productos VALUES (1, 'Laptop', 1200.00, 10);
        INSERT INTO productos VALUES (2, 'Mouse', 25.50, 50);
        INSERT INTO productos VALUES (3, 'Teclado', 45.00, 30);
    """)
    query = "INSERT INTO productos VALUES (4, 'Monitor', 300.00, 15);"
    conn.execute(query)
    print("Consulta ejecutada:")
    print(query)
    print()
    mostrar_resultados(conn, "SELECT * FROM productos;")

def solucion_2():
    print("=" * 50)
    print("SOLUCION 2: SELECT con WHERE")
    print("=" * 50)
    conn = get_db()
    conn.executescript("""
        CREATE TABLE empleados (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            salario REAL,
            departamento TEXT
        );
        INSERT INTO empleados VALUES (1, 'Ana', 45000, 'Ventas');
        INSERT INTO empleados VALUES (2, 'Luis', 52000, 'TI');
        INSERT INTO empleados VALUES (3, 'Maria', 48000, 'Ventas');
        INSERT INTO empleados VALUES (4, 'Carlos', 55000, 'TI');
        INSERT INTO empleados VALUES (5, 'Sofia', 39000, 'RH');
    """)
    query = "SELECT * FROM empleados WHERE departamento = 'Ventas' AND salario > 46000;"
    print("Consulta ejecutada:")
    print(query)
    print()
    mostrar_resultados(conn, query)

def solucion_3():
    print("=" * 50)
    print("SOLUCION 3: ORDER BY y LIMIT")
    print("=" * 50)
    conn = get_db()
    conn.executescript("""
        CREATE TABLE estudiantes (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            nota REAL,
            ciudad TEXT
        );
        INSERT INTO estudiantes VALUES (1, 'Pedro', 8.5, 'Madrid');
        INSERT INTO estudiantes VALUES (2, 'Laura', 9.2, 'Barcelona');
        INSERT INTO estudiantes VALUES (3, 'Diego', 7.8, 'Madrid');
        INSERT INTO estudiantes VALUES (4, 'Elena', 9.5, 'Barcelona');
        INSERT INTO estudiantes VALUES (5, 'Jorge', 6.5, 'Valencia');
        INSERT INTO estudiantes VALUES (6, 'Clara', 8.0, 'Valencia');
    """)
    query = "SELECT * FROM estudiantes ORDER BY nota DESC LIMIT 3;"
    print("Consulta ejecutada:")
    print(query)
    print()
    mostrar_resultados(conn, query)

def menu():
    print("SOLUCIONES - SQL FUNDAMENTOS")
    print("1 - CREATE TABLE e INSERT")
    print("2 - SELECT con WHERE")
    print("3 - ORDER BY y LIMIT")

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
