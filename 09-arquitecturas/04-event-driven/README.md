# 04 - Arquitectura Event-Driven (Event Sourcing, Pub/Sub, CQRS)

## Concepto

La arquitectura orientada a eventos (Event-Driven Architecture - EDA) se basa en la produccion, deteccion y reaccion a eventos. Un evento es un cambio significativo en el estado del sistema (ej: "PedidoCreado", "PagoRecibido").

Componentes clave:

- **Productor de eventos**: Emite eventos sin conocer a los consumidores.
- **Broker de mensajes**: Canal de comunicacion (RabbitMQ, Apache Kafka, AWS SNS/SQS, Redis Pub/Sub).
- **Consumidor de eventos**: Escucha y reacciona a los eventos.
- **Event Sourcing**: Almacenar el estado como una secuencia inmutable de eventos, no como el estado actual.
- **Consistencia eventual**: El sistema no es consistente inmediatamente, pero lo sera con el tiempo.

## Diagrama (ASCII)

```
     Productores                          Broker                          Consumidores
+-------------------+          +----------------------+          +-------------------+
| Servicio Pedidos  +---Evento->                      +--Escucha-> Servicio Email    |
+-------------------+   "PedidoCreado" |   Kafka /     |          +-------------------+
                                       |  RabbitMQ     |
+-------------------+          +-------v--------------+          +-------------------+
| Servicio Pagos    +---Evento->                      +--Escucha-> Servicio Inventario|
+-------------------+   "PagoRealizado" |              |          +-------------------+
                                       |              |
+-------------------+          +----------------------+          +-------------------+
| Servicio Usuarios +---Evento->                               | Servicio Analytics |
+-------------------+   "UsuarioRegistrado"                     +-------------------+

Event Sourcing:
+----------------+
| Event Store    |
+----------------+
| Version 1:     |  "CuentaCreada"
| Version 2:     |  "DepositoRealizado"  <- Estado actual = suma de eventos
| Version 3:     |  "RetiroRealizado"
| Version 4:     |  "DepositoRealizado"
+----------------+
```

## Ejemplo

Un sistema de comercio electronico con EDA:

1. Usuario crea pedido -> Servicio Pedidos emite `PedidoCreado`
2. Servicio Pagos consume el evento y procesa el pago -> emite `PagoExitoso` o `PagoFallido`
3. Servicio Inventario consume `PagoExitoso` y reserva productos -> emite `StockReservado`
4. Servicio Notificaciones consume `StockReservado` y envia email al cliente
5. Servicio Logistica consume `StockReservado` y programa la entrega

Cada servicio es independiente y evoluciona su propio estado.

## Ventajas / Desventajas

| Ventajas | Desventajas |
|----------|-------------|
| Desacoplamiento total entre servicios | Complejidad de debuggeo (flujo asincrono) |
| Escalabilidad horizontal (particion de eventos) | Consistencia eventual (no ACID) |
| Tolerancia a fallos (reintentos, colas) | Dificultad para mantener orden global |
| Auditoria natural (historial de eventos) | Mayor latencia en operaciones |
| Permite agregar nuevos consumidores facilmente | Brokers como punto unico de falla |

## Glosario

**Evento**: Cambio significativo en el estado del sistema representado como un mensaje inmutable (ej: "PedidoCreado", "PagoRecibido").

**Arquitectura orientada a eventos (EDA)**: Estilo arquitectonico donde los componentes se comunican produciendo y consumiendo eventos de forma desacoplada.

**Productor de eventos**: Componente que emite eventos sin conocer quienes los consumiran.

**Consumidor de eventos**: Componente que escucha y reacciona a eventos publicados en el broker.

**Broker de mensajes**: Canal de comunicacion intermediario (Kafka, RabbitMQ) que almacena y distribuye eventos entre productores y consumidores.

**Event Sourcing**: Patron que almacena el estado del sistema como una secuencia inmutable de eventos en lugar de solo el estado actual.

**Consistencia eventual**: Propiedad donde el sistema no es consistente inmediatamente tras una escritura, pero lo sera con el tiempo.

**Dead Letter Queue (DLQ)**: Cola especial donde se envian eventos que fallaron repetidamente para su inspeccion sin bloquear el flujo principal.

**Idempotencia**: Propiedad que garantiza que procesar el mismo evento varias veces produce el mismo resultado final.

