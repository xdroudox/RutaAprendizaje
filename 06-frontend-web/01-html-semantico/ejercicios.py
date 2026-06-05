"""
EJERCICIOS - HTML Semantico
Ejecuta desde raiz: python scripts/runner.py 6 1 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Estructura HTML semantica basica"""
    print(">> EJERCICIO 1: Estructura HTML semantica basica")
    print("-" * 40)
    print("Este ejercicio es en HTML.")
    print("Abre el archivo en tu navegador:")
    print("  06-frontend-web/01-html-semantico/ejercicios.html")
    print()
    print("Reemplaza los <div> por etiquetas semanticas:")
    print("  - <header>, <nav>, <main>, <section>, <article>, <footer>")
    print("Edita la seccion marcada como 'INICIO: Edita este bloque' en el HTML.")

def ejercicio_2():
    """Agregar aside y mejorar accesibilidad"""
    print(">> EJERCICIO 2: Agregar aside y mejorar accesibilidad")
    print("-" * 40)
    print("Abre: 06-frontend-web/01-html-semantico/ejercicios.html")
    print()
    print("Agrega un <aside> con contenido complementario.")
    print("Anade atributos de accesibilidad: role, aria-label, alt.")

def ejercicio_3():
    """Blog completo con figure, time y article"""
    print(">> EJERCICIO 3: Blog completo con figure, time y article")
    print("-" * 40)
    print("Abre: 06-frontend-web/01-html-semantico/ejercicios.html")
    print()
    print("Crea la estructura completa de un blog usando:")
    print("  header, nav, main, article, section, aside, figure, time, footer")
    print("Debe contener al menos 2 articulos con imagen y fecha.")

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            ejercicios[num]()
    else:
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
