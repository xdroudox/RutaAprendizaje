"""
SOLUCIONES - SQL Fundamentos
Ejecuta desde raiz: python scripts/runner.py 4 1 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Escribe una consulta SELECT que muestre los usuarios mayores de 25"""
    import sqlite3
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
    print(">>> Usuarios mayores de 25:")
    query = "SELECT * FROM usuarios WHERE edad > 25"
    c.execute(query)
    for row in c.fetchall():
        print(f"  {row[0]:<3} {row[1]:<8} {row[2]} anos")

def ejercicio_2():
    """Escribe un INSERT INTO para agregar un nuevo producto"""
    import sqlite3
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
    print(">>> Agregando Monitor (id=4, precio=299.99, stock=15):")
    query = "INSERT INTO productos VALUES (4, 'Monitor', 299.99, 15)"
    c.execute(query)
    conn.commit()
    for row in c.execute("SELECT * FROM productos"):
        print(f"  {row}")

def ejercicio_3():
    """Escribe un UPDATE para aumentar precio y un DELETE para eliminar un registro"""
    import sqlite3
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
    print(">>> Actualizando Mouse a 30.00 y eliminando Teclado (id=3):")
    c.execute("UPDATE productos SET precio = 30.00 WHERE nombre = 'Mouse'")
    c.execute("DELETE FROM productos WHERE id = 3")
    conn.commit()
    for row in c.execute("SELECT * FROM productos ORDER BY id"):
        print(f"  {row}")

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
