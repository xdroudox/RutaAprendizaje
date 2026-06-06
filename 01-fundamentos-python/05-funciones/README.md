# Funciones

Las **funciones** son bloques de codigo REUTILIZABLES con un nombre. En vez de escribir el mismo codigo varias veces, escribes una funcion y la llamas cuando la necesites.

---

## 1. TEORIA

### 1.1 Que es una funcion?

Una funcion es como una "mini-programa" dentro de tu programa: recibe datos (parametros), hace algo con ellos, y opcionalmente devuelve un resultado.

```python
def suma(a, b):
    return a + b
```

**Explicacion:**

| Parte | Codigo | Significado |
|-------|--------|-------------|
| Definicion | `def suma(a, b):` | `def` crea la funcion. `suma` es su nombre. `a` y `b` son parametros |
| Cuerpo | `return a + b` | El codigo que ejecuta. `return` devuelve el resultado |
| Llamada | `resultado = suma(5, 3)` | Ejecuta la funcion con valores reales (argumentos) |

**Analogia:** Una funcion es como un microondas. Le pones comida (parametros), seleccionas el tiempo, y te devuelve comida caliente (return). No necesitas saber como funciona internamente, solo sabes que recibe X y devuelve Y.

### 1.2 Parametros vs Argumentos

```python
def saludar(nombre="Invitado"):   # "nombre" es PARAMETRO
    print(f"Hola, {nombre}!")

saludar("Ana")                     # "Ana" es ARGUMENTO
saludar()                          # Usa el valor por defecto: "Invitado"
```

- **Parametro**: Variable que la funcion RECIBE (en la definicion)
- **Argumento**: Valor que la funcion RECIBE (en la llamada)
- **Valor por defecto**: Si no pasas argumento, usa este valor (`= "Invitado"`)

### 1.3 Return vs Print

Diferencia FUNDAMENTAL:

```python
# Con return: devuelve un valor que puedes USAR
def suma(a, b):
    return a + b

resultado = suma(5, 3)  # resultado = 8
print(resultado * 2)     # 16

# Sin return: solo muestra, no puedes usar el valor
def mostrar_suma(a, b):
    print(a + b)

resultado = mostrar_suma(5, 3)  # Muestra 8, pero resultado = None
print(resultado * 2)            # Error! None * 2 no funciona
```

**Regla:** Si necesitas el valor para algo mas, usa `return`. Si solo quieres mostrar algo en pantalla, usa `print`.

### 1.4 Scope (Ambito) de variables

Las variables dentro de una funcion SOLO existen dentro de esa funcion:

```python
def mi_funcion():
    x = 10          # x existe SOLO aqui dentro
    print(x)        # 10

mi_funcion()
print(x)            # ERROR! x no existe fuera de la funcion
```

**Conceptos clave:**
- **Variable local**: Creada dentro de una funcion. Solo existe alli.
- **Variable global**: Creada fuera de las funciones. Existe en todo el programa (evitar si es posible).
- **Variable global**: Se puede LEER dentro de una funcion, pero no MODIFICAR (a menos que uses `global`)

### 1.5 Funciones Lambda

Funciones ANONIMAS (sin nombre) de una sola linea:

```python
# Funcion normal
def cuadrado(x):
    return x ** 2

# Lambda equivalente
cuadrado = lambda x: x ** 2

print(cuadrado(5))  # 25
```

**Sintaxis:** `lambda parametros: expresion`

Las lambdas se usan con funciones como `filter()` y `map()`:

```python
numeros = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4]
```

`filter()` aplica la funcion lambda a cada elemento. Si la lambda devuelve True, el elemento se incluye en el resultado.

---

## 2. GLOSARIO DEL TEMA

