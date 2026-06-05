"""
SOLUCIONES - HTML Semantico
Ejecuta desde raiz: python scripts/runner.py 6 1 [ejercicio] -s
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Estructura HTML semantica basica"""
    print(">> SOLUCION 1: Estructura HTML semantica basica")
    print("-" * 40)
    print("Reemplaza los <div> por etiquetas semanticas:")
    print()
    print("<header>")
    print("  <h1>Mi Sitio Web</h1>")
    print("  <nav>")
    print("    <a href='#'>Inicio</a> | <a href='#'>Blog</a> | <a href='#'>Contacto</a>")
    print("  </nav>")
    print("</header>")
    print()
    print("<main>")
    print("  <section>")
    print("    <h2>Bienvenido</h2>")
    print("    <p>Este es un sitio de ejemplo...</p>")
    print("  </section>")
    print("  <article>")
    print("    <h3>HTML Semantico</h3>")
    print("    <p>El HTML semantico mejora la accesibilidad...</p>")
    print("  </article>")
    print("</main>")
    print()
    print("<footer>")
    print("  <p>&copy; 2025 Mi Sitio Web</p>")
    print("</footer>")
    print()
    print("Abre soluciones.html en el navegador para verlo en accion.")

def ejercicio_2():
    """Agregar aside y mejorar accesibilidad"""
    print(">> SOLUCION 2: Agregar aside y mejorar accesibilidad")
    print("-" * 40)
    print("Agrega <aside> con aria-label dentro de <main>:")
    print()
    print("<aside aria-label='Contenido complementario'>")
    print("  <h3>Categorias</h3>")
    print("  <ul>")
    print("    <li><a href='#'>HTML</a></li>")
    print("    <li><a href='#'>CSS</a></li>")
    print("    <li><a href='#'>JavaScript</a></li>")
    print("  </ul>")
    print("</aside>")
    print()
    print("Agrega role='navigation' al <nav> y alt a las <img>.")

def ejercicio_3():
    """Blog completo con figure, time y article"""
    print(">> SOLUCION 3: Blog completo con figure, time y article")
    print("-" * 40)
    print("Estructura completa del blog:")
    print()
    print("<header><h1>Mi Blog</h1><nav>...</nav></header>")
    print("<main>")
    print("  <article>")
    print("    <header><h2>Articulo 1</h2></header>")
    print("    <figure>")
    print("      <img src='...' alt='...'>")
    print("      <figcaption>Descripcion de la imagen</figcaption>")
    print("    </figure>")
    print("    <p>Contenido del articulo...</p>")
    print("    <time datetime='2025-01-15'>15 Enero 2025</time>")
    print("  </article>")
    print("  <aside>Sidebar</aside>")
    print("</main>")
    print("<footer>Copyright 2025</footer>")

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            ejercicios[num]()
    else:
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
