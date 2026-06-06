# Complejidad Algoritmica (Big O)

La complejidad algoritmica mide la **eficiencia** de un algoritmo: cuantos pasos ejecuta (tiempo) y cuanta memoria usa (espacio) conforme crece la entrada.

Usamos la **notacion Big O** para describir el peor caso posible.

---

## 1. TEORIA

### 1.1 Notaciones principales

| Notacion | Nombre | Descripcion | Ejemplo |
|----------|--------|-------------|---------|
| O(1) | Constante | No importa el tamano, siempre el mismo tiempo | Acceder a `arr[0]` |
| O(log n) | Logaritmico | Se reduce a la mitad en cada paso | Busqueda binaria |
| O(n) | Lineal | Crece proporcional a la entrada | Recorrer un array con un bucle |
| O(n log n) | Log-lineal | n * log n | Merge sort, Quick sort |
| O(n^2) | Cuadratico | Dos bucles anidados | Bubble sort |
| O(2^n) | Exponencial | Se duplica en cada paso | Fibonacci recursivo sin memoizacion |
| O(n!) | Factorial | Permutaciones de n elementos | Fuerza bruta en TSP |

### 1.2 Reglas de Big O

| Regla | Explicacion | Ejemplo |
|-------|-------------|---------|
| **Ignorar constantes** | O(2n) → O(n), O(n/2) → O(n) | 2n pasos sigue siendo lineal |
| **Termino dominante** | O(n + n^2) → O(n^2) | El termino de mayor orden gana |
| **Bucles anidados** | Se multiplican | for(i) { for(j) } = O(n * m) |
| **Bucles secuenciales** | Se suman (se queda el mayor) | for(i) {}; for(j) {} = O(n + m) = O(n) |
| **Entrada distinta** | Usa variables diferentes | O(n * m) para matrices n x m |

### 1.3 Visualizacion grafica

```
Tiempo
  ^
  |                          O(n!)
  |                       O(2^n)
  |                    O(n^2)
  |                 O(n log n)
  |              O(n)
  |          O(log n)
  |     O(1)
  +---------------------------------> Tamano entrada (n)
```

Para n = 10:
- O(1) = 1 operacion
- O(log n) ≈ 3
- O(n) = 10
- O(n log n) ≈ 33
- O(n^2) = 100
- O(2^n) = 1024
- O(n!) = 3,628,800

### 1.4 Ejemplos practicos

```python
# O(1) - Constante: siempre da igual el tamano
def get_first(arr):
    return arr[0]

# O(n) - Lineal: crece con el tamano
def find_max(arr):
    max_val = arr[0]
    for num in arr:       # n veces
        if num > max_val:
            max_val = num
    return max_val

# O(n^2) - Cuadratico: bucles anidados
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):          # n veces
        for j in range(n-1):    # n-1 veces ≈ n
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# O(log n) - Logaritmico: divide el problema
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:          # se reduce a la mitad
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

---

## 2. GLOSARIO

| Termino | Definicion |
|---------|------------|
| **Big O** | Notacion matematica que describe el limite superior de un algoritmo |
| **Complejidad temporal** | Numero de operaciones que ejecuta un algoritmo |
| **Complejidad espacial** | Cantidad de memoria que usa un algoritmo |
| **Peor caso** | Escenario donde el algoritmo toma el maximo tiempo posible |
| **Caso promedio** | Tiempo esperado para una entrada tipica |
| **Mejor caso** | Escenario donde el algoritmo es mas rapido (casi no se usa) |
| **Operacion elemental** | Operacion basica que toma tiempo constante (O(1)) |
| **Tasa de crecimiento** | Como aumenta el tiempo al aumentar n |
| **Asintotico** | Comportamiento cuando n tiende a infinito |
| **Complejidad amortizada** | Promedio de tiempo por operacion en una secuencia |

---

## 3. COMPARATIVA ENTRE LENGUAJES

El concepto de Big O es UNIVERSAL: no depende del lenguaje. Lo que cambia es como implementamos los mismos algoritmos:

### Medir tiempo de ejecucion

```python
# PYTHON
import time
inicio = time.time()
resultado = mi_funcion()
fin = time.time()
print(f"Tomo {fin - inicio:.4f} segundos")
```

```java
// JAVA
long inicio = System.nanoTime();
int resultado = miFuncion();
long fin = System.nanoTime();
System.out.println("Tomo " + (fin - inicio) / 1_000_000_000.0 + " segundos");
```

```javascript
// JAVASCRIPT
console.time("miFuncion");
let resultado = miFuncion();
console.timeEnd("miFuncion");
```

### Notacion en los tres lenguajes

```python
# PYTHON - O(n)
def duplicar(arr):
    for elem in arr:
        print(elem * 2)
