"""
SOLUCIONES - Variables y Tipos de Datos
Ejecuta desde raiz: python scripts/runner.py 1 2 [ejercicio] -s
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: Presentacion personal")
    print("=" * 50)
    print()

    print("--- CODIGO ---")
    print("""
nombre = input('Tu nombre: ')
edad = input('Tu edad: ')
ciudad = input('Tu ciudad: ')

print(f'Hola, me llamo {nombre}, tengo {edad} anos y vivo en {ciudad}')
""")

    print("--- EXPLICACION ---")
    print("""
1. `nombre = input(...)` — input() muestra el texto y espera que el usuario
   escriba algo. Lo que escriba se guarda en la variable.

2. Las 3 variables son de tipo str (porque input() siempre devuelve texto).

3. `f'...{nombre}...{edad}...{ciudad}...'` — f-string: las {llaves} se
   reemplazan por el valor de las variables.

   NOTA: edad es str porque no la convertimos con int(). Para solo mostrar,
   no hace falta convertir.
""")


def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: Edad en dias")
    print("=" * 50)
    print()

    print("--- CODIGO ---")
    print("""
edad_str = input('Cuantos anos tienes? ')
edad = int(edad_str)
dias = edad * 365
print(f'Has vivido aproximadamente {dias} dias')
""")

    print("--- EXPLICACION ---")
    print("""
1. `edad_str = input(...)` — Guardamos el texto que ingresa el usuario.

2. `edad = int(edad_str)` — CONVERTIMOS el texto a entero con int().
   Si no hicieramos esto, "25" * 365 daria "252525..."" (repite el texto 365 veces).

3. `dias = edad * 365` — Multiplicacion normal de enteros.

4. `print(f'...{dias}...')` — Mostramos el resultado.

   POR QUE CONVERTIR? input() devuelve str. Los strings se multiplican
   repitiendose: "5" * 3 = "555". Los enteros se multiplican: 5 * 3 = 15.
""")

    print("--- VERSION CORTA (una linea menos) ---")
    print("""
edad = int(input('Cuantos anos tienes? '))
print(f'Has vivido aproximadamente {edad * 365} dias')
""")


def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: Detector de tipos")
    print("=" * 50)
    print()

    print("--- CODIGO ---")
    print("""
v1 = input('Valor 1: ')
v2 = input('Valor 2: ')
v3 = input('Valor 3: ')

print(f'{v1} es de tipo {type(v1)}')
print(f'{v2} es de tipo {type(v2)}')
print(f'{v3} es de tipo {type(v3)}')
""")

    print("--- EXPLICACION ---")
    print("""
1. `input()` SIEMPRE devuelve un string (str), SIN IMPORTAR lo que escriba
   el usuario. Si escribe "25", es texto "25", no el numero 25.

2. `type(v1)` devuelve el tipo de la variable: <class 'str'>.

3. Los 3 valores seran de tipo str aunque el usuario escriba numeros.
   Para tener numeros, debemos convertirlos explicitamente con int() o float().

   ESTO ES IMPORTANTE: es una confusion comun en principiantes.
   input() = texto. Siempre. Sin excepcion.
""")

    print("--- PRUEBA ---")
    print("""
Si el usuario escribe: 25, Hola, 3.14
type(v1) = <class 'str'>
type(v2) = <class 'str'>
type(v3) = <class 'str'>
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
        print("Ejecuta: python scripts/runner.py 1 2 [N] -s")
