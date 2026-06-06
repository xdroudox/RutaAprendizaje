# Excepciones

Las **excepciones** son eventos que interrumpen el flujo normal del programa. Java proporciona mecanismos para PREVENIR y MANEJAR errores de forma controlada, evitando que el programa termine abruptamente.

---

## 1. TEORIA

### 1.1 Que es una excepcion?

Una excepcion es un problema que ocurre durante la ejecucion del programa. Si no se maneja, el programa TERMINA.

```java
public class Main {
    public static void main(String[] args) {
        int resultado = 10 / 0;  // ArithmeticException!
        System.out.println("Esto nunca se ejecuta");
    }
}
```

Sin manejo de excepciones, este programa termina con un error. Con manejo, podemos REACCIONAR y continuar.

### 1.2 try/catch — Capturar excepciones

El bloque `try` envuelve el codigo que PUEDE fallar. El bloque `catch` define QUE hacer si falla.

```java
try {
    int resultado = 10 / 0;  // Codigo que puede lanzar excepcion
    System.out.println("Resultado: " + resultado);  // No se ejecuta si fallo
} catch (ArithmeticException e) {
    System.out.println("Error: No se puede dividir por cero");
}
// El programa CONTINUA aqui
```

**Explicacion:**

| Codigo | Que hace |
|--------|----------|
| `try { ... }` | Intenta ejecutar el codigo. Si algo falla, SALTEA al catch |
| `catch (ArithmeticException e)` | Captura SOLO ArithmeticException. `e` es el objeto de excepcion |
| `e.getMessage()` | Obtiene el mensaje de error de la excepcion |

**Flujo de ejecucion:**
1. Java ejecuta el `try`
2. Si ocurre `10 / 0`, se lanza `ArithmeticException`
3. Java busca un `catch` que capte ese tipo de excepcion
4. Ejecuta el codigo dentro del `catch`
5. El programa CONTINUA despues del try/catch

### 1.3 Multiples catch

Puedes tener varios `catch` para diferentes tipos de excepcion:

```java
try {
    String texto = null;
    System.out.println(texto.length());  // NullPointerException

    int num = Integer.parseInt("abc");  // NumberFormatException
} catch (NullPointerException e) {
    System.out.println("Error: objeto nulo");
} catch (NumberFormatException e) {
    System.out.println("Error: formato numerico invalido");
}
```

**El orden importa:** Pon los catch mas especificos PRIMERO, los mas generales al final.

### 1.4 finally — Siempre se ejecuta

El bloque `finally` se ejecuta SIEMPRE, haya o no excepcion. Se usa para liberar recursos.

```java
try {
    int resultado = 10 / 0;
} catch (ArithmeticException e) {
    System.out.println("Error de division");
} finally {
    System.out.println("Esto se ejecuta SIEMPRE");
}
```

### 1.5 throws — Declarar excepciones

`throws` en la firma del metodo indica que el metodo PUEDE lanzar una excepcion. Obliga a quien llama al metodo a manejarla.

```java
void leerArchivo() throws IOException {
    // Este metodo puede lanzar IOException
    // Quien lo llame DEBE usar try/catch o declarar throws tambien
}
```

### 1.6 throw — Lanzar excepciones

`throw` (sin s) LANZA una excepcion manualmente:

```java
if (edad < 0) {
    throw new IllegalArgumentException("La edad no puede ser negativa");
}
```

### 1.7 Excepciones personalizadas

Puedes crear tus PROPIAS excepciones extendiendo `Exception`:

```java
class EdadInvalidaException extends Exception {
    public EdadInvalidaException(String mensaje) {
        super(mensaje);  // Llama al constructor de Exception
    }
}

// Uso:
void validarEdad(int edad) throws EdadInvalidaException {
    if (edad <= 0 || edad > 150) {
        throw new EdadInvalidaException("Edad " + edad + " no valida");
    }
}
```

**Explicacion:**

| Codigo | Que hace |
|--------|----------|
| `class EdadInvalidaException extends Exception` | Crea una nueva clase de excepcion |
| `super(mensaje)` | Pasa el mensaje a la clase padre (Exception) |
| `throws EdadInvalidaException` | Declara que el metodo puede lanzarla |
| `throw new EdadInvalidaException(...)` | LANZA la excepcion (crea el objeto con `new` y lo lanza con `throw`) |

### 1.8 Jerarquia de excepciones

```
Throwable (clase raiz)
├── Exception (recuperable: puedes capturarla y seguir)
│   ├── RuntimeException (errores de programa: NullPointer, Arithmetic...)
│   └── IOException (errores de entrada/salida)
└── Error (grave, no recuperable: OutOfMemoryError, StackOverflow...)
```

- **Checked exceptions** (`IOException`, `SQLException`): El compilador OBLIGA a manejarlas (try/catch o throws)
- **Unchecked exceptions** (`RuntimeException`): No es obligatorio manejarlas, pero es buena practica

---

## 2. GLOSARIO DEL TEMA

| Termino | Definicion | Ejemplo |
|---------|------------|---------|
| **Excepcion** | Evento que interrumpe el flujo normal del programa | `ArithmeticException`, `NullPointerException` |
| **try** | Bloque que envuelve codigo que puede fallar | `try { ... }` |
| **catch** | Bloque que captura y maneja una excepcion | `catch (IOException e) { ... }` |
| **finally** | Bloque que se ejecuta siempre (haya o no excepcion) | `finally { ... }` |
| **throws** | Declara que un metodo puede lanzar una excepcion | `void metodo() throws IOException` |
| **throw** | Palabra clave para lanzar una excepcion | `throw new Exception("error")` |
| **Checked exception** | Excepcion que el compilador obliga a manejar | `IOException` |
| **Unchecked exception** | Excepcion que no es obligatorio manejar | `NullPointerException` |

