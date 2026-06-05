# 02 - Arquitectura Hexagonal (Ports and Adapters)

## Concepto

La arquitectura hexagonal, propuesta por Alistair Cockburn, coloca el dominio de la aplicacion en el centro y lo aísla de los detalles externos (bases de datos, APIs, interfaces de usuario) mediante puertos (interfaces) y adaptadores (implementaciones).

Principio clave: **el dominio no depende de nada externo**. Las dependencias apuntan hacia adentro (Dependency Inversion Principle).

- **Puertos (Ports)**: Interfaces que definen la comunicacion entre el dominio y el exterior. Pueden ser entrantes (inbound, casos de uso) o salientes (outbound, repositorios).
- **Adaptadores (Adapters)**: Implementaciones concretas de los puertos. Por ejemplo, un adaptador REST, un adaptador de base de datos PostgreSQL, un adaptador de cola RabbitMQ.

## Diagrama (ASCII)

```
                        +-------------------+
                        |   Adaptador REST  |  <- Driving Adapter
                        +--------+----------+
                                 |  llamada
                        +--------v----------+
          +-------------+    Puerto In      +-------------+
          |             | (Caso de Uso)     |             |
          |             +--------+----------+             |
          |                      |                        |
+---------v----------+  +-------v--------+  +------------v---------+
| Adaptador Web      |  |    DOMINIO     |  | Adaptador CLI        |
| (Driving)          |  | (Entidades,    |  | (Driving)            |
|                     |  |  Servicios)    |  |                      |
+---------------------+  +-------+-------+  +----------------------+
                                  |
                    +-------------+-------------+
                    |             |             |
          +---------v---+ +------v------+ +----v----------+
          | Puerto Out  | | Puerto Out  | | Puerto Out    |
          | Repositorio | |  Notificac. | |  Facturacion  |
          +------+------+ +------+------+ +-------+-------+
                 |               |                |
          +------v------+ +------v------+ +-------v-------+
          | Adaptador   | | Adaptador   | | Adaptador     |
          | PostgreSQL  | | SendGrid    | | Stripe        |
          | (Driven)    | | (Driven)    | | (Driven)      |
          +-------------+ +-------------+ +---------------+
```

## Ejemplo

Un sistema de transferencias bancarias:

- **Dominio**: `Cuenta`, `Transferencia`, `SaldoInsuficienteException`.
- **Puerto In**: `RealizarTransferencia` (caso de uso).
- **Puerto Out**: `CuentaRepositorio` (interfaz para guardar/cargar cuentas).
- **Adaptador Driving**: `TransferenciaController` (REST).
- **Adaptador Driven**: `CuentaRepositorioPostgres` (implementacion con JDBC/ORM).

## Ventajas / Desventajas

| Ventajas | Desventajas |
|----------|-------------|
| Dominio completamente aislado y testeable | Mayor numero de interfaces/indireccion |
| Cambiar tecnologia externa no afecta el core | Curva de aprendizaje alta |
| Excelente para pruebas (mocks en puertos) | Sobrecarga inicial para proyectos pequenos |
| Alta cohesion, bajo acoplamiento | Puede llevar a sobrediseno |
| Facilita la adopcion de DDD | Dificil de justificar en CRUD simples |

## Ejercicios

### Ejercicio 1: Identificar puertos y adaptadores
Un sistema de reservas de hotel tiene las siguientes clases. Clasifica cada una como: Puerto In, Puerto Out, Adaptador Driving, Adaptador Driven, o Entidad de Dominio.

- `ReservaRepository` (interfaz)
- `ReservaRepositoryMySQL`
- `BuscarHabitacionesDisponibles` (interfaz)
- `ReservaController` (REST)
- `PagoService` (interfaz)
- `PagoConStripe`
- `Habitacion` (clase)
- `NotificadorReserva` (interfaz)
- `NotificadorReservaEmail`

> Respuesta:

### Ejercicio 2: Disenar puertos para un sistema de pedidos
Disena los puertos (inbound y outbound) necesarios para un sistema de domicilios de comida. Considera: crear pedido, consultar menu, procesar pago, notificar al cliente y al restaurante, y rastrear entrega.

> Respuesta:

### Ejercicio 3: Refactorizar a hexagonal
El siguiente codigo tiene una violacion tipica. Refactorizalo siguiendo arquitectura hexagonal:

```java
public class OrderService {
    private MySQLDatabase db = new MySQLDatabase();
    private EmailSender sender = new EmailSender();

    public void createOrder(OrderData data) {
        db.saveOrder(data);
        sender.send("cliente@email.com", "Pedido creado");
    }
}
```

> Respuesta:

## Soluciones

<details>
<summary>Solucion 1</summary>

| Clase | Tipo |
|-------|------|
| `ReservaRepository` | Puerto Out |
| `ReservaRepositoryMySQL` | Adaptador Driven |
| `BuscarHabitacionesDisponibles` | Puerto In |
| `ReservaController` | Adaptador Driving |
| `PagoService` | Puerto Out |
| `PagoConStripe` | Adaptador Driven |
| `Habitacion` | Entidad de Dominio |
| `NotificadorReserva` | Puerto Out |
| `NotificadorReservaEmail` | Adaptador Driven |

</details>

<details>
<summary>Solucion 2</summary>

**Puertos Inbound (Casos de Uso)**
- `CrearPedido` (recibe datos del pedido, valida, retorna confirmacion)
- `ConsultarMenu` (retorna platos disponibles)
- `RastrearEntrega` (retorna estado actual del pedido)

**Puertos Outbound**
- `PedidoRepositorio` (guarda y recupera pedidos)
- `MenuRepositorio` (obtener platos del restaurante)
- `ProcesadorPagos` (procesa transaccion con tarjeta/efectivo)
- `Notificador` (envia notificaciones al cliente y restaurante)
- `ServicioMapa` (obtiene coordenadas y calcula rutas)

</details>

<details>
<summary>Solucion 3</summary>

Refactorizacion:

```java
// Puerto Outbound
public interface PedidoRepositorio {
    void guardar(OrderData data);
}

public interface Notificador {
    void enviar(String destinatario, String mensaje);
}

// Puerto Inbound
public interface CrearPedido {
    void ejecutar(OrderData data);
}

// Dominio puro (no conoce detalles de infraestructura)
public class OrderService implements CrearPedido {
    private PedidoRepositorio repositorio;
    private Notificador notificador;

    public OrderService(PedidoRepositorio repositorio, Notificador notificador) {
        this.repositorio = repositorio;
        this.notificador = notificador;
    }

    public void ejecutar(OrderData data) {
        // Logica de negocio pura
        this.repositorio.guardar(data);
        this.notificador.enviar(data.getEmail(), "Pedido creado");
    }
}

// Adaptadores Driven
public class MySQLPedidoRepositorio implements PedidoRepositorio { ... }
public class EmailNotificador implements Notificador { ... }

// Adaptador Driving (REST)
public class OrderController {
    private CrearPedido crearPedido;
    // ...
}
```
</details>
