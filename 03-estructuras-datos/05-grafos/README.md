# Grafos

Un grafo es un conjunto de nodos (vertices) conectados por aristas. Pueden ser dirigidos o no dirigidos.

- **Lista de adyacencia**: Diccionario nodo -> lista de vecinos
- **Matriz de adyacencia**: Matriz booleana de n x n
- **DFS**: Depth First Search - explora en profundidad (pila/recursion)
- **BFS**: Breadth First Search - explora por niveles (cola)

Aplicaciones: redes sociales, mapas, rutas de navegacion, dependencias.

## Ejercicios

### Ejercicio 1: Grafo con diccionario de adyacencia
Implementa un grafo no dirigido usando un diccionario.
**Ejecuta:** `python scripts/runner.py 3 5 1`

### Ejercicio 2: DFS
Implementa el recorrido Depth First Search.
**Ejecuta:** `python scripts/runner.py 3 5 2`

### Ejercicio 3: BFS
Implementa el recorrido Breadth First Search.
**Ejecuta:** `python scripts/runner.py 3 5 3`

## Soluciones
```bash
python scripts/runner.py 3 5 1 -s
python scripts/runner.py 3 5 2 -s
python scripts/runner.py 3 5 3 -s
```
