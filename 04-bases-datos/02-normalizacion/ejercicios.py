"""
EJERCICIOS - Normalizacion
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
    c.executescript("""
        CREATE TABLE estudiantes (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            cursos TEXT NOT NULL
        );
        INSERT INTO estudiantes VALUES (1, 'Ana', 'Matematicas,Historia');
        INSERT INTO estudiantes VALUES (2, 'Juan', 'Ciencias,Arte,Musica');
        INSERT INTO estudiantes VALUES (3, 'Maria', 'Historia,Ciencias');
    """)
    conn.commit()
    print("=== Tabla actual (1FN violada) ===")
    print("id | nombre | cursos")
    print("---|--------|----------------------")
    for row in c.execute("SELECT * FROM estudiantes"):
        print(f" {row[0]}  | {row[1]:6s} | {row[2]}")
    print()
    print("Problema: la columna 'cursos' contiene multiples valores separados por comas.")
    print("Crea dos tablas normalizadas: estudiantes y cursos, con tabla intermedia.")
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    # Define el esquema normalizado a 1FN usando CREATE TABLE
    pass

def ejercicio_2():
    """Normaliza a 2FN: elimina dependencias parciales en una tabla de calificaciones"""
    import sqlite3
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE calificaciones (
            estudiante_id INTEGER,
            estudiante_nombre TEXT,
            curso_id INTEGER,
            curso_nombre TEXT,
            profesor TEXT,
            nota REAL,
            PRIMARY KEY (estudiante_id, curso_id)
        );
        INSERT INTO calificaciones VALUES
            (1, 'Ana', 101, 'Matematicas', 'Dr. Lopez', 8.5),
            (1, 'Ana', 102, 'Historia', 'Dra. Perez', 9.0),
            (2, 'Juan', 101, 'Matematicas', 'Dr. Lopez', 7.5),
            (2, 'Juan', 103, 'Ciencias', 'Dr. Garcia', 8.0);
    """)
    conn.commit()
    print("=== Tabla actual (2FN violada) ===")
    print("estudiante_id | estudiante_nombre | curso_id | curso_nombre | profesor    | nota")
    print("--------------|-------------------|----------|--------------|-------------|------")
    for row in c.execute("SELECT * FROM calificaciones"):
        print(f" {row[0]:<13} | {row[1]:<17} | {row[2]:<8} | {row[3]:<12} | {row[4]:<11} | {row[5]}")
    print()
    print("Problema: estudiante_nombre depende solo de estudiante_id,")
    print("curso_nombre y profesor dependen solo de curso_id.")
    print("Crea tablas separadas: estudiantes, cursos, calificaciones (2FN).")
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass

def ejercicio_3():
    """Normaliza a 3FN: elimina dependencias transitivas en una tabla de pedidos"""
    import sqlite3
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE pedidos (
            pedido_id INTEGER PRIMARY KEY,
            cliente_id INTEGER,
            cliente_nombre TEXT,
            cliente_ciudad TEXT,
            producto TEXT,
            cantidad INTEGER,
            total REAL
        );
        INSERT INTO pedidos VALUES
            (1, 1, 'Ana', 'Madrid', 'Laptop', 1, 999.99),
            (2, 2, 'Juan', 'Barcelona', 'Mouse', 2, 51.00),
            (3, 1, 'Ana', 'Madrid', 'Teclado', 1, 45.00),
            (4, 3, 'Maria', 'Valencia', 'Monitor', 2, 599.98);
    """)
    conn.commit()
    print("=== Tabla actual (3FN violada) ===")
    print("pedido_id | cliente_id | cliente_nombre | cliente_ciudad | producto | cantidad | total")
    print("----------|------------|----------------|----------------|----------|----------|-------")
    for row in c.execute("SELECT * FROM pedidos"):
        print(f" {row[0]:<9} | {row[1]:<10} | {row[2]:<14} | {row[3]:<14} | {row[4]:<8} | {row[5]:<8} | {row[6]}")
    print()
    print("Problema: cliente_nombre y cliente_ciudad dependen de cliente_id")
    print("(dependencia transitiva a traves de pedido_id -> cliente_id -> datos_cliente).")
    print("Crea tablas separadas: clientes, pedidos (3FN).")
    # ==== ESCRIBE TU RESPUESTA AQUI ====
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
