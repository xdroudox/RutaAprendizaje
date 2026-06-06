# Arrays y Listas Enlazadas

Los **arrays** almacenan elementos en posiciones **contiguas de memoria**. Las **listas enlazadas** almacenan **nodos** donde cada nodo apunta al siguiente (o anterior) mediante punteros.

---

## 1. TEORIA

### 1.1 Arrays

Un array es una secuencia de elementos del mismo tipo almacenados en posiciones de memoria consecutivas.

| Operacion | Array estatico | Array dinamico (Python list) |
|-----------|---------------|------------------------------|
| Acceso por indice | O(1) | O(1) |
| Buscar elemento | O(n) | O(n) |
| Insertar al final | No permitido (tamano fijo) | O(1) amortizado |
| Insertar al inicio | No permitido | O(n) (desplazar) |
| Eliminar al final | No permitido | O(1) |
| Eliminar al inicio | No permitido | O(n) (desplazar) |

```python
# Array estatico (simulado con lista)
arr = [10, 20, 30, 40, 50]
print(arr[0])    # O(1) - acceso directo: 10
print(arr[2])    # O(1) - acceso directo: 30

# Busqueda lineal
for elem in arr:     # O(n)
    if elem == 30:
        print("Encontrado")

# Insertar al inicio (desplaza todos)
arr.insert(0, 5)     # O(n) - [5, 10, 20, 30, 40, 50]

# Insertar al final
arr.append(60)       # O(1) - [5, 10, 20, 30, 40, 50, 60]
```

### 1.2 Listas Enlazadas

Cada **nodo** contiene un valor y uno o dos punteros a otros nodos.

#### Singly Linked List

Cada nodo apunta SOLO al siguiente nodo.

```
cabeza → [10|·] → [20|·] → [30|·] → None
```

```python
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class SinglyLinkedList:
    def __init__(self):
        self.cabeza = None

    def append(self, dato):           # O(n)
        nuevo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo

    def prepend(self, dato):          # O(1)
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
```

#### Doubly Linked List

Cada nodo apunta al siguiente Y al anterior.

```
None ← [10|·|·] ↔ [20|·|·] ↔ [30|·|·] → None
```

```python
class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None
```

### 1.3 Comparativa Arrays vs Listas Enlazadas

| Caracteristica | Array | Lista enlazada |
|----------------|-------|----------------|
| Acceso por indice | O(1) | O(n) |
| Insercion al inicio | O(n) | O(1) |
| Insercion al final | O(1) amortizado | O(n) (O(1) con cola) |
| Eliminacion al inicio | O(n) | O(1) |
| Busqueda | O(n) | O(n) |
| Memoria | Contigua, menos overhead | Dispersa, mas overhead (punteros) |
| Cache locality | Excelente (memoria contigua) | Pobre (nodos dispersos) |
| Tamano | Fijo (estatico) o dinamico | Siempre dinamico |

---

## 2. GLOSARIO

| Termino | Definicion |
|---------|------------|
| **Nodo** | Elemento basico de una lista enlazada que contiene datos y puntero(s) |
| **Cabeza (head)** | Primer nodo de la lista enlazada |
| **Cola (tail)** | Ultimo nodo de la lista enlazada |
| **Puntero (pointer)** | Referencia a otro nodo en memoria |
| **Siguiente (next)** | Puntero al nodo posterior |
| **Anterior (prev)** | Puntero al nodo anterior |
| **Singly Linked** | Lista donde cada nodo apunta solo al siguiente |
| **Doubly Linked** | Lista donde cada nodo apunta al siguiente y al anterior |
| **Overhead de memoria** | Espacio extra que ocupan los punteros ademas de los datos |
| **Cache locality** | Tendencia del procesador a acceder a posiciones de memoria cercanas |
| **Array dinamico** | Array que se redimensiona automaticamente al llenarse |
| **Desplazamiento** | Mover elementos para hacer espacio al insertar |

---

## 3. COMPARATIVA ENTRE LENGUAJES

### Arrays nativos

```python
# PYTHON - list (dinamica)
arr = [1, 2, 3]
arr.append(4)
arr.insert(0, 0)
```

