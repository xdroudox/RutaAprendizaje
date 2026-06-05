# Variables y Tipos de Datos

## ¿Que son las variables?

Una **variable** es como una caja donde guardas informacion. Cada caja tiene un **nombre** y contiene un **valor** de un **tipo** especifico.

```python
nombre = "Ana"       # tipo: str (texto)
edad = 25            # tipo: int (numero entero)
altura = 1.65        # tipo: float (numero decimal)
es_estudiante = True # tipo: bool (booleano: True/False)
```

## Tipos de datos basicos

| Tipo | Ejemplo | Descripcion |
|------|---------|-------------|
| `int` | `edad = 25` | Numeros enteros |
| `float` | `precio = 19.99` | Numeros decimales |
| `str` | `nombre = "Ana"` | Texto (entre comillas) |
| `bool` | `activo = True` | Verdadero/Falso |
| `NoneType` | `dato = None` | Ausencia de valor |

## La funcion type()

```python
print(type("Hola"))   # <class 'str'>
print(type(42))       # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type(True))     # <class 'bool'>
```

## Conversion de tipos (casting)

```python
# str -> int
numero = int("25")

# int -> str
texto = str(100)

# str -> float
decimal = float("3.14")

# cualquier cosa -> bool
print(bool(1))    # True
print(bool(0))    # False
print(bool(""))   # False
print(bool("a"))  # True
```

## Nombrar variables: reglas y convenciones

```python
# Correcto
mi_variable = 10
nombre_usuario = "Juan"
edad2 = 30
_contador = 0

# Incorrecto (darian error)
# 2edad = 10      # No empezar con numero
# mi-variable = 5  # No usar guiones
# class = "A"      # No usar palabras reservadas
```

## 🎯 Ejercicios

### 1. Presentacion personal
Crea variables con tu nombre, edad, ciudad y profesion. Luego imprimelas en una presentacion.

**Ejecuta:** `python ejercicios.py 1`

### 2. Calculadora de edad en dias
Pide la edad del usuario en anos y calcula cuantos dias ha vivido (aprox).

**Ejecuta:** `python ejercicios.py 2`

### 3. Type detective
Pide al usuario que ingrese 3 valores diferentes y muestra el tipo de cada uno.

**Ejecuta:** `python ejercicios.py 3`
