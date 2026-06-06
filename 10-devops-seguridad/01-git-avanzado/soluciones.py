"""
SOLUCIONES - Git Avanzado
Ejecuta desde raiz: python scripts/runner.py 10 01 [ejercicio] -s
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    """Init, add y commit: inicializa un repo y haz tu primer commit"""
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
    print()
    print("Explicacion:")
    print("  `git init` crea la carpeta .git con el repositorio.")
    print("  `git add README.md` lleva el archivo al staging area.")
    print("  `git commit` guarda el snapshot con el mensaje indicado.")
    print("  `git log` muestra el historial de commits.")

def solucion_2():
    """Ramas y merge: crea una rama, haz cambios y fusionala a main"""
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
    print()
    print("Explicacion:")
    print("  `-b` en checkout crea la rama y cambia a ella.")
    print("  Los commits en feature/login no afectan a main hasta el merge.")
    print("  El merge crea un commit adicional de fusion.")

def solucion_3():
    """Resolver conflicto: simula y resuelve un conflicto de merge"""
    print(">> SOLUCION 3: Resolver conflicto de merge")
    print("-" * 40)
    print("Comandos ejecutados:")
    print()
    print("  mkdir conflicto-repo && cd conflicto-repo")
    print("  git init")
    print("  echo 'version inicial' > app.txt")
    print("  git add app.txt && git commit -m 'Commit inicial'")
    print("  git checkout -b feature/cambio")
    print("  echo 'cambio en feature' > app.txt")
    print("  git add app.txt && git commit -m 'Cambio en feature'")
    print("  git checkout main")
    print("  echo 'cambio en main' > app.txt")
    print("  git add app.txt && git commit -m 'Cambio en main'")
    print("  git merge feature/cambio")
    print()
    print("Al abrir app.txt durante el conflicto:")
    print("  <<<<<<< HEAD")
    print("  cambio en main")
    print("  =======")
    print("  cambio en feature")
    print("  >>>>>>> feature/cambio")
    print()
    print("Editas app.txt para dejar el texto deseado, por ejemplo:")
    print("  cambio en main unificado")
    print()
    print("Luego:")
    print("  git add app.txt")
    print("  git commit -m 'Conflicto resuelto'")
    print()
    print("Explicacion:")
    print("  HEAD = tu rama actual (main).")
    print("  feature/cambio = la rama que estas fusionando.")
    print("  Editas, eliminas marcadores, add y commit.")

if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
    else:
        for i, sol in enumerate(soluciones, 1):
            print(f"  {i}. {sol.__doc__}")
