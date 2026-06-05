# Colecciones y Genericos

## Teoria

### Generics

Los genericos permiten crear clases, interfaces y metodos que operan con tipos parametrizados. Proporcionan seguridad de tipos en tiempo de compilacion.

```java
// Clase generica
public class Caja<T> {
    private T contenido;

    public void guardar(T contenido) {
        this.contenido = contenido;
    }

    public T obtener() {
        return contenido;
    }
}

// Uso
Caja<String> cajaString = new Caja<>();
cajaString.guardar("Hola");
String texto = cajaString.obtener();
```

### Metodo generico

```java
public static <T> void imprimirArray(T[] array) {
    for (T elemento : array) {
        System.out.println(elemento);
    }
}
```

### Wildcards

```java
List<?> listaComodin;          // cualquier tipo
List<? extends Number> nums;   // Number o subclases
List<? super Integer> enteros; // Integer o superclases
```

### Colecciones principales

```java
import java.util.*;

// List: permite duplicados, ordenada
List<String> lista = new ArrayList<>();
lista.add("Java");
lista.add("Python");
lista.get(0); // "Java"

// Set: no permite duplicados
Set<String> conjunto = new HashSet<>();
conjunto.add("A");
conjunto.add("B");
conjunto.add("A"); // Ignorado

// Map: clave-valor
Map<String, Integer> mapa = new HashMap<>();
mapa.put("Juan", 25);
mapa.put("Ana", 30);
mapa.get("Juan"); // 25
```

### Colecciones - Metodos utiles

```java
Collections.sort(lista);             // Ordenar
Collections.reverse(lista);          // Invertir
Collections.shuffle(lista);          // Aleatorizar
Collections.max(lista);              // Maximo
Collections.min(lista);              // Minimo
Collections.frequency(lista, "A");   // Frecuencia
Collections.disjoint(lista1, lista2); // Sin elementos en comun
```

### Iteracion

```java
// for-each
for (String s : lista) {
    System.out.println(s);
}

// forEach con lambda (Java 8+)
lista.forEach(s -> System.out.println(s));
lista.forEach(System.out::println);

// Map entry
for (Map.Entry<String, Integer> entry : mapa.entrySet()) {
    System.out.println(entry.getKey() + ": " + entry.getValue());
}
```

## Ejercicios

### Ejercicio 1: ArrayList de estudiantes
Crea un programa que gestione una lista de estudiantes. Cada estudiante tiene nombre y nota. Usa ArrayList para almacenarlos. Implementa: agregar, listar, calcular promedio, mostrar el de mayor nota.

### Ejercicio 2: HashMap de contactos
Crea una agenda telefonica usando HashMap<String, String> (nombre -> telefono). Implementa: anadir contacto, buscar por nombre, eliminar contacto, listar todos.

### Ejercicio 3: Clase generica Par
Crea una clase generica `Par<K, V>` que almacene un par clave-valor. Incluye metodos getClave(), getValor(), setClave(), setValor(). En el main, crea un Par<String, Integer> y un Par<Integer, String>.

### Ejecuta los ejercicios

```bash
javac Ejercicios.java && java Ejercicios
```
