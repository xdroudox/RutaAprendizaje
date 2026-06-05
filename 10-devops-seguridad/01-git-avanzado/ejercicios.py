"""
EJERCICIOS - Git Avanzado
Ejecuta desde raiz: python scripts/runner.py 10 01 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Inicializa un repositorio git, crea un archivo, haz add y commit"""
    print(">> EJERCICIO 1: Init, add y commit")
    print("-" * 40)
    print("Ejecuta estos comandos en tu terminal:")
    print()
    print("  mkdir mi-repo")
    print("  cd mi-repo")
    print("  git init")
    print("  echo '# Mi proyecto' > README.md")
    print("  git add README.md")
    print("  git commit -m 'Primer commit'")
    print()
    print("Luego ejecuta: git log --oneline")
    print("# ==== ESCRIBE AQUI EL OUTPUT DE git log ====")

def ejercicio_2():
    """Crea una rama, haz cambios en ella y fusionala a main"""
    print(">> EJERCICIO 2: Ramas y merge")
    print("-" * 40)
    print("Partiendo del repo anterior, ejecuta:")
    print()
    print("  git checkout -b feature/login")
    print("  echo '# Login page' > login.html")
    print("  git add login.html")
    print("  git commit -m 'Agrega login.html'")
    print("  git checkout main")
    print("  git merge feature/login")
    print()
    print("Luego ejecuta: git log --oneline --graph --all")
    print("# ==== ESCRIBE AQUI EL OUTPUT DE git log ====")

def ejercicio_3():
    """Simula y resuelve un conflicto de merge"""
    print(">> EJERCICIO 3: Resolver conflicto de merge")
    print("-" * 40)
    print("Ejecuta estos comandos:")
    print()
    print("  mkdir conflicto-repo && cd conflicto-repo")
    print("  git init")
    print("  echo 'Hola' > saludo.txt")
    print("  git add saludo.txt && git commit -m 'Commit inicial'")
    print("  git checkout -b feature/cambio")
    print("  echo 'Mundo' > saludo.txt")
    print("  git add saludo.txt && git commit -m 'Cambio en feature'")
    print("  git checkout main")
    print("  echo 'Hola mundo' > saludo.txt")
    print("  git add saludo.txt && git commit -m 'Cambio en main'")
    print("  git merge feature/cambio  # Aparece conflicto")
    print()
    print("Resuelve el conflicto editando saludo.txt, luego:")
    print("  git add saludo.txt")
    print("  git commit -m 'Resuelve conflicto'")
    print()
    print("# ==== ESCRIBE AQUI EL CONTENIDO FINAL DE saludo.txt ====")

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
