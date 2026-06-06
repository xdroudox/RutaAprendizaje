"""
EJERCICIOS - Eventos y Asincronia
Ejecuta desde raiz: python scripts/runner.py 6 4 [ejercicio] [-p N]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1(pista=0):
    """Eventos de raton: click, mouseenter, mouseleave"""
    print(">> EJERCICIO 1: Eventos de raton")
    print("-" * 40)
    print("Este ejercicio es en HTML/JS.")
    print("Abre el archivo en tu navegador:")
    print("  06-frontend-web/04-eventos-asincronia/ejercicios.html")
    print()
    print("Agrega event listeners a la caja roja:")
    print("  - click: cambiar color a azul y texto 'Click!'")
    print("  - mouseenter: escala 1.2 y texto 'Hover!'")
    print("  - mouseleave: restaurar original y texto 'Fuera!'")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  Usa addEventListener en la caja (document.getElementById('caja1')):")
        print("  - elemento.addEventListener('click', function() { ... })")
        print("  - elemento.addEventListener('mouseenter', function() { ... })")
        print("  - elemento.addEventListener('mouseleave', function() { ... })")
        print("  Dentro de cada funcion, this o elemento.target referencia la caja.")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  caja1.addEventListener('click', function() {")
        print("      this.style.background = '#3498db';")
        print("      this.textContent = 'Click!';")
        print("  });")
        print("  caja1.addEventListener('mouseenter', function() {")
        print("      this.style.transform = 'scale(1.2)';")
        print("      this.textContent = 'Hover!';")
        print("  });")
        print("  caja1.addEventListener('mouseleave', function() {")
        print("      this.style.transform = 'scale(1)';")
        print("      this.style.background = '#e74c3c';")
        print("      this.textContent = 'Fuera!';")
        print("  });")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  var caja1 = document.getElementById('caja1');")
        print("  caja1.addEventListener('click', function() {")
        print("      this.style.background = '#3498db'; this.textContent = 'Click!';")
        print("  });")
        print("  caja1.addEventListener('mouseenter', function() {")
        print("      this.style.transform = 'scale(1.2)'; this.textContent = 'Hover!';")
        print("  });")
        print("  caja1.addEventListener('mouseleave', function() {")
        print("      this.style.transform = 'scale(1)'; this.style.background = '#e74c3c';")
        print("      this.textContent = 'Fuera!';")
        print("  });")

def ejercicio_2(pista=0):
    """setTimeout y setInterval para cuenta regresiva"""
    print(">> EJERCICIO 2: setTimeout y setInterval para cuenta regresiva")
    print("-" * 40)
    print("Abre: 06-frontend-web/04-eventos-asincronia/ejercicios.html")
    print()
    print("Implementa una cuenta regresiva del 5 al 1:")
    print("  - setInterval cada 1 segundo")
    print("  - clearInterval al llegar a 0")
    print("  - Muestra 'Despegue!' al finalizar")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  - Inicializa contador = 5")
        print("  - setInterval cada 1000ms que decremente contador")
        print("  - Cuando contador <= 0, clearInterval y muestra 'Despegue!'")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  var contador = 5;")
        print("  display.textContent = contador;")
        print("  var intervalo = setInterval(function() {")
        print("      contador--;")
        print("      if (contador <= 0) {")
        print("          clearInterval(intervalo);")
        print("          display.textContent = 'Despegue!';")
        print("      } else {")
        print("          display.textContent = contador;")
        print("      }")
        print("  }, 1000);")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  function iniciarCuenta() {")
        print("      if (intervaloCuenta) return;")
        print("      contador = 5;")
        print("      display.textContent = contador;")
        print("      intervaloCuenta = setInterval(function() {")
        print("          contador--;")
        print("          if (contador <= 0) {")
        print("              clearInterval(intervaloCuenta);")
        print("              intervaloCuenta = null;")
        print("              display.textContent = 'Despegue!';")
        print("          } else {")
        print("              display.textContent = contador;")
        print("          }")
        print("      }, 1000);")
        print("  }")

def ejercicio_3(pista=0):
    """Promesa simple con async/await"""
    print(">> EJERCICIO 3: Promesa simple con async/await")
    print("-" * 40)
    print("Abre: 06-frontend-web/04-eventos-asincronia/ejercicios.html")
    print()
    print("Simula una operacion asincrona:")
    print("  - Crea una Promise con setTimeout de 2s")
    print("  - Usa async/await con try/catch")
    print("  - Muestra 'Cargando...' -> 'Operacion completada!'")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  1. Crea una funcion que retorne new Promise(resolve, reject)")
        print("  2. Dentro: setTimeout(resolve, 2000)")
        print("  3. Crea una funcion async que haga await de la promesa")
        print("  4. Envuelve en try/catch por si hay error")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  function esperar(ms) {")
        print("      return new Promise(function(resolve) {")
        print("          setTimeout(resolve, ms);")
        print("      });")
        print("  }")
        print("  async function iniciarOperacion() {")
        print("      try {")
        print("          await esperar(2000);")
        print("          displayOp.textContent = 'Operacion completada!';")
        print("      } catch (error) {")
        print("          displayOp.textContent = 'Error en la operacion';")
        print("      }")
        print("  }")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  function esperar(ms) {")
        print("      return new Promise(function(resolve, reject) {")
        print("          if (modoError) {")
        print("              reject(new Error('Modo error activado'));")
        print("          } else {")
        print("              setTimeout(resolve, ms);")
        print("          }")
        print("      });")
        print("  }")
        print("  async function iniciarOperacion() {")
        print("      try {")
        print("          displayOp.textContent = 'Cargando...';")
        print("          await esperar(2000);")
        print("          displayOp.textContent = 'Operacion completada!';")
        print("      } catch (error) {")
        print("          displayOp.textContent = 'Error: ' + error.message;")
        print("      }")
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
