# Variables y Tipos de Datos

Las **variables** guardan informacion en memoria. Cada variable tiene un **nombre** y un **tipo** de dato.

```python
nombre = "Ana"      # str (texto)
edad = 25           # int (entero)
altura = 1.65       # float (decimal)
activo = True       # bool (booleano)
```

## Tipos basicos

| Tipo | Ejemplo | Descripcion |
|------|---------|-------------|
| `int` | `edad = 25` | Numeros enteros |
| `float` | `precio = 19.99` | Numeros decimales |
| `str` | `nombre = "Ana"` | Texto (con comillas) |
| `bool` | `activo = True` | Verdadero o falso |

## Conversion entre tipos

```python
int("25")       # "25" -> 25
str(100)        # 100 -> "100"
float("3.14")   # "3.14" -> 3.14
```

## Ejercicios

### Ejercicio 1: Presentacion personal
Crea variables para tu nombre, edad y ciudad, luego muestralas.

**Ejecuta:** `python scripts/runner.py 1 2 1`

### Ejercicio 2: Edad en dias
Pide la edad en anos y calcula los dias vividos (edad * 365).

**Ejecuta:** `python scripts/runner.py 1 2 2`

### Ejercicio 3: Detector de tipos
Pide 3 valores al usuario y muestra el tipo de cada uno.

**Ejecuta:** `python scripts/runner.py 1 2 3`

## Soluciones

```bash
python scripts/runner.py 1 2 1 -s
python scripts/runner.py 1 2 2 -s
python scripts/runner.py 1 2 3 -s
```
