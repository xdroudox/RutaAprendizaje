# Patrones Creacionales

Controlan el proceso de creacion de objetos.

## Singleton

Garantiza una unica instancia de una clase.

```java
public class Configuracion {
    private static Configuracion instancia;
    private Configuracion() {}
    public static Configuracion getInstance() {
        if (instancia == null) instancia = new Configuracion();
        return instancia;
    }
}
```

## Factory Method

Define una interfaz para crear objetos, delegando a subclases.

```java
interface Figura { void dibujar(); }
class Circulo implements Figura { ... }
class FiguraFactory {
    static Figura crear(String tipo) { ... }
}
```

## Builder

Separa la construccion de un objeto complejo de su representacion.

```java
Pizza p = new Pizza.Builder().masa("fina").salsa("tomate").build();
```

## Ejercicios

1. **Singleton - clase Configuracion con instancia unica**
   **Ejecuta:** `python scripts/runner.py 8 1 1`

2. **Factory - crear figuras (Circulo, Cuadrado) segun tipo**
   **Ejecuta:** `python scripts/runner.py 8 1 2`

3. **Builder - construir Pizza con pasos (masa, salsa, ingredientes)**
   **Ejecuta:** `python scripts/runner.py 8 1 3`
