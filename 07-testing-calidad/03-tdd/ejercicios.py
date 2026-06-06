"""
EJERCICIOS - TDD (Test Driven Development)
Ejecuta desde raiz: python scripts/runner.py 7 3 [ejercicio] [-p N]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1(pista=0):
    """FizzBuzz con TDD (escribir test primero)"""
    print(">> EJERCICIO 1: FizzBuzz con TDD (escribir test primero)")
    print("-" * 40)
    print("Implementa FizzBuzz siguiendo TDD:")
    print("- Multiplo de 3 -> 'Fizz'")
    print("- Multiplo de 5 -> 'Buzz'")
    print("- Multiplo de 3 y 5 -> 'FizzBuzz'")
    print("- Otro -> str(n)")
    print()
    print("PASO 1 - RED: Escribe el test primero")
    print("def test_fizzbuzz_retorna_numero():")
    print("    assert fizzbuzz(1) == '1'")
    print("    assert fizzbuzz(2) == '2'")
    print()
    print("PASO 2 - GREEN: Implementa el minimo")
    print("def fizzbuzz(n):")
    print("    # ==== ESCRIBE TU RESPUESTA AQUI ====")
    print("    pass")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  El orden de las condiciones importa:")
        print("  1. Primero verifica si es multiplo de 3 y 5 (FizzBuzz)")
        print("  2. Luego solo de 3 (Fizz)")
        print("  3. Luego solo de 5 (Buzz)")
        print("  4. Si no es ninguno, str(n)")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  def fizzbuzz(n):")
        print("      if n % 3 == 0 and n % 5 == 0:")
        print("          return 'FizzBuzz'")
        print("      if n % 3 == 0:")
        print("          return 'Fizz'")
        print("      if n % 5 == 0:")
        print("          return 'Buzz'")
        print("      return str(n)")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  def fizzbuzz(n):")
        print("      if n % 3 == 0 and n % 5 == 0:")
        print("          return 'FizzBuzz'")
        print("      if n % 3 == 0:")
        print("          return 'Fizz'")
        print("      if n % 5 == 0:")
        print("          return 'Buzz'")
        print("      return str(n)")
        print()
        print("  assert fizzbuzz(1) == '1'")
        print("  assert fizzbuzz(3) == 'Fizz'")
        print("  assert fizzbuzz(5) == 'Buzz'")
        print("  assert fizzbuzz(15) == 'FizzBuzz'")

def ejercicio_2(pista=0):
    """Validador de email con TDD"""
    print(">> EJERCICIO 2: Validador de email con TDD")
    print("-" * 40)
    print("Implementa un validador de email usando TDD.")
    print("La funcion validar_email(email) debe:")
    print("- Tener exactamente un '@'")
    print("- Tener algo antes y despues del '@'")
    print("- Tener un punto despues del '@'")
    print("- No tener espacios")
    print()
    print("Ciclo TDD:")
    print("RED: Escribe test_validar_email() con varios casos")
    print("GREEN: Implementa la funcion")
    print("REFACTOR: Mejora el codigo")
    print()
    print("def validar_email(email):")
    print("    # ==== ESCRIBE TU RESPUESTA AQUI ====")
    print("    pass")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  Pasos para validar:")
        print("  1. Si contiene espacios -> False")
        print("  2. Si no tiene exactamente 1 '@' -> False")
        print("  3. Dividir por '@', verificar que ambas partes no esten vacias")
        print("  4. Verificar que la parte del dominio tenga un punto")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  def validar_email(email):")
        print("      if ' ' in email:")
        print("          return False")
        print("      if email.count('@') != 1:")
        print("          return False")
        print("      local, dominio = email.split('@')")
        print("      if not local or not dominio:")
        print("          return False")
        print("      if '.' not in dominio:")
        print("          return False")
        print("      return True")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  def validar_email(email):")
        print("      if ' ' in email:")
        print("          return False")
        print("      if email.count('@') != 1:")
        print("          return False")
        print("      local, dominio = email.split('@')")
        print("      if not local or not dominio:")
        print("          return False")
        print("      if '.' not in dominio:")
        print("          return False")
        print("      return True")
        print()
        print("  assert validar_email('user@example.com') == True")
        print("  assert validar_email('sinarroba') == False")
        print("  assert validar_email('user@') == False")
        print("  assert validar_email('@dominio.com') == False")
        print("  assert validar_email('user con@espacio.com') == False")

def ejercicio_3(pista=0):
    """Calculadora de promedios con TDD"""
    print(">> EJERCICIO 3: Calculadora de promedios con TDD")
    print("-" * 40)
    print("Implementa calcular_promedio(numeros) con TDD.")
    print("Requisitos:")
    print("- Lista vacia retorna 0")
    print("- Calcula el promedio correctamente")
    print("- Elemento no numerico lanza TypeError")
    print()
    print("def calcular_promedio(numeros):")
    print("    # ==== ESCRIBE TU RESPUESTA AQUI ====")
    print("    pass")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  - Si la lista esta vacia, retorna 0")
        print("  - Suma todos los elementos y divide entre la longitud")
        print("  - Para TypeError: recorre la lista y verifica isinstance(n, (int, float))")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  def calcular_promedio(numeros):")
        print("      if not numeros:")
        print("          return 0")
        print("      for n in numeros:")
        print("          if not isinstance(n, (int, float)):")
        print("              raise TypeError('Elemento no numerico')")
        print("      return sum(numeros) / len(numeros)")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  def calcular_promedio(numeros):")
        print("      if not numeros:")
        print("          return 0")
        print("      for n in numeros:")
        print("          if not isinstance(n, (int, float)):")
        print("              raise TypeError('Elemento no numerico')")
        print("      return sum(numeros) / len(numeros)")
        print()
        print("  assert calcular_promedio([]) == 0")
        print("  assert calcular_promedio([1, 2, 3]) == 2.0")
        print("  assert calcular_promedio([5]) == 5.0")
        print("  try:")
        print("      calcular_promedio([1, 'a'])")
        print("      assert False, 'Debio lanzar TypeError'")
        print("  except TypeError:")
        print("      pass")

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
