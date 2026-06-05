# Recursion

## Que es la recursion?

Una funcion es **recursiva** cuando se llama a si misma para resolver un problema mas pequeno del mismo tipo.

```
Receta recursiva para entender recursion:
1. Si entiendes recursion -> fin
2. Si no -> vuelve al paso 1
```

## Componentes de una funcion recursiva

1. **Caso base:** Condicion que detiene la recursion
2. **Caso recursivo:** La funcion se llama a si misma acercandose al caso base

```python
def countdown(n):
    # Caso base
    if n <= 0:
        print("Despegue!")
        return
    # Caso recursivo
    print(n)
    countdown(n - 1)
```

## Factorial (n!)

```
5! = 5 * 4 * 3 * 2 * 1 = 120
5! = 5 * 4!

Caso base: 0! = 1
Caso recursivo: n! = n * (n-1)!
```

```python
def factorial(n):
    if n <= 1:  # Caso base
        return 1
    return n * factorial(n - 1)  # Caso recursivo
```

## Fibonacci

```
fib(0) = 0
fib(1) = 1
fib(n) = fib(n-1) + fib(n-2)

Serie: 0, 1, 1, 2, 3, 5, 8, 13, 21...
```

```python
def fibonacci(n):
    if n <= 1:  # Caso base
        return n
    return fibonacci(n-1) + fibonacci(n-2)  # Caso recursivo
```

## Stack de llamadas

Cada llamada recursiva se apila en memoria:

```
factorial(5)
  -> factorial(4)
    -> factorial(3)
      -> factorial(2)
        -> factorial(1) <- caso base, retorna 1
      <- 2 * 1 = 2
    <- 3 * 2 = 6
  <- 4 * 6 = 24
<- 5 * 24 = 120
```

## Backtracking (basico)

Tecnica de prueba y error: explorar todas las opciones, retroceder si no funcionan.

```python
# Generar todas las combinaciones de [0,1] de longitud n
def generar_bits(n, prefijo=""):
    if n == 0:
        print(prefijo)
        return
    generar_bits(n-1, prefijo + "0")
    generar_bits(n-1, prefijo + "1")
```

## Ejercicios

### 1. Factorial recursivo
Implementa la funcion factorial(n) usando recursion. Calcula 0! hasta 10!.

### 2. Fibonacci recursivo
Implementa fibonacci(n) que devuelve el n-esimo numero de Fibonacci.

### 3. Torres de Hanoi
Implementa la solucion recursiva para las Torres de Hanoi con 3 discos.
