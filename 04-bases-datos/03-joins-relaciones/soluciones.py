"""
SOLUCIONES - Joins y Relaciones
Ejecuta: python scripts/runner.py 4 3 [ejercicio] -s
"""

import sys
import sqlite3

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: INNER JOIN")
    print("=" * 50)

    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE clientes (id INTEGER PRIMARY KEY, nombre TEXT, ciudad TEXT);
        CREATE TABLE pedidos (id INTEGER PRIMARY KEY, cliente_id INTEGER, producto TEXT, total REAL);
        INSERT INTO clientes VALUES (1, 'Ana', 'Madrid'), (2, 'Juan', 'Barcelona'), (3, 'Maria', 'Valencia');
        INSERT INTO pedidos VALUES (1, 1, 'Laptop', 999.99), (2, 2, 'Mouse', 25.50), (3, 1, 'Teclado', 45.00);
    """)

    print("--- CONSULTA ---")
    print("SELECT p.id, p.producto, p.total, c.nombre, c.ciudad")
    print("FROM pedidos p")
    print("INNER JOIN clientes c ON p.cliente_id = c.id;")
    print()

    query = """SELECT p.id, p.producto, p.total, c.nombre, c.ciudad
               FROM pedidos p INNER JOIN clientes c ON p.cliente_id = c.id"""
    for row in c.execute(query):
        print(f"  Pedido {row[0]}: {row[1]:<8} ${row[2]:<7.2f} → {row[3]:<6} ({row[4]})")

    print()
    print("--- EXPLICACION ---")
    print("""
INNER JOIN solo devuelve filas con correspondencia en AMBAS tablas:
  - Se combinan pedido y cliente donde pedidos.cliente_id = clientes.id
  - Maria (cliente 3) NO aparece porque no tiene pedidos
  - Ana aparece 2 veces (tiene 2 pedidos) — el JOIN duplica filas si es necesario

Sin el JOIN, tendrias que hacer 2 consultas separadas o mezclar manualmente.
""")


def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: LEFT JOIN")
    print("=" * 50)

    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE clientes (id INTEGER PRIMARY KEY, nombre TEXT);
        CREATE TABLE pedidos (id INTEGER PRIMARY KEY, cliente_id INTEGER, producto TEXT);
        INSERT INTO clientes VALUES (1, 'Ana'), (2, 'Juan'), (3, 'Maria'), (4, 'Carlos');
        INSERT INTO pedidos VALUES (1, 1, 'Laptop'), (2, 2, 'Mouse');
    """)

    print("--- CONSULTA ---")
    print("SELECT c.nombre, p.producto")
    print("FROM clientes c")
    print("LEFT JOIN pedidos p ON c.id = p.cliente_id;")
    print()

    query = """SELECT c.nombre, p.producto
               FROM clientes c LEFT JOIN pedidos p ON c.id = p.cliente_id"""
    for row in c.execute(query):
        prod = row[1] if row[1] else "NULL (sin pedido)"
        print(f"  {row[0]:<8} → {prod}")

    print()
    print("--- EXPLICACION ---")
    print("""
LEFT JOIN devuelve TODAS las filas de la tabla IZQUIERDA (clientes):
  - Ana y Juan tienen pedidos → se muestran normalmente
  - Maria y Carlos NO tienen → columnas de pedidos = NULL

Es util para: encontrar clientes inactivos, llenar reportes con
todos los elementos aunque esten incompletos, etc.

Diferencia clave:
  INNER JOIN: 4 filas (Ana, Ana, Juan — Maria excluida)
  LEFT JOIN:  4 filas (Ana, Ana, Juan, Maria, Carlos)
""")


def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: Relacion muchos-a-muchos")
    print("=" * 50)

    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE estudiantes (id INTEGER PRIMARY KEY, nombre TEXT);
        CREATE TABLE cursos (id INTEGER PRIMARY KEY, nombre TEXT);
        CREATE TABLE inscripciones (estudiante_id INTEGER, curso_id INTEGER,
            PRIMARY KEY (estudiante_id, curso_id));
        INSERT INTO estudiantes VALUES (1, 'Ana'), (2, 'Juan'), (3, 'Maria');
        INSERT INTO cursos VALUES (1, 'Matematicas'), (2, 'Historia'), (3, 'Programacion');
        INSERT INTO inscripciones VALUES (1, 1), (1, 3), (2, 1), (2, 2), (3, 2), (3, 3);
    """)

    print("--- CONSULTA ---")
    print("SELECT e.nombre, c.nombre")
    print("FROM estudiantes e")
    print("JOIN inscripciones i ON e.id = i.estudiante_id")
    print("JOIN cursos c ON i.curso_id = c.id")
    print("ORDER BY e.nombre;")
    print()

    query = """SELECT e.nombre, c.nombre FROM estudiantes e
               JOIN inscripciones i ON e.id = i.estudiante_id
               JOIN cursos c ON i.curso_id = c.id ORDER BY e.nombre"""
    for row in c.execute(query):
        print(f"  {row[0]:<8} → {row[1]}")

    print()
    print("--- EXPLICACION ---")
    print("""
Para relaciones N:M necesitas 3 INNER JOINs:

1. estudiantes → inscripciones (por estudiante_id)
2. inscripciones → cursos (por curso_id)

La tabla 'inscripciones' es la TABLA INTERMEDIA que resuelve
la relacion muchos-a-muchos:
  - Un estudiante puede estar en MUCHOS cursos
  - Un curso puede tener MUCHOS estudiantes

Sin la tabla intermedia, tendrias que repetir datos o usar
columnas con multiples valores (violando 1FN).
""")


if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
