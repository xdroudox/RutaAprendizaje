"""
SOLUCIONES - Joins y Relaciones
Ejecuta desde raiz: python scripts/runner.py 4 3 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Escribe un INNER JOIN para mostrar pedidos con datos del cliente"""
    import sqlite3
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE clientes (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            ciudad TEXT NOT NULL
        );
        CREATE TABLE pedidos (
            id INTEGER PRIMARY KEY,
            cliente_id INTEGER NOT NULL,
            producto TEXT NOT NULL,
            total REAL NOT NULL,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        );
        INSERT INTO clientes VALUES (1, 'Ana', 'Madrid'), (2, 'Juan', 'Barcelona'), (3, 'Maria', 'Valencia');
        INSERT INTO pedidos VALUES (1, 1, 'Laptop', 999.99), (2, 2, 'Mouse', 25.50), (3, 1, 'Teclado', 45.00);
    """)
    conn.commit()
    print(">>> INNER JOIN: Pedidos + Clientes")
    query = """SELECT p.id, p.producto, p.total, c.nombre, c.ciudad
               FROM pedidos p
               INNER JOIN clientes c ON p.cliente_id = c.id"""
    c.execute(query)
    for row in c.fetchall():
        print(f"  Pedido {row[0]}: {row[1]:<10} ${row[2]:>6.2f} -> {row[3]:<8} ({row[4]})")

def ejercicio_2():
    """Escribe un LEFT JOIN para mostrar todos los clientes aunque no tengan pedidos"""
    import sqlite3
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE clientes (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL
        );
        CREATE TABLE pedidos (
            id INTEGER PRIMARY KEY,
            cliente_id INTEGER NOT NULL,
            producto TEXT NOT NULL,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        );
        INSERT INTO clientes VALUES (1, 'Ana'), (2, 'Juan'), (3, 'Maria'), (4, 'Carlos');
        INSERT INTO pedidos VALUES (1, 1, 'Laptop'), (2, 2, 'Mouse');
    """)
    conn.commit()
    print(">>> LEFT JOIN: Todos los clientes (incluyendo los que no tienen pedidos)")
    query = """SELECT c.nombre, p.producto
               FROM clientes c
               LEFT JOIN pedidos p ON c.id = p.cliente_id"""
    c.execute(query)
    for row in c.fetchall():
        print(f"  {row[0]:<8} | {row[1] if row[1] else 'NULL (sin pedido)'}")

def ejercicio_3():
    """Escribe una consulta muchos-a-muchos: estudiantes y sus cursos"""
    import sqlite3
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE estudiantes (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL
        );
        CREATE TABLE cursos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL
        );
        CREATE TABLE inscripciones (
            estudiante_id INTEGER,
            curso_id INTEGER,
            PRIMARY KEY (estudiante_id, curso_id),
            FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id),
            FOREIGN KEY (curso_id) REFERENCES cursos(id)
        );
        INSERT INTO estudiantes VALUES (1, 'Ana'), (2, 'Juan'), (3, 'Maria');
        INSERT INTO cursos VALUES (1, 'Matematicas'), (2, 'Historia'), (3, 'Programacion');
        INSERT INTO inscripciones VALUES (1, 1), (1, 3), (2, 1), (2, 2), (3, 2), (3, 3);
    """)
    conn.commit()
    print(">>> Muchos-a-muchos: Estudiantes <-> Cursos")
    query = """SELECT e.nombre, c.nombre
               FROM estudiantes e
               JOIN inscripciones i ON e.id = i.estudiante_id
               JOIN cursos c ON i.curso_id = c.id
               ORDER BY e.nombre"""
    c.execute(query)
    for row in c.fetchall():
        print(f"  {row[0]:<8} -> {row[1]}")

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            print(f">> EJERCICIO {num + 1}: {ejercicios[num].__doc__}")
            print("-" * 40)
            ejercicios[num]()
    else:
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
