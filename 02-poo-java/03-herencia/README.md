# Herencia

## Teoria

La herencia permite crear una clase nueva a partir de una existente, reutilizando sus atributos y metodos. La clase existente se llama padre o superclase. La nueva se llama hija o subclase.

### extends

La palabra clave `extends` indica que una clase hereda de otra.

```java
public class Animal {
    void hacerSonido() {
        System.out.println("...");
    }
}

public class Perro extends Animal {
    // Hereda hacerSonido()
}
```

### super

`super` hace referencia a la clase padre. Se usa para llamar al constructor o metodos del padre.

```java
public class Perro extends Animal {
    String raza;

    Perro(String raza) {
        super(); // llama al constructor de Animal
        this.raza = raza;
    }
}
```

### @Override

La anotacion `@Override` indica que un metodo esta sobrescribiendo un metodo de la clase padre.

```java
public class Perro extends Animal {
    @Override
    void hacerSonido() {
        System.out.println("Guau!");
    }
}
```

## Ejercicios

### Ejercicio 1: Animal, Perro y Gato
Clase Animal con metodo hacerSonido(). Perro y Gato heredan y sobrescriben.

**Ejecuta:** `python scripts/runner.py 2 3 1`

### Ejercicio 2: Vehiculo, Coche y Bicicleta
Clase Vehiculo con mover(). Coche y Bicicleta heredan y personalizan.

**Ejecuta:** `python scripts/runner.py 2 3 2`

### Ejercicio 3: Empleado, Gerente y Vendedor
Clase Empleado con calcularSalario(). Gerente y Vendedor heredan y sobrescriben.

**Ejecuta:** `python scripts/runner.py 2 3 3`

## Soluciones

```bash
python scripts/runner.py 2 3 1 -s
python scripts/runner.py 2 3 2 -s
python scripts/runner.py 2 3 3 -s
```
