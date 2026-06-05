# Busqueda

Algoritmos para encontrar elementos en estructuras de datos.

- **Busqueda lineal**: O(n) - Recorre elemento por elemento
- **Busqueda binaria**: O(log n) - Requiere datos ordenados, divide y venceras
- **Hash table**: O(1) promedio - Usa funcion hash para acceso directo
- **HashSet**: Implementacion de conjunto con hash table

## Ejercicios

### Ejercicio 1: Busqueda lineal
Implementa una funcion que busque un valor en una lista recorriendola elemento por elemento. Devuelve el indice o -1.
**Ejecuta:** `python scripts/runner.py 3 7 1`

### Ejercicio 2: Busqueda binaria
Implementa busqueda binaria sobre una lista ordenada.
**Ejecuta:** `python scripts/runner.py 3 7 2`

### Ejercicio 3: HashSet simple
Implementa una clase HashSet con funcion hash, add, contains y remove.
**Ejecuta:** `python scripts/runner.py 3 7 3`

## Soluciones
```bash
python scripts/runner.py 3 7 1 -s
python scripts/runner.py 3 7 2 -s
python scripts/runner.py 3 7 3 -s
```
