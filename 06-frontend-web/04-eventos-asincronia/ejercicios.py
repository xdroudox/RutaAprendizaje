"""
EJERCICIOS - Eventos y Asincronia
Ejecuta desde raiz: python scripts/runner.py 6 4 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Eventos de raton: click, mouseenter, mouseleave"""
    print(">> EJERCICIO 1: Eventos de raton")
    print("-" * 40)
    print("Este ejercicio es en HTML/JS.")
    print("Abre el archivo en tu navegador:")
    print("  06-frontend-web/04-eventos-asincronia/ejercicios.html")
    print()
    print("Agrega event listeners a la caja roja:")
    print("  - click: cambiar color a azul y texto 'Click!'")
    print("  - mouseenter: escala 1.2 y texto 'Hover!'")
    print("  - mouseleave: restaurar original y texto 'Fuera!'")

def ejercicio_2():
    """setTimeout y setInterval para cuenta regresiva"""
    print(">> EJERCICIO 2: setTimeout y setInterval para cuenta regresiva")
    print("-" * 40)
    print("Abre: 06-frontend-web/04-eventos-asincronia/ejercicios.html")
    print()
    print("Implementa una cuenta regresiva del 5 al 1:")
    print("  - setInterval cada 1 segundo")
    print("  - clearInterval al llegar a 0")
    print("  - Muestra 'Despegue!' al finalizar")

def ejercicio_3():
    """Promesa simple con async/await"""
    print(">> EJERCICIO 3: Promesa simple con async/await")
    print("-" * 40)
    print("Abre: 06-frontend-web/04-eventos-asincronia/ejercicios.html")
    print()
    print("Simula una operacion asincrona:")
    print("  - Crea una Promise con setTimeout de 2s")
    print("  - Usa async/await con try/catch")
    print("  - Muestra 'Cargando...' -> 'Operacion completada!'")

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            ejercicios[num]()
    else:
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
