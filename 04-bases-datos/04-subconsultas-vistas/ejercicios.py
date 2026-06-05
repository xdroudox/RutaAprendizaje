"""
EJERCICIOS - Subconsultas y Vistas
Ejecuta desde raiz: python scripts/runner.py 4 4 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Escribe una subconsulta en WHERE: empleados con salario mayor al promedio"""
    import sqlite3
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE empleados (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            salario REAL NOT NULL,
            departamento TEXT NOT NULL
        );
        INSERT INTO empleados VALUES
            (1, 'Ana', 50000, 'Ventas'),
            (2, 'Juan', 60000, 'TI'),
            (3, 'Maria', 45000, 'Ventas'),
            (4, 'Carlos', 70000, 'TI'),
            (5, 'Laura', 55000, 'RRHH');
    """)
    conn.commit()
    print("=== Empleados ===")
    for row in c.execute("SELECT * FROM empleados"):
        print(f"  {row[0]:<3} {row[1]:<8} ${row[2]:>6}  {row[3]}")
    print()
    prom = c.execute("SELECT AVG(salario) FROM empleados").fetchone()[0]
    print(f"Salario promedio: ${prom:.2f}")
    print()
    # ==== ESCRIBE TU CONSULTA SQL AQUI ====
    # query = "SELECT * FROM empleados WHERE salario > (SELECT AVG(salario) FROM empleados)"
    # c.execute(query)
    # for row in c.fetchall():
    #     print(row)
    pass

def ejercicio_2():
    """Escribe una subconsulta en FROM: usa una subconsulta como tabla temporal"""
    import sqlite3
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE ventas (
            id INTEGER PRIMARY KEY,
            producto TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            total REAL NOT NULL,
            fecha TEXT NOT NULL
        );
        INSERT INTO ventas VALUES
            (1, 'Laptop', 2, 1999.98, '2024-01-15'),
            (2, 'Mouse', 5, 127.50, '2024-01-15'),
            (3, 'Laptop', 1, 999.99, '2024-02-10'),
            (4, 'Teclado', 3, 135.00, '2024-02-10'),
            (5, 'Mouse', 2, 51.00, '2024-03-05');
    """)
    conn.commit()
    print("=== Ventas ===")
    for row in c.execute("SELECT * FROM ventas"):
        print(f"  {row}")
    print()
    print("Usa una subconsulta en FROM para obtener el total vendido por producto")
    # ==== ESCRIBE TU CONSULTA SQL AQUI ====
    # query = "SELECT producto, total_vendido FROM (SELECT producto, SUM(total) as total_vendido FROM ventas GROUP BY producto) ORDER BY total_vendido DESC"
    pass

def ejercicio_3():
    """Crea una VIEW y consultala para obtener empleados de TI con salario alto"""
    import sqlite3
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE empleados (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            salario REAL NOT NULL,
            departamento TEXT NOT NULL
        );
        INSERT INTO empleados VALUES
            (1, 'Ana', 50000, 'Ventas'),
            (2, 'Juan', 60000, 'TI'),
            (3, 'Maria', 45000, 'Ventas'),
            (4, 'Carlos', 70000, 'TI'),
            (5, 'Laura', 55000, 'TI');
    """)
    conn.commit()
    print("=== Empleados ===")
    for row in c.execute("SELECT * FROM empleados"):
        print(f"  {row}")
    print()
    print("Crea una vista 'empleados_ti' que muestre solo los de TI con salario >= 55000")
    print("Luego consultala")
    # ==== ESCRIBE TU CONSULTA SQL AQUI ====
    # c.execute("CREATE VIEW empleados_ti AS SELECT ... FROM empleados WHERE ... AND ...")
    # for row in c.execute("SELECT * FROM empleados_ti"):
    #     print(row)
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
