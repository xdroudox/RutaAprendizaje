# Control de Flujo

Las estructuras de control permiten dirigir **que hace** tu programa y **cuando** lo hace. Sin ellas, tu programa solo ejecutaria lineas de arriba a abajo, sin tomar decisiones ni repetir cosas.

---

## 1. TEORIA

### 1.1 Condicionales: if / elif / else

Los condicionales permiten ejecutar codigo SOLO si se cumple una condicion. Piensa en ellos como "si pasa X, haz Y; si no, haz Z".

```python
nota = 85

if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
else:
    print("C")
```

**Explicacion linea por linea:**

| Linea | Codigo | Que hace | Por que |
|-------|--------|----------|---------|
| 1 | `nota = 85` | Guarda el valor 85 en la variable `nota` | Necesitamos un dato para evaluar |
| 3 | `if nota >= 90:` | Pregunta: "nota es mayor o igual a 90?" | `if` inicia un condicional. La condicion va seguida de `:` |
| 4 | `print("A")` | Solo se ejecuta si la condicion anterior es `True` | Esta dentro del `if` (indentado) |
| 5 | `elif nota >= 80:` | Si el `if` fue `False`, pregunta otra condicion | `elif` = "else if" (si no, preguntar otra cosa) |
| 6 | `print("B")` | Solo se ejecuta si `elif` es `True` | Valor 85 → 85 >= 80 es True → imprime B |
| 7 | `else:` | Si ninguna condicion anterior fue `True` | `else` no lleva condicion, es el "plan por defecto" |
| 8 | `print("C")` | Se ejecuta solo si todo lo anterior fue `False` | No se ejecuta en este caso |

**Conceptos clave:**
- **Indentacion**: El codigo dentro de `if`, `elif`, `else` debe estar indentado (4 espacios por convencion). Python usa la indentacion para saber que codigo pertenece al bloque.
- **Condicion**: Una expresion que da como resultado `True` o `False`. Usa operadores de comparacion: `>`, `<`, `>=`, `<=`, `==` (igual), `!=` (distinto).
- **Flujo**: Solo UNA rama se ejecuta. Python evalua de arriba a abajo y ejecuta la primera que sea `True`.

### 1.2 Bucle for

El bucle `for` repite codigo para CADA elemento de una secuencia. Es como decir "para cada elemento en esta coleccion, haz esto".

```python
for i in range(5):
    print(i)
```

**Explicacion linea por linea:**

| Linea | Codigo | Que hace | Por que |
|-------|--------|----------|---------|
| 1 | `for i in range(5):` | Crea un bucle que itera 5 veces | `range(5)` genera `[0, 1, 2, 3, 4]`. `i` toma cada valor en cada vuelta |
| 2 | `print(i)` | Imprime el valor actual de `i` | Se ejecuta 5 veces, una por cada valor |

**Resultado:** `0 1 2 3 4`

**Conceptos clave:**
- **range(stop)**: Genera numeros de 0 a stop-1. `range(5)` → `[0, 1, 2, 3, 4]`. El numero que pones es la CANTIDAD, no el valor final.
- **range(start, stop)**: Genera numeros de start a stop-1. `range(2, 6)` → `[2, 3, 4, 5]`.
- **range(start, stop, step)**: Genera numeros saltando de a step. `range(0, 10, 2)` → `[0, 2, 4, 6, 8]`.
- **Variable de iteracion (`i`)**: En cada vuelta del bucle, `i` toma el siguiente valor de la secuencia. El nombre `i` es convencion (de "index"), pero podria ser cualquier nombre.
- **Off-by-one error**: Error comun por olvidar que `range(n)` da 0 a n-1, no 0 a n. Si quieres 1 a 10, usa `range(1, 11)`.

### 1.3 Bucle while

El bucle `while` repite codigo MIENTRAS una condicion sea `True`. Es como decir "sigue haciendo esto mientras pase X".

```python
contador = 0
while contador < 3:
    print(contador)
    contador += 1
```

**Explicacion linea por linea:**

