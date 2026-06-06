"""
SOLUCIONES - Pruebas de Integracion
Ejecuta desde raiz: python scripts/runner.py 7 2 [ejercicio] -s
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    """Probar funcion que inserta y consulta SQLite"""
    import sqlite3
    conn = sqlite3.connect(':memory:')
    conn.execute('CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nombre TEXT, email TEXT)')
    conn.execute("INSERT INTO usuarios (nombre, email) VALUES (?, ?)", ('Ana', 'ana@test.com'))
    conn.commit()
    cursor = conn.execute("SELECT * FROM usuarios WHERE nombre = ?", ('Ana',))
    usuario = cursor.fetchone()
    assert usuario is not None
    assert usuario[1] == 'Ana'
    assert usuario[2] == 'ana@test.com'
    conn.close()
    print(">> SOLUCION 1: Probar funcion que inserta y consulta SQLite")
    print("-" * 40)
    print("Prueba de integracion con SQLite superada.")

def solucion_2():
    """Setup/teardown de base de datos en memoria"""
    print(">> SOLUCION 2: Setup/teardown de base de datos en memoria")
    print("-" * 40)
    print("import pytest")
    print("import sqlite3")
    print()
    print("@pytest.fixture")
    print("def db():")
    print("    conn = sqlite3.connect(':memory:')")
    print("    conn.execute('CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nombre TEXT, email TEXT)')")
    print("    yield conn")
    print("    conn.close()")
    print()
    print("def test_insertar_usuario(db):")
    print("    db.execute(\"INSERT INTO usuarios (nombre, email) VALUES ('Luis', 'luis@test.com')\")")
    print("    cursor = db.execute(\"SELECT * FROM usuarios WHERE nombre = 'Luis'\")")
    print("    assert cursor.fetchone() is not None")

def solucion_3():
    """Probar integracion entre 2 modulos"""
    import sqlite3
    def procesar_datos(datos):
        return [d.upper() for d in datos]
    def guardar_datos(conn, datos):
        for d in datos:
            conn.execute("INSERT INTO items (valor) VALUES (?)", (d,))
        conn.commit()
    conn = sqlite3.connect(':memory:')
    conn.execute("CREATE TABLE items (id INTEGER PRIMARY KEY, valor TEXT)")
    datos = procesar_datos(['hola', 'mundo'])
    guardar_datos(conn, datos)
    cursor = conn.execute("SELECT valor FROM items ORDER BY id")
    resultados = [row[0] for row in cursor.fetchall()]
    assert resultados == ['HOLA', 'MUNDO']
    conn.close()
    print(">> SOLUCION 3: Probar integracion entre 2 modulos")
    print("-" * 40)
    print("Integracion entre modulos verificada: datos procesados y guardados correctamente.")

if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
    else:
        for i, sol in enumerate(soluciones, 1):
            print(f"  {i}. {sol.__doc__}")
