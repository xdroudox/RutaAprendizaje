# 03 - Microservicios

## Concepto

La arquitectura de microservicios estructura una aplicacion como un conjunto de servicios pequenos, autonomos y desplegables independientemente. Cada microservicio se enfoca en un unico dominio o capacidad de negocio (principio de responsabilidad unica).

Caracteristicas clave:

- **Despliegue independiente**: Cada servicio puede ser desplegado sin afectar a los demas.
- **Descentralizacion**: Cada servicio puede usar su propia tecnologia, base de datos y lenguaje.
- **Comunicacion por red**: Los servicios se comunican via HTTP/REST, gRPC, o mensajeria asincrona (RabbitMQ, Kafka).
- **Contexto acotado**: Cada servicio modela un subdominio especifico (inspirado en DDD).

## Diagrama (ASCII)

```
+-------------------------------------------------------------------+
|                        API Gateway                                 |
+-------------------------------------------------------------------+
      |              |              |               |
+-----v------+ +-----v------+ +----v-------+ +----v--------+
| Servicio   | | Servicio   | | Servicio   | | Servicio    |
| Usuarios   | | Pedidos    | | Pagos      | | Inventario  |
+-----+------+ +-----+------+ +-----+------+ +-----+-------+
      |              |              |               |
+-----v------+ +-----v------+      |               |
| BD Usuarios| | BD Pedidos |      |               |
+------------+ +------------+      |               |
                           +-------v------+ +------v-------+
                           | BD Pagos    | | BD Inventario|
                           +-------------+ +--------------+

Comunicacion sincrona:
  Servicio A --HTTP--> Servicio B

Comunicacion asincrona:
  Servicio A --Evento--> [RabbitMQ/Kafka] --> Servicio B
```

## Ejemplo

Sistema de e-commerce como microservicios:

- **Servicio Catalogo**: Productos, categorias, busqueda (BD MongoDB).
- **Servicio Carrito**: Gestion del carrito de compras (BD Redis).
- **Servicio Pedidos**: Creacion y seguimiento de pedidos (BD PostgreSQL).
- **Servicio Pagos**: Procesamiento de pagos con Stripe/PayPal (BD PostgreSQL).
- **Servicio Inventario**: Control de stock y almacenes (BD MySQL).
- **Servicio Notificaciones**: Emails, SMS, push (sin BD propia).

## Ventajas / Desventajas

| Ventajas | Desventajas |
|----------|-------------|
| Escalabilidad independiente por servicio | Complejidad de red y latencia |
| Tecnologia heterogenea (polyglot) | Consistencia de datos entre servicios |
| Equipos autonomos por servicio | Testing de integracion complejo |
| Despliegue independiente | Debugging distribuido (trazas) |
| Aislamiento de fallos | Gestion de configuraciones y secretos |

## Glosario

**Microservicio**: Servicio pequeno, autonomo y desplegable independientemente que se enfoca en una unica capacidad de negocio.

**API Gateway**: Punto unico de entrada que enruta peticiones a los microservicios correspondientes y gestiona autenticacion, rate limiting y balanceo.

**Despliegue independiente**: Capacidad de actualizar, escalar o desplegar un servicio sin afectar a los demas.

**Contexto acotado**: Limite explicito donde un modelo de dominio es valido, inspirandose en DDD para definir el alcance de cada microservicio.

**Comunicacion sincrona**: El emisor espera una respuesta inmediata del receptor, tipicamente via HTTP/REST o gRPC.

**Comunicacion asincrona**: El emisor envía un mensaje sin esperar respuesta, usando brokers como RabbitMQ o Kafka.

**Broker de mensajes**: Sistema intermediario (cola o stream) que recibe, almacena y distribuye mensajes entre servicios.

**Polyglot persistence**: Practica de usar diferentes tipos de bases de datos segun las necesidades de cada microservicio.

**Escalabilidad horizontal**: Capacidad de agregar mas instancias de un servicio para manejar mayor carga de trabajo.

