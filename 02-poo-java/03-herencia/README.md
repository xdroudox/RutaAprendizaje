# Herencia

## Teoria

La herencia permite que una clase (subclase/hija) herede atributos y metodos de otra clase (superclase/padre). Se usa la palabra clave `extends`.

### Sintaxis basica

```java
// Superclase
public class Animal {
    protected String nombre;
    protected int edad;

    public Animal(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    public void hacerSonido() {
        System.out.println("El animal hace un sonido");
    }
}

// Subclase
public class Perro extends Animal {
    private String raza;

    public Perro(String nombre, int edad, String raza) {
        super(nombre, edad); // Llama al constructor del padre
        this.raza = raza;
    }

    @Override
    public void hacerSonido() {
        System.out.println("Guau guau!");
    }
}
```

### La palabra clave `super`

`super` se usa para:
- Llamar al constructor de la superclase: `super(parametros)`
- Llamar a un metodo de la superclase: `super.metodo()`

### `@Override`

La anotacion `@Override` indica que un metodo esta sobrescribiendo un metodo de la superclase. Es opcional pero recomendada.

### Acceso `protected`

El modificador `protected` permite que las subclases accedan directamente a los miembros de la superclase, incluso si estan en diferentes paquetes.

### Relacion "is-a"

La herencia representa una relacion "es-un" (is-a). Un Perro es un Animal. Si la relacion no es clara, es mejor usar composicion.

```java
// Correcto: un Perro es un Animal
class Perro extends Animal { }

// Incorrecto: un Coche no es una Rueda (usar composicion)
class Coche {
    private Rueda[] ruedas;
}
```

## Ejercicios

### Ejercicio 1: Jerarquia de vehiculos
Crea una clase base `Vehiculo` con atributos: marca, modelo, velocidadMaxima. Metodo `acelerar()` que imprima "El vehiculo acelera". Crea subclases `Coche` y `Moto` que hereden de Vehiculo. Coche anade numPuertas y sobrescribe acelerar(). Moto anade tipoManillar y sobrescribe acelerar().

### Ejercicio 2: Sistema de empleados
Crea una clase base `Empleado` con nombre, salario y metodo `calcularBono()`. Crea subclases:
- `Gerente`: bono del 20% del salario
- `Desarrollador`: bono del 10% del salario
Usa super para llamar al constructor base.

### Ejercicio 3: Figuras geometricas
Crea una clase abstracta `Figura` con metodo `calcularArea()`. Crea subclases `Circulo` y `Rectangulo` que implementen el area. La clase Circulo debe tener el atributo radio, y Rectangulo base y altura.

### Ejecuta los ejercicios

```bash
javac Ejercicios.java && java Ejercicios
```
