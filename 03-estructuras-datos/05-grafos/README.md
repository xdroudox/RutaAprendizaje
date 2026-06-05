# Grafos (Graphs)

## Que es un grafo?

Un grafo es un conjunto de **vertices (nodos)** conectados por **aristas (edges)**.

```
    1 --- 2
    |     |
    3 --- 4
```

## Tipos de grafos

### Dirigido vs No Dirigido
```python
# No dirigido: aristas bidireccionales
1 -- 2  (1 conectado a 2, 2 conectado a 1)

# Dirigido (Digrafo): aristas con direccion
1 -> 2  (1 apunta a 2, pero 2 no apunta a 1)
```

### Ponderado vs No Ponderado
```python
# Aristas con peso (distancia, costo, etc.)
1 --- 2 (peso: 5)
```

## Representaciones

### Lista de Adyacencia (mas comun)
```python
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4],
    4: [2, 3]
}
```

### Matriz de Adyacencia
```python
#  1 2 3 4
#1 0 1 1 0
#2 1 0 0 1
#3 1 0 0 1
#4 0 1 1 0
graph = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]
```

## Recorridos

### DFS (Depth-First Search)
Explora en profundidad antes de retroceder. Usa un **Stack**.

```
DFS desde 1: 1 -> 2 -> 4 -> 3
```

### BFS (Breadth-First Search)
Explora por niveles. Usa una **Queue**.

```
BFS desde 1: 1 -> 2 -> 3 -> 4
```

## Aplicaciones

| Aplicacion | Uso |
|------------|-----|
| Redes sociales | Amigos, conexiones |
| GPS / Mapas | Rutas mas cortas |
| Internet | PageRank, web crawling |
| Juegos | Pathfinding (IA) |

## Ejercicios

### 1. Implementar un Grafo
Crea la clase Graph con representacion de lista de adyacencia y metodo add_edge.

### 2. DFS traversal
Implementa Depth-First Search desde un nodo inicial.

### 3. BFS traversal
Implementa Breadth-First Search desde un nodo inicial.
