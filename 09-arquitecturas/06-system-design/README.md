# 06 - System Design: Cache, CDN, Balanceo, CAP, Rate Limiting

## Concepto

System Design abarca el diseno de sistemas a gran escala, considerando requisitos no funcionales como rendimiento, escalabilidad, disponibilidad y tolerancia a fallos. Este modulo cubre los componentes fundamentales para construir sistemas distribuidos robustos.

Componentes clave:

- **Cache (Redis/Memcached)**: Almacenamiento temporal en memoria para reducir latencia y carga en BD.
- **CDN (Content Delivery Network)**: Red de servidores distribuidos geograficamente para servir contenido estatico cerca del usuario.
- **Load Balancer**: Distribuye el trafico entre multiples servidores para evitar sobrecarga.
- **CAP Theorem**: Consistencia, Disponibilidad, Tolerancia a Particion - solo dos de tres.
- **Rate Limiting**: Controla la cantidad de requests que un cliente puede hacer en un periodo de tiempo.

## Diagrama (ASCII)

```
Arquitectura tipica a gran escala:

                         +-----------+
                         |   CDN     |  -> Contenido estatico (imagenes, CSS, JS)
                         +-----+-----+
                               |
+-----------+          +------v------+          +--------------+
|  Usuarios  +---------> Load        +--------->  Servidores   |
|  (Global)  |         | Balancer    |          |  Web (Nginx) |
+-----------+          +------+------+          +------+-------+
                               |                        |
                               |                 +------v-------+
                               |                 |  Cache Redis |
                               |                 +------+-------+
                               |                        |
                               |                 +------v-------+
                               |                 |  Base de     |
                               +----------------->  Datos (BD)  |
                                                  +--------------+

Teorema CAP:
                    +------------------+
                    |   Consistency    |
                    +--------+---------+
                            / \
                           /   \
                          /     \
                         /       \
          +-------------+         +-------------+
          |   CA         |         |    CP        |
          |  (Relacional)|         |  (ZooKeeper) |
          +------+-------+         +------+--------+
                 |                        |
                 |                        |
          +------v-------+         +------v--------+
          |   AP          |         |     ...       |
          |  (Dynamo,     |         |               |
          |   Cassandra)  |         |               |
          +------+--------+         +---------------+
                 |
        Availability
```

## Ejemplo

Un sistema de video bajo demanda (Netflix-style):

- **CDN**: Videos e imagenes cacheados en nodos edge cercanos al usuario.
- **Cache Redis**: Catalogo de peliculas populares, sesiones de usuario, recomendaciones.
- **Load Balancer**: Distribuye peticiones a cientos de microservicios.
- **CAP**: El sistema elige AP (Availability + Partition Tolerance) para la experiencia del usuario; la consistencia eventual es aceptable.
- **Rate Limiting**: 100 requests/min por usuario en la API de busqueda.

## Ventajas / Desventajas

| Componente | Ventajas | Desventajas |
|------------|----------|-------------|
| Cache (Redis) | Latencia < 1ms, descarga BD | Datos stale, memoria limitada |
| CDN | Baja latencia global, protege origen | Costo, no sirve contenido dinamico |
| Load Balancer | Alta disponibilidad, escalabilidad | Punto unico de falla (si no es HA) |
| CAP choices | Flexibilidad segun caso de uso | Sacrificio de una propiedad |
| Rate Limiting | Protege contra abusos y DDoS | Complejidad, falsos positivos |

## Ejercicios

### Ejercicio 1: Cache strategy
Disena una estrategia de cache para un sistema de catalogo de productos con las siguientes caracteristicas: 1M productos, 10K req/s de lectura, 100 req/s de escritura (actualizacion de precios/stock). Decide:
- Que datos cachear y con que TTL?
- Politica de invalidacion (write-through, write-around, write-back)?
- Estructura de datos en Redis (String, Hash, Sorted Set)?

> Respuesta:

### Ejercicio 2: Teorema CAP en accion
Para cada uno de los siguientes sistemas, identifica que dos propiedades del teorema CAP prioriza y cual sacrifica, justificando:

a) Sistema bancario de transferencias internacionales.
b) Red social que muestra publicaciones de amigos (feed).
c) DNS (Domain Name System).
d) Base de datos de configuracion de orquestador (Kubernetes etcd).
e) Carrito de compras de un e-commerce.

