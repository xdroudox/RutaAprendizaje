# 05 - CQRS (Command Query Responsibility Segregation)

## Concepto

CQRS es un patron que separa las operaciones de lectura (queries) de las operaciones de escritura (commands). En lugar de usar un unico modelo para leer y escribir, CQRS define modelos distintos y optimizados para cada proposito.

- **Command**: Cambia el estado del sistema (INSERT, UPDATE, DELETE). No retorna datos de dominio (solo confirmacion).
- **Query**: Lee el estado del sistema (SELECT). No modifica datos.

Cada modelo puede tener su propia base de datos, esquema y tecnologia. La sincronizacion entre ambos puede ser sincrona (misma BD) o asincrona (eventual consistency con Event Sourcing).

## Diagrama (ASCII)

```
SIN CQRS (modelo unico):
+------------------------------+
|          Cliente              |
+------------------------------+
         |
+---------v---------+
|  Modelo Unico     |
|  (Lectura/Escritura) |
+---------+---------+
          |
+---------v---------+
|  Base de Datos    |
+-------------------+

CON CQRS:
+------------------------------+
|          Cliente              |
+------------------------------+
    |                     |
+---v----------+   +------v------+
|   COMMAND    |   |   QUERY     |
| (CreateOrder)|   | (GetOrder)  |
+------+-------+   +------+------+
       |                  |
+------v-------+   +------v-------+
| BD Escritura |   | BD Lectura   |
| (Normalizada)|   | (Denormalizada|
+------+-------+   | + Cache)     |
       |           +--------------+
       |                  |
       +---Sincronizacion---+
          (Eventual/Sincrona)
```

## Cuando usar CQRS

**Usar CQRS cuando:**
- La aplicacion tiene alta disparidad entre lecturas y escrituras (muchas lecturas, pocas escrituras o viceversa).
- Los modelos de lectura y escritura son muy diferentes (lectura con joins complejos, escritura con validaciones de negocio).
- Se necesita escalar lecturas y escrituras independientemente.
- Se combina con Event Sourcing (los comandos generan eventos, las queries proyectan el estado).

**NO usar CQRS cuando:**
- CRUD simple sin logica de negocio compleja.
- El equipo es pequeno o la complejidad adicional no se justifica.
- Se requiere consistencia inmediata entre lectura y escritura.
- El volumen de datos es bajo.

## Ventajas / Desventajas

| Ventajas | Desventajas |
|----------|-------------|
| Optimizacion independiente de lecturas y escrituras | Complejidad adicional en el sistema |
| Modelos de lectura simples y rapidos (denormalizados) | Duplicacion de codigo (modelos separados) |
| Escalabilidad independiente | Consistencia eventual entre modelos |
| Seguridad granular (diferentes permisos para commands y queries) | Mayor uso de almacenamiento |
| Facil integracion con Event Sourcing | Dificil justificacion en sistemas simples |

## Glosario

**CQRS**: Patron que separa las operaciones de lectura (queries) y escritura (commands) en modelos distintos y optimizados independientemente.

**Command**: Operacion que cambia el estado del sistema (crear, actualizar, eliminar). No retorna datos de dominio, solo confirmacion.

**Query**: Operacion que lee el estado del sistema sin modificarlo. Retorna datos sin efectos secundarios.

**Modelo de escritura**: Esquema optimizado para comandos, normalmente normalizado y con validaciones de negocio.

**Modelo de lectura**: Esquema optimizado para consultas, normalmente denormalizado y con estructuras simplificadas.

**Denormalizacion**: Tecnica que combina datos en una sola estructura para acelerar lecturas, sacrificando redundancia controlada.

**Consistencia eventual**: En CQRS con sincronizacion asincrona, el modelo de lectura puede estar momentaneamente desactualizado respecto al de escritura.

**Sincronizacion**: Mecanismo (triggers, eventos, jobs) que mantiene actualizado el modelo de lectura a partir del modelo de escritura.

**Event Sourcing**: Almacen de eventos inmutable que registra todos los cambios; complementa a CQRS proporcionando el historial completo.

**Separacion de responsabilidades**: Dividir un sistema en partes con propositos distintos para facilitar su mantenimiento y evolucion.

## Ejercicios

### Ejercicio 1: Identificar commands y queries
Clasifica cada operacion como Command (C) o Query (Q):

