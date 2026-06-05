"""
SOLUCIONES - Normalizacion
Ejecuta desde raiz: python scripts/runner.py 4 2 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Identifica la violacion de 1NF: columna con multiples valores separados por comas"""
    import sqlite3
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    # Esquema normalizado a 1FN
    c.executescript("""
        CREATE TABLE estudiantes (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL
        );
        CREATE TABLE cursos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL
        );
        CREATE TABLE estudiante_curso (
            estudiante_id INTEGER,
            curso_id INTEGER,
            PRIMARY KEY (estudiante_id, curso_id),
            FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id),
            FOREIGN KEY (curso_id) REFERENCES cursos(id)
        );
        INSERT INTO estudiantes VALUES (1, 'Ana'), (2, 'Juan'), (3, 'Maria');
        INSERT INTO cursos VALUES (1, 'Matematicas'), (2, 'Historia'), (3, 'Ciencias'), (4, 'Arte'), (5, 'Musica');
        INSERT INTO estudiante_curso VALUES (1, 1), (1, 2), (2, 3), (2, 4), (2, 5), (3, 2), (3, 3);
    """)
    conn.commit()
    print(">>> Esquema normalizado a 1FN:")
    print("  Tabla: estudiantes, cursos, estudiante_curso")
    print()
    print("  Estudiantes:")
    for row in c.execute("SELECT * FROM estudiantes"):
        print(f"    {row}")
    print("  Cursos:")
    for row in c.execute("SELECT * FROM cursos"):
        print(f"    {row}")
    print("  Relaciones:")
    for row in c.execute("SELECT e.nombre, c.nombre FROM estudiante_curso ec JOIN estudiantes e ON ec.estudiante_id=e.id JOIN cursos c ON ec.curso_id=c.id"):
        print(f"    {row[0]} -> {row[1]}")

def ejercicio_2():
    """Normaliza a 2FN: elimina dependencias parciales en una tabla de calificaciones"""
    import sqlite3
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    # Esquema normalizado a 2FN
    c.executescript("""
        CREATE TABLE estudiantes (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL
        );
        CREATE TABLE cursos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            profesor TEXT NOT NULL
        );
        CREATE TABLE calificaciones (
            estudiante_id INTEGER,
            curso_id INTEGER,
            nota REAL,
            PRIMARY KEY (estudiante_id, curso_id),
            FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id),
            FOREIGN KEY (curso_id) REFERENCES cursos(id)
        );
        INSERT INTO estudiantes VALUES (1, 'Ana'), (2, 'Juan');
        INSERT INTO cursos VALUES (101, 'Matematicas', 'Dr. Lopez'), (102, 'Historia', 'Dra. Perez'), (103, 'Ciencias', 'Dr. Garcia');
        INSERT INTO calificaciones VALUES (1, 101, 8.5), (1, 102, 9.0), (2, 101, 7.5), (2, 103, 8.0);
    """)
    conn.commit()
    print(">>> Esquema normalizado a 2FN (sin dependencias parciales):")
    for row in c.execute("SELECT e.nombre, c.nombre, c.profesor, cal.nota FROM calificaciones cal JOIN estudiantes e ON cal.estudiante_id=e.id JOIN cursos c ON cal.curso_id=c.id"):
        print(f"  {row[0]:<8} | {row[1]:<12} | {row[2]:<12} | {row[3]}")

def ejercicio_3():
    """Normaliza a 3FN: elimina dependencias transitivas en una tabla de pedidos"""
    import sqlite3
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    # Esquema normalizado a 3FN
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
            cantidad INTEGER NOT NULL,
            total REAL NOT NULL,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        );
        INSERT INTO clientes VALUES (1, 'Ana', 'Madrid'), (2, 'Juan', 'Barcelona'), (3, 'Maria', 'Valencia');
        INSERT INTO pedidos VALUES (1, 1, 'Laptop', 1, 999.99), (2, 2, 'Mouse', 2, 51.00), (3, 1, 'Teclado', 1, 45.00), (4, 3, 'Monitor', 2, 599.98);
    """)
    conn.commit()
    print(">>> Esquema normalizado a 3FN (sin dependencias transitivas):")
    print("  Clientes:")
    for row in c.execute("SELECT * FROM clientes"):
        print(f"    {row}")
    print("  Pedidos:")
    for row in c.execute("SELECT * FROM pedidos JOIN clientes ON pedidos.cliente_id=clientes.id"):
        print(f"    Pedido {row[0]}: {row[5]} ({row[6]}) - {row[3]} x {row[4]}")

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
