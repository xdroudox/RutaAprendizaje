"""
EJERCICIOS - HTML Semantico
Ejecuta desde raiz: python scripts/runner.py 6 1 [ejercicio] [-p N]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1(pista=0):
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
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  Las etiquetas semanticas describen el proposito del contenido.")
        print("  - <header>: cabecera de la pagina o seccion")
        print("  - <nav>: enlaces de navegacion")
        print("  - <main>: contenido principal (unico por pagina)")
        print("  - <section>: agrupa contenido relacionado tematicamente")
        print("  - <article>: contenido independiente y reutilizable")
        print("  - <footer>: pie de pagina")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  La estructura tipica es:")
        print("  <header>")
        print("    <h1>Titulo</h1>")
        print("    <nav><a href='#'>Inicio</a> | <a href='#'>Blog</a></nav>")
        print("  </header>")
        print("  <main>")
        print("    <section><h2>Seccion</h2><p>Contenido</p></section>")
        print("    <article><h3>Articulo</h3><p>Texto</p></article>")
        print("  </main>")
        print("  <footer><p>Copyright 2025</p></footer>")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  <header>")
        print("    <h1>Mi Sitio Web</h1>")
        print("    <nav>")
        print("      <a href='#'>Inicio</a> | <a href='#'>Blog</a> | <a href='#'>Contacto</a>")
        print("    </nav>")
        print("  </header>")
        print("  <main>")
        print("    <section>")
        print("      <h2>Bienvenido</h2>")
        print("      <p>Este es un sitio de ejemplo con HTML semantico.</p>")
        print("    </section>")
        print("    <article>")
        print("      <h3>HTML Semantico</h3>")
        print("      <p>El HTML semantico mejora la accesibilidad y el SEO.</p>")
        print("    </article>")
        print("  </main>")
        print("  <footer>")
        print("    <p>&copy; 2025 Mi Sitio Web</p>")
        print("  </footer>")

def ejercicio_2(pista=0):
    """Agregar aside y mejorar accesibilidad"""
    print(">> EJERCICIO 2: Agregar aside y mejorar accesibilidad")
    print("-" * 40)
    print("Abre: 06-frontend-web/01-html-semantico/ejercicios.html")
    print()
    print("Agrega un <aside> con contenido complementario.")
    print("Anade atributos de accesibilidad: role, aria-label, alt.")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  <aside> se usa para contenido tangencial como barras laterales.")
        print("  Atributos de accesibilidad utiles:")
        print("  - role='navigation' en <nav>")
        print("  - aria-label='Descripcion' en secciones")
        print("  - alt='Texto alternativo' en <img>")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  <aside aria-label='Contenido complementario'>")
        print("    <h3>Categorias</h3>")
        print("    <ul>")
        print("      <li><a href='#'>HTML</a></li>")
        print("      <li><a href='#'>CSS</a></li>")
        print("      <li><a href='#'>JavaScript</a></li>")
        print("    </ul>")
        print("  </aside>")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  Coloca <aside> dentro de <main>, despues del <article>:")
        print("  <main>")
        print("    <article>...contenido del articulo...</article>")
        print("    <aside aria-label='Sidebar'>")
        print("      <h3>Articulos Recientes</h3>")
        print("      <ul><li><a href='#'>Post 1</a></li><li><a href='#'>Post 2</a></li></ul>")
        print("    </aside>")
        print("  </main>")
        print("  Ademas, agrega role='navigation' al <nav> y alt descriptivo a las imagenes.")

def ejercicio_3(pista=0):
    """Blog completo con figure, time y article"""
    print(">> EJERCICIO 3: Blog completo con figure, time y article")
    print("-" * 40)
    print("Abre: 06-frontend-web/01-html-semantico/ejercicios.html")
    print()
    print("Crea la estructura completa de un blog usando:")
    print("  header, nav, main, article, section, aside, figure, time, footer")
    print("Debe contener al menos 2 articulos con imagen y fecha.")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  - <figure> agrupa imagen + <figcaption>")
        print("  - <time datetime='2025-01-15'>15 Enero 2025</time>")
        print("  - Cada <article> debe tener su propio <header> con <h2>")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  <article>")
        print("    <header><h2>Titulo del Articulo</h2></header>")
        print("    <figure>")
        print("      <img src='imagen.jpg' alt='Descripcion'>")
        print("      <figcaption>Pie de foto</figcaption>")
        print("    </figure>")
        print("    <p>Contenido del articulo...</p>")
        print("    <time datetime='2025-01-15'>15 Enero 2025</time>")
        print("  </article>")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  <header><h1>Mi Blog</h1><nav><a href='#'>Inicio</a><a href='#'>Contacto</a></nav></header>")
        print("  <main>")
        print("    <article>")
        print("      <header><h2>Como usar HTML Semantico</h2></header>")
        print("      <figure><img src='html.jpg' alt='Codigo HTML'><figcaption>Ejemplo</figcaption></figure>")
        print("      <p>El HTML semantico mejora la accesibilidad...</p>")
        print("      <time datetime='2025-01-15'>15 Enero 2025</time>")
        print("    </article>")
        print("    <article>")
        print("      <header><h2>CSS Grid vs Flexbox</h2></header>")
        print("      <figure><img src='css.jpg' alt='Layout CSS'><figcaption>Comparativa</figcaption></figure>")
        print("      <p>Ambos son herramientas de layout complementarias...</p>")
        print("      <time datetime='2025-01-20'>20 Enero 2025</time>")
        print("    </article>")
        print("    <aside><h3>Categorias</h3><ul><li>HTML</li><li>CSS</li></ul></aside>")
        print("  </main>")
        print("  <footer><p>&copy; 2025 Mi Blog</p></footer>")

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
