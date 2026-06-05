# HTTP Status Codes

Los codigos de estado HTTP indican el resultado de una peticion. Se agrupan
en 5 familias.

## Familia 1xx: Informativos

| Codigo | Significado |
|--------|-------------|
| 100    | Continue |
| 101    | Switching Protocols |

## Familia 2xx: Exito

| Codigo | Significado | Ejemplo |
|--------|-------------|---------|
| 200    | OK | GET exitoso |
| 201    | Created | POST que crea un recurso |
| 204    | No Content | DELETE exitoso sin cuerpo |

## Familia 3xx: Redireccion

| Codigo | Significado | Ejemplo |
|--------|-------------|---------|
| 301    | Moved Permanently | URL cambio permanente |
| 302    | Found (redireccion temporal) | Mantenimiento |
| 304    | Not Modified | Cache valida |

## Familia 4xx: Errores del cliente

| Codigo | Significado | Ejemplo |
|--------|-------------|---------|
| 400    | Bad Request | JSON mal formado |
| 401    | Unauthorized | Falta token |
| 403    | Forbidden | Sin permisos |
| 404    | Not Found | Recurso inexistente |
| 405    | Method Not Allowed | POST en ruta solo GET |
| 409    | Conflict | Duplicado |
| 429    | Too Many Requests | Rate limit excedido |

## Familia 5xx: Errores del servidor

| Codigo | Significado | Ejemplo |
|--------|-------------|---------|
| 500    | Internal Server Error | Error inesperado |
| 502    | Bad Gateway | Proxy recibe respuesta invalida |
| 503    | Service Unavailable | Servidor saturado |
| 504    | Gateway Timeout | Proxy timeout |

## Como elegir el codigo correcto

- GET exitoso -> 200
- POST que crea -> 201
- DELETE exitoso -> 204 (sin cuerpo)
- Datos invalidos -> 400
- No autenticado -> 401
- No autorizado -> 403
- Recurso no existe -> 404
- Error del servidor -> 500

```python
import http.client

conn = http.client.HTTPSConnection("httpbin.org")
conn.request("GET", "/status/404")
resp = conn.getresponse()
print(f"Estado: {resp.status} {resp.reason}")
conn.close()
```

Ejecuta: python ejercicios.py 1
