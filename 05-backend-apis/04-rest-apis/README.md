# REST APIs

REST (Representational State Transfer) es un estilo arquitectonico para disenar APIs web.

## Principios REST
- Recursos identificados por URLs (ej: `/api/usuarios`)
- Operaciones via metodos HTTP
- Stateless: cada request contiene toda la informacion necesaria
- Representaciones: JSON, XML, etc.

## CRUD a HTTP
| Operacion | HTTP  | Idempotente |
|-----------|-------|-------------|
| Crear     | POST  | No          |
| Leer      | GET   | Si          |
| Actualizar| PUT   | Si          |
| Eliminar  | DELETE| Si          |

## Ejercicios

1. **Disenar endpoints REST** - Crear endpoints para un blog (posts, comments, users).
   **Ejecuta:** `python scripts/runner.py 5 4 1`

2. **Mapear CRUD a metodos HTTP** - Asignar GET/POST/PUT/DELETE a cada operacion.
   **Ejecuta:** `python scripts/runner.py 5 4 2`

3. **Identificar endpoints idempotentes** - Determinar que endpoints son idempotentes y por que.
   **Ejecuta:** `python scripts/runner.py 5 4 3`
