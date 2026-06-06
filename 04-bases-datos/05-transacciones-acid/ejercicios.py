"""
EJERCICIOS - Transacciones ACID
Ejecuta desde raiz: python scripts/runner.py 4 5 [ejercicio]

Niveles:
  🟢 Ej 1: BEGIN + COMMIT (transferencia bancaria)
  🟡 Ej 2: ROLLBACK por fondos insuficientes
  🔴 Ej 3: Fallo simulado + verificar consistencia

Pistas: python scripts/runner.py 4 5 N -p [1|2|3]
"""

import sys
import sqlite3

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1(pista=0):
    """🟢 BEGIN + COMMIT (transferencia bancaria)"""
    print(">> 🟢 EJERCICIO 1: Transferencia bancaria con BEGIN y COMMIT")
    print("-" * 50)

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

    if pista == 1:
        print("\n💡 Pista 1: La secuencia basica de una transaccion:")
        print("  1. BEGIN   → inicia la transaccion")
        print("  2. UPDATE  → modifica datos")
        print("  3. UPDATE  → segunda modificacion")
        print("  4. COMMIT  → confirma los cambios")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  c.execute('BEGIN')")
        print("  c.execute('UPDATE cuentas SET saldo = saldo - 200 WHERE id = 1')")
        print("  c.execute('UPDATE cuentas SET saldo = saldo + 200 WHERE id = 2')")
        print("  conn.commit()")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Resultado esperado:")
        print("  Ana:  $1000 - $200  = $800")
        print("  Juan: $500  + $200  = $700")
        print("  Saldo total se mantiene: $1500 en ambos casos")
        return

    print("\nTransfiere $200 de Ana (id=1) a Juan (id=2):")
    print("  1. BEGIN")
    print("  2. UPDATE ... SET saldo = saldo - 200 WHERE id = 1")
    print("  3. UPDATE ... SET saldo = saldo + 200 WHERE id = 2")
    print("  4. COMMIT")
    print("  5. SELECT * FROM cuentas para verificar")
    print("\n# ==== ESCRIBE TU CODIGO AQUI ====")


def ejercicio_2(pista=0):
    """🟡 ROLLBACK por fondos insuficientes"""
    print(">> 🟡 EJERCICIO 2: ROLLBACK cuando no hay saldo suficiente")
    print("-" * 50)

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
        print(f"  {row[0]}. {row[1]:<6} ${row[2]:>7.2f}")

    if pista == 1:
        print("\n💡 Pista 1: Verifica el saldo ANTES de transferir:")
        print("  saldo = c.execute('SELECT saldo FROM cuentas WHERE id=1').fetchone()[0]")
        print("  if saldo >= 1200:")
        print("      # realizar transferencia + COMMIT")
        print("  else:")
        print("      # ROLLBACK + mensaje de error")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  BEGIN")
        print("  if saldo >= 1200:")
        print("      UPDATE cuentas SET saldo = saldo - 1200 WHERE id=1")
        print("      UPDATE cuentas SET saldo = saldo + 1200 WHERE id=2")
        print("      COMMIT")
        print("  else:")
        print("      ROLLBACK")
        print("      print('Fondos insuficientes')")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Resultado esperado:")
        print("  Ana tiene $1000, intenta transferir $1200")
        print("  → 'Fondos insuficientes, transaccion REVERTIDA'")
        print("  → Las cuentas quedan IGUAL que al inicio")
        return

    print("\nIntenta transferir $1200 de Ana a Juan (ella solo tiene $1000):")
    print("  Si hay saldo: UPDATE + UPDATE + COMMIT")
    print("  Si NO hay saldo: ROLLBACK + mensaje de error")
    print("\n# ==== ESCRIBE TU CODIGO AQUI ====")


def ejercicio_3(pista=0):
    """🔴 Fallo simulado + verificar consistencia"""
    print(">> 🔴 EJERCICIO 3: Mantener consistencia ante fallos con ROLLBACK")
    print("-" * 50)

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

    if pista == 1:
        print("\n💡 Pista 1: Simula un fallo a mitad de la transferencia:")
        print("  1. BEGIN")
        print("  2. Resta $300 de Ana (pero NO sumes a Juan)")
        print("  3. ROLLBACK (simula que el programa fallo)")
        print("  4. Verifica que todo volvio al estado original")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  c.execute('BEGIN')")
        print("  c.execute('UPDATE cuentas SET saldo = saldo - 300 WHERE id = 1')")
        print("  print('Fallo simulado...')")
        print("  conn.rollback()")
        print("  print(f'Saldo total tras ROLLBACK: ${saldo_total()}'")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Resultado esperado:")
        print("  Saldo total inicial: $1500.00")
        print("  Fallo simulado a mitad de la transferencia...")
        print("  Saldo total despues de ROLLBACK: $1500.00")
        print("  Las cuentas vuelven a su estado original")
        print("  Sin ROLLBACK, $300 se habrian perdido (consistencia rota)")
        return

    print("\nSimula una transferencia que falla a mitad del proceso:")
    print("  1. BEGIN")
    print("  2. Resta $300 de Ana (NO sumes a Juan — simula un fallo)")
    print("  3. ROLLBACK")
    print("  4. Verifica que el saldo total volvio al valor original")
    print("\n# ==== ESCRIBE TU CODIGO AQUI ====")


if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            pista = 0
            if "-p" in sys.argv:
                idx = sys.argv.index("-p")
                if idx + 1 < len(sys.argv) and sys.argv[idx + 1].isdigit():
                    pista = int(sys.argv[idx + 1])
            ejercicios[num](pista)
    else:
        print("EJERCICIOS:")
        for i, ej in enumerate(ejercicios, 1):
            doc = ej.__doc__ or ""
            print(f"  {i}. {doc}")
