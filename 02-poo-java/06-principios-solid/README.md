# Principios SOLID

## Teoria

Los principios SOLID son cinco principios de diseno orientado a objetos que ayudan a crear codigo mantenible y escalable.

### SRP - Single Responsibility Principle

Una clase debe tener una unica razon para cambiar. Cada clase debe tener una sola responsabilidad.

```java
// Mal: Reporte imprime y almacena datos
class Reporte {
    String titulo;
    void imprimir() { ... }
}

// Bien: Separado en dos clases
class Reporte { String titulo; }
class Impresora {
    static void imprimir(Reporte r) { ... }
}
```

### OCP - Open/Closed Principle

Las clases deben estar abiertas para extension pero cerradas para modificacion.

```java
interface Descuento {
    double aplicar(double precio);
}

// Nuevos descuentos se anaden sin modificar codigo existente
class DescuentoPorcentaje implements Descuento { ... }
class DescuentoFijo implements Descuento { ... }
```

### DIP - Dependency Inversion Principle

Depender de abstracciones, no de implementaciones concretas.

```java
interface BaseDatos {
    void guardar(String dato);
}

class Servicio {
    private BaseDatos db; // Depende de la abstraccion, no de una clase concreta
    Servicio(BaseDatos db) { this.db = db; }
}
```

## Ejercicios

### Ejercicio 1: SRP
Separa una clase Reporte en Reporte (datos) e Impresora (impresion).

**Ejecuta:** `python scripts/runner.py 2 6 1`

### Ejercicio 2: OCP
Sistema de descuentos con interface Descuento, abierto a extension.

**Ejecuta:** `python scripts/runner.py 2 6 2`

### Ejercicio 3: DIP
Servicio que depende de interface BaseDatos, no de implementaciones concretas.

**Ejecuta:** `python scripts/runner.py 2 6 3`

## Soluciones

```bash
python scripts/runner.py 2 6 1 -s
python scripts/runner.py 2 6 2 -s
python scripts/runner.py 2 6 3 -s
```
