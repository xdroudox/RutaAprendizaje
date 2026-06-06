# Variables y Tipos de Datos

Las **variables** son como "cajas" donde guardas informacion. Cada variable tiene un **nombre** que la identifica y un **tipo** de dato que indica que clase de informacion contiene.

---

## 1. TEORIA

### 1.1 Que es una variable?

Una variable es un espacio en la memoria de la computadora que tiene:

- **Nombre**: Como la etiqueta de la caja (ej: `edad`, `nombre`)
- **Valor**: El dato guardado (ej: `25`, `"Ana"`)
- **Tipo**: Que clase de dato es (numero, texto, etc.)

```python
nombre = "Ana"    # str (texto)
edad = 25          # int (entero)
altura = 1.65      # float (decimal)
activo = True      # bool (booleano)
```

**Explicacion:**

| Codigo | Que hace | La variable... |
|--------|----------|----------------|
| `nombre = "Ana"` | Guarda el texto "Ana" en la variable `nombre` | Es tipo `str` (string = cadena de texto) |
| `edad = 25` | Guarda el numero 25 en la variable `edad` | Es tipo `int` (integer = entero) |
| `altura = 1.65` | Guarda el decimal 1.65 en `altura` | Es tipo `float` (numero de punto flotante) |
| `activo = True` | Guarda el valor verdadero en `activo` | Es tipo `bool` (booleano: True o False) |

**Analogia:** Una variable es como una caja con una etiqueta. La etiqueta es el nombre, lo que hay dentro es el valor. El tipo es si la caja contiene libros (texto), canicas (numeros), o un interruptor (booleano).

### 1.2 Reglas para nombrar variables

| Regla | Ejemplo correcto | Ejemplo incorrecto |
|-------|------------------|--------------------|
| Solo letras, numeros y _ | `mi_variable` | `mi-variable` |
| No empezar con numero | `variable1` | `1variable` |
| No usar palabras reservadas | `nombre` | `class` (es palabra reservada) |
| Sensible a mayusculas | `Edad` y `edad` son diferentes | — |
| Usar snake_case en Python | `mi_variable` | `miVariable` (eso es camelCase, se usa en JS) |

### 1.3 Tipos de datos basicos

| Tipo | Que guarda | Ejemplos |
|------|-----------|----------|
| `int` | Numeros enteros (sin decimales) | `42`, `-5`, `0`, `1000` |
| `float` | Numeros decimales | `3.14`, `-0.5`, `1.0` |
| `str` | Texto (entre comillas) | `"Hola"`, `'Python'`, `"123"` |
| `bool` | Verdadero o Falso | `True`, `False` |

### 1.4 Conversion entre tipos (type casting)

A veces necesitas convertir un tipo a otro:

```python
int("25")        # "25" (str) → 25 (int)
str(100)         # 100 (int) → "100" (str)
float("3.14")    # "3.14" (str) → 3.14 (float)
bool(1)          # 1 (int) → True (bool). 0 → False
```

**Por que es util?** `input()` siempre devuelve texto (`str`). Si quieres hacer operaciones matematicas, debes convertir a `int` o `float`.

```python
edad_texto = input("Cuantos anos tienes? ")  # "25" (str)
edad = int(edad_texto)                       # 25 (int)
dias = edad * 365                            # 9125 (funciona porque ahora es int)
```

### 1.5 La funcion type()

`type()` te dice de que tipo es cualquier valor o variable:

```python
print(type(25))       # <class 'int'>
print(type("Hola"))   # <class 'str'>
print(type(True))     # <class 'bool'>
```

---

## 2. GLOSARIO DEL TEMA

| Termino | Definicion | Ejemplo |
|---------|------------|---------|
| **Variable** | "Caja" con nombre para guardar datos | `edad = 25` |
| **Valor** | El dato guardado en la variable | `25` |
| **Tipo de dato** | Categoria del valor (int, str, float, bool) | `type(25)` → `int` |
| **Asignacion** | Operacion de guardar un valor en una variable | `=` en `x = 5` |
| **String / str** | Tipo para texto | `"Hola"` |
| **Entero / int** | Tipo para numeros sin decimales | `42` |
| **Float** | Tipo para numeros con decimales | `3.14` |
| **Booleano / bool** | Tipo para verdadero/falso | `True`, `False` |
| **Type casting** | Convertir un tipo a otro | `int("25")` |
| **Palabra reservada** | Palabra que Python usa para su sintaxis, no puedes usarla como variable | `if`, `for`, `class`, `return` |
| **Snake case** | Convencion de nombres en Python: palabras separadas por _ | `mi_variable` |

