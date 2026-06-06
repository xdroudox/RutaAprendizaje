"""
EJERCICIOS - SQL Fundamentos
Ejecuta desde raiz: python scripts/runner.py 4 1 [ejercicio]

Niveles:
  🟢 Ej 1: SELECT con WHERE (usuarios > 25)
  🟡 Ej 2: INSERT INTO (nuevo producto)
  🔴 Ej 3: UPDATE y DELETE

Pistas: python scripts/runner.py 4 1 N -p [1|2|3]
"""

import sys
import sqlite3

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1(pista=0):
    """🟢 SELECT con WHERE (usuarios > 25)"""
    print(">> 🟢 EJERCICIO 1: SELECT con WHERE")
    print("-" * 50)

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
    for row in c.execute("SELECT * FROM usuarios"):
        print(f"  {row[0]}  | {row[1]:6s} | {row[2]}")

    if pista == 1:
        print("\n💡 Pista 1: La sintaxis basica de SELECT con WHERE es:")
        print("  SELECT columnas FROM tabla WHERE condicion")
        print("  Para comparar edad: WHERE edad > 25")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  Tu consulta debe ser algo como:")
        print("  SELECT * FROM usuarios WHERE ...")
        return
    elif pista == 3:
        print("\n💡 Pista 3:")
        print("  SELECT * FROM usuarios WHERE edad > 25")
        return

    print("\nEscribe una consulta SELECT que muestre los usuarios con edad > 25:")
    print("# ==== ESCRIBE TU CONSULTA SQL AQUI ====")


def ejercicio_2(pista=0):
    """🟡 INSERT INTO (nuevo producto)"""
    print(">> 🟡 EJERCICIO 2: INSERT INTO")
    print("-" * 50)

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
        print(f"  {row}")

    if pista == 1:
        print("\n💡 Pista 1: Sintaxis basica de INSERT:")
        print("  INSERT INTO tabla VALUES (val1, val2, ...)")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  INSERT INTO productos VALUES (4, 'Monitor', 299.99, 15)")
        return
    elif pista == 3:
        print("\n💡 Pista 3:")
        print("  Despues del INSERT, ejecuta con c.execute(query)")
        print("  y haz conn.commit() para guardar los cambios.")
        print("  Luego verifica con SELECT * FROM productos")
        return

    print("\nAgrega un nuevo producto:")
    print("  id=4, nombre='Monitor', precio=299.99, stock=15")
    print()
    print("# ==== ESCRIBE TU CONSULTA SQL AQUI ====")


def ejercicio_3(pista=0):
    """🔴 UPDATE y DELETE"""
    print(">> 🔴 EJERCICIO 3: UPDATE y DELETE")
    print("-" * 50)

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
        print(f"  {row}")

    if pista == 1:
        print("\n💡 Pista 1: Sintaxis:")
        print("  UPDATE: UPDATE productos SET precio = X WHERE nombre = 'Y'")
        print("  DELETE: DELETE FROM productos WHERE id = Z")
        print("  ¡Siempre usa WHERE o afectaras TODAS las filas!")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  UPDATE productos SET precio = 30.00 WHERE nombre = 'Mouse'")
        print("  DELETE FROM productos WHERE id = 3")
        return
    elif pista == 3:
        print("\n💡 Pista 3:")
        print("  Despues de UPDATE y DELETE, haz conn.commit()")
        print("  y verifica con SELECT * FROM productos ORDER BY id")
        return

    print("\nRealiza las siguientes operaciones:")
    print("  1. Actualiza el precio del 'Mouse' a 30.00")
    print("  2. Elimina el producto con id=3 ('Teclado')")
    print()
    print("# ==== ESCRIBE TUS CONSULTAS SQL AQUI ====")


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
