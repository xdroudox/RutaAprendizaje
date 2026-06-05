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
    print("EJERCICIO 1: INNER JOIN")
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
    print("Tablas: clientes (3 registros), pedidos (3 registros)")
    print()
    print("TAREA: Escribe un INNER JOIN que muestre el nombre del")
    print("cliente y el total de cada pedido.")
    print()
    print("PISTA: SELECT c.nombre, p.total FROM clientes c")
    print("  INNER JOIN pedidos p ON c.id = p.cliente_id;")

def ejercicio_2():
    print("=" * 50)
    print("EJERCICIO 2: LEFT JOIN (clientes sin pedidos)")
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
    print("Cliente 'Maria' (id=3) no tiene pedidos.")
    print()
    print("TAREA: Escribe un LEFT JOIN que muestre TODOS los")
    print("clientes, incluso los que no tienen pedidos.")
    print("Los clientes sin pedidos deben mostrar NULL en producto.")
    print()
    print("PISTA: LEFT JOIN ... ON ...")

def ejercicio_3():
    print("=" * 50)
    print("EJERCICIO 3: Muchos a Muchos")
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
    """)
    print("Tablas: estudiantes (3) y cursos (3).")
    print("Falta la tabla intermedia estudiante_curso.")
    print()
    print("TAREA: Crea la tabla intermedia e inserta datos para que:")
    print("- Ana curse Matematicas y Fisica")
    print("- Luis curse Historia")
    print("- Maria curse Matematicas y Historia")
    print("Luego escribe un JOIN triple que muestre: estudiante, curso")
    print()
    print("PISTA: estudiante_curso(estudiante_id, curso_id) + dos INNER JOINs")

pistas = {
    "1": "SELECT c.nombre, p.total FROM clientes c INNER JOIN pedidos p ON c.id = p.cliente_id;",
    "2": "SELECT c.nombre, p.producto FROM clientes c LEFT JOIN pedidos p ON c.id = p.cliente_id;",
    "3": "CREATE TABLE estudiante_curso (estudiante_id INTEGER, curso_id INTEGER, PRIMARY KEY (estudiante_id, curso_id));\nINSERT INTO estudiante_curso VALUES (1,1),(1,3),(2,2),(3,1),(3,2);\nSELECT e.nombre AS estudiante, c.nombre AS curso FROM estudiantes e INNER JOIN estudiante_curso ec ON e.id = ec.estudiante_id INNER JOIN cursos c ON ec.curso_id = c.id;"
}

def menu():
    print("=" * 50)
    print("JOINS Y RELACIONES - EJERCICIOS")
    print("=" * 50)
    print("1 - INNER JOIN")
    print("2 - LEFT JOIN")
    print("3 - Muchos a Muchos")
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
