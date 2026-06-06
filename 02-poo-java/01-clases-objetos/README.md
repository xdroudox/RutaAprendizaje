# Clases y Objetos

Las **clases** son las plantillas para crear objetos, y los **objetos** son las instancias concretas de esas plantillas. Es el concepto FUNDAMENTAL de la Programacion Orientada a Objetos.

---

## 1. TEORIA

### 1.1 Clase

Una **clase** es como un molde o plantilla. Define que atributos (datos) y que metodos (comportamientos) tendran los objetos creados a partir de ella.

```java
// Definicion de una clase
public class Persona {
    // Atributos (caracteristicas)
    String nombre;
    int edad;

    // Metodo (comportamiento)
    void saludar() {
        System.out.println("Hola, soy " + nombre);
    }
}
```

**Explicacion:**

| Codigo | Que hace |
|--------|----------|
| `public class Persona {` | Define una clase llamada Persona. `public` significa que es accesible desde cualquier parte |
| `String nombre;` | Declara un ATRIBUTO de tipo String. Cada Persona tendra su propio nombre |
| `int edad;` | Otro atributo, de tipo entero |
| `void saludar() { ... }` | Declara un METODO. `void` significa que no devuelve valor |
| `System.out.println(...)` | Imprime en consola. Usa la variable `nombre` del objeto actual |

> **Nota:** En Java, el nombre del archivo DEBE coincidir con el nombre de la clase publica. `Persona` debe estar en `Persona.java`.

### 1.2 Objeto

Un **objeto** es una INSTANCIA CONCRETA de una clase. Ocupa memoria y tiene valores especificos en sus atributos.

```java
// Crear (instanciar) un objeto
Persona persona1 = new Persona();

// Asignar valores a sus atributos
persona1.nombre = "Ana";
persona1.edad = 25;

// Llamar a sus metodos
persona1.saludar();  // Imprime: Hola, soy Ana
```

**Explicacion:**

| Codigo | Que hace |
|--------|----------|
| `Persona persona1` | Declara una variable de tipo `Persona` |
| `new Persona()` | Crea el objeto en memoria y devuelve su direccion (referencia) |
| `=` | Asigna esa referencia a `persona1` |
| `persona1.nombre = "Ana"` | Accede al atributo `nombre` del objeto y le asigna "Ana" |
| `persona1.saludar()` | Ejecuta el metodo `saludar()` en ese objeto especifico |

**Multiples objetos:**

```java
Persona p1 = new Persona();
p1.nombre = "Ana";
p1.edad = 25;

Persona p2 = new Persona();
p2.nombre = "Luis";
p2.edad = 30;

p1.saludar();  // Hola, soy Ana
p2.saludar();  // Hola, soy Luis
```

Cada objeto tiene sus PROPIOS valores. Son independientes entre si.

### 1.3 Constructor

El **constructor** es un metodo especial que se ejecuta AUTOMATICAMENTE al crear un objeto con `new`. Sirve para INICIALIZAR los atributos.

**Reglas:**
- Tiene el MISMO nombre que la clase
- NO tiene tipo de retorno (ni `void`)
- Se ejecuta una sola vez: al crear el objeto

```java
public class Persona {
    String nombre;
    int edad;

    // Constructor
    Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    void saludar() {
        System.out.println("Hola, soy " + nombre);
    }
}
```

**Explicacion:**

| Codigo | Que hace |
|--------|----------|
| `Persona(String nombre, int edad)` | Constructor: mismo nombre que la clase, sin `void` |
| `this.nombre = nombre` | Asigna el parametro `nombre` al ATRIBUTO `nombre`. `this.nombre` es el atributo, `nombre` es el parametro |

**Antes vs despues del constructor:**

```java
// Sin constructor: 3 pasos
Persona p = new Persona();
p.nombre = "Ana";
p.edad = 25;

// Con constructor: 1 paso
Persona p = new Persona("Ana", 25);
```

Si NO defines ningun constructor, Java crea uno VACIO automaticamente (`Persona() { }`). Pero si defines UN constructor, el por defecto DESAPARECE.

### 1.4 La palabra clave this

