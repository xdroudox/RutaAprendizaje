# 01 - Arquitectura en Capas (Layered Architecture)

## Concepto

La arquitectura en capas organiza el software en niveles horizontales donde cada capa tiene una responsabilidad especifica. Las capas superiores dependen de las inferiores, y cada una solo se comunica con la capa inmediatamente siguiente (o anterior).

Las cuatro capas tipicas son:

- **Presentacion**: Interfaz de usuario (API, UI, controllers). Maneja la entrada/salida con el exterior.
- **Negocio (Business/Service)**: Logica de dominio, reglas de negocio, validaciones. Es el corazon de la aplicacion.
- **Persistencia (Data Access)**: Acceso a datos, repositorios, DAOs. Abstracts el almacenamiento.
- **Base de Datos**: El motor de base de datos fisico (SQL, NoSQL, archivos).

## Diagrama (ASCII)

```
+---------------------------+
|     Presentacion          |  <- API, Controllers, Vistas
+---------------------------+
        |  llamadas
+---------------------------+
|     Negocio / Servicios   |  <- Reglas de negocio, DTOs
+---------------------------+
        |  llamadas
+---------------------------+
|     Persistencia / DAO    |  <- Repositorios, acceso a datos
+---------------------------+
        |  SQL/ORM
+---------------------------+
|     Base de Datos         |  <- MySQL, PostgreSQL, MongoDB
+---------------------------+
```

## Ejemplo

Un sistema de gestion de usuarios:

- **Presentacion**: `UserController` recibe peticiones HTTP (GET /users, POST /users).
- **Negocio**: `UserService` valida reglas (email unico, edad minima, hash de password).
- **Persistencia**: `UserRepository` ejecuta consultas SQL o usa un ORM.
- **BD**: Tabla `users` en PostgreSQL.

Flujo tipico: `Controller -> Service -> Repository -> DB`

## Ventajas / Desventajas

| Ventajas | Desventajas |
|----------|-------------|
| Separacion clara de responsabilidades | Acoplamiento entre capas |
| Facil de entender para equipos nuevos | Puede degenerar en "big ball of mud" |
| Reutilizacion de capas inferiores | Dificil escalar horizontalmente |
| Pruebas unitarias por capa aislada | Transicion a microservicios dolorosa |
| Ampliamente conocida y documentada | Rigidez en la direccion de dependencias |

## Glosario

**Arquitectura en capas**: Estilo de diseno que organiza el software en niveles horizontales con responsabilidades separadas.

**Capa de presentacion**: Capa que maneja la interaccion con el usuario (interfaz grafica, API, controladores).

**Capa de negocio**: Capa que contiene la logica de dominio, reglas de negocio y validaciones de la aplicacion.

**Capa de persistencia**: Capa encargada del acceso a datos, repositorios y abstraccion del almacenamiento.

**DTO (Data Transfer Object)**: Objeto ligero que transporta datos entre capas sin incluir logica de negocio.

**ORM (Object-Relational Mapping)**: Tecnica que mapea objetos del codigo a tablas de una base de datos relacional.

**Acoplamiento**: Grado de dependencia entre capas o modulos; un alto acoplamiento dificulta los cambios.

**Responsabilidad unica**: Principio que indica que cada capa o modulo debe tener una unica razon para cambiar.

**Big ball of mud**: Antipatron donde el software crece sin estructura clara, volviendose caotico y dificil de mantener.

**Separacion de preocupaciones (SoC)**: Principio de dividir el sistema en secciones distintas que no se solapan en responsabilidades.

## Ejercicios

### Ejercicio 1: Identificacion de capas
Dado el siguiente listado de clases, asignalas a la capa correspondiente (Presentacion, Negocio, Persistencia, BD):

- `OrderController`
- `UserRepository`
- `ProductService`
- `PaymentGatewayAdapter`
- `Invoice`
- `DatabaseConnectionPool`
- `AuthMiddleware`
- `DiscountCalculator`

> Respuesta:

### Ejercicio 2: Diseno de capas para un e-commerce
Disena la estructura de capas para un sistema de e-commerce que debe manejar: catalogo de productos, carrito de compras, procesamiento de pagos y envio de notificaciones. Describe que clases/metodos existirian en cada capa.

> Respuesta:

### Ejercicio 3: Identificar violaciones
El siguiente codigo muestra una violacion tipica de la arquitectura en capas. Identifica el problema y propon una correccion:

```java
// En un controller
public class OrderController {
    public void createOrder(OrderRequest req) {
        Connection conn = DriverManager.getConnection(DB_URL);
        conn.execute("INSERT INTO orders ...");
        sendEmail(req.getEmail(), "Pedido creado");
    }
}
```

> Respuesta:

## Soluciones

<details>
<summary>Solucion 1</summary>

| Clase | Capa |
|-------|------|
| `OrderController` | Presentacion |
| `UserRepository` | Persistencia |
| `ProductService` | Negocio |
| `PaymentGatewayAdapter` | Negocio / Persistencia (depende del diseno) |
| `Invoice` | Negocio (entidad de dominio) |
| `DatabaseConnectionPool` | Persistencia / BD |
| `AuthMiddleware` | Presentacion |
| `DiscountCalculator` | Negocio |

</details>

<details>
<summary>Solucion 2</summary>

**Presentacion**
- `ProductController` (GET /products, GET /products/{id})
- `CartController` (POST /cart/items, DELETE /cart/items/{id})
- `CheckoutController` (POST /checkout)
- `NotificationController` (GET /notifications)

**Negocio**
- `CatalogService` (busqueda, filtros, recomendaciones)
- `CartService` (agregar/quitar items, calcular subtotal)
- `PaymentService` (procesar pago, validar tarjeta, reembolsos)
- `NotificationService` (email, SMS, push)
- `InventoryService` (validar stock, reservar)

**Persistencia**
- `ProductRepository` (CRUD productos)
- `CartRepository` (persistencia del carrito)
- `OrderRepository` (ordenes de compra)
- `PaymentRepository` (transacciones de pago)

**Base de Datos**
- Tablas: `products`, `categories`, `cart_items`, `orders`, `order_items`, `payments`, `notifications`

</details>

<details>
<summary>Solucion 3</summary>

**Problema**: El controller (`OrderController`) esta accediendo directamente a la base de datos y enviando emails. Viola la separacion de capas: el controller solo deberia manejar la peticion HTTP y delegar al servicio de negocio.

**Correccion**:

```java
// Controller solo maneja la entrada
public class OrderController {
    private OrderService orderService;

    public void createOrder(OrderRequest req) {
        OrderResponse response = orderService.createOrder(req);
        return ResponseEntity.ok(response);
    }
}

// Service contiene la logica de negocio
public class OrderService {
    private OrderRepository orderRepository;
    private EmailService emailService;

    public OrderResponse createOrder(OrderRequest req) {
        Order order = new Order(req);
        orderRepository.save(order);
        emailService.sendConfirmation(order.getEmail());
        return new OrderResponse(order);
    }
}
```
</details>