---

## 3. COMPARATIVA ENTRE LENGUAJES

### try/catch

| Java | Python | JavaScript |
|------|--------|------------|
| `try {` | `try:` | `try {` |
| `    int r = 10 / 0;` | `    r = 10 / 0` | `    let r = 10 / 0;` |
| `} catch (ArithmeticException e) {` | `except ZeroDivisionError as e:` | `} catch (e) {` |
| `    System.out.println(e);` | `    print(e)` | `    console.log(e);` |
| `} finally { ... }` | `finally: ...` | `} finally { ... }` |

### Lanzar excepcion

| Java | Python | JavaScript |
|------|--------|------------|
| `throw new Exception("msg")` | `raise Exception("msg")` | `throw new Error("msg")` |

### Excepcion personalizada

| Java | Python | JavaScript |
|------|--------|------------|
| `class MiEx extends Exception {` | `class MiEx(Exception):` | `class MiEx extends Error {` |
| `    MiEx(String msg) { super(msg); }` | `    def __init__(self, msg):` | `    constructor(msg) {` |
| `}` | `        super().__init__(msg)` | `        super(msg);` |
| | | `    }` |
| | | `}` |

**Diferencias clave:**
- **Java**: Diferencia entre checked y unchecked. `throws` en la firma del metodo
- **Python**: Todo es runtime. Usa `raise` y `except`
- **JavaScript**: Similar a Java pero sin checked exceptions

---

## 4. EJEMPLO GUIADO

### Problema: Calculadora con manejo de excepciones

> "Crea un metodo `dividir(int a, int b)` que lance `ArithmeticException` si b es 0. En el main, llama al metodo con 10/2 y 10/0, captura la excepcion y muestra un mensaje amigable."

---

**Paso 1: Analizar**
- Metodo `dividir(int a, int b)` que retorna a/b
- Si b == 0, lanza `ArithmeticException` con mensaje
- En el main, llamar con try/catch

**Paso 2: Pseudocodigo**
```
METODO int dividir(int a, int b):
    SI b == 0:
        LANZAR ArithmeticException("No se puede dividir por cero")
    DEVOLVER a / b

PROGRAMA PRINCIPAL:
    INTENTAR:
        imprimir dividir(10, 2)
        imprimir dividir(10, 0)  // Esto lanza excepcion
    CAPTURAR ArithmeticException e:
        imprimir "Error: " + e.getMessage()
```

**Paso 3: Codigo completo**
```java
public class Main {

    static int dividir(int a, int b) {
        if (b == 0) {
            throw new ArithmeticException("No se puede dividir por cero");
        }
        return a / b;
    }

    public static void main(String[] args) {
        try {
            System.out.println("10 / 2 = " + dividir(10, 2));
            System.out.println("10 / 0 = " + dividir(10, 0));  // Excepcion aqui
            System.out.println("Esto no se ejecuta");  // Saltado por la excepcion
        } catch (ArithmeticException e) {
            System.out.println("Error: " + e.getMessage());
        }

        System.out.println("El programa CONTINUA...");
    }
}
```

**Explicacion:**

| Linea | Explicacion |
|-------|-------------|
| `throw new ArithmeticException("...")` | Creamos y lanzamos la excepcion manualmente |
| `dividir(10, 2)` | Funciona bien, imprime 5 |
| `dividir(10, 0)` | El metodo lanza ArithmeticException |
| El flujo SALTEA al catch | `System.out.println("Esto no se ejecuta")` se salta |
| `catch (ArithmeticException e)` | Captura la excepcion, imprime el mensaje |
| `e.getMessage()` | Obtiene "No se puede dividir por cero" |
| `"El programa CONTINUA..."` | Se ejecuta! El programa no termino abruptamente |

**Paso 4: Probar**
```
$ java Main
10 / 2 = 5
Error: No se puede dividir por cero
El programa CONTINUA...
```

---

## 5. EJERCICIOS

### 🟢 Ejercicio 1: Division con try/catch (Basico)

Escribe un programa que divida dos numeros enteros. Usa `try/catch` para capturar `ArithmeticException` si se divide por cero. Prueba con 10/2 y con 10/0.

**Ejecuta:** `python scripts/runner.py 2 7 1`

---

### 🟡 Ejercicio 2: NumberFormatException (Intermedio)

Usa `Integer.parseInt()` para convertir un String a int. Captura `NumberFormatException` si el formato es invalido. Prueba con "123" (valido) y con "abc" (invalido).

**Ejecuta:** `python scripts/runner.py 2 7 2`

---

### 🔴 Ejercicio 3: Excepcion personalizada (Avanzado)

Crea `EdadInvalidaException extends Exception`. Crea un metodo `validarEdad(int edad)` que la lance si edad <= 0 o edad > 150. En el main, prueba con 25 y con -5.

**Ejecuta:** `python scripts/runner.py 2 7 3`

---

## Soluciones

```bash
python scripts/runner.py 2 7 1 -s
python scripts/runner.py 2 7 2 -s
python scripts/runner.py 2 7 3 -s
```