`this` es una referencia al OBJETO ACTUAL. Se usa para:

1. **Diferenciar atributos de parametros** (mismo nombre):
```java
public void setNombre(String nombre) {
    this.nombre = nombre;  // this.nombre = atributo, nombre = parametro
}
```

2. **Llamar a otro constructor** de la misma clase:
```java
public class Persona {
    String nombre;
    int edad;

    Persona() {
        this("Desconocido", 0);  // Llama al constructor de abajo
    }

    Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }
}
```

### 1.5 Atributos y Metodos

| Componente | Descripcion | Ejemplo |
|------------|-------------|---------|
| **Atributo** | Variable que guarda el estado del objeto | `String nombre;` |
| **Metodo** | Funcion que define el comportamiento | `void caminar() { }` |
| **Constructor** | Inicializa el objeto al crearlo | `Persona(String n) { }` |
| **Variable local** | Variable declarada DENTRO de un metodo | `int temp = 0;` |

---

## 2. GLOSARIO DEL TEMA

| Termino | Definicion | Ejemplo |
|---------|------------|---------|
| **Clase** | Plantilla que define atributos y metodos | `class Persona { ... }` |
| **Objeto** | Instancia concreta de una clase | `new Persona()` |
| **Instanciar** | Crear un objeto a partir de una clase | `new Persona("Ana", 25)` |
| **Atributo** | Variable declarada dentro de una clase | `String nombre;` |
| **Metodo** | Funcion declarada dentro de una clase | `void saludar() { }` |
| **Constructor** | Metodo especial que se ejecuta al instanciar | `Persona(String n) { }` |
| **new** | Palabra clave que CREA el objeto en memoria | `new Persona()` |
| **this** | Referencia al objeto actual | `this.nombre = nombre` |
| **Referencia** | Direccion de memoria del objeto | `Persona p = ...` |
| **null** | Ausencia de referencia, el objeto no apunta a nada | `Persona p = null;` |
| **Instancia** | Sinonimo de objeto | `p es una instancia de Persona` |
| **Estado** | Conjunto de valores de los atributos en un momento dado | `nombre="Ana", edad=25` |

---

## 3. COMPARATIVA ENTRE LENGUAJES

### Definir una clase

| Java | Python | JavaScript |
|------|--------|------------|
| `public class Persona {` | `class Persona:` | `class Persona {` |
| `    String nombre;` | `    def __init__(self, n, e):` | `    constructor(nombre, edad) {` |
| `    int edad;` | `        self.nombre = n` | `        this.nombre = nombre;` |
| `    Persona(String n, int e) {` | `        self.edad = e` | `        this.edad = edad;` |
| `        this.nombre = n;` | | `    }` |
| `        this.edad = e;` | | `}` |
| `    }` | | |
| `}` | | |

### Crear un objeto

| Java | Python | JavaScript |
|------|--------|------------|
| `Persona p = new Persona("Ana", 25);` | `p = Persona("Ana", 25)` | `const p = new Persona("Ana", 25);` |

### this / self

| Java | Python | JavaScript |
|------|--------|------------|
| `this.nombre` | `self.nombre` | `this.nombre` |

**Diferencias clave:**
- **Java**: Tipos EXPLICITOS en atributos y parametros. Obligatorio usar `new`. `this` es implicito a veces, explicito cuando hay conflicto
- **Python**: Tipado DINAMICO. `self` es EXPLICITO como primer parametro de todos los metodos. No usa `new`
- **JavaScript**: Sintaxis similar a Java. `constructor()` es el metodo especial. Sin tipos

---

## 4. EJEMPLO GUIADO

### Problema: Cuenta bancaria

> "Crea una clase `CuentaBancaria` con atributos `titular` (String) y `saldo` (double). Incluye un constructor que inicialice ambos, y metodos `depositar(monto)` que aumente el saldo y `mostrarInfo()` que imprima los datos. Luego crea una cuenta, deposita dinero y muestra la informacion."

---

