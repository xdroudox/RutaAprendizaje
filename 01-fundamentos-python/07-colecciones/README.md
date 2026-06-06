# Colecciones

Las **colecciones** son estructuras que permiten guardar MULTIPLES valores en una sola variable. Piensa en ellas como "contenedores" de datos. Cada tipo de coleccion tiene propiedades distintas: si permite cambios, si mantiene orden, si permite duplicados.

---

## 1. TEORIA

### 1.1 Listas (list)

Las listas son colecciones **ordenadas** y **mutables** (se pueden modificar). El tipo de coleccion mas usado.

```python
numeros = [1, 2, 3, 4, 5]
numeros.append(6)
print(numeros[0])  # 1
```

**Explicacion linea por linea:**

| Linea | Codigo | Que hace | Por que |
|-------|--------|----------|---------|
| 1 | `numeros = [1, 2, 3, 4, 5]` | Crea una lista con 5 elementos | Los `[]` definen una lista. Los elementos van separados por coma |
| 2 | `numeros.append(6)` | Agrega el 6 al FINAL de la lista | `append()` es un metodo de las listas que agrega un elemento al final |
| 3 | `print(numeros[0])` | Accede al elemento en posicion 0 | Los **indices** empiezan en 0. `[0]` = primer elemento |

**Conceptos clave:**
- **Indice**: Posicion de un elemento. `[0]` es el primero, `[1]` es el segundo, etc.
- **Indice negativo**: `[-1]` es el ULTIMO elemento, `[-2]` el penultimo.
- **Mutable**: Las listas se pueden modificar (agregar, quitar, cambiar elementos).
- **Metodos comunes**: `append()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`.

### 1.2 Tuplas (tuple)

Las tuplas son colecciones **ordenadas** e **INMUTABLES** (no se pueden modificar una vez creadas).

```python
coordenadas = (10, 20)
x, y = coordenadas
```

**Explicacion:**

| Linea | Codigo | Que hace | Por que |
|-------|--------|----------|---------|
| 1 | `coordenadas = (10, 20)` | Crea una tupla con 2 valores | Los `()` definen una tupla. Se usa cuando los datos no deben cambiar |
| 2 | `x, y = coordenadas` | **Desempaqueta** la tupla: x=10, y=20 | Asigna cada elemento de la tupla a una variable. Se llama "tuple unpacking" |

**Conceptos clave:**
- **Inmutable**: Una vez creada, NO puedes cambiar, agregar ni quitar elementos.
- **Usos comunes**: Coordenadas, configuraciones, valores que no deben cambiar.
- **Desempaquetado**: Asignar los elementos de una tupla a variables en una sola linea.

### 1.3 Diccionarios (dict)

Los diccionarios guardan pares **clave:valor**. Como una agenda: buscas por nombre (clave) y obtienes el telefono (valor).

```python
persona = {"nombre": "Ana", "edad": 25}
print(persona["nombre"])  # Ana
```

**Explicacion:**

| Linea | Codigo | Que hace | Por que |
|-------|--------|----------|---------|
| 1 | `persona = {"nombre": "Ana", "edad": 25}` | Crea un diccionario con 2 pares clave:valor | Las `{}` con `:` definen un diccionario |
| 2 | `print(persona["nombre"])` | Accede al valor asociado a la clave "nombre" | En vez de indice numerico, usas la clave (texto) |

**Conceptos clave:**
- **Clave**: Identificador unico (generalmente texto). No puede repetirse.
- **Valor**: El dato asociado a la clave. Puede ser cualquier tipo.
- **Acceso**: Se usa `dict[clave]` en vez de `dict[indice]`.
- **Mutable**: Se pueden agregar, modificar y eliminar pares.

### 1.4 Sets (conjuntos)

Los sets son colecciones **SIN duplicados** y **SIN orden**.

```python
unicos = {1, 2, 3, 3, 2}
print(unicos)  # {1, 2, 3}
```

**Explicacion:**

| Linea | Codigo | Que hace | Por que |
|-------|--------|----------|---------|
| 1 | `unicos = {1, 2, 3, 3, 2}` | Crea un set con valores (algunos repetidos) | Las `{}` sin `:` definen un set (no confundir con diccionario) |
| 2 | `print(unicos)` | Muestra `{1, 2, 3}` | Los sets ELIMINAN automaticamente los duplicados |

