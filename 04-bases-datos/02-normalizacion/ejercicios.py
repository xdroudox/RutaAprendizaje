"""
EJERCICIOS - Normalizacion
Ejecuta desde raiz: python scripts/runner.py 4 2 [ejercicio]

Niveles:
  🟢 Ej 1: Identificar y corregir 1FN
  🟡 Ej 2: Normalizar a 2FN
  🔴 Ej 3: Normalizar a 3FN

Pistas: python scripts/runner.py 4 2 N -p [1|2|3]
"""

import sys
import sqlite3

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1(pista=0):
    """🟢 Identificar y corregir 1FN"""
    print(">> 🟢 EJERCICIO 1: Identificar y corregir 1FN")
    print("-" * 50)

    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE estudiantes (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            cursos TEXT NOT NULL
        );
        INSERT INTO estudiantes VALUES (1, 'Ana', 'Matematicas,Historia');
        INSERT INTO estudiantes VALUES (2, 'Juan', 'Ciencias,Arte,Musica');
        INSERT INTO estudiantes VALUES (3, 'Maria', 'Historia,Ciencias');
    """)
    conn.commit()

    print("=== Tabla actual (viola 1FN) ===")
    for row in c.execute("SELECT * FROM estudiantes"):
        print(f"  {row[0]} | {row[1]:6s} | {row[2]}")

    if pista == 1:
        print("\n💡 Pista 1: 1FN requiere columnas ATOMICAS.")
        print("  'cursos' contiene multiples valores → violacion.")
        print("  Solucion: crear tablas estudiantes, cursos, y una")
        print("  tabla intermedia estudiante_curso.")
        return
    elif pista == 2:
        print("\n💡 Pista 2: Necesitas 3 tablas:")
        print("  estudiantes(id, nombre)")
        print("  cursos(id, nombre)")
        print("  estudiante_curso(estudiante_id, curso_id)")
        print("  Con PRIMARY KEY compuesta y FOREIGN KEYs")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Esquema completo:")
        print("""
  CREATE TABLE estudiantes (id INTEGER PRIMARY KEY, nombre TEXT);
  CREATE TABLE cursos (id INTEGER PRIMARY KEY, nombre TEXT);
  CREATE TABLE estudiante_curso (
      estudiante_id INTEGER,
      curso_id INTEGER,
      PRIMARY KEY (estudiante_id, curso_id),
      FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id),
      FOREIGN KEY (curso_id) REFERENCES cursos(id)
  );
""")
        return

    print("\nProblema: columna 'cursos' tiene multiples valores (viola 1FN).")
    print("Disena el esquema normalizado con CREATE TABLE.")
    print()
    print("# ==== ESCRIBE TU ESQUEMA SQL AQUI ====")


def ejercicio_2(pista=0):
    """🟡 Normalizar a 2FN"""
    print(">> 🟡 EJERCICIO 2: Normalizar a 2FN")
    print("-" * 50)

    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE calificaciones (
            estudiante_id INTEGER,
            estudiante_nombre TEXT,
            curso_id INTEGER,
            curso_nombre TEXT,
            profesor TEXT,
            nota REAL,
            PRIMARY KEY (estudiante_id, curso_id)
        );
        INSERT INTO calificaciones VALUES
            (1, 'Ana', 101, 'Matematicas', 'Dr. Lopez', 8.5),
            (1, 'Ana', 102, 'Historia', 'Dra. Perez', 9.0),
            (2, 'Juan', 101, 'Matematicas', 'Dr. Lopez', 7.5),
            (2, 'Juan', 103, 'Ciencias', 'Dr. Garcia', 8.0);
    """)
    conn.commit()

    print("=== Tabla actual (viola 2FN) ===")
    for row in c.execute("SELECT * FROM calificaciones"):
        print(f"  {row}")

    if pista == 1:
        print("\n💡 Pista 1: Dependencias parciales:")
        print("  estudiante_nombre depende SOLO de estudiante_id")
        print("  curso_nombre y profesor dependen SOLO de curso_id")
        return
    elif pista == 2:
        print("\n💡 Pista 2: 2FN requiere 3 tablas:")
        print("  estudiantes(id, nombre)")
        print("  cursos(id, nombre, profesor)")
        print("  calificaciones(estudiante_id, curso_id, nota)")
        print("  PK compuesta en calificaciones, FK a las otras")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Esquema completo 2FN:")
        print("""
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
""")
        return

    print("\nProblema: dependencias parciales (viola 2FN).")
    print("Crea tablas separadas: estudiantes, cursos, calificaciones.")
    print()
    print("# ==== ESCRIBE TU ESQUEMA SQL AQUI ====")


def ejercicio_3(pista=0):
    """🔴 Normalizar a 3FN"""
    print(">> 🔴 EJERCICIO 3: Normalizar a 3FN")
    print("-" * 50)

    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE pedidos (
            pedido_id INTEGER PRIMARY KEY,
            cliente_id INTEGER,
            cliente_nombre TEXT,
            cliente_ciudad TEXT,
            producto TEXT,
            cantidad INTEGER,
            total REAL
        );
        INSERT INTO pedidos VALUES
            (1, 1, 'Ana', 'Madrid', 'Laptop', 1, 999.99),
            (2, 2, 'Juan', 'Barcelona', 'Mouse', 2, 51.00),
            (3, 1, 'Ana', 'Madrid', 'Teclado', 1, 45.00),
            (4, 3, 'Maria', 'Valencia', 'Monitor', 2, 599.98);
    """)
    conn.commit()

    print("=== Tabla actual (viola 3FN) ===")
    for row in c.execute("SELECT * FROM pedidos"):
        print(f"  {row}")

    if pista == 1:
        print("\n💡 Pista 1: Dependencia transitiva:")
        print("  pedido_id → cliente_id → cliente_nombre")
        print("  pedido_id → cliente_id → cliente_ciudad")
        return
    elif pista == 2:
        print("\n💡 Pista 2: 3FN requiere 2 tablas:")
        print("  clientes(id, nombre, ciudad)")
        print("  pedidos(id, cliente_id, producto, cantidad, total)")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Esquema completo 3FN:")
        print("""
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
""")
        return

    print("\nProblema: dependencias transitivas (viola 3FN).")
    print("Crea tablas separadas: clientes, pedidos.")
    print()
    print("# ==== ESCRIBE TU ESQUEMA SQL AQUI ====")


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
