import sys, sqlite3

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def get_db():
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    return conn

def mostrar_resultados(conn, query):
    try:
        cur = conn.execute(query)
        filas = cur.fetchall()
        if not filas:
            print("(Sin resultados)")
            return
        headers = [d[0] for d in cur.description]
        print(" | ".join(h for h in headers))
        print("-" * 40)
        for f in filas:
            print(" | ".join(str(f[h]) for h in headers))
    except Exception as e:
        print("ERROR:", e)

def solucion_1():
    print("=" * 50)
    print("SOLUCION 1: Transferencia con transaccion")
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
    print("Antes:")
    mostrar_resultados(conn, "SELECT * FROM cuentas;")
    print()
    conn.execute("BEGIN;")
    conn.execute("UPDATE cuentas SET saldo = saldo - 200 WHERE id = 1;")
    conn.execute("UPDATE cuentas SET saldo = saldo + 200 WHERE id = 2;")
    conn.execute("COMMIT;")
    print("Despues de transferir $200 de Ana a Luis:")
    mostrar_resultados(conn, "SELECT * FROM cuentas;")

def solucion_2():
    print("=" * 50)
    print("SOLUCION 2: ROLLBACK por saldo insuficiente")
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
    print("Antes:")
    mostrar_resultados(conn, "SELECT * FROM cuentas;")
    print()
    print("Verificando saldo de Ana (id=1):")
    cur = conn.execute("SELECT saldo FROM cuentas WHERE id = 1;")
    saldo_ana = cur.fetchone()["saldo"]
    print(f"  Saldo disponible: ${saldo_ana:.2f}")
    monto = 300
    print(f"  Intento transferir: ${monto:.2f}")
    if saldo_ana >= monto:
        conn.execute("BEGIN;")
        conn.execute("UPDATE cuentas SET saldo = saldo - ? WHERE id = 1;", (monto,))
        conn.execute("UPDATE cuentas SET saldo = saldo + ? WHERE id = 2;", (monto,))
        conn.execute("COMMIT;")
        print("  Transferencia exitosa.")
    else:
        print(f"  Saldo insuficiente (${saldo_ana:.2f} < ${monto:.2f}).")
        print("  ROLLBACK ejecutado (no hay cambios que revertir en este caso).")
    print()
    print("Despues:")
    mostrar_resultados(conn, "SELECT * FROM cuentas;")

def solucion_3():
    print("=" * 50)
    print("SOLUCION 3: Propiedades ACID")
    print("=" * 50)
    print()
    print("Caso A: Una transferencia debita $200 de la cuenta A")
    print("pero el sistema falla antes de acreditar a la cuenta B.")
    print("  Propiedad violada: ATOMICITY (Atomicidad)")
    print("  La transaccion debe ejecutarse completa o no ejecutarse.")
    print()
    print("Caso B: Dos usuarios ven simultaneamente saldo = $1000.")
    print("Ambos transfieren $900 y el banco permite ambos.")
    print("  Propiedad violada: ISOLATION (Aislamiento)")
    print("  Las transacciones concurrentes no deben interferir.")
    print()
    print("Caso C: El sistema confirma una venta pero tras un reinicio")
    print("los datos se pierden.")
    print("  Propiedad violada: DURABILITY (Durabilidad)")
    print("  Una vez confirmados, los cambios deben persistir.")

def menu():
    print("SOLUCIONES - TRANSACCIONES ACID")
    print("1 - Transferencia con transaccion")
    print("2 - ROLLBACK por saldo insuficiente")
    print("3 - Propiedades ACID")

def main():
    args = sys.argv[1:]
    if not args:
        menu()
        return
    num = args[0]
    if num == "1":
        solucion_1()
    elif num == "2":
        solucion_2()
    elif num == "3":
        solucion_3()
    else:
        print("Solucion no valida. Usa 1, 2 o 3.")

if __name__ == "__main__":
    main()
