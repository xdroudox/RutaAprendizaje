"""
SOLUCIONES - Pruebas Unitarias
Ejecuta: python soluciones.py [numero]

Uso:
  python soluciones.py    -> Menu
  python soluciones.py 1  -> Solucion del ejercicio 1
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        return a / b


def solucion_1():
    print("=" * 50)
    print("SOLUCION 1: Pruebas basicas con assert")
    print("=" * 50)
    print()
    print("Pruebas unitarias usando solo assert de Python:")
    print()
    print("```python")
    print("calc = Calculadora()")
    print()
    print("def test_sumar():")
    print("    assert calc.sumar(2, 3) == 5")
    print()
    print("def test_restar():")
    print("    assert calc.restar(10, 4) == 6")
    print()
    print("def test_multiplicar():")
    print("    assert calc.multiplicar(3, 4) == 12")
    print()
    print("def test_dividir():")
    print("    assert calc.dividir(10, 2) == 5.0")
    print()
    print("test_sumar()")
    print("test_restar()")
    print("test_multiplicar()")
    print("test_dividir()")
    print("print('Todas las pruebas pasaron')")
    print("```")
    print()
    print("Salida esperada:")
    print("  Todas las pruebas pasaron")
    print()
    print("Nota: Si una asercion falla, se lanza AssertionError")
    print("y el programa se detiene. Por eso pytest es mejor:"),
    print("ejecuta todas las pruebas y reporta cuales fallaron.")


def solucion_2():
    print("=" * 50)
    print("SOLUCION 2: Fixtures con pytest")
    print("=" * 50)
    print()
    print("Fixture y pruebas con pytest:")
    print()
    print("```python")
    print("import pytest")
    print()
    print("@pytest.fixture")
    print("def calculadora():")
    print("    return Calculadora()")
    print()
    print("def test_suma_con_fixture(calculadora):")
    print("    assert calculadora.sumar(5, 7) == 12")
    print()
    print("def test_resta_con_fixture(calculadora):")
    print("    assert calculadora.restar(20, 8) == 12")
    print()
    print("def test_multiplicacion_con_fixture(calculadora):")
    print("    assert calculadora.multiplicar(6, 7) == 42")
    print("```")
    print()
    print("Scope de fixtures:")
    print("  - function (default): se ejecuta antes de cada prueba")
    print("  - class: una vez por clase")
    print("  - module: una vez por modulo")
    print("  - session: una vez por sesion de pytest")
    print()
    print("@pytest.fixture(scope='module')")
    print("def calculadora():")
    print("    return Calculadora()")


def solucion_3():
    print("=" * 50)
    print("SOLUCION 3: Probar excepciones")
    print("=" * 50)
    print()
    print("Pruebas de excepciones con pytest.raises:")
    print()
    print("```python")
    print("import pytest")
    print()
    print("def test_division_por_cero():")
    print("    calc = Calculadora()")
    print("    with pytest.raises(ZeroDivisionError):")
    print("        calc.dividir(10, 0)")
    print()
    print("def test_mensaje_error():")
    print("    calc = Calculadora()")
    print("    with pytest.raises(ZeroDivisionError, match='No se puede dividir por cero'):")
    print("        calc.dividir(10, 0)")
    print("```")
    print()
    print("Otra forma: capturar la excepcion para inspeccionarla:")
    print()
    print("```python")
    print("def test_excepcion_capturada():")
    print("    calc = Calculadora()")
    print("    with pytest.raises(ZeroDivisionError) as exc_info:")
    print("        calc.dividir(10, 0)")
    print("    assert str(exc_info.value) == 'No se puede dividir por cero'")
    print("```")


def menu():
    while True:
        print()
        print("=" * 50)
        print("SOLUCIONES - Pruebas Unitarias")
        print("=" * 50)
        print("1. Pruebas basicas con assert")
        print("2. Fixtures con pytest")
        print("3. Probar excepciones")
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
