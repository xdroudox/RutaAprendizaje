import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import html

def ejercicio_1():
    print(">> SOLUCION EJERCICIO 1: SQL Injection")
    print("")
    print("Problema: concatenar el input del usuario directamente en la query")
    print("permite inyeccion SQL. Un atacante puede ingresar: \" OR 1=1; --")
    print("")
    print("Solucion con consultas parametrizadas:")
    print("")
    print("  import sqlite3")
    print("  conn = sqlite3.connect('basedatos.db')")
    print("  cursor = conn.cursor()")
    print("  usuario = input('Usuario: ')")
    print("  cursor.execute('SELECT * FROM usuarios WHERE nombre = ?', (usuario,))")
    print("  resultados = cursor.fetchall()")

def ejercicio_2():
    print(">> SOLUCION EJERCICIO 2: Sanitizar XSS")
    def sanitizar(texto):
        return html.escape(texto)
    print("")
    entrada = "<script>alert('xss')</script>"
    print(f"Entrada: {entrada}")
    print(f"Sanitizado: {sanitizar(entrada)}")

def ejercicio_3():
    print(">> SOLUCION EJERCICIO 3: Verificar CSP header")
    headers = {
        "Content-Type": "text/html",
        "X-Frame-Options": "DENY",
    }
    if "Content-Security-Policy" not in headers:
        print("ADVERTENCIA: Falta el header Content-Security-Policy")
        print("Se recomienda anadirlo para prevenir XSS:")
        print("Content-Security-Policy: default-src 'self'")
    else:
        print("Header CSP presente")

def menu():
    print("=== Seguridad Web - Soluciones ===")
    print("1. SQL Injection")
    print("2. Sanitizar XSS")
    print("3. Verificar CSP header")
    print("0. Salir")
    return input("Selecciona un ejercicio: ")

def main():
    while True:
        opcion = menu()
        if opcion == "1":
            ejercicio_1()
        elif opcion == "2":
            ejercicio_2()
        elif opcion == "3":
            ejercicio_3()
        elif opcion == "0":
            break
        else:
            print("Opcion no valida")
        input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()
