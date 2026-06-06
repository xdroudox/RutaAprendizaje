# Encapsulacion

La **encapsulacion** protege los datos de un objeto ocultando su implementacion interna y controlando como se accede y modifica. Es uno de los pilares de la POO.

---

## 1. TEORIA

### 1.1 El problema: acceso directo a atributos

Sin encapsulacion, cualquier codigo puede modificar los atributos de un objeto directamente:

```java
Persona p = new Persona();
p.edad = -5;  // Sin sentido! Una edad negativa no existe
```

Esto rompe la **integridad** del objeto. La encapsulacion resuelve este problema.

### 1.2 Modificadores de acceso

Java tiene 4 niveles de acceso que controlan QUIEN puede ver y usar un atributo o metodo:

| Modificador | Misma clase | Mismo paquete | Subclases | Cualquier lugar |
|------------|:-----------:|:-------------:|:---------:|:---------------:|
| **private** | Si | No | No | No |
| **default** (sin palabra) | Si | Si | No | No |
| **protected** | Si | Si | Si | No |
| **public** | Si | Si | Si | Si |

**Regla practica:** Haz los atributos `private` y solo haz `public` lo que otros necesiten usar.

```java
public class Persona {
    private int edad;      // Solo accesible DENTRO de Persona
    String nombre;         // default: accesible desde el mismo paquete
    protected String dni;  // accesible desde subclases
    public void saludar() { }  // accesible desde cualquier parte
}
```

**Explicacion:**

| Codigo | Que hace |
|--------|----------|
| `private int edad` | Solo los metodos DENTRO de Persona pueden leer/modificar `edad` |
| `String nombre` | Sin modificador = `default`. Visible en el mismo paquete |
| `public void saludar()` | Cualquier clase puede llamar a `saludar()` |

### 1.3 Getters y Setters

Si los atributos son `private`, como los accedemos desde fuera? Con metodos PUBLICOS llamados **getters** (obtener) y **setters** (establecer).

```java
public class Persona {
    private int edad;

    // Getter: devuelve el valor del atributo
    public int getEdad() {
        return edad;
    }

    // Setter: permite modificar el valor CON VALIDACION
    public void setEdad(int edad) {
        if (edad >= 0 && edad <= 150) {  // Validacion!
        this.edad = edad;
        } else {
            System.out.println("Error: edad invalida");
        }
    }
}
```

**Explicacion:**

| Codigo | Que hace |
|--------|----------|
| `private int edad` | Protegemos el atributo. Nadie externo puede tocarlo directamente |
| `public int getEdad()` | Getter: devuelve `edad`. Convencion: `get` + NombreAtributo |
| `public void setEdad(int edad)` | Setter: permite CAMBIAR `edad`, pero con control |
| `if (edad >= 0 && edad <= 150)` | Validacion: solo acepta edades razonables |
| `this.edad = edad` | Solo se asigna si paso la validacion |

**Por que getters y setters y no solo hacer public?**

| Sin encapsulacion (public) | Con encapsulacion (private + getter/setter) |
|---------------------------|---------------------------------------------|
| `p.edad = -5;` // funciona | `p.setEdad(-5);` // valida y rechaza |
| No hay control | Podemos agregar validacion, logs, etc. |
| Si cambiamos internamente, todo se rompe | Podemos cambiar la implementacion sin afectar a quien usa la clase |

### 1.4 Convencion de nombres

| Atributo | Getter | Setter |
|----------|--------|--------|
| `edad` | `getEdad()` | `setEdad(int)` |
| `nombre` | `getNombre()` | `setNombre(String)` |
| `saldo` | `getSaldo()` | `setSaldo(double)` |
| `activo` (boolean) | `isActivo()` o `getActivo()` | `setActivo(boolean)` |

Para booleanos, se usa `is` en vez de `get`: `isActivo()`, `isVisible()`.

### 1.5 Beneficios de la encapsulacion

1. **Control**: Validamos antes de modificar datos
2. **Seguridad**: Protegemos datos sensibles
3. **Flexibilidad**: Podemos cambiar la implementacion interna sin afectar a quien usa la clase
4. **Mantenibilidad**: El codigo queda mas organizado y claro

---

## 2. GLOSARIO DEL TEMA

| Termino | Definicion | Ejemplo |
|---------|------------|---------|
| **Encapsulacion** | Ocultar los datos internos y controlar el acceso mediante metodos | Atributos `private`, getters/setters |
| **Modificador de acceso** | Palabra clave que controla la visibilidad | `private`, `public`, `protected` |
| **private** | Acceso solo desde la misma clase | `private double saldo;` |
| **public** | Acceso desde cualquier clase | `public void metodo()` |
| **Getter** | Metodo que devuelve el valor de un atributo privado | `getNombre()` |
| **Setter** | Metodo que modifica un atributo privado, usualmente con validacion | `setEdad(int)` |
| **Validacion** | Verificar que un dato cumple reglas antes de aceptarlo | `if (edad >= 0)` |
| **Ocultacion** | Esconder la implementacion interna, solo exponer la interfaz | Usuario del objeto no necesita saber como se guardan los datos |

---

## 3. COMPARATIVA ENTRE LENGUAJES

### Atributo privado con getter/setter

| Java | Python | JavaScript |
|------|--------|------------|
| `private int edad;` | `self.__edad = edad` | `#edad = edad` (privada) |
| `public int getEdad()` | `@property` | `get edad()` |
| `    return edad;` | `def edad(self):` | `    return this.#edad` |
| | `    return self.__edad` | |
| `public void setEdad(int e)` | `@edad.setter` | `set edad(valor)` |
| `    if (e >= 0) this.edad = e;` | `def edad(self, e):` | `    if (valor >= 0)` |
| `}` | `    self.__edad = e` | `        this.#edad = valor` |

