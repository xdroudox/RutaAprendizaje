# Arboles

Un **arbol** es una estructura jerarquica de nodos conectados por aristas. El **Binary Search Tree (BST)** es un caso especial donde cada nodo tiene: izquierda < raiz < derecha.

---

## 1. TEORIA

### 1.1 Estructura basica

```
        ┌───┐
        │ 5 │  ← raiz
        └───┘
       /     \
    ┌───┐   ┌───┐
    │ 3 │   │ 7 │  ← nodos internos
    └───┘   └───┘
   /   \   /     \
 ┌─┐   ┌─┐ ┌─┐   ┌─┐
 │2│   │4│ │6│   │8│  ← hojas
 └─┘   └─┘ └─┘   └─┘
```

| Termino | Definicion |
|---------|------------|
| **Raiz** | Nodo superior del arbol (no tiene padre) |
| **Nodo** | Elemento del arbol con valor y referencias a hijos |
| **Hoja** | Nodo sin hijos |
| **Padre** | Nodo que tiene referencias a otros nodos (hijos) |
| **Hijo** | Nodo referenciado por otro nodo (padre) |
| **Subarbol** | Conjunto de nodos que cuelgan de un nodo dado |
| **Altura** | Distancia maxima desde la raiz hasta una hoja |
| **Profundidad** | Distancia desde la raiz hasta un nodo |

### 1.2 Binary Search Tree (BST)

Propiedad fundamental del BST:
- **Izquierdo**: todos los valores son MENOR que la raiz
- **Derecho**: todos los valores son MAYOR (o igual) que la raiz

```python
class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class BST:
    def __init__(self):
        self.raiz = None

    def insert(self, valor):
        """Inserta un valor manteniendo la propiedad del BST"""
        if not self.raiz:
            self.raiz = NodoArbol(valor)
            return
        self._insert(self.raiz, valor)

    def _insert(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo:
                self._insert(nodo.izquierdo, valor)
            else:
                nodo.izquierdo = NodoArbol(valor)
        else:
            if nodo.derecho:
                self._insert(nodo.derecho, valor)
            else:
                nodo.derecho = NodoArbol(valor)
```

### 1.3 Recorridos

Los recorridos determinan el ORDEN en que visitamos los nodos.

| Recorrido | Orden | Resultado en BST |
|-----------|-------|------------------|
| **Inorder** | Izquierdo → Raiz → Derecho | Valores ORDENADOS |
| **Preorder** | Raiz → Izquierdo → Derecho | Copiar arbol |
| **Postorder** | Izquierdo → Derecho → Raiz | Eliminar arbol |

```python
def inorder(nodo):
    """Izquierdo, Raiz, Derecho — valores ordenados"""
    if nodo:
        inorder(nodo.izquierdo)
        print(nodo.valor, end=' ')
        inorder(nodo.derecho)

def preorder(nodo):
    """Raiz, Izquierdo, Derecho — raiz primero"""
    if nodo:
        print(nodo.valor, end=' ')
        preorder(nodo.izquierdo)
        preorder(nodo.derecho)

def postorder(nodo):
    """Izquierdo, Derecho, Raiz — hojas primero"""
    if nodo:
        postorder(nodo.izquierdo)
        postorder(nodo.derecho)
        print(nodo.valor, end=' ')
```

Para el arbol `[5, 3, 7, 2, 4, 6, 8]`:

```
Inorder:    2 3 4 5 6 7 8     (ordenado)
Preorder:   5 3 2 4 7 6 8     (raiz primero)
Postorder:  2 4 3 6 8 7 5     (hojas primero)
```

### 1.4 Busqueda en BST

```python
def buscar(nodo, valor):
    """Busca un valor en el BST. Retorna True/False."""
    if not nodo:
        return False
    if nodo.valor == valor:
        return True
    if valor < nodo.valor:
        return buscar(nodo.izquierdo, valor)
    else:
        return buscar(nodo.derecho, valor)

# O(log n) promedio — O(n) peor caso (arbol inclinado)
```

---

## 2. GLOSARIO

