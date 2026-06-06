# Herencia

La **herencia** es un mecanismo que permite crear una clase NUEVA a partir de una EXISTENTE, reutilizando sus atributos y metodos. Es como decir: "un Perro ES UN Animal" o "un Coche ES UN Vehiculo".

---

## 1. TEORIA

### 1.1 El concepto de herencia

En la vida real, las cosas se organizan en categorias: "Un perro es un animal", "Un triangulo es una figura geometrica". La herencia en POO modela esta relacion **"ES UN"**.

- **Superclase / Clase padre**: La clase general (ej: `Animal`)
- **Subclase / Clase hija**: La clase especifica que hereda (ej: `Perro`)

```java
// Superclase: define lo basico
public class Animal {
    void hacerSonido() {
        System.out.println("...");
    }
}

// Subclase: hereda todo de Animal
public class Perro extends Animal {
    // No necesita escribir hacerSonido(), ya lo hereda
}
```

**Explicacion:**

| Codigo | Que hace |
|--------|----------|
| `class Animal { ... }` | Define la superclase. Tiene el metodo `hacerSonido()` |
| `class Perro extends Animal` | `extends` indica que Perro HEREDA de Animal |
| `Perro` | Tiene automaticamente el metodo `hacerSonido()` aunque no lo escriba |

### 1.2 La palabra clave super

`super` se refiere a la clase PADRE. Se usa para:

1. **Llamar al constructor del padre:**
```java
public class Perro extends Animal {
    String raza;

    Perro(String raza) {
        super();  // Llama al constructor de Animal
        this.raza = raza;
    }
}
```

2. **Llamar a un metodo del padre:**
```java
public class Perro extends Animal {
    @Override
    void hacerSonido() {
        super.hacerSonido();  // Llama al metodo del padre
        System.out.println("Guau!");  // + lo que agregamos
    }
}
```

### 1.3 La anotacion @Override

`@Override` le dice a Java: "estoy SOBRESCRIBIENDO un metodo del padre". No es obligatorio, pero es buena practica porque:

- Java verifica que el metodo del padre EXISTA (si no, da error)
- Hace el codigo mas legible: cualquiera sabe que estas sobrescribiendo

```java
public class Perro extends Animal {
    @Override
    void hacerSonido() {
        System.out.println("Guau!");
    }
}
```

**Sin @Override**, si escribes mal el nombre (`hacerRuido()` en vez de `hacerSonido()`), Java trata de crear un metodo nuevo, no sobrescribir. Con `@Override`, Java te avisa del error.

### 1.4 Tipos de herencia

| Tipo | Descripcion | Java lo soporta? |
|------|-------------|------------------|
| **Herencia simple** | Una clase hereda de UNA sola clase | SI (toda herencia en Java es simple) |
| **Herencia multiple** | Una clase hereda de VARIAS clases | NO (Java no lo permite explicitamente) |
| **Herencia multinivel** | Una clase hereda de una que hereda de otra | SI: `Perro extends AnimalTerrestre extends Animal` |
| **Jerarquica** | Varias clases heredan de una misma clase | SI: `Perro extends Animal`, `Gato extends Animal` |

Java NO permite herencia multiple de clases (una clase no puede extender dos clases). Pero se puede lograr algo similar con **interfaces** (proximo tema).

---

## 2. GLOSARIO DEL TEMA

| Termino | Definicion | Ejemplo |
|---------|------------|---------|
| **Herencia** | Mecanismo donde una clase adquiere atributos y metodos de otra | `class Perro extends Animal` |
| **Superclase** | Clase padre, la que presta sus miembros | `Animal` |
| **Subclase** | Clase hija, la que hereda | `Perro` |
| **extends** | Palabra clave para heredar en Java | `class A extends B` |
| **@Override** | Anotacion que indica que sobrescribes un metodo del padre | `@Override void hacerSonido()` |
| **super** | Referencia a la clase padre | `super()` llama al constructor padre |
| **Reutilizacion** | Beneficio de la herencia: no reescribes codigo | El metodo ya existe en el padre |
| **Sobrescritura (override)** | Reescribir un metodo del padre en la hija | Cambiar el comportamiento heredado |

---

## 3. COMPARATIVA ENTRE LENGUAJES

### Herencia simple

| Java | Python | JavaScript |
|------|--------|------------|
| `class Perro extends Animal {` | `class Perro(Animal):` | `class Perro extends Animal {` |
| `    @Override` | `    def hacer_sonido(self):` | `    hacer_sonido() {` |
| `    void hacerSonido() {` | `        super().hacer_sonido()` | `        super.hacer_sonido();` |
| `        super.hacerSonido();` | `        print("Guau!")` | `        console.log("Guau!");` |
| `        System.out.println("Guau!");` | | |
| `    }` | | `    }` |
| `}` | | `}` |

**Diferencias clave:**
- **Java**: Usa `extends`, `@Override`, `super()`, tipos explicitos
- **Python**: Usa `(Animal)` en la definicion, `super().__init__()`, tipado dinamico
- **JavaScript**: Usa `extends`, `super()` (similar a Java, pero sin tipos)

### super()

