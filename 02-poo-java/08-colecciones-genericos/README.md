# Colecciones y Genericos

Las **colecciones** son estructuras de datos que almacenan y manipulan grupos de objetos. Los **genericos** permiten crear codigo que funciona con cualquier tipo de dato.

---

## 1. TEORIA

### 1.1 El problema: Arrays de tamaño fijo

Los arrays tradicionales tienen un TAMAÑO FIJO:

```java
String[] nombres = new String[3];  // Solo 3 espacios!
nombres[0] = "Ana";
nombres[1] = "Luis";
nombres[2] = "Carlos";
nombres[3] = "Marta";  // ERROR: ArrayIndexOutOfBoundsException!
```

Las colecciones resuelven esto: son REDIMENSIONABLES.

### 1.2 ArrayList

`ArrayList` es una lista redimensionable. Puedes agregar y quitar elementos DINAMICAMENTE.

```java
import java.util.ArrayList;

ArrayList<String> nombres = new ArrayList<>();

// Agregar elementos
nombres.add("Ana");
nombres.add("Luis");
nombres.add("Carlos");

// Obtener elementos
System.out.println(nombres.get(0));  // "Ana"

// Tamaño actual
System.out.println(nombres.size());  // 3

// Recorrer con for-each
for (String n : nombres) {
    System.out.println(n);
}

// Eliminar
nombres.remove(1);  // Elimina "Luis" (indice 1)
nombres.remove("Carlos");  // Elimina por objeto
```

**Explicacion:**

| Codigo | Que hace |
|--------|----------|
| `ArrayList<String>` | Lista de Strings. El `<String>` es el GENERICO: indica que tipo guarda |
| `new ArrayList<>()` | Crea una lista VACIA. El `<>` (diamond) infiere el tipo |
| `add("Ana")` | Agrega al FINAL de la lista |
| `get(0)` | Obtiene el elemento en el INDICE 0 |
| `size()` | Cantidad de elementos actual (no confundir con length de arrays) |
| `remove(1)` | Elimina el elemento en el indice 1 |

**ArrayList vs Array:**

| Caracteristica | Array | ArrayList |
|----------------|-------|-----------|
| Tamaño | Fijo | Redimensionable |
| Sintaxis | `new String[3]` | `new ArrayList<>()` |
| Acceso | `arr[0]` | `lista.get(0)` |
| Agregar | No se puede | `add(elemento)` |
| Eliminar | No se puede | `remove(indice)` |
| Tipo | Nativo | Clase (solo objetos, no primitivos) |

> **Nota:** Para tipos primitivos (int, double...), usa clases wrapper: `ArrayList<Integer>`, `ArrayList<Double>`. Java convierte automaticamente (autoboxing).

### 1.3 HashMap

`HashMap` almacena pares **clave-valor**. Como un diccionario: buscas por palabra (clave) y obtienes la definicion (valor).

```java
import java.util.HashMap;
import java.util.Map;

HashMap<String, Integer> agenda = new HashMap<>();

// Agregar pares clave-valor
agenda.put("Ana", 123456789);
agenda.put("Luis", 987654321);

// Obtener valor por clave
System.out.println(agenda.get("Ana"));     // 123456789
System.out.println(agenda.get("Pedro"));   // null (no existe)

// Verificar si existe una clave
if (agenda.containsKey("Ana")) {
    System.out.println("Ana existe en la agenda");
}

// Recorrer todas las entradas
for (Map.Entry<String, Integer> entrada : agenda.entrySet()) {
    String nombre = entrada.getKey();
    Integer telefono = entrada.getValue();
    System.out.println(nombre + ": " + telefono);
}
```

**Explicacion:**

| Codigo | Que hace |
|--------|----------|
| `HashMap<String, Integer>` | Clave = String, Valor = Integer |
| `put("Ana", 123456789)` | Agrega o actualiza la clave "Ana" con valor 123456789 |
| `get("Ana")` | Devuelve el valor asociado a "Ana" |
| `containsKey("Ana")` | Verifica si la clave existe (devuelve boolean) |
| `entrySet()` | Devuelve todas las entradas como pares clave-valor |
| `Map.Entry<String, Integer>` | Tipo de cada entrada: tiene getKey() y getValue() |