| Termino | Definicion |
|---------|------------|
| **BST** | Binary Search Tree, arbol binario de busqueda con orden izquierda < raiz < derecha |
| **Arbol binario** | Cada nodo tiene maximo 2 hijos (izquierdo y derecho) |
| **Raiz** | Nodo superior sin padre |
| **Hoja** | Nodo sin hijos |
| **Altura** | Longitud del camino mas largo de raiz a hoja |
| **Balanceado** | Arbol donde la altura de ambos subarboles difiere en maximo 1 |
| **Recorrido** | Forma de visitar todos los nodos en un orden especifico |
| **Inorder** | Recorrido que visita: izquierdo, raiz, derecho |
| **Preorder** | Recorrido que visita: raiz, izquierdo, derecho |
| **Postorder** | Recorrido que visita: izquierdo, derecho, raiz |
| **Subarbol** | Arbol formado por un nodo y todos sus descendientes |

---

## 3. COMPARATIVA ENTRE LENGUAJES

### Nodo de arbol

```python
# PYTHON
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
```

```java
// JAVA
class Nodo {
    int valor;
    Nodo izquierdo;
    Nodo derecho;

    Nodo(int valor) {
        this.valor = valor;
    }
}
```

```javascript
// JAVASCRIPT
class Nodo {
    constructor(valor) {
        this.valor = valor;
        this.izquierdo = null;
        this.derecho = null;
    }
}
```

### Recorrido inorder

```python
# PYTHON
def inorder(nodo):
    if nodo:
        inorder(nodo.izquierdo)
        print(nodo.valor)
        inorder(nodo.derecho)
```

```java
// JAVA
void inorder(Nodo nodo) {
    if (nodo != null) {
        inorder(nodo.izquierdo);
        System.out.println(nodo.valor);
        inorder(nodo.derecho);
    }
}
```

```javascript
// JAVASCRIPT
function inorder(nodo) {
    if (nodo) {
        inorder(nodo.izquierdo);
        console.log(nodo.valor);
        inorder(nodo.derecho);
    }
}
```

---

## 4. EJEMPLO GUIADO: Diccionario con BST

**Problema:** Queremos almacenar palabras en orden alfabetico para poder buscar rapidamente.

### Paso 1: Insertar palabras

```python
diccionario = BST()
palabras = ["casa", "arbol", "perro", "gato", "zorro", "bicicleta"]
for p in palabras:
    diccionario.insert(p)
```

El arbol resultante (orden alfabetico):
```
         "casa"
        /      \
   "arbol"    "perro"
   /         /      \
"bicicleta" "gato" "zorro"
```

### Paso 2: Mostrar en orden alfabetico

```python
def inorder_con_formato(nodo, nivel=0):
    if nodo:
        inorder_con_formato(nodo.izquierdo, nivel + 1)
        print("  " * nivel + f"- {nodo.valor}")
        inorder_con_formato(nodo.derecho, nivel + 1)

inorder_con_formato(diccionario.raiz)
```

Salida:
```
- arbol
    - bicicleta
- casa
    - gato
    - perro
        - zorro
```

### Paso 3: Buscar palabras

```python
print(buscar(diccionario.raiz, "gato"))   # True
print(buscar(diccionario.raiz, "avion"))  # False
print(buscar(diccionario.raiz, "casa"))   # True
```

### Paso 4: Analisis de complejidad

| Operacion | BST promedio | BST peor caso | Array ordenado |
|-----------|-------------|---------------|----------------|
| Insertar | O(log n) | O(n) | O(n) |
| Buscar | O(log n) | O(n) | O(log n) |
| Listar ordenado | O(n) | O(n) | O(n) |

El BST gana en insercion, el array ordenado en busqueda (binary search).

---

## 5. EJERCICIOS

### 🟢 Ejercicio 1: NodoArbol y BST con insert

Implementa la clase `NodoArbol` y la clase `BST` con un metodo `insert(valor)` que mantenga la propiedad del BST (menores a la izquierda, mayores a la derecha).

**Ejecuta:** `python scripts/runner.py 3 4 1`

---

### 🟡 Ejercicio 2: Recorrido inorder

Implementa la funcion recursiva `inorder(nodo)` que imprime los valores del BST en orden ascendente.

**Ejecuta:** `python scripts/runner.py 3 4 2`

---

### 🔴 Ejercicio 3: Buscar en BST

Implementa la funcion recursiva `buscar(nodo, valor)` que retorna `True` si el valor existe en el BST, `False` en caso contrario. Debe aprovechar la propiedad del BST para decidir que rama explorar.

**Ejecuta:** `python scripts/runner.py 3 4 3`
