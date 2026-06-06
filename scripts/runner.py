"""
RUNNER GLOBAL - Ejecuta cualquier ejercicio desde la raiz
Uso: python scripts/runner.py [nivel] [modulo] [ejercicio] [opciones]

Opciones:
  -s         Ver solucion
  -p N       Ver pista nivel N (1, 2 o 3)
  --check    Verificar si el ejercicio esta resuelto

Ejemplos:
  python scripts/runner.py              -> Lista niveles
  python scripts/runner.py 1            -> Lista modulos del nivel 1
  python scripts/runner.py 1 1          -> Lista ejercicios del modulo
  python scripts/runner.py 1 1 1        -> Ejecuta ejercicio 1
  python scripts/runner.py 1 1 1 -s     -> Ver solucion
  python scripts/runner.py 1 1 1 -p 1   -> Pista nivel 1
  python scripts/runner.py 1 1 1 --check -> Verificar si esta resuelto
"""

import sys
import os
import subprocess
import re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NIVELES = [
    ("01-fundamentos-python", "Fundamentos de Programacion", "Python"),
    ("02-poo-java", "POO + SOLID", "Java"),
    ("03-estructuras-datos", "Estructuras de Datos", "Python"),
    ("04-bases-datos", "Bases de Datos", "SQL + Python"),
    ("05-backend-apis", "Backend y APIs", "Python"),
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


def revisar_examen(ruta_mod, archivo):
    """Revisa si el ejercicio aun tiene placeholders sin resolver."""
    archivo_path = os.path.join(ruta_mod, archivo)
    if not os.path.exists(archivo_path):
        return None, "No se encontro el archivo de ejercicios"

    with open(archivo_path, "r", encoding="utf-8") as f:
        contenido = f.read()

    placeholders = []
    if "pass" in contenido:
        # Encontrar cuantos pass hay en funciones
        passes = re.findall(r'def ejercicio_\d+.*?:\n\s+pass', contenido)
        for p in passes:
            # Extraer el numero de ejercicio
            ej_num = re.search(r'ejercicio_(\d+)', p)
            if ej_num:
                placeholders.append(int(ej_num.group(1)))

    if "ESCRIBE TU RESPUESTA AQUI" in contenido:
        return False, "Aun tiene marcadores 'ESCRIBE TU RESPUESTA AQUI'"

    if placeholders:
        return False, f"Ejercicio(s) aun sin resolver: #{', #'.join(map(str, placeholders))}"

    return True, "Ejercicio completado (no se detectaron placeholders)"


def safe_print(text):
    """Print con reemplazo de emojis para compatibilidad con Windows."""
    try:
        print(text)
    except UnicodeEncodeError:
        safe = text.replace("🟢", "[BAS]").replace("🟡", "[INT]").replace("🔴", "[AVZ]")
        safe = safe.replace("💡", "[i]").replace("✅", "[OK]").replace("❌", "[X]")
        print(safe)


def listar_ejercicios(py_file, java_file):
    """Lista los ejercicios disponibles en un modulo."""
    for ext, name in [(py_file, "ejercicios.py"), (java_file, "Ejercicios.java")]:
        if os.path.exists(ext):
            with open(ext, "r", encoding="utf-8") as f:
                content = f.read()
            # Python: extraer de docstrings (con o sin parametro pista)
            ej_descs = re.findall(r'def ejercicio_(\d+)\([^)]*\):.*?"""(.*?)"""', content, re.DOTALL)
            if not ej_descs:
                # Java: extraer "🟢 Ej N: descripcion"
                java_ejs = re.findall(r'([🟢🟡🔴])\s+Ej\s+(\d+):\s*(.+)', content)
                if java_ejs:
                    for emoji, num, desc in java_ejs:
                        safe_print(f"  {num}. {emoji} {desc.strip()}")
                    return
                else:
                    continue
            for num, desc in ej_descs:
                desc = desc.strip().split("\n")[0][:80]
                nivel = "🟢"
                if "🔴" in desc or "avanz" in desc.lower():
                    nivel = "🔴"
                elif "🟡" in desc or "intermed" in desc.lower():
                    nivel = "🟡"
                desc = desc.replace("🟢", "").replace("🟡", "").replace("🔴", "").strip()
                safe_print(f"  {num}. {nivel} {desc}")
            return
    safe_print("  (No se encontraron ejercicios)")


def main():
    args = sys.argv[1:]

    if not args:
        print("=" * 50)
        print("  RUTA DE APRENDIZAJE - Runner")
        print("=" * 50)
        print()
        print("NIVELES DISPONIBLES:")
        for i, (_, nombre, lang) in enumerate(NIVELES, 1):
            mods = obtener_modulos(i - 1)
            print(f"  {i}. {nombre} ({lang}) - {len(mods)} modulos")
        print()
        print("Uso: python scripts/runner.py [nivel] [modulo] [ejercicio]")
        print("Ej:  python scripts/runner.py 1 1 1")
        print()
        print("Opciones:")
        print("  -s         Ver solucion")
        print("  -p N       Pista nivel N (1, 2, 3)")
        print("  --check    Verificar si el ejercicio esta resuelto")
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
        print(f"MODULO: {modulo}")
        print(f"Ejecuta: python scripts/runner.py {nivel} {mod_num} [N]")
        print()
        print("EJERCICIOS:")
        listar_ejercicios(py_file, java_file)
        return

    # Parsear banderas del runner (no consumir -p, eso va al subproceso)
    ver_solucion = "-s" in args
    hacer_check = "--check" in args

    # Pasar args al subproceso: solo quitar flags del runner
    ej_args = [a for a in args[2:] if a != "-s" and a != "--check"]

    if hacer_check:
        print(f"REVISANDO: {modulo}")
        print("-" * 40)
        if os.path.exists(py_file):
            resuelto, mensaje = revisar_examen(ruta_mod, "ejercicios.py")
            if resuelto is None:
                print(f"  {mensaje}")
            elif resuelto:
                print(f"  [OK] {mensaje}")
            else:
                print(f"  [PENDIENTE] {mensaje}")
                print()
                print("  Consejo: revisa la teoria con:")
                print(f"    code {carp_nivel}/{modulo}/README.md")
        elif os.path.exists(java_file):
            # Verificar si el archivo Java tiene placeholders
            resuelto, mensaje = revisar_examen(ruta_mod, "Ejercicios.java")
            if resuelto is None:
                print(f"  {mensaje}")
            elif resuelto:
                print(f"  [OK] {mensaje}")
            else:
                print(f"  [PENDIENTE] {mensaje}")
        else:
            print("  No hay archivos de ejercicios en este modulo")
        return

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
