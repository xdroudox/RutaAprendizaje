"""
EJERCICIOS - TDD (Test Driven Development)
Ejecuta: python ejercicios.py [numero]

Uso:
  python ejercicios.py      -> Menu
  python ejercicios.py 1    -> Ejercicio 1
  python ejercicios.py -s 1 -> Solucion del ejercicio 1
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1():
    print("=" * 50)
    print(">> EJERCICIO 1: FizzBuzz con TDD")
    print("=" * 50)
    print()
    print("Implementa la funcion fizzbuzz(n) usando el ciclo TDD.")
    print()
    print("Reglas de FizzBuzz:")
    print("  - Si n es multiplo de 3, retorna 'Fizz'")
    print("  - Si n es multiplo de 5, retorna 'Buzz'")
    print("  - Si n es multiplo de 3 y 5, retorna 'FizzBuzz'")
    print("  - En otro caso, retorna str(n)")
    print()
    print("PASOS TDD:")
    print("  RED:   Escribir prueba test_fizzbuzz_retorna_numero()")
    print("         assert fizzbuzz(1) == '1'")
    print("         assert fizzbuzz(2) == '2'")
    print("  GREEN: def fizzbuzz(n): return str(n)")
    print("  RED:   Escribir test_fizzbuzz_multiplo_de_3()")
    print("         assert fizzbuzz(3) == 'Fizz'")
    print("  GREEN: Agregar if n % 3 == 0: return 'Fizz'")
    print("  RED:   Escribir test_fizzbuzz_multiplo_de_5()")
    print("  RED:   Escribir test_fizzbuzz_multiplo_de_3_y_5()")
    print()
    print("PISTA: Completa la funcion fizzbuzz siguiendo el ciclo")
    print()
    print("Edita el archivo:")
    print("def fizzbuzz(n):")
    print("    # --- TU CODIGO AQUI ---")


def solucion_1():
    print("=" * 50)
    print("SOLUCION 1: FizzBuzz con TDD")
    print("=" * 50)
    print()
    print("Implementacion final de FizzBuzz:")
    print()
    print("```python")
    print("def fizzbuzz(n):")
    print("    if n % 3 == 0 and n % 5 == 0:")
    print("        return 'FizzBuzz'")
    print("    if n % 3 == 0:")
    print("        return 'Fizz'")
    print("    if n % 5 == 0:")
    print("        return 'Buzz'")
    print("    return str(n)")
    print("```")
    print()
    print("Pruebas correspondientes:")
    print()
    print("```python")
    print("def test_fizzbuzz_retorna_numero():")
    print("    assert fizzbuzz(1) == '1'")
    print("    assert fizzbuzz(2) == '2'")
    print("    assert fizzbuzz(4) == '4'")
    print()
    print("def test_fizzbuzz_multiplo_de_3():")
    print("    assert fizzbuzz(3) == 'Fizz'")
    print("    assert fizzbuzz(6) == 'Fizz'")
    print("    assert fizzbuzz(9) == 'Fizz'")
    print()
    print("def test_fizzbuzz_multiplo_de_5():")
    print("    assert fizzbuzz(5) == 'Buzz'")
    print("    assert fizzbuzz(10) == 'Buzz'")
    print("    assert fizzbuzz(20) == 'Buzz'")
    print()
    print("def test_fizzbuzz_multiplo_de_3_y_5():")
    print("    assert fizzbuzz(15) == 'FizzBuzz'")
    print("    assert fizzbuzz(30) == 'FizzBuzz'")
    print("    assert fizzbuzz(45) == 'FizzBuzz'")
    print("```")
    print()
    print("Progresion TDD:")
    print("  RED: prueba falla (fizzbuzz no existe)")
    print("  GREEN: return str(n) -> pasa test_retorna_numero")
    print("  RED: test multiplo de 3 falla")
    print("  GREEN: agregar if n % 3 == 0")
    print("  RED: test multiplo de 5 falla")
    print("  GREEN: agregar if n % 5 == 0")
    print("  RED: test multiplo de 3 y 5 falla")
    print("  GREEN: ajustar orden (3y5 primero)")
    print("  REFACTOR: mejorar legibilidad")


def ejercicio_2():
    print("=" * 50)
    print(">> EJERCICIO 2: Calculadora de promedios con TDD")
    print("=" * 50)
    print()
    print("Implementa la funcion calcular_promedio(numeros) usando TDD.")
    print()
    print("Requisitos:")
    print("  - Recibe una lista de numeros")
    print("  - Retorna el promedio (suma / cantidad)")
    print("  - Si la lista esta vacia, retorna 0")
    print("  - Si algun elemento no es numero, lanza TypeError")
    print()
    print("PASOS TDD sugeridos:")
    print("  1. prueba_lista_vacia -> espera 0")
    print("  2. prueba_un_numero -> promedio es el mismo numero")
    print("  3. prueba_varios_numeros -> verifica calculo")
    print("  4. prueba_elemento_no_numerico -> espera TypeError")
    print()
    print("PISTA: sum(numeros) / len(numeros), type(valor) == int or float")
    print()
    print("Edita el archivo:")
    print("def calcular_promedio(numeros):")
    print("    # --- TU CODIGO AQUI ---")


def solucion_2():
    print("=" * 50)
    print("SOLUCION 2: Calculadora de promedios con TDD")
    print("=" * 50)
    print()
    print("```python")
    print("def calcular_promedio(numeros):")
    print("    if not numeros:")
    print("        return 0")
    print("    for n in numeros:")
    print("        if not isinstance(n, (int, float)):")
    print("            raise TypeError('Elemento no numerico')")
    print("    return sum(numeros) / len(numeros)")
    print("```")
    print()
    print("Pruebas:")
    print()
    print("```python")
    print("def test_lista_vacia():")
    print("    assert calcular_promedio([]) == 0")
    print()
    print("def test_un_numero():")
    print("    assert calcular_promedio([5]) == 5")
    print()
    print("def test_varios_numeros():")
    print("    assert calcular_promedio([1, 2, 3, 4, 5]) == 3.0")
    print()
    print("def test_elemento_no_numerico():")
    print("    with pytest.raises(TypeError):")
    print("        calcular_promedio([1, 'a', 3])")
    print("```")
    print()
    print("Progresion TDD:")
    print("  RED: test_lista_vacia falla")
    print("  GREEN: return 0")
    print("  RED: test_un_numero falla")
    print("  GREEN: return sum(numeros) / len(numeros)")
    print("  RED: test_lista_vacia falla DE NUEVO (division por cero)")
    print("  GREEN: if not numeros: return 0")
    print("  RED: test_elemento_no_numerico falla")
    print("  GREEN: agregar validacion de tipos")
    print("  REFACTOR: mejora el codigo")


def ejercicio_3():
    print("=" * 50)
    print(">> EJERCICIO 3: Validador de palindromos con TDD")
    print("=" * 50)
    print()
    print("Implementa la funcion es_palindromo(texto) usando TDD.")
    print()
    print("Un palindromo es una palabra o frase que se lee igual")
    print("al derecho y al reves (ignorando espacios, mayusculas")
    print("y signos de puntuacion).")
    print()
    print("Ejemplos: 'reconocer', 'Anita lava la tina', 'Somos'")
    print()
    print("PASOS TDD sugeridos:")
    print("  1. palabra simple: 'reconocer' -> True, 'hola' -> False")
    print("  2. con mayusculas: 'Somos' -> True")
    print("  3. frase con espacios: 'anita lava la tina' -> True")
    print("  4. cadena vacia -> False")
    print()
    print("PISTA: Limpia el texto: lower(), replace(' ', ''), luego compara")
    print("       con texto[::-1]")
    print()
    print("Edita el archivo:")
    print("def es_palindromo(texto):")
    print("    # --- TU CODIGO AQUI ---")


def solucion_3():
    print("=" * 50)
    print("SOLUCION 3: Validador de palindromos con TDD")
    print("=" * 50)
    print()
    print("```python")
    print("def es_palindromo(texto):")
    print("    if not texto:")
    print("        return False")
    print("    limpio = texto.lower().replace(' ', '')")
    print("    return limpio == limpio[::-1]")
    print("```")
    print()
    print("Pruebas:")
    print()
    print("```python")
    print("def test_palabra_simple():")
    print("    assert es_palindromo('reconocer') == True")
    print("    assert es_palindromo('hola') == False")
    print()
    print("def test_con_mayusculas():")
    print("    assert es_palindromo('Somos') == True")
    print()
    print("def test_frase_con_espacios():")
    print("    assert es_palindromo('anita lava la tina') == True")
    print()
    print("def test_cadena_vacia():")
    print("    assert es_palindromo('') == False")
    print("```")
    print()
    print("Progresion TDD:")
    print("  RED: test_palabra_simple falla")
    print("  GREEN: return texto == texto[::-1]")
    print("  RED: test_con_mayusculas falla (Somos != somos)")
    print("  GREEN: texto.lower()")
    print("  RED: test_frase_con_espacios falla")
    print("  GREEN: texto.lower().replace(' ', '')")
    print("  RED: test_cadena_vacia -> '' == '' -> True (queremos False)")
    print("  GREEN: if not texto: return False")
    print("  REFACTOR: codigo limpio y claro")


def menu():
    while True:
        print()
        print("=" * 50)
        print("TDD - EJERCICIOS")
        print("=" * 50)
        print("1. FizzBuzz con TDD")
        print("2. Calculadora de promedios con TDD")
        print("3. Validador de palindromos con TDD")
        print("0. Salir")
        print()

        opcion = input("Selecciona un ejercicio: ")

        if opcion == "1":
            ejercicio_1()
            input("Presiona ENTER para continuar...")
        elif opcion == "2":
            ejercicio_2()
            input("Presiona ENTER para continuar...")
        elif opcion == "3":
            ejercicio_3()
            input("Presiona ENTER para continuar...")
        elif opcion == "0":
            print("Sigue practicando!")
            break
        else:
            print("Opcion invalida")


def main():
    args = sys.argv[1:]

    if not args:
        menu()
        return

    if "-s" in args:
        idx = args.index("-s")
        if idx + 1 < len(args) and args[idx + 1].isdigit():
            num = int(args[idx + 1])
            [solucion_1, solucion_2, solucion_3][num - 1]()
        return

    if args[0].isdigit():
        num = int(args[0])
        [ejercicio_1, ejercicio_2, ejercicio_3][num - 1]()


if __name__ == "__main__":
    main()
