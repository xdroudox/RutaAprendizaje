# Clases y Objetos

## Teoria

### Clase

Una clase es una plantilla o molde que define las caracteristicas (atributos) y comportamientos (metodos) que tendran los objetos creados a partir de ella.

```java
public class Persona {
    // Atributos
    String nombre;
    int edad;

    // Metodos
    void saludar() {
        System.out.println("Hola, soy " + nombre);
    }
}
```

### Objeto

Un objeto es una instancia concreta de una clase. Se crea con la palabra clave `new`.

```java
Persona p = new Persona();
p.nombre = "Ana";
p.edad = 25;
p.saludar();
```

### Constructor

El constructor es un metodo especial que se ejecuta al crear un objeto. Tiene el mismo nombre que la clase y no retorna nada.

```java
public class Persona {
    String nombre;
    int edad;

    // Constructor
    public Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }
}
```

### La palabra clave `this`

`this` hace referencia al objeto actual. Se usa para diferenciar entre parametros y atributos cuando tienen el mismo nombre.

```java
public void setNombre(String nombre) {
    this.nombre = nombre; // this.nombre es el atributo, nombre es el parametro
}
```

### Atributos y Metodos

Los atributos almacenan el estado del objeto. Los metodos definen su comportamiento.

| Componente | Descripcion | Ejemplo |
|------------|-------------|---------|
| Atributo | Variable que guarda datos | `String nombre;` |
| Metodo | Funcion que define comportamiento | `void caminar() { }` |
| Constructor | Metodo que inicializa el objeto | `public Persona() { }` |

## Ejercicios

### Ejercicio 1: Crear clase Persona
Crea una clase Persona con atributos nombre, edad y dni. Incluye un constructor que inicialice los tres atributos y un metodo `mostrarDatos()` que imprima los datos en consola. En el main, crea dos personas y muestra sus datos.

### Ejercicio 2: Clase Rectangulo
Crea una clase Rectangulo con atributos base y altura. Incluye:
- Constructor con parametros
- Metodo `calcularArea()` que retorne el area
- Metodo `calcularPerimetro()` que retorne el perimetro
- Metodo `esCuadrado()` que devuelva true si base == altura

### Ejercicio 3: Clase CuentaBancaria
Crea una clase CuentaBancaria con atributos titular, saldo y numeroCuenta. Incluye:
- Constructor que reciba el titular y genere un numero de cuenta aleatorio
- Metodo `depositar(double cantidad)` que incremente el saldo
- Metodo `retirar(double cantidad)` que decremente el saldo si hay fondos
- Metodo `mostrarInfo()` que muestre los datos de la cuenta

### Ejecuta los ejercicios

```bash
javac Ejercicios.java && java Ejercicios
```
