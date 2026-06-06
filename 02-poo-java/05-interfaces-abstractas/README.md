# Interfaces y Clases Abstractas

Las **interfaces** y **clases abstractas** son dos mecanismos de Java para definir contratos y comportamientos sin implementarlos completamente. Son fundamentales para el diseno orientado a objetos.

---

## 1. TEORIA

### 1.1 Interface

Una **interface** es un contrato que define QUE debe hacer una clase, pero no COMO. Las clases que la implementan deben proporcionar el codigo.

```java
// Definicion de una interface
interface Volador {
    void volar();  // Metodo abstracto: solo la firma, sin cuerpo
}

// Implementacion de la interface
class Pajaro implements Volador {
    @Override
    public void volar() {
        System.out.println("El pajaro vuela batiendo alas");
    }
}

class Avion implements Volador {
    @Override
    public void volar() {
        System.out.println("El avion vuela con motores");
    }
}
```

**Explicacion:**

| Codigo | Que hace |
|--------|----------|
| `interface Volador { ... }` | Define una interface. No es una clase, es un CONTRATO |
| `void volar();` | Metodo abstracto: solo declara la firma, sin `{}` |
| `class Pajaro implements Volador` | `implements` = Pajaro FIRMA el contrato: debe implementar volar() |
| `public void volar()` | El metodo DEBE ser `public` (los metodos de interface son public por defecto) |

**Una clase puede implementar VARIAS interfaces:**

```java
interface Volador { void volar(); }
interface Nadador { void nadar(); }

class Pato implements Volador, Nadador {
    public void volar() { System.out.println("Pato volando"); }
    public void nadar() { System.out.println("Pato nadando"); }
}
```

### 1.2 Clase Abstracta

Una **clase abstracta** es una clase que NO se puede instanciar directamente. Puede tener metodos ABSTRACTOS (sin cuerpo) y metodos CONCRETOS (con implementacion).

```java
// Clase abstracta: mezcla de abstracto y concreto
abstract class Forma {
    // Metodo abstracto: las subclases DEBEN implementarlo
    abstract double area();

    // Metodo concreto: se hereda tal cual
    void info() {
        System.out.println("Soy una forma");
    }
}

class Circulo extends Forma {
    double radio;

    Circulo(double radio) {
        this.radio = radio;
    }

    @Override
    double area() {
        return Math.PI * radio * radio;
    }
    // info() se hereda automaticamente, no necesito reescribirlo
}
```

**Explicacion:**

| Codigo | Que hace |
|--------|----------|
| `abstract class Forma` | No puedes hacer `new Forma()`. Solo existe para ser heredada |
| `abstract double area()` | Metodo abstracto: sin cuerpo. Obliga a las subclases a implementarlo |
| `void info()` | Metodo CONCRETO: tiene implementacion. Las subclases lo heredan sin cambios |
| `class Circulo extends Forma` | Circulo hereda de Forma (como herencia normal) |
| `double area()` | Implementa el metodo abstracto. Si no lo hiciera, Circulo tambien seria abstracta |

### 1.3 Interface vs Clase Abstracta

| Caracteristica | Interface | Clase Abstracta |
|---------------|-----------|-----------------|
| Palabra clave | `interface` | `abstract class` |
| Se puede instanciar? | No | No |
| Metodos abstractos | Si (todos, hasta Java 7) | Si |
| Metodos concretos | `default` (Java 8+) | Si |
| Atributos | `static final` (constantes) | Puede tener atributos normales |
| Constructores | No | Si |
| Herencia multiple | Si: `implements A, B` | No: `extends A` (solo una) |
| Relacion | "Puede hacer" (capacidad) | "ES UN" (jerarquia) |

**Cuando usar cada una:**
- **Interface**: Para definir CAPACIDADES que cualquier clase puede tener (volador, nadador, imprimible)
- **Clase abstracta**: Para definir una BASE con comportamiento comun y obligar a implementar partes especificas

---

## 2. GLOSARIO DEL TEMA

| Termino | Definicion | Ejemplo |
|---------|------------|---------|
| **Interface** | Contrato que define metodos sin implementacion | `interface Volador { void volar(); }` |
| **Clase abstracta** | Clase que no se puede instanciar, mezcla metodos abstractos y concretos | `abstract class Forma { ... }` |
| **implements** | Palabra clave para implementar una interface | `class Pajaro implements Volador` |
| **abstract** | Modificador que indica que un metodo no tiene cuerpo | `abstract double area();` |
| **Metodo abstracto** | Metodo declarado sin implementacion | `void volar();` (sin `{}`) |
| **Metodo concreto** | Metodo con implementacion completa | `void info() { ... }` |
| **default** (Java 8+) | Metodo con implementacion dentro de una interface | `default void metodo() { ... }` |
| **Contrato** | Conjunto de metodos que una clase se compromete a implementar | La interface es el contrato |

---

## 3. COMPARATIVA ENTRE LENGUAJES

### Interface

| Java | Python | JavaScript |
|------|--------|------------|
| `interface Volador {` | `from abc import ABC, abstractmethod` | No tiene interfaces nativas |
| `    void volar();` | `class Volador(ABC):` | Se simula con duck typing |
| `}` | `    @abstractmethod` | o con TypeScript |
| | `    def volar(self): pass` | |

### Clase abstracta

