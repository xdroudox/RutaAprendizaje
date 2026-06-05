"""
EJERCICIOS - Pruebas Unitarias
Ejecuta desde raiz: python scripts/runner.py 7 1 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Escribir funcion es_par() y probarla con assert"""
    print("Escribe una funcion es_par(n) que retorne True si n es par.")
    print("Luego pruebala con assert para varios casos (0, 2, 3, -1, etc.).")
    print()
    print("def es_par(n):")
    print("    # ==== ESCRIBE TU RESPUESTA AQUI ====")
    print("    pass")
    print()
    print("# Pruebas:")
    print("# assert es_par(2) == True")
    print("# assert es_par(3) == False")

def ejercicio_2():
    """Escribir test para funcion que suma lista"""
    print("Escribe una funcion sumar_lista(numeros) que sume los elementos")
    print("de una lista. Luego escribe pruebas con assert que verifiquen:")
    print("- Lista vacia retorna 0")
    print("- [1,2,3] retorna 6")
    print("- [-1,1] retorna 0")
    print()
    print("def sumar_lista(numeros):")
    print("    # ==== ESCRIBE TU RESPUESTA AQUI ====")
    print("    pass")

def ejercicio_3():
    """Usar pytest (funcion test_...)"""
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
