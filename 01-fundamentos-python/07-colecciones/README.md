# Colecciones

Python ofrece varios tipos de colecciones: listas, tuplas, diccionarios y sets. Cada una tiene propiedades distintas de mutabilidad, orden y duplicados.

```python
# Lista (mutable, ordenada)
numeros = [1, 2, 3, 4, 5]
numeros.append(6)
print(numeros[0])  # 1

# Tupla (inmutable, ordenada)
coordenadas = (10, 20)
x, y = coordenadas

# Diccionario (clave:valor)
persona = {"nombre": "Ana", "edad": 25}
print(persona["nombre"])  # Ana

# Set (sin duplicados, no ordenado)
unicos = {1, 2, 3, 3, 2}
print(unicos)  # {1, 2, 3}

# List comprehension
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]
```

## Ejercicios

### Ejercicio 1: Lista de 5 numeros
Crea una lista con 5 numeros enteros. Muestra la lista, la suma de sus elementos (usando sum()) y el promedio.

**Ejecuta:** `python scripts/runner.py 1 7 1`

### Ejercicio 2: Diccionario persona
Crea un diccionario con los datos de una persona (nombre, edad, ciudad, profesion). Accede a cada clave y muestra su valor.

**Ejecuta:** `python scripts/runner.py 1 7 2`

### Ejercicio 3: List comprehension pares
Usa una list comprehension para generar una lista con los numeros pares del 1 al 20.

**Ejecuta:** `python scripts/runner.py 1 7 3`

## Soluciones

```bash
python scripts/runner.py 1 7 1 -s
python scripts/runner.py 1 7 2 -s
python scripts/runner.py 1 7 3 -s
```
