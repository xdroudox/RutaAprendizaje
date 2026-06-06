# Operadores y Expresiones

Los **operadores** son simbolos que realizan operaciones con valores. Las **expresiones** son combinaciones de valores y operadores que producen un resultado.

---

## 1. TEORIA

### 1.1 Operadores Aritmeticos

Realizan operaciones matematicas basicas:

```python
print(10 + 3)    # 13  - SUMA
print(10 - 3)    # 7   - RESTA
print(10 * 3)    # 30  - MULTIPLICACION
print(10 / 3)    # 3.3333 - DIVISION REAL (siempre da decimal)
print(10 // 3)   # 3   - DIVISION ENTERA (trunca decimales)
print(10 % 3)    # 1   - MODULO (resto de la division)
print(2 ** 3)    # 8   - POTENCIA (2 elevado a 3)
```

**Explicacion de cada uno:**

| Operador | Nombre | Que hace | Ejemplo | Resultado |
|----------|--------|----------|---------|-----------|
| `+` | Suma | Suma dos numeros | `5 + 3` | `8` |
| `-` | Resta | Resta dos numeros | `5 - 3` | `2` |
| `*` | Multiplicacion | Multiplica dos numeros | `5 * 3` | `15` |
| `/` | Division real | Divide y da resultado DECIMAL | `10 / 3` | `3.3333` |
| `//` | Division entera | Divide y trunca decimales | `10 // 3` | `3` |
| `%` | Modulo | Da el RESTO de la division | `10 % 3` | `1` |
| `**` | Potencia | Eleva al exponente | `2 ** 3` | `8` |

**Division entera vs Modulo:** Son complementos. `10 // 3 = 3` porque 3 cabe 3 veces en 10. `10 % 3 = 1` porque sobran 1 para llegar a 10. Siempre se cumple: `(a // b) * b + (a % b) == a`

### 1.2 Operadores de Comparacion

Comparan dos valores y devuelven `True` o `False`:

```python
print(5 == 5)    # True  - IGUAL QUE
print(5 != 3)    # True  - DISTINTO DE
print(5 > 3)     # True  - MAYOR QUE
print(5 < 3)     # False - MENOR QUE
print(5 >= 5)    # True  - MAYOR O IGUAL
print(5 <= 3)    # False - MENOR O IGUAL
```

**Cuidado:** `=` es ASIGNACION (guarda un valor). `==` es COMPARACION (pregunta si son iguales). Confundirlos es el error mas comun en programacion.

### 1.3 Operadores Logicos

Combinan condiciones:

```python
print(True and False)   # False - AND: ambas deben ser True
print(True or False)    # True  - OR: al menos una debe ser True
print(not True)         # False - NOT: invierte (True → False, False → True)
```

**Ejemplos practicos:**

```python
edad = 20
tiene_licencia = True

# AND: ambas condiciones deben cumplirse
if edad >= 18 and tiene_licencia:
    print("Puede conducir")  # Se ejecuta porque ambas son True

# OR: al menos una debe cumplirse
if edad < 12 or edad > 80:
    print("No recomendado")  # No se ejecuta (20 no es <12 ni >80)

# NOT: invierte
if not tiene_licencia:     # Es lo mismo que: if tiene_licencia == False:
    print("No tiene licencia")
```

### 1.4 Precedencia de Operadores (Orden de evaluacion)

Igual que en matematicas, algunos operadores se evaluan antes que otros:

1. Parentesis `()`
2. Potencia `**`
3. Multiplicacion, division, modulo `*`, `/`, `//`, `%`
4. Suma, resta `+`, `-`
5. Comparacion `<`, `>`, `==`, `!=`, `<=`, `>=`
6. Logicos: `not`, `and`, `or`

```python
resultado = 5 + 3 * 2      # 5 + 6 = 11  (multiplicacion primero)
resultado = (5 + 3) * 2    # 8 * 2 = 16  (parentesis primero)
```

**Regla practica:** Cuando tengas dudas, USA PARENTESIS. Hacen el codigo mas legible.

---

## 2. GLOSARIO DEL TEMA

| Termino | Definicion | Ejemplo |
|---------|------------|---------|
| **Operador** | Simbolo que realiza una operacion | `+`, `-`, `*`, `/` |
| **Expresion** | Combinacion de valores y operadores que da un resultado | `(5 + 3) * 2` → `16` |
| **Modulo / %** | Operador que da el resto de una division | `10 % 3` → `1` |
| **Division entera //** | Division que trunca los decimales | `10 // 3` → `3` |
| **Precedencia** | Orden en que se evaluan los operadores | `*` antes que `+` |
| **Boolean** | Tipo de dato que solo puede ser True o False | `5 > 3` → `True` |
| **Cortocircuito** | Cuando Python deja de evaluar porque ya sabe el resultado | `False and ...` → ni evalua lo siguiente |

