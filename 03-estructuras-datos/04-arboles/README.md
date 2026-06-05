# Arboles

Un arbol es una estructura jerarquica con nodos conectados por aristas. Un arbol binario de busqueda (BST) tiene la propiedad: izquierda < raiz < derecha.

- **Nodo**: Contiene un valor y referencias a hijos
- **Raiz**: Nodo superior del arbol
- **Hoja**: Nodo sin hijos
- **BST**: Binary Search Tree - insercion y busqueda O(log n) promedio

Recorridos: inorder (izquierdo, raiz, derecho), preorder (raiz, izquierdo, derecho), postorder (izquierdo, derecho, raiz).

## Ejercicios

### Ejercicio 1: NodoArbol y BST con insert
Implementa la clase NodoArbol y la clase BST con el metodo insert.
**Ejecuta:** `python scripts/runner.py 3 4 1`

### Ejercicio 2: Recorrido inorder
Implementa el recorrido inorder que imprime los valores ordenados.
**Ejecuta:** `python scripts/runner.py 3 4 2`

### Ejercicio 3: Buscar en BST
Implementa la busqueda de un valor en un arbol binario de busqueda.
**Ejecuta:** `python scripts/runner.py 3 4 3`

## Soluciones
```bash
python scripts/runner.py 3 4 1 -s
python scripts/runner.py 3 4 2 -s
python scripts/runner.py 3 4 3 -s
```
