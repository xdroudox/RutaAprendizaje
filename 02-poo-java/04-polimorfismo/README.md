# Polimorfismo

## Teoria

El polimorfismo permite que un mismo metodo tenga diferentes comportamientos segun el contexto.

### Sobrecarga (Overloading)

Varios metodos con el mismo nombre pero distintos parametros (numero o tipo).

```java
public class Calculadora {
    int sumar(int a, int b) {
        return a + b;
    }

    int sumar(int a, int b, int c) {
        return a + b + c;
    }
}
```

### Sobrescritura (Overriding)

Una subclase redefine un metodo de la superclase.

```java
public class Animal {
    void hacerSonido() { System.out.println("..."); }
}

public class Perro extends Animal {
    @Override
    void hacerSonido() { System.out.println("Guau!"); }
}
```

### Dynamic Dispatch

Cuando se llama a un metodo sobre una variable de tipo padre, Java ejecuta el metodo del tipo real del objeto.

```java
Animal a = new Perro();
a.hacerSonido(); // Imprime "Guau!" (no "...")
```

## Ejercicios

### Ejercicio 1: Sobrecarga de sumar()
Crea una Calculadora con dos versiones de sumar() (2 y 3 parametros).

**Ejecuta:** `python scripts/runner.py 2 4 1`

### Ejercicio 2: Array polimorfico de Animales
Usa un array Animal[] con Perro y Gato para demostrar dynamic dispatch.

**Ejecuta:** `python scripts/runner.py 2 4 2`

### Ejercicio 3: Figura, Circulo y Rectangulo
Clase Figura con area(). Circulo y Rectangulo heredan y sobrescriben.

**Ejecuta:** `python scripts/runner.py 2 4 3`

## Soluciones

```bash
python scripts/runner.py 2 4 1 -s
python scripts/runner.py 2 4 2 -s
python scripts/runner.py 2 4 3 -s
```