**Conceptos clave:**
- **Sin duplicados**: Si agregas un elemento que ya existe, se ignora.
- **Sin orden**: No puedes acceder por indice `set[0]` → no funciona.
- **Usos comunes**: Eliminar duplicados, operaciones de conjuntos (union, interseccion).

### 1.5 List Comprehension

Una forma COMPACTA de crear listas aplicando una transformacion o filtro.

```python
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]
```

**Explicacion:**

```python
# Estructura: [expresion for variable in iterable if condicion]
#            [   x       for    x   in range(10) if x % 2 == 0 ]
#             ^            ^         ^               ^
#             |            |         |               |
#             Que          Cada      De donde        Filtro (opcional)
#             guardar      elemento  vienen los
#                          se llama  elementos
#
# Sin comprehension (equivalente):
#   pares = []
#   for x in range(10):
#       if x % 2 == 0:
#           pares.append(x)
```

**Conceptos clave:**
- Es una forma mas CORTA de escribir un bucle `for` con `append()`.
- La sintaxis imita la notacion matematica de conjuntos: `{ x | x ∈ R, x > 0 }`.
- Puede tener o no el `if` final (si no tiene, transforma TODOS los elementos).

---

## 2. GLOSARIO DEL TEMA

| Termino | Definicion | Ejemplo |
|---------|------------|---------|
| **Coleccion** | Estructura que guarda multiples valores | `[1, 2, 3]`, `{"a": 1}` |
| **Elemento / Item** | Cada valor individual dentro de una coleccion | En `[1, 2, 3]`, el 2 es un elemento |
| **Indice** | Posicion numerica de un elemento (empieza en 0) | `lista[0]` → primer elemento |
| **Mutable** | Que se puede modificar despues de creado | Listas: `lista.append(4)` |
| **Inmutable** | Que NO se puede modificar despues de creado | Tuplas: no se puede agregar/quitar |
| **Clave / Key** | Identificador unico en un diccionario | `persona["nombre"]` → "nombre" es la clave |
| **Valor / Value** | Dato asociado a una clave en un diccionario | `persona["nombre"]` → "Ana" es el valor |
| **Desempaquetar** | Extraer elementos de una coleccion a variables | `a, b = (1, 2)` → a=1, b=2 |
| **Iterar** | Recorrer los elementos uno por uno | `for x in lista:` |
| **Comprehension** | Sintaxis compacta para crear colecciones | `[x*2 for x in range(5)]` |

---

## 3. COMPARATIVA ENTRE LENGUAJES

### Listas / Arrays

| Operacion | Python | Java | JavaScript |
|-----------|--------|------|------------|
| Crear | `nums = [1, 2, 3]` | `int[] nums = {1, 2, 3};` | `let nums = [1, 2, 3];` |
| Acceder | `nums[0]` | `nums[0]` | `nums[0]` |
| Agregar al final | `nums.append(4)` | Usar ArrayList | `nums.push(4)` |
| Largo | `len(nums)` | `nums.length` | `nums.length` |
| Ordenar | `nums.sort()` | `Arrays.sort(nums)` | `nums.sort()` |

### Diccionarios / Mapas / Objetos

| Operacion | Python | Java | JavaScript |
|-----------|--------|------|------------|
| Crear | `d = {"a": 1}` | `Map<String, Integer> m = ...` | `let d = {a: 1};` |
| Acceder | `d["a"]` | `m.get("a")` | `d.a` o `d["a"]` |
| Asignar | `d["b"] = 2` | `m.put("b", 2)` | `d.b = 2` |
| Eliminar | `del d["a"]` | `m.remove("a")` | `delete d.a` |

**Diferencia clave:** En Python los indices SIEMPRE empiezan en 0, igual que en Java y JS. Es universal.

---

## 4. EJEMPLO GUIADO

### Problema: Analizar calificaciones de estudiantes

> "Tienes una lista de calificaciones (0-100). Calcula el promedio, cuenta cuantos aprobaron (>=60), y muestra los nombres de los que sacaron mas de 90."

---

### Paso 1: Analizar el problema

| Pregunta | Respuesta |
|----------|-----------|
| Que datos tenemos? | Una lista de numeros (calificaciones) |
| Que necesitamos? | 3 resultados: promedio, conteo de aprobados, lista de excelentes |
| Que colecciones usar? | Lista para las notas, diccionario para asociar nombres a notas |
| Que herramientas? | `sum()`, `len()`, `for`, `if`, `append()` |

---

