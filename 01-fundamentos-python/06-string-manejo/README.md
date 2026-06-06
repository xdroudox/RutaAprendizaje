# Manejo de Strings

Los **strings** (cadenas de texto) son uno de los tipos de datos mas usados. Python ofrece potentes herramientas para manipular texto: desde extraer partes hasta cambiar formato.

---

## 1. TEORIA

### 1.1 Que es un string?

Un string es una secuencia de caracteres (letras, numeros, espacios, signos) encerrada entre comillas.

```python
texto = "Python es genial"
```

**Explicacion:**
- Las comillas pueden ser simples `'...'` o dobles `"..."`. Ambas funcionan igual.
- Los strings son **inmutables**: no puedes cambiar un caracter individual. Para "cambiar" un string, creas uno nuevo.

### 1.2 Slicing (Rebanado)

Extraer PARTES de un string usando `[inicio:fin:paso]`:

```python
texto = "Python es genial"

print(texto[0:6])     # Python  (posiciones 0 a 5)
print(texto[:6])      # Python  (desde el inicio hasta 6)
print(texto[7:])      # es genial (desde 7 hasta el final)
print(texto[-1])      # l  (ultimo caracter)
print(texto[::-1])    # laineg se nohtyP (invertido)
```

**El indice en Python:**

```
String:  P  y  t  h  o  n     e  s     g  e  n  i  a  l
Indice:  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
Negativo: ...
```

| Expresion | Resultado | Explicacion |
|-----------|-----------|-------------|
| `texto[0]` | `'P'` | Primer caracter (indice 0) |
| `texto[0:6]` | `'Python'` | Desde 0 hasta 6 (sin incluir 6) |
| `texto[:6]` | `'Python'` | Desde el inicio hasta 6 |
| `texto[7:]` | `'es genial'` | Desde 7 hasta el final |
| `texto[-1]` | `'l'` | Ultimo caracter |
| `texto[::2]` | `'Pto eil'` | Cada 2 caracteres |
| `texto[::-1]` | `'laineg se nohtyP'` | Paso negativo = invertido |

### 1.3 Metodos principales

Los strings tienen **metodos** (funciones propias del string) para manipularlos:

```python
texto = "  Python es genial  "

# Cambiar formato
print(texto.upper())          # "  PYTHON ES GENIAL  " (todo mayusculas)
print(texto.lower())          # "  python es genial  " (todo minusculas)
print(texto.strip())          # "Python es genial" (quita espacios adelante/atras)

# Busqueda y reemplazo
print(texto.replace("genial", "poderoso"))  # "  Python es poderoso  "
print("Python" in texto)      # True (esta la palabra?)

# Division y union
print(texto.split())          # ["Python", "es", "genial"] (separa por espacios)
print("-".join(["a", "b"]))   # "a-b" (une con guion)
```

| Metodo | Que hace | Ejemplo | Resultado |
|--------|----------|---------|-----------|
| `upper()` | Convierte a MAYUSCULAS | `"hola".upper()` | `"HOLA"` |
| `lower()` | Convierte a minusculas | `"HOLA".lower()` | `"hola"` |
| `strip()` | Quita espacios del inicio y final | `"  hola  ".strip()` | `"hola"` |
| `split()` | Divide en lista por separador | `"a,b,c".split(",")` | `["a","b","c"]` |
| `join()` | Une lista con separador | `"-".join(["a","b"])` | `"a-b"` |
| `replace()` | Reemplaza texto | `"a".replace("a","b")` | `"b"` |
| `in` | Verifica si existe (operador) | `"x" in "texto"` | `True`/`False` |

### 1.4 f-strings (formato)

La forma mas moderna y legible de incrustar variables en texto:

```python
nombre = "Ana"
edad = 25
print(f"Hola, me llamo {nombre} y tengo {edad} anos.")
# Hola, me llamo Ana y tengo 25 anos.

# Con formato numerico
print(f"Valor: {3.14159:.2f}")   # "Valor: 3.14" (2 decimales)
print(f"Porcentaje: {0.85:.1%}") # "Porcentaje: 85.0%"
```

La `f` antes del string activa el formato. Las `{llaves}` se reemplazan por el valor de la variable o expresion.

---

## 2. GLOSARIO DEL TEMA

