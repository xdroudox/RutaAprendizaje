# Operadores y Expresiones

Los operadores permiten realizar operaciones con valores. Python tiene operadores aritmeticos (+, -, *, /, //, %, **), de comparacion (==, !=, <, >, <=, >=) y logicos (and, or, not).

```python
print(10 + 3)   # 13 - suma
print(10 / 3)   # 3.33 - division real
print(10 // 3)  # 3 - division entera
print(10 % 3)   # 1 - modulo
print(2 ** 3)   # 8 - potencia
print(5 == 5)   # True - igualdad
print(5 > 3)    # True - mayor que
print(True and False)  # False - and logico
print(True or False)   # True - or logico
print(not True)        # False - not logico
```

## Ejercicios

### Ejercicio 1: Calculadora de propina
Pide el total de la cuenta y el porcentaje de propina. Calcula el monto de propina y el total a pagar.

**Ejecuta:** `python scripts/runner.py 1 3 1`

### Ejercicio 2: Ano bisiesto
Pide un ano y determina si es bisiesto. Un ano es bisiesto si es divisible entre 4, excepto los divisibles entre 100 a menos que tambien sean divisibles entre 400.

**Ejecuta:** `python scripts/runner.py 1 3 2`

### Ejercicio 3: Verificar triangulo
Pide 3 numeros y verifica si pueden formar un triangulo. La suma de dos lados debe ser mayor que el tercero para todas las combinaciones.

**Ejecuta:** `python scripts/runner.py 1 3 3`

## Soluciones

```bash
python scripts/runner.py 1 3 1 -s
python scripts/runner.py 1 3 2 -s
python scripts/runner.py 1 3 3 -s
```
