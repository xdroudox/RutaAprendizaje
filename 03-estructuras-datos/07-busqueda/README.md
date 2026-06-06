# Busqueda

Los algoritmos de **busqueda** encuentran elementos dentro de una estructura de datos. Desde la busqueda lineal mas simple hasta la busqueda binaria y las tablas hash.

---

## 1. TEORIA

### 1.1 Busqueda Lineal — O(n)

Recorre elemento por elemento hasta encontrar el objetivo. No requiere datos ordenados.

```python
def busqueda_lineal(arr, objetivo):
    for i in range(len(arr)):
        if arr[i] == objetivo:
            return i          # Encontrado, devuelve indice
    return -1                 # No encontrado

# Uso
nums = [5, 3, 8, 1, 9, 2]
print(busqueda_lineal(nums, 8))   # 2
print(busqueda_lineal(nums, 10))  # -1
```

**Complejidad:** O(n) — en el peor caso recorre todo el array.

### 1.2 Busqueda Binaria — O(log n)

Requiere datos **ordenados**. Divide el espacio de busqueda a la mitad en cada paso.

```python
def busqueda_binaria(arr, objetivo):
    bajo, alto = 0, len(arr) - 1

    while bajo <= alto:
        medio = (bajo + alto) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            bajo = medio + 1      # Descartar mitad izquierda
        else:
            alto = medio - 1      # Descartar mitad derecha
    return -1

# Uso (requiere array ordenado)
nums = [1, 3, 5, 7, 9, 11, 13]
print(busqueda_binaria(nums, 7))   # 3
print(busqueda_binaria(nums, 6))   # -1
```

### 1.3 Tabla Hash — O(1) promedio

Usa una funcion hash para mapear claves a posiciones en un array. Permite busqueda, insercion y eliminacion en tiempo constante promedio.

```python
class HashSet:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, valor):
        return hash(valor) % self.size

    def add(self, valor):
        idx = self._hash(valor)
        if valor not in self.buckets[idx]:
            self.buckets[idx].append(valor)

    def contains(self, valor):
        idx = self._hash(valor)
        return valor in self.buckets[idx]

    def remove(self, valor):
        idx = self._hash(valor)
        if valor in self.buckets[idx]:
            self.buckets[idx].remove(valor)

# Uso
hs = HashSet()
hs.add(10)
hs.add(20)
hs.add(10)           # No se duplica
print(hs.contains(20))  # True
hs.remove(20)
print(hs.contains(20))  # False
```

### Comparativa

| Algoritmo | Peor caso | Requisitos | Memoria |
|-----------|-----------|------------|---------|
| Busqueda lineal | O(n) | Ninguno | O(1) |
| Busqueda binaria | O(log n) | Datos ordenados | O(1) |
| Tabla hash | O(n) | Funcion hash | O(n) |

---

## 2. GLOSARIO

| Termino | Definicion |
|---------|------------|
| **Busqueda lineal** | Recorrer elemento por elemento hasta encontrar el objetivo |
| **Busqueda binaria** | Divide el espacio de busqueda a la mitad en cada paso |
| **Hash** | Funcion que mapea datos de tamano arbitrario a un entero fijo |
| **Bucket** | Contenedor donde se almacenan elementos con el mismo hash |
| **Colision** | Cuando dos elementos diferentes tienen el mismo hash |
| **Factor de carga** | Numero de elementos / numero de buckets |
| **HashSet** | Implementacion de conjunto usando tabla hash |

---

## 3. COMPARATIVA ENTRE LENGUAJES

### Busqueda binaria

```python
# PYTHON - manual
def busqueda_binaria(arr, obj):
    b, a = 0, len(arr) - 1
    while b <= a:
        m = (b + a) // 2
        if arr[m] == obj: return m
        if arr[m] < obj: b = m + 1
        else: a = m - 1
    return -1
```

```java
// JAVA - nativa
int idx = Arrays.binarySearch(arr, objetivo);
```

```javascript
// JAVASCRIPT - las busquedas nativas son lineales
let idx = arr.indexOf(objetivo);      // Lineal O(n)
let idx = arr.findIndex(x => x === objetivo);  // Lineal O(n)
```

### HashSet

```python
# PYTHON - nativo
s = set()
s.add(10)
s.remove(10)
10 in s  # contains
```

```java
// JAVA - nativo
HashSet<Integer> set = new HashSet<>();
set.add(10);
set.remove(10);
set.contains(10);
```

```javascript
// JAVASCRIPT - nativo
let set = new Set();
set.add(10);
set.delete(10);
set.has(10);
```

---

## 4. EJEMPLO GUIADO: Sistema de busqueda de productos

**Problema:** Tenemos un catalogo de productos y queremos buscar rapidamente por ID.

### Paso 1: Datos

```python
productos = [
    {"id": 101, "nombre": "Laptop", "precio": 1200},
    {"id": 205, "nombre": "Mouse", "precio": 25},
    {"id": 308, "nombre": "Teclado", "precio": 80},
    {"id": 412, "nombre": "Monitor", "precio": 350},
]
```

### Paso 2: Busqueda lineal (catalogo pequeno)

```python
def buscar_producto_lineal(productos, id_buscar):
    for p in productos:
        if p["id"] == id_buscar:
            return p
    return None

print(buscar_producto_lineal(productos, 308))
# {"id": 308, "nombre": "Teclado", "precio": 80}
```

### Paso 3: Indice hash para busqueda rapida

```python
# Construir indice (una vez)
indice = {}
for p in productos:
    indice[p["id"]] = p

# Busqueda O(1)
print(indice.get(308))
# {"id": 308, "nombre": "Teclado", "precio": 80}
```

### Paso 4: Analisis

| Metodo | Tiempo | Cuando usarlo |
|--------|--------|---------------|
| Lineal | O(n) | Catalogo pequeno (<100 items) |
| Binario (ordenar por ID) | O(log n) | Busquedas frecuentes, datos ordenados |
| Hash (indice) | O(1) | Busquedas MUY frecuentes, datos cambiantes |

---

## 5. EJERCICIOS

### 🟢 Ejercicio 1: Busqueda lineal

Implementa `busqueda_lineal(arr, objetivo)` que devuelve el indice donde se encuentra el objetivo o -1 si no existe.

**Ejecuta:** `python scripts/runner.py 3 7 1`

---

### 🟡 Ejercicio 2: Busqueda binaria

Implementa `busqueda_binaria(arr, objetivo)` sobre una lista ordenada. Divide el espacio de busqueda a la mitad en cada paso.

**Ejecuta:** `python scripts/runner.py 3 7 2`

---

### 🔴 Ejercicio 3: HashSet simple

Implementa una clase `HashSet` con `add(valor)`, `contains(valor)` y `remove(valor)` usando una tabla hash con buckets (listas) para manejar colisiones.

**Ejecuta:** `python scripts/runner.py 3 7 3`