| Linea | Codigo | Que hace | Por que |
|-------|--------|----------|---------|
| 1 | `contador = 0` | Inicializa una variable en 0 | Necesitamos un valor inicial para la condicion |
| 2 | `while contador < 3:` | Verifica: "contador es menor que 3?" | Si es True, ejecuta el bloque. Si es False, termina el bucle |
| 3 | `print(contador)` | Imprime el valor actual | Muestra 0, luego 1, luego 2 |
| 4 | `contador += 1` | Incrementa contador en 1 | Esto es `contador = contador + 1`. SIN ESTO, el bucle seria infinito |

**Resultado:** `0 1 2`

**Conceptos clave:**
- **Bucle infinito**: Si la condicion nunca se vuelve `False`, el bucle se ejecuta para siempre. Siempre asegurate de que algo cambie dentro del bucle para que la condicion eventualmente sea `False`.
- **Diferencia for vs while**: `for` se usa cuando SABES cuantas veces repetir (o tienes una lista de elementos). `while` se usa cuando NO SABES cuantas veces (ej: "sigue pidiendo al usuario hasta que acierte").

### 1.4 break y continue

Dos instrucciones especiales para controlar bucles desde adentro:

```python
# break: SALTA fuera del bucle inmediatamente
for i in range(10):
    if i == 5:
        break      # Termina el bucle cuando i es 5
    if i % 2 == 0:
        continue   # Salta a la siguiente iteracion (no ejecuta el print)
    print(i)
```

**Explicacion:**

| Codigo | Que hace |
|--------|----------|
| `break` | Termina el bucle por completo. El programa sigue ejecutando lo que este despues del bucle |
| `continue` | Salta a la siguiente iteracion. Ignora el resto del codigo en esta vuelta |

**Conceptos clave:**
- `break` es util para salir de un bucle cuando encuentras lo que buscas (ej: "adivina el numero")
- `continue` es util para saltarte casos que no te interesan (ej: "procesa solo los numeros pares, saltate los impares")

---

## 2. GLOSARIO DEL TEMA

| Termino | Definicion | Ejemplo |
|---------|------------|---------|
| **Condicion** | Expresion que da `True` o `False` | `edad >= 18` |
| **Operador de comparacion** | Simbolo que compara dos valores: `==`, `!=`, `>`, `<`, `>=`, `<=` | `5 > 3` → `True` |
| **Bloque de codigo** | Conjunto de lineas indentadas que se ejecutan juntas | Todo lo indentado bajo un `if` |
| **Indentacion** | Espacios al inicio de la linea (4 por nivel). Python la usa para agrupar bloques | `    print("hola")` |
| **Iterar** | Repetir un proceso sobre cada elemento de una coleccion | "Iterar sobre una lista" = "recorrer cada elemento" |
| **Variable de iteracion** | Variable que toma cada valor de la secuencia en cada vuelta | `i` en `for i in range(5):` |
| **Incrementar** | Aumentar el valor de una variable | `contador += 1` |
| **Off-by-one error** | Error por calcular mal los limites (off-by-one = "desviado por uno") | Usar `range(10)` cuando quieres 1-10 |
| **Bucle infinito** | Bucle que nunca termina porque la condicion siempre es `True` | `while True:` sin un `break` |
| **Flag / Bandera** | Variable booleana que controla el flujo de un programa | `encontrado = False` → se vuelve `True` cuando encuentras algo |

---

## 3. COMPARATIVA ENTRE LENGUAJES

### Condicional if

| Python | Java | JavaScript |
|--------|------|------------|
| `if x > 5:` | `if (x > 5) {` | `if (x > 5) {` |
| `    print("mayor")` | `    System.out.println("mayor");` | `    console.log("mayor");` |
| `elif x > 2:` | `} else if (x > 2) {` | `} else if (x > 2) {` |
| `    print("medio")` | `    System.out.println("medio");` | `    console.log("medio");` |
| `else:` | `} else {` | `} else {` |
| `    print("menor")` | `    System.out.println("menor");` | `    console.log("menor");` |

**Diferencias clave:**
- Los parentesis alrededor de la condicion son OBLIGATORIOS en Java y JS, OPCIONALES en Python
- Las llaves `{}` delimitan bloques en Java y JS; en Python se usa indentacion
- `elif` es exclusivo de Python; en Java/JS es `else if` (dos palabras)
- El `:` al final de `if`, `elif`, `else` es exclusivo de Python

