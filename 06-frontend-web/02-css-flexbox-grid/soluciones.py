"""
SOLUCIONES - CSS Flexbox y Grid
Ejecuta desde raiz: python scripts/runner.py 6 2 [ejercicio] -s
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Centrar elemento con Flexbox"""
    print(">> SOLUCION 1: Centrar elemento con Flexbox")
    print("-" * 40)
    print(".contenedor-flex {")
    print("    display: flex;")
    print("    justify-content: center;")
    print("    align-items: center;")
    print("}")
    print()
    print("Abre soluciones.html en el navegador para verlo en accion.")

def ejercicio_2():
    """Galeria responsiva con Flexbox wrap"""
    print(">> SOLUCION 2: Galeria responsiva con Flexbox wrap")
    print("-" * 40)
    print(".galeria {")
    print("    display: flex;")
    print("    flex-wrap: wrap;")
    print("    gap: 10px;")
    print("}")
    print(".galeria .item {")
    print("    flex: 1 1 200px;")
    print("}")

def ejercicio_3():
    """Layout completo con CSS Grid"""
    print(">> SOLUCION 3: Layout completo con CSS Grid")
    print("-" * 40)
    print(".grid-layout {")
    print("    display: grid;")
    print("    grid-template-columns: 200px 1fr 200px;")
    print("    grid-template-rows: 80px 1fr 60px;")
    print("    grid-template-areas:")
    print("        'header header header'")
    print("        'sidebar main aside'")
    print("        'footer footer footer';")
    print("    gap: 10px;")
    print("}")
    print(".grid-layout > :nth-child(1) { grid-area: header; }")
    print(".grid-layout > :nth-child(2) { grid-area: sidebar; }")
    print(".grid-layout > :nth-child(3) { grid-area: main; }")
    print(".grid-layout > :nth-child(4) { grid-area: aside; }")
    print(".grid-layout > :nth-child(5) { grid-area: footer; }")

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            ejercicios[num]()
    else:
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
