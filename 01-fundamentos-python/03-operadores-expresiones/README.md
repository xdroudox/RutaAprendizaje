# Operadores y Expresiones

## Operadores Aritmeticos

Se usan para realizar operaciones matematicas basicas.

```python
a = 10
b = 3

print(a + b)   # 13  (suma)
print(a - b)   # 7   (resta)
print(a * b)   # 30  (multiplicacion)
print(a / b)   # 3.333... (division real)
print(a // b)  # 3   (division entera: descarta decimales)
print(a % b)   # 1   (modulo: resto de la division)
print(a ** b)  # 1000 (potencia: 10 elevado a 3)
```

| Operador | Nombre | Ejemplo | Resultado |
|----------|--------|---------|-----------|
| `+` | Suma | `5 + 3` | `8` |
| `-` | Resta | `5 - 3` | `2` |
| `*` | Multiplicacion | `5 * 3` | `15` |
| `/` | Division real | `5 / 2` | `2.5` |
| `//` | Division entera | `5 // 2` | `2` |
| `%` | Modulo (resto) | `5 % 2` | `1` |
| `**` | Potencia | `5 ** 2` | `25` |

## Operadores de Comparacion

Comparan dos valores y devuelven `True` o `False`.

```python
x = 5
y = 10

print(x == y)   # False (igual a)
print(x != y)   # True  (distinto de)
print(x < y)    # True  (menor que)
print(x > y)    # False (mayor que)
print(x <= y)   # True  (menor o igual)
print(x >= y)   # False (mayor o igual)
```

| Operador | Significado | Ejemplo verdadero |
|----------|-------------|-------------------|
| `==` | Igual a | `5 == 5` |
| `!=` | Distinto de | `5 != 3` |
| `<` | Menor que | `3 < 5` |
| `>` | Mayor que | `5 > 3` |
| `<=` | Menor o igual | `5 <= 5` |
| `>=` | Mayor o igual | `5 >= 3` |

## Operadores Logicos

Combinan expresiones booleanas.

```python
edad = 20
tiene_licencia = True

# and: ambas deben ser True
print(edad >= 18 and tiene_licencia)  # True

# or: al menos una debe ser True
print(edad < 18 or tiene_licencia)    # True

# not: invierte el valor
print(not tiene_licencia)             # False
```

| Operador | Descripcion | Ejemplo | Resultado |
|----------|-------------|---------|-----------|
| `and` | True si ambos son True | `True and False` | `False` |
| `or` | True si al menos uno es True | `True or False` | `True` |
| `not` | Invierte el valor | `not True` | `False` |

## Precedencia de Operadores

1. Parentesis `()`
2. Potencia `**`
3. Multiplicacion, division, modulo `* / // %`
4. Suma y resta `+ -`
5. Comparacion `< > <= >= == !=`
6. Logicos: `not`, `and`, `or`

```python
resultado = (5 + 3) * 2 ** 2  # 8 * 4 = 32
```

## Ejercicios

### 1. Calculadora de propinas
Pide el total de la cuenta y el porcentaje de propina, calcula el monto de propina y el total a pagar.

**Ejecuta:** `python ejercicios.py 1`

### 2. Comparador de numeros
Pide dos numeros al usuario y muestra si son iguales, cual es mayor, y si son pares o impares.

**Ejecuta:** `python ejercicios.py 2`

### 3. Sistema de acceso VIP
Pide edad, si tiene boleto VIP y si esta en la lista de invitados. Usa operadores logicos para determinar el acceso.

**Ejecuta:** `python ejercicios.py 3`
