"""
EJERCICIOS - SQL Fundamentos
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
    print("=== Tabla: usuarios ===")
    print("id | nombre | edad")
    print("---|--------|-----")
    for row in c.execute("SELECT * FROM usuarios"):
        print(f" {row[0]}  | {row[1]:6s} | {row[2]}")
    print()
    # ==== ESCRIBE TU CONSULTA SQL AQUI ====
    # query = "SELECT * FROM usuarios WHERE ..."
    # c.execute(query)
    # for row in c.fetchall():
    #     print(row)
    pass

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
    print("=== Productos actuales ===")
    for row in c.execute("SELECT * FROM productos"):
        print(row)
    print()
    print("Agrega un nuevo producto (id=4, nombre='Monitor', precio=299.99, stock=15)")
    # ==== ESCRIBE TU CONSULTA SQL AQUI ====
    # query = "INSERT INTO productos VALUES (...)"
    # c.execute(query)
    # conn.commit()
    # for row in c.execute("SELECT * FROM productos"):
    #     print(row)
    pass

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
    print("=== Productos actuales ===")
    for row in c.execute("SELECT * FROM productos"):
        print(row)
    print()
    print("1. Actualiza el precio del 'Mouse' a 30.00")
    print("2. Elimina el producto con id=3 ('Teclado')")
    print()
    # ==== ESCRIBE TU CONSULTA SQL AQUI ====
    # c.execute("UPDATE productos SET precio = ... WHERE ...")
    # c.execute("DELETE FROM productos WHERE ...")
    # conn.commit()
    # for row in c.execute("SELECT * FROM productos ORDER BY id"):
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
