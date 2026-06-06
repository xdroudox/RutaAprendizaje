"""
SOLUCIONES - JavaScript DOM
Ejecuta desde raiz: python scripts/runner.py 6 3 [ejercicio] -s
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    """Manipular texto y estilos con DOM"""
    print(">> SOLUCION 1: Manipular texto y estilos con DOM")
    print("-" * 40)
    print("function ejercicio1() {")
    print("    var parrafo = document.getElementById('parrafo-ej1');")
    print("    parrafo.textContent = 'Texto cambiado con exito!';")
    print("    parrafo.classList.add('destacado');")
    print("}")
    print()
    print("Abre soluciones.html en el navegador para verlo en accion.")

def solucion_2():
    """Crear elementos con createElement y appendChild"""
    print(">> SOLUCION 2: Crear elementos con createElement y appendChild")
    print("-" * 40)
    print("function ejercicio2() {")
    print("    var contenedor = document.getElementById('contenedor-ej2');")
    print("    var div = document.createElement('div');")
    print("    div.classList.add('card');")
    print("    div.textContent = 'Elemento #' + (++contadorEj2);")
    print("    contenedor.appendChild(div);")
    print("}")
    print("function limpiarEj2() {")
    print("    var contenedor = document.getElementById('contenedor-ej2');")
    print("    contenedor.innerHTML = '';")
    print("    contadorEj2 = 0;")
    print("}")

def solucion_3():
    """Lista de tareas interactiva (to-do list)"""
    print(">> SOLUCION 3: Lista de tareas interactiva (to-do list)")
    print("-" * 40)
    print("function agregarTarea() {")
    print("    var input = document.getElementById('input-tarea');")
    print("    var lista = document.getElementById('lista-tareas');")
    print("    var texto = input.value.trim();")
    print("    if (texto === '') return;")
    print()
    print("    var li = document.createElement('li');")
    print("    li.textContent = texto;")
    print()
    print("    var btnEliminar = document.createElement('button');")
    print("    btnEliminar.textContent = 'Eliminar';")
    print("    btnEliminar.classList.add('btn-eliminar');")
    print("    btnEliminar.onclick = function() { li.remove(); };")
    print()
    print("    li.appendChild(btnEliminar);")
    print("    li.onclick = function(e) {")
    print("        if (e.target.tagName !== 'BUTTON') {")
    print("            li.classList.toggle('completada');")
    print("        }")
    print("    };")
    print("    lista.appendChild(li);")
    print("    input.value = '';")
    print("}")

if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
    else:
        for i, sol in enumerate(soluciones, 1):
            print(f"  {i}. {sol.__doc__}")
