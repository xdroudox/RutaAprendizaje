"""
SOLUCIONES - Transacciones ACID
Ejecuta: python scripts/runner.py 4 5 [ejercicio] -s
"""

import sys
import sqlite3

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: Transferencia bancaria con BEGIN y COMMIT")
    print("=" * 50)

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

    print("--- CODIGO ---")
    print("c.execute('BEGIN')")
    print("c.execute('UPDATE cuentas SET saldo = saldo - 200 WHERE id = 1')")
    print("c.execute('UPDATE cuentas SET saldo = saldo + 200 WHERE id = 2')")
    print("conn.commit()")
    print()

    c.execute("BEGIN")
    c.execute("UPDATE cuentas SET saldo = saldo - 200 WHERE id = 1")
    c.execute("UPDATE cuentas SET saldo = saldo + 200 WHERE id = 2")
    conn.commit()

    print("--- RESULTADO ---")
    for row in c.execute("SELECT * FROM cuentas"):
        print(f"  {row[0]}. {row[1]:<6} ${row[2]:>7.2f}")

    print()
    print("--- EXPLICACION ---")
    print("""
BEGIN inicia una transaccion. Hasta que no hacemos COMMIT,
los cambios son VISIBLES SOLO para esta conexion.

Si ocurre un error entre BEGIN y COMMIT, la BD queda en un
estado intermedio INCONSISTENTE. Por eso se agrupan las
operaciones en una transaccion atomica.

Propiedades ACID aplicadas:
  A - Atomicidad: O se hacen TODOS los cambios o NINGUNO
  C - Consistencia: El saldo total no cambia ($1500)
  I - Aislamiento: Otras conexiones no ven cambios hasta COMMIT
  D - Durabilidad: Una vez COMMIT, los cambios persisten
""")


def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: ROLLBACK por fondos insuficientes")
    print("=" * 50)

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

    print("--- CODIGO ---")
    print("c.execute('BEGIN')")
    print("saldo = c.execute('SELECT saldo FROM cuentas WHERE id=1').fetchone()[0]")
    print("if saldo >= 1200:")
    print("    c.execute('UPDATE cuentas SET saldo = saldo - 1200 WHERE id=1')")
    print("    c.execute('UPDATE cuentas SET saldo = saldo + 1200 WHERE id=2')")
    print("    conn.commit()")
    print("    print('Transferencia exitosa')")
    print("else:")
    print("    conn.rollback()")
    print("    print('Fondos insuficientes, transaccion REVERTIDA')")
    print()

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

    print()
    print("--- RESULTADO ---")
    for row in c.execute("SELECT * FROM cuentas"):
        print(f"  {row[0]}. {row[1]:<6} ${row[2]:>7.2f}")

    print()
    print("--- EXPLICACION ---")
    print("""
ROLLBACK deshace TODOS los cambios desde el ultimo BEGIN.
Esto es clave para mantener la consistencia.

Sin ROLLBACK, si transferimos $1200 sin verificar saldo:
  - Ana quedaria con saldo negativo (-$200)
  - Esto violaria la consistencia de la BD

Patron tipico en transacciones:
  1. BEGIN
  2. Validar condiciones
  3. Si todo OK  → COMMIT
  4. Si algo mal → ROLLBACK
""")


def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: Mantener consistencia ante fallos con ROLLBACK")
    print("=" * 50)

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

    print("--- CODIGO ---")
    print("c.execute('BEGIN')")
    print("c.execute('UPDATE cuentas SET saldo = saldo - 300 WHERE id = 1')")
    print("print('Fallo simulado a mitad de la transferencia...')")
    print("conn.rollback()")
    print()

    c.execute("BEGIN")
    c.execute("UPDATE cuentas SET saldo = saldo - 300 WHERE id = 1")
    print("  Fallo simulado a mitad de la transferencia...")
    conn.rollback()
    print(f"  Saldo total despues de ROLLBACK: ${saldo_total():.2f}")
    print("  (La consistencia se mantuvo gracias a ROLLBACK)")

    print()
    print("--- RESULTADO ---")
    for row in c.execute("SELECT * FROM cuentas"):
        print(f"  {row[0]}. {row[1]:<6} ${row[2]:>7.2f}")

    print()
    print("--- EXPLICACION ---")
    print("""
Este ejemplo simula un fallo del sistema (crash, desconexion, etc.)
a mitad de una transferencia.

Sin ROLLBACK la BD quedaria en estado inconsistente:
  - Ana perderia $300 sin que Juan los reciba
  - $300 desaparecerian del sistema
  - Saldo total: $1500 → $1200 (INCONSISTENTE)

Con ROLLBACK:
  - Todos los cambios se deshacen
  - La BD vuelve al estado consistente anterior
  - Saldo total se mantiene: $1500

Esto es la A de ACID: ATOMICIDAD.
La transaccion se ejecuta COMPLETAMENTE o NO SE EJECUTA.
""")


if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
