# Control de Flujo

## Condicionales if / elif / else

Permiten ejecutar codigo solo si se cumple una condicion.

```python
edad = 18

if edad < 12:
    print("Eres un nino")
elif edad < 18:
    print("Eres adolescente")
elif edad < 65:
    print("Eres adulto")
else:
    print("Eres adulto mayor")
```

Sintaxis:
- `if condicion:` -- primera condicion
- `elif condicion:` -- condiciones adicionales (opcional)
- `else:` -- si nada se cumple (opcional)

## Bucle for

Itera sobre una secuencia (lista, string, range, etc.).

```python
# Con range()
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(inicio, fin, paso)
for i in range(1, 10, 2):
    print(i)  # 1, 3, 5, 7, 9

# Sobre una lista
colores = ["rojo", "verde", "azul"]
for color in colores:
    print(color)

# Sobre un string
for letra in "Hola":
    print(letra)
```

## Bucle while

Repite mientras una condicion sea True.

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1  # IMPORTANTE: actualizar la variable
```

## break y continue

- `break`: sale del bucle inmediatamente
- `continue`: salta a la siguiente iteracion

```python
# break: encontrar el primer numero par
for i in range(1, 10):
    if i % 2 == 0:
        print(f"Primer par: {i}")
        break

# continue: saltar impares
for i in range(10):
    if i % 2 != 0:
        continue
    print(i)  # solo pares: 0, 2, 4, 6, 8
```

## Resumen

| Estructura | Uso |
|------------|-----|
| `if/elif/else` | Tomar decisiones |
| `for` | Iterar secuencias conocidas |
| `while` | Repetir hasta que algo cambie |
| `break` | Salir del bucle |
| `continue` | Saltar a la siguiente iteracion |
| `range()` | Generar secuencias numericas |

## Ejercicios

### 1. Clasificador de notas
Pide una nota numerica (0-100) y muestra la calificacion: A (90+), B (80-89), C (70-79), D (60-69), F (<60).

**Ejecuta:** `python ejercicios.py 1`

### 2. Tabla de multiplicar
Pide un numero y muestra su tabla de multiplicar del 1 al 10 usando for y range().

**Ejecuta:** `python ejercicios.py 2`

### 3. Adivina el numero
El programa piensa un numero aleatorio entre 1 y 20. El usuario tiene 5 intentos para adivinarlo. Usa while, break y continue.

**Ejecuta:** `python ejercicios.py 3`
