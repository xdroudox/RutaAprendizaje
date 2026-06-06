# Polimorfismo

El **polimorfismo** (del griego "muchas formas") permite que un mismo metodo tenga comportamientos diferentes segun el contexto o el objeto que lo ejecuta. Es el tercer pilar de la POO.

---

## 1. TEORIA

### 1.1 Que es el polimorfismo?

Polimorfismo = "muchas formas". Un mismo mensaje (llamada a metodo) se comporta distinto segun el objeto que lo recibe.

```java
Animal a1 = new Perro();
Animal a2 = new Gato();

a1.hacerSonido();  // "Guau!"  (comportamiento de Perro)
a2.hacerSonido();  // "Miau!"  (comportamiento de Gato)
```

**Mismo metodo** (`hacerSonido()`), **mismo tipo de variable** (`Animal`), pero **comportamiento diferente** segun el objeto real.

### 1.2 Sobrecarga (Overloading)

**Overloading** = Varios metodos con el MISMO nombre pero DIFERENTES parametros (numero o tipo). Ocurre en TIEMPO DE COMPILACION (compile-time polymorphism).

```java
public class Calculadora {
    // Mismo nombre, diferentes parametros
    int sumar(int a, int b) {
        return a + b;
    }

    int sumar(int a, int b, int c) {
        return a + b + c;
    }

    double sumar(double a, double b) {
        return a + b;
    }
}
```

**Explicacion:**

| Codigo | Que hace |
|--------|----------|
| `sumar(int a, int b)` | Suma 2 enteros. Si llamas `calc.sumar(3, 4)`, Java usa esta version |
| `sumar(int a, int b, int c)` | Suma 3 enteros. Si llamas `calc.sumar(3, 4, 5)`, Java usa esta |
| `sumar(double a, double b)` | Suma 2 doubles. Si llamas `calc.sumar(3.5, 2.5)`, Java usa esta |

**Java decide automaticamente que version ejecutar segun los ARGUMENTOS que pasas:**

```java
Calculadora c = new Calculadora();
c.sumar(3, 4);       // Llama a sumar(int, int)
c.sumar(3, 4, 5);    // Llama a sumar(int, int, int)
c.sumar(3.5, 2.5);   // Llama a sumar(double, double)
```

### 1.3 Sobrescritura (Overriding)

**Overriding** = Una subclase redefine un metodo heredado de la superclase. Ocurre en TIEMPO DE EJECUCION (runtime polymorphism).

```java
class Animal {
    void hacerSonido() {
        System.out.println("...");
    }
}

class Perro extends Animal {
    @Override
    void hacerSonido() {
        System.out.println("Guau!");
    }
}

class Gato extends Animal {
    @Override
    void hacerSonido() {
        System.out.println("Miau!");
    }
}
```

**Explicacion:**

| Codigo | Que hace |
|--------|----------|
| `@Override` | Le dice a Java: "estoy sobrescribiendo intencionalmente". Si el metodo no existe en el padre, Java da error |
| `void hacerSonido()` en Perro | Redefine el metodo. Cuando un Perro ejecuta hacerSonido(), imprime "Guau!" |
| `void hacerSonido()` en Gato | Redefine el metodo. Cuando un Gato ejecuta hacerSonido(), imprime "Miau!" |

### 1.4 Dynamic Dispatch (Enlace dinamico)

Es el mecanismo que Java usa para decidir EN TIEMPO DE EJECUCION que metodo ejecutar.

```java
Animal a;           // Variable de tipo Animal
a = new Perro();    // a apunta a un objeto Perro
a.hacerSonido();    // Java mira: el objeto REAL es Perro → ejecuta el metodo de Perro → "Guau!"

a = new Gato();     // a apunta a un objeto Gato
a.hacerSonido();    // Java mira: el objeto REAL es Gato → ejecuta el metodo de Gato → "Miau!"
```

