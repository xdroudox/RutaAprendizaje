# Middleware y Filtros

El middleware es software que actua como intermediario entre una peticion
entrante y el manejador final de la aplicacion. Se ejecuta en orden secuencial
formando un pipeline.

## Concepto

```
Peticion -> Middleware1 -> Middleware2 -> ... -> Manejador -> Respuesta
                                        |
                                    Middleware3 (despues)
```

Cada middleware puede:
- Ejecutar codigo antes de pasar la peticion al siguiente
- Modificar la peticion o la respuesta
- Detener el pipeline (por ejemplo, si no hay autenticacion)
- Ejecutar codigo despues de que se genere la respuesta

## Middleware de Logging

```python
import time

def logging_middleware(peticion):
    inicio = time.time()
    print(f"[{time.ctime()}] {peticion['metodo']} {peticion['ruta']}")
    # Pasar al siguiente
    respuesta = {"status": 200, "body": "OK"}
    duracion = time.time() - inicio
    print(f"[{time.ctime()}] Completado en {duracion:.3f}s")
    return respuesta
```

## Middleware de Autenticacion

```python
def auth_middleware(peticion):
    if "Authorization" not in peticion["headers"]:
        return {"status": 401, "body": "No autorizado"}
    token = peticion["headers"]["Authorization"]
    if not token.startswith("Bearer "):
        return {"status": 401, "body": "Token invalido"}
    return None  # Continua al siguiente middleware
```

## Middleware CORS

```python
def cors_middleware(respuesta):
    respuesta["headers"]["Access-Control-Allow-Origin"] = "*"
    respuesta["headers"]["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE"
    return respuesta
```

## Pipeline completo

```python
def procesar_peticion(peticion):
    # Pipeline de middlewares
    for middleware in [auth_middleware, logging_middleware]:
        resultado = middleware(peticion)
        if resultado:  # middleware detuvo el pipeline
            return resultado
    # Manejador final
    return {"status": 200, "body": "Recurso servido"}
```

## Tipos de middleware comun

- Logging: registrar peticiones y tiempos
- Autenticacion: verificar tokens
- CORS: permitir origenes cruzados
- Compresion: comprimir respuestas
- Rate limiting: limitar peticiones por IP
- Body parsing: analizar cuerpos JSON/XML

Ejecuta: python ejercicios.py 1
