# Funciones

## Definir funciones con def

Las funciones encapsulan codigo reutilizable.

```python
def saludar(nombre):
    """Documentacion: saluda a una persona."""
    print(f"Hola, {nombre}!")

saludar("Ana")  # Hola, Ana!
```

Sintaxis:
```python
def nombre_funcion(parametro1, parametro2):
    # cuerpo
    return resultado
```

## Parametros y argumentos

```python
def sumar(a, b):
    return a + b

resultado = sumar(3, 5)  # 8
```

## Valores por defecto

```python
def saludar(nombre="Invitado"):
    print(f"Hola, {nombre}!")

saludar()        # Hola, Invitado!
saludar("Luis")  # Hola, Luis!
```

## return

Devuelve un valor desde la funcion. Sin return, la funcion devuelve `None`.

```python
def cuadrado(n):
    return n ** 2

def solo_imprimir(n):
    print(n ** 2)

resultado = cuadrado(4)    # resultado = 16
resultado2 = solo_imprimir(4)  # resultado2 = None
```

## Scope (ambito de variables)

- Variables dentro de la funcion: **locales**
- Variables fuera de la funcion: **globales**

```python
x = 10  # global

def funcion():
    x = 5  # local (no modifica la global)
    print(x)  # 5

funcion()
print(x)  # 10
```

## Lambda (funciones anonimas)

Funciones pequeñas de una sola linea.

```python
# Funcion normal
def cuadrado(x):
    return x ** 2

# Equivalente lambda
cuadrado_lambda = lambda x: x ** 2

print(cuadrado_lambda(4))  # 16

# Uso comun con sorted, filter, map
numeros = [3, 1, 4, 1, 5]
ordenados = sorted(numeros, key=lambda x: -x)
print(ordenados)  # [5, 4, 3, 1, 1]
```

Sintaxis lambda: `lambda argumentos: expresion`

## Resumen

| Concepto | Descripcion |
|----------|-------------|
| `def` | Define una funcion |
| `return` | Devuelve un valor |
| Parametros | Valores que recibe la funcion |
| Default args | Valores por defecto en parametros |
| Scope | Ambito de las variables (local/global) |
| Lambda | Funcion anonima de una expresion |

## Ejercicios

### 1. Calculadora con funciones
Crea funciones para sumar, restar, multiplicar y dividir. El usuario elige la operacion y los numeros.

**Ejecuta:** `python ejercicios.py 1`

### 2. Contador de vocales
Crea una funcion que reciba un texto y devuelva cuantas vocales tiene. Usa un parametro con default para elegir si contar mayusculas.

**Ejecuta:** `python ejercicios.py 2`

### 3. Ordenar con lambda
Pide al usuario 5 numeros y muestralos ordenados de mayor a menor usando sorted() con una funcion lambda como key.

**Ejecuta:** `python ejercicios.py 3`