| Java | Python | JavaScript |
|------|--------|------------|
| `abstract class Forma {` | `from abc import ABC, abstractmethod` | `class Forma {` |
| `    abstract double area();` | `class Forma(ABC):` | `    constructor() {` |
| `    void info() { ... }` | `    @abstractmethod` | `        if (this.constructor === Forma)` |
| `}` | `    def area(self): pass` | `            throw new Error("Abstracta!");` |
| | `    def info(self):` | `    }` |
| | `        print("Soy una forma")` | `    area() { throw new Error("Implementar!"); }` |
| | | `}` |

**Diferencias clave:**
- **Java**: `interface` e `abstract class` son palabras clave del lenguaje. Soporta herencia multiple SOLO con interfaces
- **Python**: Usa el modulo `abc` (Abstract Base Classes). No hay distincion sintactica entre interface y abstracta
- **JavaScript**: No tiene soporte nativo. Se simula lanzando errores en el constructor o metodos

---

## 4. EJEMPLO GUIADO

### Problema: Sistema de notificaciones con interfaces

> "Crea una interface `Notificable` con metodo `enviar(String mensaje)`. Luego crea `EmailNotif` y `SMSNotif` que la implementen. Usa polimorfismo para enviar notificaciones."

---

**Paso 1: Analizar**
- Interface `Notificable`: metodo `enviar(String mensaje)`
- `EmailNotif`: implementa `enviar()` simulando envio de email
- `SMSNotif`: implementa `enviar()` simulando envio de SMS
- Array `Notificable[]` para demostrar polimorfismo

**Paso 2: Pseudocodigo**
```
INTERFACE Notificable:
    METODO void enviar(String mensaje)

CLASE EmailNotif IMPLEMENTS Notificable:
    METODO void enviar(String mensaje):
        imprimir "[EMAIL] " + mensaje

CLASE SMSNotif IMPLEMENTS Notificable:
    METODO void enviar(String mensaje):
        imprimir "[SMS] " + mensaje

PROGRAMA PRINCIPAL:
    Notificable[] notificaciones = [new EmailNotif(), new SMSNotif()]
    PARA CADA Notificable n EN notificaciones:
        n.enviar("Hola mundo!")
```

**Paso 3: Codigo completo**
```java
interface Notificable {
    void enviar(String mensaje);
}

class EmailNotif implements Notificable {
    @Override
    public void enviar(String mensaje) {
        System.out.println("[EMAIL] " + mensaje);
    }
}

class SMSNotif implements Notificable {
    @Override
    public void enviar(String mensaje) {
        System.out.println("[SMS] " + mensaje);
    }
}

public class Main {
    public static void main(String[] args) {
        Notificable[] notificaciones = new Notificable[2];
        notificaciones[0] = new EmailNotif();
        notificaciones[1] = new SMSNotif();

        for (Notificable n : notificaciones) {
            n.enviar("Hola mundo!");
        }
    }
}
```

**Explicacion:**

| Linea | Explicacion |
|-------|-------------|
| `interface Notificable { void enviar(String m); }` | Define el contrato: cualquier clase notificable debe tener `enviar()` |
| `class EmailNotif implements Notificable` | EmailNotif FIRMA el contrato |
| `public void enviar(String mensaje)` | Implementa el metodo. DEBE ser public (los metodos de interface son implicitamente public) |
| `Notificable[] notificaciones` | Array de tipo NOTIFICABLE (la interface). Puede contener cualquier implementacion |
| `n.enviar("Hola mundo!")` | Polimorfismo via interface: cada implementacion hace algo distinto |

**Paso 4: Probar**
```
$ java Main
[EMAIL] Hola mundo!
[SMS] Hola mundo!
```

---

## 5. EJERCICIOS

### 🟢 Ejercicio 1: Interface Volador (Basico)

Crea una interface `Volador` con metodo `volar()`.
- `Pajaro implements Volador`: `volar()` imprime `"El pajaro vuela batiendo alas"`
- `Avion implements Volador`: `volar()` imprime `"El avion vuela con motores"`

En el `main`, crea un Pajaro y un Avion y llama a `volar()`.

**Ejecuta:** `python scripts/runner.py 2 5 1`

---

### 🟡 Ejercicio 2: Clase abstracta Forma (Intermedio)

Crea una clase abstracta `Forma` con:
- Metodo abstracto `double area()`
- Metodo concreto `void info()` que imprima `"Soy una forma"`

`Circulo extends Forma`: implementa `area()` con `Math.PI * radio * radio`
`Rectangulo extends Forma`: implementa `area()` con `base * altura`

En el `main`, crea un Circulo y Rectangulo, muestra area e info().

**Ejecuta:** `python scripts/runner.py 2 5 2`

---

### 🔴 Ejercicio 3: Interface Reproducible (Avanzado)

Crea una interface `Reproducible` con metodo `reproducir()`.
- `Musica implements Reproducible`: `reproducir()` imprime `"Reproduciendo cancion..."`
- `Video implements Reproducible`: `reproducir()` imprime `"Reproduciendo video..."`

En el `main`, usa un array de `Reproducible[]` para mostrar polimorfismo.

**Ejecuta:** `python scripts/runner.py 2 5 3`

---

## Soluciones

```bash
python scripts/runner.py 2 5 1 -s
python scripts/runner.py 2 5 2 -s
python scripts/runner.py 2 5 3 -s
```
