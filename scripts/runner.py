"""
RUNNER GLOBAL - Ejecuta cualquier ejercicio desde la raiz
Uso: python scripts/runner.py [nivel] [modulo] [ejercicio]

Ejemplos:
  python scripts/runner.py          -> Lista niveles
  python scripts/runner.py 1        -> Lista modulos del nivel 1
  python scripts/runner.py 1 1      -> Lista ejercicios del modulo
  python scripts/runner.py 1 1 1    -> Ejecuta ejercicio 1
  python scripts/runner.py 1 1 1 -s -> Ver solucion
"""

import sys
import os
import subprocess

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NIVELES = [
    ("01-fundamentos-python", "Fundamentos de Programacion", "Python"),
    ("02-poo-java", "POO + SOLID", "Java"),
    ("03-estructuras-datos", "Estructuras de Datos", "Python"),
    ("04-bases-datos", "Bases de Datos", "SQL + Python"),
    ("05-backend-apis", "Backend y APIs", "Java + Python"),
    ("06-frontend-web", "Frontend Web", "HTML/CSS/JS"),
    ("07-testing-calidad", "Testing y Calidad", "Python"),
    ("08-patrones-diseno", "Patrones de Diseno", "Java"),
    ("09-arquitecturas", "Arquitecturas", "Teoria"),
    ("10-devops-seguridad", "DevOps y Seguridad", "Varios"),
    ("11-proyecto-final", "Proyecto Final", "Todos"),
]

def obtener_modulos(nivel_idx):
    carpeta = NIVELES[nivel_idx][0]
    ruta = os.path.join(BASE, carpeta)
    modulos = sorted([d for d in os.listdir(ruta)
                      if os.path.isdir(os.path.join(ruta, d))])
    return modulos

def ejecutar_python(ruta, args):
    subprocess.run([sys.executable, ruta] + args)

def ejecutar_java(ruta_mod, args):
    java_file = os.path.join(ruta_mod, "Ejercicios.java")
    subprocess.run(["javac", java_file], cwd=ruta_mod, capture_output=True)
    subprocess.run(["java", "-cp", ruta_mod, "Ejercicios"] + args)

def main():
    args = sys.argv[1:]

    if not args:
        print("NIVELES DISPONIBLES:")
        for i, (_, nombre, lang) in enumerate(NIVELES, 1):
            mods = obtener_modulos(i - 1)
            print(f"  {i}. {nombre} ({lang}) - {len(mods)} modulos")
        print()
        print("Uso: python scripts/runner.py [nivel] [modulo] [ejercicio]")
        print("Ej:  python scripts/runner.py 1 1 1")
        return

    if not args[0].isdigit():
        print("El primer argumento debe ser un numero (nivel)")
        return

    nivel = int(args[0])
    if nivel < 1 or nivel > len(NIVELES):
        print(f"Nivel {nivel} no existe. Valores: 1-{len(NIVELES)}")
        return

    carp_nivel, nom_nivel, lang = NIVELES[nivel - 1]
    modulos = obtener_modulos(nivel - 1)

    if len(args) == 1:
        print(f"NIVEL {nivel}: {nom_nivel}")
        for i, m in enumerate(modulos, 1):
            print(f"  {i}. {m}")
        print()
        print(f"Uso: python scripts/runner.py {nivel} [modulo] [ejercicio]")
        return

    if not args[1].isdigit():
        return

    mod_num = int(args[1])
    if mod_num < 1 or mod_num > len(modulos):
        print(f"Modulo {mod_num} no existe. Valores: 1-{len(modulos)}")
        return

    modulo = modulos[mod_num - 1]
    ruta_mod = os.path.join(BASE, carp_nivel, modulo)

    py_file = os.path.join(ruta_mod, "ejercicios.py")
    java_file = os.path.join(ruta_mod, "Ejercicios.java")
    sol_file = os.path.join(ruta_mod, "soluciones.py")
    sol_java = os.path.join(ruta_mod, "Soluciones.java")

    if len(args) == 2:
        print(f"MENU DE EJERCICIOS - {modulo}")
        print(f"Ejecuta: python scripts/runner.py {nivel} {mod_num} [N]")
        print()
        # Try to show exercise descriptions from the file
        for ext, name in [(py_file, "ejercicios.py"), (java_file, "Ejercicios.java")]:
            if os.path.exists(ext):
                with open(ext, "r", encoding="utf-8") as f:
                    content = f.read()
                import re
                ej_descs = re.findall(r'def ejercicio_(\d+)\(\):.*?"""(.*?)"""', content, re.DOTALL)
                if ej_descs:
                    for num, desc in ej_descs:
                        desc = desc.strip().split("\n")[0][:80]
                        print(f"  {num}. {desc}")
                break
        return

    # Check for -s flag (solution)
    ver_solucion = "-s" in args
    ej_args = [a for a in args[2:] if a != "-s"]

    if ver_solucion:
        if os.path.exists(sol_file):
            ejecutar_python(sol_file, ej_args)
        elif os.path.exists(sol_java):
            subprocess.run(["javac", sol_java], cwd=ruta_mod, capture_output=True)
            subprocess.run(["java", "-cp", ruta_mod, "Soluciones"] + ej_args)
        else:
            print("No hay archivo de soluciones para este modulo")
        return

    if os.path.exists(py_file):
        ejecutar_python(py_file, ej_args)
    elif os.path.exists(java_file):
        ejecutar_java(ruta_mod, ej_args)
    else:
        print(f"No se encontro ejercicios.py ni Ejercicios.java en {ruta_mod}")

if __name__ == "__main__":
    main()
