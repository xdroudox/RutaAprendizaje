# API Testing y Documentacion

## Contenido
- Requests HTTP con http.client
- Validacion de respuestas (status code, body)
- Documentacion OpenAPI/Swagger

---

## 1. Testing de APIs

Probar APIs manualmente es tedioso y propenso a errores. La automatizacion de pruebas de API permite verificar rapidamente que los endpoints funcionan correctamente.

### Con http.client (modulo nativo)
```python
import http.client
conn = http.client.HTTPSConnection("api.ejemplo.com", timeout=5)
conn.request("GET", "/posts/1")
resp = conn.getresponse()
print(resp.status, resp.read().decode())
conn.close()
```

### Validaciones comunes
- Status code correcto (200, 201, 404, etc.)
- Body contiene los campos esperados
- Headers correctos (Content-Type, etc.)
- Tiempo de respuesta aceptable

---

## 2. Documentacion OpenAPI/Swagger

OpenAPI (antes Swagger) es un estandar para describir APIs REST en formato YAML o JSON.

### Estructura basica
```yaml
openapi: 3.0.0
info:
  title: API de Usuarios
  version: 1.0.0
paths:
  /api/usuarios:
    get:
      summary: Listar usuarios
      responses:
        '200':
          description: OK
```

### Herramientas
- **Swagger UI:** interfaz grafica interactiva
- **Swagger Editor:** editor con preview visual
- **Redoc:** documentacion en HTML

---

## 3. Glosario

| Termino         | Definicion |
|----------------|-----------|
| **http.client** | Modulo nativo de Python para hacer requests HTTP |
| **HTTPSConnection** | Conexion segura (TLS) a un servidor |
| **getresponse()** | Obtiene la respuesta del servidor |
| **Status code** | Codigo de 3 digitos que indica el resultado |
| **OpenAPI**     | Estandar para documentar APIs REST |
| **Swagger**     | Herramientas para trabajar con OpenAPI |
| **Schema**      | Definicion de la estructura de los datos |

---

## 4. Comparativa entre lenguajes

### Python (http.client)
```python
conn = http.client.HTTPSConnection("api.ejemplo.com")
conn.request("GET", "/usuarios")
resp = conn.getresponse()
datos = json.loads(resp.read())
```

### Python (requests - mas usado)
```python
import requests
resp = requests.get("https://api.ejemplo.com/usuarios", timeout=5)
datos = resp.json()
```

### JavaScript (fetch)
```javascript
const resp = await fetch("https://api.ejemplo.com/usuarios");
const datos = await resp.json();
```

### Java (RestTemplate)
```java
RestTemplate rest = new RestTemplate();
List<User> users = rest.getForObject("https://api.ejemplo.com/usuarios", List.class);
```

---

## 5. Ejemplo guiado paso a paso

**Problema:** Hacer GET a JSONPlaceholder API y validar la respuesta.

1. Conectar a `jsonplaceholder.typicode.com`
2. Request: `GET /posts/1`
3. Validar status code = 200
4. Validar que body tenga `id`, `title` y `body`
5. Mostrar los datos

```python
import http.client, json

conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com", timeout=5)
conn.request("GET", "/posts/1")
resp = conn.getresponse()

assert resp.status == 200, f"Expected 200, got {resp.status}"

datos = json.loads(resp.read())
for campo in ["id", "title", "body"]:
    print(f"  {campo}: {datos.get(campo)}")

conn.close()
```

---

## Ejercicios

| #  | Ejercicio | Dificultad |
|----|-----------|------------|
| 1  | Request GET con http.client | 🟢 |
| 2  | Validar status code y body | 🟡 |
| 3  | Documentacion OpenAPI (dict) | 🔴 |

## Comandos

```bash
python scripts/runner.py 5 9 1
python scripts/runner.py 5 9 2
python scripts/runner.py 5 9 3
python scripts/runner.py 5 9 1 -p 1
python scripts/runner.py 5 9 3 -s
```
