# Complejidad Algoritmica (Big O)

## Que es la complejidad algoritmica?

Es una forma de medir que tan eficiente es un algoritmo conforme crece la cantidad de datos de entrada. Se representa con la notacion **Big O** que describe el **peor caso posible**.

## Notaciones principales

| Notacion | Nombre | Ejemplo | Tiempo |
|----------|--------|---------|--------|
| O(1) | Constante | Acceder a un indice de array | Instantaneo |
| O(log n) | Logaritmico | Busqueda binaria | Muy rapido |
| O(n) | Lineal | Recorrer un array | Proporcional |
| O(n log n) | Log-lineal | Merge sort, Quick sort | Moderado |
| O(n^2) | Cuadratico | Bubble sort, bucles anidados | Lento |

## Ejemplos visuales

```
O(1)     -> [x][ ][ ][ ][ ]  (un solo paso)
O(log n) -> Buscar en arbol binario
O(n)     -> [x][x][x][x][x]  (recorrer todo)
O(n^2)   -> [x][x][x]        (n * n pasos)
            [x][x][x]
            [x][x][x]
O(n log n)-> Dividir y conquistar (merge sort)
```

## Reglas para calcular Big O

1. **Ignorar constantes:** O(2n) = O(n), O(5n^2) = O(n^2)
2. **Dominante gana:** O(n + n^2) = O(n^2)
3. **Bucles anidados se multiplican:** for anidado = O(n^2)
4. **Bucles consecutivos se suman:** dos for seguidos = O(n + n) = O(2n) = O(n)

## Ejemplo practico

```python
# Caso 1: O(1) - Tiempo constante
def get_first(arr):
    return arr[0]  # Siempre 1 paso

# Caso 2: O(n) - Tiempo lineal
def print_all(arr):
    for item in arr:  # n pasos
        print(item)

# Caso 3: O(n^2) - Tiempo cuadratico
def print_pairs(arr):
    for i in arr:      # n pasos
        for j in arr:  # n pasos cada uno
            print(i, j)  # n * n = n^2
```

## Ejercicios

### 1. Analisis de complejidad I
Determina la complejidad Big O de varios fragmentos de codigo.

### 2. Analisis de complejidad II
Identifica la complejidad de funciones con bucles anidados y recursivas.

### 3. Ordenar por eficiencia
Ordena un conjunto de funciones de menor a mayor complejidad Big O.
