# Nivel 5: Backend y APIs

Bienvenido al nivel de Backend y APIs. Aqui aprenderas los fundamentos de
la comunicacion cliente-servidor, protocolo HTTP, formatos de datos,
autenticacion, y diseno de APIs REST.

## Modulos

### 1. Protocolo HTTP (01-protocolo-http)
Metodos GET/POST/PUT/DELETE, cabeceras, estructura request/response,
partes de una URL.

### 2. HTTP Status Codes (02-http-status-codes)
Familias 1xx, 2xx, 3xx, 4xx, 5xx y los codigos mas comunes con ejemplos.

### 3. JSON y XML (03-json-xml)
Formato JSON, serializacion con modulo json, dict a JSON, bases de XML,
cuando usar cada uno.

### 4. REST APIs (04-rest-apis)
Principios REST, nombrado de recursos, mapeo CRUD a HTTP, idempotencia,
stateless.

### 5. JWT y Autenticacion (05-jwt-autenticacion)
Estructura JWT: header.payload.signature, como funciona, generacion y
verificacion de tokens, refresh tokens.

### 6. OAuth2 (06-oauth2)
Flujos OAuth2: authorization code, implicit, client credentials, roles:
resource owner, client, auth server.

### 7. Sockets y Redes (07-sockets-redes)
Pila TCP/IP, sockets, modelo cliente-servidor, IP/puertos, procesos vs hilos.

### 8. Middleware y Filtros (08-middleware-filtros)
Concepto de middleware, pipeline de peticiones, ejemplos de middleware de
logging/autenticacion/CORS.

### 9. API Testing y Documentacion (09-api-testing-docs)
Postman, curl, testing de endpoints, Swagger/OpenAPI, documentacion de APIs.

## Como usar

Cada modulo contiene:

- `README.md` -- Explicacion teorica del tema
- `ejercicios.py` -- Ejercicios practicos
- `soluciones.py` -- Soluciones a los ejercicios

Ejecutar un ejercicio:

    python ejercicios.py 1
    python ejercicios.py 1 -p   (con pista)
    python soluciones.py 1

## Requisitos

- Python 3.6+
- Modulos: json, http.client, socket, base64, hashlib (todos incluidos)
