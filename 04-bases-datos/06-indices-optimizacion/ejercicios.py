import sys, sqlite3

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def get_db():
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    return conn

def ejercicio_1():
    print("=" * 50)
    print("EJERCICIO 1: CREATE INDEX y EXPLAIN")
    print("=" * 50)
    conn = get_db()
    conn.executescript("""
        CREATE TABLE ventas (
            id INTEGER PRIMARY KEY,
            producto TEXT,
            cantidad INTEGER,
            total REAL
        );
        INSERT INTO ventas VALUES (1, 'Laptop', 2, 2400.00);
        INSERT INTO ventas VALUES (2, 'Mouse', 10, 250.00);
        INSERT INTO ventas VALUES (3, 'Monitor', 3, 900.00);
        INSERT INTO ventas VALUES (4, 'Laptop', 1, 1200.00);
        INSERT INTO ventas VALUES (5, 'Teclado', 5, 225.00);
    """)
    print("Tabla 'ventas' con 5 registros.")
    print()
    print('TAREA: Ejecuta EXPLAIN QUERY PLAN para la consulta:')
    print("SELECT * FROM ventas WHERE producto = 'Laptop';")
    print()
    print("Luego crea un indice en la columna 'producto' y")
    print("vuelve a ejecutar EXPLAIN QUERY PLAN.")
    print()
    print("PISTA: CREATE INDEX idx_producto ON ventas(producto);")

def ejercicio_2():
    print("=" * 50)
    print("EJERCICIO 2: Indices compuestos")
    print("=" * 50)
    conn = get_db()
    conn.executescript("""
        CREATE TABLE pedidos (
            id INTEGER PRIMARY KEY,
            cliente_id INTEGER,
            fecha TEXT,
            total REAL
        );
        INSERT INTO pedidos VALUES
            (1, 1, '2024-01-15', 150.00),
            (2, 1, '2024-02-10', 75.00),
            (3, 2, '2024-01-20', 200.00),
            (4, 3, '2024-03-05', 50.00);
    """)
    print("Tabla 'pedidos' con 4 registros.")
    print()
    print("TAREA: Crea un indice compuesto optimizado para consultas")
    print("que filtran por cliente_id y luego ordenan por fecha.")
    print()
    print("PISTA: CREATE INDEX idx_cliente_fecha ON pedidos(cliente_id, fecha);")

def ejercicio_3():
    print("=" * 50)
    print("EJERCICIO 3: Cuando (no) indexar")
    print("=" * 50)
    print("Para cada escenario, decide si conviene o no crear un indice:")
    print()
    print("1. Tabla 'usuarios' con 1,000,000 de filas.")
    print("   Columna 'email' consultada frecuentemente en WHERE.")
    print()
    print("2. Tabla 'configuracion' con 10 filas.")
    print("   Columna 'clave' consultada con WHERE.")
    print()
    print("3. Columna 'activo' (valores: 0 o 1) en tabla grande.")
    print()
    print("4. Columna 'fecha_creacion' donde se ordena frecuentemente.")
    print()
    print("PISTA: Responde mentalmente SI o NO a cada caso,")
    print("luego revisa soluciones.py.")

pistas = {
    "1": "CREATE INDEX idx_producto ON ventas(producto);",
    "2": "CREATE INDEX idx_cliente_fecha ON pedidos(cliente_id, fecha);",
    "3": "1: SI  (tabla grande, columna buscada)\n2: NO  (tabla muy pequena, indice innecesario)\n3: NO  (pocos valores distintos, 0 y 1)\n4: SI  (ORDER BY frecuente)"
}

def menu():
    print("=" * 50)
    print("INDICES Y OPTIMIZACION - EJERCICIOS")
    print("=" * 50)
    print("1 - CREATE INDEX y EXPLAIN")
    print("2 - Indices compuestos")
    print("3 - Cuando (no) indexar")
    print()
    print("Usa: python ejercicios.py <numero>")
    print("     python ejercicios.py <numero> -p  (pista)")

def main():
    args = sys.argv[1:]
    if not args:
        menu()
        return
    num = args[0]
    mostrar_pista = "-p" in args
    if mostrar_pista and num in pistas:
        print("=== PISTA ===")
        print(pistas[num])
        print()
    if num == "1":
        ejercicio_1()
    elif num == "2":
        ejercicio_2()
    elif num == "3":
        ejercicio_3()
    else:
        print("Ejercicio no valido. Usa 1, 2 o 3.")

if __name__ == "__main__":
    main()
