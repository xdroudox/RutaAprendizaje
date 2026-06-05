# API Testing y Documentacion

## curl

Curl es una herramienta de linea de comandos para hacer peticiones HTTP.

```bash
curl https://jsonplaceholder.typicode.com/posts/1
curl -X POST https://jsonplaceholder.typicode.com/posts \
  -H "Content-Type: application/json" \
  -d '{"title": "foo", "body": "bar", "userId": 1}'
```

## http.client (Python)

```python
import http.client, json

conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")

# GET
conn.request("GET", "/posts/1")
resp = conn.getresponse()
print(resp.status, json.loads(resp.read()))

# POST
payload = json.dumps({"title": "foo", "body": "bar", "userId": 1})
conn.request("POST", "/posts", body=payload, headers={"Content-Type": "application/json"})
resp = conn.getresponse()
print(resp.status, json.loads(resp.read()))

conn.close()
```

## Postman

Postman es una GUI para probar APIs. Permite:
- Crear colecciones de peticiones
- Guardar variables de entorno
- Escribir tests automatizados
- Generar documentacion
- Compartir colecciones con el equipo

## Swagger / OpenAPI

OpenAPI es un estandar para documentar APIs REST. Se escribe en YAML o JSON.

```yaml
openapi: 3.0.0
info:
  title: API de Usuarios
  version: 1.0.0
paths:
  /usuarios:
    get:
      summary: Lista todos los usuarios
      responses:
        '200':
          description: Lista de usuarios
          content:
            application/json:
              schema:
                type: array
    post:
      summary: Crea un nuevo usuario
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                nombre:
                  type: string
                email:
                  type: string
```

## Buenas practicas de testing

1. Probar todos los codigos de estado (200, 201, 400, 401, 404, 500)
2. Probar casos borde (datos vacios, IDs inexistentes)
3. Probar autenticacion (con y sin token)
4. Validar estructura de la respuesta
5. Automatizar tests cuando sea posible

Ejecuta: python ejercicios.py 1