### Bucle for (rango)

| Python | Java | JavaScript |
|--------|------|------------|
| `for i in range(5):` | `for (int i = 0; i < 5; i++) {` | `for (let i = 0; i < 5; i++) {` |
| `    print(i)` | `    System.out.println(i);` | `    console.log(i);` |
| (sin llaves, usa indentacion) | `}` | `}` |

**Diferencias clave:**
- Python: `range(5)` es una funcion que genera la secuencia. Simple, legible.
- Java: `for (int i = 0; i < 5; i++)` tienes que manejar: inicializacion (`int i = 0`), condicion (`i < 5`), e incremento (`i++`) explicitamente.
- JS: Igual que Java pero con `let` en vez de `int`.
- **Patron comun**: Todos hacen lo mismo (0, 1, 2, 3, 4). Cambia la sintaxis, no la logica.

### Bucle while

| Python | Java | JavaScript |
|--------|------|------------|
| `while x < 5:` | `while (x < 5) {` | `while (x < 5) {` |
| `    print(x)` | `    System.out.println(x);` | `    console.log(x);` |
| `    x += 1` | `    x++;` | `    x++;` |

### break y continue

Los tres lenguajes soportan `break` y `continue` exactamente con la misma sintaxis y significado. Lo unico que cambia es que en Java/JS los bloques van entre `{}`.

---

## 4. EJEMPLO GUIADO

Vamos a resolver un problema paso a paso, explicando CADA decision.

### Problema: Sumar solo los numeros pares del 1 al 10

> "Escribe un programa que sume todos los numeros pares entre 1 y 10 y muestre el resultado"

---

### Paso 1: Analizar el problema

Primero, entendamos que nos pide:

| Pregunta | Respuesta |
|----------|-----------|
| Que datos tenemos? | Numeros del 1 al 10 |
| Que son "pares"? | Numeros divisibles por 2 (resto = 0) |
| Que operacion? | Sumar |
| Que mostrar? | El resultado final |

Desglosemos: necesitamos:
1. Una forma de generar los numeros 1, 2, 3, ..., 10 → `range(1, 11)`
2. Una forma de identificar pares → `numero % 2 == 0`
3. Una variable para acumular la suma → `total = 0` y luego `total += numero`
4. Mostrar el resultado → `print(total)`

---

### Paso 2: Escribir pseudocodigo

El pseudocodigo es el programa escrito en lenguaje humano. No es codigo real, es el plan:

```
total = 0

PARA CADA numero desde 1 hasta 10:
    SI numero es par:
        total = total + numero

MOSTRAR total
```

Esto es mas facil de leer que el codigo real. Deberias poder escribir esto ANTES de programar.

---

### Paso 3: Traducir a codigo (con explicacion de CADA linea)

```python
# 1. Inicializamos el acumulador
total = 0

# 2. Recorremos los numeros del 1 al 10
for numero in range(1, 11):
    # 3. Preguntamos si es par
    if numero % 2 == 0:
        # 4. Si es par, lo sumamos al total
        total += numero

# 5. Mostramos el resultado
print(total)
```

**Explicacion linea por linea:**

| Linea | Codigo | Explicacion |
|-------|--------|-------------|
| 2 | `total = 0` | Creamos una variable llamada `total` y le asignamos 0. Es nuestro "acumulador". |
| 4 | `for numero in range(1, 11):` | `range(1, 11)` genera `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`. El bucle se ejecutara una vez por cada numero. La variable `numero` tomara cada valor en cada iteracion. |
| 6 | `if numero % 2 == 0:` | El operador `%` (modulo) da el RESTO de la division. Si un numero es par, dividirlo por 2 da resto 0. Ej: `4 % 2 = 0` (4/2=2, resto 0). `5 % 2 = 1` (5/2=2, resto 1). |
| 8 | `total += numero` | Esto es equivalente a `total = total + numero`. Toma el valor actual de `total`, le suma `numero`, y guarda el resultado en `total`. |
| 10 | `print(total)` | Muestra el valor final: `30` |