**Como funciona:**
1. `a` es de tipo `Animal` (tipo declarado)
2. Pero el objeto REAL es `Perro` o `Gato` (tipo real)
3. Java mira el TIPO REAL del objeto, no el tipo de la variable
4. Ejecuta el metodo del tipo real

**Ejemplo con array polimorfico:**

```java
Animal[] animales = new Animal[2];
animales[0] = new Perro();
animales[1] = new Gato();

for (Animal a : animales) {
    a.hacerSonido();  // Primera iteracion: "Guau!", Segunda: "Miau!"
}
```

Aunque el array es de tipo `Animal[]`, cada objeto conserva su tipo real. Java ejecuta el metodo adecuado para cada uno.

### 1.5 Resumen: Overloading vs Overriding

| Caracteristica | Overloading (Sobrecarga) | Overriding (Sobrescritura) |
|----------------|--------------------------|----------------------------|
| Cuando ocurre | Compilacion | Ejecucion |
| Donde ocurre | Misma clase | Clase padre → subclase |
| Parametros | Deben ser diferentes | Deben ser identicos |
| Tipo de retorno | Puede ser diferente | Debe ser el mismo (o covariante) |
| Palabra clave | Ninguna | `@Override` (recomendado) |

---

## 2. GLOSARIO DEL TEMA

| Termino | Definicion | Ejemplo |
|---------|------------|---------|
| **Polimorfismo** | Capacidad de un objeto de tomar multiples formas | Un mismo metodo se comporta distinto segun el objeto |
| **Overloading** | Varios metodos con mismo nombre, distintos parametros | `sumar(int, int)`, `sumar(int, int, int)` |
| **Overriding** | Subclase redefine un metodo del padre | `@Override void hacerSonido()` |
| **Dynamic Dispatch** | Mecanismo que elige el metodo en ejecucion segun el tipo real | `Animal a = new Perro(); a.hacerSonido()` |
| **Tipo declarado** | Tipo de la variable (lo que ves en el codigo) | `Animal a` |
| **Tipo real** | Tipo del objeto creado con `new` | `new Perro()` |
| **@Override** | Anotacion que indica sobrescritura intencional | `@Override void metodo()` |
| **Firma del metodo** | Nombre + tipo/orden de parametros | `sumar(int, int)` |

---

## 3. COMPARATIVA ENTRE LENGUAJES

### Overloading (Sobrecarga)

| Java | Python | JavaScript |
|------|--------|------------|
| `int sumar(int a, int b)` | `def sumar(a, b=None, c=None):` | `function sumar(a, b, c) {` |
| `int sumar(int a, int b, int c)` | `    if c is None:` | `    if (c === undefined) {` |
| | `        return a + b` | `        return a + b;` |
| | `    return a + b + c` | `    }` |
| | | `    return a + b + c;` |
| | | `}` |

**Diferencias clave:**
- **Java**: Soporta overloading nativamente. Mismo nombre, diferentes parametros, son metodos distintos
- **Python**: No tiene overloading. Se simula con parametros opcionales (`None`)
- **JavaScript**: Tampoco tiene overloading. Se maneja con `undefined` o `arguments`

### Overriding (Sobrescritura)

| Java | Python | JavaScript |
|------|--------|------------|
| `class Perro extends Animal {` | `class Perro(Animal):` | `class Perro extends Animal {` |
| `    @Override` | `    def hacer_sonido(self):` | `    hacer_sonido() {` |
| `    void hacerSonido() {` | `        print("Guau!")` | `        console.log("Guau!");` |
| `        System.out.println("Guau!");` | | `    }` |
| `    }` | | `}` |
| `}` | | |

Los tres lenguajes soportan overriding. La diferencia es que Java requiere `@Override` (opcional pero recomendado), Python y JavaScript no.

---

## 4. EJEMPLO GUIADO

### Problema: Sistema de notificaciones polimorfico

> "Crea una clase `Notificacion` con metodo `enviar()` que imprima 'Enviando notificacion...'. Luego crea `Email` y `SMS` que hereden y sobrescriban `enviar()`. Demuestra polimorfismo con un array."

