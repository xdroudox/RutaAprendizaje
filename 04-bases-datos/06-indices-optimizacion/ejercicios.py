"""
EJERCICIOS - Indices y Optimizacion
Ejecuta desde raiz: python scripts/runner.py 4 6 [ejercicio]

Niveles:
  🟢 Ej 1: CREATE INDEX + EXPLAIN QUERY PLAN
  🟡 Ej 2: Comparacion temporal CON vs SIN indice
  🔴 Ej 3: Identificar queries lentas y proponer indices

Pistas: python scripts/runner.py 4 6 N -p [1|2|3]
"""

import sys
import sqlite3

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1(pista=0):
    """🟢 CREATE INDEX + EXPLAIN QUERY PLAN"""
    print(">> 🟢 EJERCICIO 1: Crear un indice y analizar su efecto")
    print("-" * 50)

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

    print("=== EXPLAIN QUERY PLAN - SIN indice ===")
    for row in c.execute("EXPLAIN QUERY PLAN SELECT * FROM productos WHERE categoria = 'Electronica'"):
        print(f"  {row}")

    if pista == 1:
        print("\n💡 Pista 1: Crea un indice sobre la columna 'categoria':")
        print("  CREATE INDEX idx_categoria ON productos(categoria)")
        return
    elif pista == 2:
        print("\n💡 Pista 2: Despues de crear el indice, repite el EXPLAIN:")
        print("  c.execute('CREATE INDEX idx_categoria ON productos(categoria)')")
        print("  c.execute('EXPLAIN QUERY PLAN SELECT * FROM productos WHERE categoria = ...')")
        print("  Nota: 'SEARCH' (con indice) vs 'SCAN' (sin indice)")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Resultado esperado:")
        print("  SIN indice:  SCAN productos (busqueda linea por linea)")
        print("  CON indice:  SEARCH productos USING INDEX idx_categoria")
        print("  La diferencia es que SEARCH es O(log n) vs SCAN es O(n)")
        return

    print("\n1. Crea un indice llamado 'idx_categoria' sobre la columna 'categoria'")
    print("2. Vuelve a ejecutar EXPLAIN QUERY PLAN para ver como cambio la estrategia")
    print("\n# ==== ESCRIBE TU CONSULTA AQUI ====")


def ejercicio_2(pista=0):
    """🟡 Comparacion temporal CON vs SIN indice"""
    print(">> 🟡 EJERCICIO 2: Medir velocidad con y sin indice")
    print("-" * 50)

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

    if pista == 1:
        print("\n💡 Pista 1: Crea una funcion para medir tiempo:")
        print("  def medir(query):")
        print("      inicio = time.time()")
        print("      c.execute(query)")
        print("      c.fetchall()")
        print("      return time.time() - inicio")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  1. Mide sin indice:  SELECT * FROM usuarios WHERE email = 'usuario9999@email.com'")
        print("  2. CREATE INDEX idx_email ON usuarios(email)")
        print("  3. Mide con indice:  misma consulta")
        print("  Nota: 10000 registros es poco para ver gran diferencia")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Resultado esperado:")
        print("  Sin indice: ~0.003-0.010 seg (SCAN completo)")
        print("  Con indice: ~0.001-0.003 seg (SEARCH por arbol)")
        print("  Mejora: 3-10x mas rapido")
        print("  Con 1M de registros, la diferencia seria dramatica")
        return

    print("Compara la velocidad de busqueda por email:")
    print("  1. Mide tiempo SIN indice")
    print("  2. Crea CREATE INDEX idx_email ON usuarios(email)")
    print("  3. Mide tiempo CON indice (misma consulta)")
    print("  4. Muestra la mejora X veces")
    print("\n# ==== ESCRIBE TU CODIGO AQUI ====")


def ejercicio_3(pista=0):
    """🔴 Identificar queries lentas y proponer indices"""
    print(">> 🔴 EJERCICIO 3: Optimizar queries con indices")
    print("-" * 50)

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

    print("=== EXPLAIN de queries sin optimizar ===")
    print()
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

    if pista == 1:
        print("\n💡 Pista 1: Observa que TODAS usan SCAN (sin indice)")
        print("  Cada columna usada en WHERE se beneficia de un indice:")
        print("    - CREATE INDEX idx_estado ON pedidos(estado)")
        print("    - CREATE INDEX idx_cliente ON pedidos(cliente_id)")
        print("    - CREATE INDEX idx_fecha ON pedidos(fecha)")
        return
    elif pista == 2:
        print("\n💡 Pista 2: Despues de crear los 3 indices:")
        print("  Vuelve a ejecutar los 3 EXPLAIN QUERY PLAN")
        print("  Veras SEARCH en lugar de SCAN para cada uno")
        print("  Si usas '=' el indice busca exacto (mas rapido)")
        print("  Si usas 'BETWEEN' el indice busca por rango (tambien optimo)")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Resultado esperado (EXPLAIN):")
        print("  Query 1: SEARCH pedidos USING INDEX idx_estado")
        print("  Query 2: SEARCH pedidos USING INDEX idx_cliente")
        print("  Query 3: SEARCH pedidos USING INDEX idx_fecha")
        print("  Nota: Los indices NO son gratis (ocupan espacio, ralentizan INSERT/UPDATE)")
        print("  Solo indexa columnas que uses FRECUENTEMENTE en WHERE, JOIN u ORDER BY")
        return

    print("Analiza las 3 queries y propon indices para optimizarlas:")
    print("  1. Identifica que columnas se usan en WHERE")
    print("  2. Crea CREATE INDEX para cada columna relevante")
    print("  3. Vuelve a ejecutar EXPLAIN para confirmar la mejora")
    print("\n# ==== ESCRIBE TU CODIGO AQUI ====")


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
