"""
EJERCICIOS - CI/CD
Ejecuta desde raiz: python scripts/runner.py 10 03 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Escribe un workflow YAML de GitHub Actions (build + test)"""
    print(">> EJERCICIO 1: Workflow basico CI")
    print("-" * 40)
    print("Crea .github/workflows/ci.yml con:")
    print()
    print("  - name: CI")
    print("  - on: push y pull_request a main")
    print("  - runs-on: ubuntu-latest")
    print("  - steps:")
    print("      1. actions/checkout@v4")
    print("      2. actions/setup-python@v5 (python 3.11)")
    print("      3. pip install -r requirements.txt")
    print("      4. pytest")
    print()
    print("# ==== ESCRIBE AQUI EL CONTENIDO DEL YAML ====")

def ejercicio_2():
    """Agrega un step de linting al workflow"""
    print(">> EJERCICIO 2: Agregar linting")
    print("-" * 40)
    print("Modifica el workflow anterior para agregar un step de linting:")
    print()
    print("  - Instalar ruff o flake8")
    print("  - Ejecutar linter sobre el codigo")
    print()
    print("Agrega despues del paso de pytest:")
    print("  - run: pip install ruff")
    print("  - run: ruff check .")
    print()
    print("# ==== ESCRIBE AQUI EL WORKFLOW COMPLETO CON LINTING ====")

def ejercicio_3():
    """Agrega deploy a produccion al workflow"""
    print(">> EJERCICIO 3: Deploy a produccion")
    print("-" * 40)
    print("Crea un workflow con DOS jobs:")
    print()
    print("  Job 'test':")
    print("    - checkout, setup python, dependencias, pytest, lint")
    print()
    print("  Job 'deploy':")
    print("    - needs: test")
    print("    - if: github.ref == 'refs/heads/main'")
    print("    - run: echo 'Desplegando a produccion...'")
    print()
    print("# ==== ESCRIBE AQUI EL WORKFLOW COMPLETO CON DEPLOY ====")

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