**Las claves son UNICAS:** Si haces `put("Ana", 555)` cuando "Ana" ya existe, se SOBREESCRIBE el valor.

### 1.4 Genericos <T>

Los **genericos** permiten crear clases, interfaces y metodos que trabajan con UN TIPO ESPECIFICO pero sin definirlo hasta que se usan.

```java
// Definicion de una clase generica
class Caja<T> {
    private T contenido;  // T es un tipo placeholder

    public void guardar(T contenido) {
        this.contenido = contenido;
    }

    public T obtener() {
        return contenido;
    }
}

// Uso con diferentes tipos
Caja<String> cajaString = new Caja<>();
cajaString.guardar("Hola");
String texto = cajaString.obtener();  // No necesita casting!

Caja<Integer> cajaInt = new Caja<>();
cajaInt.guardar(42);
int numero = cajaInt.obtener();  // No necesita casting!
```

**Explicacion:**

| Codigo | Que hace |
|--------|----------|
| `class Caja<T>` | `T` es un parametro de tipo. Se reemplazara por un tipo real al usar la clase |
| `private T contenido` | El atributo es del tipo que se defina al instanciar |
| `Caja<String>` | T = String. La caja solo guarda Strings |
| `cajaString.obtener()` | Devuelve String directamente, SIN hacer casting |
| `Caja<Integer>` | T = Integer. La caja solo guarda Integers |

**Ventajas de los genericos:**
1. **Seguridad de tipos**: El compilador verifica que usas el tipo correcto
2. **Sin casting**: No necesitas convertir el resultado
3. **Reutilizacion**: Una sola clase funciona con cualquier tipo

---

## 2. GLOSARIO DEL TEMA

| Termino | Definicion | Ejemplo |
|---------|------------|---------|
| **Coleccion** | Estructura de datos que almacena grupos de objetos | `ArrayList`, `HashMap` |
| **ArrayList** | Lista redimensionable | `ArrayList<String> lista = new ArrayList<>()` |
| **HashMap** | Mapa clave-valor | `HashMap<String, Integer> mapa = new HashMap<>()` |
| **Generico** | Parametro de tipo que permite reutilizar codigo | `class Caja<T> { ... }` |
| **T (Type)** | Identificador comun para parametro de tipo generico | `class Caja<T>` |
| **Autoboxing** | Conversion automatica de primitivo a wrapper | `int` -> `Integer` |
| **Wrapper** | Clase que envuelve un tipo primitivo | `Integer`, `Double`, `Boolean` |
| **entrySet()** | Metodo que devuelve todas las entradas de un mapa | `mapa.entrySet()` |
| **keySet()** | Metodo que devuelve todas las claves de un mapa | `mapa.keySet()` |

---

## 3. COMPARATIVA ENTRE LENGUAJES

### Listas

| Operacion | Java | Python | JavaScript |
|-----------|------|--------|------------|
| Crear | `new ArrayList<String>()` | `[]` | `[]` |
| Agregar | `lista.add("x")` | `lista.append("x")` | `lista.push("x")` |
| Acceder | `lista.get(0)` | `lista[0]` | `lista[0]` |
| Tamaño | `lista.size()` | `len(lista)` | `lista.length` |

### Mapas / Diccionarios

| Operacion | Java | Python | JavaScript |
|-----------|------|--------|------------|
| Crear | `new HashMap<>()` | `{}` | `{}` |
| Asignar | `mapa.put("k", 1)` | `mapa["k"] = 1` | `mapa["k"] = 1` |
| Obtener | `mapa.get("k")` | `mapa["k"]` | `mapa["k"]` |
| Recorrer | `mapa.entrySet()` | `mapa.items()` | `Object.entries(mapa)` |

### Genericos

