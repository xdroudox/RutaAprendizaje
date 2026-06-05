"""
EJERCICIOS - Seguridad Web
Ejecuta desde raiz: python scripts/runner.py 6 7 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
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

def ejercicio_2():
    """Sanitizar entrada de URL"""
    print(">> EJERCICIO 2: Sanitizar entrada de URL")
    print("-" * 40)
    print("Abre: 06-frontend-web/07-seguridad-web/ejercicios.html")
    print()
    print("Valida que la URL sea segura:")
    print("  - Acepta solo http:// y https://")
    print("  - Bloquea javascript: y data:")
    print("  - Usa .startsWith() para verificar")

def ejercicio_3():
    """Simular CSRF y su prevencion con token"""
    print(">> EJERCICIO 3: Simular CSRF y su prevencion con token")
    print("-" * 40)
    print("Abre: 06-frontend-web/07-seguridad-web/ejercicios.html")
    print()
    print("Implementa proteccion CSRF:")
    print("  - Genera token aleatorio con Math.random()")
    print("  - Verifica token al enviar formulario")
    print("  - Muestra exito o error segun corresponda")

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            ejercicios[num]()
    else:
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