---

## 3. COMPARATIVA ENTRE LENGUAJES

### Declarar variables

| Operacion | Python | Java | JavaScript |
|-----------|--------|------|------------|
| Entero | `edad = 25` | `int edad = 25;` | `let edad = 25;` |
| Texto | `nombre = "Ana"` | `String nombre = "Ana";` | `let nombre = "Ana";` |
| Decimal | `precio = 1.99` | `double precio = 1.99;` | `let precio = 1.99;` |
| Booleano | `activo = True` | `boolean activo = true;` | `let activo = true;` |
| Constante | `PI = 3.14` (convencion) | `final double PI = 3.14;` | `const PI = 3.14;` |

**Diferencias clave:**
- **Python**: No declaras el tipo. El tipo se INFIERE del valor.
- **Java**: DECLARAS el tipo explicitamente (`int edad`). Si pones un texto ahi, error de compilacion.
- **JavaScript**: Usas `let` para declarar (moderno). El tipo se infiere como en Python.

Python es el mas flexible para empezar.

### Conversion de tipos

| Python | Java | JavaScript |
|--------|------|------------|
| `int("25")` | `Integer.parseInt("25")` | `parseInt("25")` |
| `str(100)` | `String.valueOf(100)` | `String(100)` |
| `float("3.14")` | `Double.parseDouble("3.14")` | `parseFloat("3.14")` |

---

## 4. EJEMPLO GUIADO

### Problema: Convertir temperatura de Celsius a Fahrenheit

> "Pide una temperatura en grados Celsius y muestrala en Fahrenheit. La formula es: F = C * 9/5 + 32"

---

**Paso 1: Analizar**
- Entrada: temperatura en Celsius (numero, posiblemente decimal)
- Proceso: aplicar formula F = C * 9/5 + 32
- Salida: temperatura en Fahrenheit

**Paso 2: Pseudocodigo**
```
PEDIR celsius
fahrenheit = celsius * 9/5 + 32
MOSTRAR fahrenheit
```

**Paso 3: Codigo**
```python
celsius = float(input("Temperatura en Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius}°C = {fahrenheit}°F")
```

**Explicacion:**
1. `float(input(...))` — Usamos float porque la temperatura puede tener decimales (36.5°C)
2. `celsius * 9 / 5 + 32` — Respetamos el orden de operaciones: multiplicacion y division primero, luego suma
3. `f"...{celsius}°C = {fahrenheit}°F"` — Mostramos ambos valores con el formato "X°C = Y°F"

**Prueba:** Si celsius = 0 → 0 * 9/5 + 32 = 32°F. Si celsius = 100 → 100 * 9/5 + 32 = 212°F. Correcto!

---

## 5. EJERCICIOS

### 🟢 Ejercicio 1: Presentacion personal (Basico)

Crea variables para tu nombre, edad y ciudad. Luego muestralas en una presentacion usando f-strings.

**Ejemplo:** "Hola, me llamo Ana, tengo 25 anos y vivo en Madrid"

**Conceptos que aplicas:** Variables, `input()`, f-strings.

**Ejecuta:** `python scripts/runner.py 1 2 1`

---

### 🟡 Ejercicio 2: Edad en dias (Intermedio)

Pide la edad de una persona en anos y calcula cuantos dias ha vivido aproximadamente (edad * 365). Muestra el resultado.

**Conceptos que aplicas:** `input()`, `int()`, multiplicacion, f-strings.

**Ejecuta:** `python scripts/runner.py 1 2 2`

---

### 🔴 Ejercicio 3: Detector de tipos (Avanzado)

Pide 3 valores al usuario (sin convertir) y muestra el tipo de cada uno usando `type()`. Explica por que todos son `str` aunque el usuario escriba numeros.

**Conceptos que aplicas:** `input()`, `type()`, entender que input() siempre devuelve str.

**Ejecuta:** `python scripts/runner.py 1 2 3`

---

## Soluciones

```bash
python scripts/runner.py 1 2 1 -s
python scripts/runner.py 1 2 2 -s
python scripts/runner.py 1 2 3 -s
```
