# Complejidad Algoritmica

La complejidad algoritmica mide la eficiencia de un algoritmo usando la notacion Big O, que describe el peor caso posible conforme crece la entrada.

- O(1): Constante - Acceder a un indice de array
- O(log n): Logaritmico - Busqueda binaria
- O(n): Lineal - Recorrer un array
- O(n log n): Log-lineal - Merge sort
- O(n^2): Cuadratico - Bucles anidados
- O(2^n): Exponencial - Fibonacci recursivo
- O(n!): Factorial - Permutaciones

Reglas: ignorar constantes (O(2n) = O(n)), el termino dominante gana (O(n + n^2) = O(n^2)), bucles anidados se multiplican, bucles consecutivos se suman.

## Ejercicios

### Ejercicio 1: Analizar Big O de funciones
Determina si cada funcion es O(1), O(n) o O(n^2).
**Ejecuta:** `python scripts/runner.py 3 1 1`

### Ejercicio 2: Ordenar por eficiencia
Ordena funciones de O(1) a O(n!).
**Ejecuta:** `python scripts/runner.py 3 1 2`

### Ejercicio 3: Calcular nested loops
Calcula la complejidad de algoritmos con bucles anidados.
**Ejecuta:** `python scripts/runner.py 3 1 3`

## Soluciones
```bash
python scripts/runner.py 3 1 1 -s
python scripts/runner.py 3 1 2 -s
python scripts/runner.py 3 1 3 -s
```
