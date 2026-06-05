# Algoritmos de Busqueda

## Busqueda Lineal (Linear Search)

Recorre elemento por elemento hasta encontrar el objetivo.

```
Array: [4, 2, 7, 1, 9, 3]
Buscar: 7
Pasos: 4? no -> 2? no -> 7? si! (3 pasos)
```

```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1
```

**Complejidad:** O(n) - Recorre todo el array en el peor caso.

## Busqueda Binaria (Binary Search)

Requiere que el array este **ordenado**. Divide el espacio de busqueda a la mitad en cada paso.

```
Array: [1, 3, 5, 7, 9, 11, 13]
Buscar: 9
- mid = 7 (indice 3), 9 > 7 -> busca derecha
- mid = 11 (indice 5), 9 < 11 -> busca izquierda
- mid = 9 (indice 4), encontrado! (3 pasos vs 5 lineal)
```

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

**Complejidad:** O(log n) - Exponencialmente mas rapido que lineal.

## Hash Table Search

Usa una funcion hash para acceder directamente al elemento.

```python
hash_table = {"juan": 25, "maria": 30, "pedro": 35}
edad = hash_table["maria"]  # O(1) promedio
```

**Complejidad:** O(1) promedio, O(n) peor caso (colisiones).

## Comparativa

| Algoritmo | Estructura | Tiempo | Requisito |
|-----------|-----------|--------|-----------|
| Lineal | Array/Lista | O(n) | Ninguno |
| Binaria | Array | O(log n) | Datos ordenados |
| Hash | Hash Table | O(1) promedio | Funcion hash |

## Ejercicios

### 1. Busqueda Lineal
Implementa linear_search que devuelve el indice de un elemento.

### 2. Busqueda Binaria
Implementa binary_search de forma iterativa y recursiva.

### 3. Hash Table
Implementa una clase HashTable simple con put, get, delete usando listas para colisiones.
