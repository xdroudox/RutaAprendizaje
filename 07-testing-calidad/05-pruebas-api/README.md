# Pruebas de API

Verificar que endpoints HTTP funcionen correctamente.

## Conceptos Basicos

- **Endpoint**: URL especifica donde un API recibe peticiones (ej: `GET /api/usuarios`).
- **Peticion HTTP**: mensaje que el cliente envia al servidor (GET, POST, PUT, DELETE).
- **Respuesta HTTP**: mensaje que el servidor devuelve (status code, headers, body).
- **JSONPlaceholder**: API falsa gratuita para hacer pruebas y prototipos.
- **Status code**: codigo numerico que indica el resultado de la peticion (200=OK, 201=Creado, 404=No encontrado).

## Glosario

| Termino | Definicion |
|---------|-----------|
| **Endpoint** | URL especifica del API (ej: `/posts/1`) |
| **Status Code** | Codigo de 3 digitos que indica el estado de la respuesta |
| **Headers** | Metadatos de la peticion/respuesta (Content-Type, Auth, etc.) |
| **Body** | Cuerpo de la respuesta en formato JSON, XML, etc. |
| **JSON** | Formato de datos ligero basado en texto (JavaScript Object Notation) |
| **requests** | Libreria Python para hacer peticiones HTTP de forma sencilla |
| **GET** | Metodo HTTP para obtener recursos |
| **POST** | Metodo HTTP para crear recursos |
| **200 OK** | Peticion exitosa |
| **201 Created** | Recurso creado exitosamente |
| **404 Not Found** | Recurso no encontrado |

## Comparativa entre Lenguajes

### Python (requests)
```python
import requests

# GET
r = requests.get('https://api.ejemplo.com/usuarios')
assert r.status_code == 200
data = r.json()

# POST
r = requests.post('https://api.ejemplo.com/usuarios',
                  json={'nombre': 'Ana', 'email': 'ana@test.com'})
assert r.status_code == 201
```

### Java (RestTemplate / HttpClient)
```java
// GET
RestTemplate rest = new RestTemplate();
ResponseEntity<String> response = rest.getForEntity(
    "https://api.ejemplo.com/usuarios", String.class);
assertEquals(200, response.getStatusCodeValue());

// POST
HttpHeaders headers = new HttpHeaders();
headers.setContentType(MediaType.APPLICATION_JSON);
HttpEntity<String> request = new HttpEntity<>(
    "{\"nombre\":\"Ana\"}", headers);
ResponseEntity<String> response = rest.postForEntity(
    "https://api.ejemplo.com/usuarios", request, String.class);
assertEquals(201, response.getStatusCodeValue());
```

### JavaScript (fetch + Jest)
```javascript
// GET
test('GET /usuarios', async () => {
    const r = await fetch('https://api.ejemplo.com/usuarios');
    expect(r.status).toBe(200);
    const data = await r.json();
});

// POST
test('POST /usuarios', async () => {
    const r = await fetch('https://api.ejemplo.com/usuarios', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nombre: 'Ana' })
    });
    expect(r.status).toBe(201);
});
```

## Libreria requests en Python

### Instalacion
```bash
pip install requests
```

### Uso basico
```python
import requests

# GET
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print(response.status_code)     # 200
print(response.headers)         # Dict con headers
print(response.json())          # Body parseado como dict

# POST
payload = {'title': 'foo', 'body': 'bar', 'userId': 1}
response = requests.post('https://jsonplaceholder.typicode.com/posts',
                        json=payload)
print(response.status_code)     # 201
print(response.json()['id'])    # ID del recurso creado
```

### Validaciones comunes
```python
def validar_respuesta(response):
    assert response.status_code == 200, f"Status code: {response.status_code}"
    assert 'application/json' in response.headers.get('Content-Type', '')
    data = response.json()
    assert isinstance(data, dict) or isinstance(data, list)
    return data
```

## Ejemplo Guiado: Probar JSONPlaceholder

Paso 1: GET a /posts/1
```python
import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
assert response.status_code == 200
data = response.json()
print(f"Post #{data['id']}: {data['title']}")
# Post #1: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
```

Paso 2: POST a /posts
```python
payload = {'title': 'Mi post', 'body': 'Contenido', 'userId': 1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload)
assert response.status_code == 201
data = response.json()
assert 'id' in data
print(f"Post creado con ID: {data['id']}")
```

Paso 3: Validar estructura de /users
```python
response = requests.get('https://jsonplaceholder.typicode.com/users')
assert response.status_code == 200
assert 'application/json' in response.headers.get('Content-Type', '')
usuarios = response.json()
assert isinstance(usuarios, list)

for u in usuarios:
    assert 'id' in u
    assert 'name' in u
    assert 'email' in u

print(f"Validados {len(usuarios)} usuarios correctamente")
```

## Referencia rapida de requests

| Metodo | Descripcion |
|--------|-------------|
| `requests.get(url)` | Peticion GET |
| `requests.post(url, json=...)` | Peticion POST con JSON |
| `requests.put(url, json=...)` | Peticion PUT |
| `requests.delete(url)` | Peticion DELETE |
| `response.status_code` | Codigo de estado |
| `response.json()` | Body parseado como JSON |
| `response.headers` | Dict con headers de respuesta |
| `response.text` | Body como texto plano |

## Ejercicios

**Ejecuta:** `python scripts/runner.py 7 5 [ejercicio] [-p N]`

1. 🟢 **Probar GET a JSONPlaceholder**
2. 🟢 **Probar POST con datos JSON**
3. 🟡 **Validar estructura de response (status, headers, body)**
