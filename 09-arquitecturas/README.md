# Nivel 9: Arquitecturas de Software

## Concepto

Este nivel cubre los patrones y estilos arquitectonicos mas importantes en el desarrollo de software moderno. Comprender estas arquitecturas permite disenar sistemas mantenibles, escalables y alineados con las necesidades del negocio.

## Modulos

1. **01-capas** - Arquitectura en capas (presentacion, negocio, persistencia, base de datos)
2. **02-hexagonal** - Puertos y adaptadores, dominio limpio, inversion de dependencias
3. **03-microservicios** - Descomposicion en servicios, contexto acotado, comunicacion sincrona/asincrona
4. **04-event-driven** - Event sourcing, pub/sub, brokers de mensajes, consistencia eventual, CQRS
5. **05-cqrs** - Separacion de responsabilidades de comandos y consultas
6. **06-system-design** - Cache con Redis, CDN, balanceadores, escalabilidad, teorema CAP, rate limiting
7. **07-ddd-intro** - Lenguaje ubicuo, contexto acotado, entidades, objetos valor, agregados, repositorios

## Ejercicios del Nivel

### Ejercicio 1: Seleccion de arquitectura
Un equipo debe construir un sistema de gestion de pedidos para una cadena de restaurantes. Debe manejar menus, pedidos en linea, pagos, inventario y entregas. El sistema comenzara pequeno pero debe escalar a nivel nacional. Que arquitectura recomendarias y por que? Justifica considerando capas, microservicios, CQRS y DDD.

> Respuesta:

### Ejercicio 2: Comparacion de estilos
Completa la siguiente tabla comparativa con tus conocimientos:

| Aspecto | Capas | Hexagonal | Microservicios | Event-Driven |
|---------|-------|-----------|----------------|--------------|
| Acoplamiento | | | | |
| Complejidad inicial | | | | |
| Escalabilidad | | | | |
| Pruebas unitarias | | | | |
| Despliegue | | | | |

> Respuesta:

### Ejercicio 3: Mapa conceptual
Dibuja un mapa conceptual (en ASCII) que relacione todos los temas de este nivel (capas, hexagonal, microservicios, event-driven, CQRS, system design, DDD). Muestra como se complementan entre si.

> Respuesta:

## Soluciones

<details>
<summary>Solucion 1</summary>

Recomendacion: Microservicios con DDD y CQRS.

Justificacion:
- **Microservicios**: Cada dominio (menus, pedidos, pagos, inventario, entregas) puede ser un servicio independiente. Esto permite escalar horizontalmente solo los servicios con mayor carga (pedidos, pagos).
- **DDD**: Ayuda a delimitar los contextos acotados de cada dominio. El lenguaje ubicuo permite que el equipo de negocio y desarrollo hablen el mismo idioma.
- **CQRS**: Los pedidos tienen alta concurrencia de escritura (creacion, actualizacion) y lectura (consulta de estado). Separar comandos y consultas optimiza ambos lados.
- **Capas**: Cada microservicio internamente puede usar arquitectura en capas para separar responsabilidades internas.
</details>

<details>
<summary>Solucion 2</summary>

| Aspecto | Capas | Hexagonal | Microservicios | Event-Driven |
|---------|-------|-----------|----------------|--------------|
| Acoplamiento | Alto entre capas | Bajo (dependencias hacia dentro) | Bajo (cada servicio independiente) | Bajo (desacoplados por eventos) |
| Complejidad inicial | Baja | Media | Alta | Alta |
| Escalabilidad | Vertical | Vertical | Horizontal | Horizontal |
| Pruebas unitarias | Faciles (capas aisladas) | Muy faciles (dominio puro) | Complejas (integración entre servicios) | Complejas (eventos asincronos) |
| Despliegue | Monolitico | Monolitico | Independiente por servicio | Independiente por servicio |

</details>

<details>
<summary>Solucion 3</summary>

```
                    +-------------------+
                    |      DDD          |
                    | (Lenguaje Ubicuo,  |
                    |  Contextos,        |
                    |  Agregados)        |
                    +--------+----------+
                             |
            +----------------+------------------+
            |                                    |
+-----------v----------+             +-----------v-----------+
|    Hexagonal         |             |    Microservicios     |
| (Puertos/Adaptadores)|             | (Contextos acotados)  |
| Dominio puro         |             | Comunicacion por red  |
+----------+-----------+             +-----------+-----------+
           |                                      |
+----------v-----------+              +-----------v-----------+
|      Capas           |              |   Event-Driven        |
| (Presentacion,       |              |   (Pub/Sub, Broker)   |
|  Negocio, Datos)     |              |                        |
+----------------------+              +-----------+-----------+
                                                   |
                                          +--------v--------+
                                          |      CQRS       |
                                          | (Commands/Queries|
                                          |  separados)      |
                                          +------------------+
                                                   |
                                          +--------v--------+
                                          |  System Design   |
                                          | (Cache, CDN,     |
                                          |  Balanceo, CAP)  |
                                          +------------------+
```

DDD define los limites del dominio. Hexagonal mantiene el dominio puro. Microservicios despliegan cada contexto. Capas organizan cada microservicio internamente. Event-Driven y CQRS manejan la comunicacion y optimizacion de lecturas/escrituras. System Design resuelve los problemas de escalabilidad e infraestructura.
</details>