**Diferencias clave:**
- **Java**: `private` es obligatorio para ocultar. Getters/setters son metodos explicitos
- **Python**: Usa `__` (doble guion bajo) para "name mangling". Usa decoradores `@property` para getters/setters estilo atributo
- **JavaScript**: Usa `#` para campos privados (ES2022+). Getters/setters con `get`/`set`

---

## 4. EJEMPLO GUIADO

### Problema: Cuenta bancaria con validacion

> "Crea una clase `CuentaBancaria` con atributo `saldo` privado. Incluye getter `getSaldo()`, un metodo `depositar(monto)` que solo acepte montos positivos, y un metodo `retirar(monto)` que solo permita retirar si hay saldo suficiente."

---

**Paso 1: Analizar**
- Clase `CuentaBancaria` con 1 atributo privado: `saldo` (double)
- `getSaldo()`: devuelve el saldo actual
- `depositar(double monto)`: solo si monto > 0, aumenta saldo
- `retirar(double monto)`: solo si monto > 0 y monto <= saldo
- Las validaciones evitan estados invalidos

**Paso 2: Pseudocodigo**
```
CLASE CuentaBancaria:
    PRIVATE double saldo

    PUBLIC CuentaBancaria(double saldoInicial):
        this.saldo = saldoInicial   (confiamos en el constructor por ahora)

    PUBLIC double getSaldo():
        return saldo

    PUBLIC void depositar(double monto):
        SI monto > 0:
            saldo = saldo + monto
        SINO:
            imprimir "Error: el monto debe ser positivo"

    PUBLIC void retirar(double monto):
        SI monto > 0 Y monto <= saldo:
            saldo = saldo - monto
        SINO:
            imprimir "Error: saldo insuficiente o monto invalido"

PROGRAMA PRINCIPAL:
    CuentaBancaria c = new CuentaBancaria(1000)
    c.depositar(500)       // saldo: 1500
    c.retirar(200)         // saldo: 1300
    c.retirar(2000)        // Error: saldo insuficiente
    c.depositar(-100)      // Error: monto debe ser positivo
    imprimir c.getSaldo()  // 1300
```

**Paso 3: Codigo completo**
```java
class CuentaBancaria {
    private double saldo;

    public CuentaBancaria(double saldoInicial) {
        saldo = saldoInicial;
    }

    public double getSaldo() {
        return saldo;
    }

    public void depositar(double monto) {
        if (monto > 0) {
            saldo += monto;
        } else {
            System.out.println("Error: el monto a depositar debe ser positivo");
        }
    }

    public void retirar(double monto) {
        if (monto > 0 && monto <= saldo) {
            saldo -= monto;
        } else {
            System.out.println("Error: saldo insuficiente o monto invalido");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        CuentaBancaria c = new CuentaBancaria(1000);

        c.depositar(500);     // OK
        c.retirar(200);       // OK
        System.out.println("Saldo: " + c.getSaldo());  // 1300

        c.retirar(2000);      // Error: saldo insuficiente
        c.depositar(-100);    // Error: monto debe ser positivo
    }
}
```

**Explicacion:**

| Linea | Explicacion |
|-------|-------------|
| `private double saldo;` | Nadie fuera de esta clase puede tocar `saldo` directamente |
| `c.saldo = 5000;` | Esto daria ERROR de compilacion desde fuera. Solo metodos internos pueden modificarlo |
| `public double getSaldo()` | Unico camino para LEER el saldo desde fuera |
| `if (monto > 0)` | Validacion: protegemos contra montos invalidos |
| `saldo += monto;` | Solo se ejecuta si paso la validacion |
| `monto <= saldo` | Validacion combinada: no podemos retirar mas de lo que hay |

**Paso 4: Probar**
```
$ java Main
Saldo: 1300
Error: saldo insuficiente o monto invalido
Error: el monto a depositar debe ser positivo
```

---

## 5. EJERCICIOS

### 🟢 Ejercicio 1: CuentaBancaria (Basico)

Crea una clase `CuentaBancaria` con:
- Atributo `saldo` (private double)
- Getter `getSaldo()`
- Setter `setSaldo(double)` que solo acepte valores >= 0. Si es negativo, imprime `"Error: saldo no puede ser negativo"`

En el `main`, crea una cuenta, asigna saldo 1000, y prueba asignar -50 (debe mostrar error).

**Ejecuta:** `python scripts/runner.py 2 2 1`

---

### 🟡 Ejercicio 2: Producto (Intermedio)

Crea una clase `Producto` con:
- Atributos `nombre` (private String) y `precio` (private double)
- Constructor que reciba nombre y precio (usa el setter para validar)
- Getter y setter para `precio`. El setter rechaza negativos.
- Getter para `nombre`

En el `main`, crea un producto "Laptop" con precio 1500, e intenta crear otro con precio -100.

**Ejecuta:** `python scripts/runner.py 2 2 2`

---

### 🔴 Ejercicio 3: Estudiante (Avanzado)

Crea una clase `Estudiante` con:
- Atributo `notas` (private double[])
- Constructor que reciba el array de notas
- Getter `getNotas()` y setter `setNotas(double[])`
- Metodo `promedio()` que calcule la media

En el `main`, crea un estudiante con notas `{7.5, 8.0, 6.5}` y muestra su promedio.

**Ejecuta:** `python scripts/runner.py 2 2 3`

---

## Soluciones

```bash
python scripts/runner.py 2 2 1 -s
python scripts/runner.py 2 2 2 -s
python scripts/runner.py 2 2 3 -s
```
