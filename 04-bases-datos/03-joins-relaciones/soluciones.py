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
    print("SOLUCION 1: INNER JOIN")
    print("=" * 50)
    conn = get_db()
    conn.executescript("""
        CREATE TABLE clientes (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            ciudad TEXT
        );
        INSERT INTO clientes VALUES (1, 'Ana', 'Madrid'), (2, 'Luis', 'Barcelona'), (3, 'Maria', 'Valencia');
        CREATE TABLE pedidos (
            id INTEGER PRIMARY KEY,
            cliente_id INTEGER,
            total REAL,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        );
        INSERT INTO pedidos VALUES (1, 1, 150.00), (2, 1, 75.00), (3, 2, 200.00);
    """)
    query = "SELECT c.nombre, p.total FROM clientes c INNER JOIN pedidos p ON c.id = p.cliente_id;"
    print("Consulta ejecutada:")
    print(query)
    print()
    mostrar_resultados(conn, query)

def solucion_2():
    print("=" * 50)
    print("SOLUCION 2: LEFT JOIN")
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
            producto TEXT,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        );
        INSERT INTO pedidos VALUES (1, 1, 'Laptop'), (2, 2, 'Mouse');
    """)
    query = "SELECT c.nombre, p.producto FROM clientes c LEFT JOIN pedidos p ON c.id = p.cliente_id;"
    print("Consulta ejecutada:")
    print(query)
    print()
    mostrar_resultados(conn, query)
    print()
    print("Nota: Maria aparece con NULL en producto porque no tiene pedidos.")

def solucion_3():
    print("=" * 50)
    print("SOLUCION 3: Muchos a Muchos")
    print("=" * 50)
    conn = get_db()
    conn.executescript("""
        CREATE TABLE estudiantes (
            id INTEGER PRIMARY KEY,
            nombre TEXT
        );
        INSERT INTO estudiantes VALUES (1, 'Ana'), (2, 'Luis'), (3, 'Maria');
        CREATE TABLE cursos (
            id INTEGER PRIMARY KEY,
            nombre TEXT
        );
        INSERT INTO cursos VALUES (1, 'Matematicas'), (2, 'Historia'), (3, 'Fisica');
        CREATE TABLE estudiante_curso (
            estudiante_id INTEGER,
            curso_id INTEGER,
            PRIMARY KEY (estudiante_id, curso_id),
            FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id),
            FOREIGN KEY (curso_id) REFERENCES cursos(id)
        );
        INSERT INTO estudiante_curso VALUES
            (1, 1), (1, 3),
            (2, 2),
            (3, 1), (3, 2);
    """)
    query = """
        SELECT e.nombre AS estudiante, c.nombre AS curso
        FROM estudiantes e
        INNER JOIN estudiante_curso ec ON e.id = ec.estudiante_id
        INNER JOIN cursos c ON ec.curso_id = c.id;
    """
    print("Consulta ejecutada:")
    print(query.strip())
    print()
    mostrar_resultados(conn, query)

def menu():
    print("SOLUCIONES - JOINS Y RELACIONES")
    print("1 - INNER JOIN")
    print("2 - LEFT JOIN")
    print("3 - Muchos a Muchos")

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
