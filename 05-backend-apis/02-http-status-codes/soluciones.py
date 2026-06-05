"""
SOLUCIONES - HTTP Status Codes
Ejecuta desde raiz: python scripts/runner.py 5 2 1 -s
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Clasificar codigos HTTP en familias"""
    codigos = [100, 200, 201, 301, 400, 401, 403, 404, 500, 502, 503]
    for codigo in codigos:
        if codigo < 200:
            familia = "1xx Informativo"
        elif codigo < 300:
            familia = "2xx Exito"
        elif codigo < 400:
            familia = "3xx Redireccion"
        elif codigo < 500:
            familia = "4xx Error Cliente"
        else:
            familia = "5xx Error Servidor"
        print(f"  {codigo} -> {familia}")

def ejercicio_2():
    """Elegir status code correcto segun escenario"""
    escenarios = [
        ("Usuario crea un recurso nuevo exitosamente", 201),
        ("Cliente solicita un recurso que no existe", 404),
        ("El servidor tuvo un error interno", 500),
        ("Cliente no esta autenticado", 401),
        ("Recurso movido permanentemente a otra URL", 301),
    ]
    for escenario, codigo in escenarios:
        print(f"  [{codigo}] {escenario}")

def ejercicio_3():
    """Manejar errores HTTP con if/elif"""
    status_code = 404
    if status_code == 200:
        print("Procesando respuesta exitosa...")
    elif status_code == 201:
        print("Recurso creado exitosamente.")
    elif status_code == 301:
        print("Redirigiendo a la nueva URL...")
    elif status_code == 400:
        print("Error en la solicitud. Revisa los parametros.")
    elif status_code == 401:
        print("Autenticacion requerida. Inicia sesion.")
    elif status_code == 403:
        print("Acceso denegado. No tienes permisos.")
    elif status_code == 404:
        print("Recurso no encontrado. Verifica la URL.")
    elif status_code == 500:
        print("Error interno del servidor. Intenta mas tarde.")
    else:
        print(f"Codigo desconocido: {status_code}")

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            print(f">> SOLUCION {num + 1}: {ejercicios[num].__doc__}")
            print("-" * 40)
            ejercicios[num]()
    else:
        print("SOLUCIONES:")
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
