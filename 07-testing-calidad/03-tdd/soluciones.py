"""
SOLUCIONES - TDD (Test Driven Development)
Ejecuta desde raiz: python scripts/runner.py 7 3 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Solucion: FizzBuzz con TDD"""
    def fizzbuzz(n):
        if n % 3 == 0 and n % 5 == 0:
            return 'FizzBuzz'
        if n % 3 == 0:
            return 'Fizz'
        if n % 5 == 0:
            return 'Buzz'
        return str(n)
    assert fizzbuzz(1) == '1'
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(15) == 'FizzBuzz'
    print("def fizzbuzz(n):")
    print("    if n % 3 == 0 and n % 5 == 0:")
    print("        return 'FizzBuzz'")
    print("    if n % 3 == 0:")
    print("        return 'Fizz'")
    print("    if n % 5 == 0:")
    print("        return 'Buzz'")
    print("    return str(n)")
    print()
    print("Todas las pruebas FizzBuzz pasaron.")

def ejercicio_2():
    """Solucion: validador de email con TDD"""
    def validar_email(email):
        if ' ' in email:
            return False
        if email.count('@') != 1:
            return False
        local, dominio = email.split('@')
        if not local or not dominio:
            return False
        if '.' not in dominio:
            return False
        return True
    assert validar_email('user@example.com') == True
    assert validar_email('sinarroba') == False
    assert validar_email('user@') == False
    assert validar_email('@dominio.com') == False
    assert validar_email('user con@espacio.com') == False
    print("def validar_email(email): ...")
    print("Todas las pruebas de validacion de email pasaron.")

def ejercicio_3():
    """Solucion: calculadora de promedios con TDD"""
    def calcular_promedio(numeros):
        if not numeros:
            return 0
        for n in numeros:
            if not isinstance(n, (int, float)):
                raise TypeError('Elemento no numerico')
        return sum(numeros) / len(numeros)
    assert calcular_promedio([]) == 0
    assert calcular_promedio([1, 2, 3]) == 2.0
    assert calcular_promedio([5]) == 5.0
    try:
        calcular_promedio([1, 'a'])
        assert False, "Debio lanzar TypeError"
    except TypeError:
        pass
    print("def calcular_promedio(numeros): ...")
    print("Todas las pruebas de promedio pasaron.")

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            print(f">> EJERCICIO {num + 1}: {ejercicios[num].__doc__}")
            print("-" * 40)
            ejercicios[num]()
    else:
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
