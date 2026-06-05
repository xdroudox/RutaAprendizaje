"""
EJERCICIOS - Joins y Relaciones
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
    print("=== Pedidos con datos del cliente ===")
    print("id_pedido | producto | total  | cliente  | ciudad")
    print("----------|----------|--------|----------|--------")
    # ==== ESCRIBE TU CONSULTA SQL AQUI ====
    # query = "SELECT ... FROM pedidos INNER JOIN clientes ON ..."
    # c.execute(query)
    # for row in c.fetchall():
    #     print(row)
    pass

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
    print("=== Todos los clientes (con o sin pedidos) ===")
    print("cliente | producto")
    print("--------|---------")
    print("(Carlos no tiene pedidos, debe aparecer con NULL)")
    # ==== ESCRIBE TU CONSULTA SQL AQUI ====
    # query = "SELECT ... FROM clientes LEFT JOIN pedidos ON ..."
    # c.execute(query)
    # for row in c.fetchall():
    #     print(row)
    pass

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
    print("=== Estudiantes con sus cursos (relacion muchos-a-muchos) ===")
    # ==== ESCRIBE TU CONSULTA SQL AQUI ====
    # Usa INNER JOIN entre las 3 tablas
    # for row in c.fetchall():
    #     print(f"  {row[0]} -> {row[1]}")
    pass

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
