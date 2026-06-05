"""
SOLUCIONES - Pruebas Unitarias
Ejecuta desde raiz: python scripts/runner.py 7 1 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Solucion: funcion es_par() con assert"""
    def es_par(n):
        return n % 2 == 0
    assert es_par(2) == True
    assert es_par(0) == True
    assert es_par(3) == False
    assert es_par(-2) == True
    assert es_par(-3) == False
    print("def es_par(n):")
    print("    return n % 2 == 0")
    print()
    print("Pruebas superadas: es_par funciona correctamente.")

def ejercicio_2():
    """Solucion: funcion sumar_lista() con pruebas"""
    def sumar_lista(numeros):
        return sum(numeros)
    assert sumar_lista([]) == 0
    assert sumar_lista([1, 2, 3]) == 6
    assert sumar_lista([-1, 1]) == 0
    assert sumar_lista([5]) == 5
    print("def sumar_lista(numeros):")
    print("    return sum(numeros)")
    print()
    print("Pruebas superadas: sumar_lista funciona correctamente.")

def ejercicio_3():
    """Solucion: funciones test_* con pytest"""
    print("Crea un archivo test_pruebas.py con:")
    print()
    print("import pytest")
    print()
    print("def es_par(n):")
    print("    return n % 2 == 0")
    print()
    print("def sumar_lista(numeros):")
    print("    return sum(numeros)")
    print()
    print("def test_es_par():")
    print("    assert es_par(2) == True")
    print("    assert es_par(3) == False")
    print("    assert es_par(0) == True")
    print()
    print("def test_sumar_lista():")
    print("    assert sumar_lista([]) == 0")
    print("    assert sumar_lista([1, 2, 3]) == 6")
    print()
    print("Ejecuta: pytest test_pruebas.py -v")

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
