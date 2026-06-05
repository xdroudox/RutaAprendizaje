# HTTP Status Codes

Los codigos de estado HTTP indican el resultado de una peticion.

## Familias
- **1xx (Informativos):** 100 Continue, 101 Switching Protocols
- **2xx (Exito):** 200 OK, 201 Created, 204 No Content
- **3xx (Redireccion):** 301 Moved Permanently, 302 Found, 304 Not Modified
- **4xx (Error cliente):** 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 409 Conflict
- **5xx (Error servidor):** 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable

## Ejercicios

1. **Clasificar codigos en familias** - Dado un codigo, identificar su familia (1xx, 2xx, 3xx, 4xx, 5xx).
   **Ejecuta:** `python scripts/runner.py 5 2 1`

2. **Elegir status code correcto** - Dado un escenario, seleccionar el codigo HTTP apropiado.
   **Ejecuta:** `python scripts/runner.py 5 2 2`

3. **Manejar errores HTTP** - Usar if/elif para actuar segun el codigo de estado.
   **Ejecuta:** `python scripts/runner.py 5 2 3`