```java
// JAVA - Array estatico / ArrayList
int[] estatico = new int[3];          // Tamano fijo
ArrayList<Integer> dinamico = new ArrayList<>();
dinamico.add(1);
dinamico.add(0, 0);                   // Insertar al inicio
```

```javascript
// JAVASCRIPT - Array (dinamico)
let arr = [1, 2, 3];
arr.push(4);
arr.unshift(0);                        // Insertar al inicio
```

### Listas Enlazadas

Python y JavaScript NO tienen listas enlazadas nativas. Java si:

```java
// JAVA - LinkedList nativa
import java.util.LinkedList;
LinkedList<Integer> lista = new LinkedList<>();
lista.addFirst(10);     // O(1)
lista.addLast(20);      // O(1)
lista.getFirst();       // O(1)
lista.getLast();        // O(1)
```

En Python toca implementarlas manualmente (como haremos en los ejercicios).

```python
# PYTHON - No hay lista enlazada nativa
# Se implementa con clases como vimos en teoria
```

```javascript
// JAVASCRIPT - No hay lista enlazada nativa
class Nodo {
    constructor(dato) {
        this.dato = dato;
        this.siguiente = null;
    }
}
```

---

## 4. EJEMPLO GUIADO: Sistema de playlist musical

**Problema:** Implementar una playlist donde podemos agregar canciones al final y al inicio, y mostrar la lista completa.

### Paso 1: Clase Nodo

```python
class Cancion:
    def __init__(self, titulo):
        self.titulo = titulo
        self.siguiente = None
```

Cada cancion es un nodo con un titulo y un puntero a la siguiente cancion.

### Paso 2: Clase Playlist (SinglyLinkedList)

```python
class Playlist:
    def __init__(self):
        self.cabeza = None

    def agregar_final(self, titulo):
        """Agrega cancion al final O(n)"""
        nueva = Cancion(titulo)
        if not self.cabeza:
            self.cabeza = nueva
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nueva
        print(f"  + {titulo} (agregada al final)")

    def agregar_inicio(self, titulo):
        """Agrega cancion al inicio O(1)"""
        nueva = Cancion(titulo)
        nueva.siguiente = self.cabeza
        self.cabeza = nueva
        print(f"  + {titulo} (agregada al inicio)")

    def mostrar(self):
        """Muestra la playlist completa"""
        if not self.cabeza:
            print("  Playlist vacia")
            return
        actual = self.cabeza
        pos = 1
        while actual:
            print(f"  {pos}. {actual.titulo}")
            actual = actual.siguiente
            pos += 1
```

### Paso 3: Usar la playlist

```python
mi_playlist = Playlist()
mi_playlist.agregar_final("Bohemian Rhapsody")
mi_playlist.agregar_final("Stairway to Heaven")
mi_playlist.agregar_inicio("Imagine")

print("\nMi playlist:")
mi_playlist.mostrar()
```

### Paso 4: Salida

```
  + Bohemian Rhapsody (agregada al final)
  + Stairway to Heaven (agregada al final)
  + Imagine (agregada al inicio)

Mi playlist:
  1. Imagine
  2. Bohemian Rhapsody
  3. Stairway to Heaven
```

**Analisis de complejidad:**
- `agregar_final()`: O(n) — recorre toda la lista hasta el ultimo nodo.
- `agregar_inicio()`: O(1) — solo reasigna la cabeza.
- `mostrar()`: O(n) — recorre toda la lista.

---

## 5. EJERCICIOS

### 🟢 Ejercicio 1: SinglyLinkedList basica

Implementa una clase `SinglyLinkedList` con:
- `append(dato)`: agrega al final
- `display()`: muestra los elementos separados por ` -> ` y termina en `None`

**Ejecuta:** `python scripts/runner.py 3 2 1`

---

### 🟡 Ejercicio 2: Eliminar duplicados

Implementa la funcion `eliminar_duplicados(lista)` que elimina valores repetidos de una lista enlazada usando un conjunto (`set`) para trackear valores vistos.

**Ejecuta:** `python scripts/runner.py 3 2 2`

---

### 🔴 Ejercicio 3: Revertir lista enlazada

Implementa la funcion `revertir(lista)` que invierte el orden de los nodos in-place (sin crear nuevos nodos). La cabeza debe apuntar al que era el ultimo nodo.

**Ejecuta:** `python scripts/runner.py 3 2 3`
