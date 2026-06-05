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
    print("EJERCICIO 1: CREATE TABLE e INSERT")
    print("=" * 50)
    conn = get_db()
    conn.executescript("""
        CREATE TABLE productos (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            precio REAL,
            stock INTEGER
        );
        INSERT INTO productos VALUES (1, 'Laptop', 1200.00, 10);
        INSERT INTO PRODUCTOS VALUES (2, 'Mouse', 25.50, 50);
        INSERT INTO PRODUCTOS VALUES (3, 'Teclado', 45.00, 30);
    """)
    print("Tabla 'productos' creada con 3 registros.")
    print()
    print("TAREA: Escribe un INSERT para agregar un nuevo producto")
    print("con id=4, nombre='Monitor', precio=300.00, stock=15")
    print()
    print("PISTA: INSERT INTO productos VALUES (...)")

def ejercicio_2():
    print("=" * 50)
    print("EJERCICIO 2: SELECT con WHERE")
    print("=" * 50)
    conn = get_db()
    conn.executescript("""
        CREATE TABLE empleados (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            salario REAL,
            departamento TEXT
        );
        INSERT INTO empleados VALUES (1, 'Ana', 45000, 'Ventas');
        INSERT INTO empleados VALUES (2, 'Luis', 52000, 'TI');
        INSERT INTO empleados VALUES (3, 'Maria', 48000, 'Ventas');
        INSERT INTO empleados VALUES (4, 'Carlos', 55000, 'TI');
        INSERT INTO empleados VALUES (5, 'Sofia', 39000, 'RH');
    """)
    print("Tabla 'empleados' creada con 5 registros.")
    print()
    print("TAREA: Escribe un SELECT que muestre los empleados")
    print("del departamento 'Ventas' con salario mayor a 46000.")
    print()
    print("PISTA: WHERE departamento = ... AND salario > ...")

def ejercicio_3():
    print("=" * 50)
    print("EJERCICIO 3: ORDER BY y LIMIT")
    print("=" * 50)
    conn = get_db()
    conn.executescript("""
        CREATE TABLE estudiantes (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            nota REAL,
            ciudad TEXT
        );
        INSERT INTO estudiantes VALUES (1, 'Pedro', 8.5, 'Madrid');
        INSERT INTO estudiantes VALUES (2, 'Laura', 9.2, 'Barcelona');
        INSERT INTO estudiantes VALUES (3, 'Diego', 7.8, 'Madrid');
        INSERT INTO estudiantes VALUES (4, 'Elena', 9.5, 'Barcelona');
        INSERT INTO estudiantes VALUES (5, 'Jorge', 6.5, 'Valencia');
        INSERT INTO estudiantes VALUES (6, 'Clara', 8.0, 'Valencia');
    """)
    print("Tabla 'estudiantes' creada con 6 registros.")
    print()
    print("TAREA: Escribe un SELECT que muestre los 3 estudiantes")
    print("con mayor nota, ordenados de mayor a menor.")
    print()
    print("PISTA: ORDER BY nota DESC LIMIT 3")

pistas = {
    "1": "INSERT INTO productos VALUES (4, 'Monitor', 300.00, 15);",
    "2": "SELECT * FROM empleados WHERE departamento = 'Ventas' AND salario > 46000;",
    "3": "SELECT * FROM estudiantes ORDER BY nota DESC LIMIT 3;"
}

def menu():
    print("=" * 50)
    print("SQL FUNDAMENTOS - EJERCICIOS")
    print("=" * 50)
    print("1 - CREATE TABLE e INSERT")
    print("2 - SELECT con WHERE")
    print("3 - ORDER BY y LIMIT")
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
