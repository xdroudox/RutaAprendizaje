"""
EJERCICIOS - Fetch API
Ejecuta desde raiz: python scripts/runner.py 6 6 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """GET request con fetch"""
    print(">> EJERCICIO 1: GET request con fetch")
    print("-" * 40)
    print("Este ejercicio es en HTML/JS.")
    print("Abre el archivo en tu navegador:")
    print("  06-frontend-web/06-fetch-api/ejercicios.html")
    print()
    print("Usa fetch() para obtener los primeros 5 posts de")
    print("JSONPlaceholder y muestralos en pantalla.")
    print("Endpoint: https://jsonplaceholder.typicode.com/posts")

def ejercicio_2():
    """POST request con JSON body"""
    print(">> EJERCICIO 2: POST request con JSON body")
    print("-" * 40)
    print("Abre: 06-frontend-web/06-fetch-api/ejercicios.html")
    print()
    print("Envia un POST con method, headers y body.")
    print("Incluye Content-Type: application/json")
    print("Muestra la respuesta del servidor.")

def ejercicio_3():
    """Manejar errores de fetch con catch"""
    print(">> EJERCICIO 3: Manejar errores de fetch con catch")
    print("-" * 40)
    print("Abre: 06-frontend-web/06-fetch-api/ejercicios.html")
    print()
    print("Usa async/await con try/catch.")
    print("Verifica respuesta.ok, lanza error si !ok.")
    print("Muestra mensaje de error si falla la peticion.")

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            ejercicios[num]()
    else:
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
