"""
EJERCICIOS - TDD (Test Driven Development)
Ejecuta desde raiz: python scripts/runner.py 7 3 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """FizzBuzz con TDD (escribir test primero)"""
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

def ejercicio_2():
    """Validador de email con TDD"""
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

def ejercicio_3():
    """Calculadora de promedios con TDD"""
    print("Implementa calcular_promedio(numeros) con TDD.")
    print("Requisitos:")
    print("- Lista vacia retorna 0")
    print("- Calcula el promedio correctamente")
    print("- Elemento no numerico lanza TypeError")
    print()
    print("def calcular_promedio(numeros):")
    print("    # ==== ESCRIBE TU RESPUESTA AQUI ====")
    print("    pass")

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
