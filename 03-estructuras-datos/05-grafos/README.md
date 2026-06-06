# Grafos

Un **grafo** es un conjunto de **vertices** (nodos) conectados por **aristas**. Son la base de redes sociales, mapas, rutas de navegacion y sistemas de recomendacion.

---

## 1. TEORIA

### 1.1 Tipos de grafos

| Tipo | Descripcion | Ejemplo |
|------|-------------|---------|
| **No dirigido** | Las aristas son bidireccionales | Amistad en Facebook (si A es amigo de B, B es amigo de A) |
| **Dirigido** | Las aristas tienen direccion | Seguir en Twitter (A sigue a B no implica B sigue a A) |
| **Ponderado** | Aristas con peso/distancia | Mapas de carreteras (km entre ciudades) |
| **Ciclico** | Tiene caminos cerrados | Grafo con triangulos de amistad |
| **Aciclico** | No tiene ciclos | Arbol de dependencias |

### 1.2 Representaciones

#### Lista de adyacencia (usaremos esta)

Cada nodo tiene una LISTA de sus vecinos.

```python
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
```

```
    A
   / \
  B---C
   \ /
    D
```

**Ventaja:** eficiente en memoria para grafos dispersos (pocas aristas).

#### Matriz de adyacencia

Matriz n x n donde `matriz[i][j] = 1` si hay arista.

```
    A  B  C  D
A  [0, 1, 1, 0]
B  [1, 0, 0, 1]
C  [1, 0, 0, 1]
D  [0, 1, 1, 0]
```

**Ventaja:** saber si dos nodos son vecinos es O(1).
**Desventaja:** ocupa O(n^2) memoria, aunque el grafo tenga pocas aristas.

### 1.3 Recorridos

#### DFS (Depth First Search) — Busqueda en profundidad

Usa una **pila** (o recursion). Explora tan lejos como puede antes de retroceder.

```python
def dfs(grafo, inicio, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(inicio)
    print(inicio, end=' ')
    for vecino in grafo[inicio]:
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)
```

Recorrido desde A: `A B D C`

```
A → B → D → C
```

**Usos:** deteccion de ciclos, caminos en laberintos, orden topologico.

#### BFS (Breadth First Search) — Busqueda en amplitud

Usa una **cola**. Explora por niveles (primero los vecinos directos).

```python
from collections import deque

def bfs(grafo, inicio):
    visitados = set()
    cola = deque([inicio])
    visitados.add(inicio)
    while cola:
        nodo = cola.popleft()
        print(nodo, end=' ')
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
```

Recorrido desde A: `A B C D`

```
A → (B, C) → D
```

**Usos:** camino mas corto en grafos no ponderados, redes sociales (amigos en comun).

---

## 2. GLOSARIO

| Termino | Definicion |
|---------|------------|
| **Vertice (nodo)** | Unidad basica del grafo |
| **Arista** | Conexion entre dos vertices |
| **Grafo dirigido** | Aristas con direccion (A→B no implica B→A) |
| **Grafo no dirigido** | Aristas bidireccionales |
| **Lista de adyacencia** | Diccionario nodo → lista de vecinos |
| **Matriz de adyacencia** | Matriz n x n de booleanos |
| **DFS** | Depth First Search, exploracion en profundidad |
| **BFS** | Breadth First Search, exploracion por niveles |
| **Visitados** | Conjunto de nodos ya procesados (evita ciclos) |
| **Ciclo** | Camino cerrado (vuelve al mismo nodo) |
| **Grafo conexo** | Todos los nodos son alcanzables desde cualquier nodo |
| **Grado** | Numero de aristas que conectan un nodo |

---

## 3. COMPARATIVA ENTRE LENGUAJES

### Lista de adyacencia

```python
# PYTHON - diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A']
}
```

```java
// JAVA - HashMap
Map<String, List<String>> grafo = new HashMap<>();
grafo.put("A", Arrays.asList("B", "C"));
grafo.put("B", Arrays.asList("A"));
grafo.put("C", Arrays.asList("A"));
```

```javascript
// JAVASCRIPT - objeto/Map
const grafo = {
    A: ['B', 'C'],
    B: ['A'],
    C: ['A']
};
```

### DFS recursivo

```python
# PYTHON
def dfs(grafo, nodo, vistos):
    vistos.add(nodo)
    for vecino in grafo[nodo]:
        if vecino not in vistos:
            dfs(grafo, vecino, vistos)
```

```java
// JAVA
void dfs(Map<String, List<String>> grafo,
         String nodo, Set<String> vistos) {
    vistos.add(nodo);
    for (String vecino : grafo.get(nodo)) {
        if (!vistos.contains(vecino)) {
            dfs(grafo, vecino, vistos);
        }
    }
}
```

```javascript
// JAVASCRIPT
function dfs(grafo, nodo, vistos = new Set()) {
    vistos.add(nodo);
    for (let vecino of grafo[nodo]) {
        if (!vistos.has(vecino)) {
            dfs(grafo, vecino, vistos);
        }
    }
}
```

---

## 4. EJEMPLO GUIADO: Red social de amistades

**Problema:** Modelar una red social donde las personas son nodos y las amistades son aristas. Queremos encontrar el camino mas corto entre dos personas.

### Paso 1: Crear el grafo

```python
red = Grafo()
red.agregar_arista("Alice", "Bob")
red.agregar_arista("Alice", "Charlie")
red.agregar_arista("Bob", "Diana")
red.agregar_arista("Charlie", "Diana")
red.agregar_arista("Diana", "Eve")
```

```
    Alice
    /   \
  Bob   Charlie
    \   /
    Diana
      |
     Eve
```

### Paso 2: Camino mas corto con BFS

```python
from collections import deque

def camino_mas_corto(grafo, inicio, destino):
    visitados = {inicio}
    cola = deque([(inicio, [inicio])])   # (nodo, camino hasta el)

    while cola:
        nodo, camino = cola.popleft()
        if nodo == destino:
            return camino
        for vecino in grafo.adyacencia[nodo]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append((vecino, camino + [vecino]))
    return None
```

### Paso 3: Probar

```python
camino = camino_mas_corto(red, "Alice", "Eve")
print(f"Camino: {' → '.join(camino)}")
# Camino: Alice → Bob → Diana → Eve
# (o Alice → Charlie → Diana → Eve, ambos de longitud 3)
```

### Paso 4: Analisis

- BFS encuentra el camino mas corto en grafos NO ponderados.
- Complejidad: O(V + E) donde V = vertices, E = aristas.
- Usa una cola para explorar por niveles: primero amigos, luego amigos de amigos, etc.

---

## 5. EJERCICIOS

### 🟢 Ejercicio 1: Grafo con diccionario de adyacencia

Implementa una clase `Grafo` con:
- `agregar_nodo(nodo)`: agrega nodo si no existe
- `agregar_arista(a, b)`: conecta a y b (grafo NO dirigido)
- `mostrar()`: imprime cada nodo con sus vecinos

**Ejecuta:** `python scripts/runner.py 3 5 1`

---

### 🟡 Ejercicio 2: DFS (Depth First Search)

Implementa `dfs(grafo, inicio)` que recorre el grafo en profundidad usando recursion e imprime los nodos visitados.

**Ejecuta:** `python scripts/runner.py 3 5 2`

---

### 🔴 Ejercicio 3: BFS (Breadth First Search)

Implementa `bfs(grafo, inicio)` que recorre el grafo por niveles usando una cola (`deque` de `collections`) e imprime los nodos visitados.

**Ejecuta:** `python scripts/runner.py 3 5 3`
