# Patrones de Comportamiento

Gestionan algoritmos y responsabilidades entre objetos.

## Observer

Define dependencia uno-a-muchos: cuando un objeto cambia, notifica a todos.

```java
interface Suscriptor { void notificar(String noticia); }
class Editorial {
    private List<Suscriptor> suscriptores = new ArrayList<>();
    public void publicar(String n) {
        for (Suscriptor s : suscriptores) s.notificar(n);
    }
}
```

## Strategy

Familia de algoritmos intercambiables.

```java
interface Estrategia { void ordenar(int[] arr); }
class BubbleSort implements Estrategia { ... }
class Contexto {
    private Estrategia e;
    public void ejecutar(int[] arr) { e.ordenar(arr); }
}
```

## Template Method

Define el esqueleto de un algoritmo, pasos delegados a subclases.

```java
abstract class Procesador {
    public final void procesar() {
        leer(); transformar(); guardar();
    }
}
```

## Ejercicios

1. **Observer - suscriptores reciben noticias de una Editorial**
   **Ejecuta:** `python scripts/runner.py 8 3 1`

2. **Strategy - ordenar lista con diferentes estrategias**
   **Ejecuta:** `python scripts/runner.py 8 3 2`

3. **Template Method - procesar datos con plantilla**
   **Ejecuta:** `python scripts/runner.py 8 3 3`
