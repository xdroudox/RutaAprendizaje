import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    print("=" * 50)
    print("EJERCICIO 1: Test GET con http.client")
    print("=" * 50)
    print()
    print("TAREA: Realiza una peticion GET a la API publica")
    print("https://jsonplaceholder.typicode.com/posts para obtener todos")
    print("los posts. Imprime el codigo de estado y la cantidad de posts")
    print("recibidos.")
    print()
    print("PISTA: conn = http.client.HTTPSConnection('jsonplaceholder.typicode.com'); conn.request('GET', '/posts'); resp = conn.getresponse(); data = json.loads(resp.read()); print(len(data))")

def ejercicio_2():
    print("=" * 50)
    print("EJERCICIO 2: Test POST para crear recurso")
    print("=" * 50)
    print()
    print("TAREA: Realiza una peticion POST a")
    print("https://jsonplaceholder.typicode.com/posts para crear un")
    print("nuevo post con los siguientes datos:")
    print()
    print('  {"title": "Mi post", "body": "Contenido del post", "userId": 1}')
    print()
    print("Imprime el codigo de estado y el ID del post creado.")
    print()
    print("PISTA: Usa json.dumps() para el body, headers={'Content-Type': 'application/json'}")

def ejercicio_3():
    print("=" * 50)
    print("EJERCICIO 3: Documentar un endpoint en OpenAPI")
    print("=" * 50)
    print()
    print("TAREA: Escribe la especificacion OpenAPI para el siguiente endpoint:")
    print()
    print("  GET /productos/{id}")
    print("  Descripcion: Obtiene un producto por su ID")
    print("  Parametro: id (integer, path, requerido)")
    print("  Respuesta 200: {id, nombre, precio}")
    print("  Respuesta 404: Producto no encontrado")
    print()
    print("Escribe la estructura YAML del path correspondiente.")
    print()
    print("PISTA: paths: /productos/{id}: get: summary: '...' parameters: - name: id in: path required: true schema: type: integer")

pistas = {
    "1": "conn = http.client.HTTPSConnection('jsonplaceholder.typicode.com'); conn.request('GET', '/posts'); resp = conn.getresponse(); data = json.loads(resp.read()); print('Status:', resp.status); print('Cantidad:', len(data)); conn.close()",
    "2": "payload = json.dumps({'title': 'Mi post', 'body': 'Contenido del post', 'userId': 1}); conn = http.client.HTTPSConnection('jsonplaceholder.typicode.com'); conn.request('POST', '/posts', body=payload, headers={'Content-Type': 'application/json'}); resp = conn.getresponse(); data = json.loads(resp.read()); print('Status:', resp.status); print('ID creado:', data['id']); conn.close()",
    "3": "paths:\n  /productos/{id}:\n    get:\n      summary: Obtiene un producto por su ID\n      parameters:\n        - name: id\n          in: path\n          required: true\n          schema:\n            type: integer\n      responses:\n        '200':\n          description: Producto encontrado\n        '404':\n          description: Producto no encontrado"
}

def menu():
    print("=" * 50)
    print("API TESTING Y DOCS - EJERCICIOS")
    print("=" * 50)
    print("1 - Test GET con http.client")
    print("2 - Test POST para crear recurso")
    print("3 - Documentar un endpoint en OpenAPI")
    print()
    print("Usa: python ejercicios.py <numero>")
    print("     python ejercicios.py <numero> -p  (pista)")

def main():
    args = sys.argv[1:]
    if not args:
        menu()
        return
    num = args[0]
    mostrar_pista = "-p" in args
    if mostrar_pista and num in pistas:
        print("=== PISTA ===")
        print(pistas[num])
        print()
    if num == "1":
        ejercicio_1()
    elif num == "2":
        ejercicio_2()
    elif num == "3":
        ejercicio_3()
    else:
        print("Ejercicio no valido. Usa 1, 2 o 3.")

if __name__ == "__main__":
    main()
