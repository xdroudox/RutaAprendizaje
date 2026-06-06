"""
EJERCICIOS - JavaScript DOM
Ejecuta desde raiz: python scripts/runner.py 6 3 [ejercicio] [-p N]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1(pista=0):
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
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  Pasos:")
        print("  1. Obtener el elemento con document.getElementById('parrafo-ej1')")
        print("  2. Cambiar su texto con .textContent")
        print("  3. Anadir clase con .classList.add('destacado')")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  var parrafo = document.getElementById('parrafo-ej1');")
        print("  parrafo.textContent = 'Texto cambiado con exito!';")
        print("  parrafo.classList.add('destacado');")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  function ejercicio1() {")
        print("      var parrafo = document.getElementById('parrafo-ej1');")
        print("      parrafo.textContent = 'Texto cambiado con exito!';")
        print("      parrafo.classList.add('destacado');")
        print("  }")

def ejercicio_2(pista=0):
    """Crear elementos con createElement y appendChild"""
    print(">> EJERCICIO 2: Crear elementos con createElement y appendChild")
    print("-" * 40)
    print("Abre: 06-frontend-web/03-javascript-dom/ejercicios.html")
    print()
    print("Crea nuevos divs con clase 'card' y los agrega al contenedor.")
    print("Usa document.createElement(), .classList.add(), .appendChild().")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  Pasos:")
        print("  1. Crear div con document.createElement('div')")
        print("  2. Anadir clase 'card' con .classList.add('card')")
        print("  3. Asignar texto con .textContent")
        print("  4. Agregar al contenedor con .appendChild()")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  var div = document.createElement('div');")
        print("  div.classList.add('card');")
        print("  div.textContent = 'Elemento #' + contador;")
        print("  contenedor.appendChild(div);")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  var contenedor = document.getElementById('contenedor-ej2');")
        print("  var div = document.createElement('div');")
        print("  div.classList.add('card');")
        print("  div.textContent = 'Elemento #' + (++contadorEj2);")
        print("  contenedor.appendChild(div);")

def ejercicio_3(pista=0):
    """Lista de tareas interactiva (to-do list)"""
    print(">> EJERCICIO 3: Lista de tareas interactiva (to-do list)")
    print("-" * 40)
    print("Abre: 06-frontend-web/03-javascript-dom/ejercicios.html")
    print()
    print("Crea una to-do list completa:")
    print("  - Lee el input y crea elementos <li>")
    print("  - Cada li tiene boton 'Eliminar'")
    print("  - Clic en li alterna clase 'completada'")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  Pasos en agregarTarea():")
        print("  1. Obtener el valor del input y recortar espacios (.trim())")
        print("  2. Si esta vacio, retornar")
        print("  3. Crear <li> con createElement")
        print("  4. Crear <button> con texto 'Eliminar'")
        print("  5. Agregar el boton al li con appendChild")
        print("  6. Agregar el li a la lista")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  var li = document.createElement('li');")
        print("  li.textContent = texto;")
        print("  var btn = document.createElement('button');")
        print("  btn.textContent = 'Eliminar';")
        print("  btn.onclick = function() { li.remove(); };")
        print("  li.appendChild(btn);")
        print("  li.onclick = function(e) {")
        print("      if (e.target.tagName !== 'BUTTON') li.classList.toggle('completada');")
        print("  };")
        print("  lista.appendChild(li);")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  function agregarTarea() {")
        print("      var input = document.getElementById('input-tarea');")
        print("      var lista = document.getElementById('lista-tareas');")
        print("      var texto = input.value.trim();")
        print("      if (texto === '') return;")
        print("      var li = document.createElement('li');")
        print("      li.textContent = texto;")
        print("      var btn = document.createElement('button');")
        print("      btn.textContent = 'Eliminar';")
        print("      btn.className = 'btn-eliminar';")
        print("      btn.onclick = function() { li.remove(); };")
        print("      li.appendChild(btn);")
        print("      li.onclick = function(e) {")
        print("          if (e.target.tagName !== 'BUTTON') li.classList.toggle('completada');")
        print("      };")
        print("      lista.appendChild(li);")
        print("      input.value = '';")
        print("  }")

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
