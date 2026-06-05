# Interfaces y Clases Abstractas

## Teoria

### Interface

Una interface es un contrato que define metodos abstractos (sin implementacion). Las clases que la implementan deben proporcionar el codigo.

```java
interface Volador {
    void volar();
}

class Pajaro implements Volador {
    public void volar() {
        System.out.println("El pajaro vuela");
    }
}
```

### Clase Abstracta

Una clase abstracta no puede instanciarse directamente. Puede tener metodos abstractos (sin cuerpo) y metodos concretos (con implementacion).

```java
abstract class Forma {
    abstract double area();

    void info() {
        System.out.println("Soy una forma");
    }
}
```

### Diferencias

| Caracteristica | Interface | Clase Abstracta |
|---------------|-----------|-----------------|
| Instanciacion | No | No |
| Metodos abstractos | Si | Si |
| Metodos concretos | default (Java 8+) | Si |
| Atributos | static final | Puede tener atributos |
| Herencia multiple | Una clase puede implementar varias interfaces | Una clase solo puede extender una clase abstracta |

## Ejercicios

### Ejercicio 1: Interface Volador
Crea una interface Volador con metodo volar(). Implementa en Pajaro y Avion.

**Ejecuta:** `python scripts/runner.py 2 5 1`

### Ejercicio 2: Clase abstracta Forma
Crea una clase abstracta Forma con area() abstracto e info() concreto.

**Ejecuta:** `python scripts/runner.py 2 5 2`

### Ejercicio 3: Interface Reproducible
Crea una interface Reproducible con metodo reproducir(). Implementa en Musica y Video.

**Ejecuta:** `python scripts/runner.py 2 5 3`

## Soluciones

```bash
python scripts/runner.py 2 5 1 -s
python scripts/runner.py 2 5 2 -s
python scripts/runner.py 2 5 3 -s
```
