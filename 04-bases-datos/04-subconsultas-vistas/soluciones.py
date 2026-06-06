"""
SOLUCIONES - Subconsultas y Vistas
Ejecuta: python scripts/runner.py 4 4 [ejercicio] -s
"""

import sys
import sqlite3

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: Subconsulta en WHERE")
    print("=" * 50)

    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE empleados (id INTEGER PRIMARY KEY, nombre TEXT, salario REAL, departamento TEXT);
        INSERT INTO empleados VALUES
            (1, 'Ana', 50000, 'Ventas'), (2, 'Juan', 60000, 'TI'),
            (3, 'Maria', 45000, 'Ventas'), (4, 'Carlos', 70000, 'TI'),
            (5, 'Laura', 55000, 'RRHH');
    """)

    print("--- CONSULTA ---")
    print("SELECT * FROM empleados")
    print("WHERE salario > (SELECT AVG(salario) FROM empleados);")
    print()

    query = "SELECT * FROM empleados WHERE salario > (SELECT AVG(salario) FROM empleados)"
    for r in c.execute(query):
        print(f"  {r[0]:<3} {r[1]:<8} ${r[2]:>6}  {r[3]}")

    print()
    print("--- EXPLICACION ---")
    print("""
La subconsulta se ejecuta PRIMERO:
  (SELECT AVG(salario) FROM empleados) → 56000

Luego la consulta principal usa ese valor:
  WHERE salario > 56000

Solo Juan (60000) y Carlos (70000) cumplen.
Ana (50000), Maria (45000) y Laura (55000) NO.

Las subconsultas en WHERE pueden usar:
  =, >, <, >=, <=, != con subconsultas que devuelven 1 valor
  IN, NOT IN con subconsultas que devuelven varios valores
  EXISTS, NOT EXISTS para verificar existencia
""")


def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: Subconsulta en FROM")
    print("=" * 50)

    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE ventas (id INTEGER PRIMARY KEY, producto TEXT, cantidad INTEGER, total REAL, fecha TEXT);
        INSERT INTO ventas VALUES
            (1, 'Laptop', 2, 1999.98, '2024-01-15'), (2, 'Mouse', 5, 127.50, '2024-01-15'),
            (3, 'Laptop', 1, 999.99, '2024-02-10'), (4, 'Teclado', 3, 135.00, '2024-02-10'),
            (5, 'Mouse', 2, 51.00, '2024-03-05');
    """)

    print("--- CONSULTA ---")
    print("SELECT producto, total_vendido")
    print("FROM (SELECT producto, SUM(total) AS total_vendido")
    print("      FROM ventas GROUP BY producto)")
    print("ORDER BY total_vendido DESC;")
    print()

    query = """SELECT producto, total_vendido FROM
               (SELECT producto, SUM(total) AS total_vendido FROM ventas GROUP BY producto)
               ORDER BY total_vendido DESC"""
    for r in c.execute(query):
        print(f"  {r[0]:<10} ${r[1]:>7.2f}")

    print()
    print("--- EXPLICACION ---")
    print("""
La subconsulta en FROM crea una TABLA DERIVADA temporal:

Subconsulta interna:
  SELECT producto, SUM(total) AS total_vendido
  FROM ventas GROUP BY producto
  → (Laptop, 2999.97), (Mouse, 178.50), (Teclado, 135.00)

Consulta externa:
  Ordena por total_vendido DESC

Esto es util cuando necesitas trabajar con resultados agregados
como si fueran una tabla normal.
""")


def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: Crear y consultar una VIEW")
    print("=" * 50)

    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE empleados (id INTEGER PRIMARY KEY, nombre TEXT, salario REAL, departamento TEXT);
        INSERT INTO empleados VALUES
            (1, 'Ana', 50000, 'Ventas'), (2, 'Juan', 60000, 'TI'),
            (3, 'Maria', 45000, 'Ventas'), (4, 'Carlos', 70000, 'TI'),
            (5, 'Laura', 55000, 'TI');
    """)

    print("--- CONSULTA ---")
    print("CREATE VIEW empleados_ti AS")
    print("SELECT * FROM empleados")
    print("WHERE departamento = 'TI' AND salario >= 55000;")
    print()
    print("SELECT * FROM empleados_ti;")
    print()

    c.execute("CREATE VIEW empleados_ti AS SELECT * FROM empleados WHERE departamento = 'TI' AND salario >= 55000")
    for r in c.execute("SELECT * FROM empleados_ti"):
        print(f"  {r[0]:<3} {r[1]:<8} ${r[2]:>6}  {r[3]}")

    print()
    print("--- EXPLICACION ---")
    print("""
CREATE VIEW guarda la consulta como una "tabla virtual":
  - No almacena datos fisicos, solo la definicion
  - Cada vez que consultas la vista, se ejecuta la consulta subyacente
  - Puedes usarla como cualquier tabla en SELECTs, JOINs, etc.

Ventajas de vistas:
  1. SIMPLIFICAR: ocultar joins complejos
  2. SEGURIDAD: mostrar solo ciertas columnas/filas
  3. CONSISTENCIA: misma definicion para todos los usuarios
  4. MANTENIBILIDAD: cambiar la consulta en 1 lugar

Limitaciones:
  - No todas las vistas son actualizables (INSERT/UPDATE/DELETE)
  - Depende de las tablas base (si las tablas cambian, la vista se rompe)
""")


if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
