# Colecciones

## Listas

Secuencia ordenada y mutable de elementos.

```python
# Creacion
numeros = [1, 2, 3, 4, 5]
mixta = [1, "hola", True, 3.14]

# Indexacion
print(numeros[0])    # 1
print(numeros[-1])   # 5
print(numeros[1:3])  # [2, 3]

# Metodos
numeros.append(6)       # [1, 2, 3, 4, 5, 6]
numeros.insert(0, 0)    # [0, 1, 2, 3, 4, 5, 6]
numeros.remove(3)       # [0, 1, 2, 4, 5, 6]
ultimo = numeros.pop()  # 6, lista: [0, 1, 2, 4, 5]
numeros.sort()          # ordena la lista
numeros.reverse()       # invierte el orden
print(len(numeros))     # 5
```

## Tuplas

Secuencia ordenada e INMUTABLE (no se puede modificar).

```python
coordenadas = (10, 20)
print(coordenadas[0])  # 10
# coordenadas[0] = 5   # ERROR: no se puede modificar

# Desempaquetado
x, y = coordenadas
print(x, y)  # 10 20
```

## Diccionarios

Pares clave-valor. Acceso rapido por clave.

```python
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}

print(persona["nombre"])     # Ana
print(persona.get("edad"))   # 25
print(persona.keys())        # dict_keys(["nombre", "edad", "ciudad"])
print(persona.values())      # dict_values(["Ana", 25, "Madrid"])

persona["profesion"] = "Ingeniera"  # agregar
persona["edad"] = 26                # modificar
```

## Sets (conjuntos)

Coleccion NO ordenada y SIN duplicados.

```python
frutas = {"manzana", "pera", "banana"}
frutas.add("uva")
frutas.remove("pera")

print("manzana" in frutas)  # True (busqueda rapida)

# Operaciones de conjunto
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)  # union: {1, 2, 3, 4, 5, 6}
print(a & b)  # interseccion: {3, 4}
print(a - b)  # diferencia: {1, 2}
```

## Comprehensions

Sintaxis compacta para crear colecciones.

```python
# List comprehension
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]

cuadrados = [x ** 2 for x in range(5)]
print(cuadrados)  # [0, 1, 4, 9, 16]

# Dict comprehension
cuadrados_dict = {x: x ** 2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set comprehension
pares_set = {x for x in range(10) if x % 2 == 0}
# {0, 2, 4, 6, 8}
```

## Resumen de colecciones

| Tipo | Mutable | Ordenada | Duplicados | Sintaxis |
|------|---------|----------|------------|----------|
| Lista | Si | Si | Si | `[1, 2, 3]` |
| Tupla | No | Si | Si | `(1, 2, 3)` |
| Diccionario | Si | Si (3.7+) | No (claves) | `{"a": 1}` |
| Set | Si | No | No | `{1, 2, 3}` |

## Ejercicios

### 1. Lista de compras
Crea un programa que permita al usuario agregar items a una lista de compras, eliminarlos y ver la lista completa.

**Ejecuta:** `python ejercicios.py 1`

### 2. Agenda telefonica
Usa un diccionario para almacenar contactos (nombre: telefono). Permite agregar, buscar y listar contactos.

**Ejecuta:** `python ejercicios.py 2`

### 3. Numeros unicos
Pide 10 numeros al usuario y muestra cuantos son unicos (sin repetir) usando un set. Usa list comprehension para filtrar.

**Ejecuta:** `python ejercicios.py 3`