> Respuesta:

### Ejercicio 3: Disenar rate limiting
Disena un rate limiter para una API publica de clima que tiene los siguientes limites:
- Usuarios gratuitos: 10 req/min
- Usuarios premium: 1000 req/min
- La API tiene picos de trafico los fines de semana

Escoge entre: Token Bucket, Leaky Bucket, Fixed Window, Sliding Window. Explica tu eleccion y describe la implementacion con Redis.

> Respuesta:

## Soluciones

<details>
<summary>Solucion 1</summary>

**Que cachear y TTL:**
- Productos mas vistos (top 20%): Redis Hash con TTL de 5 minutos.
- Precios y stock: TTL corto de 30 segundos (datos volatiles).
- Categorias y filtros: TTL de 1 hora (cambian poco).
- Busquedas recientes: TTL de 10 minutos.

**Politica de invalidacion:**
- **Write-through**: Al actualizar precio/stock, se escribe primero en cache y luego en BD. Garantiza consistencia pero aumenta latencia de escritura. Adecuado para datos criticos como stock.
- **Write-around**: Para categorias y filtros, se escribe directo en BD y el cache se invalida. Proximo request populara el cache.
- **Write-back**: No recomendado por riesgo de perder datos de precio/stock.

**Estructura en Redis:**
- Producto individual: `HSET product:123 name "Laptop" price 999 stock 50`
- Catalogo paginado: `SORTED SET catalog:electronics` con score = precio para ordenamiento.
- Busquedas: `SET search:laptops {JSON con resultados}` con TTL.

</details>

<details>
<summary>Solucion 2</summary>

a) **Sistema bancario**: Prioriza **CP** (Consistency + Partition Tolerance). Sacrifica Availability. Una transferencia debe ser consistente (no perder dinero) aunque signifique rechazar la operacion si hay particion de red.

b) **Red social (feed)**: Prioriza **AP** (Availability + Partition Tolerance). Sacrifica Consistency. Es aceptable que el feed no muestre la publicacion mas reciente inmediatamente. Mejor mostrar algo aunque sea ligeramente desactualizado.

c) **DNS**: Prioriza **AP**. Sacrifica Consistency. DNS usa cache extensivo y replicacion. Si un servidor no responde, otro responde con datos posiblemente desactualizados.

d) **etcd (Kubernetes)**: Prioriza **CP**. Sacrifica Availability. etcd usa consenso Raft. Si hay particion, la mayoria debe estar de acuerdo. La consistencia de configuracion es critica.

e) **Carrito de compras**: Prioriza **AP**. Sacrifica Consistency. Es mejor que el usuario pueda agregar productos aunque temporalmente el carrito no este sincronizado entre dispositivos. La consistencia eventual es aceptable.

</details>

<details>
<summary>Solucion 3</summary>

**Eleccion: Sliding Window Log con Redis Sorted Sets.**

Justificacion:
- **Fixed Window**: Problema de "thundering herd" al final de la ventana.
- **Leaky Bucket**: No permite bursts (peticiones se procesan a tasa constante).
- **Token Bucket**: Permite bursts, pero es mas complejo resetear por usuario.
- **Sliding Window**: La mas precisa, evita los picos al borde de la ventana.

**Implementacion con Redis:**

```python
import time
import redis

r = redis.Redis()

def is_rate_limited(user_id: str, limit: int, window: int = 60) -> bool:
    key = f"ratelimit:{user_id}"
    now = time.time()
    window_start = now - window

    # Limpiar entradas viejas y contar las actuales
    r.zremrangebyscore(key, 0, window_start)
    count = r.zcard(key)

    if count >= limit:
        return True

    # Agregar request actual
    r.zadd(key, {str(now): now})
    r.expire(key, window)
    return False
```

**Estructura:**
- Key: `ratelimit:{user_id}`
- Value: Sorted Set con timestamps como scores y miembros.
- A cada request se limpian las entradas fuera de la ventana y se cuenta el total.

**Cacheo de la decision**: Para usuarios gratuitos, se puede cachear el bloqueo por 1 segundo para evitar llamadas multiples a Redis.
</details>
