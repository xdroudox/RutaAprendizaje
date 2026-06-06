"""
SOLUCIONES - Control de Flujo
Ejecuta desde raiz: python scripts/runner.py 1 4 [ejercicio] -s

Cada solucion incluye:
  - El codigo resuelto
  - Explicacion de por que funciona
  - Alternativas si las hay
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


# ---------------------------------------------------------------------------
# 🟢 SOLUCION 1: Clasificador de notas
# ---------------------------------------------------------------------------

def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: Clasificador de notas")
    print("=" * 50)
    print()

    print("--- CODIGO ---")
    print("""
nota = int(input('Ingresa la nota (0-100): '))

if nota < 0 or nota > 100:
    print('Nota invalida')
elif nota >= 90:
    print('Calificacion: A')
elif nota >= 80:
    print('Calificacion: B')
elif nota >= 70:
    print('Calificacion: C')
elif nota >= 60:
    print('Calificacion: D')
else:
    print('Calificacion: F')
""")

    print("--- EXPLICACION ---")
    print("""
1. `nota = int(input(...))` — Leemos la nota como texto y la convertimos a entero.
   input() siempre devuelve texto; int() lo convierte a numero.

2. `if nota < 0 or nota > 100:` — Validacion: si la nota esta fuera de rango,
   mostramos error. El operador `or` significa "si se cumple cualquiera de las dos".

3. Evaluamos en ORDEN DESCENDENTE (de mayor a menor):
   - `>= 90` primero → si es True, es A
   - `>= 80` segundo → si llegamos aqui, es porque nota < 90, pero >= 80
   - Y asi hasta F

   Por que descendente? Si hicieramos >= 60 primero, una nota de 95 cumpliria
   >= 60 y daria D (incorrecto). El orden importa.

4. `else:` — Atrapa cualquier nota que no cumplio ninguna condicion anterior
   (0-59, que ya paso la validacion de rango).
""")

    print("--- ALTERNATIVA ---")
    print("""
Tambien se puede hacer con una estructura de rangos:
if 90 <= nota <= 100:
    ...
Pero el enfoque con elif es mas legible y comun.
""")


# ---------------------------------------------------------------------------
# 🟡 SOLUCION 2: Tabla de multiplicar formateada
# ---------------------------------------------------------------------------

def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: Tabla de multiplicar formateada")
    print("=" * 50)
    print()

    print("--- CODIGO ---")
    print("""
numero = int(input('Que tabla deseas ver? '))

for i in range(1, 11):
    resultado = numero * i
    if resultado % 5 == 0:
        print(f'{numero} x {i} = {resultado} *')
    else:
        print(f'{numero} x {i} = {resultado}')
""")

    print("--- EXPLICACION ---")
    print("""
1. `numero = int(input(...))` — Leemos el numero base de la tabla.

2. `for i in range(1, 11):` — range(1, 11) genera [1, 2, 3, ..., 10].
   El bucle se ejecuta 10 veces, una por cada numero de la tabla.
   En cada iteracion, `i` toma el siguiente valor (1, luego 2, etc.).

3. `resultado = numero * i` — Calculamos el producto actual.

4. `if resultado % 5 == 0:` — El operador % da el RESTO de la division.
   Si resultado es multiplo de 5, el resto de dividir por 5 es 0.
   Ej: 10 % 5 = 0 (10/5=2, resto 0), 7 % 5 = 2 (7/5=1, resto 2).

5. `f'{numero} x {i} = {resultado} *'` — f-string: incrusta variables
   directamente en el texto con {}. El ` *` al final marca multiplos de 5.
""")

    print("--- ALTERNATIVA ---")
    print("""
Usando un solo print con expresion ternaria:
for i in range(1, 11):
    resultado = numero * i
    marca = ' *' if resultado % 5 == 0 else ''
    print(f'{numero} x {i} = {resultado}{marca}')
