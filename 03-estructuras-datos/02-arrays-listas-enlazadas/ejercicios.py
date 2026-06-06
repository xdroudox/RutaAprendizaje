"""
EJERCICIOS - Arrays y Listas Enlazadas
Ejecuta desde raiz: python scripts/runner.py 3 2 [ejercicio]

Niveles:
  🟢 Ej 1: Clase SinglyLinkedList con append y display
  🟡 Ej 2: Eliminar duplicados de lista enlazada
  🔴 Ej 3: Revertir lista enlazada

Pistas: python scripts/runner.py 3 2 N -p [1|2|3]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1(pista=0):
    """🟢 SinglyLinkedList con append y display"""
    print(">> 🟢 EJERCICIO 1: SinglyLinkedList con append y display")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1:")
        print("  class Nodo:")
        print("      def __init__(self, dato):")
        print("          self.dato = dato")
        print("          self.siguiente = None")
        print()
        print("  Tu SinglyLinkedList necesita:")
        print("  - __init__: self.cabeza = None")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  append(dato):")
        print("    1. Crear nuevo Nodo")
        print("    2. Si cabeza is None → cabeza = nuevo")
        print("    3. Si no → recorrer hasta el ultimo y enlazar")
        print()
        print("  display():")
        print("    1. Empezar desde cabeza")
        print("    2. Mientras actual no sea None:")
        print("       print(actual.dato, end=' -> ')")
        print("       actual = actual.siguiente")
        print("    3. print('None')")
        return
    elif pista == 3:
        print("\n💡 Pista 3:")
        print("  Codigo completo de append:")
        print("  def append(self, dato):")
        print("      nuevo = Nodo(dato)")
        print("      if not self.cabeza:")
        print("          self.cabeza = nuevo")
        print("          return")
        print("      actual = self.cabeza")
        print("      while actual.siguiente:")
        print("          actual = actual.siguiente")
        print("      actual.siguiente = nuevo")
        return

    print("\nImplementa la clase SinglyLinkedList con:")
    print("  1. Clase Nodo (dato y siguiente)")
    print("  2. __init__ con cabeza = None")
    print("  3. append(dato): agrega al final")
    print("  4. display(): muestra elementos")
    print()
    print("--- EJEMPLO DE USO ---")
    print("lista = SinglyLinkedList()")
    print("lista.append(10)")
    print("lista.append(20)")
    print("lista.display()  # 10 -> 20 -> None")
    print()
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")


def ejercicio_2(pista=0):
    """🟡 Eliminar duplicados"""
    print(">> 🟡 EJERCICIO 2: Eliminar duplicados de lista enlazada")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1:")
        print("  Para trackear valores vistos usa un set():")
        print("  vistos = set()")
        print("  Agrega cada dato que encuentres.")
        print("  Si el siguiente ya esta en vistos → lo SALTAS.")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  def eliminar_duplicados(lista):")
        print("      if not lista.cabeza: return")
        print("      vistos = {lista.cabeza.dato}")
        print("      actual = lista.cabeza")
        print("      while actual.siguiente:")
        print("          if actual.siguiente.dato in vistos:")
        print("              actual.siguiente = actual.siguiente.siguiente")
        print("          else:")
        print("              vistos.add(actual.siguiente.dato)")
        print("              actual = actual.siguiente")
        return
    elif pista == 3:
        print("\n💡 Pista 3:")
        print("  La clave: cuando encuentras un duplicado, NO avanzas")
        print("  al siguiente nodo (porque puede haber MAS duplicados")
        print("  consecutivos). Solo avanzas cuando NO hay duplicado.")
        return

    print("\nImplementa:")
    print("  def eliminar_duplicados(lista):")
    print()
    print("  Entrada: lista = 10 -> 20 -> 10 -> 30 -> 20")
    print("  Salida:  lista = 10 -> 20 -> 30")
    print()
    print("Usa un set() para trackear valores vistos.")
    print()
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")


def ejercicio_3(pista=0):
    """🔴 Revertir lista enlazada"""
    print(">> 🔴 EJERCICIO 3: Revertir lista enlazada")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1:")
        print("  Necesitas 3 variables: anterior, actual, siguiente")
        print("  En cada paso:")
        print("    1. Guardar el siguiente nodo")
        print("    2. Invertir el enlace: actual.siguiente = anterior")
        print("    3. Avanzar: anterior = actual, actual = siguiente")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  def revertir(lista):")
        print("      anterior = None")
        print("      actual = lista.cabeza")
        print("      while actual:")
        print("          siguiente = actual.siguiente")
        print("          actual.siguiente = anterior")
        print("          anterior = actual")
        print("          actual = siguiente")
        print("      lista.cabeza = anterior")
        return
    elif pista == 3:
        print("\n💡 Pista 3:")
        print("  Visualizacion de un paso:")
        print("  Antes:  ... → [A|·] → [B|·] → [C|·] → ...")
        print("                         ↑ actual")
        print("  Paso:   actual.siguiente = anterior")
        print("  Despues: ... → [A|·] → [B|·] → None  [C|·] → ...")
        print("                         ↑ actual      ↑ siguiente")
        print("  Luego: anterior = actual, actual = siguiente")
        return

    print("\nImplementa:")
    print("  def revertir(lista):")
    print()
    print("  Entrada: lista = 10 -> 20 -> 30 -> None")
    print("  Salida:  lista = 30 -> 20 -> 10 -> None")
    print()
    print("Debe ser IN-PLACE (sin crear nuevos nodos).")
    print()
    print("# ==== ESCRIBE TU RESPUESTA AQUI ====")


if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            pista = 0
            if "-p" in sys.argv:
                idx = sys.argv.index("-p")
                if idx + 1 < len(sys.argv) and sys.argv[idx + 1].isdigit():
                    pista = int(sys.argv[idx + 1])
            ejercicios[num](pista)
    else:
        print("EJERCICIOS:")
        for i, ej in enumerate(ejercicios, 1):
            doc = ej.__doc__ or ""
            print(f"  {i}. {doc}")
