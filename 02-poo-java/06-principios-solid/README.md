# Principios SOLID

Los principios **SOLID** son cinco principios de diseno orientado a objetos que ayudan a crear codigo mantenible, escalable y facil de modificar. No son reglas estrictas, sino guias para escribir mejor codigo.

---

## 1. TEORIA

### 1.1 Que es SOLID?

SOLID es un acronimo que resume 5 principios:

| Letra | Principio | Significado |
|-------|-----------|-------------|
| **S** | **Single Responsibility** | Una clase debe tener UNA sola responsabilidad |
| **O** | **Open/Closed** | Clases abiertas para extension, cerradas para modificacion |
| **L** | **Liskov Substitution** | Las subclases deben poder reemplazar a sus padres |
| **I** | **Interface Segregation** | Interfaces especificas, no generales |
| **D** | **Dependency Inversion** | Depender de abstracciones, no de implementaciones |

---

### S — Single Responsibility Principle (SRP)

> "Una clase debe tener una unica razon para cambiar."

Cada clase debe tener UNA sola responsabilidad. Si una clase hace demasiadas cosas, es dificil de mantener y modificar.

**MAL EJEMPLO:** Una clase que almacena datos Y los imprime:

```java
class Reporte {
    String titulo;
    String contenido;

    // Responsabilidad 1: almacenar datos
    Reporte(String titulo, String contenido) {
        this.titulo = titulo;
        this.contenido = contenido;
    }

    // Responsabilidad 2: imprimir (viola SRP!)
    void imprimir() {
        System.out.println(titulo);
        System.out.println("---");
        System.out.println(contenido);
    }
}
```

**BIEN EJEMPLO:** Separado en dos clases, cada una con una responsabilidad:

```java
class Reporte {
    String titulo;
    String contenido;

    Reporte(String titulo, String contenido) {
        this.titulo = titulo;
        this.contenido = contenido;
    }
    // Solo almacena datos
}

class Impresora {
    // Solo imprime reportes
    static void imprimir(Reporte r) {
        System.out.println(r.titulo);
        System.out.println("---");
        System.out.println(r.contenido);
    }
}
```

**Por que es mejor?** Si cambia el formato de impresion, solo modificas `Impresora`. `Reporte` no se toca. Si cambian los datos del reporte, solo modificas `Reporte`.

---

### O — Open/Closed Principle (OCP)

> "Las clases deben estar ABIERTAS para extension, pero CERRADAS para modificacion."

Debes poder agregar NUEVO comportamiento sin modificar el codigo existente.

**MAL EJEMPLO:** Cada vez que agregamos un nuevo descuento, modificamos la clase:

```java
class CalculadoraPrecio {
    double calcular(double precio, String tipoDescuento) {
        if (tipoDescuento.equals("porcentaje")) {
            return precio * 0.9;  // 10% off
        } else if (tipoDescuento.equals("fijo")) {
            return precio - 15;
        }
        // Si agregamos otro descuento, MODIFICAMOS esta clase!
        return precio;
    }
}
```

**BIEN EJEMPLO:** Usamos una interface. Agregar descuentos = crear nuevas clases, no modificar existentes:

```java
interface Descuento {
    double aplicar(double precio);
}

class DescuentoPorcentaje implements Descuento {
    double porcentaje;
    DescuentoPorcentaje(double p) { this.porcentaje = p; }
    public double aplicar(double p) { return p * (1 - porcentaje / 100); }
}

class DescuentoFijo implements Descuento {
    double cantidad;
    DescuentoFijo(double c) { this.cantidad = c; }
    public double aplicar(double p) { return Math.max(0, p - cantidad); }
}

class CalculadoraPrecio {
    double calcular(double precio, Descuento d) {
        return d.aplicar(precio);  // No sabe que tipo de descuento es!
    }
}
```

Para agregar un nuevo descuento (ej: "2x1"), creas `Descuento2x1 implements Descuento`. No tocas `CalculadoraPrecio`. **Cumple OCP**.

---

### L — Liskov Substitution Principle (LSP)

> "Las subclases deben poder reemplazar a sus clases padre sin alterar el comportamiento correcto."

Si tienes una variable de tipo `Animal`, deberias poder asignarle cualquier subclase (`Perro`, `Gato`) y que todo funcione.

```java
void hacerSonido(Animal a) {
    a.hacerSonido();  // Funciona con Animal, Perro, Gato...
}

// Uso:
hacerSonido(new Perro());  // "Guau!" ✓
hacerSonido(new Gato());   // "Miau!" ✓
```

**Violacion de LSP:** Si una subclase cambia el comportamiento esperado:

```java
class Rectangulo {
    int base, altura;
    void setBase(int b) { this.base = b; }
    void setAltura(int a) { this.altura = a; }
    int area() { return base * altura; }
}

class Cuadrado extends Rectangulo {
    // Un cuadrado NO deberia permitir base != altura!
    void setBase(int b) {
        this.base = b;
        this.altura = b;  // Modifica altura tambien!
    }
}
```

Si el codigo espera un `Rectangulo` y recibe un `Cuadrado`, el comportamiento cambia inesperadamente. **Violacion de LSP**.

