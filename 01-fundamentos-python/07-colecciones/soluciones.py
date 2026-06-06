"""
SOLUCIONES - Colecciones
Ejecuta desde raiz: python scripts/runner.py 1 7 [ejercicio] -s
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


# ---------------------------------------------------------------------------
# 🟢 SOLUCION 1: Operaciones con listas
# ---------------------------------------------------------------------------

def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: Operaciones con listas")
    print("=" * 50)
    print()

    print("--- CODIGO ---")
    print("""
nums = []

# Agregar 1 al 5 con append()
nums.append(1)
nums.append(2)
nums.append(3)
nums.append(4)
nums.append(5)
print('Despues de append:', nums)  # [1, 2, 3, 4, 5]

# Insertar 0 al principio
nums.insert(0, 0)
print('Despues de insert(0, 0):', nums)  # [0, 1, 2, 3, 4, 5]

# Eliminar el ultimo elemento
ultimo = nums.pop()
print(f'Elemento eliminado: {ultimo}')  # 5
print('Despues de pop():', nums)  # [0, 1, 2, 3, 4]

# Mostrar resultado final
print(f'Lista final: {nums}')
print(f'Longitud: {len(nums)}')
""")

    print("--- EXPLICACION ---")
    print("""
1. `nums = []` — Creamos una lista vacia.

2. `nums.append(1)` — append() agrega el elemento al FINAL de la lista.
   Despues de 5 append: [1, 2, 3, 4, 5].

3. `nums.insert(0, 0)` — insert(posicion, elemento) inserta en la posicion
   indicada. insert(0, 0) pone el 0 al principio: [0, 1, 2, 3, 4, 5].

4. `nums.pop()` — pop() sin argumentos elimina y devuelve el ULTIMO elemento.
   El 5 sale de la lista: [0, 1, 2, 3, 4].

5. `len(nums)` — Devuelve la cantidad de elementos: 5.
""")

    print("--- VARIANTE: con bucle for ---")
    print("""
nums = []
for i in range(1, 6):
    nums.append(i)
# Mismo resultado, menos repetitivo
""")


# ---------------------------------------------------------------------------
# 🟡 SOLUCION 2: Agenda telefonica
# ---------------------------------------------------------------------------

def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: Agenda telefonica")
    print("=" * 50)
    print()

    print("--- CODIGO ---")
    print("""
agenda = {}

while True:
    print()
    print('=== AGENDA TELEFONICA ===')
    print('1. Agregar contacto')
    print('2. Buscar telefono')
    print('3. Mostrar todos')
    print('4. Salir')
    print('=========================')

    opcion = input('Elige una opcion: ')

    if opcion == '1':
        nombre = input('Nombre: ')
        telefono = input('Telefono: ')
        agenda[nombre] = telefono
        print(f'Contacto {nombre} agregado.')

    elif opcion == '2':
        nombre = input('Nombre a buscar: ')
        telefono = agenda.get(nombre)
        if telefono:
            print(f'{nombre}: {telefono}')
        else:
            print(f'{nombre} no encontrado.')

    elif opcion == '3':
        if not agenda:
            print('La agenda esta vacia.')
        else:
            print('Contactos:')
            for nombre, telefono in agenda.items():
                print(f'  {nombre}: {telefono}')

    elif opcion == '4':
        print('Hasta luego!')
        break

    else:
        print('Opcion no valida. Intenta de nuevo.')
""")

    print("--- EXPLICACION ---")
    print("""
1. `agenda = {}` — Diccionario vacio.

2. `while True:` — Bucle infinito para el menu. Solo se sale con break.

3. `agenda[nombre] = telefono` — Agrega un par clave:valor al diccionario.
   Si el nombre ya existe, SE SOBRESCRIBE el telefono.

4. `agenda.get(nombre)` — Metodo SEGURO para buscar. Si la clave NO existe,
   devuelve None en vez de lanzar error (a diferencia de agenda[nombre]).

5. `for nombre, telefono in agenda.items():` — .items() devuelve pares
   (clave, valor). Los desempaquetamos en dos variables.

6. `if not agenda:` — Un diccionario vacio es "falsy". Si tiene elementos,
   es "truthy". Forma Pythonica de verificar si hay datos.
""")

    print("--- VARIANTE: con .get() con valor por defecto ---")
    print("""
telefono = agenda.get(nombre, 'NO REGISTRADO')
print(f'{nombre}: {telefono}')
# Si no existe, muestra 'NO REGISTRADO' en vez de None
""")


# ---------------------------------------------------------------------------
# 🔴 SOLUCION 3: Analizador de texto
# ---------------------------------------------------------------------------

def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: Analizador de texto")
    print("=" * 50)
    print()

    print("--- CODIGO ---")
    print("""
frase = input('Ingresa una frase o parrafo: ')

# Dividir en palabras
palabras = frase.split()

# 1. Total de caracteres
print(f'\\nTotal de caracteres: {len(frase)}')

# 2. Cantidad de palabras
print(f'Cantidad de palabras: {len(palabras)}')

# 3. Frecuencia de cada palabra
frecuencia = {}
for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

print('\\nFrecuencia de palabras:')
for palabra, conteo in sorted(frecuencia.items()):
    print(f'  {palabra}: {conteo}')

# 4. Palabra mas larga
mas_larga = max(palabras, key=len)
print(f'\\nPalabra mas larga: {mas_larga} ({len(mas_larga)} letras)')
""")

    print("--- EXPLICACION ---")
    print("""
1. `frase.split()` — Divide el string en palabras usando espacios como separador.
   "Hola mundo cruel" → ["Hola", "mundo", "cruel"]

2. `len(frase)` — Cuenta TODOS los caracteres, incluyendo espacios. Si quieres
   solo letras, hariamos: len(frase.replace(' ', '')).

3. `len(palabras)` — Cuenta cuantos elementos tiene la lista de palabras.

4. `frecuencia.get(palabra, 0) + 1` — FORMA INTELIGENTE de contar frecuencias:
   - Si la palabra NO existe en el diccionario, .get() devuelve 0, luego +1 = 1
   - Si la palabra YA existe, .get() devuelve el valor actual, luego +1
   - Esto evita tener que hacer un if/else explicito

5. `sorted(frecuencia.items())` — Ordena alfabeticamente las palabras para
   una salida mas legible. sorted() sin argumentos extra ordena por clave.

6. `max(palabras, key=len)` — Encuentra el elemento MAXIMO segun un criterio.
   key=len significa "compara por longitud". Devuelve la palabra con mayor len().
""")

    print("--- VARIANTE: ignorando mayusculas y signos ---")
    print("""
import string
# Limpiar la frase: minusculas + quitar puntuacion
frase_limpia = frase.lower()
for signo in string.punctuation:
    frase_limpia = frase_limpia.replace(signo, '')
palabras = frase_limpia.split()
# Ahora "Hola" y "hola" cuentan como la misma palabra
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
        print("Ejecuta: python scripts/runner.py 1 7 [N] -s")
