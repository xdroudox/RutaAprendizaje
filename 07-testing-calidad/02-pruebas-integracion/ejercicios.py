"""
EJERCICIOS - Pruebas de Integracion
Ejecuta: python ejercicios.py [numero]

Uso:
  python ejercicios.py      -> Menu
  python ejercicios.py 1    -> Ejercicio 1
  python ejercicios.py -s 1 -> Solucion del ejercicio 1
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


def ejercicio_1():
    print("=" * 50)
    print(">> EJERCICIO 1: Prueba de integracion con SQLite")
    print("=" * 50)
    print()
    print("Completa la funcion test_insertar_y_consultar() que:")
    print("  1. Cree una conexion a SQLite en memoria (:memory:)")
    print("  2. Cree la tabla usuarios")
    print("  3. Inserte un usuario con nombre='Ana' y email='ana@test.com'")
    print("  4. Consulte el usuario por nombre")
    print("  5. Verifique que el nombre y email coincidan")
    print()
    print("PISTA: sqlite3.connect(':memory:') y cursor.fetchone()")
    print()
    print("Edita el archivo:")
    print("def test_insertar_y_consultar():")
    print("    conn = sqlite3.connect(':memory:')")
    print("    # --- TU CODIGO AQUI ---")
    print("    conn.close()")


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
    print("Esta prueba verifica que la insercion y consulta")
    print("funcionan correctamente juntas (integracion).")


def ejercicio_2():
    print("=" * 50)
    print(">> EJERCICIO 2: Setup y Teardown con fixtures")
    print("=" * 50)
    print()
    print("Crea un fixture de pytest que:")
    print("  1. Crear conexion a :memory:")
    print("  2. Crear la tabla usuarios (setup)")
    print("  3. Proporcionar la conexion a la prueba (yield)")
    print("  4. Cerrar la conexion despues de la prueba (teardown)")
    print()
    print("Luego escribe 2 pruebas que usen el fixture:")
    print("  - test_insertar_usuario: inserta y verifica")
    print("  - test_insertar_multiples: inserta 2 usuarios y verifica")
    print()
    print("PISTA: Usa @pytest.fixture con yield para separar setup/teardown")
    print()
    print("Edita el archivo:")
    print("@pytest.fixture")
    print("def db():")
    print("    # Setup")
    print("    conn = sqlite3.connect(':memory:')")
    print("    # --- TU CODIGO AQUI ---")
    print("    # Teardown")
    print("    conn.close()")


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
    print("    conn = sqlite3.connect(':memory:')")
    print("    crear_tabla_usuarios(conn)")
    print("    yield conn")
    print("    conn.close()")
    print()
    print("def test_insertar_usuario(db):")
    print("    insertar_usuario(db, 'Luis', 'luis@test.com')")
    print("    usuario = obtener_usuario(db, 'Luis')")
    print("    assert usuario is not None")
    print("    assert usuario[1] == 'Luis'")
    print()
    print("def test_insertar_multiples(db):")
    print("    insertar_usuario(db, 'A', 'a@test.com')")
    print("    insertar_usuario(db, 'B', 'b@test.com')")
    print("    cursor = db.execute('SELECT COUNT(*) FROM usuarios')")
    print("    assert cursor.fetchone()[0] == 2")
    print("```")
    print()
    print("El yield separa el setup (antes) del teardown (despues).")
    print("Cada prueba obtiene una base de datos fresca.")


def ejercicio_3():
    print("=" * 50)
    print(">> EJERCICIO 3: Integracion entre modulos")
    print("=" * 50)
    print()
    print("Dado el siguiente modulo de procesamiento de usuarios:")
    print()
    print("  def procesar_usuario(conn, nombre, email):")
    print("      if not nombre or not email:")
    print("          raise ValueError('Nombre y email requeridos')")
    print("      if '@' not in email:")
    print("          raise ValueError('Email invalido')")
    print("      insertar_usuario(conn, nombre, email)")
    print("      return obtener_usuario(conn, nombre)")
    print()
    print("Escribe pruebas de integracion que:")
    print("  1. Prueben el flujo completo (insercion exitosa)")
    print("  2. Prueben validacion de email invalido")
    print("  3. Prueben con nombre vacio")
    print()
    print("PISTA: Usa pytest.raises para las validaciones")
    print()
    print("Edita el archivo:")
    print("def test_procesar_usuario_exitoso(db):")
    print("    # --- TU CODIGO AQUI ---")
    print()
    print("def test_procesar_usuario_email_invalido(db):")
    print("    # --- TU CODIGO AQUI ---")


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
    print("    assert usuario is not None")
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
    print("Estas pruebas verifican la integracion entre la funcion")
    print("procesar_usuario y las funciones de base de datos.")


pistas = {
    "1": "conn = sqlite3.connect(':memory:')\ncrear_tabla_usuarios(conn)\ninsertar_usuario(conn, 'Ana', 'ana@test.com')\nusuario = obtener_usuario(conn, 'Ana')\nassert usuario is not None\nassert usuario[1] == 'Ana'",
    "2": "@pytest.fixture\ndef db():\n    conn = sqlite3.connect(':memory:')\n    crear_tabla_usuarios(conn)\n    yield conn\n    conn.close()",
    "3": "Usa pytest.raises(ValueError) y verifica el mensaje con match"
}


def menu():
    while True:
        print()
        print("=" * 50)
        print("PRUEBAS DE INTEGRACION - EJERCICIOS")
        print("=" * 50)
        print("1. Prueba de integracion con SQLite")
        print("2. Setup y Teardown con fixtures")
        print("3. Integracion entre modulos")
        print("0. Salir")
        print()

        opcion = input("Selecciona un ejercicio: ")

        if opcion == "1":
            ejercicio_1()
            input("Presiona ENTER para continuar...")
        elif opcion == "2":
            ejercicio_2()
            input("Presiona ENTER para continuar...")
        elif opcion == "3":
            ejercicio_3()
            input("Presiona ENTER para continuar...")
        elif opcion == "0":
            print("Sigue practicando!")
            break
        else:
            print("Opcion invalida")


def main():
    args = sys.argv[1:]

    if not args:
        menu()
        return

    if "-s" in args:
        idx = args.index("-s")
        if idx + 1 < len(args) and args[idx + 1].isdigit():
            num = int(args[idx + 1])
            [solucion_1, solucion_2, solucion_3][num - 1]()
        return

    if args[0].isdigit():
        num = int(args[0])
        [ejercicio_1, ejercicio_2, ejercicio_3][num - 1]()


if __name__ == "__main__":
    main()
