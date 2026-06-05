# Polimorfismo

## Teoria

El polimorfismo permite que objetos de diferentes clases respondan al mismo mensaje de formas distintas. En Java hay dos tipos principales: sobrecarga (compile-time) y sobrescritura (runtime).

### Sobrecarga (Overloading)

Varios metodos con el mismo nombre pero diferentes parametros (tipo, numero u orden). Se resuelve en tiempo de compilacion.

```java
public class Calculadora {
    public int sumar(int a, int b) {
        return a + b;
    }

    public double sumar(double a, double b) {
        return a + b;
    }

    public int sumar(int a, int b, int c) {
        return a + b + c;
    }
}
```

### Sobrescritura (Overriding)

Una subclase redefine un metodo heredado. Se resuelve en tiempo de ejecucion (dynamic dispatch).

```java
class Animal {
    void saludar() { System.out.println("Hola"); }
}

class Perro extends Animal {
    @Override
    void saludar() { System.out.println("Guau"); }
}

class Gato extends Animal {
    @Override
    void saludar() { System.out.println("Miau"); }
}
```

### Dynamic Dispatch

En tiempo de ejecucion, Java determina que metodo ejecutar basado en el tipo real del objeto, no el tipo de la referencia.

```java
Animal a = new Perro();
a.saludar(); // Imprime "Guau" (no "Hola")
```

### Polimorfismo con Arrays y Parametros

```java
Animal[] animales = { new Perro(), new Gato(), new Perro() };
for (Animal a : animales) {
    a.saludar(); // Cada uno hace su sonido
}

void hacerSaludar(Animal a) {
    a.saludar();
}
```

## Ejercicios

### Ejercicio 1: Sobrecarga de metodos
Crea una clase `Impresora` con metodos `imprimir` sobrecargados:
- `imprimir(String texto)` - imprime texto
- `imprimir(int numero)` - imprime el numero
- `imprimir(String texto, int veces)` - imprime el texto N veces
- `imprimir(int[] numeros)` - imprime todos los numeros del array

### Ejercicio 2: Polimorfismo con animales
Crea una clase base `Animal` con metodo `hacerSonido()`. Crea subclases `Perro`, `Gato` y `Vaca` que sobrescriban el metodo. En el main, crea un array de Animal y usa un bucle para que cada uno haga su sonido.

### Ejercicio 3: Sistema de pagos
Crea una interfaz `Pagable` con metodo `double calcularPago()`. Implementala en clases `Factura` (monto fijo) y `Empleado` (salario * horas). Usa polimorfismo para procesar una lista de pagables.

### Ejecuta los ejercicios

```bash
javac Ejercicios.java && java Ejercicios
```
