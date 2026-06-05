"""
SOLUCIONES - Pruebas de Integracion
Ejecuta: python soluciones.py [numero]

Uso:
  python soluciones.py    -> Menu
  python soluciones.py 1  -> Solucion del ejercicio 1
"""

import sys, sqlite3

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def crear_tabla_usuarios(conn):
    conn.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nombre TEXT, email TEXT)")


def insertar_usuario(conn, nombre, email):
    conn.execute("INSERT INTO usuarios (nombre, email) VALUES (?, ?)", (nombre, email))
    conn.commit()


def obtener_usuario(conn, nombre):
    cursor = conn.execute("SELECT * FROM usuarios WHERE nombre = ?", (nombre,))
    return cursor.fetchone()


def solucion_1():
    print("=" * 50)
    print("SOLUCION 1: Prueba de integracion con SQLite")
    print("=" * 50)
    print()
    print("```python")
    print("def test_insertar_y_consultar():")
    print("    conn = sqlite3.connect(':memory:')")
    print("    crear_tabla_usuarios(conn)")
    print("    insertar_usuario(conn, 'Ana', 'ana@test.com')")
    print("    usuario = obtener_usuario(conn, 'Ana')")
    print("    assert usuario is not None")
    print("    assert usuario[1] == 'Ana'")
    print("    assert usuario[2] == 'ana@test.com'")
    print("    conn.close()")
    print("    print('Prueba de integracion pasada')")
    print("```")
    print()
    print("Ejecucion:")
    test_insertar_y_consultar()

    print()
    print("Esta prueba verifica el flujo completo:")
    print("  Crear tabla -> Insertar -> Consultar -> Verificar")


def test_insertar_y_consultar():
    conn = sqlite3.connect(":memory:")
    crear_tabla_usuarios(conn)
    insertar_usuario(conn, "Ana", "ana@test.com")
    usuario = obtener_usuario(conn, "Ana")
    assert usuario is not None
    assert usuario[1] == "Ana"
    assert usuario[2] == "ana@test.com"
    conn.close()
    print("  Prueba de integracion pasada")


def solucion_2():
    print("=" * 50)
    print("SOLUCION 2: Setup y Teardown con fixtures")
    print("=" * 50)
    print()
    print("```python")
    print("import pytest")
    print()
    print("@pytest.fixture")
    print("def db():")
    print("    # Setup")
    print("    conn = sqlite3.connect(':memory:')")
    print("    crear_tabla_usuarios(conn)")
    print("    yield conn  # La prueba recibe este valor")
    print("    # Teardown")
    print("    conn.close()")
    print()
    print("def test_insertar_usuario(db):")
    print("    insertar_usuario(db, 'Luis', 'luis@test.com')")
    print("    usuario = obtener_usuario(db, 'Luis')")
    print("    assert usuario[1] == 'Luis'")
    print("    assert usuario[2] == 'luis@test.com'")
    print()
    print("def test_insertar_multiples(db):")
    print("    insertar_usuario(db, 'A', 'a@test.com')")
    print("    insertar_usuario(db, 'B', 'b@test.com')")
    print("    cursor = db.execute('SELECT COUNT(*) FROM usuarios')")
    print("    count = cursor.fetchone()[0]")
    print("    assert count == 2")
    print("```")
    print()
    print("Ventajas del patron fixture con yield:")
    print("- Garantiza que el teardown se ejecute incluso si la prueba falla")
    print("- Cada prueba comienza con una base de datos limpia")
    print("- Las pruebas son independientes entre si")


def solucion_3():
    print("=" * 50)
    print("SOLUCION 3: Integracion entre modulos")
    print("=" * 50)
    print()
    print("```python")
    print("import pytest")
    print()
    print("def procesar_usuario(conn, nombre, email):")
    print("    if not nombre or not email:")
    print("        raise ValueError('Nombre y email requeridos')")
    print("    if '@' not in email:")
    print("        raise ValueError('Email invalido')")
    print("    insertar_usuario(conn, nombre, email)")
    print("    return obtener_usuario(conn, nombre)")
    print()
    print("def test_procesar_usuario_exitoso(db):")
    print("    usuario = procesar_usuario(db, 'Maria', 'maria@test.com')")
    print("    assert usuario[1] == 'Maria'")
    print("    assert usuario[2] == 'maria@test.com'")
    print()
    print("def test_procesar_usuario_email_invalido(db):")
    print("    with pytest.raises(ValueError, match='Email invalido'):")
    print("        procesar_usuario(db, 'Maria', 'correo-sin-arroba')")
    print()
    print("def test_procesar_usuario_nombre_vacio(db):")
    print("    with pytest.raises(ValueError, match='Nombre y email requeridos'):")
    print("        procesar_usuario(db, '', 'maria@test.com')")
    print("```")
    print()
    print("Pruebas de integracion vs unitarias:")
    print("- Unitarias: prueban una funcion aislada (ej: validar email)")
    print("- Integracion: prueban funciones trabajando juntas (ej: validar + insertar)")


def menu():
    while True:
        print()
        print("=" * 50)
        print("SOLUCIONES - Pruebas de Integracion")
        print("=" * 50)
        print("1. Prueba de integracion con SQLite")
        print("2. Setup y Teardown con fixtures")
        print("3. Integracion entre modulos")
        print("0. Salir")
        print()

        opcion = input("Ver solucion: ")

        soluciones = {"1": solucion_1, "2": solucion_2, "3": solucion_3}

        if opcion in soluciones:
            soluciones[opcion]()
            input("Presiona ENTER para continuar...")
        elif opcion == "0":
            print("Sigue asi!")
            break
        else:
            print("Opcion invalida")


def main():
    args = sys.argv[1:]
    if args and args[0].isdigit():
        [solucion_1, solucion_2, solucion_3][int(args[0]) - 1]()
    else:
        menu()


if __name__ == "__main__":
    main()