| Java | Python | JavaScript |
|------|--------|------------|
| `super()` | `super().__init__()` | `super()` |
| `super.metodo()` | `super().metodo()` | `super.metodo()` |

El concepto es identico en los tres: llamar al constructor o metodo del padre.

---

## 4. EJEMPLO GUIADO

### Problema: Sistema de empleados con herencia

> "Crea una clase `Empleado` con atributo `nombre` y metodo `trabajar()`. Luego crea `Programador` que hereda y sobrescribe `trabajar()`, y `Disenador` que tambien hereda."

---

**Paso 1: Analizar**
- Necesitamos 1 superclase (`Empleado`) y 2 subclases (`Programador`, `Disenador`)
- `Empleado` tiene: atributo `nombre`, metodo `trabajar()`
- `Programador`: sobrescribe `trabajar()` para programar
- `Disenador`: sobrescribe `trabajar()` para disenar

**Paso 2: Pseudocodigo (Java)**
```
CLASE Empleado:
    ATRIBUTO: String nombre
    CONSTRUCTOR: Empleado(String nombre) → this.nombre = nombre
    METODO: void trabajar() → print(nombre + " esta trabajando")

CLASE Programador EXTENDS Empleado:
    CONSTRUCTOR: Programador(String nombre) → super(nombre)
    @Override
    METODO: void trabajar() → print(nombre + " esta escribiendo codigo")

CLASE Disenador EXTENDS Empleado:
    CONSTRUCTOR: Disenador(String nombre) → super(nombre)
    @Override
    METODO: void trabajar() → print(nombre + " esta disenando interfaces")

PROGRAMA PRINCIPAL:
    Empleado emp1 = new Programador("Ana")
    Empleado emp2 = new Disenador("Luis")
    emp1.trabajar()  // "Ana esta escribiendo codigo"
    emp2.trabajar()  // "Luis esta disenando interfaces"
```

**Paso 3: Codigo completo**
```java
// Superclase
class Empleado {
    String nombre;

    Empleado(String nombre) {
        this.nombre = nombre;
    }

    void trabajar() {
        System.out.println(nombre + " esta trabajando");
    }
}

// Subclase 1
class Programador extends Empleado {
    Programador(String nombre) {
        super(nombre);  // Llama al constructor de Empleado
    }

    @Override
    void trabajar() {
        System.out.println(nombre + " esta escribiendo codigo");
    }
}

// Subclase 2
class Disenador extends Empleado {
    Disenador(String nombre) {
        super(nombre);
    }

    @Override
    void trabajar() {
        System.out.println(nombre + " esta disenando interfaces");
    }
}

// Programa principal
public class Main {
    public static void main(String[] args) {
        Empleado e1 = new Programador("Ana");
        Empleado e2 = new Disenador("Luis");

        e1.trabajar();  // Polimorfismo: llama al metodo de Programador
        e2.trabajar();  // Polimorfismo: llama al metodo de Disenador
    }
}
```

**Explicacion:**

| Linea | Explicacion |
|-------|-------------|
| `class Programador extends Empleado` | Programador HEREDA de Empleado |
| `super(nombre)` | Llama al constructor de Empleado que recibe String. Si no lo hicieramos, Java intentaria llamar a `super()` (sin args) y daria error |
| `@Override` | Indicamos que sobrescribimos `trabajar()` |
| `Empleado e1 = new Programador(...)` | Variable de tipo `Empleado` pero objeto de tipo `Programador`. TIPO REAL = Programador, TIPO DECLARADO = Empleado |
| `e1.trabajar()` | Aunque `e1` es tipo `Empleado`, el metodo que se ejecuta es el de `Programador`. Esto es **POLIMORFISMO** |

---

## 5. EJERCICIOS

### 🟢 Ejercicio 1: Animal, Perro y Gato (Basico)

Clase `Animal` con metodo `hacerSonido()` que imprime `"..."`. `Perro` y `Gato` heredan y sobrescriben: Perro imprime `"Guau!"`, Gato imprime `"Miau!"`.

**Ejecuta:** `python scripts/runner.py 2 3 1`

---

### 🟡 Ejercicio 2: Vehiculo, Coche y Bicicleta (Intermedio)

Clase `Vehiculo` con atributo `velocidad` (int) y metodo `mover()` que imprime `"El vehiculo se mueve..."`.
`Coche` sobrescribe: `"El coche acelera a X km/h"`.
`Bicicleta` sobrescribe: `"La bicicleta pedalea a X km/h"`.

**Ejecuta:** `python scripts/runner.py 2 3 2`

---

### 🔴 Ejercicio 3: Empleado, Gerente y Vendedor (Avanzado)

Clase `Empleado` con `nombre` y metodo `calcularSalario()` que devuelve `0.0`.
`Gerente` hereda, agrega `bono`, y `calcularSalario()` devuelve `50000 + bono`.
`Vendedor` hereda, agrega `comision`, y `calcularSalario()` devuelve `30000 + comision`.

**Ejecuta:** `python scripts/runner.py 2 3 3`

---

## Soluciones

```bash
python scripts/runner.py 2 3 1 -s
python scripts/runner.py 2 3 2 -s
python scripts/runner.py 2 3 3 -s
```
