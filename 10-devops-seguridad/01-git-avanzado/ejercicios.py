"""
EJERCICIOS - Git Avanzado
Ejecuta desde raiz: python scripts/runner.py 10 01 [ejercicio] [-p N]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1(pista=0):
    """Init, add y commit: inicializa un repo y haz tu primer commit"""
    print(">> EJERCICIO 1: Init, add y commit")
    print("-" * 40)
    print("Crea un repositorio git, agrega un archivo README.md y realiza tu primer commit.")
    print()
    print("Comandos base:")
    print("  mkdir mi-repo")
    print("  cd mi-repo")
    print("  git init")
    print("  echo '# Mi proyecto' > README.md")
    print("  git add README.md")
    print("  git commit -m 'Primer commit'")
    print()
    print("Luego ejecuta:")
    print("  git log --oneline")
    print()
    print("# ==== ESCRIBE AQUI EL OUTPUT DE git log ====")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  `git init` crea el repositorio (solo una vez).")
        print("  `git add` pasa archivos al staging area.")
        print("  `git commit` los guarda en el historial.")
        print("  Sin `git add` no hay nada que commitear.")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  Secuencia completa:")
        print("    mkdir mi-repo")
        print("    cd mi-repo")
        print("    git init")
        print("    echo '# Mi proyecto' > README.md")
        print("    git add README.md")
        print("    git commit -m 'Primer commit'")
        print("    git log --oneline")
        print()
        print("  Si git log no muestra nada, olvidaste hacer commit.")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  La salida esperada de git log --oneline es algo como:")
        print("    abc1234 (HEAD -> main) Primer commit")
        print()
        print("  Para verificar tu estado en cada paso usa: git status")

def ejercicio_2(pista=0):
    """Ramas y merge: crea una rama, haz cambios y fusionala a main"""
    print(">> EJERCICIO 2: Ramas y merge")
    print("-" * 40)
    print("Partiendo del repositorio anterior (o uno nuevo), crea una rama")
    print("feature/login, agrega un archivo y fusiona los cambios a main.")
    print()
    print("Comandos:")
    print("  git checkout -b feature/login")
    print("  echo '# Login page' > login.html")
    print("  git add login.html")
    print("  git commit -m 'Agrega login.html'")
    print("  git checkout main")
    print("  git merge feature/login")
    print()
    print("Verifica el historial:")
    print("  git log --oneline --graph --all")
    print()
    print("# ==== ESCRIBE AQUI EL OUTPUT DE git log ====")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  `git checkout -b <rama>` crea y cambia a una nueva rama.")
        print("  `git merge <rama>` trae los cambios de esa rama a la actual.")
        print("  Haz merge estando en la rama donde QUIERES recibir los cambios.")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  Secuencia:")
        print("    git checkout -b feature/login")
        print("    echo '# Login page' > login.html")
        print("    git add login.html && git commit -m 'Agrega login.html'")
        print("    git checkout main")
        print("    git merge feature/login")
        print()
        print("  Si el merge falla, puede haber conflictos (los veremos en ej. 3).")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  Salida esperada de git log --oneline --graph --all:")
        print("    *   def7890 (HEAD -> main) Merge branch 'feature/login'")
        print("    |\\")
        print("    | * bcd2345 (feature/login) Agrega login.html")
        print("    |/")
        print("    * abc1234 Primer commit")
        print()
        print("  Las ramas no se borran solas. Puedes eliminar feature/login:")
        print("    git branch -d feature/login")

def ejercicio_3(pista=0):
    """Resolver conflicto: simula y resuelve un conflicto de merge"""
    print(">> EJERCICIO 3: Resolver conflicto de merge")
    print("-" * 40)
    print("Crea dos ramas que modifiquen la misma linea del mismo archivo")
    print("y luego resuelve el conflicto manualmente.")
    print()
    print("Comandos para generar el conflicto:")
    print("  mkdir conflicto-repo && cd conflicto-repo")
    print("  git init")
    print("  echo 'version inicial' > app.txt")
    print("  git add app.txt && git commit -m 'Commit inicial'")
    print()
    print("  git checkout -b feature/cambio")
    print("  echo 'cambio en feature' > app.txt")
    print("  git add app.txt && git commit -m 'Cambio en feature'")
    print()
    print("  git checkout main")
    print("  echo 'cambio en main' > app.txt")
    print("  git add app.txt && git commit -m 'Cambio en main'")
    print()
    print("  git merge feature/cambio   # Aparece CONFLICTO")
    print()
    print("Resuelve editando app.txt, conservando el texto que quieras.")
    print("Luego:")
    print("  git add app.txt")
    print("  git commit -m 'Conflicto resuelto'")
    print()
    print("# ==== ESCRIBE AQUI EL CONTENIDO FINAL DE app.txt ====")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  Cuando hay conflicto, git muestra:")
        print("    CONFLICT (content): Merge conflict in app.txt")
        print("  El archivo tendra marcadores especiales.")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  Abre app.txt y veras algo como:")
        print("    <<<<<<< HEAD")
        print("    cambio en main")
        print("    =======")
        print("    cambio en feature")
        print("    >>>>>>> feature/cambio")
        print()
        print("  Edita: borra los marcadores y deja solo el texto final deseado.")
        print("  Ejemplo: deja 'cambio en main unificado con feature'.")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  Despues de editar app.txt con el texto final:")
        print("    git add app.txt")
        print("    git commit -m 'Conflicto resuelto'")
        print()
        print("  Verifica: git log --oneline --graph --all")
        print("  Veras el commit de merge que resuelve el conflicto.")
        print("  Consejo: usa `git status` en cada paso para saber que sigue.")

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    pista_level = 0
    if "-p" in sys.argv:
        idx = sys.argv.index("-p")
        if idx + 1 < len(sys.argv) and sys.argv[idx + 1].isdigit():
            pista_level = int(sys.argv[idx + 1])
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            ejercicios[num](pista=pista_level)
    else:
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
