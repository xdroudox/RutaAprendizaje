"""
SOLUCIONES - CI/CD
Ejecuta desde raiz: python scripts/runner.py 10 03 [ejercicio] -s
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    """Workflow basico: crea un workflow YAML con build y test"""
    print(">> SOLUCION 1: Workflow basico CI")
    print("-" * 40)
    print("Contenido de .github/workflows/ci.yml:")
    print()
    print("  name: CI")
    print()
    print("  on:")
    print("    push:")
    print("      branches: [main]")
    print("    pull_request:")
    print("      branches: [main]")
    print()
    print("  jobs:")
    print("    test:")
    print("      runs-on: ubuntu-latest")
    print("      steps:")
    print("        - uses: actions/checkout@v4")
    print("        - uses: actions/setup-python@v5")
    print("          with:")
    print("            python-version: '3.11'")
    print("        - run: pip install -r requirements.txt")
    print("        - run: pytest")
    print()
    print("Explicacion:")
    print("  El workflow se dispara en push y PR a main.")
    print("  Clona el repo, instala Python, dependencias y ejecuta tests.")
    print("  Si algo falla, GitHub muestra el error en la pestana Actions.")

def solucion_2():
    """Agregar linting: anade un paso de linting al workflow"""
    print(">> SOLUCION 2: Workflow con linting")
    print("-" * 40)
    print("Contenido de .github/workflows/ci-lint.yml:")
    print()
    print("  name: CI with Lint")
    print()
    print("  on: [push, pull_request]")
    print()
    print("  jobs:")
    print("    test:")
    print("      runs-on: ubuntu-latest")
    print("      steps:")
    print("        - uses: actions/checkout@v4")
    print("        - uses: actions/setup-python@v5")
    print("          with:")
    print("            python-version: '3.11'")
    print("        - run: pip install -r requirements.txt")
    print("        - run: pytest")
    print("        - run: pip install ruff")
    print("        - run: ruff check .")
    print()
    print("Explicacion:")
    print("  Los pasos de linting se ejecutan SOLO si pytest pasa.")
    print("  Ruff revisa el codigo y falla si encuentra problemas de estilo o errores.")
    print("  Si el linter falla, el workflow se marca como fallido.")

def solucion_3():
    """Deploy a produccion: crea un pipeline completo CI/CD"""
    print(">> SOLUCION 3: Pipeline completo CI/CD")
    print("-" * 40)
    print("Contenido de .github/workflows/cd.yml:")
    print()
    print("  name: CI/CD")
    print()
    print("  on:")
    print("    push:")
    print("      branches: [main]")
    print()
    print("  jobs:")
    print("    test:")
    print("      runs-on: ubuntu-latest")
    print("      steps:")
    print("        - uses: actions/checkout@v4")
    print("        - uses: actions/setup-python@v5")
    print("          with:")
    print("            python-version: '3.11'")
    print("        - run: pip install -r requirements.txt")
    print("        - run: pytest")
    print("        - run: pip install ruff")
    print("        - run: ruff check .")
    print()
    print("    deploy:")
    print("      needs: test")
    print("      runs-on: ubuntu-latest")
    print("      if: github.ref == 'refs/heads/main'")
    print("      steps:")
    print("        - run: echo 'Desplegando a produccion...'")
    print()
    print("Explicacion:")
    print("  `needs: test` asegura que deploy solo corre si test pasa.")
    print("  `if: github.ref == 'refs/heads/main'` evita deploy en otras ramas.")
    print("  En produccion reemplazarias el echo por un script de deploy real.")

if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
    else:
        for i, sol in enumerate(soluciones, 1):
            print(f"  {i}. {sol.__doc__}")