### Paso 2: Pseudocodigo

```
calificaciones = {"Ana": 85, "Luis": 92, "Carlos": 58, "Marta": 95, "Sofia": 70}

# Promedio
suma = SUMAR todos los valores
promedio = suma / CANTIDAD de elementos

# Aprobados
aprobados = 0
PARA CADA nota en calificaciones:
    SI nota >= 60:
        aprobados += 1

# Excelentes
excelentes = []
PARA CADA (nombre, nota) en calificaciones:
    SI nota > 90:
        AGREGAR nombre a excelentes

MOSTRAR promedio, aprobados, excelentes
```

---

### Paso 3: Codigo (explicado linea por linea)

```python
# Datos iniciales: diccionario con nombre → nota
calificaciones = {
    "Ana": 85,
    "Luis": 92,
    "Carlos": 58,
    "Marta": 95,
    "Sofia": 70
}

# --- PUNTO 1: Promedio ---
# .values() devuelve SOLO los valores del diccionario (las notas)
suma = sum(calificaciones.values())
cantidad = len(calificaciones)
promedio = suma / cantidad
print(f"Promedio del curso: {promedio:.1f}")  # :.1f = 1 decimal

# --- PUNTO 2: Contar aprobados (nota >= 60) ---
aprobados = 0
for nota in calificaciones.values():  # Solo nos interesan las notas
    if nota >= 60:
        aprobados += 1
print(f"Aprobados: {aprobados} de {cantidad}")

# --- PUNTO 3: Nombres de estudiantes excelentes (nota > 90) ---
excelentes = []
for nombre, nota in calificaciones.items():  # .items() da pares (clave, valor)
    if nota > 90:
        excelentes.append(nombre)
print(f"Excelentes (nota > 90): {', '.join(excelentes)}")
```

**Explicacion de conceptos nuevos:**

| Codigo | Explicacion |
|--------|-------------|
| `.values()` | Devuelve SOLO los valores del diccionario: `[85, 92, 58, 95, 70]` |
| `.items()` | Devuelve pares (clave, valor): `[("Ana",85), ("Luis",92), ...]` |
| `sum()` | Funcion que suma todos los elementos de una lista |
| `len()` | Funcion que da la cantidad de elementos de una coleccion |
| `for nombre, nota in ...` | Desempaqueta cada tupla (clave, valor) en dos variables |
| `', '.join(excelentes)` | Une los nombres con coma: "Luis, Marta" |

---

### Paso 4: Probar

Con los datos de ejemplo:
```
Promedio del curso: 80.0
Aprobados: 4 de 5
Excelentes (nota > 90): Luis, Marta
```

---

## 5. EJERCICIOS

### 🟢 Ejercicio 1: Operaciones con listas (Basico)

Crea una lista vacia. Luego:
1. Agrega los numeros del 1 al 5 usando `append()`
2. Inserta el 0 al principio usando `insert(0, 0)`
3. Elimina el ultimo elemento con `pop()`
4. Muestra la lista final y su longitud

**Conceptos que aplicas:** `list`, `append()`, `insert()`, `pop()`, `len()`.

**Ejecuta:** `python scripts/runner.py 1 7 1`

---

### 🟡 Ejercicio 2: Agenda telefonica (Intermedio)

Crea un diccionario que funcione como agenda telefonica. El usuario puede:
1. Agregar contactos (nombre: telefono)
2. Buscar un telefono por nombre
3. Mostrar todos los contactos

Usa un bucle para mostrar el menu de opciones hasta que el usuario elija salir.

**Conceptos que aplicas:** `dict`, `for`, `if/elif/else`, `input()`, `items()`.

**Ejecuta:** `python scripts/runner.py 1 7 2`

---

### 🔴 Ejercicio 3: Analizador de texto (Avanzado)

Pide al usuario una frase o parrafo. Luego muestra:
1. Numero total de caracteres (incluyendo espacios)
2. Numero de palabras (separadas por espacios)
3. Frecuencia de cada palabra (cuantas veces aparece cada una)
4. La palabra mas larga

**Conceptos que aplicas:** `str.split()`, `dict` para frecuencias, `for`, `if`, `len()`, `max()` con `key=`.

**Ejecuta:** `python scripts/runner.py 1 7 3`

---

## Soluciones

```bash
python scripts/runner.py 1 7 1 -s
python scripts/runner.py 1 7 2 -s
python scripts/runner.py 1 7 3 -s
```
