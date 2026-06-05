"""
EJERCICIOS - Pruebas de Integracion
Ejecuta desde raiz: python scripts/runner.py 7 2 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Probar funcion que inserta y consulta SQLite"""
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

def ejercicio_2():
    """Setup/teardown de base de datos en memoria"""
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

def ejercicio_3():
    """Probar integracion entre 2 modulos"""
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
