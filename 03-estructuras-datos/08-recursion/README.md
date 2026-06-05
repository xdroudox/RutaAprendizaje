# Recursion

Una funcion recursiva es aquella que se llama a si misma para resolver un problema dividiendolo en subproblemas mas pequenos.

Componentes de la recursion:
- **Caso base**: Condicion que detiene la recursion
- **Caso recursivo**: Llamada a la funcion con parametros reducidos

Ejemplos clasicos: factorial, fibonacci, torres de hanoi, suma de digitos.

## Ejercicios

### Ejercicio 1: Factorial recursivo
Implementa el factorial de un numero de forma recursiva. n! = n * (n-1)!
**Ejecuta:** `python scripts/runner.py 3 8 1`

### Ejercicio 2: Fibonacci recursivo
Implementa la serie de Fibonacci recursivamente. fib(n) = fib(n-1) + fib(n-2)
**Ejecuta:** `python scripts/runner.py 3 8 2`

### Ejercicio 3: Suma de digitos recursiva
Implementa una funcion que sume los digitos de un numero recursivamente.
**Ejecuta:** `python scripts/runner.py 3 8 3`

## Soluciones
```bash
python scripts/runner.py 3 8 1 -s
python scripts/runner.py 3 8 2 -s
python scripts/runner.py 3 8 3 -s
```
