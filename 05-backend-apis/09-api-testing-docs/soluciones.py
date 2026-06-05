import sys
import http.client
import json

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    print("=" * 50)
    print("SOLUCION 1: Test GET con http.client")
    print("=" * 50)
    conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
    conn.request("GET", "/posts")
    resp = conn.getresponse()
    data = json.loads(resp.read().decode())
    print(f"Codigo de estado: {resp.status} {resp.reason}")
    print(f"Cantidad de posts recibidos: {len(data)}")
    print()
    print("Primer post:")
    print(json.dumps(data[0], indent=2))
    conn.close()

def solucion_2():
    print("=" * 50)
    print("SOLUCION 2: Test POST para crear recurso")
    print("=" * 50)
    conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
    payload = json.dumps({
        "title": "Mi post",
        "body": "Contenido del post",
        "userId": 1
    })
    conn.request("POST", "/posts", body=payload, headers={"Content-Type": "application/json"})
    resp = conn.getresponse()
    data = json.loads(resp.read().decode())
    print(f"Codigo de estado: {resp.status} {resp.reason}")
    print(f"ID del post creado: {data['id']}")
    print()
    print("Respuesta completa:")
    print(json.dumps(data, indent=2))
    conn.close()

def solucion_3():
    print("=" * 50)
    print("SOLUCION 3: Documentar un endpoint en OpenAPI")
    print("=" * 50)
    spec = """
openapi: 3.0.0
info:
  title: API de Productos
  version: 1.0.0
paths:
  /productos/{id}:
    get:
      summary: Obtiene un producto por su ID
      parameters:
        - name: id
          in: path
          required: true
          description: ID del producto
          schema:
            type: integer
      responses:
        '200':
          description: Producto encontrado
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
                  nombre:
                    type: string
                  precio:
                    type: number
        '404':
          description: Producto no encontrado
"""
    print(spec)

def menu():
    print("SOLUCIONES - API TESTING Y DOCS")
    print("1 - Test GET con http.client")
    print("2 - Test POST para crear recurso")
    print("3 - Documentar un endpoint en OpenAPI")

def main():
    args = sys.argv[1:]
    if not args:
        menu()
        return
    num = args[0]
    if num == "1":
        solucion_1()
    elif num == "2":
        solucion_2()
    elif num == "3":
        solucion_3()
    else:
        print("Solucion no valida. Usa 1, 2 o 3.")

if __name__ == "__main__":
    main()
