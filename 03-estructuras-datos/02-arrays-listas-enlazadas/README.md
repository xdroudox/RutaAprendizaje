# Arrays y Listas Enlazadas

## Arrays

Los arrays almacenan elementos en posiciones **contiguas** de memoria. Cada elemento se accede por su indice.

**Ventajas:**
- Acceso O(1) por indice
- Cache friendly (datos contiguos)
- Sin overhead de punteros

**Desventajas:**
- Tamano fijo (en arrays estaticos)
- Insercion/eliminacion O(n) (hay que desplazar)

```python
arr = [10, 20, 30, 40, 50]
print(arr[2])  # O(1) -> 30
arr.insert(1, 15)  # O(n) - desplaza elementos
```

## Listas Enlazadas (Linked Lists)

Cada elemento (nodo) contiene un valor y un puntero al siguiente nodo.

### Simplemente Enlazada (Singly Linked List)
```
[10|*] -> [20|*] -> [30|*] -> None
```

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

### Doblemente Enlazada (Doubly Linked List)
```
None <- [10|*|*] <-> [20|*|*] <-> [30|*|*] -> None
```

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
```

**Ventajas:**
- Insercion/eliminacion O(1) si tienes el nodo
- Tamano dinamico
- No requiere memoria contigua

**Desventajas:**
- Acceso O(n) (hay que recorrer)
- Overhead de memoria por punteros
- No cache friendly

## Comparativa

| Operacion | Array | Linked List |
|-----------|-------|-------------|
| Acceso por indice | O(1) | O(n) |
| Insercion al inicio | O(n) | O(1) |
| Insercion al final | O(1)* | O(1)* |
| Eliminacion | O(n) | O(1) |
| Busqueda | O(n) | O(n) |

*Amortizado con *append* / con cola separada

## Ejercicios

### 1. Lista Simplemente Enlazada
Implementa una SinglyLinkedList con insert, delete, search y print.

### 2. Lista Doblemente Enlazada
Implementa una DoublyLinkedList con insercion al inicio y al final.

### 3. Invertir lista enlazada
Dada una lista enlazada, implementa una funcion para invertirla.