---

### Paso 4: Probar

Si ejecutamos el programa:

```python
# Iteracion 1: numero = 1 → 1 % 2 != 0 → no suma
# Iteracion 2: numero = 2 → 2 % 2 == 0 → total = 0 + 2 = 2
# Iteracion 3: numero = 3 → 3 % 2 != 0 → no suma
# Iteracion 4: numero = 4 → 4 % 2 == 0 → total = 2 + 4 = 6
# Iteracion 5: numero = 5 → 5 % 2 != 0 → no suma
# Iteracion 6: numero = 6 → 6 % 2 == 0 → total = 6 + 6 = 12
# Iteracion 7: numero = 7 → 7 % 2 != 0 → no suma
# Iteracion 8: numero = 8 → 8 % 2 == 0 → total = 12 + 8 = 20
# Iteracion 9: numero = 9 → 9 % 2 != 0 → no suma
# Iteracion 10: numero = 10 → 10 % 2 == 0 → total = 20 + 10 = 30

# Resultado: 30
```

**Verificacion manual:** 2 + 4 + 6 + 8 + 10 = 30. Correcto!

---

### Paso 5: Posibles errores y como evitarlos

| Error | Por que pasa | Como evitarlo |
|-------|-------------|---------------|
| `range(10)` en vez de `range(1, 11)` | Empieza en 0 y termina en 9 | Recuerda: `range(stop)` va de 0 a stop-1. `range(start, stop)` va de start a stop-1 |
| `numero % 2 == 1` para pares | Estás detectando impares, no pares | Par → resto 0. Impar → resto 1 |
| `total = numero` en vez de `total += numero` | Sobrescribes el acumulador en vez de sumar | `+=` significa "suma a lo que ya hay" |
| Olvidar inicializar `total = 0` | La variable no existe cuando intentas sumarle | Siempre inicializa los acumuladores antes del bucle |

---

## 5. EJERCICIOS

### 🟢 Ejercicio 1: Clasificador de notas (Basico)

Pide una nota numerica (0-100) y muestra la calificacion: A (90-100), B (80-89), C (70-79), D (60-69), F (<60). Valida que la nota este en rango.

**Conceptos que aplicas:** `input()`, `int()`, `if/elif/else`, validacion.

**Ejecuta:** `python scripts/runner.py 1 4 1`

**Pistas si te atascas:**
```bash
python scripts/runner.py 1 4 1 -p 1
python scripts/runner.py 1 4 1 -p 2
python scripts/runner.py 1 4 1 -p 3
```

---

### 🟡 Ejercicio 2: Tabla de multiplicar formateada (Intermedio)

Pide un numero y muestra su tabla de multiplicar del 1 al 10 usando un bucle `for`. Cada linea debe mostrar: `NUM x i = RESULTADO`. Ademas, si el resultado es multiplo de 5, muestra un asterisco al final.

**Ejemplo de salida:**
```
5 x 1 = 5 *
5 x 2 = 10
5 x 3 = 15 *
...
```

**Conceptos que aplicas:** `for`, `range()`, `f-strings`, operador `%`, `if` dentro de un bucle.

**Ejecuta:** `python scripts/runner.py 1 4 2`

---

### 🔴 Ejercicio 3: Juego de adivinar con limite de intentos (Avanzado)

El programa genera un numero aleatorio entre 1 y 20. El usuario debe adivinarlo. Por cada intento:
- Si acierta: mensaje de felicitaciones y termina
- Si falla: pista de "mayor" o "menor", y se resta un intento
- El usuario tiene 5 intentos maximos
- Si se quedan sin intentos: mensaje de game over y muestra el numero secreto
- Al final: preguntar si quiere jugar de nuevo

**Conceptos que aplicas:** `while`, `if/elif/else`, `random.randint()`, `break`, variable contador, bucle anidado, validacion de entrada.

**Ejecuta:** `python scripts/runner.py 1 4 3`

---

## Soluciones

```bash
python scripts/runner.py 1 4 1 -s
python scripts/runner.py 1 4 2 -s
python scripts/runner.py 1 4 3 -s
```
