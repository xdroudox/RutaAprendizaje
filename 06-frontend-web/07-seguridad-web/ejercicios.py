"""
EJERCICIOS - Seguridad Web
Ejecuta desde raiz: python scripts/runner.py 6 7 [ejercicio] [-p N]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1(pista=0):
    """Prevenir XSS usando textContent en vez de innerHTML"""
    print(">> EJERCICIO 1: Prevenir XSS usando textContent")
    print("-" * 40)
    print("Este ejercicio es en HTML/JS.")
    print("Abre el archivo en tu navegador:")
    print("  06-frontend-web/07-seguridad-web/ejercicios.html")
    print()
    print("Corrige la funcion ejercicio1():")
    print("  - Cambia innerHTML por textContent")
    print("  - textContent no interpreta etiquetas HTML")
    print("  - Prueba con <script>alert('XSS')</script>")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  textContent asigna texto plano (no interpreta HTML).")
        print("  innerHTML interpreta y ejecuta etiquetas HTML/JS.")
        print("  En lugar de resultado.innerHTML = 'Contenido: ' + texto;")
        print("  usa resultado.textContent = 'Contenido: ' + texto;")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  function ejercicio1() {")
        print("      var input = document.getElementById('input-xss');")
        print("      var resultado = document.getElementById('resultado-ej1');")
        print("      var texto = input.value;")
        print("      resultado.textContent = 'Contenido: ' + texto;")
        print("  }")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  Con textContent, si el usuario escribe <script>alert('XSS')</script>,")
        print("  se muestra literalmente como texto. Con innerHTML se ejecutaria.")
        print("  La solucion es cambiar resultado.innerHTML por resultado.textContent.")

def ejercicio_2(pista=0):
    """Sanitizar entrada de URL"""
    print(">> EJERCICIO 2: Sanitizar entrada de URL")
    print("-" * 40)
    print("Abre: 06-frontend-web/07-seguridad-web/ejercicios.html")
    print()
    print("Valida que la URL sea segura:")
    print("  - Acepta solo http:// y https://")
    print("  - Bloquea javascript: y data:")
    print("  - Usa .startsWith() para verificar")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  Usa .startsWith('https://') y .startsWith('http://')")
        print("  para verificar que la URL comienza correctamente.")
        print("  Verifica tambien que NO contenga 'javascript:' ni 'data:'")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  var url = input.value.trim();")
        print("  if ((url.startsWith('https://') || url.startsWith('http://'))")
        print("      && !url.includes('javascript:') && !url.includes('data:')) {")
        print("      // URL valida, crear enlace")
        print("  } else {")
        print("      // URL no permitida")
        print("  }")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  function ejercicio2() {")
        print("      var url = input.value.trim();")
        print("      if ((url.startsWith('https://') || url.startsWith('http://'))")
        print("          && !url.includes('javascript:') && !url.includes('data:')) {")
        print("          resultado.innerHTML = '<a href=\"' + url + '\" target=\"_blank\">Ir a ' + url + '</a>';")
        print("          resultado.innerHTML += '<br>URL valida';")
        print("      } else {")
        print("          resultado.textContent = 'Error: URL no permitida (solo http/https)';")
        print("      }")
        print("  }")

def ejercicio_3(pista=0):
    """Simular CSRF y su prevencion con token"""
    print(">> EJERCICIO 3: Simular CSRF y su prevencion con token")
    print("-" * 40)
    print("Abre: 06-frontend-web/07-seguridad-web/ejercicios.html")
    print()
    print("Implementa proteccion CSRF:")
    print("  - Genera token aleatorio con Math.random()")
    print("  - Verifica token al enviar formulario")
    print("  - Muestra exito o error segun corresponda")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  - Math.random().toString(36).substring(2, 15) genera un token")
        print("  - Guarda el token en una variable global")
        print("  - Al enviar, compara el token guardado con el del input")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  function generarToken() {")
        print("      csrfToken = Math.random().toString(36).substring(2, 15);")
        print("      document.getElementById('csrf-token-input').value = csrfToken;")
        print("  }")
        print("  function ejercicio3() {")
        print("      var tokenInput = document.getElementById('csrf-token-input').value;")
        print("      if (tokenInput === csrfToken && csrfToken !== '') {")
        print("          // Token valido, procesar")
        print("      } else {")
        print("          // Token invalido, rechazar")
        print("      }")
        print("  }")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  var csrfToken = '';")
        print("  function generarToken() {")
        print("      csrfToken = Math.random().toString(36).substring(2, 15);")
        print("      document.getElementById('csrf-token-input').value = csrfToken;")
        print("  }")
        print("  function ejercicio3() {")
        print("      var monto = document.getElementById('monto').value;")
        print("      var cuenta = document.getElementById('cuenta').value;")
        print("      var tokenInput = document.getElementById('csrf-token-input').value;")
        print("      if (tokenInput === csrfToken && csrfToken !== '') {")
        print("          resultado.textContent = 'Transferencia de $' + monto + ' a cuenta ' + cuenta + ' exitosa';")
        print("          resultado.style.background = '#d4edda';")
        print("      } else {")
        print("          resultado.textContent = 'Error: CSRF detected - token invalido';")
        print("          resultado.style.background = '#f8d7da';")
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
