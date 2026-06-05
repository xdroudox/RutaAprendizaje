"""
EJERCICIOS - JavaScript DOM
Ejecuta desde raiz: python scripts/runner.py 6 3 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Manipular texto y estilos con DOM"""
    print(">> EJERCICIO 1: Manipular texto y estilos con DOM")
    print("-" * 40)
    print("Este ejercicio es en HTML/JS.")
    print("Abre el archivo en tu navegador:")
    print("  06-frontend-web/03-javascript-dom/ejercicios.html")
    print()
    print("Usa document.getElementById(), .textContent, .classList.add()")
    print("para cambiar el texto del parrafo y aplicar la clase 'destacado'.")
    print("Edita la funcion ejercicio1() en el HTML.")

def ejercicio_2():
    """Crear elementos con createElement y appendChild"""
    print(">> EJERCICIO 2: Crear elementos con createElement y appendChild")
    print("-" * 40)
    print("Abre: 06-frontend-web/03-javascript-dom/ejercicios.html")
    print()
    print("Crea nuevos divs con clase 'card' y los agrega al contenedor.")
    print("Usa document.createElement(), .classList.add(), .appendChild().")

def ejercicio_3():
    """Lista de tareas interactiva (to-do list)"""
    print(">> EJERCICIO 3: Lista de tareas interactiva (to-do list)")
    print("-" * 40)
    print("Abre: 06-frontend-web/03-javascript-dom/ejercicios.html")
    print()
    print("Crea una to-do list completa:")
    print("  - Lee el input y crea elementos <li>")
    print("  - Cada li tiene boton 'Eliminar'")
    print("  - Clic en li alterna clase 'completada'")

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            ejercicios[num]()
    else:
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
