"""
SOLUCIONES - Manejo de Strings
Ejecuta desde raiz: python scripts/runner.py 1 6 [ejercicio] -s
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: Mayusculas y minusculas")
    print("=" * 50)
    print()

    print("--- CODIGO ---")
    print("""
nombre = input('Ingresa tu nombre: ')
print(f'En mayusculas: {nombre.upper()}')
print(f'En minusculas: {nombre.lower()}')
""")

    print("--- EXPLICACION ---")
    print("""
1. `upper()` — Convierte TODOS los caracteres a mayusculas.
   "Ana" → "ANA"

2. `lower()` — Convierte TODOS los caracteres a minusculas.
   "Ana" → "ana"

Estos metodos NO modifican el string original (los strings son inmutables).
Devuelven un NUEVO string con el cambio aplicado.
""")


def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: Invertir palabra y palindromo")
    print("=" * 50)
    print()

    print("--- CODIGO ---")
    print("""
palabra = input('Ingresa una palabra: ')
invertida = palabra[::-1]

print(f'Palabra original: {palabra}')
print(f'Palabra invertida: {invertida}')

if palabra == invertida:
    print('Es un palindromo!')
else:
    print('No es un palindromo')
""")

    print("--- EXPLICACION ---")
    print("""
1. `[::-1]` — Slicing con paso -1. Significa: "desde el inicio hasta el final,
   pero yendo de atras hacia adelante de 1 en 1". Esto INVIERTE el string.

2. `palabra == invertida` — Comparamos el original con el invertido.
   Si son iguales, es palindromo (ej: "reconocer", "ana", "radar").

3. Los strings se comparan caracter por caracter. "ana" == "ana" → True.

   Palindromos famosos: "neuquen", "reconocer", "somos", "radar"
""")


def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: Contar vocales")
    print("=" * 50)
    print()

    print("--- CODIGO ---")
    print("""
frase = input('Ingresa una frase: ').lower()
vocales = 'aeiou'
conteo = 0

for letra in frase:
    if letra in vocales:
        conteo += 1

print(f'La frase tiene {conteo} vocales')
""")

    print("--- EXPLICACION ---")
    print("""
1. `.lower()` al final del input — Convierte toda la frase a minusculas
   INMEDIATAMENTE. Asi 'A' y 'a' se cuentan igual.

2. `vocales = 'aeiou'` — String con las vocales (solo minusculas porque
   ya convertimos la frase).

3. `for letra in frase:` — Itera sobre CADA caracter del string.
   Los strings son iterables: se pueden recorrer letra por letra.

4. `if letra in vocales:` — Pregunta: "esta letra dentro del string vocales?"
   Si letra es 'a', 'a' in 'aeiou' → True. Si es 'z', 'z' in 'aeiou' → False.

5. `conteo += 1` — Si la condicion se cumple, incrementamos el contador.

   NOTA: Tambien se puede hacer con una comprehension:
   conteo = sum(1 for letra in frase if letra in vocales)
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
        print("Ejecuta: python scripts/runner.py 1 6 [N] -s")
