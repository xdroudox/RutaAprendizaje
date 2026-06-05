"""
EJERCICIOS - CSS Flexbox y Grid
Ejecuta desde raiz: python scripts/runner.py 6 2 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
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

def ejercicio_2():
    """Galeria responsiva con Flexbox wrap"""
    print(">> EJERCICIO 2: Galeria responsiva con Flexbox wrap")
    print("-" * 40)
    print("Abre: 06-frontend-web/02-css-flexbox-grid/ejercicios.html")
    print()
    print("Usa flex-wrap:wrap + flex: 1 1 200px en los items.")
    print("En grande: 3 por fila, mediano: 2, chico: 1.")

def ejercicio_3():
    """Layout completo con CSS Grid"""
    print(">> EJERCICIO 3: Layout completo con CSS Grid")
    print("-" * 40)
    print("Abre: 06-frontend-web/02-css-flexbox-grid/ejercicios.html")
    print()
    print("Crea: grid-template-columns: 200px 1fr 200px")
    print("      grid-template-rows: 80px 1fr 60px")
    print("Asigna grid-area a cada hijo para el layout completo.")

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            ejercicios[num]()
    else:
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
