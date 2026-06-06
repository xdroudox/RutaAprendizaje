"""
SOLUCIONES - SQL Fundamentos
Ejecuta: python scripts/runner.py 4 1 [ejercicio] -s
"""

import sys
import sqlite3

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: SELECT con WHERE")
    print("=" * 50)

    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE usuarios (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL
        );
        INSERT INTO usuarios VALUES (1, 'Ana', 25);
        INSERT INTO usuarios VALUES (2, 'Juan', 30);
        INSERT INTO usuarios VALUES (3, 'Maria', 22);
        INSERT INTO usuarios VALUES (4, 'Carlos', 28);
        INSERT INTO usuarios VALUES (5, 'Laura', 19);
    """)
    conn.commit()

    print("--- CONSULTA ---")
    print("SELECT * FROM usuarios WHERE edad > 25;")
    print()

    query = "SELECT * FROM usuarios WHERE edad > 25"
    c.execute(query)
    print("--- RESULTADO ---")
    for row in c.fetchall():
        print(f"  {row[0]:<3} {row[1]:<8} {row[2]} anos")

    print()
    print("--- EXPLICACION ---")
    print("""
WHERE filtra las filas que cumplen la condicion.
Solo se muestran Juan (30) y Carlos (28) porque Ana tiene
exactamente 25 (no > 25) y los demas son menores.

Operadores de comparacion en WHERE:
  =   igual
  <>  distinto (o !=)
  >   mayor que
  <   menor que
  >=  mayor o igual
  <=  menor o igual
""")


def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: INSERT INTO")
    print("=" * 50)

    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE productos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER DEFAULT 0
        );
        INSERT INTO productos VALUES (1, 'Laptop', 999.99, 10);
        INSERT INTO productos VALUES (2, 'Mouse', 25.50, 50);
        INSERT INTO productos VALUES (3, 'Teclado', 45.00, 30);
    """)
    conn.commit()

    print("--- CONSULTA ---")
    print("INSERT INTO productos VALUES (4, 'Monitor', 299.99, 15);")
    print()

    query = "INSERT INTO productos VALUES (4, 'Monitor', 299.99, 15)"
    c.execute(query)
    conn.commit()

    print("--- RESULTADO ---")
    for row in c.execute("SELECT * FROM productos"):
        print(f"  {row}")

    print()
    print("--- EXPLICACION ---")
    print("""
INSERT INTO agrega una nueva fila a la tabla.
Los valores deben coincidir en ORDEN y TIPO con las columnas:
  (id INTEGER, nombre TEXT, precio REAL, stock INTEGER)

Variantes de INSERT:
  - Con columnas explicitas: INSERT INTO productos (nombre, precio)
    VALUES ('Monitor', 299.99)  -- id y stock toman valores por defecto
  - Multiples filas: INSERT INTO productos VALUES
    (4, 'A', 1, 1), (5, 'B', 2, 2), (6, 'C', 3, 3);
""")


def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: UPDATE y DELETE")
    print("=" * 50)

    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE productos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER DEFAULT 0
        );
        INSERT INTO productos VALUES (1, 'Laptop', 999.99, 10);
        INSERT INTO productos VALUES (2, 'Mouse', 25.50, 50);
        INSERT INTO productos VALUES (3, 'Teclado', 45.00, 30);
        INSERT INTO productos VALUES (4, 'Monitor', 299.99, 15);
    """)
    conn.commit()

    print("--- CONSULTAS ---")
    print("UPDATE productos SET precio = 30.00 WHERE nombre = 'Mouse';")
    print("DELETE FROM productos WHERE id = 3;")
    print()

    c.execute("UPDATE productos SET precio = 30.00 WHERE nombre = 'Mouse'")
    c.execute("DELETE FROM productos WHERE id = 3")
    conn.commit()

    print("--- RESULTADO ---")
    for row in c.execute("SELECT * FROM productos ORDER BY id"):
        print(f"  {row}")

    print()
    print("--- EXPLICACION ---")
    print("""
UPDATE modifica filas existentes:
  - SET columna = valor  → que columna cambiar
  - WHERE condicion      → que filas afectar
  - SIN WHERE se actualizarian TODAS las filas. ¡Peligro!

DELETE elimina filas:
  - WHERE condicion → que filas eliminar
  - SIN WHERE se vaciaria la tabla entera. ¡Peligro!

Buenas practicas:
  1. Siempre hacer SELECT primero para ver que filas afecta el WHERE
  2. Hacer backup antes de UPDATE/DELETE masivos
  3. Usar transacciones (BEGIN/COMMIT) para poder hacer ROLLBACK
""")


if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
