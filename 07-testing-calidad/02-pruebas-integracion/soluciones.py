"""
SOLUCIONES - Pruebas de Integracion
Ejecuta desde raiz: python scripts/runner.py 7 2 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Solucion: insertar y consultar SQLite"""
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
    print("Prueba de integracion con SQLite superada.")

def ejercicio_2():
    """Solucion: fixture con setup/teardown"""
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

def ejercicio_3():
    """Solucion: integracion entre modulos"""
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
    print("Integracion entre modulos verificada: datos procesados y guardados correctamente.")

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
