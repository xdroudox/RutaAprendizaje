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
    print("EJERCICIO 1: BEGIN, COMMIT, ROLLBACK basico")
    print("=" * 50)
    conn = get_db()
    conn.executescript("""
        CREATE TABLE cuentas (
            id INTEGER PRIMARY KEY,
            titular TEXT,
            saldo REAL
        );
        INSERT INTO cuentas VALUES (1, 'Ana', 1000.00), (2, 'Luis', 500.00);
    """)
    print("Cuentas:")
    cur = conn.execute("SELECT * FROM cuentas;")
    for f in cur.fetchall():
        print(f"  {f['id']}: {f['titular']} - ${f['saldo']:.2f}")
    print()
    print("TAREA: Escribe el codigo SQL para transferir $200 de")
    print("Ana a Luis usando una transaccion (BEGIN, UPDATE, UPDATE, COMMIT).")
    print()
    print("PISTA: BEGIN; UPDATE cuentas SET saldo = saldo - 200 WHERE id = 1;")
    print("  UPDATE cuentas SET saldo = saldo + 200 WHERE id = 2; COMMIT;")

def ejercicio_2():
    print("=" * 50)
    print("EJERCICIO 2: ROLLBACK por saldo insuficiente")
    print("=" * 50)
    conn = get_db()
    conn.executescript("""
        CREATE TABLE cuentas (
            id INTEGER PRIMARY KEY,
            titular TEXT,
            saldo REAL
        );
        INSERT INTO cuentas VALUES (1, 'Ana', 100.00), (2, 'Luis', 500.00);
    """)
    print("Cuentas:")
    cur = conn.execute("SELECT * FROM cuentas;")
    for f in cur.fetchall():
        print(f"  {f['id']}: {f['titular']} - ${f['saldo']:.2f}")
    print()
    print("TAREA: Intenta transferir $300 de Ana (que solo tiene $100)")
    print("a Luis. Usa BEGIN, intenta el UPDATE, verifica saldo, y")
    print("haz ROLLBACK si el saldo es insuficiente.")
    print()
    print("PISTA: BEGIN; UPDATE ... WHERE id=1 (saldo queda -200);")
    print("  Eso es incorrecto. Hay que VERIFICAR antes de transferir.")

def ejercicio_3():
    print("=" * 50)
    print("EJERCICIO 3: Propiedades ACID")
    print("=" * 50)
    print("Identifica que propiedad ACID se violaria en cada caso:")
    print()
    print("Caso A: Una transferencia debita $200 de la cuenta A")
    print("pero el sistema falla antes de acreditar a la cuenta B.")
    print()
    print("Caso B: Dos usuarios ven simultaneamente saldo = $1000.")
    print("Ambos transfieren $900 y el banco permite ambos.")
    print()
    print("Caso C: El sistema confirma una venta pero tras un reinicio")
    print("los datos se pierden.")
    print()
    print("PISTA: Atomicity, Isolation, Durability")
    print()
    print("TAREA: Escribe el nombre de la propiedad para cada caso")
    print("(responde mentalmente y luego revisa soluciones.py)")

pistas = {
    "1": "BEGIN;\nUPDATE cuentas SET saldo = saldo - 200 WHERE id = 1;\nUPDATE cuentas SET saldo = saldo + 200 WHERE id = 2;\nCOMMIT;",
    "2": "BEGIN;\nSELECT saldo FROM cuentas WHERE id = 1;  (si saldo < 300 -> ROLLBACK)\nSi saldo >= 300: UPDATE ... SET saldo = saldo - 300 WHERE id = 1;\nUPDATE ... SET saldo = saldo + 300 WHERE id = 2;\nCOMMIT;",
    "3": "Caso A: Atomicity (se viola atomicidad)\nCaso B: Isolation (se viola aislamiento)\nCaso C: Durability (se viola durabilidad)"
}

def menu():
    print("=" * 50)
    print("TRANSACCIONES ACID - EJERCICIOS")
    print("=" * 50)
    print("1 - BEGIN, COMMIT, ROLLBACK basico")
    print("2 - ROLLBACK por saldo insuficiente")
    print("3 - Propiedades ACID")
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
