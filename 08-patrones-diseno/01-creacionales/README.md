# Patrones Creacionales

Los patrones creacionales abstraen el proceso de instanciacion de objetos, haciendo un sistema independiente de como sus objetos son creados, compuestos y representados.

## Singleton

**Intencion:** Garantizar que una clase tenga una unica instancia y proporcionar un punto de acceso global a ella.

**Problema:** Necesitamos una unica instancia compartida de un recurso (logger, configuracion, pool de conexiones) y controlar el acceso concurrente.

**Estructura:**
- Una clase con constructor privado
- Un campo estatico privado que almacena la unica instancia
- Un metodo estatico publico que devuelve la instancia

**Cuando usar:**
- Cuando necesites exactamente una instancia de una clase
- Cuando el control de acceso a un recurso compartido sea necesario

**Ejemplo:**
```java
public class Logger {
    private static Logger instancia;
    private Logger() {}
    public static synchronized Logger getInstance() {
        if (instancia == null) {
            instancia = new Logger();
        }
        return instancia;
    }
    public void log(String mensaje) {
        System.out.println("[LOG] " + mensaje);
    }
}
```

## Factory Method

**Intencion:** Definir una interfaz para crear un objeto, pero dejar que las subclases decidan que clase instanciar.

**Problema:** Una clase no puede anticipar la clase de objetos que debe crear.

**Estructura:**
- Producto (interfaz o clase abstracta)
- Productos Concretos (implementaciones)
- Creador (declara el factory method)
- Creadores Concretos (implementan el factory method)

**Cuando usar:**
- Cuando una clase no conoce por adelantado la clase exacta de objetos que debe crear
- Cuando delegas la responsabilidad de creacion a subclases

**Ejemplo:**
```java
interface Figura { void dibujar(); }
class Circulo implements Figura {
    public void dibujar() { System.out.println("Dibujando circulo"); }
}
class Cuadrado implements Figura {
    public void dibujar() { System.out.println("Dibujando cuadrado"); }
}
class FiguraFactory {
    public static Figura crearFigura(String tipo) {
        if (tipo.equals("circulo")) return new Circulo();
        if (tipo.equals("cuadrado")) return new Cuadrado();
        throw new IllegalArgumentException("Tipo desconocido");
    }
}
```

## Builder

**Intencion:** Separar la construccion de un objeto complejo de su representacion, permitiendo el mismo proceso de construccion crear diferentes representaciones.

**Problema:** Una clase tiene muchos atributos opcionales y constructores telescopicos.

**Estructura:**
- Builder (interfaz con metodos para construir partes)
- ConcreteBuilder (implementa los metodos)
- Director (construye usando el builder)
- Producto (el objeto final)

**Cuando usar:**
- Cuando un objeto tiene muchos parametros opcionales
- Cuando quieres construir objetos inmutables con configuracion flexible

**Ejemplo:**
```java
class Computadora {
    private String cpu; private int ram; private int almacenamiento;
    private Computadora(Builder b) {
        this.cpu = b.cpu; this.ram = b.ram; this.almacenamiento = b.almacenamiento;
    }
    static class Builder {
        private String cpu = "i5"; private int ram = 8; private int almacenamiento = 256;
        Builder cpu(String c) { this.cpu = c; return this; }
        Builder ram(int r) { this.ram = r; return this; }
        Builder almacenamiento(int a) { this.almacenamiento = a; return this; }
        Computadora build() { return new Computadora(this); }
    }
}
```

## Ejecuta

```
javac Ejercicios.java && java Ejercicios 1
javac Ejercicios.java && java Ejercicios 1 -p   (pista)
javac Ejercicios.java && java Ejercicios -s 1   (solucion)
```
