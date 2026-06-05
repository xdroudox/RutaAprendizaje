"""
EJERCICIOS - Indices y Optimizacion
Ejecuta desde raiz: python scripts/runner.py 4 6 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Crea un indice y analiza su efecto con EXPLAIN QUERY PLAN"""
    import sqlite3
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
    # Insertar datos de prueba
    categorias = ['Electronica', 'Hogar', 'Deportes', 'Jugueteria']
    for i in range(1, 1001):
        cat = categorias[i % len(categorias)]
        c.execute("INSERT INTO productos VALUES (?, ?, ?, ?)",
                  (i, f'Producto{i}', cat, round(i * 1.5, 2)))
    conn.commit()
    print("=== EXPLAIN sin indice ===")
    for row in c.execute("EXPLAIN QUERY PLAN SELECT * FROM productos WHERE categoria = 'Electronica'"):
        print(f"  {row}")
    print()
    # ==== ESCRIBE TU CONSULTA SQL AQUI ====
    # c.execute("CREATE INDEX idx_categoria ON productos(categoria)")
    # print("=== EXPLAIN CON indice ===")
    # for row in c.execute("EXPLAIN QUERY PLAN SELECT * FROM productos WHERE categoria = 'Electronica'"):
    #     print(f"  {row}")
    pass

def ejercicio_2():
    """Compara velocidad de una misma consulta CON y SIN indice usando time"""
    import time
    import sqlite3
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE usuarios (
            id INTEGER PRIMARY KEY,
            email TEXT NOT NULL,
            nombre TEXT NOT NULL
        );
    """)
    # Insertar 10000 registros
    for i in range(1, 10001):
        c.execute("INSERT INTO usuarios VALUES (?, ?, ?)",
                  (i, f'usuario{i}@email.com', f'Nombre{i}'))
    conn.commit()
    # ==== ESCRIBE TU CONSULTA SQL AQUI ====
    # def medir(query):
    #     inicio = time.time()
    #     c.execute(query)
    #     c.fetchall()
    #     return time.time() - inicio

    # print("Sin indice:")
    # t1 = medir("SELECT * FROM usuarios WHERE email = 'usuario9999@email.com'")
    # print(f"  {t1:.4f} seg")
    # c.execute("CREATE INDEX idx_email ON usuarios(email)")
    # print("Con indice:")
    # t2 = medir("SELECT * FROM usuarios WHERE email = 'usuario9999@email.com'")
    # print(f"  {t2:.4f} seg")
    # print(f"Mejora: {t1/t2:.1f}x mas rapido")
    pass

def ejercicio_3():
    """Identifica queries lentas y propone indices para optimizarlas"""
    import sqlite3
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
    print("=== Queries sin optimizar ===")
    print()
    print("Query 1: Buscar por estado")
    for row in c.execute("EXPLAIN QUERY PLAN SELECT * FROM pedidos WHERE estado = 'pendiente'"):
        print(f"  {row}")
    print()
    print("Query 2: Buscar por cliente_id")
    for row in c.execute("EXPLAIN QUERY PLAN SELECT * FROM pedidos WHERE cliente_id = 50"):
        print(f"  {row}")
    print()
    print("Query 3: Buscar por rango de fechas")
    for row in c.execute("EXPLAIN QUERY PLAN SELECT * FROM pedidos WHERE fecha BETWEEN '2024-01-01' AND '2024-03-01'"):
        print(f"  {row}")
    print()
    print("Propuesta de indices (escribe tu respuesta en comentarios):")
    # ==== ESCRIBE TU RESPUESTA AQUI ====
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
