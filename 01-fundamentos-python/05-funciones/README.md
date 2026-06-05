# Funciones

Las funciones encapsulan codigo reutilizable. Se definen con `def`, pueden recibir parametros y devolver valores con `return`. Las funciones lambda son anonimas y de una sola expresion.

```python
# Funcion con def
def suma(a, b):
    return a + b

# Funcion con parametro por defecto
def saludar(nombre="Invitado"):
    print(f"Hola, {nombre}!")

# Lambda
cuadrado = lambda x: x ** 2
print(cuadrado(5))  # 25

# filter con lambda
numeros = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4]
```

## Ejercicios

### Ejercicio 1: Funcion suma
Crea una funcion que reciba 2 numeros como parametros y devuelva su suma. Luego pide dos numeros al usuario y muestra el resultado.

**Ejecuta:** `python scripts/runner.py 1 5 1`

### Ejercicio 2: Funcion promedio
Crea una funcion que reciba una lista de numeros y devuelva el promedio. Usa sum() y len().

**Ejecuta:** `python scripts/runner.py 1 5 2`

### Ejercicio 3: Filtrar pares con lambda
Usa filter() con una funcion lambda para obtener solo los numeros pares de una lista dada.

**Ejecuta:** `python scripts/runner.py 1 5 3`

## Soluciones

```bash
python scripts/runner.py 1 5 1 -s
python scripts/runner.py 1 5 2 -s
python scripts/runner.py 1 5 3 -s
```