```

```java
// JAVA - O(n)
void duplicar(int[] arr) {
    for (int elem : arr) {
        System.out.println(elem * 2);
    }
}
```

```javascript
// JAVASCRIPT - O(n)
function duplicar(arr) {
    for (let elem of arr) {
        console.log(elem * 2);
    }
}
```

---

## 4. EJEMPLO GUIADO: Analisis de tres algoritmos

**Problema:** Dado un array numeros, queremos saber si hay algun valor duplicado. Analicemos tres enfoques:

### Paso 1: Algoritmo naive (fuerza bruta) - O(n^2)

```python
def tiene_duplicado_naive(arr):
    for i in range(len(arr)):          # n veces
        for j in range(i + 1, len(arr)):  # n-i-1 veces ≈ n
            if arr[i] == arr[j]:
                return True
    return False
```

**Analisis:** Dos bucles anidados → O(n^2). Para n=1000 son ~500,000 comparaciones.

### Paso 2: Algoritmo con ordenamiento - O(n log n)

```python
def tiene_duplicado_sort(arr):
    arr.sort()                            # O(n log n)
    for i in range(len(arr) - 1):         # O(n)
        if arr[i] == arr[i + 1]:
            return True
    return False
```

**Analisis:** sort() domina con O(n log n). Para n=1000 son ~10,000 operaciones.

### Paso 3: Algoritmo optimo con conjunto - O(n)

```python
def tiene_duplicado_set(arr):
    vistos = set()                        # O(1) insercion/promedio
    for num in arr:                       # n veces
        if num in vistos:                 # O(1) promedio
            return True
        vistos.add(num)                   # O(1) promedio
    return False
```

**Analisis:** Un solo bucle con operaciones O(1) → O(n). Para n=1000 son ~1000 operaciones.

### Tabla comparativa

| Algoritmo | Big O | n = 10 | n = 100 | n = 1000 |
|-----------|-------|--------|---------|----------|
| Naive bucles | O(n^2) | 100 | 10,000 | 1,000,000 |
| Sort + lineal | O(n log n) | 33 | 664 | 9,966 |
| Con set | O(n) | 10 | 100 | 1,000 |

**Conclusion:** El algoritmo con set es el mas eficiente. La diferencia se vuelve ABISMAL a medida que n crece.

---

## 5. EJERCICIOS

### 🟢 Ejercicio 1: Identificar Big O

Dadas las siguientes funciones, identifica si son O(1), O(n) o O(n^2):

- **A)** `arr[0]` - O(?)
- **B)** `for x in arr: print(x)` - O(?)
- **C)** `for i in arr: for j in arr: print(i, j)` - O(?)
- **D)** `arr[len(arr)//2]` - O(?)

**Ejecuta:** `python scripts/runner.py 3 1 1`

---

### 🟡 Ejercicio 2: Ordenar por eficiencia

Ordena las siguientes notaciones de MENOR a MAYOR crecimiento:

`O(n!)`, `O(1)`, `O(n^2)`, `O(n)`, `O(log n)`, `O(2^n)`, `O(n log n)`

**Ejecuta:** `python scripts/runner.py 3 1 2`

---

### 🔴 Ejercicio 3: Calcular complejidad de nested loops

Para cada fragmento, determina la complejidad Big O:

```python
# Fragmento A
for i in range(n):
    for j in range(n):
        print(i, j)
```

```python
# Fragmento B
for i in range(n):
    for j in range(i):
        print(i, j)
```

```python
# Fragmento C
for i in range(n):
    for j in range(m):
        print(i, j)
```

**Ejecuta:** `python scripts/runner.py 3 1 3`
