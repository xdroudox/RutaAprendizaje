"""
SOLUCIONES - Seguridad Web
Ejecuta desde raiz: python scripts/runner.py 10 06 [ejercicio] solucion
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    """Simula SQL injection: concatenar string vs usar parametros"""
    import sqlite3
    print(">> SQL INJECTION - Version VULNERABLE:")
    print()
    usuario = "admin' OR '1'='1"
    query_vulnerable = f"SELECT * FROM usuarios WHERE nombre = '{usuario}'"
    print(f"  Input: {usuario}")
    print(f"  Query: {query_vulnerable}")
    print("  Problema: el atacante inyecta SQL para evitar la autenticacion.")
    print()
    print(">> Version SEGURA (parametrizada):")
    query_segura = "SELECT * FROM usuarios WHERE nombre = ?"
    print(f"  Query: {query_segura}")
    print("  Los datos se pasan por separado, nunca se concatenan.")

def solucion_2():
    """Escapa HTML para prevenir XSS"""
    import html
    entrada = '<script>alert("xss")</script>'
    sanitizado = html.escape(entrada)
    print(f"Entrada original: {entrada}")
    print(f"Sanitizado:       {sanitizado}")
    print()
    print("html.escape() convierte < > & \" ' en entidades HTML")
    print("evitando que el navegador los interprete como codigo.")

def solucion_3():
    """Verifica headers de seguridad en una respuesta simulada"""
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
    print("Headers de la respuesta:")
    for clave, valor in headers.items():
        print(f"  {clave}: {valor}")
    print()
    for h in headers_requeridos:
        if h not in headers:
            print(f"ADVERTENCIA: Falta el header '{h}'")
    if "Content-Security-Policy" not in headers:
        print("  Recomendacion: Content-Security-Policy: default-src 'self'")

if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            print(f">> SOLUCION {num + 1}: {soluciones[num].__doc__}")
            print("-" * 40)
            soluciones[num]()
    else:
        for i, sol in enumerate(soluciones, 1):
            print(f"  {i}. {sol.__doc__}")
