"""
EJERCICIOS - Transacciones ACID
Ejecuta desde raiz: python scripts/runner.py 4 5 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Realiza una transferencia bancaria usando BEGIN, INSERT y COMMIT"""
    import sqlite3
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE cuentas (
            id INTEGER PRIMARY KEY,
            titular TEXT NOT NULL,
            saldo REAL NOT NULL
        );
        INSERT INTO cuentas VALUES (1, 'Ana', 1000.00);
        INSERT INTO cuentas VALUES (2, 'Juan', 500.00);
    """)
    conn.commit()
    print("=== Cuentas antes de la transferencia ===")
    for row in c.execute("SELECT * FROM cuentas"):
        print(f"  {row[0]}. {row[1]:<6} ${row[2]:>7.2f}")
    print()
    print("Transfiere $200 de la cuenta 1 (Ana) a la cuenta 2 (Juan)")
    print("Usa BEGIN, UPDATE, UPDATE, COMMIT")
    # ==== ESCRIBE TU CONSULTA SQL AQUI ====
    # c.execute("BEGIN")
    # c.execute("UPDATE cuentas SET saldo = saldo - 200 WHERE id = 1")
    # c.execute("UPDATE cuentas SET saldo = saldo + 200 WHERE id = 2")
    # conn.commit()
    # for row in c.execute("SELECT * FROM cuentas"):
    #     print(row)
    pass

def ejercicio_2():
    """Usa ROLLBACK para revertir cambios ante un error"""
    import sqlite3
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE cuentas (
            id INTEGER PRIMARY KEY,
            titular TEXT NOT NULL,
            saldo REAL NOT NULL
        );
        INSERT INTO cuentas VALUES (1, 'Ana', 1000.00);
        INSERT INTO cuentas VALUES (2, 'Juan', 500.00);
    """)
    conn.commit()
    print("=== Cuentas antes ===")
    for row in c.execute("SELECT * FROM cuentas"):
        print(f"  {row}")
    print()
    print("Intenta transferir $1200 (saldo insuficiente) y haz ROLLBACK")
    # ==== ESCRIBE TU CONSULTA SQL AQUI ====
    # c.execute("BEGIN")
    # saldo = c.execute("SELECT saldo FROM cuentas WHERE id=1").fetchone()[0]
    # if saldo >= 1200:
    #     c.execute("UPDATE cuentas SET saldo = saldo - 1200 WHERE id=1")
    #     c.execute("UPDATE cuentas SET saldo = saldo + 1200 WHERE id=2")
    #     conn.commit()
    #     print("Transferencia exitosa")
    # else:
    #     conn.rollback()
    #     print("Fondos insuficientes, transaccion revertida")
    # for row in c.execute("SELECT * FROM cuentas"):
    #     print(row)
    pass

def ejercicio_3():
    """Simula un fallo y muestra que ROLLBACK mantiene la consistencia"""
    import sqlite3
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE cuentas (
            id INTEGER PRIMARY KEY,
            titular TEXT NOT NULL,
            saldo REAL NOT NULL
        );
        INSERT INTO cuentas VALUES (1, 'Ana', 1000.00);
        INSERT INTO cuentas VALUES (2, 'Juan', 500.00);
    """)
    conn.commit()

    def saldo_total():
        return c.execute("SELECT SUM(saldo) FROM cuentas").fetchone()[0]

    print(f"Saldo total inicial: ${saldo_total():.2f}")
    print()
    print("Simula una transferencia que falla a mitad del proceso:")
    print("1. BEGIN")
    print("2. Restar $300 de Ana")
    print("3. (Simular fallo antes de sumar a Juan)")
    print("4. ROLLBACK")
    print("5. Verificar que el saldo total volvio al valor original")
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass

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
