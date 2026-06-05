# Arboles (Trees)

## Arbol Binario (Binary Tree)

Cada nodo tiene **maximo 2 hijos**: izquierdo y derecho.

```
        10
       /  \
      5    15
     / \     \
    3   7     20
```

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

## Arbol Binario de Busqueda (BST)

Propiedad: izquierda < raiz < derecha para todos los nodos.

```
        10
       /  \
      5    15
     / \     \
    3   7     20
```

- Busqueda: O(log n) promedio, O(n) peor caso
- Insercion: O(log n) promedio
- In-order traversal devuelve valores ordenados

## Recorridos (Traversals)

### In-order (izquierda - raiz - derecha)
```python
def inorder(node):
    if node:
        inorder(node.left)
        print(node.value)
        inorder(node.right)
# Resultado: 3, 5, 7, 10, 15, 20
```

### Pre-order (raiz - izquierda - derecha)
```python
def preorder(node):
    if node:
        print(node.value)
        preorder(node.left)
        preorder(node.right)
# Resultado: 10, 5, 3, 7, 15, 20
```

### Post-order (izquierda - derecha - raiz)
```python
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value)
# Resultado: 3, 7, 5, 20, 15, 10
```

## Tipos de arboles

- **BST:** Valores ordenados, busqueda eficiente
- **AVL:** Balanceado automaticamente
- **Heap:** Max/Min en raiz (usado en priority queues)
- **Trie:** Arbol de prefijos (autocompletado)

## Ejercicios

### 1. Implementar un BST
Crea la clase BinarySearchTree con metodos insert y search.

### 2. Recorridos del arbol
Implementa las funciones inorder, preorder y postorder para un BST.

### 3. Minimo y maximo en BST
Encuentra el valor minimo y maximo en un arbol binario de busqueda.