**Paso 1: Analizar**
- Clase `CuentaBancaria` con 2 atributos: `titular`, `saldo`
- Constructor: recibe `titular` y `saldo` inicial
- Metodo `depositar(double monto)`: suma `monto` a `saldo`
- Metodo `mostrarInfo()`: imprime los datos
- Programa principal: crear cuenta, depositar 500, mostrar

**Paso 2: Pseudocodigo**
```
CLASE CuentaBancaria:
    ATRIBUTOS:
        String titular
        double saldo
    CONSTRUCTOR CuentaBancaria(String titular, double saldo):
        this.titular = titular
        this.saldo = saldo
    METODO void depositar(double monto):
        saldo = saldo + monto
    METODO void mostrarInfo():
        imprimir "Titular: " + titular + ", Saldo: $" + saldo

PROGRAMA PRINCIPAL:
    CuentaBancaria c = new CuentaBancaria("Ana", 1000)
    c.depositar(500)
    c.mostrarInfo()  // Titular: Ana, Saldo: $1500.0
```

**Paso 3: Codigo completo**
```java
class CuentaBancaria {
    String titular;
    double saldo;

    CuentaBancaria(String titular, double saldo) {
        this.titular = titular;
        this.saldo = saldo;
    }

    void depositar(double monto) {
        saldo = saldo + monto;  // tambien: saldo += monto
    }

    void mostrarInfo() {
        System.out.println("Titular: " + titular + ", Saldo: $" + saldo);
    }
}

public class Main {
    public static void main(String[] args) {
        CuentaBancaria cuenta = new CuentaBancaria("Ana", 1000);
        cuenta.depositar(500);
        cuenta.mostrarInfo();  // Titular: Ana, Saldo: $1500.0
    }
}
```

**Explicacion:**

| Linea | Explicacion |
|-------|-------------|
| `class CuentaBancaria { ... }` | Define la plantilla para cuentas bancarias |
| `String titular;` | Atributo: nombre del dueno |
| `double saldo;` | Atributo: dinero disponible |
| `CuentaBancaria(String t, double s) { ... }` | Constructor: recibe valores iniciales |
| `this.titular = titular` | `this.titular` (atributo) = `titular` (parametro). Mismo nombre, `this` los distingue |
| `void depositar(double monto)` | Metodo que MODIFICA el estado del objeto |
| `saldo = saldo + monto` | Aumenta el saldo. El objeto CAMBIA su estado interno |
| `new CuentaBancaria("Ana", 1000)` | Crea una cuenta con saldo inicial 1000 |
| `cuenta.depositar(500)` | Ejecuta depositar en esa cuenta. saldo: 1000 -> 1500 |

**Paso 4: Probar**
```
$ java Main
Titular: Ana, Saldo: $1500.0
```

---

## 5. EJERCICIOS

### 🟢 Ejercicio 1: Clase Persona (Basico)

Crea una clase `Persona` con:
- Atributos: `nombre` (String), `edad` (int)
- Constructor que reciba ambos y use `this`
- Metodo `mostrarDatos()` que imprima "Nombre: X, Edad: Y"

En el `main`, crea DOS personas distintas y llama a `mostrarDatos()` para cada una.

**Ejecuta:** `python scripts/runner.py 2 1 1`

---

### 🟡 Ejercicio 2: Clase Rectangulo (Intermedio)

Crea una clase `Rectangulo` con:
- Atributos: `base` (double), `altura` (double)
- Constructor con parametros
- Metodo `area()` que retorne `base * altura`

En el `main`, crea un rectangulo de 5x3 e imprime su area.

**Ejecuta:** `python scripts/runner.py 2 1 2`

---

### 🔴 Ejercicio 3: Clase Libro (Avanzado)

Crea una clase `Libro` con:
- Atributos: `titulo` (String), `autor` (String), `paginas` (int)
- Constructor que inicialice todos los atributos
- Metodo `esLargo()` que retorne `true` si `paginas > 300`

En el `main`, crea DOS libros y muestra si cada uno es largo o no.

**Ejecuta:** `python scripts/runner.py 2 1 3`

---

## Soluciones

```bash
python scripts/runner.py 2 1 1 -s
python scripts/runner.py 2 1 2 -s
python scripts/runner.py 2 1 3 -s
```