| Termino | Definicion | Ejemplo |
|---------|------------|---------|
| **String / str** | Tipo de dato para texto | `"Hola"` |
| **Caracter** | Unidad minima de un string (letra, numero, signo) | `'a'`, `'1'`, `'?'` |
| **Indice** | Posicion de un caracter (empieza en 0) | `"Hola"[0]` → `'H'` |
| **Slicing** | Extraer una parte del string | `"Hola"[0:2]` → `"Ho"` |
| **Metodo** | Funcion que pertenece a un objeto | `"hola".upper()` |
| **Inmutable** | Que no se puede modificar despues de creado | Los strings no se pueden modificar, siempre se crean nuevos |
| **f-string** | String con formato que permite incrustar variables | `f"Hola, {nombre}"` |

---

## 3. COMPARATIVA ENTRE LENGUAJES

### Operaciones con texto

| Operacion | Python | Java | JavaScript |
|-----------|--------|------|------------|
| Largo | `len(s)` | `s.length()` | `s.length` |
| Mayusculas | `s.upper()` | `s.toUpperCase()` | `s.toUpperCase()` |
| Minusculas | `s.lower()` | `s.toLowerCase()` | `s.toLowerCase()` |
| Reemplazar | `s.replace(a, b)` | `s.replace(a, b)` | `s.replaceAll(a, b)` |
| Dividir | `s.split(",")` | `s.split(",")` | `s.split(",")` |
| Unir | `",".join(lista)` | `String.join(",", lista)` | `lista.join(",")` |
| Subcadena | `s[0:5]` | `s.substring(0, 5)` | `s.substring(0, 5)` |
| Contiene? | `"x" in s` | `s.contains("x")` | `s.includes("x")` |

---

## 4. EJEMPLO GUIADO

### Problema: Limpiar y analizar un nombre completo

> "Pide al usuario su nombre completo (puede tener espacios extra). Muestra: el nombre sin espacios, cuantas letras tiene, y las iniciales en mayuscula."

---

**Paso 1: Analizar**
- Entrada: texto con posibles espacios extra
- Proceso: limpiar, contar, extraer iniciales
- Salida: 3 resultados

**Paso 2: Pseudocodigo**
```
PEDIR nombre_completo
nombre_limpio = QUITAR espacios del inicio y final
cantidad = CONTAR caracteres (sin espacios)
iniciales = PRIMERA letra de cada nombre, en mayuscula
MOSTRAR todo
```

**Paso 3: Codigo**
```python
nombre = input("Ingresa tu nombre completo: ")

# Limpiar espacios
nombre = nombre.strip()

# 1. Nombre sin espacios extras
print(f"Nombre limpio: '{nombre}'")

# 2. Cantidad de letras (sin espacios)
letras = len(nombre.replace(" ", ""))
print(f"Cantidad de letras: {letras}")

# 3. Iniciales en mayuscula
partes = nombre.split()
iniciales = ""
for parte in partes:
    iniciales += parte[0].upper() + "."
print(f"Iniciales: {iniciales}")
```

**Explicacion:**
1. `strip()` — Quita espacios del inicio y final que el usuario puso sin querer
2. `replace(" ", "")` — Quita TODOS los espacios para contar solo letras
3. `split()` — Divide el nombre completo en partes (nombre, apellido1, apellido2)
4. `parte[0].upper()` — Toma la primera letra de cada parte y la pone en mayuscula
5. `iniciales += ...` — Va agregando cada inicial al string

---

## 5. EJERCICIOS

### 🟢 Ejercicio 1: Mayusculas y minusculas (Basico)

Pide al usuario su nombre y muestralo en mayusculas (`upper()`) y en minusculas (`lower()`).

**Conceptos que aplicas:** `input()`, `upper()`, `lower()`, f-strings.

**Ejecuta:** `python scripts/runner.py 1 6 1`

---

### 🟡 Ejercicio 2: Invertir palabra (Intermedio)

Pide una palabra y muestrala INVERTIDA usando slicing con paso negativo `[::-1]`. Tambien muestra si la palabra es un palindromo (se lee igual al derecho y al reves).

**Conceptos que aplicas:** Slicing, `[::-1]`, comparacion de strings.

**Ejecuta:** `python scripts/runner.py 1 6 2`

---

### 🔴 Ejercicio 3: Contar vocales (Avanzado)

Pide una frase y cuenta cuantas vocales (a, e, i, o, u) tiene. Recorre la frase con un bucle `for`. Debe funcionar tanto para mayusculas como minusculas.

**Conceptos que aplicas:** `for` con strings, `in`, `lower()`, contador.

**Ejecuta:** `python scripts/runner.py 1 6 3`

---

## Soluciones

```bash
python scripts/runner.py 1 6 1 -s
python scripts/runner.py 1 6 2 -s
python scripts/runner.py 1 6 3 -s
```