---

## 3. COMPARATIVA ENTRE LENGUAJES

### Operadores aritmeticos

| Operacion | Python | Java | JavaScript |
|-----------|--------|------|------------|
| Suma | `+` | `+` | `+` |
| Resta | `-` | `-` | `-` |
| Multiplicacion | `*` | `*` | `*` |
| Division real | `/` | `/` | `/` |
| Division entera | `//` | `int / int` (si ambos son int) | `Math.floor(a / b)` |
| Modulo | `%` | `%` | `%` |
| Potencia | `**` | `Math.pow(a, b)` | `Math.pow(a, b)` o `**` (ES7+) |

### Operadores logicos

| Python | Java | JavaScript | Significado |
|--------|------|------------|-------------|
| `and` | `&&` | `&&` | Y logico |
| `or` | `\|\|` | `\|\|` | O logico |
| `not` | `!` | `!` | Negacion |

**Dato curioso:** Python es el unico que usa palabras (`and`, `or`, `not`) mientras que Java y JS usan simbolos (`&&`, `||`, `!`).

---

## 4. EJEMPLO GUIADO

### Problema: Calcular si un numero es par y multiplo de 5

> "Pide un numero al usuario y muestra si es par y multiplo de 5 al mismo tiempo. Si no lo es, muestra que condicion no cumple."

---

**Paso 1: Analizar**
- Necesitamos saber si el numero es: par (`num % 2 == 0`) Y multiplo de 5 (`num % 5 == 0`)
- Si solo es par: "Es par pero no multiplo de 5"
- Si solo es multiplo de 5: "Es multiplo de 5 pero no es par"
- Si ninguna: "No es par ni multiplo de 5"

**Paso 2: Pseudocodigo**
```
PEDIR numero

SI numero % 2 == 0 Y numero % 5 == 0:
    MOSTRAR "Es par y multiplo de 5"
SINO SI numero % 2 == 0:
    MOSTRAR "Solo es par"
SINO SI numero % 5 == 0:
    MOSTRAR "Solo es multiplo de 5"
SINO:
    MOSTRAR "No es ninguno"
```

**Paso 3: Codigo**
```python
num = int(input("Ingresa un numero: "))

if num % 2 == 0 and num % 5 == 0:
    print(f"{num} es par y multiplo de 5")
elif num % 2 == 0:
    print(f"{num} es par pero no multiplo de 5")
elif num % 5 == 0:
    print(f"{num} es multiplo de 5 pero no es par")
else:
    print(f"{num} no es par ni multiplo de 5")
```

**Explicacion:**
1. `num % 2 == 0` — Verifica si es par (resto 0 al dividir por 2)
2. `num % 5 == 0` — Verifica si es multiplo de 5 (resto 0 al dividir por 5)
3. `and` — Ambas condiciones deben ser True
4. El orden de los elif importa: la condicion mas especifica va primero

---

## 5. EJERCICIOS

### 🟢 Ejercicio 1: Calculadora de propina (Basico)

Pide el total de la cuenta y el porcentaje de propina. Calcula: el monto de propina y el total a pagar (cuenta + propina).

**Formula:** `propina = total * porcentaje / 100`

**Conceptos que aplicas:** `float()`, multiplicacion, division, suma, f-strings.

**Ejecuta:** `python scripts/runner.py 1 3 1`

---

### 🟡 Ejercicio 2: Ano bisiesto (Intermedio)

Pide un ano y determina si es bisiesto. Regla: un ano es bisiesto si es divisible entre 4, EXCEPTO si es divisible entre 100 (a menos que tambien sea divisible entre 400).

**Formula:** `(año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)`

**Conceptos que aplicas:** `%`, `and`, `or`, operadores combinados.

**Ejecuta:** `python scripts/runner.py 1 3 2`

---

### 🔴 Ejercicio 3: Verificar triangulo (Avanzado)

Pide 3 numeros (lados) y verifica si pueden formar un triangulo. La condicion es: la suma de DOS lados debe ser MAYOR que el tercero, para TODAS las combinaciones.

**Condicion:** `a + b > c and a + c > b and b + c > a`

**Conceptos que aplicas:** `float()`, operadores de comparacion, `and`, validacion multiple.

**Ejecuta:** `python scripts/runner.py 1 3 3`

---

## Soluciones

```bash
python scripts/runner.py 1 3 1 -s
python scripts/runner.py 1 3 2 -s
python scripts/runner.py 1 3 3 -s
```
