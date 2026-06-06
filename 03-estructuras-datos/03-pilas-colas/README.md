# Pilas y Colas

Las **pilas (Stack)** siguen LIFO (Last In, First Out): el ultimo en entrar es el primero en salir. Las **colas (Queue)** siguen FIFO (First In, First Out): el primero en entrar es el primero en salir.

---

## 1. TEORIA

### 1.1 Stack (Pila) — LIFO

Imagina una pila de platos: el ultimo plato que pones arriba es el primero que sacas.

| Operacion | Descripcion | Complejidad |
|-----------|-------------|-------------|
| `push(item)` | Agrega elemento en la cima | O(1) |
| `pop()` | Quita y devuelve el elemento en la cima | O(1) |
| `peek()` | Ve el elemento en la cima sin quitarlo | O(1) |
| `is_empty()` | Verifica si la pila esta vacia | O(1) |

```python
# Implementacion con list de Python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)       # Agrega al final

    def pop(self):
        if not self.is_empty():
            return self.items.pop()   # Quita del final
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]     # Ultimo elemento
        return None

    def is_empty(self):
        return len(self.items) == 0

# Uso
pila = Stack()
pila.push("Libro A")
pila.push("Libro B")
pila.push("Libro C")
print(pila.pop())    # "Libro C" - el ultimo en entrar
print(pila.peek())   # "Libro B" - nueva cima
```

**Usos reales:**
- Deshacer/rehacer en editores (Ctrl+Z)
- Navegacion del browser (atras/adelante)
- Evaluacion de expresiones matematicas
- Algoritmo de busqueda en profundidad (DFS)

### 1.2 Queue (Cola) — FIFO

Imagina una fila en el supermercado: la primera persona en llegar es la primera en ser atendida.

| Operacion | Descripcion | Complejidad |
|-----------|-------------|-------------|
| `enqueue(item)` | Agrega elemento al final | O(1) |
| `dequeue()` | Quita y devuelve el elemento del inicio | O(1) |
| `front()` | Ve el primer elemento sin quitarlo | O(1) |
| `is_empty()` | Verifica si la cola esta vacia | O(1) |

```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()          # deque = double-ended queue

    def enqueue(self, item):
        self.items.append(item)       # Agrega a la derecha

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()  # Quita de la izquierda
        return None

    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

# Uso
cola = Queue()
cola.enqueue("Persona 1")
cola.enqueue("Persona 2")
cola.enqueue("Persona 3")
print(cola.dequeue())   # "Persona 1" - la primera en llegar
print(cola.front())     # "Persona 2" - ahora es la primera
```

**Usos reales:**
- Impresion de documentos (buffer de impresion)
- Procesamiento de tareas en background
- Buzon de mensajes (message queues)
- Algoritmo de busqueda en amplitud (BFS)

### 1.3 Deque (Cola doble)

Permite insercion y eliminacion en AMBOS extremos con O(1).

```python
from collections import deque

d = deque()
d.append("derecha")       # Agrega al final
d.appendleft("izquierda") # Agrega al inicio
print(d.pop())            # Quita del final: "derecha"
print(d.popleft())        # Quita del inicio: "izquierda"
```

---

## 2. GLOSARIO

| Termino | Definicion |
|---------|------------|
| **Stack (pila)** | Estructura LIFO donde el ultimo en entrar es el primero en salir |
| **Queue (cola)** | Estructura FIFO donde el primero en entrar es el primero en salir |
| **LIFO** | Last In, First Out — ultimo en entrar, primero en salir |
| **FIFO** | First In, First Out — primero en entrar, primero en salir |
| **Cima (top)** | Elemento superior de una pila |
| **Frente (front)** | Primer elemento de una cola |
| **Final (rear)** | Ultimo elemento de una cola |
| **Push** | Operacion de insertar en una pila |
| **Pop** | Operacion de extraer de una pila |
| **Enqueue** | Operacion de insertar en una cola |
| **Dequeue** | Operacion de extraer de una cola |
| **Deque** | Double-ended queue, cola con acceso en ambos extremos |

