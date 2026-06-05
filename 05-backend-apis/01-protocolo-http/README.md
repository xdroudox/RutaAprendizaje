# Protocolo HTTP

HTTP (HyperText Transfer Protocol) es el protocolo de comunicacion entre clientes y servidores web. Usa un modelo request-response sin estado.

## Estructura de una URL
`esquema://host:puerto/ruta?query=valor#fragmento`

## Metodos HTTP
- GET: obtener recurso (idempotente)
- POST: crear recurso (no idempotente)
- PUT: reemplazar recurso (idempotente)
- DELETE: eliminar recurso (idempotente)

## Request HTTP
Linea inicial: `METODO RUTA HTTP/version`
Headers: `Clave: Valor`
Cuerpo: opcional (POST/PUT)

## Response HTTP
Linea inicial: `HTTP/version CODIGO MENSAJE`
Headers: metadatos
Cuerpo: datos

## Ejercicios

1. **Crear URL desde componentes** - Construir una URL a partir de scheme, host, path y query params.
   **Ejecuta:** `python scripts/runner.py 5 1 1`

2. **Simular request HTTP** - Crear un diccionario con method, headers y body simulando una peticion.
   **Ejecuta:** `python scripts/runner.py 5 1 2`

3. **Parsear response HTTP** - Extraer status, headers y body de un string de respuesta HTTP.
   **Ejecuta:** `python scripts/runner.py 5 1 3`
