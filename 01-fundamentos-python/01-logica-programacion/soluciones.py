"""
SOLUCIONES - Logica de Programacion
Ejecuta desde raiz: python scripts/runner.py 1 1 [ejercicio] -s
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: Preparar un sandwich")
    print("=" * 50)
    print()

    print("--- CODIGO ---")
    print("""
print('1. Abrir la nevera')
print('2. Sacar pan, jamon, queso y lechuga')
print('3. Colocar dos rebanadas de pan en un plato')
print('4. Agregar jamon, queso y lechuga a una rebanada')
print('5. Colocar la otra rebanada de pan encima')
print('6. Disfrutar del sandwich')
""")

    print("--- EXPLICACION ---")
    print("""
Cada print() muestra un paso del algoritmo en la pantalla.
El orden importa: no puedes poner el jamon antes de abrir la nevera.

En programacion, cuando las instrucciones se ejecutan secuencialmente
(una tras otra), el ORDEN es fundamental.
""")


def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: Par o impar")
    print("=" * 50)
    print()

    print("--- CODIGO ---")
    print("""
numero = int(input('Ingresa un numero: '))
if numero % 2 == 0:
    print(f'{numero} es PAR')
else:
    print(f'{numero} es IMPAR')
""")

    print("--- EXPLICACION ---")
    print("""
1. `int(input(...))` — Leemos texto y convertimos a entero.

2. `numero % 2` — El operador % da el RESTO de la division.
   - Si numero = 4: 4 % 2 = 0 (4/2=2, resto 0) → PAR
   - Si numero = 7: 7 % 2 = 1 (7/2=3, resto 1) → IMPAR

3. `if numero % 2 == 0:` — Si el resto es 0, es divisible por 2 = PAR.

4. `else:` — Si no se cumplio el if, forzosamente es IMPAR.
""")


def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: Mayor de 3 numeros")
    print("=" * 50)
    print()

    print("--- CODIGO (Version con if/elif) ---")
    print("""
a = int(input('Numero 1: '))
b = int(input('Numero 2: '))
c = int(input('Numero 3: '))

if a >= b and a >= c:
    print(f'El mayor es {a}')
elif b >= a and b >= c:
    print(f'El mayor es {b}')
else:
    print(f'El mayor es {c}')
""")

    print("--- EXPLICACION ---")
    print("""
1. Pedimos 3 numeros y los guardamos en a, b, c.

2. `if a >= b and a >= c:` — Pregunta: "a es mayor o igual que b Y
   tambien mayor o igual que c?" Si ambas condiciones se cumplen,
   a es el mayor (o hay empate).

3. `elif b >= a and b >= c:` — Si NO fue a, preguntamos por b.

4. `else:` — Si no fue ni a ni b, entonces c es el mayor.

   NOTA: Usamos >= en vez de > para manejar EMPATES. Si dos numeros
   son iguales, cualquiera de los dos es valido como "mayor".
""")

    print("--- ALTERNATIVA: Usando max() ---")
    print("""
# La forma mas simple:
print(f'El mayor es {max(a, b, c)}')
# Pero el ejercicio era SIN usar max() para practicar logica.
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
        print("Ejecuta: python scripts/runner.py 1 1 [N] -s")
