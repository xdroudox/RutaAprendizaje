"""
SOLUCIONES - TDD (Test Driven Development)
Ejecuta: python soluciones.py [numero]

Uso:
  python soluciones.py    -> Menu
  python soluciones.py 1  -> Solucion del ejercicio 1
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print("=" * 50)
    print("SOLUCION 1: FizzBuzz con TDD")
    print("=" * 50)
    print()
    print("Implementacion final:")
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
    print("Pruebas finales:")
    print()
    print("```python")
    print("import pytest")
    print()
    print("def test_fizzbuzz_retorna_numero():")
    print("    assert fizzbuzz(1) == '1'")
    print("    assert fizzbuzz(2) == '2'")
    print("    assert fizzbuzz(4) == '4'")
    print()
    print("def test_fizzbuzz_multiplo_de_3():")
    print("    assert fizzbuzz(3) == 'Fizz'")
    print("    assert fizzbuzz(6) == 'Fizz'")
    print("    assert fizzbuzz(99) == 'Fizz'")
    print()
    print("def test_fizzbuzz_multiplo_de_5():")
    print("    assert fizzbuzz(5) == 'Buzz'")
    print("    assert fizzbuzz(10) == 'Buzz'")
    print("    assert fizzbuzz(100) == 'Buzz'")
    print()
    print("def test_fizzbuzz_multiplo_de_3_y_5():")
    print("    assert fizzbuzz(15) == 'FizzBuzz'")
    print("    assert fizzbuzz(30) == 'FizzBuzz'")
    print("    assert fizzbuzz(150) == 'FizzBuzz'")
    print("```")
    print()
    print("Ciclo TDD completo:")
    print()
    print("  == RED ==    Prueba test_retorna_numero falla (no existe)")
    print("  == GREEN ==  def fizzbuzz(n): return str(n)")
    print("  == RED ==    test_multiplo_de_3 falla (3->'Fizz', obtenemos '3')")
    print("  == GREEN ==  Agregar if n % 3 == 0: return 'Fizz'")
    print("  == RED ==    test_multiplo_de_5 falla")
    print("  == GREEN ==  Agregar if n % 5 == 0: return 'Buzz'")
    print("  == RED ==    test_multiplo_de_3_y_5 falla (15->'FizzBuzz', obtenemos 'Fizz')")
    print("  == GREEN ==  Poner condicion 3y5 primero")
    print("  == REFACTOR == Codigo limpio y listo")


def solucion_2():
    print("=" * 50)
    print("SOLUCION 2: Calculadora de promedios con TDD")
    print("=" * 50)
    print()
    print("Implementacion final:")
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
    print("Pruebas finales:")
    print()
    print("```python")
    print("import pytest")
    print()
    print("def test_lista_vacia():")
    print("    assert calcular_promedio([]) == 0")
    print()
    print("def test_un_numero():")
    print("    assert calcular_promedio([5]) == 5")
    print()
    print("def test_varios_numeros():")
    print("    resultado = calcular_promedio([1, 2, 3, 4, 5])")
    print("    assert resultado == 3.0")
    print()
    print("def test_elemento_no_numerico():")
    print("    with pytest.raises(TypeError):")
    print("        calcular_promedio([1, 'a', 3])")
    print("```")
    print()
    print("Ciclo TDD completo:")
    print()
    print("  RED:   test_lista_vacia falla (funcion no existe)")
    print("  GREEN: def calcular_promedio(numeros): return 0")
    print("  RED:   test_un_numero falla (5->0, esperado 5)")
    print("  GREEN: return sum(numeros) / len(numeros)")
    print("  RED:   test_lista_vacia falla (division por cero)")
    print("  GREEN: if not numeros: return 0")
    print("  RED:   test_elemento_no_numerico falla")
    print("  GREEN: agregar validacion isinstance")
    print("  REFACTOR: codigo limpio")


def solucion_3():
    print("=" * 50)
    print("SOLUCION 3: Validador de palindromos con TDD")
    print("=" * 50)
    print()
    print("Implementacion final:")
    print()
    print("```python")
    print("def es_palindromo(texto):")
    print("    if not texto:")
    print("        return False")
    print("    limpio = texto.lower().replace(' ', '')")
    print("    return limpio == limpio[::-1]")
    print("```")
    print()
    print("Pruebas finales:")
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
    print("Ciclo TDD:")
    print()
    print("  RED:   test_palabra_simple falla")
    print("  GREEN: return texto == texto[::-1]")
    print("  RED:   test_con_mayusculas falla")
    print("  GREEN: texto.lower()")
    print("  RED:   test_frase_con_espacios falla")
    print("  GREEN: texto.lower().replace(' ', '')")
    print("  RED:   test_cadena_vacia (''=='' -> True, esperamos False)")
    print("  GREEN: if not texto: return False")
    print("  REFACTOR: codigo limpio")
    print()
    print("Extension posible: eliminar signos de puntuacion")
    print("ej: 'A mama, Roma le aviva el amor a papa' es palindromo")


def menu():
    while True:
        print()
        print("=" * 50)
        print("SOLUCIONES - TDD")
        print("=" * 50)
        print("1. FizzBuzz con TDD")
        print("2. Calculadora de promedios con TDD")
        print("3. Validador de palindromos con TDD")
        print("0. Salir")
        print()

        opcion = input("Ver solucion: ")

        soluciones = {"1": solucion_1, "2": solucion_2, "3": solucion_3}

        if opcion in soluciones:
            soluciones[opcion]()
            input("Presiona ENTER para continuar...")
        elif opcion == "0":
            print("Sigue asi!")
            break
        else:
            print("Opcion invalida")


def main():
    args = sys.argv[1:]
    if args and args[0].isdigit():
        [solucion_1, solucion_2, solucion_3][int(args[0]) - 1]()
    else:
        menu()


if __name__ == "__main__":
    main()
