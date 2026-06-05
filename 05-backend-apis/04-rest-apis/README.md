# REST APIs

REST (Representational State Transfer) es un estilo arquitectonico para
disenar APIs web. Se basa en recursos identificados por URLs y operaciones
definidas por metodos HTTP.

## Principios REST

1. **Recursos**: Todo es un recurso (usuarios, productos, pedidos)
2. **URLs descriptivas**: /api/usuarios, /api/productos/123
3. **Metodos HTTP**: GET, POST, PUT, PATCH, DELETE
4. **Sin estado (stateless)**: Cada peticion contiene toda la informacion
5. **Formato multiple**: JSON, XML, etc.

## Mapeo CRUD a HTTP

| Operacion | SQL | HTTP | URL |
|-----------|-----|------|-----|
| Create | INSERT | POST | /api/usuarios |
| Read | SELECT | GET | /api/usuarios/1 |
| Update (completo) | UPDATE | PUT | /api/usuarios/1 |
| Update (parcial) | UPDATE | PATCH | /api/usuarios/1 |
| Delete | DELETE | DELETE | /api/usuarios/1 |
| Listar | SELECT | GET | /api/usuarios |

## Nombrado de recursos

- Plural: /usuarios, /productos
- Anidado: /usuarios/1/pedidos
- Sin verbos: NO /getUsuarios, /createUser
- Consistente: siempre plural

## Idempotencia

Una operacion es idempotente si ejecutarla varias veces produce el mismo
resultado que ejecutarla una vez.

- GET: idempotente
- PUT: idempotente (mismo recurso actualizado varias veces = mismo estado)
- DELETE: idempotente (borrar algo ya borrado no cambia el estado)
- POST: NO idempotente (crea un nuevo recurso cada vez)

## Stateless

Cada peticion del cliente al servidor debe contener toda la informacion
necesaria para entender y procesar la peticion. El servidor no almacena
estado del cliente entre peticiones.

```python
# Simulacion de endpoints REST
endpoints = {
    "GET /api/usuarios": "Listar todos los usuarios",
    "GET /api/usuarios/1": "Obtener usuario con id=1",
    "POST /api/usuarios": "Crear nuevo usuario (cuerpo: JSON)",
    "PUT /api/usuarios/1": "Actualizar usuario completo",
    "PATCH /api/usuarios/1": "Actualizar parcialmente usuario",
    "DELETE /api/usuarios/1": "Eliminar usuario"
}
```

Ejecuta: python ejercicios.py 1