| Java | Python | JavaScript |
|------|--------|------------|
| `class Caja<T>` | `from typing import TypeVar` | No tiene genericos nativos |
| `Caja<String> c = new Caja<>()` | `T = TypeVar('T')` | Se usa TypeScript para esto |
| Seguridad en COMPILACION | Tipado DINAMICO | Tipado DINAMICO |

---

## 4. EJEMPLO GUIADO

### Problema: Sistema de inventario con colecciones

> "Crea un sistema de inventario usando un `HashMap<String, Integer>` donde las claves son nombres de productos y los valores son cantidades. Agrega productos, actualiza cantidades y muestra el inventario."

---

**Paso 1: Analizar**
- HashMap<String, Integer> para producto -> cantidad
- Agregar 3 productos
- Actualizar cantidad de uno
- Mostrar todo el inventario

**Paso 2: Pseudocodigo**
```
HashMap<String, Integer> inventario = new HashMap<>()
inventario.put("Manzanas", 50)
inventario.put("Naranjas", 30)
inventario.put("Peras", 20)

inventario.put("Manzanas", 45)  // Actualizar (sobrescribe)

PARA CADA entrada EN inventario.entrySet():
    imprimir entrada.getKey() + ": " + entrada.getValue()
```

**Paso 3: Codigo completo**
```java
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        HashMap<String, Integer> inventario = new HashMap<>();

        // Agregar productos
        inventario.put("Manzanas", 50);
        inventario.put("Naranjas", 30);
        inventario.put("Peras", 20);

        // Actualizar cantidad (sobrescribe el valor anterior)
        inventario.put("Manzanas", 45);

        // Mostrar inventario
        System.out.println("=== INVENTARIO ===");
        for (Map.Entry<String, Integer> entrada : inventario.entrySet()) {
            System.out.println(entrada.getKey() + ": " + entrada.getValue());
        }

        // Verificar existencia
        String producto = "Uvas";
        if (inventario.containsKey(producto)) {
            System.out.println(producto + " existe en el inventario");
        } else {
            System.out.println(producto + " NO existe en el inventario");
        }
    }
}
```

**Explicacion:**

| Linea | Explicacion |
|-------|-------------|
| `HashMap<String, Integer>` | Clave: String (nombre producto), Valor: Integer (cantidad) |
| `put("Manzanas", 50)` | Crea la entrada Manzanas = 50 |
| `put("Manzanas", 45)` | SOBREESCRIBE: ahora Manzanas = 45 |
| `entrySet()` | Devuelve TODAS las entradas del mapa |
| `entrada.getKey()` | Obtiene la clave de esa entrada ("Manzanas") |
| `entrada.getValue()` | Obtiene el valor de esa entrada (45) |
| `containsKey("Uvas")` | Verifica si la clave existe. Devuelve false |

**Paso 4: Probar**
```
$ java Main
=== INVENTARIO ===
Manzanas: 45
Naranjas: 30
Peras: 20
Uvas NO existe en el inventario
```

---

## 5. EJERCICIOS

### 🟢 Ejercicio 1: ArrayList de nombres (Basico)

Crea un `ArrayList<String>` de nombres. Agrega 4 nombres con `add()`. Muestra todos con un bucle for-each y el tamaño con `size()`.

**Ejecuta:** `python scripts/runner.py 2 8 1`

---

### 🟡 Ejercicio 2: HashMap agenda telefonica (Intermedio)

Crea un `HashMap<String, Integer>` para una agenda telefonica. Agrega 3 contactos. Muestra el telefono de un contacto con `get()`. Recorre el mapa mostrando todos los contactos.

**Ejecuta:** `python scripts/runner.py 2 8 2`

---

### 🔴 Ejercicio 3: Clase generica Caja<T> (Avanzado)

Crea una clase generica `Caja<T>` que pueda guardar cualquier tipo. Incluye `guardar(T)` y `T obtener()`. En el main, crea una `Caja<String>` y una `Caja<Integer>` y usalas.

**Ejecuta:** `python scripts/runner.py 2 8 3`

---

## Soluciones

```bash
python scripts/runner.py 2 8 1 -s
python scripts/runner.py 2 8 2 -s
python scripts/runner.py 2 8 3 -s
```
