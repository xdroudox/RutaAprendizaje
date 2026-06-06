# Ordenamiento

Los algoritmos de **ordenamiento** organizan los elementos de una coleccion en un orden especifico (ascendente, descendente). Son fundamentales porque muchos algoritmos requieren datos ordenados.

---

## 1. TEORIA

### 1.1 Bubble Sort — O(n^2)

Compara pares adyacentes y los intercambia si estan en orden incorrecto. El elemento mas grande "flota" hacia el final como una burbuja.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):                # n pasadas
        for j in range(n - i - 1):    # n-i-1 comparaciones
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# [5, 3, 8, 1] → [1, 3, 5, 8]
```

Visual: `[5, 3, 8, 1]` → `[3, 5, 1, 8]` → `[3, 1, 5, 8]` → `[1, 3, 5, 8]`

### 1.2 Selection Sort — O(n^2)

En cada pasada, encuentra el elemento minimo y lo coloca en su posicion correcta.

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):                    # n pasadas
        min_idx = i
        for j in range(i + 1, n):         # buscar el minimo
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # intercambiar
    return arr
```

### 1.3 Merge Sort — O(n log n)

Algoritmo de "divide y conquista": divide el array en mitades, ordena cada mitad recursivamente, luego fusiona.

```python
def merge_sort(arr):
    if len(arr) <= 1:          # Caso base
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    resultado = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            resultado.append(left[i])
            i += 1
        else:
            resultado.append(right[j])
            j += 1
    resultado.extend(left[i:])    # Resto de izquierda
    resultado.extend(right[j:])   # Resto de derecha
    return resultado
```

### 1.4 Quick Sort — O(n log n) promedio

Elige un pivote y particiona el array: menores a la izquierda, mayores a la derecha.

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivote = arr[0]
    menores = [x for x in arr[1:] if x <= pivote]
    mayores = [x for x in arr[1:] if x > pivote]
    return quick_sort(menores) + [pivote] + quick_sort(mayores)
```

### Comparativa de rendimiento

| Algoritmo | Mejor caso | Promedio | Peor caso | Memoria |
|-----------|-----------|----------|-----------|---------|
| Bubble Sort | O(n) | O(n^2) | O(n^2) | O(1) |
| Selection Sort | O(n^2) | O(n^2) | O(n^2) | O(1) |
| Insertion Sort | O(n) | O(n^2) | O(n^2) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n^2) | O(log n) |

---

## 2. GLOSARIO

| Termino | Definicion |
|---------|------------|
| **Ordenamiento estable** | Mantiene el orden relativo de elementos iguales |
| **In-place** | Ordena usando solo memoria constante adicional |
| **Divide y conquista** | Divide el problema en subproblemas mas pequenos |
| **Particion** | Dividir el array alrededor de un pivote |
| **Fusion (merge)** | Combinar dos arrays ordenados en uno solo |
| **Burbuja** | Intercambiar pares adyacentes, el mayor "flota" |
| **Seleccion** | Elegir el minimo en cada pasada |

---

## 3. COMPARATIVA ENTRE LENGUAJES

### Bubble Sort

```python
# PYTHON
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

```java
// JAVA
void bubbleSort(int[] arr) {
    int n = arr.length;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n - i - 1; j++)
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
}
```

```javascript
// JAVASCRIPT
function bubbleSort(arr) {
    const n = arr.length;
    for (let i = 0; i < n; i++)
        for (let j = 0; j < n - i - 1; j++)
            if (arr[j] > arr[j + 1])
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
}
```

---

## 4. EJEMPLO GUIADO: Ordenar calificaciones

**Problema:** Un profesor tiene las calificaciones de sus alumnos y quiere ordenarlas de menor a mayor.

### Paso 1: Datos de entrada

```python
calificaciones = [85, 92, 76, 88, 90, 61, 95, 70]
```

### Paso 2: Implementar Merge Sort

Usamos merge_sort porque es estable y predecible O(n log n).

```python
def ordenar_calificaciones(notas):
    return merge_sort(notas)
```

### Paso 3: Proceso paso a paso

```
[85, 92, 76, 88, 90, 61, 95, 70]
          ↓ divide
[85, 92, 76, 88]    [90, 61, 95, 70]
    ↓ divide              ↓ divide
[85, 92] [76, 88]    [90, 61] [95, 70]
  ↓        ↓            ↓        ↓
[85][92] [76][88]    [90][61] [95][70]
  ↓ fusion ↓
[85, 92] [76, 88]      ↓ fusion ↓
    ↓ fusion        [61, 90] [70, 95]
[76, 85, 88, 92]        ↓ fusion
                    [61, 70, 90, 95]
                          ↓ fusion
              [61, 70, 76, 85, 88, 90, 92, 95]
```

### Paso 4: Resultado

```python
print(ordenar_calificaciones([85, 92, 76, 88, 90, 61, 95, 70]))
# [61, 70, 76, 85, 88, 90, 92, 95]
```

---

## 5. EJERCICIOS

### 🟢 Ejercicio 1: Bubble Sort

Implementa `bubble_sort(arr)` que ordena una lista de numeros usando el algoritmo de burbuja.

**Ejecuta:** `python scripts/runner.py 3 6 1`

---

### 🟡 Ejercicio 2: Selection Sort

Implementa `selection_sort(arr)` que ordena una lista usando el algoritmo de seleccion.

**Ejecuta:** `python scripts/runner.py 3 6 2`

---

### 🔴 Ejercicio 3: Merge Sort

Implementa `merge_sort(arr)` y `merge(left, right)` para ordenar una lista con divide y conquista.

**Ejecuta:** `python scripts/runner.py 3 6 3`
