"""
EJERCICIOS - Pruebas Unitarias
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


def ejercicio_1():
    print("=" * 50)
    print(">> EJERCICIO 1: Pruebas basicas con assert")
    print("=" * 50)
    print()
    print("Dada la clase Calculadora, escribe pruebas unitarias")
    print("usando la sentencia assert de Python.")
    print()
    print("Crea las siguientes pruebas:")
    print("  - test_sumar: verifica que 2 + 3 = 5")
    print("  - test_restar: verifica que 10 - 4 = 6")
    print("  - test_multiplicar: verifica que 3 * 4 = 12")
    print("  - test_dividir: verifica que 10 / 2 = 5.0")
    print()
    print("PISTA: Crea una instancia de Calculadora y usa assert")
    print()
    print("Edita el archivo:")
    print("calc = Calculadora()")
    print("# --- TU CODIGO AQUI ---")


def solucion_1():
    print("=" * 50)
    print("SOLUCION 1: Pruebas basicas con assert")
    print("=" * 50)
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
    print("# Ejecutar pruebas")
    print("test_sumar()")
    print("test_restar()")
    print("test_multiplicar()")
    print("test_dividir()")
    print("print('Todas las pruebas pasaron')")
    print("```")
    print()
    print("Para usar con pytest, guarda en un archivo test_calculadora.py")
    print("y ejecuta: pytest test_calculadora.py")


def ejercicio_2():
    print("=" * 50)
    print(">> EJERCICIO 2: Fixtures con pytest")
    print("=" * 50)
    print()
    print("Usando pytest, crea un fixture llamado 'calculadora'")
    print("que retorne una instancia de Calculadora.")
    print()
    print("Luego escribe pruebas que usen el fixture:")
    print("  - test_suma_con_fixture(calculadora)")
    print("  - test_resta_con_fixture(calculadora)")
    print("  - test_multiplicacion_con_fixture(calculadora)")
    print()
    print("PISTA: Usa @pytest.fixture y pasa el parametro a la funcion")
    print()
    print("Edita el archivo:")
    print("import pytest")
    print()
    print("@pytest.fixture")
    print("def calculadora():")
    print("    # --- TU CODIGO AQUI ---")


def solucion_2():
    print("=" * 50)
    print("SOLUCION 2: Fixtures con pytest")
    print("=" * 50)
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
    print("Beneficios del fixture:")
    print("- No repites la creacion de Calculadora()")
    print("- Si cambia el constructor, solo actualizas el fixture")
    print("- Puedes agregar logica de setup/teardown")
    print()
    print("Ejecutar: pytest -v test_calculadora.py")


def ejercicio_3():
    print("=" * 50)
    print(">> EJERCICIO 3: Probar excepciones")
    print("=" * 50)
    print()
    print("Escribe una prueba que verifique que dividir por cero")
    print("lanza la excepcion ZeroDivisionError.")
    print()
    print("Usa pytest.raises para capturar la excepcion:")
    print()
    print("  def test_division_por_cero():")
    print("      with pytest.raises(ZeroDivisionError):")
    print("          calc.dividir(10, 0)")
    print()
    print("Luego escribe una prueba adicional que verifique que")
    print("el mensaje de error contenga 'No se puede dividir por cero'")
    print()
    print("PISTA: pytest.raises(ZeroDivisionError, match='...')")
    print()
    print("Edita el archivo:")
    print("def test_division_por_cero():")
    print("    # --- TU CODIGO AQUI ---")


def solucion_3():
    print("=" * 50)
    print("SOLUCION 3: Probar excepciones")
    print("=" * 50)
    print()
    print("```python")
    print("import pytest")
    print()
    print("def test_division_por_cero():")
    print("    calc = Calculadora()")
    print("    with pytest.raises(ZeroDivisionError):")
    print("        calc.dividir(10, 0)")
    print()
    print("def test_mensaje_error_division_por_cero():")
    print("    calc = Calculadora()")
    print("    with pytest.raises(ZeroDivisionError, match='No se puede dividir por cero'):")
    print("        calc.dividir(10, 0)")
    print("```")
    print()
    print("Explicacion:")
    print("- pytest.raises captura la excepcion esperada")
    print("- Si la excepcion no ocurre, la prueba falla")
    print("- El parametro match verifica el mensaje con regex")


def menu():
    while True:
        print()
        print("=" * 50)
        print("PRUEBAS UNITARIAS - EJERCICIOS")
        print("=" * 50)
        print("1. Pruebas basicas con assert")
        print("2. Fixtures con pytest")
        print("3. Probar excepciones")
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
