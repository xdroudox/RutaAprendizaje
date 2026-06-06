"""
SOLUCIONES - Seguridad Web
Ejecuta desde raiz: python scripts/runner.py 6 7 [ejercicio] -s
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    """Prevenir XSS usando textContent en vez de innerHTML"""
    print(">> SOLUCION 1: Prevenir XSS usando textContent")
    print("-" * 40)
    print("function ejercicio1() {")
    print("    var input = document.getElementById('input-xss');")
    print("    var resultado = document.getElementById('resultado-ej1');")
    print("    var texto = input.value;")
    print("    resultado.textContent = 'Contenido: ' + texto;")
    print("}")
    print()
    print("Abre soluciones.html en el navegador para verlo en accion.")
    print("Con textContent, <script> se muestra como texto, no se ejecuta.")

def solucion_2():
    """Sanitizar entrada de URL"""
    print(">> SOLUCION 2: Sanitizar entrada de URL")
    print("-" * 40)
    print("function ejercicio2() {")
    print("    var url = input.value.trim();")
    print("    if ((url.startsWith('https://') || url.startsWith('http://'))")
    print("        && !url.includes('javascript:') && !url.includes('data:')) {")
    print("        resultado.innerHTML = '<a href=\"' + url + '\" target=\"_blank\">Ir a ' + url + '</a>';")
    print("        resultado.innerHTML += '<br>URL valida';")
    print("    } else {")
    print("        resultado.textContent = 'Error: URL no permitida (solo http/https)';")
    print("    }")
    print("}")

def solucion_3():
    """Simular CSRF y su prevencion con token"""
    print(">> SOLUCION 3: Simular CSRF y su prevencion con token")
    print("-" * 40)
    print("var csrfToken = '';")
    print("function generarToken() {")
    print("    csrfToken = Math.random().toString(36).substring(2, 15);")
    print("    document.getElementById('csrf-token-input').value = csrfToken;")
    print("}")
    print("function ejercicio3() {")
    print("    var monto = document.getElementById('monto').value;")
    print("    var cuenta = document.getElementById('cuenta').value;")
    print("    var tokenInput = document.getElementById('csrf-token-input').value;")
    print("    if (tokenInput === csrfToken && csrfToken !== '') {")
    print("        resultado.textContent = 'Transferencia de $' + monto + ' a cuenta ' + cuenta + ' exitosa';")
    print("        resultado.style.background = '#d4edda';")
    print("    } else {")
    print("        resultado.textContent = 'Error: CSRF detected - token invalido';")
    print("        resultado.style.background = '#f8d7da';")
    print("    }")
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
