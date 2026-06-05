# Patrones de Comportamiento

Los patrones de comportamiento se centran en algoritmos y la asignacion de responsabilidades entre objetos.

## Observer

**Intencion:** Definir una dependencia de uno-a-muchos entre objetos, de modo que cuando un objeto cambie su estado, todos sus dependientes sean notificados y actualizados automaticamente.

**Problema:** Necesitas notificar cambios a multiples objetos sin acoplarlos fuertemente al emisor.

**Estructura:**
- Subject (mantiene lista de observers, provee metodos para registrar/eliminar)
- Observer (interfaz con metodo update())
- ConcreteSubject (estado concreto, notifica cambios)
- ConcreteObservers (reaccionan a las notificaciones)

**Cuando usar:**
- Cuando un cambio en un objeto requiere cambiar otros, y no sabes cuantos objetos deben cambiar
- Cuando un objeto debe notificar a otros sin hacer suposiciones sobre quienes son

**Ejemplo:**
```java
interface Observer { void update(String mensaje); }
class Subject {
    private List<Observer> observers = new ArrayList<>();
    public void addObserver(Observer o) { observers.add(o); }
    public void notifyObservers(String msg) {
        for (Observer o : observers) o.update(msg);
    }
}
```

## Strategy

**Intencion:** Definir una familia de algoritmos, encapsular cada uno, y hacerlos intercambiables. Permite que el algoritmo varie independientemente de los clientes que lo usan.

**Problema:** Tienes multiples variantes de un algoritmo y quieres evitar condicionales extensos.

**Estructura:**
- Strategy (interfaz comun para algoritmos)
- ConcreteStrategies (implementaciones del algoritmo)
- Context (mantiene referencia a Strategy y delega)

**Cuando usar:**
- Cuando tienes muchas clases relacionadas que solo difieren en su comportamiento
- Cuando necesitas diferentes variantes de un algoritmo

**Ejemplo:**
```java
interface Ordenamiento { void ordenar(int[] arr); }
class BubbleSort implements Ordenamiento {
    public void ordenar(int[] arr) { /* bubble sort */ }
}
class QuickSort implements Ordenamiento {
    public void ordenar(int[] arr) { /* quick sort */ }
}
class Contexto {
    private Ordenamiento strategy;
    public void setStrategy(Ordenamiento s) { this.strategy = s; }
    public void ejecutar(int[] arr) { strategy.ordenar(arr); }
}
```

## Template Method

**Intencion:** Definir el esqueleto de un algoritmo en una operacion, postergando algunos pasos a las subclases. Permite que subclases redefinan ciertos pasos sin cambiar la estructura del algoritmo.

**Problema:** Dos clases tienen algoritmos similares que solo varian en algunos pasos.

**Estructura:**
- AbstractClass (define el template method con pasos fijos y abstractos)
- ConcreteClass (implementa los pasos abstractos)

**Cuando usar:**
- Cuando varias clases comparten el mismo algoritmo pero con variaciones en algunos pasos
- Para evitar duplicacion de codigo

**Ejemplo:**
```java
abstract class ProcesadorDatos {
    public final void procesar() {
        leerDatos();
        transformar();
        guardar();
    }
    abstract void leerDatos();
    abstract void transformar();
    void guardar() { System.out.println("Guardando..."); }
}
```

## Ejecuta

```
javac Ejercicios.java && java Ejercicios 1
javac Ejercicios.java && java Ejercicios 1 -p
javac Ejercicios.java && java Ejercicios -s 1
```