---

## 3. COMPARATIVA ENTRE LENGUAJES

### Stack

```python
# PYTHON - con list
stack = []
stack.append(1)       # push
stack.pop()           # pop (None si vacia)
```

```java
// JAVA - Stack class (legacy, no recomendada)
Stack<Integer> stack = new Stack<>();
stack.push(1);
stack.pop();

// JAVA - Mejor usar ArrayDeque
ArrayDeque<Integer> stack = new ArrayDeque<>();
stack.push(1);
stack.pop();
```

```javascript
// JAVASCRIPT - con array
let stack = [];
stack.push(1);         // push
stack.pop();           // pop
```

### Queue

```python
# PYTHON - con collections.deque
from collections import deque
q = deque()
q.append(1)            # enqueue
q.popleft()            # dequeue
```

```java
// JAVA - LinkedList como Queue
Queue<Integer> q = new LinkedList<>();
q.offer(1);            // enqueue
q.poll();              // dequeue
q.peek();              // front
```

```javascript
// JAVASCRIPT - con array (dequeue es O(n))
let q = [];
q.push(1);             // enqueue
q.shift();             // dequeue (O(n)!)
```

---

## 4. EJEMPLO GUIADO: Verificador de parentesis balanceados

**Problema:** Dada una expresion matematica como `"{[()]}"`, determinar si los parentesis, corchetes y llaves estan correctamente balanceados.

### Paso 1: Entender el problema

Balanceado: `"([])"` ✅  |  No balanceado: `"([)]"` ❌

Regla: cada apertura debe tener su cierre correspondiente en el orden correcto.

### Paso 2: Estrategia con Stack

```
Expresion: " { [ ( ) ] } "

Caracter por caracter:
  { → apilar: [{]
  [ → apilar: [{, []
  ( → apilar: [{, [, (]
  ) → cierre, cima es '(' → coincide → pop: [{, []
  ] → cierre, cima es '[' → coincide → pop: [{]
  } → cierre, cima es '{' → coincide → pop: []

Stack vacio al final → balanceado ✅
```

### Paso 3: Implementacion

```python
def esta_balanceada(expr):
    stack = Stack()
    pares = {')': '(', ']': '[', '}': '{'}

    for char in expr:
        if char in '([{':               # Apertura → apilar
            stack.push(char)
        elif char in ')]}':             # Cierre → verificar
            if stack.is_empty():
                return False            # Cierre sin apertura
            if stack.pop() != pares[char]:
                return False            # No coincide

    return stack.is_empty()             # Debe quedar vacia
```

### Paso 4: Pruebas

```python
print(esta_balanceada("()"))       # True
print(esta_balanceada("([])"))     # True
print(esta_balanceada("{[()]}"))   # True
print(esta_balanceada("([)]"))     # False
print(esta_balanceada("("))        # False
print(esta_balanceada(")("))       # False
```

---

## 5. EJERCICIOS

### 🟢 Ejercicio 1: Implementar Stack

Crea una clase `Stack` (con list interna) con los metodos:
- `push(item)` — agrega a la cima
- `pop()` — quita y devuelve la cima (None si vacio)
- `peek()` — muestra la cima sin quitarla (None si vacio)
- `is_empty()` — True si vacio

**Ejecuta:** `python scripts/runner.py 3 3 1`

---

### 🟡 Ejercicio 2: Implementar Queue

Crea una clase `Queue` (con `deque` de `collections`) con los metodos:
- `enqueue(item)` — agrega al final
- `dequeue()` — quita y devuelve el primero (None si vacio)
- `front()` — muestra el primero sin quitarlo (None si vacio)
- `is_empty()` — True si vacio

**Ejecuta:** `python scripts/runner.py 3 3 2`

---

### 🔴 Ejercicio 3: Parentesis balanceados

Implementa la funcion `esta_balanceada(expr)` que verifica si los parentesis `()`, corchetes `[]` y llaves `{}` estan balanceados usando un Stack.

**Ejecuta:** `python scripts/runner.py 3 3 3`
