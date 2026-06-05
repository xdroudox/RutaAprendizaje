# Pilas y Colas

Las pilas (Stack) siguen el principio LIFO (Last In, First Out). Las colas (Queue) siguen FIFO (First In, First Out).

- **Stack**: push (agregar), pop (quitar ultimo), peek (ver ultimo)
- **Queue**: enqueue (agregar al final), dequeue (quitar del inicio), front (ver primero)
- **Deque**: Cola doble, permite insercion/eliminacion en ambos extremos

## Ejercicios

### Ejercicio 1: Implementar Stack
Crea una clase Stack con push, pop y peek usando una list de Python.
**Ejecuta:** `python scripts/runner.py 3 3 1`

### Ejercicio 2: Implementar Queue
Crea una clase Queue con enqueue y dequeue.
**Ejecuta:** `python scripts/runner.py 3 3 2`

### Ejercicio 3: Parentesis balanceados
Usa un Stack para verificar si los parentesis, corchetes y llaves estan balanceados.
**Ejecuta:** `python scripts/runner.py 3 3 3`

## Soluciones
```bash
python scripts/runner.py 3 3 1 -s
python scripts/runner.py 3 3 2 -s
python scripts/runner.py 3 3 3 -s
```
