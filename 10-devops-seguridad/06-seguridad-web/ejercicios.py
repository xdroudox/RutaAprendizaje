"""
EJERCICIOS - Seguridad Web
Ejecuta desde raiz: python scripts/runner.py 10 06 [ejercicio] [-p N]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1(pista=0):
    """Simular SQL injection: concatenacion vs consulta parametrizada"""
    print(">> EJERCICIO 1: Simular SQL injection")
    print("-" * 40)
    print("Simulamos una consulta SQL a una base de datos de usuarios.")
    print("El atacante ingresa: admin' OR '1'='1")
    print()
    usuario_malicioso = "admin' OR '1'='1"
    print("Instrucciones:")
    print("  1. Crea una query vulnerable concatenando el input del usuario")
    print("  2. Crea una query segura usando ? como placeholder")
    print("  3. Imprime ambas para ver la diferencia")
    print()
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")
    print("query_vulnerable = f\"SELECT * FROM usuarios WHERE nombre = '{...}'\"")
    print("query_segura = 'SELECT * FROM usuarios WHERE nombre = ?'")
    if pista:
        print("\n" + "=" * 40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  La query vulnerable usa f-strings para insertar el input directamente.")
        print("  La query segura usa ? y nunca concatena el input.")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  query_vulnerable = f\"SELECT * FROM usuarios WHERE nombre = '{usuario_malicioso}'\"")
        print("  query_segura = 'SELECT * FROM usuarios WHERE nombre = ?'")
        print("  print(f'Vulnerable: {query_vulnerable}')")
        print("  print(f'Segura:     {query_segura}')")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  usuario_malicioso = \"admin' OR '1'='1\"")
        print("  query_vulnerable = f\"SELECT * FROM usuarios WHERE nombre = '{usuario_malicioso}'\"")
        print("  query_segura = 'SELECT * FROM usuarios WHERE nombre = ?'")
        print("  print('=== Version VULNERABLE ===')")
        print("  print(f'Input: {usuario_malicioso}')")
        print("  print(f'Query: {query_vulnerable}')")
        print("  print('*** Esta query retorna TODOS los usuarios! ***')")
        print("  print()")
        print("  print('=== Version SEGURA (parametrizada) ===')")
        print("  print(f'Query: {query_segura}')")
        print("  print('Los datos se pasan por separado, nunca se concatenan.')")


def ejercicio_2(pista=0):
    """Escapar HTML con html.escape() para prevenir XSS"""
    import html
    print(">> EJERCICIO 2: Prevenir XSS escapando HTML")
    print("-" * 40)
    entrada_usuario = '<script>alert("xss")</script>'
    print("Un usuario malicioso ingresa un comentario con codigo JavaScript.")
    print(f"Entrada: {entrada_usuario}")
    print()
    print("Instrucciones:")
    print("  1. Usa html.escape() para sanitizar la entrada")
    print("  2. Imprime el resultado sanitizado")
    print()
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")
    print("sanitizado = html.escape(...)")
    if pista:
        print("\n" + "=" * 40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  html.escape() convierte < > & \" ' en entidades HTML.")
        print("  < se convierte en &lt;")
        print("  > se convierte en &gt;")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  entrada = '<script>alert(\"xss\")</script>'")
        print("  sanitizado = html.escape(entrada)")
        print("  print(f'Original:   {entrada}')")
        print("  print(f'Sanitizado: {sanitizado}')")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  entrada_usuario = '<script>alert(\"xss\")</script>'")
        print("  sanitizado = html.escape(entrada_usuario)")
        print("  print(f'Original:   {entrada_usuario}')")
        print("  print(f'Sanitizado: {sanitizado}')")
        print("  print()")
        print("  print('El navegador muestra el texto sin ejecutar el script.')")


def ejercicio_3(pista=0):
    """Verificar headers de seguridad en una respuesta simulada"""
    print(">> EJERCICIO 3: Verificar headers de seguridad")
    print("-" * 40)
    headers_respuesta = {
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
    print("Headers actuales de la respuesta:")
    for clave, valor in headers_respuesta.items():
        print(f"  {clave}: {valor}")
    print()
    print("Instrucciones:")
    print("  1. Revisa si cada header requerido esta presente en headers_respuesta")
    print("  2. Si falta, imprime una advertencia")
    print()
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")
    print("for header in headers_requeridos:")
    print("    if header not in ...:")
    if pista:
        print("\n" + "=" * 40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  Usa 'in' para verificar si una clave existe en un diccionario.")
        print("  Ejemplo: if 'X-Frame-Options' in headers_respuesta:")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  for h in headers_requeridos:")
        print("      if h in headers_respuesta:")
        print("          print(f'[OK] {h} presente')")
        print("      else:")
        print("          print(f'[FALTA] {h}')")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  headers_requeridos = [")
        print("      'Content-Security-Policy',")
        print("      'X-Frame-Options',")
        print("      'X-Content-Type-Options',")
        print("      'Strict-Transport-Security',")
        print("  ]")
        print("  for h in headers_requeridos:")
        print("      if h in headers_respuesta:")
        print("          print(f'  [OK] {h}: {headers_respuesta[h]}')")
        print("      else:")
        print("          print(f'  [FALTA] {h} - Recomendado agregarlo')")
        print("  if 'Content-Security-Policy' not in headers_respuesta:")
        print('      print("Sugerencia: Content-Security-Policy: default-src \'self\'")')


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
