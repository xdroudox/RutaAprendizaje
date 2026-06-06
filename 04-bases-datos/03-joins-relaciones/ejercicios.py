"""
EJERCICIOS - Joins y Relaciones
Ejecuta desde raiz: python scripts/runner.py 4 3 [ejercicio]

Niveles:
  🟢 Ej 1: INNER JOIN (pedidos + clientes)
  🟡 Ej 2: LEFT JOIN (todos los clientes)
  🔴 Ej 3: Muchos-a-muchos (estudiantes-cursos)

Pistas: python scripts/runner.py 4 3 N -p [1|2|3]
"""

import sys
import sqlite3

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1(pista=0):
    """🟢 INNER JOIN (pedidos + clientes)"""
    print(">> 🟢 EJERCICIO 1: INNER JOIN")
    print("-" * 50)

    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE clientes (
            id INTEGER PRIMARY KEY, nombre TEXT NOT NULL, ciudad TEXT NOT NULL
        );
        CREATE TABLE pedidos (
            id INTEGER PRIMARY KEY, cliente_id INTEGER NOT NULL,
            producto TEXT NOT NULL, total REAL NOT NULL,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        );
        INSERT INTO clientes VALUES (1, 'Ana', 'Madrid'), (2, 'Juan', 'Barcelona'), (3, 'Maria', 'Valencia');
        INSERT INTO pedidos VALUES (1, 1, 'Laptop', 999.99), (2, 2, 'Mouse', 25.50), (3, 1, 'Teclado', 45.00);
    """)
    conn.commit()

    print("=== Datos ===")
    print("Clientes:")
    for r in c.execute("SELECT * FROM clientes"): print(f"  {r}")
    print("Pedidos:")
    for r in c.execute("SELECT * FROM pedidos"): print(f"  {r}")

    if pista == 1:
        print("\n💡 Pista 1: Sintaxis INNER JOIN:")
        print("  SELECT columnas FROM tabla1")
        print("  INNER JOIN tabla2 ON tabla1.columna = tabla2.columna")
        return
    elif pista == 2:
        print("\n💡 Pista 2: La condicion es:")
        print("  ON pedidos.cliente_id = clientes.id")
        return
    elif pista == 3:
        print("\n💡 Pista 3:")
        print("  SELECT p.id, p.producto, p.total, c.nombre, c.ciudad")
        print("  FROM pedidos p INNER JOIN clientes c")
        print("  ON p.cliente_id = c.id")
        return

    print("\nMuestra pedidos con nombre y ciudad del cliente (INNER JOIN):")
    print("# ==== ESCRIBE TU CONSULTA AQUI ====")


def ejercicio_2(pista=0):
    """🟡 LEFT JOIN (todos los clientes)"""
    print(">> 🟡 EJERCICIO 2: LEFT JOIN")
    print("-" * 50)

    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE clientes (id INTEGER PRIMARY KEY, nombre TEXT NOT NULL);
        CREATE TABLE pedidos (id INTEGER PRIMARY KEY, cliente_id INTEGER NOT NULL,
            producto TEXT NOT NULL, FOREIGN KEY (cliente_id) REFERENCES clientes(id));
        INSERT INTO clientes VALUES (1, 'Ana'), (2, 'Juan'), (3, 'Maria'), (4, 'Carlos');
        INSERT INTO pedidos VALUES (1, 1, 'Laptop'), (2, 2, 'Mouse');
    """)
    conn.commit()

    print("=== Datos ===")
    for r in c.execute("SELECT * FROM clientes"): print(f"  Cliente: {r}")
    for r in c.execute("SELECT * FROM pedidos"): print(f"  Pedido: {r}")

    if pista == 1:
        print("\n💡 Pista 1: LEFT JOIN muestra TODAS las filas de la izquierda.")
        print("  Si no hay match, las columnas de la derecha son NULL.")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  SELECT c.nombre, p.producto")
        print("  FROM clientes c LEFT JOIN pedidos p")
        print("  ON c.id = p.cliente_id")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Resultado esperado:")
        print("  Ana → Laptop, Juan → Mouse,")
        print("  Maria → NULL, Carlos → NULL")
        return

    print("\nMuestra TODOS los clientes (con o sin pedidos):")
    print("  Carlos no tiene pedidos → debe aparecer con NULL.")
    print("# ==== ESCRIBE TU CONSULTA AQUI ====")


def ejercicio_3(pista=0):
    """🔴 Muchos-a-muchos (estudiantes-cursos)"""
    print(">> 🔴 EJERCICIO 3: Relacion muchos-a-muchos")
    print("-" * 50)

    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE estudiantes (id INTEGER PRIMARY KEY, nombre TEXT NOT NULL);
        CREATE TABLE cursos (id INTEGER PRIMARY KEY, nombre TEXT NOT NULL);
        CREATE TABLE inscripciones (
            estudiante_id INTEGER, curso_id INTEGER,
            PRIMARY KEY (estudiante_id, curso_id),
            FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id),
            FOREIGN KEY (curso_id) REFERENCES cursos(id));
        INSERT INTO estudiantes VALUES (1, 'Ana'), (2, 'Juan'), (3, 'Maria');
        INSERT INTO cursos VALUES (1, 'Matematicas'), (2, 'Historia'), (3, 'Programacion');
        INSERT INTO inscripciones VALUES (1, 1), (1, 3), (2, 1), (2, 2), (3, 2), (3, 3);
    """)
    conn.commit()

    if pista == 1:
        print("\n💡 Pista 1: Necesitas 3 JOINs:")
        print("  estudiantes → inscripciones → cursos")
        print("  La tabla intermedia conecta ambas.")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  SELECT e.nombre, c.nombre")
        print("  FROM estudiantes e")
        print("  JOIN inscripciones i ON e.id = i.estudiante_id")
        print("  JOIN cursos c ON i.curso_id = c.id")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Las relaciones son:")
        print("  Ana → Matematicas, Programacion")
        print("  Juan → Matematicas, Historia")
        print("  Maria → Historia, Programacion")
        return

    print("=== Muestra estudiantes con sus cursos ===")
    for r in c.execute("SELECT * FROM estudiantes"): print(f"  {r[0]}. {r[1]}")
    for r in c.execute("SELECT * FROM cursos"): print(f"  Curso: {r[1]}")
    print()
    print("# ==== ESCRIBE TU CONSULTA AQUI ====")


if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            pista = 0
            if "-p" in sys.argv:
                idx = sys.argv.index("-p")
                if idx + 1 < len(sys.argv) and sys.argv[idx + 1].isdigit():
                    pista = int(sys.argv[idx + 1])
            ejercicios[num](pista)
    else:
        print("EJERCICIOS:")
        for i, ej in enumerate(ejercicios, 1):
            doc = ej.__doc__ or ""
            print(f"  {i}. {doc}")