**Tolerancia a fallos**: Capacidad del sistema de seguir operando ante la caida de uno o varios servicios individuales.

## Ejercicios

### Ejercicio 1: Descomposicion de un monolitico
Un sistema monolítico de gestion hospitalaria maneja: pacientes, citas, historial medico, facturacion, farmacia, laboratorio y recursos humanos. Propone una descomposicion en microservicios indicando que servicio se encargaria de cada modulo y que base de datos usaria cada uno.

> Respuesta:

### Ejercicio 2: Sincrono vs Asincrono
Para cada uno de los siguientes escenarios en un sistema de microservicios, indica si la comunicacion debe ser sincrona (HTTP/gRPC) o asincrona (eventos/cola) y justifica:

a) Un usuario hace clic en "Realizar pedido" y debe confirmarse el pago antes de responder.
b) Cuando un pedido es enviado, el inventario debe actualizarse y el cliente debe recibir una notificacion.
c) El servicio de recomendaciones necesita el historial de compras del usuario para calcular sugerencias.
d) Un administrador actualiza el precio de un producto y todos los servicios deben reflejar el cambio.

> Respuesta:

### Ejercicio 3: Disenar API Gateway
Disena las rutas y responsabilidades de un API Gateway para un sistema de microservicios de reservas de vuelos. Considera servicios de: busqueda de vuelos, reservas, pagos, usuarios y notificaciones. Que rutas expone el gateway? Como maneja autenticacion y rate limiting?

> Respuesta:

## Soluciones

<details>
<summary>Solucion 1</summary>

| Modulo | Microservicio | Base de Datos sugerida |
|--------|--------------|----------------------|
| Pacientes | Servicio Pacientes | PostgreSQL |
| Citas | Servicio Citas | PostgreSQL |
| Historial Medico | Servicio Historias Clinicas | MongoDB (documentos) |
| Facturacion | Servicio Facturacion | PostgreSQL |
| Farmacia | Servicio Farmacia | PostgreSQL |
| Laboratorio | Servicio Laboratorio | PostgreSQL |
| Recursos Humanos | Servicio RRHH | PostgreSQL (aislado) |

Cada servicio es autonmo y se comunica via API REST o eventos.

</details>

<details>
<summary>Solucion 2</summary>

a) **Sincrono**. El usuario necesita una respuesta inmediata sobre el exito del pago para confirmar el pedido.

b) **Asincrono**. No es necesario que el cliente espere a que el inventario se actualice. Se publica un evento "PedidoEnviado" y los servicios de inventario y notificaciones reaccionan.

c) **Sincrono** (con cache). El servicio de recomendaciones necesita los datos inmediatamente para calcular la respuesta. Puede cachear resultados para optimizar.

d) **Asincrono**. Se publica un evento "PrecioActualizado". Cada servicio consume el evento y actualiza su cache local. No es necesario que todos respondan sincronamente.

</details>

<details>
<summary>Solucion 3</summary>

**API Gateway - Reservas de Vuelos**

Rutas expuestas:

| Ruta Publica | Metodo | Servicio Destino |
|-------------|--------|-----------------|
| `/api/v1/vuelos` | GET | Busqueda (catalogo) |
| `/api/v1/vuelos/{id}` | GET | Busqueda (catalogo) |

Rutas autenticadas (requieren JWT):

| Ruta | Metodo | Servicio Destino |
|------|--------|-----------------|
| `/api/v1/reservas` | GET/POST | Reservas |
| `/api/v1/reservas/{id}` | GET/DELETE | Reservas |
| `/api/v1/pagos` | POST | Pagos |
| `/api/v1/usuarios/perfil` | GET/PUT | Usuarios |
| `/api/v1/notificaciones` | GET | Notificaciones |

**Autenticacion**: El Gateway valida el JWT en cada request antes de enrutar. Si es invalido, responde 401 sin llegar al servicio.

**Rate Limiting**: El Gateway limita a 100 req/min por usuario en rutas publicas y 1000 req/min en rutas autenticadas. Usa Redis para contador de requests por IP/usuario.
</details>
