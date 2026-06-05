# Protocolo HTTP

HTTP (HyperText Transfer Protocol) es el protocolo de comunicacion entre
clientes (navegadores) y servidores web. Es un protocolo sin estado basado
en el modelo request-response.

## Estructura de una URL

```
esquema://dominio:puerto/ruta?query#fragmento
http://ejemplo.com:8080/api/usuarios?edad=25#seccion
```

- Esquema: http o https
- Dominio: nombre del servidor
- Puerto: 80 (http) o 443 (https) por defecto
- Ruta: recurso en el servidor
- Query: parametros clave=valor separados por &
- Fragmento: seccion interna (no viaja al servidor)

## Metodos HTTP

| Metodo | Descripcion | Idempotente |
|--------|-------------|-------------|
| GET    | Obtener recurso | Si |
| POST   | Crear recurso | No |
| PUT    | Reemplazar recurso | Si |
| DELETE | Eliminar recurso | Si |
| PATCH  | Modificar parcialmente | No |

## Estructura de Request

```
GET /api/usuarios HTTP/1.1
Host: ejemplo.com
User-Agent: Mozilla/5.0
Accept: application/json
Authorization: Bearer token123
```

Linea inicial: METODO RUTA VERSION
Headers: pares clave: valor
Cuerpo: (opcional, para POST/PUT)

## Estructura de Response

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 42
Set-Cookie: session=abc123

{"id": 1, "nombre": "Ana"}
```

Linea inicial: VERSION CODIGO MENSAJE
Headers: metadatos de la respuesta
Cuerpo: datos devueltos

## Headers comunes

- Content-Type: tipo de contenido (application/json, text/html)
- Authorization: credenciales de autenticacion
- Accept: formato que acepta el cliente
- User-Agent: identificacion del cliente
- Set-Cookie: cookie a almacenar
- Cache-Control: directivas de cache

## Metodos en accion

```python
import http.client

# GET request
conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
conn.request("GET", "/posts/1")
resp = conn.getresponse()
print(resp.status, resp.reason)
data = resp.read()
print(data.decode())
conn.close()
```

Ejecuta: python ejercicios.py 1