""")


# ---------------------------------------------------------------------------
# 🔴 SOLUCION 3: Juego de adivinar con limite de intentos
# ---------------------------------------------------------------------------

def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: Juego de adivinar con limite de intentos")
    print("=" * 50)
    print()

    print("--- CODIGO ---")
    print("""
import random

while True:
    secreto = random.randint(1, 20)
    intentos = 5
    print('Adivina el numero entre 1 y 20. Tienes 5 intentos!')

    while intentos > 0:
        print(f'Intentos restantes: {intentos}')
        num = int(input('Tu numero: '))

        if num == secreto:
            print('Felicidades! Adivinaste!')
            break
        elif num > secreto:
            print('Muy alto')
        else:
            print('Muy bajo')

        intentos -= 1

    if intentos == 0:
        print(f'Game over! El numero era {secreto}')

    again = input('Jugar de nuevo? (s/n): ')
    if again != 's':
        break

print('Gracias por jugar!')
""")

    print("--- EXPLICACION ---")
    print("""
ESTRUCTURA GENERAL:

while True (bucle exterior)
    ├── Se genera el numero secreto
    ├── Se inicializan los intentos
    │
    └── while intentos > 0 (bucle interior)
        ├── Se pide un numero
        ├── Si acierta: break (sale del bucle interior)
        ├── Si falla: da pista y resta un intento
        │
    ├── Si intentos == 0: game over
    └── Pregunta si jugar de nuevo (si no, break sale del bucle exterior)

LINEA POR LINEA:

1. `import random` — Importamos el modulo random para generar numeros aleatorios.

2. `while True:` — Bucle INFINITO. Solo se sale con break. Este es el bucle
   exterior que permite jugar multiples partidas.

3. `secreto = random.randint(1, 20)` — Genera un entero aleatorio entre 1 y 20.
   random.randint(a, b) incluye tanto a como b.

4. `intentos = 5` — Contador de intentos. Se reduce en cada fallo.

5. `while intentos > 0:` — Bucle interior. Se ejecuta MIENTRAS queden intentos.
   Cuando intentos llega a 0, la condicion es False y el bucle termina.

6. `if num == secreto:` — Si adivina... `==` es comparacion (no confundir con `=` que es asignacion).

7. `break` — Sale del bucle interior. El programa continua despues del `while intentos > 0`.

8. `intentos -= 1` — Equivalente a `intentos = intentos - 1`. Se ejecuta SOLO
   cuando falla (porque si acierta, break sale antes de llegar aqui).

9. `if again != 's': break` — Si el usuario NO escribe 's', sale del bucle
   exterior con break. El `!=` significa "distinto de".

FLUJO COMPLETO (ejemplo):
  - Secreto = 15
  - Intento 1: usuario dice 10 → "Muy bajo", intentos = 4
  - Intento 2: usuario dice 18 → "Muy alto", intentos = 3
  - Intento 3: usuario dice 15 → "Felicidades!", break
  - (intentos es 3, no 0, asi que NO muestra game over)
  - "Jugar de nuevo? (s/n): " → si es 's', vuelve a empezar
""")

    print("--- VARIANTE: Con validacion de entrada ---")
    print("""
Para hacerlo mas robusto, podrias validar que el usuario ingrese un numero valido:

    while intentos > 0:
        try:
            num = int(input('Tu numero: '))
        except ValueError:
            print('Debes ingresar un numero!')
            continue

        if num < 1 or num > 20:
            print('El numero debe estar entre 1 y 20')
            continue
        ...
El bloque try/except captura errores si el usuario escribe texto en vez de numero.
""")


# ---------------------------------------------------------------------------
# DISPATCHER
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
    else:
        print("SOLUCIONES:")
        niveles = ["🟢", "🟡", "🔴"]
        for i, sol in enumerate(soluciones, 1):
            doc = sol.__doc__.strip() if sol.__doc__ else "Sin descripcion"
            print(f"  {niveles[i-1]} {i}. {doc}")
        print()
        print("Ejecuta: python scripts/runner.py 1 4 [N] -s")
