"""
SOLUCIONES - Funciones
Ejecuta desde raiz: python scripts/runner.py 1 5 [ejercicio] -s
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: Funcion suma")
    print("=" * 50)
    print()

    print("--- CODIGO ---")
    print("""
def sumar(a, b):
    return a + b

num1 = float(input('Ingresa el primer numero: '))
num2 = float(input('Ingresa el segundo numero: '))

resultado = sumar(num1, num2)
print(f'La suma es: {resultado}')
""")

    print("--- EXPLICACION ---")
    print("""
1. `def sumar(a, b):` — Definimos la funcion con DOS parametros.

2. `return a + b` — Calcula la suma y la DEVUELVE. Quien llama a la funcion
   recibe este valor y puede usarlo.

3. `resultado = sumar(num1, num2)` — LLAMAMOS a la funcion con los valores
   del usuario. Lo que devuelve return se guarda en resultado.

   Diferencia clave: si usara `print(a + b)` en vez de `return a + b`,
   no podria guardar el resultado en una variable.
""")


def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: Funcion promedio")
    print("=" * 50)
    print()

    print("--- CODIGO ---")
    print("""
def promedio(lista):
    return sum(lista) / len(lista)

numeros = [10, 20, 30, 40, 50]
resultado = promedio(numeros)
print(f'El promedio es: {resultado}')
""")

    print("--- EXPLICACION ---")
    print("""
1. `def promedio(lista):` — La funcion recibe una LISTA como parametro.

2. `sum(lista) / len(lista)` — sum() suma TODOS los elementos de la lista.
   len() da la cantidad de elementos. Promedio = suma / cantidad.

3. `promedio(numeros)` — Pasamos la lista completa como argumento.

   La funcion NO SABE cuantos elementos tiene la lista, y no necesita saberlo.
   sum() y len() funcionan con listas de cualquier tamaño.
""")


def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: Filtrar pares con lambda")
    print("=" * 50)
    print()

    print("--- CODIGO ---")
    print("""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = list(filter(lambda x: x % 2 == 0, numeros))

print(f'Numeros pares: {pares}')
""")

    print("--- EXPLICACION ---")
    print("""
1. `filter(funcion, iterable)` — filter() APLICA la funcion a CADA elemento
   del iterable (lista). Si la funcion devuelve True, el elemento pasa el filtro.

2. `lambda x: x % 2 == 0` — Funcion ANONIMA que recibe x y devuelve True si
   x es par (resto 0 al dividir por 2).

3. `list(...)` — filter() devuelve un objeto filter. Lo convertimos a lista
   con list() para poder verlo y usarlo.

   Equivalente sin lambda:
   def es_par(x):
       return x % 2 == 0
   pares = list(filter(es_par, numeros))
""")

    print("--- VARIANTE: Pidiendo los numeros al usuario ---")
    print("""
entrada = input('Ingresa numeros separados por espacio: ')
numeros = list(map(int, entrada.split()))
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f'Pares: {pares}')
""")


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
        print("Ejecuta: python scripts/runner.py 1 5 [N] -s")