---

**Paso 1: Analizar**
- Clase `Notificacion`: metodo `enviar()` generico
- `Email`: sobrescribe `enviar()` para enviar email
- `SMS`: sobrescribe `enviar()` para enviar SMS
- Array polimorfico para demostrar dynamic dispatch

**Paso 2: Pseudocodigo**
```
CLASE Notificacion:
    METODO void enviar():
        imprimir "Enviando notificacion generica..."

CLASE Email EXTENDS Notificacion:
    @Override METODO void enviar():
        imprimir "Enviando email a destinatario..."

CLASE SMS EXTENDS Notificacion:
    @Override METODO void enviar():
        imprimir "Enviando SMS al numero..."

PROGRAMA PRINCIPAL:
    Notificacion[] notis = [new Email(), new SMS()]
    PARA CADA Notificacion n EN notis:
        n.enviar()
    // Output:
    // Enviando email a destinatario...
    // Enviando SMS al numero...
```

**Paso 3: Codigo completo**
```java
class Notificacion {
    void enviar() {
        System.out.println("Enviando notificacion generica...");
    }
}

class Email extends Notificacion {
    @Override
    void enviar() {
        System.out.println("Enviando email a destinatario...");
    }
}

class SMS extends Notificacion {
    @Override
    void enviar() {
        System.out.println("Enviando SMS al numero...");
    }
}

public class Main {
    public static void main(String[] args) {
        Notificacion[] notificaciones = new Notificacion[2];
        notificaciones[0] = new Email();
        notificaciones[1] = new SMS();

        for (Notificacion n : notificaciones) {
            n.enviar();
        }
    }
}
```

**Explicacion:**

| Linea | Explicacion |
|-------|-------------|
| `class Email extends Notificacion` | Email HEREDA de Notificacion |
| `@Override void enviar()` | SOBRESCRIBE el metodo del padre |
| `Notificacion[] notificaciones` | Array de tipo NOTIFICACION (el tipo general) |
| `notificaciones[0] = new Email()` | Guardamos un EMAIL en una posicion del array |
| `n.enviar()` | Java mira el tipo REAL: si es Email, ejecuta enviar() de Email; si es SMS, ejecuta el de SMS |

**Paso 4: Probar**
```
$ java Main
Enviando email a destinatario...
Enviando SMS al numero...
```

---

## 5. EJERCICIOS

### 🟢 Ejercicio 1: Sobrecarga de sumar() (Basico)

Crea una clase `Calculadora` con dos metodos `sumar`:
- `sumar(int a, int b)` que retorne `a + b`
- `sumar(int a, int b, int c)` que retorne `a + b + c`

En el `main`, crea una Calculadora y prueba ambos metodos.

**Ejecuta:** `python scripts/runner.py 2 4 1`

---

### 🟡 Ejercicio 2: Array polimorfico de Animales (Intermedio)

Usando las clases `Animal`, `Perro` y `Gato` (del tema de herencia):
- Crea un array de tipo `Animal[]` con un `Perro` y un `Gato`
- Recorre el array con un bucle for llamando a `hacerSonido()`
- Observa como cada animal ejecuta su propia version

**Ejecuta:** `python scripts/runner.py 2 4 2`

---

### 🔴 Ejercicio 3: Figura, Circulo y Rectangulo (Avanzado)

Crea una clase `Figura` con metodo `area()` que retorne `0.0`.
- `Circulo extends Figura`: atributo `radio`, `area()` retorna `Math.PI * radio * radio`
- `Rectangulo extends Figura`: atributos `base` y `altura`, `area()` retorna `base * altura`

En el `main`, crea un array de `Figura[]` con un circulo de radio 5 y un rectangulo de 4x6, y muestra el area de cada uno.

**Ejecuta:** `python scripts/runner.py 2 4 3`

---

## Soluciones

```bash
python scripts/runner.py 2 4 1 -s
python scripts/runner.py 2 4 2 -s
python scripts/runner.py 2 4 3 -s
```
