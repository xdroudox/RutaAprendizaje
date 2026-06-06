"""
EJERCICIOS - CSS Flexbox y Grid
Ejecuta desde raiz: python scripts/runner.py 6 2 [ejercicio] [-p N]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1(pista=0):
    """Centrar elemento con Flexbox"""
    print(">> EJERCICIO 1: Centrar elemento con Flexbox")
    print("-" * 40)
    print("Este ejercicio es en HTML/CSS.")
    print("Abre el archivo en tu navegador:")
    print("  06-frontend-web/02-css-flexbox-grid/ejercicios.html")
    print()
    print("Usa display:flex, justify-content:center, align-items:center")
    print("en la clase .contenedor-flex para centrar el item rojo.")
    print("Edita el CSS en la seccion 'TU CODIGO AQUI'.")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  Necesitas 3 propiedades en .contenedor-flex:")
        print("  1. display: flex;  -- activa Flexbox")
        print("  2. justify-content: center;  -- centra horizontalmente")
        print("  3. align-items: center;  -- centra verticalmente")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  El contenedor padre debe tener altura definida:")
        print("  .contenedor-flex {")
        print("      display: flex;")
        print("      justify-content: center;")
        print("      align-items: center;")
        print("      /* height ya esta definido en el HTML */")
        print("  }")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  .contenedor-flex {")
        print("      display: flex;")
        print("      justify-content: center;")
        print("      align-items: center;")
        print("  }")
        print("  Esto centra el .item-rojo tanto horizontal como verticalmente.")

def ejercicio_2(pista=0):
    """Galeria responsiva con Flexbox wrap"""
    print(">> EJERCICIO 2: Galeria responsiva con Flexbox wrap")
    print("-" * 40)
    print("Abre: 06-frontend-web/02-css-flexbox-grid/ejercicios.html")
    print()
    print("Usa flex-wrap:wrap + flex: 1 1 200px en los items.")
    print("En grande: 3 por fila, mediano: 2, chico: 1.")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  - En el contenedor .galeria: display:flex + flex-wrap:wrap")
        print("  - En los items: flex: 1 1 200px")
        print("  - flex: grow shrink basis (crecer, encoger, tamano base)")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  .galeria {")
        print("      display: flex;")
        print("      flex-wrap: wrap;")
        print("      gap: 10px;")
        print("  }")
        print("  .galeria .item {")
        print("      flex: 1 1 200px;")
        print("  }")
        print("  flex: 1 1 200px significa:")
        print("  - grow: 1 (los items crecen para llenar el espacio)")
        print("  - shrink: 1 (los items se encogen si no caben)")
        print("  - basis: 200px (tamano base de cada item)")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  .galeria { display: flex; flex-wrap: wrap; gap: 10px; }")
        print("  .galeria .item { flex: 1 1 200px; }")
        print("  Con flex-wrap: wrap, cuando no caben 3 en 200px cada uno,")
        print("  pasan a 2 por fila, y finalmente 1 en pantallas pequenas.")

def ejercicio_3(pista=0):
    """Layout completo con CSS Grid"""
    print(">> EJERCICIO 3: Layout completo con CSS Grid")
    print("-" * 40)
    print("Abre: 06-frontend-web/02-css-flexbox-grid/ejercicios.html")
    print()
    print("Crea: grid-template-columns: 200px 1fr 200px")
    print("      grid-template-rows: 80px 1fr 60px")
    print("Asigna grid-area a cada hijo para el layout completo.")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  Necesitas definir: ")
        print("  - grid-template-columns: 200px 1fr 200px (3 columnas)")
        print("  - grid-template-rows: 80px 1fr 60px (3 filas)")
        print("  - grid-template-areas: para nombrar las regiones")
        print("  - grid-area en cada elemento hijo para asignarlo a una region")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  .grid-layout {")
        print("      display: grid;")
        print("      grid-template-columns: 200px 1fr 200px;")
        print("      grid-template-rows: 80px 1fr 60px;")
        print("      grid-template-areas:")
        print("          'header header header'")
        print("          'sidebar main aside'")
        print("          'footer footer footer';")
        print("      gap: 10px;")
        print("  }")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  .grid-layout > :nth-child(1) { grid-area: header; }")
        print("  .grid-layout > :nth-child(2) { grid-area: sidebar; }")
        print("  .grid-layout > :nth-child(3) { grid-area: main; }")
        print("  .grid-layout > :nth-child(4) { grid-area: aside; }")
        print("  .grid-layout > :nth-child(5) { grid-area: footer; }")
        print("  El layout resultante: header arriba, sidebar-main-aside en medio, footer abajo.")

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
