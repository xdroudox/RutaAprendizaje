# Algoritmos de Ordenamiento

## Bubble Sort (O(n^2))

Compara pares adyacentes y los intercambia si estan desordenados.

```
[5, 3, 8, 1] -> [3, 5, 1, 8] -> [3, 1, 5, 8] -> [1, 3, 5, 8]
```

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```

## Selection Sort (O(n^2))

Encuentra el minimo y lo coloca al inicio.

```
[5, 3, 8, 1] -> [1, 3, 8, 5] -> [1, 3, 8, 5] -> [1, 3, 5, 8]
```

```python
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
```

## Insertion Sort (O(n^2))

Toma elementos y los inserta en la posicion correcta.

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
```

## Quick Sort (O(n log n) promedio)

Divide y venceras: elige un pivote y particiona.

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)
```

## Merge Sort (O(n log n))

Divide el array en mitades, ordena cada una, y las fusiona.

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
```

## Comparativa

| Algoritmo | Mejor caso | Peor caso | Memoria |
|-----------|-----------|-----------|---------|
| Bubble | O(n) | O(n^2) | O(1) |
| Selection | O(n^2) | O(n^2) | O(1) |
| Insertion | O(n) | O(n^2) | O(1) |
| Quick | O(n log n) | O(n^2) | O(log n) |
| Merge | O(n log n) | O(n log n) | O(n) |

## Ejercicios

### 1. Bubble Sort
Implementa bubble sort con optimizacion (detener si ya esta ordenado).

### 2. Selection Sort
Implementa selection sort ordenando de menor a mayor.

### 3. Merge Sort
Implementa merge sort con su funcion auxiliar merge.
