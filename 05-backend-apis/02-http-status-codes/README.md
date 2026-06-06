# HTTP Status Codes

## Contenido
- Familias de codigos HTTP (1xx-5xx)
- Codigos mas comunes por familia
- Manejo de errores segun status code

---

## 1. Que son los Status Codes?

Cuando un servidor responde a una peticion HTTP, incluye un codigo numerico de 3 digitos que indica el resultado. El primer digito define la **familia** (categoria general).

---

## 2. Familias de codigos

| Familia | Rango   | Significado         | Ejemplos tipicos |
|---------|---------|--------------------|------------------|
| **1xx** | 100-199 | Informativo        | 100 Continue |
| **2xx** | 200-299 | Exito              | 200 OK, 201 Created, 204 No Content |
| **3xx** | 300-399 | Redireccion        | 301 Moved Permanently, 302 Found, 304 Not Modified |
| **4xx** | 400-499 | Error del cliente  | 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 409 Conflict |
| **5xx** | 500-599 | Error del servidor | 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable |

---

## 3. Codigos mas comunes

| Codigo | Nombre              | Significado |
|--------|---------------------|-------------|
| **200** | OK                  | La peticion fue exitosa |
| **201** | Created             | Recurso creado exitosamente (POST) |
| **204** | No Content          | Exito sin contenido en el body (DELETE) |
| **301** | Moved Permanently   | El recurso cambio de URL permanentemente |
| **400** | Bad Request         | La solicitud tiene un error de formato |
| **401** | Unauthorized        | Se requiere autenticacion |
| **403** | Forbidden           | No tienes permisos para acceder |
| **404** | Not Found           | El recurso no existe |
| **500** | Internal Server Error | Error interno del servidor |
| **502** | Bad Gateway         | El servidor recibio respuesta invalida de otro servidor |
| **503** | Service Unavailable | El servidor no esta disponible (mantenimiento, sobrecarga) |

---

## 4. Glosario

| Termino    | Definicion |
|-----------|-----------|
| **Status code** | Codigo numerico de 3 digitos que indica el resultado de una peticion HTTP |
| **1xx** | Informativo: la peticion se esta procesando |
| **2xx** | Exito: la peticion fue recibida y procesada correctamente |
| **3xx** | Redireccion: se requiere accion adicional para completar la peticion |
| **4xx** | Error del cliente: la peticion tiene un error (el cliente es responsable) |
| **5xx** | Error del servidor: el servidor fallo al procesar la peticion |

---

## 5. Ejemplo guiado paso a paso

**Problema:** Haces un GET a `/api/usuarios/999` y recibes status 404.

1. El cliente envia GET a `/api/usuarios/999`
2. El servidor busca el usuario con id=999 en la BD
3. No encuentra el registro
4. Responde con:
   ```
   HTTP/1.1 404 Not Found
   Content-Type: application/json
   
   {"error": "Usuario no encontrado", "codigo": 404}
   ```
5. Tu codigo debe detectar el 404 e informar al usuario

---

## Ejercicios

| #  | Ejercicio | Dificultad |
|----|-----------|------------|
| 1  | Clasificar codigos HTTP en familias | 🟢 |
| 2  | Elegir status code correcto segun escenario | 🟡 |
| 3  | Manejar errores HTTP con if/elif | 🔴 |

## Comandos

```bash
python scripts/runner.py 5 2 1
python scripts/runner.py 5 2 2
python scripts/runner.py 5 2 3
python scripts/runner.py 5 2 1 -p 1
python scripts/runner.py 5 2 3 -s
```
