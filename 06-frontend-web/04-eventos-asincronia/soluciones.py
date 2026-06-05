"""
SOLUCIONES - Eventos y Asincronia
Ejecuta desde raiz: python scripts/runner.py 6 4 [ejercicio] -s
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Eventos de raton: click, mouseenter, mouseleave"""
    print(">> SOLUCION 1: Eventos de raton")
    print("-" * 40)
    print("caja1.addEventListener('click', function() {")
    print("    this.style.background = '#3498db';")
    print("    this.textContent = 'Click!';")
    print("    logMsg('Click!');")
    print("});")
    print("caja1.addEventListener('mouseenter', function() {")
    print("    this.style.transform = 'scale(1.2)';")
    print("    this.textContent = 'Hover!';")
    print("    logMsg('Mouse enter');")
    print("});")
    print("caja1.addEventListener('mouseleave', function() {")
    print("    this.style.transform = 'scale(1)';")
    print("    this.style.background = '#e74c3c';")
    print("    this.textContent = 'Fuera!';")
    print("    logMsg('Mouse leave');")
    print("});")
    print()
    print("Abre soluciones.html en el navegador para verlo en accion.")

def ejercicio_2():
    """setTimeout y setInterval para cuenta regresiva"""
    print(">> SOLUCION 2: setTimeout y setInterval para cuenta regresiva")
    print("-" * 40)
    print("function iniciarCuenta() {")
    print("    if (intervaloCuenta) return;")
    print("    contador = 5;")
    print("    display.textContent = contador;")
    print("    intervaloCuenta = setInterval(function() {")
    print("        contador--;")
    print("        if (contador <= 0) {")
    print("            clearInterval(intervaloCuenta);")
    print("            intervaloCuenta = null;")
    print("            display.textContent = 'Despegue!';")
    print("        } else {")
    print("            display.textContent = contador;")
    print("        }")
    print("    }, 1000);")
    print("}")
    print("function detenerCuenta() {")
    print("    if (intervaloCuenta) {")
    print("        clearInterval(intervaloCuenta);")
    print("        intervaloCuenta = null;")
    print("    }")
    print("    display.textContent = '-';")
    print("}")

def ejercicio_3():
    """Promesa simple con async/await"""
    print(">> SOLUCION 3: Promesa simple con async/await")
    print("-" * 40)
    print("function esperar(ms) {")
    print("    return new Promise(function(resolve, reject) {")
    print("        if (modoError) {")
    print("            reject(new Error('Modo error activado'));")
    print("        } else {")
    print("            setTimeout(resolve, ms);")
    print("        }")
    print("    });")
    print("}")
    print("async function iniciarOperacion() {")
    print("    try {")
    print("        await esperar(2000);")
    print("        displayOp.textContent = 'Operacion completada!';")
    print("    } catch (error) {")
    print("        displayOp.textContent = 'Error en la operacion';")
    print("    }")
    print("}")

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            ejercicios[num]()
    else:
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
