"""
EJERCICIOS - Pruebas de Integracion
Ejecuta desde raiz: python scripts/runner.py 7 2 [ejercicio] [-p N]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1(pista=0):
    """Probar funcion que inserta y consulta SQLite"""
    print(">> EJERCICIO 1: Probar funcion que inserta y consulta SQLite")
    print("-" * 40)
    print("Usando sqlite3 en memoria, escribe una prueba que:")
    print("1. Cree una conexion a ':memory:'")
    print("2. Cree una tabla 'usuarios' (id, nombre, email)")
    print("3. Inserte un usuario")
    print("4. Consulte el usuario y verifique los datos con assert")
    print()
    print("import sqlite3")
    print()
    print("conn = sqlite3.connect(':memory:')")
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")
    print("conn.close()")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  - conn.execute() ejecuta sentencias SQL")
        print("  - conn.commit() confirma los cambios")
        print("  - conn.execute('SELECT ...').fetchone() obtiene una fila")
        print("  - Usa ? como placeholder para parametros (SQL injection safe)")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  conn.execute('CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nombre TEXT, email TEXT)')")
        print('  conn.execute("INSERT INTO usuarios (nombre, email) VALUES (?, ?)", ("Ana", "ana@test.com"))')
        print("  conn.commit()")
        print("  cursor = conn.execute(\"SELECT * FROM usuarios WHERE nombre = ?\", (\"Ana\",))")
        print("  usuario = cursor.fetchone()")
        print("  assert usuario is not None")
        print("  assert usuario[1] == 'Ana'")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  import sqlite3")
        print("  conn = sqlite3.connect(':memory:')")
        print("  conn.execute('CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nombre TEXT, email TEXT)')")
        print('  conn.execute("INSERT INTO usuarios (nombre, email) VALUES (?, ?)", ("Ana", "ana@test.com"))')
        print("  conn.commit()")
        print("  cursor = conn.execute(\"SELECT * FROM usuarios WHERE nombre = ?\", (\"Ana\",))")
        print("  usuario = cursor.fetchone()")
        print("  assert usuario is not None")
        print("  assert usuario[1] == 'Ana'")
        print("  assert usuario[2] == 'ana@test.com'")
        print("  conn.close()")

def ejercicio_2(pista=0):
    """Setup/teardown de base de datos en memoria"""
    print(">> EJERCICIO 2: Setup/teardown de base de datos en memoria")
    print("-" * 40)
    print("Crea un fixture de pytest que configure y limpie")
    print("una base de datos SQLite en memoria para cada prueba.")
    print()
    print("import pytest")
    print("import sqlite3")
    print()
    print("@pytest.fixture")
    print("def db():")
    print("    # Setup")
    print("    conn = sqlite3.connect(':memory:')")
    print("    # ==== ESCRIBE TU RESPUESTA AQUI ====")
    print("    yield conn")
    print("    # Teardown")
    print("    conn.close()")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  En el setup (antes del yield): crea la tabla que usaran las pruebas.")
        print("  En el teardown (despues del yield): cierra la conexion (conn.close()).")
        print("  Las funciones test_* reciben el fixture como parametro 'db'.")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  @pytest.fixture")
        print("  def db():")
        print("      conn = sqlite3.connect(':memory:')")
        print("      conn.execute('CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nombre TEXT, email TEXT)')")
        print("      yield conn")
        print("      conn.close()")
        print()
        print("  def test_insertar_usuario(db):")
        print("      db.execute(\"INSERT INTO usuarios (nombre, email) VALUES ('Luis', 'luis@test.com')\")")
        print("      cursor = db.execute(\"SELECT * FROM usuarios WHERE nombre = 'Luis'\")")
        print("      assert cursor.fetchone() is not None")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  import pytest")
        print("  import sqlite3")
        print()
        print("  @pytest.fixture")
        print("  def db():")
        print("      conn = sqlite3.connect(':memory:')")
        print("      conn.execute('CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nombre TEXT, email TEXT)')")
        print("      yield conn")
        print("      conn.close()")
        print()
        print("  def test_insertar_usuario(db):")
        print("      db.execute(\"INSERT INTO usuarios (nombre, email) VALUES ('Luis', 'luis@test.com')\")")
        print("      cursor = db.execute(\"SELECT * FROM usuarios WHERE nombre = 'Luis'\")")
        print("      assert cursor.fetchone() is not None")
        print("  # Ejecutar: pytest test_archivo.py -v")

def ejercicio_3(pista=0):
    """Probar integracion entre 2 modulos"""
    print(">> EJERCICIO 3: Probar integracion entre 2 modulos")
    print("-" * 40)
    print("Dado un modulo que procesa datos y otro que los guarda,")
    print("escribe una prueba de integracion que verifique el flujo")
    print("completo: procesar -> guardar -> recuperar.")
    print()
    print("def procesar_datos(datos):")
    print("    return [d.upper() for d in datos]")
    print()
    print("def guardar_datos(conn, datos):")
    print("    for d in datos:")
    print("        conn.execute('INSERT INTO items (valor) VALUES (?)', (d,))")
    print("    conn.commit()")
    print()
    print("# ==== ESCRIBE TU PRUEBA DE INTEGRACION AQUI ====")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  La prueba debe: conectar a :memory:, crear la tabla items,")
        print("  llamar a procesar_datos(), llamar a guardar_datos(),")
        print("  consultar los datos guardados y verificar con assert.")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  import sqlite3")
        print("  conn = sqlite3.connect(':memory:')")
        print("  conn.execute('CREATE TABLE items (id INTEGER PRIMARY KEY, valor TEXT)')")
        print("  datos = procesar_datos(['hola', 'mundo'])")
        print("  guardar_datos(conn, datos)")
        print("  cursor = conn.execute('SELECT valor FROM items ORDER BY id')")
        print("  resultados = [row[0] for row in cursor.fetchall()]")
        print("  assert resultados == ['HOLA', 'MUNDO']")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  import sqlite3")
        print("  conn = sqlite3.connect(':memory:')")
        print("  conn.execute('CREATE TABLE items (id INTEGER PRIMARY KEY, valor TEXT)')")
        print("  datos = procesar_datos(['hola', 'mundo'])")
        print("  guardar_datos(conn, datos)")
        print("  cursor = conn.execute('SELECT valor FROM items ORDER BY id')")
        print("  resultados = [row[0] for row in cursor.fetchall()]")
        print("  assert resultados == ['HOLA', 'MUNDO']")
        print("  conn.close()")
        print("  print('Integracion entre modulos verificada')")

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    pista_level = 0
    if "-p" in sys.argv:
        idx = sys.argv.index("-p")
        if idx + 1 < len(sys.argv) and sys.argv[idx + 1].isdigit():
            pista_level = int(sys.argv[idx + 1])
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            ejercicios[num](pista=pista_level)
    else:
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
