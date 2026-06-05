# Principios SOLID

## Teoria

SOLID son cinco principios de diseno orientado a objetos que ayudan a crear codigo mantenible, escalable y facil de probar.

### S - Single Responsibility Principle (SRP)

Una clase debe tener una unica responsabilidad. Debe existir una sola razon para cambiar la clase.

```java
// MAL: La clase maneja datos y tambien los persiste
class Empleado {
    private String nombre;
    private double salario;

    public void guardarEnBD() { /* ... */ }
    public void generarReporte() { /* ... */ }
}

// BIEN: Separamos responsabilidades
class Empleado {
    private String nombre;
    private double salario;
}

class EmpleadoRepository {
    public void guardar(Empleado e) { /* ... */ }
}

class ReporteService {
    public void generar(Empleado e) { /* ... */ }
}
```

### O - Open/Closed Principle (OCP)

Las clases deben estar abiertas para extension pero cerradas para modificacion.

```java
// MAL: Hay que modificar la clase para anadir nuevas formas
class CalculadoraArea {
    public double calcular(Object forma) {
        if (forma instanceof Circulo) { /* ... */ }
        else if (forma instanceof Rectangulo) { /* ... */ }
    }
}

// BIEN: Usamos polimorfismo
interface Forma {
    double calcularArea();
}
class Circulo implements Forma { /* ... */ }
class Rectangulo implements Forma { /* ... */ }
```

### L - Liskov Substitution Principle (LSP)

Las subclases deben poder sustituir a su superclase sin alterar el comportamiento del programa.

```java
// MAL: Rectangulo no deberia heredar de Cuadrado
class Cuadrado {
    private int lado;
    public void setLado(int lado) { this.lado = lado; }
}

class Rectangulo extends Cuadrado {
    // Rompe la logica porque un rectangulo necesita base y altura
}

// BIEN: Crear una interfaz Forma
interface Forma { int getArea(); }
class Cuadrado implements Forma { /* ... */ }
class Rectangulo implements Forma { /* ... */ }
```

### I - Interface Segregation Principle (ISP)

Las interfaces deben ser especificas. Mejor varias interfaces pequenas que una grande.

```java
// MAL: Interfaz con metodos que no todas las clases necesitan
interface Trabajador {
    void trabajar();
    void comer();
    void dormir();
}

// BIEN: Interfaces segregadas
interface Trabajador { void trabajar(); }
interface Comedor { void comer(); }
interface Durmiente { void dormir(); }

class Robot implements Trabajador { /* solo trabajar */ }
class Humano implements Trabajador, Comedor, Durmiente { /* todo */ }
```

### D - Dependency Inversion Principle (DIP)

Las clases de alto nivel no deben depender de clases de bajo nivel. Ambas deben depender de abstracciones.

```java
// MAL: Dependencia directa
class ServicioUsuario {
    private MySQLDatabase db = new MySQLDatabase();
}

// BIEN: Dependencia invertida
interface Database { void guardar(); }
class ServicioUsuario {
    private Database db; // Depende de abstraccion
    public ServicioUsuario(Database db) { this.db = db; }
}
class MySQLDatabase implements Database { /* ... */ }
class PostgreSQLDatabase implements Database { /* ... */ }
```

## Ejercicios

### Ejercicio 1: SRP - Refactorizar clase
Dada la siguiente clase que viola SRP, refactorizala en al menos 3 clases separadas:

```java
class Pedido {
    void calcularTotal() { }
    void guardarEnBD() { }
    void enviarEmail() { }
    void imprimirFactura() { }
}
```

### Ejercicio 2: OCP - Sistema de descuentos
Crea un sistema que calcule descuentos para diferentes tipos de clientes (Normal, Premium, VIP) siguiendo el principio Open/Closed. Usa una interfaz o clase abstracta.

### Ejercicio 3: DIP - Sistema de notificaciones
Crea un sistema que pueda enviar notificaciones por email y SMS, siguiendo el principio de Inversion de Dependencias.

### Ejecuta los ejercicios

```bash
javac Ejercicios.java && java Ejercicios
```
