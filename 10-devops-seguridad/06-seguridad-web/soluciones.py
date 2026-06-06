"""
SOLUCIONES - Seguridad Web
Ejecuta desde raiz: python scripts/runner.py 10 06 [ejercicio] -s
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    """Simular SQL injection: concatenacion vs consulta parametrizada"""
    usuario_malicioso = "admin' OR '1'='1"
    query_vulnerable = f"SELECT * FROM usuarios WHERE nombre = '{usuario_malicioso}'"
    query_segura = "SELECT * FROM usuarios WHERE nombre = ?"
    assert "OR '1'='1'" in query_vulnerable
    assert "?" in query_segura
    print(">> SOLUCION 1: Simular SQL injection")
    print("-" * 40)
    print("=== Version VULNERABLE ===")
    print(f"Input del atacante: {usuario_malicioso}")
    print(f"Query generada:     {query_vulnerable}")
    print()
    print("Problema: la condicion OR '1'='1' siempre es verdadera,")
    print("por lo que la consulta retorna TODOS los usuarios de la tabla.")
    print("El atacante evade la autenticacion sin conocer la contrasena.")
    print()
    print("=== Version SEGURA (parametrizada) ===")
    print(f"Query: {query_segura}")
    print("Los datos se pasan por separado como parametros.")
    print("El SQL y los datos nunca se mezclan, haciendo imposible la inyeccion.")
    print()
    print("Ejemplo con sqlite3:")
    print("  cursor.execute('SELECT * FROM usuarios WHERE nombre = ?', (usuario,))")


def solucion_2():
    """Escapar HTML con html.escape() para prevenir XSS"""
    import html
    entrada = '<script>alert("xss")</script>'
    sanitizado = html.escape(entrada)
    assert "<" not in sanitizado
    assert "&lt;" in sanitizado
    print(">> SOLUCION 2: Prevenir XSS escapando HTML")
    print("-" * 40)
    print("import html")
    print(f"entrada = '{entrada}'")
    print("sanitizado = html.escape(entrada)")
    print()
    print(f"Original:   {entrada}")
    print(f"Sanitizado: {sanitizado}")
    print()
    print("Explicacion:")
    print("  html.escape() convierte caracteres especiales en entidades HTML:")
    print("    <  ->  &lt;")
    print("    >  ->  &gt;")
    print("    \"  ->  &#x27;")
    print("    &  ->  &amp;")
    print("  El navegador muestra el texto como caracteres seguros,")
    print("  sin interpretarlos como codigo JavaScript.")
    print("  Esto previene ataques XSS (Cross-Site Scripting).")


def solucion_3():
    """Verificar headers de seguridad en una respuesta simulada"""
    headers = {
        "Content-Type": "text/html",
        "X-Frame-Options": "DENY",
        "X-Content-Type-Options": "nosniff",
    }
    headers_requeridos = [
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Strict-Transport-Security",
    ]
    faltantes = [h for h in headers_requeridos if h not in headers]
    assert "Content-Security-Policy" in faltantes
    print(">> SOLUCION 3: Verificar headers de seguridad")
    print("-" * 40)
    print("Headers de la respuesta:")
    for clave, valor in headers.items():
        print(f"  {clave}: {valor}")
    print()
    print("Verificando headers requeridos...")
    for h in headers_requeridos:
        if h in headers:
            print(f"  [OK] {h}: {headers[h]}")
        else:
            print(f"  [FALTA] {h}")
    print()
    print("Explicacion:")
    print("  Content-Security-Policy: restringe que recursos puede cargar el navegador.")
    print("  X-Frame-Options: evita clickjacking al impedir iframes.")
    print("  X-Content-Type-Options: evita MIME sniffing.")
    print("  Strict-Transport-Security: fuerza conexiones HTTPS.")
    print()
    print("Los headers faltantes se deben agregar en la configuracion del servidor web.")


if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
    else:
        for i, sol in enumerate(soluciones, 1):
            print(f"  {i}. {sol.__doc__}")
