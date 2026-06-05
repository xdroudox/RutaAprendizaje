"""
SOLUCIONES - Transacciones ACID
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
    print(">>> Transferencia exitosa de $200 (Ana -> Juan):")
    c.execute("BEGIN")
    c.execute("UPDATE cuentas SET saldo = saldo - 200 WHERE id = 1")
    c.execute("UPDATE cuentas SET saldo = saldo + 200 WHERE id = 2")
    conn.commit()
    for row in c.execute("SELECT * FROM cuentas"):
        print(f"  {row[0]}. {row[1]:<6} ${row[2]:>7.2f}")

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
    print(">>> Intento de transferencia de $1200 (fondo insuficiente):")
    c.execute("BEGIN")
    saldo = c.execute("SELECT saldo FROM cuentas WHERE id=1").fetchone()[0]
    if saldo >= 1200:
        c.execute("UPDATE cuentas SET saldo = saldo - 1200 WHERE id=1")
        c.execute("UPDATE cuentas SET saldo = saldo + 1200 WHERE id=2")
        conn.commit()
        print("  Transferencia exitosa")
    else:
        conn.rollback()
        print("  Fondos insuficientes, transaccion REVERTIDA (ROLLBACK)")
    print("  Estado final:")
    for row in c.execute("SELECT * FROM cuentas"):
        print(f"    {row[0]}. {row[1]:<6} ${row[2]:>7.2f}")

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

    print(f"  Saldo total inicial: ${saldo_total():.2f}")
    c.execute("BEGIN")
    c.execute("UPDATE cuentas SET saldo = saldo - 300 WHERE id = 1")
    # Simulamos un fallo: no completamos la transferencia
    print("  Fallo simulado a mitad de la transferencia...")
    conn.rollback()
    print(f"  Saldo total despues de ROLLBACK: ${saldo_total():.2f}")
    print("  (La consistencia se mantuvo gracias a ROLLBACK)")
    for row in c.execute("SELECT * FROM cuentas"):
        print(f"    {row[0]}. {row[1]:<6} ${row[2]:>7.2f}")

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
