"""
EJERCICIOS - HTTP Status Codes
Ejecuta desde raiz: python scripts/runner.py 5 2 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Clasificar codigos HTTP en familias"""
    codigos = [100, 200, 201, 301, 400, 401, 403, 404, 500, 502, 503]
    for codigo in codigos:
        pass  # Clasifica e imprime: {codigo} -> {familia}
    # ==== ESCRIBE TU RESPUESTA AQUI ====

def ejercicio_2():
    """Elegir status code correcto segun escenario"""
    escenarios = [
        "Usuario crea un recurso nuevo exitosamente",
        "Cliente solicita un recurso que no existe",
        "El servidor tuvo un error interno",
        "Cliente no esta autenticado",
        "Recurso movido permanentemente a otra URL"
    ]
    for escenario in escenarios:
        pass  # Asigna el codigo correcto a cada escenario
    # ==== ESCRIBE TU RESPUESTA AQUI ====

def ejercicio_3():
    """Manejar errores HTTP con if/elif"""
    status_code = 404
    # Usa if/elif para imprimir una accion segun el codigo:
    # 200: Procesar respuesta
    # 201: Recurso creado
    # 301: Redirigir
    # 400: Revisar solicitud
    # 401: Autenticarse
    # 403: Acceso denegado
    # 404: Recurso no encontrado
    # 500: Error del servidor
    # otro: Codigo desconocido
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            print(f">> EJERCICIO {num + 1}: {ejercicios[num].__doc__}")
            print("-" * 40)
            ejercicios[num]()
    else:
        print("EJERCICIOS:")
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
