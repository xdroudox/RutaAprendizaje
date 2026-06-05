# Manejo de Strings

## Slicing (rebanado)

Permite extraer partes de un string.

```python
texto = "Python"

print(texto[0])    # P  (primer caracter)
print(texto[-1])   # n  (ultimo caracter)
print(texto[0:3])  # Pyt (del indice 0 al 2)
print(texto[2:])   # thon (del 2 al final)
print(texto[:4])   # Pyth (del inicio al 3)
print(texto[::2])  # Pto (cada 2 caracteres)
print(texto[::-1]) # nohtyP (invertido)
```

Sintaxis: `string[inicio:fin:paso]`

## Metodos de string

```python
texto = "  Hola Mundo  "

# Cambio de mayusculas/minusculas
print(texto.upper())       # "  HOLA MUNDO  "
print(texto.lower())       # "  hola mundo  "
print(texto.capitalize())  # "  hola mundo  "
print(texto.title())       # "  Hola Mundo  "

# Limpiar espacios
print(texto.strip())       # "Hola Mundo" (quita bordes)
print(texto.lstrip())      # "Hola Mundo  " (quita izquierda)
print(texto.rstrip())      # "  Hola Mundo" (quita derecha)

# Dividir y unir
palabras = texto.strip().split()  # ["Hola", "Mundo"]
print(" ".join(palabras))         # "Hola Mundo"

# Reemplazar
print(texto.replace("Mundo", "Python"))  # "  Hola Python  "

# Buscar
print(texto.find("Mundo"))  # 7 (indice donde empieza)
print("Mundo" in texto)     # True
print(len(texto))           # 13 (contando espacios)
```

## Metodos comunes de string

| Metodo | Descripcion | Ejemplo |
|--------|-------------|---------|
| `upper()` | Todo mayusculas | `"hola".upper()` -> `"HOLA"` |
| `lower()` | Todo minusculas | `"HOLA".lower()` -> `"hola"` |
| `strip()` | Quita espacios bordes | `" hola ".strip()` -> `"hola"` |
| `split()` | Divide en lista | `"a,b,c".split(",")` -> `["a","b","c"]` |
| `join()` | Une lista en string | `"-".join(["a","b"])` -> `"a-b"` |
| `replace()` | Reemplaza texto | `"a b".replace(" ","-")` -> `"a-b"` |
| `find()` | Busca indice | `"abc".find("b")` -> `1` |
| `len()` | Longitud | `len("hola")` -> `4` |
| `count()` | Cuenta ocurrencias | `"ana".count("a")` -> `2` |

## F-strings (formato moderno)

```python
nombre = "Ana"
edad = 25
precio = 19.99

print(f"Hola, {nombre}")                # Hola, Ana
print(f"Tienes {edad} anos")            # Tienes 25 anos
print(f"Precio: ${precio:.2f}")         # Precio: $19.99
print(f"{'Hola':<10}|")                 # "Hola      |" (alineado izq)
print(f"{'Hola':>10}|")                 # "      Hola|" (alineado der)
```

## Formato con .format()

```python
print("Hola, {} tienes {} anos".format(nombre, edad))
print("Precio: ${:.2f}".format(precio))
```

## Ejercicios

### 1. Limpiador de texto
Pide al usuario una frase con espacios extras y mayusculas irregulares. Limpiala: sin espacios al inicio/final, primera letra mayuscula, el resto minusculas.

**Ejecuta:** `python ejercicios.py 1`

### 2. Analizador de oraciones
Pide una oracion y muestra: numero de palabras, cada palabra en mayusculas, la oracion con guiones en vez de espacios.

**Ejecuta:** `python ejercicios.py 2`

### 3. Formateador de factura
Pide nombre del producto, cantidad y precio unitario. Usa f-strings para mostrar una factura formateada con alineacion y 2 decimales.

**Ejecuta:** `python ejercicios.py 3`
