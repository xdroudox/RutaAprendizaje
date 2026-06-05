# Middleware y Filtros

Middleware es software que se ejecuta entre la peticion y la respuesta del servidor, formando un pipeline de procesamiento.

## Concepto
Cada middleware recibe la request, puede procesarla, modificarla, o rechazarla, y pasa el control al siguiente middleware o al manejador final.

## Ejemplos comunes
- **Logging:** registra cada peticion
- **Autenticacion:** verifica tokens antes de procesar
- **CORS:** permite peticiones de otros origenes
- **Compresion:** comprime respuestas

## Pipeline tipico
```
Request -> Logger -> Auth -> CORS -> Handler -> Response
```

## Ejercicios

1. **Middleware de logging** - Funcion que recibe un request y lo imprime en consola.
   **Ejecuta:** `python scripts/runner.py 5 8 1`

2. **Middleware de autenticacion** - Funcion que revisa un token en los headers.
   **Ejecuta:** `python scripts/runner.py 5 8 2`

3. **Pipeline de middlewares** - Componer una lista de funciones middleware en secuencia.
   **Ejecuta:** `python scripts/runner.py 5 8 3`
