import sys
import subprocess
import platform

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def check(comando, nombre, version_flag="-v"):
    try:
        r = subprocess.run(
            f"{comando} {version_flag}".split(),
            capture_output=True, text=True, timeout=5
        )
        salida = r.stdout.strip() or r.stderr.strip()
        print(f"  [OK] {nombre}: {salida.splitlines()[0]}")
        return True
    except:
        print(f"  [NO] {nombre}: NO INSTALADO")
        return False

def main():
    print("=" * 50)
    print("  VERIFICANDO REQUISITOS")
    print("=" * 50)

    ok = True

    print(f"\nSistema: {platform.system()} {platform.release()}")

    print("\nPython:")
    if not check("python", "Python", "--version"):
        ok = False

    print("\nJava:")
    if not check("java", "Java", "-version"):
        ok = False
    if not check("javac", "Java Compiler", "-version"):
        ok = False

    print("\nGit:")
    if not check("git", "Git", "--version"):
        ok = False

    print("\nSQLite (built-in):")
    try:
        import sqlite3
        print(f"  [OK] SQLite {sqlite3.sqlite_version}")
    except:
        print("  [NO] SQLite no disponible")
        ok = False

    print(f"\n{'=' * 50}")
    if ok:
        print("  TODO LISTO! Comienza tu aventura!")
        print(f"  cd {__file__}\\..\\..")
        print("  code 00-roadmap/README.md")
    else:
        print("  Faltan requisitos. Instalalos y vuelve a ejecutar.")
    print("=" * 50)

if __name__ == "__main__":
    main()
