"""
EJERCICIOS - Pruebas de API
Ejecuta desde raiz: python scripts/runner.py 7 5 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Probar GET a JSONPlaceholder"""
    print("Usando la libreria requests, haz una peticion GET a:")
    print("https://jsonplaceholder.typicode.com/posts/1")
    print()
    print("Verifica:")
    print("- status_code == 200")
    print("- La respuesta contiene 'title'")
    print("- El campo 'id' es 1")
    print()
    print("import requests")
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")

def ejercicio_2():
    """Probar POST con datos JSON"""
    print("Haz una peticion POST a:")
    print("https://jsonplaceholder.typicode.com/posts")
    print()
    print("Envia JSON: {'title': 'foo', 'body': 'bar', 'userId': 1}")
    print()
    print("Verifica:")
    print("- status_code == 201")
    print("- La respuesta contiene 'id'")
    print()
    print("import requests")
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")

def ejercicio_3():
    """Validar estructura de response (status, headers, body)"""
    print("Haz GET a https://jsonplaceholder.typicode.com/users")
    print()
    print("Verifica:")
    print("- status_code == 200")
    print("- Content-Type contiene 'application/json'")
    print("- La respuesta es una lista")
    print("- Cada usuario tiene: id, name, email")
    print()
    print("import requests")
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            print(f">> EJERCICIO {num + 1}: {ejercicios[num].__doc__}")
            print("-" * 40)
            ejercicios[num]()
    else:
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
