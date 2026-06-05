# Manejo de Strings

Los strings son cadenas de texto. Python ofrece potentes metodos para manipularlos: slicing, conversion de mayusculas/minusculas, separacion, union, reemplazo y formato con f-strings.

```python
texto = "Python es genial"

# Slicing
print(texto[0:6])    # Python
print(texto[::-1])   # laineg se nohtyP (invertido)

# Metodos
print(texto.upper())        # PYTHON ES GENIAL
print(texto.lower())        # python es genial
print("  hola  ".strip())   # hola
print(texto.split())        # ['Python', 'es', 'genial']
print("-".join(texto.split()))  # Python-es-genial
print(texto.replace("genial", "poderoso"))  # Python es poderoso

# f-strings
nombre = "Ana"
edad = 25
print(f"Hola, me llamo {nombre} y tengo {edad} anos.")
```

## Ejercicios

### Ejercicio 1: Mayusculas y minusculas
Pide al usuario su nombre y muestralo en mayusculas (upper()) y en minusculas (lower()).

**Ejecuta:** `python scripts/runner.py 1 6 1`

### Ejercicio 2: Invertir palabra
Pide una palabra y muestrala invertida usando slicing con paso negativo [::-1].

**Ejecuta:** `python scripts/runner.py 1 6 2`

### Ejercicio 3: Contar vocales
Pide una frase y cuenta cuantas vocales (a, e, i, o, u) tiene. Recorre la frase con un bucle for.

**Ejecuta:** `python scripts/runner.py 1 6 3`

## Soluciones

```bash
python scripts/runner.py 1 6 1 -s
python scripts/runner.py 1 6 2 -s
python scripts/runner.py 1 6 3 -s
```