---

### I — Interface Segregation Principle (ISP)

> "Es mejor tener interfaces PEQUENAS y ESPECIFICAS que una grande y general."

**MAL EJEMPLO:** Una interface que obliga a implementar metodos que no se necesitan:

```java
interface Trabajador {
    void trabajar();
    void comer();
    void dormir();
}

class Robot implements Trabajador {
    public void trabajar() { /* programar */ }
    public void comer() { /* Los robots no comen! */ }
    public void dormir() { /* Los robots no duermen! */ }
    // Forzado a implementar metodos que no tienen sentido
}
```

**BIEN EJEMPLO:** Interfaces separadas:

```java
interface Trabajador { void trabajar(); }
interface Comedor { void comer(); }
interface Durmiente { void dormir(); }

class Robot implements Trabajador {
    public void trabajar() { /* programar */ }
    // No implementa comer() ni dormir() - no necesita
}

class Humano implements Trabajador, Comedor, Durmiente {
    public void trabajar() { /* trabajar */ }
    public void comer() { /* comer */ }
    public void dormir() { /* dormir */ }
}
```

---

### D — Dependency Inversion Principle (DIP)

> "Depende de ABSTRACCIONES, no de IMPLEMENTACIONES concretas."

Las clases de alto nivel no deberian depender de clases de bajo nivel. Ambas deberian depender de abstracciones (interfaces).

**MAL EJEMPLO:** Servicio depende directamente de una implementacion concreta:

```java
class Servicio {
    private BaseDatosMySQL db;  // Depende de una implementacion CONCRETA

    Servicio() {
        this.db = new BaseDatosMySQL();  // Acoplado a MySQL!
    }

    void procesar(String dato) {
        db.guardar(dato);
    }
}
```

Si queremos cambiar a PostgreSQL, hay que MODIFICAR `Servicio`. **Violacion de DIP**.

**BIEN EJEMPLO:** Servicio depende de una abstraccion (interface):

```java
interface BaseDatos {
    void guardar(String dato);
}

class BaseDatosMySQL implements BaseDatos {
    public void guardar(String dato) {
        System.out.println("Guardado en MySQL: " + dato);
    }
}

class BaseDatosArchivo implements BaseDatos {
    public void guardar(String dato) {
        System.out.println("Guardado en archivo: " + dato);
    }
}

class Servicio {
    private BaseDatos db;  // Depende de la ABSTRACCION

    Servicio(BaseDatos db) {  // Inyeccion de dependencia
        this.db = db;
    }

    void procesar(String dato) {
        db.guardar(dato);  // No sabe si es MySQL o Archivo!
    }
}
```

Ahora podemos cambiar la base de datos sin modificar `Servicio`. Solo cambiamos lo que pasamos al constructor.

---

## 2. GLOSARIO DEL TEMA

| Termino | Definicion | Ejemplo |
|---------|------------|---------|
| **SRP** | Una clase = una responsabilidad | `Reporte` almacena, `Impresora` imprime |
| **OCP** | Abierto a extension, cerrado a modificacion | Interface `Descuento`, nuevas clases la implementan |
| **LSP** | Subclases reemplazan a padres sin romper nada | `Perro` puede usarse donde se espera `Animal` |
| **ISP** | Interfaces pequenas y especificas | `Trabajador`, `Comedor`, `Durmiente` separadas |
| **DIP** | Depender de abstracciones, no de concreciones | `Servicio` usa `BaseDatos` (interface), no `BaseDatosMySQL` |
| **Inyeccion de dependencia** | Pasar dependencias por constructor | `new Servicio(db)` en vez de `new Servicio()` con `new BaseDatosMySQL()` |
| **Acoplamiento** | Dependencia entre clases. Bajo acoplamiento = mejor | Clases que dependen de interfaces estan poco acopladas |

---

## 3. COMPARATIVA ENTRE LENGUAJES

Los principios SOLID son universales, no dependen del lenguaje. Pero cada lenguaje tiene herramientas distintas para aplicarlos:

| Principio | Java | Python | JavaScript |
|-----------|------|--------|------------|
| **SRP** | Clases con una responsabilidad | Igual | Igual |
| **OCP** | Interfaces o herencia | Clases abstractas, duck typing | Clases, herencia |
| **LSP** | Herencia con `extends` | Herencia | Herencia con `extends` |
| **ISP** | Interfaces pequeñas | Varias clases base abstractas | Varias clases base (simulado) |
| **DIP** | Inyeccion por constructor | Inyeccion por constructor | Inyeccion por constructor |

SOLID se aplica igual en los tres lenguajes. La diferencia es que Java tiene `interface` como palabra clave explicita. Python usa `ABC`. JavaScript no tiene interfaces nativas.

---

## 4. EJEMPLO GUIADO

### Problema: Sistema de notificaciones (aplicando DIP + OCP)

> "Crea un sistema de notificaciones donde un `ServicioNotificacion` pueda enviar mensajes por diferentes canales (email, SMS). Debe cumplir OCP (poder agregar canales sin modificar codigo existente) y DIP (depender de abstracciones)."

