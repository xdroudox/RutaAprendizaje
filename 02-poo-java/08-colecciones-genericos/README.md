# Colecciones y Genericos

## Teoria

### Colecciones

Las colecciones son estructuras de datos que almacenan y manipulan grupos de objetos.

#### ArrayList

Lista redimensionable que permite elementos duplicados.

```java
import java.util.ArrayList;

ArrayList<String> nombres = new ArrayList<>();
nombres.add("Ana");
nombres.add("Luis");
System.out.println(nombres.get(0)); // Ana
System.out.println(nombres.size()); // 2
```

#### HashMap

Estructura que almacena pares clave-valor. Las claves son unicas.

```java
import java.util.HashMap;
import java.util.Map;

HashMap<String, Integer> agenda = new HashMap<>();
agenda.put("Ana", 123456789);
System.out.println(agenda.get("Ana"));

for (Map.Entry<String, Integer> e : agenda.entrySet()) {
    System.out.println(e.getKey() + ": " + e.getValue());
}
```

### Genericos (<T>)

Los genericos permiten crear clases, interfaces y metodos que trabajan con tipos parametrizados.

```java
class Caja<T> {
    private T contenido;

    public void guardar(T contenido) {
        this.contenido = contenido;
    }

    public T obtener() {
        return contenido;
    }
}

Caja<String> caja = new Caja<>();
caja.guardar("Hola");
String texto = caja.obtener();
```

## Ejercicios

### Ejercicio 1: ArrayList de nombres
Crea un ArrayList<String>, agrega nombres y muestralos.

**Ejecuta:** `python scripts/runner.py 2 8 1`

### Ejercicio 2: HashMap agenda telefonica
Crea una agenda con HashMap<String, Integer> y recorrela.

**Ejecuta:** `python scripts/runner.py 2 8 2`

### Ejercicio 3: Clase generica Caja<T>
Crea una clase generica que guarde y devuelva cualquier tipo.

**Ejecuta:** `python scripts/runner.py 2 8 3`

## Soluciones

```bash
python scripts/runner.py 2 8 1 -s
python scripts/runner.py 2 8 2 -s
python scripts/runner.py 2 8 3 -s
```
