# Pilas (Stacks) y Colas (Queues)

## Pila (Stack) - LIFO

Ultimo en entrar, primero en salir (Last In, First Out).

```
      Push(3)      Push(5)      Pop() -> 5
   [ ]          [ ]          [ ]
   [ ]          [ ]          [ ]
   [ ]          [3]          [3]
   [1]          [1]          [1]
```

```python
# Implementacion con list
stack = []
stack.append(1)    # Push
stack.append(2)    # Push
top = stack.pop()  # Pop -> 2
```

**Operaciones:** push (agregar), pop (quitar), peek (ver tope), is_empty

## Cola (Queue) - FIFO

Primero en entrar, primero en salir (First In, First Out).

```
   Enqueue(1)   Enqueue(2)   Dequeue() -> 1
   [1]          [1, 2]       [2]
```

```python
from collections import deque
queue = deque()
queue.append(1)           # Enqueue
queue.append(2)           # Enqueue
first = queue.popleft()   # Dequeue -> 1
```

**Operaciones:** enqueue (agregar), dequeue (quitar), front (ver primero), is_empty

## Deque (Double-Ended Queue)

Permite operaciones por ambos extremos.

```python
from collections import deque
d = deque()
d.append(1)        # Agregar al final
d.appendleft(2)    # Agregar al inicio
d.pop()            # Quitar del final
d.popleft()        # Quitar del inicio
```

## Aplicaciones

| Estructura | Uso tipico |
|------------|------------|
| Stack | Call stack de funciones, undo/redo, validacion de parentesis |
| Queue | Buffers, colas de impresion, BFS en grafos |
| Deque | Ventanas deslizantes, palindromos |

## Ejercicios

### 1. Implementar un Stack
Crea una clase Stack usando una lista Python con push, pop, peek, is_empty.

### 2. Implementar una Queue
Crea una clase Queue usando collections.deque con enqueue, dequeue, front, is_empty.

### 3. Parentesis balanceados
Usa un Stack para verificar si una cadena de parentesis ()[]{} esta balanceada.
