"""
SOLUCIONES - Arrays y Listas Enlazadas
Ejecuta: python scripts/runner.py 3 2 [ejercicio] -s
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: SinglyLinkedList")
    print("=" * 50)

    print("""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class SinglyLinkedList:
    def __init__(self):
        self.cabeza = None

    def append(self, dato):
        \"\"\"Agrega al final O(n)\"\"\"
        nuevo = Nodo(dato)
        if not self.cabeza:          # Lista vacia
            self.cabeza = nuevo
            return
        actual = self.cabeza
        while actual.siguiente:      # Llegar al ultimo nodo
            actual = actual.siguiente
        actual.siguiente = nuevo     # Enlazar nuevo nodo

    def display(self):
        \"\"\"Muestra elementos separados por ->\"\"\"
        actual = self.cabeza
        while actual:
            print(actual.dato, end=' -> ')
            actual = actual.siguiente
        print('None')
""")

    print("--- EXPLICACION ---")
    print("""
- Nodo: unidad basica con dato y puntero al siguiente.
- append(): si la lista esta vacia, el nuevo nodo es la cabeza.
  Si no, recorre hasta el final y enlaza.
- display(): recorre desde cabeza imprimiendo cada dato.
  end=' -> ' evita el salto de linea entre elementos.
  El bucle termina cuando actual es None.
- Complejidad append(): O(n) — recorre toda la lista.
- Complejidad display(): O(n) — recorre toda la lista.
""")


def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: Eliminar duplicados")
    print("=" * 50)

    print("""
def eliminar_duplicados(lista):
    if not lista.cabeza:
        return

    vistos = set()
    vistos.add(lista.cabeza.dato)
    actual = lista.cabeza

    while actual.siguiente:
        if actual.siguiente.dato in vistos:
            # Saltar el nodo duplicado
            actual.siguiente = actual.siguiente.siguiente
        else:
            vistos.add(actual.siguiente.dato)
            actual = actual.siguiente
""")

    print("--- EXPLICACION ---")
    print("""
1. Si la lista esta vacia, no hay nada que eliminar.

2. Creamos un set vacio 'vistos'. Un set tiene busqueda O(1),
   mucho mas eficiente que una lista (O(n)).

3. Agregamos el primer nodo a vistos y empezamos desde alli.

4. Para cada nodo siguiente:
   - SI ya esta en vistos → lo SALTAMOS:
     actual.siguiente = actual.siguiente.siguiente
     (Esto efectivamente elimina el nodo duplicado de la cadena)
   - SI NO esta en vistos → lo agregamos y AVANZAMOS:
     actual = actual.siguiente

5. Importante: NO avanzamos cuando encontramos un duplicado,
   porque puede haber varios duplicados consecutivos.

Ejemplo:
  Entrada: 10 -> 20 -> 10 -> 30 -> 20 -> None
  vistos = {10}, actual = 10
  20 no en vistos → vistos = {10, 20}, actual = 20
  10 SI en vistos → saltar, actual sigue en 20
  30 no en vistos → vistos = {10, 20, 30}, actual = 30
  20 SI en vistos → saltar
  Resultado: 10 -> 20 -> 30 -> None
""")


def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: Revertir lista enlazada")
    print("=" * 50)

    print("""
def revertir(lista):
    anterior = None
    actual = lista.cabeza

    while actual:
        siguiente = actual.siguiente   # 1. Guardar siguiente
        actual.siguiente = anterior    # 2. Invertir enlace
        anterior = actual              # 3. Avanzar anterior
        actual = siguiente             # 4. Avanzar actual

    lista.cabeza = anterior            # Nueva cabeza
""")

    print("--- EXPLICACION ---")
    print("""
Este algoritmo recorre la lista UNA sola vez (O(n)), invirtiendo
cada enlace sobre la marcha. Usa 3 punteros:

1. anterior: nodo que estaba antes del actual (empieza en None)
2. actual: nodo que estamos procesando (empieza en cabeza)
3. siguiente: guarda el siguiente antes de perder la referencia

En cada iteracion:
  1. Guardamos 'siguiente' (antes de romper el enlace)
  2. Hacemos que 'actual' apunte hacia ATRAS (a 'anterior')
  3. Avanzamos 'anterior' a donde estaba 'actual'
  4. Avanzamos 'actual' al que habia sido 'siguiente'

Al final, 'anterior' termina apuntando al ultimo nodo,
que ahora es la nueva cabeza.

Visual:
  Inicio:    10 -> 20 -> 30 -> None
  Paso 1:    None <- 10  20 -> 30
  Paso 2:    None <- 10 <- 20  30
  Paso 3:    None <- 10 <- 20 <- 30
  Final:     30 -> 20 -> 10 -> None

Complejidad: O(n) tiempo, O(1) espacio (in-place).
""")


if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
