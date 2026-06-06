"""
SOLUCIONES - Indices y Optimizacion
Ejecuta: python scripts/runner.py 4 6 [ejercicio] -s
"""

import sys
import sqlite3

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: CREATE INDEX + EXPLAIN QUERY PLAN")
    print("=" * 50)

    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE productos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            categoria TEXT NOT NULL,
            precio REAL NOT NULL
        );
    """)
    categorias = ['Electronica', 'Hogar', 'Deportes', 'Jugueteria']
    for i in range(1, 1001):
        cat = categorias[i % len(categorias)]
        c.execute("INSERT INTO productos VALUES (?, ?, ?, ?)",
                  (i, f'Producto{i}', cat, round(i * 1.5, 2)))
    conn.commit()

    print("--- SIN INDICE ---")
    print("EXPLAIN QUERY PLAN SELECT * FROM productos WHERE categoria = 'Electronica';")
    for row in c.execute("EXPLAIN QUERY PLAN SELECT * FROM productos WHERE categoria = 'Electronica'"):
        print(f"  {row}")
    print()

    c.execute("CREATE INDEX idx_categoria ON productos(categoria)")

    print("--- CON INDICE ---")
    print("CREATE INDEX idx_categoria ON productos(categoria);")
    for row in c.execute("EXPLAIN QUERY PLAN SELECT * FROM productos WHERE categoria = 'Electronica'"):
        print(f"  {row}")

    print()
    print("--- EXPLICACION ---")
    print("""
Sin indice: SCAN (recorre TODAS las filas una por una) → O(n)
Con indice: SEARCH ... USING INDEX (busqueda por arbol B+) → O(log n)

EXPLAIN QUERY PLAN muestra como SQLite ejecutara la consulta:
  - SCAN: Recorre toda la tabla (lento en tablas grandes)
  - SEARCH: Usa un indice para encontrar rapido los registros

Diferencia practica:
  - 1000 productos: SCAN = 1000 comparaciones, SEARCH ≈ 10 comparaciones
  - 1M productos:  SCAN = 1M comparaciones, SEARCH ≈ 20 comparaciones

El indice es como el indice de un libro: en lugar de leer pagina
por pagina, vas directamente a la seccion que te interesa.
""")


def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: Comparacion temporal CON vs SIN indice")
    print("=" * 50)

    import time
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE usuarios (
            id INTEGER PRIMARY KEY,
            email TEXT NOT NULL,
            nombre TEXT NOT NULL
        );
    """)
    for i in range(1, 10001):
        c.execute("INSERT INTO usuarios VALUES (?, ?, ?)",
                  (i, f'usuario{i}@email.com', f'Nombre{i}'))
    conn.commit()

    def medir(query):
        inicio = time.time()
        c.execute(query)
        c.fetchall()
        return time.time() - inicio

    print("--- CODIGO ---")
    print("def medir(query):")
    print("    inicio = time.time()")
    print("    c.execute(query)")
    print("    c.fetchall()")
    print("    return time.time() - inicio")
    print()

    print("  Sin indice:")
    print("    SELECT * FROM usuarios WHERE email = 'usuario9999@email.com'")
    t1 = medir("SELECT * FROM usuarios WHERE email = 'usuario9999@email.com'")
    print(f"    {t1:.4f} seg")
    print()

    c.execute("CREATE INDEX idx_email ON usuarios(email)")
    print("  Con indice:")
    print("    CREATE INDEX idx_email ON usuarios(email)")
    t2 = medir("SELECT * FROM usuarios WHERE email = 'usuario9999@email.com'")
    print(f"    {t2:.4f} seg")
    print()
    print(f"  Mejora: {t1/t2:.1f}x mas rapido")

    print()
    print("--- EXPLICACION ---")
    print("""
Con solo 10,000 registros la mejora es modesta (3-10x).
Pero la diferencia crece exponencialmente con mas datos:

  Registros   | Sin indice | Con indice
  1,000       |   0.001s   |   0.001s   (apenas perceptible)
  100,000     |   0.050s   |   0.002s   (25x mas rapido)
  10,000,000  |   5.000s   |   0.020s   (250x mas rapido)

Razon: SCAN es O(n) y SEARCH con arbol B+ es O(log n).

Costo del indice:
  - Ocupa espacio en disco (tipicamente 20-50% del tamano de la tabla)
  - Ralentiza INSERT/UPDATE/DELETE (hay que actualizar el arbol)
  - No conviene indexar columnas con pocos valores distintos
""")


def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: Optimizar queries con indices")
    print("=" * 50)

    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE pedidos (
            id INTEGER PRIMARY KEY,
            cliente_id INTEGER NOT NULL,
            fecha TEXT NOT NULL,
            total REAL NOT NULL,
            estado TEXT NOT NULL
        );
    """)
    for i in range(1, 5001):
        c.execute("INSERT INTO pedidos VALUES (?, ?, ?, ?, ?)",
                  (i, (i % 100) + 1, f'2024-{(i % 12) + 1:02d}-{(i % 28) + 1:02d}',
                   round(i * 10.0, 2), ['pendiente', 'enviado', 'entregado'][i % 3]))
    conn.commit()

    print("--- INDICES CREADOS ---")
    print("CREATE INDEX idx_estado ON pedidos(estado);")
    print("CREATE INDEX idx_cliente ON pedidos(cliente_id);")
    print("CREATE INDEX idx_fecha ON pedidos(fecha);")
    print()

    c.execute("CREATE INDEX idx_estado ON pedidos(estado)")
    c.execute("CREATE INDEX idx_cliente ON pedidos(cliente_id)")
    c.execute("CREATE INDEX idx_fecha ON pedidos(fecha)")

    print("--- EXPLAIN CON INDICES ---")
    queries = [
        ("WHERE estado = 'pendiente'", "SELECT * FROM pedidos WHERE estado = 'pendiente'"),
        ("WHERE cliente_id = 50", "SELECT * FROM pedidos WHERE cliente_id = 50"),
        ("WHERE fecha BETWEEN", "SELECT * FROM pedidos WHERE fecha BETWEEN '2024-01-01' AND '2024-03-01'"),
    ]
    for i, (desc, q) in enumerate(queries, 1):
        print(f"Query {i} ({desc}):")
        for row in c.execute(f"EXPLAIN QUERY PLAN {q}"):
            print(f"  {row}")
        print()

    print("--- EXPLICACION ---")
    print("""
Reglas para elegir que columnas indexar:

✅ BUENOS candidatos para indice:
  - Columnas usadas en WHERE (filtros frecuentes)
  - Columnas usadas en JOIN (claves foraneas)
  - Columnas usadas en ORDER BY
  - Columnas con alta cardinalidad (muchos valores distintos)

❌ MALOS candidatos para indice:
  - Columnas raramente usadas en consultas
  - Columnas con pocos valores (ej. booleano, genero)
  - Tablas muy pequenas (< 1000 registros)
  - Tablas con muchas escrituras y pocas lecturas

En este ejercicio, las 3 columnas (estado, cliente_id, fecha)
son buenos candidatos porque se usan frecuentemente en WHERE.
""")


if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
