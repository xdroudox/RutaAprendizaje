# Pruebas de API

## Que son las pruebas de API

Las pruebas de API verifican que los endpoints HTTP funcionen correctamente: envian la respuesta esperada, manejan errores adecuadamente y cumplen con el contrato definido.

## La libreria requests

Para hacer peticiones HTTP en Python se usa la libreria `requests`:

```
pip install requests
```

Peticiones basicas:

```python
import requests

respuesta = requests.get("https://api.ejemplo.com/usuarios")
respuesta = requests.post("https://api.ejemplo.com/usuarios", json={"nombre": "Ana"})
respuesta = requests.put("https://api.ejemplo.com/usuarios/1", json={"nombre": "Ana"})
respuesta = requests.delete("https://api.ejemplo.com/usuarios/1")
```

## Codigos de estado HTTP

- 200 OK: Peticion exitosa (GET)
- 201 Created: Recurso creado (POST)
- 204 No Content: Exitoso sin contenido (DELETE)
- 400 Bad Request: Error del cliente
- 401 Unauthorized: No autenticado
- 404 Not Found: Recurso no encontrado
- 500 Internal Server Error: Error del servidor

## Validacion de respuestas

```python
respuesta = requests.get("https://api.ejemplo.com/usuarios/1")

# Verificar codigo de estado
assert respuesta.status_code == 200

# Verificar contenido JSON
datos = respuesta.json()
assert datos["id"] == 1
assert datos["nombre"] == "Ana"

# Verificar cabeceras
assert "application/json" in respuesta.headers["Content-Type"]
```

## Probar contra httpbin.org

httpbin.org es un servicio gratuito para probar peticiones HTTP:

```python
# GET
respuesta = requests.get("https://httpbin.org/get")
print(respuesta.json())

# POST
respuesta = requests.post("https://httpbin.org/post", data={"clave": "valor"})
print(respuesta.json())

# Codigos de estado
respuesta = requests.get("https://httpbin.org/status/404")
print(respuesta.status_code)  # 404
```

## Estructura de una prueba de API

```python
import requests

def test_obtener_usuario():
    respuesta = requests.get("https://httpbin.org/get")
    assert respuesta.status_code == 200
    datos = respuesta.json()
    assert "url" in datos
    assert datos["url"] == "https://httpbin.org/get"
```
