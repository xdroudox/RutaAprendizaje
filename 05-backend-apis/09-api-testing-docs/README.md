# API Testing y Documentacion

Probar y documentar APIs es esencial para mantener calidad y facilitar la integracion.

## Herramientas de testing
- **http.client:** modulo nativo de Python para hacer requests
- **curl:** herramienta de linea de comandos
- **Postman:** GUI para probar APIs

## Documentacion OpenAPI/Swagger
Formato estandar YAML/JSON para describir:
- Endpoints disponibles
- Metodos HTTP
- Parametros y schemas
- Respuestas esperadas

## Ejercicios

1. **Construir request GET con http.client** - Hacer una peticion GET a una API publica.
   **Ejecuta:** `python scripts/runner.py 5 9 1`

2. **Validar status code y body** - Verificar que la respuesta tenga el formato esperado.
   **Ejecuta:** `python scripts/runner.py 5 9 2`

3. **Escribir documentacion OpenAPI** - Crear un dict con la estructura de una API.
   **Ejecuta:** `python scripts/runner.py 5 9 3`
