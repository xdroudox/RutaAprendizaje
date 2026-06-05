# Clases y Objetos

## Teoria

### Clase

Una clase es una plantilla que define atributos (caracteristicas) y metodos (comportamientos) que tendran los objetos creados a partir de ella.

```java
public class Persona {
    String nombre;
    int edad;

    void saludar() {
        System.out.println("Hola, soy " + nombre);
    }
}
```

### Objeto

Un objeto es una instancia concreta de una clase. Se crea con `new`.

```java
Persona p = new Persona();
p.nombre = "Ana";
p.saludar();
```

### Constructor

Metodo especial que se ejecuta al crear un objeto. Tiene el mismo nombre que la clase.

```java
public Persona(String nombre, int edad) {
    this.nombre = nombre;
    this.edad = edad;
}
```

### this

`this` hace referencia al objeto actual. Se usa para diferenciar parametros de atributos.

```java
public void setNombre(String nombre) {
    this.nombre = nombre;
}
```

### Atributos y Metodos

| Componente | Descripcion | Ejemplo |
|------------|-------------|---------|
| Atributo | Variable que guarda datos | `String nombre;` |
| Metodo | Funcion del objeto | `void caminar() { }` |
| Constructor | Inicializa el objeto | `public Persona() { }` |

## Ejercicios

### Ejercicio 1: Clase Persona
Crea una clase Persona con atributos nombre y edad. Incluye constructor y metodo `mostrarDatos()`.

**Ejecuta:** `python scripts/runner.py 2 1 1`

### Ejercicio 2: Clase Rectangulo
Crea una clase Rectangulo con base y altura. Incluye constructor y metodo `area()`.

**Ejecuta:** `python scripts/runner.py 2 1 2`

### Ejercicio 3: Clase Libro
Crea una clase Libro con titulo, autor y paginas. Incluye metodo `esLargo()` (>300 pag).

**Ejecuta:** `python scripts/runner.py 2 1 3`

## Soluciones

```bash
python scripts/runner.py 2 1 1 -s
python scripts/runner.py 2 1 2 -s
python scripts/runner.py 2 1 3 -s
```