---

**Paso 1: Analizar**
- Interface `CanalNotificacion`: contrato para cualquier canal
- `EmailCanal`: implementa el canal de email
- `SMSCanal`: implementa el canal de SMS
- `ServicioNotificacion`: depende de la interface, no de canales concretos

**Paso 2: Pseudocodigo**
```
INTERFACE CanalNotificacion:
    METODO void enviar(String mensaje, String destinatario)

CLASE EmailCanal IMPLEMENTS CanalNotificacion:
    METODO void enviar(String mensaje, String dest):
        imprimir "[EMAIL a " + dest + "] " + mensaje

CLASE SMSCanal IMPLEMENTS CanalNotificacion:
    METODO void enviar(String mensaje, String dest):
        imprimir "[SMS a " + dest + "] " + mensaje

CLASE ServicioNotificacion:
    PRIVATE CanalNotificacion canal
    CONSTRUCTOR ServicioNotificacion(CanalNotificacion canal):
        this.canal = canal
    METODO void notificar(String mensaje, String dest):
        canal.enviar(mensaje, dest)

PROGRAMA PRINCIPAL:
    ServicioNotificacion s1 = new ServicioNotificacion(new EmailCanal())
    s1.notificar("Hola", "ana@email.com")
    ServicioNotificacion s2 = new ServicioNotificacion(new SMSCanal())
    s2.notificar("Hola", "+123456789")
```

**Paso 3: Codigo completo**
```java
interface CanalNotificacion {
    void enviar(String mensaje, String destinatario);
}

class EmailCanal implements CanalNotificacion {
    @Override
    public void enviar(String mensaje, String destinatario) {
        System.out.println("[EMAIL a " + destinatario + "] " + mensaje);
    }
}

class SMSCanal implements CanalNotificacion {
    @Override
    public void enviar(String mensaje, String destinatario) {
        System.out.println("[SMS a " + destinatario + "] " + mensaje);
    }
}

class ServicioNotificacion {
    private CanalNotificacion canal;

    public ServicioNotificacion(CanalNotificacion canal) {
        this.canal = canal;
    }

    public void notificar(String mensaje, String destinatario) {
        canal.enviar(mensaje, destinatario);
    }
}

public class Main {
    public static void main(String[] args) {
        ServicioNotificacion emailService =
            new ServicioNotificacion(new EmailCanal());
        emailService.notificar("Bienvenido!", "usuario@email.com");

        ServicioNotificacion smsService =
            new ServicioNotificacion(new SMSCanal());
        smsService.notificar("Tu codigo es 1234", "+52123456789");
    }
}
```

**Explicacion:**

| Linea | Principio | Explicacion |
|-------|-----------|-------------|
| `interface CanalNotificacion` | DIP | Servicio depende de la abstraccion, no de una clase concreta |
| `class SMSCanal implements CanalNotificacion` | OCP | Agregamos un canal NUEVO sin modificar `ServicioNotificacion` |
| `private CanalNotificacion canal` | DIP | El atributo es de tipo INTERFACE, no de una clase especifica |
| `new ServicioNotificacion(new EmailCanal())` | DIP | Inyeccion de dependencia: el canal se pasa por constructor |

**Paso 4: Probar**
```
$ java Main
[EMAIL a usuario@email.com] Bienvenido!
[SMS a +52123456789] Tu codigo es 1234
```

---

## 5. EJERCICIOS

### 🟢 Ejercicio 1: SRP - Reporte e Impresora (Basico)

Refactoriza: crea una clase `Reporte` con atributos `titulo` y `contenido` (solo datos), y una clase `Impresora` con metodo estatico `imprimir(Reporte r)` que muestre titulo, `---`, y contenido.

En el `main`, crea un Reporte y pasalo a `Impresora.imprimir()`.

**Ejecuta:** `python scripts/runner.py 2 6 1`

---

### 🟡 Ejercicio 2: OCP - Sistema de descuentos (Intermedio)

Crea:
- Interface `Descuento` con metodo `double aplicar(double precio)`
- `DescuentoPorcentaje`: aplica un % de descuento
- `DescuentoFijo`: resta una cantidad fija (minimo 0)
- `CalculadoraPrecio`: metodo `calcular(double precio, Descuento d)`

En el `main`, prueba calcular(100, 10%) = 90, y calcular(100, fijo $15) = 85.

**Ejecuta:** `python scripts/runner.py 2 6 2`

---

### 🔴 Ejercicio 3: DIP - Servicio con inyeccion de dependencia (Avanzado)

Crea:
- Interface `BaseDatos` con metodo `void guardar(String dato)`
- `BaseDatosMySQL` y `BaseDatosArchivo` que la implementen
- `Servicio` que reciba `BaseDatos` por constructor y tenga metodo `procesar(String)`

En el `main`, crea un Servicio con cada implementacion y llama a procesar().

**Ejecuta:** `python scripts/runner.py 2 6 3`

---

## Soluciones

```bash
python scripts/runner.py 2 6 1 -s
python scripts/runner.py 2 6 2 -s
python scripts/runner.py 2 6 3 -s
```
