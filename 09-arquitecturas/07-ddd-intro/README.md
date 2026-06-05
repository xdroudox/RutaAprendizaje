# 07 - DDD (Domain-Driven Design) - Introduccion

## Concepto

Domain-Driven Design (DDD) es una aproximacion al diseno de software que pone el foco en el dominio del negocio y su logica. Fue popularizada por Eric Evans en su libro "Domain-Driven Design: Tackling Complexity in the Heart of Software".

Principios fundamentales:

- **Lenguaje Ubicuo (Ubiquitous Language)**: Vocabulario compartido entre expertos de negocio y desarrolladores. Un "pedido" significa lo mismo para todos.
- **Contexto Acotado (Bounded Context)**: Limite explicito donde un modelo de dominio es valido. El concepto "Producto" puede significar algo diferente en el contexto de Catalogo vs Almacen.
- **Entidades (Entities)**: Objetos con identidad unica (un Usuario tiene un ID, aunque sus atributos cambien).
- **Objetos Valor (Value Objects)**: Objetos sin identidad, definidos por sus atributos (Direccion, Dinero, Color).
- **Agregados (Aggregates)**: Grupo de objetos de dominio tratados como una unidad. Un Pedido (Agregado) contiene lineas de pedido (Entidades hijas).
- **Repositorios (Repositories)**: Mecanismo para recuperar y persistir agregados.

## Diagrama (ASCII)

```
+---------------------------------------------------------------------+
|                    CONTEXTO ACOTADO: VENTAS                          |
+---------------------------------------------------------------------+
|  Lenguaje Ubicuo: "Pedido", "Cliente", "Producto", "Factura"        |
|                                                                      |
|  +---------------------------+                                      |
|  |   AGREGADO: Pedido        |                                      |
|  |  +---------------------+  |                                      |
|  |  | Entidad: Pedido     |  |   +--------------------------------+ |
|  |  | - id: UUID          |  |   | Objeto Valor: Direccion        | |
|  |  | - fecha: DateTime   |  |   | - calle: String                | |
|  |  | - estado: String    |  |   | - ciudad: String               | |
|  |  | - direccion: VO     |  |   | - codigoPostal: String         | |
|  |  +---------------------+  |   +--------------------------------+ |
|  |         |  contiene       |                                      |
|  |  +------v---------------+ |   +--------------------------------+ |
|  |  | Entidad: LineaPedido | |   | Objeto Valor: Dinero           | |
|  |  | - id: UUID           | |   | - monto: BigDecimal            | |
|  |  | - producto: String   | |   | - moneda: String               | |
|  |  | - cantidad: int      | |   +--------------------------------+ |
|  |  | - precio: Dinero (VO)| |                                      |
|  |  +----------------------+ |                                      |
|  +---------------------------+                                      |
|                                                                      |
|  +---------------------------+                                      |
|  | REPOSITORIO: PedidoRepo  |                                      |
|  | - save(Pedido)           |                                      |
|  | - findById(id): Pedido   |                                      |
|  +---------------------------+                                      |
+---------------------------------------------------------------------+
             |
             | (diferente contexto)
             v
+---------------------------------------------------------------------+
|                    CONTEXTO ACOTADO: INVENTARIO                      |
+---------------------------------------------------------------------+
|  Lenguaje Ubicuo: "Stock", "Almacen", "Movimiento"                  |
|  "Producto" aqui es SOLO codigo + cantidad, no precio               |
+---------------------------------------------------------------------+
```

## Ejemplo

Sistema de gestion de restaurantes:

- **Contexto**: "Gestion de Mesas"
- **Lenguaje Ubicuo**: Mesa, Comensal, Cuenta, Plato, Bebida, Propina
- **Entidades**: `Mesa` (identificada por numero), `Cuenta` (identificada por ID)
- **Objetos Valor**: `Plato` (nombre, precio), `Direccion` (calle, numero, ciudad)
- **Agregado**: `Cuenta` (contiene lineas de platos y bebidas, calcula total)
- **Repositorio**: `CuentaRepository` (guarda y busca cuentas)

## Ventajas / Desventajas

| Ventajas | Desventajas |
|----------|-------------|
| Modelo de software alineado con el negocio | Curva de aprendizaje pronunciada |
| Comunicacion fluida entre negocio y tecnologia | Requiere expertos de dominio disponibles |
| Reduce la complejidad accidental | Puede generar sobrediseno en proyectos simples |
| Facilita el mantenimiento a largo plazo | Dificil de aplicar en equipos sin experiencia |
| Complementa perfectamente Hexagonal y Microservicios | Requiere refactorizacion continua del modelo |