| Termino | Definicion | Ejemplo |
|---------|------------|---------|
| **Funcion** | Bloque de codigo reutilizable con nombre | `def suma(a, b):` |
| **Parametro** | Variable que recibe la funcion (al definirla) | `a` y `b` en `def suma(a, b):` |
| **Argumento** | Valor que pasas a la funcion (al llamarla) | `5` y `3` en `suma(5, 3)` |
| **Return** | Palabra que devuelve un valor desde la funcion | `return resultado` |
| **Llamar / Invocar** | Ejecutar una funcion | `suma(5, 3)` |
| **Scope / Ambito** | Region donde una variable existe | Una variable dentro de una funcion solo existe alli |
| **Variable local** | Variable que solo existe dentro de una funcion | `x` dentro de `def f(): x = 10` |
| **Lambda** | Funcion anonima de una sola expresion | `lambda x: x * 2` |
| **Parametro por defecto** | Valor que se usa si no se pasa argumento | `def f(x=5):` |

---

## 3. COMPARATIVA ENTRE LENGUAJES

### Definir y llamar funciones

| Python | Java | JavaScript |
|--------|------|------------|
| `def suma(a, b):` | `public static int suma(int a, int b) {` | `function suma(a, b) {` |
| `    return a + b` | `    return a + b;` | `    return a + b;` |
| (indentacion) | `}` | `}` |
| `suma(5, 3)` | `suma(5, 3);` | `suma(5, 3);` |

### Lambda / Funcion anonima

| Python | Java | JavaScript |
|--------|------|------------|
| `lambda x: x*2` | `x -> x * 2` | `x => x * 2` |

**Diferencia clave:** En Java las funciones DEBEN estar dentro de una clase. En Python y JS pueden estar "sueltas".

---

## 4. EJEMPLO GUIADO

### Problema: Calculadora con funciones

> "Crea funciones para sumar, restar, multiplicar y dividir. Luego pide 2 numeros y una operacion al usuario, y muestra el resultado usando las funciones."

---

**Paso 1: Analizar**
- Necesitamos 4 funciones: sumar, restar, multiplicar, dividir
- Cada una recibe 2 numeros y devuelve un resultado
- El menu pide operacion y numeros

**Paso 2: Codigo**
```python
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

# Programa principal
num1 = float(input("Primer numero: "))
num2 = float(input("Segundo numero: "))

print(f"{num1} + {num2} = {sumar(num1, num2)}")
print(f"{num1} - {num2} = {restar(num1, num2)}")
print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
print(f"{num1} / {num2} = {dividir(num1, num2)}")
```

**Explicacion:**
1. Cada funcion tiene una RESPONSABILIDAD UNICA (hace una sola cosa)
2. `return` devuelve el resultado para que el programa principal lo use
3. En `dividir()`, validamos que `b != 0` antes de dividir
4. El programa llama a las funciones y usa los valores devueltos en los f-strings

---

## 5. EJERCICIOS

### 🟢 Ejercicio 1: Funcion suma (Basico)

Crea una funcion que reciba 2 numeros como parametros y devuelva su suma. Luego pide dos numeros al usuario, llama a la funcion y muestra el resultado.

**Conceptos que aplicas:** `def`, `return`, `parametros`, llamar a una funcion.

**Ejecuta:** `python scripts/runner.py 1 5 1`

---

### 🟡 Ejercicio 2: Funcion promedio (Intermedio)

Crea una funcion que reciba una lista de numeros (con cualquier cantidad de elementos) y devuelva el promedio. Usa `sum()` y `len()`.

**Conceptos que aplicas:** Funcion con parametro tipo lista, `sum()`, `len()`.

**Ejecuta:** `python scripts/runner.py 1 5 2`

---

### 🔴 Ejercicio 3: Filtrar pares con lambda (Avanzado)

Usa `filter()` con una `lambda` para obtener solo los numeros pares de una lista dada. La lista debe pedirse al usuario (numeros separados por espacio).

**Conceptos que aplicas:** `lambda`, `filter()`, `list()`, `split()`, `map()`.

**Ejecuta:** `python scripts/runner.py 1 5 3`

---

## Soluciones

```bash
python scripts/runner.py 1 5 1 -s
python scripts/runner.py 1 5 2 -s
python scripts/runner.py 1 5 3 -s
```
