"""
SOLUCIONES - TDD (Test Driven Development)
Ejecuta desde raiz: python scripts/runner.py 7 3 [ejercicio] -s
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    """FizzBuzz con TDD (escribir test primero)"""
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
    print(">> SOLUCION 1: FizzBuzz con TDD")
    print("-" * 40)
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

def solucion_2():
    """Validador de email con TDD"""
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
    print(">> SOLUCION 2: Validador de email con TDD")
    print("-" * 40)
    print("def validar_email(email):")
    print("    if ' ' in email: return False")
    print("    if email.count('@') != 1: return False")
    print("    local, dominio = email.split('@')")
    print("    if not local or not dominio: return False")
    print("    if '.' not in dominio: return False")
    print("    return True")
    print()
    print("Todas las pruebas de validacion de email pasaron.")

def solucion_3():
    """Calculadora de promedios con TDD"""
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
    print(">> SOLUCION 3: Calculadora de promedios con TDD")
    print("-" * 40)
    print("def calcular_promedio(numeros):")
    print("    if not numeros: return 0")
    print("    for n in numeros:")
    print("        if not isinstance(n, (int, float)):")
    print("            raise TypeError('Elemento no numerico')")
    print("    return sum(numeros) / len(numeros)")
    print()
    print("Todas las pruebas de promedio pasaron.")

if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
    else:
        for i, sol in enumerate(soluciones, 1):
            print(f"  {i}. {sol.__doc__}")
