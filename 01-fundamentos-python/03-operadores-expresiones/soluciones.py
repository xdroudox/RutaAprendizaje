"""
SOLUCIONES - Operadores y Expresiones
Ejecuta desde raiz: python scripts/runner.py 1 3 [ejercicio] -s
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: Calculadora de propina")
    print("=" * 50)
    print()

    print("--- CODIGO ---")
    print("""
total = float(input('Total de la cuenta: $'))
porcentaje = float(input('Porcentaje de propina: '))

propina = total * porcentaje / 100
total_pagar = total + propina

print(f'Propina: ${propina:.2f}')
print(f'Total a pagar: ${total_pagar:.2f}')
""")

    print("--- EXPLICACION ---")
    print("""
1. `float(input(...))` — Usamos float para aceptar decimales ($12.50, etc.)

2. `propina = total * porcentaje / 100` — Calculamos el monto.
   Ej: total=50, porcentaje=15 → 50 * 15 / 100 = 7.5

3. `.2f` en el f-string — Formatea con 2 decimales. 7.5 se muestra como 7.50.
""")


def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: Ano bisiesto")
    print("=" * 50)
    print()

    print("--- CODIGO ---")
    print("""
year = int(input('Ingresa un ano: '))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f'{year} es bisiesto')
else:
    print(f'{year} no es bisiesto')
""")

    print("--- EXPLICACION ---")
    print("""
Regla oficial: Un ano es bisiesto si:
- Es divisible entre 4, PERO
- NO es divisible entre 100 (siglo), EXCEPTO
- Si es divisible entre 400 (si es siglo, igual es bisiesto)

Desglose de la condicion:
- `year % 4 == 0` → divisible entre 4? Ej: 2024 si, 2023 no.
- `year % 100 != 0` → NO es divisible entre 100? (no es siglo)
- `year % 400 == 0` → Es divisible entre 400? (siglo bisiesto)

La condicion completa:
`(year % 4 == 0 and year % 100 != 0)` — anos normales bisiestos
`or (year % 400 == 0)` — siglos bisiestos (2000, 2400)

Ejemplos:
- 2024: divisible entre 4, no entre 100 → BISIESTO
- 1900: divisible entre 4 y entre 100, pero NO entre 400 → NO bisiesto
- 2000: divisible entre 4, entre 100, y entre 400 → BISIESTO
""")


def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: Verificar triangulo")
    print("=" * 50)
    print()

    print("--- CODIGO ---")
    print("""
a = float(input('Lado 1: '))
b = float(input('Lado 2: '))
c = float(input('Lado 3: '))

if a + b > c and a + c > b and b + c > a:
    print('Los lados SI pueden formar un triangulo')
else:
    print('Los lados NO pueden formar un triangulo')
""")

    print("--- EXPLICACION ---")
    print("""
La DESIGUALDAD TRIANGULAR dice: la suma de dos lados SIEMPRE debe ser
mayor que el tercero. Y esto debe cumplirse para LAS 3 combinaciones.

`a + b > c` → lado mas corto? se cumple
`a + c > b` → combinando de otra forma? se cumple
`b + c > a` → la tercera forma? se cumple

Si CUALQUIERA de las 3 no se cumple, no es triangulo.

AND conecta las 3 condiciones: TODAS deben ser True.

Ejemplo: 3, 4, 5
- 3 + 4 > 5 → 7 > 5 ✅
- 3 + 5 > 4 → 8 > 4 ✅
- 4 + 5 > 3 → 9 > 3 ✅
→ SI es triangulo (es un triangulo rectangulo, de hecho)

Ejemplo: 1, 1, 3
- 1 + 1 > 3 → 2 > 3 ❌
→ NO es triangulo
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
        print("Ejecuta: python scripts/runner.py 1 3 [N] -s")