a) `GET /api/users/123`
b) `POST /api/orders`
c) `DELETE /api/products/456`
d) `GET /api/search?q=laptop`
e) `PUT /api/profile`
f) `PATCH /api/orders/789/status`
g) `POST /api/login`
h) `GET /api/reports/sales`

> Respuesta:

### Ejercicio 2: Disenar modelos separados
Un sistema de blogging tiene las siguientes operaciones:

**Escritura**: Crear articulo, editar articulo, publicar/despublicar, agregar comentario, eliminar comentario.
**Lectura**: Ver articulo con todos sus comentarios, listar articulos recientes, buscar por titulo, ver dashboard de estadisticas.

Disena un modelo de escritura (tablas normalizadas) y un modelo de lectura (vistas denormalizadas u optimizadas) siguiendo CQRS. Explica como se sincronizan.

> Respuesta:

### Ejercicio 3: CQRS sin Event Sourcing
Un equipo quiere implementar CQRS pero no quiere usar Event Sourcing por simplicidad. Proponen usar la misma base de datos pero con tablas separadas para lectura y escritura, sincronizadas con triggers o jobs programados. Analiza las ventajas y desventajas de este enfoque hibrido frente a CQRS completo con Event Sourcing.

> Respuesta:

## Soluciones

<details>
<summary>Solucion 1</summary>

a) GET /api/users/123 -> **Q** (query - lectura)
b) POST /api/orders -> **C** (command - creacion)
c) DELETE /api/products/456 -> **C** (command - eliminacion)
d) GET /api/search?q=laptop -> **Q** (query - busqueda)
e) PUT /api/profile -> **C** (command - actualizacion)
f) PATCH /api/orders/789/status -> **C** (command - cambio de estado)
g) POST /api/login -> **C** (command - genera sesion/token; modifica estado)
h) GET /api/reports/sales -> **Q** (query - reporte)

Nota: POST /login puede considerarse command porque modifica estado (crea sesion, actualiza ultimo login, etc).

</details>

<details>
<summary>Solucion 2</summary>

**Modelo de Escritura (normalizado)**:

| Tabla | Columnas |
|-------|----------|
| `autores` | id, nombre, email |
| `articulos` | id, autor_id, titulo, contenido, estado (borrador/publicado), fecha_creacion, fecha_publicacion |
| `comentarios` | id, articulo_id, autor_nombre, contenido, fecha, estado (pendiente/aprobado/rechazado) |
| `tags` | id, nombre |
| `articulos_tags` | articulo_id, tag_id |

**Modelo de Lectura (denormalizado)**:

| Tabla/Vista | Columnas | Uso |
|-------------|----------|-----|
| `v_articulos_detalle` | articulo_id, titulo, contenido, autor_nombre, tags (JSON), fecha_publicacion, num_comentarios | Pagina del articulo |
| `v_articulos_recientes` | articulo_id, titulo, resumen, autor_nombre, fecha_publicacion, tags (JSON) | Lista de articulos |
| `v_estadisticas` | total_articulos, total_comentarios, articulos_publicados_hoy, autor_top | Dashboard |

**Sincronizacion**: Un worker/proceso escucha eventos del modelo de escritura (ej: "ArticuloCreado", "ComentarioAgregado") y actualiza las vistas de lectura. Puede ser inmediato (dentro de la misma transaccion) o eventual (cola de mensajes).

</details>

<details>
<summary>Solucion 3</summary>

**Ventajas del enfoque hibrido (CQRS sin Event Sourcing)**:

| Aspecto | Hibrido (BD unica) | Completo (con Event Sourcing) |
|---------|-------------------|-------------------------------|
| Complejidad | Baja-media | Alta |
| Consistencia | Fuerte (misma BD) | Eventual |
| Stack | Una BD, triggers/jobs | Event Store + BD de lectura |
| Auditoria | Limitada (logs de BD) | Completa (historial de eventos) |
| Reconstruccion | No posible | Posible en cualquier punto |

**Analisis**:

El enfoque hibrido es adecuado cuando:
- El equipo quiere los beneficios de separar lecturas/escrituras pero sin la inversion de Event Sourcing.
- La consistencia inmediata es necesaria para ciertas operaciones.
- No se necesita auditoria historica completa.
- El sistema es mediano y no justifica la infraestructura de Event Sourcing.

Limitaciones:
- Las tablas de lectura y escritura en la misma BD compiten por recursos (CPU, disco, memoria).
- No hay trazabilidad completa de cambios (solo el estado actual).
- Los triggers y jobs pueden volverse un punto de falla y complejidad.
</details>
