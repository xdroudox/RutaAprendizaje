"""
SOLUCIONES - Git Avanzado
Ejecuta desde raiz: python scripts/runner.py 10 01 [ejercicio] solucion
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    """Inicializa un repositorio git, crea un archivo, haz add y commit"""
    print(">> SOLUCION 1: Init, add y commit")
    print("-" * 40)
    print("Comandos ejecutados:")
    print()
    print("  mkdir mi-repo")
    print("  cd mi-repo")
    print("  git init")
    print("  echo '# Mi proyecto' > README.md")
    print("  git add README.md")
    print("  git commit -m 'Primer commit'")
    print("  git log --oneline")
    print()
    print("Output esperado:")
    print("  $ git log --oneline")
    print("  abc1234 (HEAD -> main) Primer commit")

def solucion_2():
    """Crea una rama, haz cambios en ella y fusionala a main"""
    print(">> SOLUCION 2: Ramas y merge")
    print("-" * 40)
    print("Comandos ejecutados:")
    print()
    print("  git checkout -b feature/login")
    print("  echo '# Login page' > login.html")
    print("  git add login.html")
    print("  git commit -m 'Agrega login.html'")
    print("  git checkout main")
    print("  git merge feature/login")
    print()
    print("Output esperado:")
    print("  $ git log --oneline --graph --all")
    print("  *   def7890 (HEAD -> main) Merge branch 'feature/login'")
    print("  |\\")
    print("  | * bcd2345 (feature/login) Agrega login.html")
    print("  |/")
    print("  * abc1234 Primer commit")

def solucion_3():
    """Simula y resuelve un conflicto de merge"""
    print(">> SOLUCION 3: Resolver conflicto de merge")
    print("-" * 40)
    print("Comandos ejecutados:")
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
    print("Contenido final de saludo.txt:")
    print("  Hola mundo")
    print()
    print("Explicacion:")
    print("  main tenia 'Hola mundo', feature tenia 'Mundo'.")
    print("  Se edito manualmente para dejar el texto deseado y se confirmo.")

if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            print(f">> SOLUCION {num + 1}: {soluciones[num].__doc__}")
            print("-" * 40)
            soluciones[num]()
    else:
        for i, sol in enumerate(soluciones, 1):
            print(f"  {i}. {sol.__doc__}")
