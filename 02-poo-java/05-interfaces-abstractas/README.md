# Interfaces y Clases Abstractas

## Teoria

### Clase Abstracta

Una clase abstracta no se puede instanciar directamente. Puede tener metodos abstractos (sin implementacion) y metodos concretos (con implementacion). Sirve como base para otras clases.

```java
public abstract class Figura {
    protected String color;

    public Figura(String color) {
        this.color = color;
    }

    // Metodo abstracto - las subclases deben implementarlo
    public abstract double calcularArea();

    // Metodo concreto - todas las subclases lo heredan
    public String getColor() {
        return color;
    }
}
```

### Interface

Una interfaz define un contrato que las clases deben cumplir. Todos sus metodos son abstractos (hasta Java 7). Desde Java 8 pueden tener metodos `default` y `static`.

```java
public interface Volador {
    void volar(); // public abstract implicito
    void aterrizar();
}

public interface Cantante {
    void cantar();

    // Metodo default (Java 8+)
    default void calentarVoz() {
        System.out.println("Calentando la voz...");
    }
}
```

### Diferencia entre Interface y Clase Abstracta

| Caracteristica | Clase Abstracta | Interface |
|----------------|-----------------|-----------|
| Palabra clave | `abstract class` | `interface` |
| Puede tener constructores | Si | No |
| Atributos | Cualquier tipo | public static final |
| Metodos abstractos | Si | Si |
| Metodos concretos | Si | default/static (Java 8+) |
| Herencia multiple | No (extends 1 clase) | Si (implements N interfaces) |

### Implementacion multiple

```java
public class Superheroe implements Volador, Cantante {
    @Override
    public void volar() {
        System.out.println("Volando!");
    }

    @Override
    public void aterrizar() {
        System.out.println("Aterrizando!");
    }

    @Override
    public void cantar() {
        System.out.println("Cantando!");
    }
}
```

## Ejercicios

### Ejercicio 1: Sistema de figuras con interfaz
Crea una interfaz `Dibujable` con metodos `dibujar()` y `cambiarColor(String color)`. Implementala en las clases `Circulo` y `Rectangulo`. Cada una debe tener sus atributos especificos.

### Ejercicio 2: Clase abstracta Animal
Crea una clase abstracta `Animal` con atributo nombre, constructor, metodo concreto `dormir()`, y metodo abstracto `hacerSonido()`. Crea subclases `Perro` y `Gato` que implementen hacerSonido().

### Ejercicio 3: Multiple implementacion
Crea las interfaces `Nadador` (metodo nadar) y `Caminador` (metodo caminar). Crea la clase `Pato` que implemente ambas y ademas tenga un metodo `volar()`. Demuestra el uso en el main.

### Ejecuta los ejercicios

```bash
javac Ejercicios.java && java Ejercicios
```
