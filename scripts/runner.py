"""
🏃 Ejecutador rápido de ejercicios

Uso:
  python scripts/runner.py                    # Ver niveles disponibles
  python scripts/runner.py 1                   # Ver temas del nivel 1
  python scripts/runner.py 1 2                 # Ejecutar ejercicio 2 del nivel 1
  python scripts/runner.py 1 2 -p             # Con pista
  python scripts/runner.py 1 2 -s             # Ver solución
"""

import sys
import os
import subprocess

NIVELES = {
    1: ("01-fundamentos-python", "Python"),
    2: ("02-poo-java", "Java"),
    3: ("03-estructuras-datos", "Python"),
    4: ("04-bases-datos", "SQL+Python"),
    5: ("05-backend-apis", "Java+Python"),
    6: ("06-frontend-web", "HTML/CSS/JS"),
    7: ("07-testing-calidad", "Python"),
    8: ("08-patrones-diseno", "Java"),
    9: ("09-arquitecturas", "Teoría"),
    10: ("10-devops-seguridad", "Varios"),
    11: ("11-proyecto-final", "Todos"),
}

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def listar_niveles():
    print("📋 NIVELES DISPONIBLES:")
    for n, (carp, lang) in NIVELES.items():
        carpetas = os.listdir(os.path.join(BASE, carp))
        temas = [c for c in carpetas if os.path.isdir(os.path.join(BASE, carp, c))]
        print(f"  {n}. {carp} ({lang}) - {len(temas)} temas")

def listar_temas(nivel):
    carp, _ = NIVELES.get(nivel, (None, None))
    if not carp:
        print(f"❌ Nivel {nivel} no existe")
        return
    ruta = os.path.join(BASE, carp)
    temas = sorted([c for c in os.listdir(ruta) if os.path.isdir(os.path.join(ruta, c))])
    print(f"📋 TEMAS DEL {carp}:")
    for i, t in enumerate(temas, 1):
        print(f"  {i}. {t}")

def ejecutar(nivel, tema_num=1, pista=False, solucion=False):
    carp, lang = NIVELES.get(nivel, (None, None))
    if not carp:
        print(f"❌ Nivel {nivel} no existe")
        return
    ruta = os.path.join(BASE, carp)
    temas = sorted([c for c in os.listdir(ruta) if os.path.isdir(os.path.join(ruta, c))])
    if tema_num < 1 or tema_num > len(temas):
        print(f"❌ Tema {tema_num} no existe (hay {len(temas)})")
        return
    tema = temas[tema_num - 1]
    ruta_tema = os.path.join(ruta, tema)

    if solucion:
        archivo = None
        for f in os.listdir(ruta_tema):
            if f.lower().startswith("solucion"):
                archivo = os.path.join(ruta_tema, f)
                break
        if not archivo:
            print(f"❌ No se encontró archivo de soluciones en {tema}")
            return
    else:
        archivo = None
        for f in os.listdir(ruta_tema):
            if f.lower().startswith("ejercicio"):
                archivo = os.path.join(ruta_tema, f)
                break
        if not archivo:
            print(f"❌ No se encontró archivo de ejercicios en {tema}")
            return

    print(f"🎯 Ejecutando: {tema}")
    print(f"📁 {archivo}")
    print()

    if archivo.endswith(".py"):
        cmd = ["python", archivo]
        if solucion:
            cmd.extend(["--solucion"])
        elif pista:
            cmd.extend(["--pista"])
        else:
            cmd.append("1")
        subprocess.run(cmd, cwd=ruta_tema)
    elif archivo.endswith(".java"):
        subprocess.run(["javac", archivo], cwd=ruta_tema)
        class_name = os.path.splitext(os.path.basename(archivo))[0]
        cmd = ["java", class_name]
        if solucion:
            cmd.append("--solucion")
        elif pista:
            cmd.append("--pista")
        else:
            cmd.append("1")
        subprocess.run(cmd, cwd=ruta_tema)

def main():
    args = sys.argv[1:]

    if not args:
        listar_niveles()
        return

    if args[0].isdigit():
        nivel = int(args[0])
        if len(args) >= 2 and args[1].isdigit():
            tema = int(args[1])
            pista = "-p" in args
            solucion = "-s" in args
            ejecutar(nivel, tema, pista, solucion)
        else:
            listar_temas(nivel)

if __name__ == "__main__":
    main()