**Backoff exponencial**: Estrategia de reintentos donde el tiempo de espera se incrementa progresivamente (1s, 2s, 4s, 8s...).

## Ejercicios

### Ejercicio 1: Disenar flujo de eventos
Disena el flujo de eventos para un sistema de reservas de hotel. Incluye al menos 5 eventos diferentes y muestra que servicios los producen y cuales los consumen. Usa flechas ASCII.

> Respuesta:

### Ejercicio 2: Event Sourcing vs Estado Actual
Un sistema bancario debe mantener el historial completo de transacciones de una cuenta. Explica por que Event Sourcing es adecuado aqui. Compara con un modelo tradicional de tabla `accounts` donde solo se almacena el saldo actual. Que ventajas tiene Event Sourcing para auditoria y deteccion de fraudes?

> Respuesta:

### Ejercicio 3: Manejo de fallos en EDA
En un sistema event-driven, el servicio de notificaciones falla durante 10 minutos. Durante ese tiempo ocurren 3 eventos "PedidoConfirmado". Disena una estrategia para que ningun evento se pierda y las notificaciones pendientes se procesen cuando el servicio se recupere. Considera dead letter queues, reintentos y persistencia.

> Respuesta:

## Soluciones

<details>
<summary>Solucion 1</summary>

```
[Cliente] --reserva--> [Servicio Reservas]
                        |
                        +-- evento "ReservaCreada"
                              |
                     +--------+--------+
                     |                  |
              [Servicio Pago]    [Servicio Inventario]
                     |                  |
                     +-- "PagoExitoso"  +-- "HabitacionReservada"
                           |                  |
                     +-----+-----+     +------+------+
                     |           |     |             |
              [Servicio Email] [Servicio Factura] [Servicio Limpieza]
                     |           |                   |
                     |           +-- "FacturaEmitida"|
                     |                               |
                     +-- "EmailEnviado"               +-- "LimpiezaProgramada"
```

Eventos:
1. `ReservaCreada` (Reservas -> Pago, Inventario)
2. `PagoExitoso` (Pago -> Email, Factura)
3. `HabitacionReservada` (Inventario -> Limpieza)
4. `FacturaEmitida` (Factura -> Email)
5. `EmailEnviado` (Email -> Logging/Auditoria)

</details>

<details>
<summary>Solucion 2</summary>

**Modelo tradicional (solo saldo)**:
- Tabla `accounts`: `id, saldo, updated_at`
- Ventaja: consulta de saldo rapida (O(1))
- Desventaja: no hay historial de transacciones, no se puede auditar, no se puede detectar fraudes retroactivamente.

**Event Sourcing**:
- Event Store con eventos: `CuentaCreada(1000)`, `Deposito(500)`, `Retiro(200)`, `Deposito(300)`, etc.
- Saldo actual = sumar todos los eventos.
- Ventajas para auditoria: se puede reconstruir el estado en cualquier punto del tiempo, detectar transacciones anomalas, auditar quien hizo que y cuando.
- Deteccion de fraudes: si un retiro parece sospechoso, se puede revisar toda la secuencia de eventos de la cuenta. Un modelo tradicional solo mostraria el saldo final.

</details>

<details>
<summary>Solucion 3</summary>

Estrategia con Kafka / RabbitMQ:

1. **Persistencia en el broker**: Los mensajes persisten en disco (Kafka retention o colas durables en RabbitMQ). Aunque el consumidor caiga, los eventos no se pierden.

2. **Consumer offset**: Kafka mantiene el offset de cada consumidor. Cuando el servicio de notificaciones se recupera, reanuda desde el ultimo offset procesado.

3. **Dead Letter Queue (DLQ)**: Si un evento falla despues de N reintentos, se mueve a una DLQ para inspeccion manual sin bloquear el flujo principal.

4. **Reintentos con backoff**: El consumidor reintenta con backoff exponencial (1s, 2s, 4s, ...) hasta un maximo de reintentos.

5. **Idempotencia**: El servicio de notificaciones debe ser idempotente (marcar eventos como procesados) para evitar notificaciones duplicadas si un mismo evento se entrega mas de una vez.

Flujo:
```
[Broker] -> Consumidor Notificaciones (CAIDO) -> eventos en cola
[10 min despues] -> Consumidor se recupera -> lee desde offset pendiente
-> procesa eventos 1, 2, 3 -> envia 3 emails -> confirma offsets
```
</details>
