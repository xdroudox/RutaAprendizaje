# Control de Flujo

Las estructuras de control permiten dirigir el flujo de ejecucion del programa. Incluyen condicionales (if/elif/else) y bucles (for, while).

```python
# Condicional
nota = 85
if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
else:
    print("C")

# Bucle for
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Bucle while
contador = 0
while contador < 3:
    print(contador)
    contador += 1

# break y continue
for i in range(10):
    if i == 5:
        break      # sale del bucle
    if i % 2 == 0:
        continue   # salta a la siguiente iteracion
    print(i)
```

## Ejercicios

### Ejercicio 1: Clasificador de notas
Pide una nota numerica (0-100) y muestra la calificacion: A (90-100), B (80-89), C (70-79), D (60-69), F (<60). Valida que la nota este en rango.

**Ejecuta:** `python scripts/runner.py 1 4 1`

### Ejercicio 2: Tabla de multiplicar
Pide un numero y muestra su tabla de multiplicar del 1 al 10 usando un bucle for y range().

**Ejecuta:** `python scripts/runner.py 1 4 2`

### Ejercicio 3: Adivina el numero
El programa genera un numero aleatorio entre 1 y 20. El usuario debe adivinarlo. En cada intento se da una pista (mayor/menor) hasta que acierte.

**Ejecuta:** `python scripts/runner.py 1 4 3`

## Soluciones

```bash
python scripts/runner.py 1 4 1 -s
python scripts/runner.py 1 4 2 -s
python scripts/runner.py 1 4 3 -s
```
