# Arrays y Listas Enlazadas

Los arrays almacenan elementos en posiciones contiguas de memoria (acceso O(1), insercion/eliminacion O(n)). Las listas enlazadas almacenan nodos con punteros al siguiente elemento (insercion/eliminacion O(1) en la cabeza, busqueda O(n)).

- **SinglyLinkedList**: Cada nodo apunta al siguiente
- **DoublyLinkedList**: Cada nodo apunta al siguiente y al anterior
- **Array**: Tamano fijo, acceso aleatorio rapido
- **List en Python**: Dinamica, internamente es un array redimensionable

## Ejercicios

### Ejercicio 1: SinglyLinkedList con append y display
Implementa una clase SinglyLinkedList con los metodos append (agregar al final) y display (mostrar elementos).
**Ejecuta:** `python scripts/runner.py 3 2 1`

### Ejercicio 2: Eliminar duplicados
Elimina los valores duplicados de una lista enlazada.
**Ejecuta:** `python scripts/runner.py 3 2 2`

### Ejercicio 3: Revertir lista enlazada
Invierte el orden de los nodos de una lista enlazada.
**Ejecuta:** `python scripts/runner.py 3 2 3`

## Soluciones
```bash
python scripts/runner.py 3 2 1 -s
python scripts/runner.py 3 2 2 -s
python scripts/runner.py 3 2 3 -s
```
