"""
EJERCICIOS - Pruebas Unitarias
Ejecuta desde raiz: python scripts/runner.py 7 1 [ejercicio] [-p N]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1(pista=0):
    """Escribir funcion es_par() y probarla con assert"""
    print(">> EJERCICIO 1: Escribir funcion es_par() y probarla con assert")
    print("-" * 40)
    print("Escribe una funcion es_par(n) que retorne True si n es par.")
    print("Luego pruebala con assert para varios casos (0, 2, 3, -1, etc.).")
    print()
    print("def es_par(n):")
    print("    # ==== ESCRIBE TU RESPUESTA AQUI ====")
    print("    pass")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  Un numero es par si el residuo de dividirlo entre 2 es 0.")
        print("  En Python: n % 2 == 0")
        print("  La funcion debe retornar True o False con 'return'.")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  def es_par(n):")
        print("      return n % 2 == 0")
        print()
        print("  Pruebas sugeridas:")
        print("  assert es_par(2) == True")
        print("  assert es_par(0) == True")
        print("  assert es_par(3) == False")
        print("  assert es_par(-2) == True")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  def es_par(n):")
        print("      return n % 2 == 0")
        print()
        print("  assert es_par(2) == True")
        print("  assert es_par(0) == True")
        print("  assert es_par(3) == False")
        print("  assert es_par(-2) == True")
        print("  assert es_par(-3) == False")
        print("  print('Todas las pruebas pasaron')")

def ejercicio_2(pista=0):
    """Escribir test para funcion que suma lista"""
    print(">> EJERCICIO 2: Escribir test para funcion que suma lista")
    print("-" * 40)
    print("Escribe una funcion sumar_lista(numeros) que sume los elementos")
    print("de una lista. Luego escribe pruebas con assert que verifiquen:")
    print("- Lista vacia retorna 0")
    print("- [1,2,3] retorna 6")
    print("- [-1,1] retorna 0")
    print()
    print("def sumar_lista(numeros):")
    print("    # ==== ESCRIBE TU RESPUESTA AQUI ====")
    print("    pass")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  La funcion sum() de Python suma todos los elementos de un iterable.")
        print("  sum([]) retorna 0 (lista vacia).")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  def sumar_lista(numeros):")
        print("      return sum(numeros)")
        print()
        print("  Pruebas:")
        print("  assert sumar_lista([]) == 0")
        print("  assert sumar_lista([1, 2, 3]) == 6")
        print("  assert sumar_lista([-1, 1]) == 0")
        print("  assert sumar_lista([5]) == 5")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  def sumar_lista(numeros):")
        print("      return sum(numeros)")
        print()
        print("  assert sumar_lista([]) == 0")
        print("  assert sumar_lista([1, 2, 3]) == 6")
        print("  assert sumar_lista([-1, 1]) == 0")
        print("  assert sumar_lista([5]) == 5")
        print("  print('Todas las pruebas de sumar_lista pasaron')")

def ejercicio_3(pista=0):
    """Usar pytest (funcion test_...)"""
    print(">> EJERCICIO 3: Usar pytest (funcion test_...)")
    print("-" * 40)
    print("Convierte las pruebas anteriores en funciones test_* que pytest")
    print("pueda ejecutar. Escribe:")
    print()
    print("def test_es_par():")
    print("    # ==== ESCRIBE TU RESPUESTA AQUI ====")
    print("    pass")
    print()
    print("def test_sumar_lista():")
    print("    # ==== ESCRIBE TU RESPUESTA AQUI ====")
    print("    pass")
    print()
    print("Ejecuta con: pytest")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  pytest descubre automaticamente funciones que empiezan con test_.")
        print("  Crea un archivo .py con las funciones test_* y las funciones a probar.")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  Crea un archivo test_pruebas.py con:")
        print()
        print("  def es_par(n):")
        print("      return n % 2 == 0")
        print()
        print("  def sumar_lista(numeros):")
        print("      return sum(numeros)")
        print()
        print("  def test_es_par():")
        print("      assert es_par(2) == True")
        print("      assert es_par(3) == False")
        print("      assert es_par(0) == True")
        print()
        print("  def test_sumar_lista():")
        print("      assert sumar_lista([]) == 0")
        print("      assert sumar_lista([1, 2, 3]) == 6")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  Crea test_pruebas.py y ejecuta: pytest test_pruebas.py -v")
        print()
        print("  def es_par(n):")
        print("      return n % 2 == 0")
        print()
        print("  def sumar_lista(numeros):")
        print("      return sum(numeros)")
        print()
        print("  def test_es_par():")
        print("      assert es_par(2) == True")
        print("      assert es_par(3) == False")
        print("      assert es_par(0) == True")
        print()
        print("  def test_sumar_lista():")
        print("      assert sumar_lista([]) == 0")
        print("      assert sumar_lista([1, 2, 3]) == 6")
        print("      assert sumar_lista([-1, 1]) == 0")

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    pista_level = 0
    if "-p" in sys.argv:
        idx = sys.argv.index("-p")
        if idx + 1 < len(sys.argv) and sys.argv[idx + 1].isdigit():
            pista_level = int(sys.argv[idx + 1])
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            ejercicios[num](pista=pista_level)
    else:
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