## Ejercicios

### Ejercicio 1: Identificar Entidades y Objetos Valor
Clasifica cada concepto como Entidad (E) u Objeto Valor (OV):

a) Persona (con DNI)
b) Color RGB (255, 0, 0)
c) Factura (con numero de factura unico)
d) Coordenadas GPS (latitud, longitud)
e) Correo electronico ("user@example.com")
f) Cuenta bancaria (con numero de cuenta)
g) Rango de fechas (inicio, fin)
h) Reserva de hotel (con codigo de reserva)

> Respuesta:

### Ejercicio 2: Definir Agregados
Un sistema de gestion de biblioteca tiene las siguientes entidades y objetos valor. Agrupalos en agregados. Define cual es la entidad raiz (root) de cada agregado y que invariantes debe mantener.

Entidades: `Libro`, `Ejemplar`, `Prestamo`, `Usuario`, `Multa`
Objetos Valor: `ISBN`, `FechaPrestamo`, `FechaDevolucion`, `MontoMulta`

> Respuesta:

### Ejercicio 3: Disenar contexto acotado
Un sistema universitario tiene los siguientes modulos: Admisiones, Academico (cursos, calificaciones), Biblioteca, Finanzas (pagos, becas), Recursos Humanos (profesores). Identifica los contextos acotados y explica como el concepto "Estudiante" puede tener significados diferentes en cada contexto. Que atributos son relevantes en cada uno?

> Respuesta:

## Soluciones

<details>
<summary>Solucion 1</summary>

a) Persona (con DNI) -> **E** (Entidad - tiene identidad unica: DNI)
b) Color RGB (255, 0, 0) -> **OV** (Objeto Valor - definido por sus atributos, sin identidad)
c) Factura (con numero unico) -> **E** (Entidad - numero de factura como identidad)
d) Coordenadas GPS -> **OV** (Objeto Valor - latitud/longitud lo definen completamente)
e) Correo electronico -> **OV** (Objeto Valor - dos correos iguales son equivalentes)
f) Cuenta bancaria -> **E** (Entidad - numero de cuenta como identidad)
g) Rango de fechas -> **OV** (Objeto Valor - definido por inicio y fin)
h) Reserva de hotel -> **E** (Entidad - codigo de reserva como identidad)

</details>

<details>
<summary>Solucion 2</summary>

**Agregado 1: Libro**
- Raiz: `Libro` (identificado por ISBN)
- Contiene: `Ejemplar` (cada copia fisica)
- Invariantes: El numero de ejemplares debe coincidir con el stock registrado. No puede haber mas prestamos que ejemplares disponibles.

**Agregado 2: Prestamo**
- Raiz: `Prestamo` (identificado por ID de prestamo)
- Contiene: `FechaPrestamo`, `FechaDevolucion` (Objetos Valor)
- Invariantes: La fecha de devolucion debe ser posterior a la fecha de prestamo. Un usuario no puede tener mas de 5 prestamos activos simultaneamente.

**Agregado 3: Usuario**
- Raiz: `Usuario` (identificado por ID de usuario)
- Contiene: `Multa` (entidad hija, con `MontoMulta` como VO)
- Invariantes: Un usuario con multas pendientes no puede realizar nuevos prestamos. Las multas expiran despues de 30 dias.

</details>

<details>
<summary>Solucion 3</summary>

| Contexto | Significado de "Estudiante" | Atributos relevantes |
|----------|---------------------------|---------------------|
| **Admisiones** | Aspirante a ingresar | Nombre, documentos, puntaje examen, fecha solicitud, estado (aprobado/rechazado) |
| **Academico** | Alumno inscrito en cursos | ID estudiante, semestre, carrera, cursos inscritos, calificaciones, promedio |
| **Biblioteca** | Usuario con prestamos | ID estudiante, prestamos activos, multas pendientes, historial |
| **Finanzas** | Deudor o becado | ID estudiante, saldo pendiente, tipo beca, fecha pago, estado financiero |
| **RRHH** | No existe como concepto (aplica a profesores, no estudiantes) | N/A |

Cada contexto tiene su propia vision del "Estudiante". En Admisiones es un aspirante; en Academico es un alumno activo con notas; en Biblioteca es un usuario con prestamos; en Finanzas es un deudor. DDD sugiere modelos separados para cada contexto.
</details>
