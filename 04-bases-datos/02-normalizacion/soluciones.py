"""
SOLUCIONES - Normalizacion
Ejecuta: python scripts/runner.py 4 2 [ejercicio] -s
"""

import sys
import sqlite3

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: Corregir 1FN")
    print("=" * 50)

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
        CREATE TABLE estudiante_curso (
            estudiante_id INTEGER,
            curso_id INTEGER,
            PRIMARY KEY (estudiante_id, curso_id),
            FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id),
            FOREIGN KEY (curso_id) REFERENCES cursos(id)
        );
        INSERT INTO estudiantes VALUES (1, 'Ana'), (2, 'Juan'), (3, 'Maria');
        INSERT INTO cursos VALUES (1, 'Matematicas'), (2, 'Historia'),
            (3, 'Ciencias'), (4, 'Arte'), (5, 'Musica');
        INSERT INTO estudiante_curso VALUES
            (1, 1), (1, 2), (2, 3), (2, 4), (2, 5), (3, 2), (3, 3);
    """)
    conn.commit()

    print("--- ESQUEMA NORMALIZADO A 1FN ---")
    print()
    print("Estudiantes:")
    for row in c.execute("SELECT * FROM estudiantes"):
        print(f"  {row}")
    print("Cursos:")
    for row in c.execute("SELECT * FROM cursos"):
        print(f"  {row}")
    print("Relaciones estudiante-curso:")
    for row in c.execute("""
        SELECT e.nombre, c.nombre
        FROM estudiante_curso ec
        JOIN estudiantes e ON ec.estudiante_id = e.id
        JOIN cursos c ON ec.curso_id = c.id
    """):
        print(f"  {row[0]} → {row[1]}")

    print()
    print("--- EXPLICACION ---")
    print("""
Antes (viola 1FN):
  estudiantes(id, nombre, cursos)
  Fila: 1 | Ana | Matematicas,Historia  ← columna NO atomica

Despues (1FN):
  estudiantes(id, nombre)
  cursos(id, nombre)
  estudiante_curso(estudiante_id, curso_id)
  Fila: 1 | Ana | Matematicas  → cada fila tiene un solo valor

La tabla intermedia permite relacion MUCHOS a MUCHOS:
  - Un estudiante puede tener muchos cursos
  - Un curso puede tener muchos estudiantes
""")


def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: Normalizar a 2FN")
    print("=" * 50)

    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE estudiantes (id INTEGER PRIMARY KEY, nombre TEXT);
        CREATE TABLE cursos (id INTEGER PRIMARY KEY, nombre TEXT, profesor TEXT);
        CREATE TABLE calificaciones (
            estudiante_id INTEGER,
            curso_id INTEGER,
            nota REAL,
            PRIMARY KEY (estudiante_id, curso_id),
            FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id),
            FOREIGN KEY (curso_id) REFERENCES cursos(id)
        );
        INSERT INTO estudiantes VALUES (1, 'Ana'), (2, 'Juan');
        INSERT INTO cursos VALUES (101, 'Matematicas', 'Dr. Lopez'),
            (102, 'Historia', 'Dra. Perez'), (103, 'Ciencias', 'Dr. Garcia');
        INSERT INTO calificaciones VALUES (1, 101, 8.5), (1, 102, 9.0),
            (2, 101, 7.5), (2, 103, 8.0);
    """)
    conn.commit()

    print("--- ESQUEMA NORMALIZADO A 2FN ---")
    for row in c.execute("""
        SELECT e.nombre, c.nombre, c.profesor, cal.nota
        FROM calificaciones cal
        JOIN estudiantes e ON cal.estudiante_id = e.id
        JOIN cursos c ON cal.curso_id = c.id
    """):
        print(f"  {row[0]:8s} | {row[1]:12s} | {row[2]:12s} | {row[3]}")

    print()
    print("--- EXPLICACION ---")
    print("""
Antes (viola 2FN):
  calificaciones(estudiante_id, estudiante_nombre, curso_id,
                 curso_nombre, profesor, nota)
  PK: (estudiante_id, curso_id)
  - estudiante_nombre depende SOLO de estudiante_id (dependencia parcial)
  - curso_nombre, profesor dependen SOLO de curso_id (dependencia parcial)

Despues (2FN):
  estudiantes(id, nombre)
  cursos(id, nombre, profesor)
  calificaciones(estudiante_id, curso_id, nota)

Ventajas: sin redundancia. Si 'Ana' se cambia a 'Maria',
solo se cambia en 1 lugar (tabla estudiantes).
""")


def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: Normalizar a 3FN")
    print("=" * 50)

    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE clientes (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            ciudad TEXT
        );
        CREATE TABLE pedidos (
            id INTEGER PRIMARY KEY,
            cliente_id INTEGER REFERENCES clientes(id),
            producto TEXT,
            cantidad INTEGER,
            total REAL
        );
        INSERT INTO clientes VALUES (1, 'Ana', 'Madrid'),
            (2, 'Juan', 'Barcelona'), (3, 'Maria', 'Valencia');
        INSERT INTO pedidos VALUES (1, 1, 'Laptop', 1, 999.99),
            (2, 2, 'Mouse', 2, 51.00), (3, 1, 'Teclado', 1, 45.00),
            (4, 3, 'Monitor', 2, 599.98);
    """)
    conn.commit()

    print("--- ESQUEMA NORMALIZADO A 3FN ---")
    print("Clientes:")
    for row in c.execute("SELECT * FROM clientes"):
        print(f"  {row}")
    print("Pedidos:")
    for row in c.execute("""
        SELECT p.id, c.nombre, c.ciudad, p.producto, p.cantidad, p.total
        FROM pedidos p JOIN clientes c ON p.cliente_id = c.id
    """):
        print(f"  Pedido {row[0]}: {row[1]} ({row[2]}) → {row[3]} x{row[4]} = ${row[5]:.2f}")

    print()
    print("--- EXPLICACION ---")
    print("""
Antes (viola 3FN):
  pedidos(pedido_id, cliente_id, cliente_nombre, cliente_ciudad,
          producto, cantidad, total)
  Dependencia transitiva:
    pedido_id → cliente_id → cliente_nombre
    pedido_id → cliente_id → cliente_ciudad

Despues (3FN):
  clientes(id, nombre, ciudad)
  pedidos(id, cliente_id, producto, cantidad, total)

Ventajas:
  - Los datos del cliente NO se repiten en cada pedido
  - Si Ana se muda a 'Sevilla', se cambia en 1 solo lugar
  - No hay riesgo de inconsistencias
""")


if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
