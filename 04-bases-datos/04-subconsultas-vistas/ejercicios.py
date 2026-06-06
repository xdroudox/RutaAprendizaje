"""
EJERCICIOS - Subconsultas y Vistas
Ejecuta desde raiz: python scripts/runner.py 4 4 [ejercicio]

Niveles:
  🟢 Ej 1: Subconsulta en WHERE (salario > promedio)
  🟡 Ej 2: Subconsulta en FROM (total por producto)
  🔴 Ej 3: Crear y consultar una VIEW

Pistas: python scripts/runner.py 4 4 N -p [1|2|3]
"""

import sys
import sqlite3

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1(pista=0):
    """🟢 Subconsulta en WHERE (salario > promedio)"""
    print(">> 🟢 EJERCICIO 1: Subconsulta en WHERE")
    print("-" * 50)

    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE empleados (id INTEGER PRIMARY KEY, nombre TEXT, salario REAL, departamento TEXT);
        INSERT INTO empleados VALUES
            (1, 'Ana', 50000, 'Ventas'), (2, 'Juan', 60000, 'TI'),
            (3, 'Maria', 45000, 'Ventas'), (4, 'Carlos', 70000, 'TI'),
            (5, 'Laura', 55000, 'RRHH');
    """)
    conn.commit()

    print("=== Empleados ===")
    for r in c.execute("SELECT * FROM empleados"):
        print(f"  {r[0]:<3} {r[1]:<8} ${r[2]:>6}  {r[3]}")
    prom = c.execute("SELECT AVG(salario) FROM empleados").fetchone()[0]
    print(f"\nSalario promedio: ${prom:.2f}")

    if pista == 1:
        print("\n💡 Pista 1: La subconsulta calcula el promedio:")
        print("  (SELECT AVG(salario) FROM empleados)")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  SELECT * FROM empleados")
        print("  WHERE salario > (SELECT AVG(salario) FROM empleados)")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Resultado esperado:")
        print("  Juan (60000), Carlos (70000)")
        print("  Ana (50000) y Maria (45000) estan por debajo")
        print("  Laura (55000) esta justo en el promedio (56000)? No, 55000 < 56000")
        return

    print("\nMuestra empleados con salario mayor al promedio:")
    print("# ==== ESCRIBE TU CONSULTA AQUI ====")


def ejercicio_2(pista=0):
    """🟡 Subconsulta en FROM (total por producto)"""
    print(">> 🟡 EJERCICIO 2: Subconsulta en FROM")
    print("-" * 50)

    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE ventas (id INTEGER PRIMARY KEY, producto TEXT, cantidad INTEGER, total REAL, fecha TEXT);
        INSERT INTO ventas VALUES
            (1, 'Laptop', 2, 1999.98, '2024-01-15'), (2, 'Mouse', 5, 127.50, '2024-01-15'),
            (3, 'Laptop', 1, 999.99, '2024-02-10'), (4, 'Teclado', 3, 135.00, '2024-02-10'),
            (5, 'Mouse', 2, 51.00, '2024-03-05');
    """)
    conn.commit()

    print("=== Ventas ===")
    for r in c.execute("SELECT * FROM ventas"): print(f"  {r}")

    if pista == 1:
        print("\n💡 Pista 1: La subconsulta agrupa y suma:")
        print("  SELECT producto, SUM(total) AS total_vendido")
        print("  FROM ventas GROUP BY producto")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  SELECT producto, total_vendido")
        print("  FROM (SELECT producto, SUM(total) AS total_vendido")
        print("        FROM ventas GROUP BY producto)")
        print("  ORDER BY total_vendido DESC")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Resultado:")
        print("  Laptop  = 1999.98 + 999.99 = 2999.97")
        print("  Mouse   = 127.50 + 51.00 = 178.50")
        print("  Teclado = 135.00")
        return

    print("\nObtén el total vendido por producto (subconsulta en FROM):")
    print("# ==== ESCRIBE TU CONSULTA AQUI ====")


def ejercicio_3(pista=0):
    """🔴 Crear y consultar una VIEW"""
    print(">> 🔴 EJERCICIO 3: Crear y consultar una VIEW")
    print("-" * 50)

    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE empleados (id INTEGER PRIMARY KEY, nombre TEXT, salario REAL, departamento TEXT);
        INSERT INTO empleados VALUES
            (1, 'Ana', 50000, 'Ventas'), (2, 'Juan', 60000, 'TI'),
            (3, 'Maria', 45000, 'Ventas'), (4, 'Carlos', 70000, 'TI'),
            (5, 'Laura', 55000, 'TI');
    """)
    conn.commit()

    print("=== Empleados ===")
    for r in c.execute("SELECT * FROM empleados"): print(f"  {r}")

    if pista == 1:
        print("\n💡 Pista 1: Crear vista:")
        print("  CREATE VIEW empleados_ti AS")
        print("  SELECT * FROM empleados")
        print("  WHERE departamento = 'TI' AND salario >= 55000")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  1. CREATE VIEW empleados_ti AS ...")
        print("  2. SELECT * FROM empleados_ti")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Resultado:")
        print("  Juan (60000, TI), Carlos (70000, TI)")
        print("  Laura (55000, TI) tambien porque >= 55000")
        print("  Ana y Maria no son de TI")
        return

    print("\nCrea una vista 'empleados_ti' solo con TI de salario >= 55000.")
    print("Luego consultala con SELECT.")
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
