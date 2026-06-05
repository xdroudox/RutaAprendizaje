# Nivel 5: Backend y APIs

Aprende los fundamentos de comunicacion cliente-servidor, protocolo HTTP, formatos de datos, autenticacion y diseno de APIs REST.

## Modulos

1. **Protocolo HTTP** - Metodos GET/POST/PUT/DELETE, cabeceras, estructura request/response, URL
2. **HTTP Status Codes** - Familias 1xx-5xx y codigos mas comunes
3. **JSON y XML** - Serializacion json.dumps/loads, lectura de archivos
4. **REST APIs** - Principios REST, CRUD a HTTP, idempotencia
5. **JWT y Autenticacion** - Estructura header.payload.firma, generacion y verificacion
6. **OAuth2** - Flujos Authorization Code y Client Credentials, roles
7. **Sockets y Redes** - TCP/IP, socket cliente/servidor, echo server
8. **Middleware y Filtros** - Pipeline de middlewares, logging, autenticacion
9. **API Testing y Documentacion** - http.client, validacion, OpenAPI

## Como usar

Cada modulo contiene `ejercicios.py`, `soluciones.py` y `README.md`.

Ejecutar un ejercicio desde la raiz del proyecto:

    python scripts/runner.py 5 [modulo] [ejercicio]

Ejemplos:
    python scripts/runner.py 5 1    -> Lista ejercicios del modulo 1
    python scripts/runner.py 5 1 1  -> Ejecuta ejercicio 1 del modulo 1
    python scripts/runner.py 5 1 1 -s -> Ver solucion
