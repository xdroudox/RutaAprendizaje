import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    print("=" * 50)
    print("EJERCICIO 1: Identificar codigos por escenario")
    print("=" * 50)
    print()
    escenarios = [
        ("Un usuario intenta acceder a /admin sin estar autenticado", ""),
        ("Un recurso solicitado no existe en el servidor", ""),
        ("Una peticion POST crea un nuevo usuario exitosamente", ""),
        ("El servidor sufrio un error interno inesperado", ""),
        ("Un cliente envio JSON con formato incorrecto", ""),
        ("Un recurso fue movido permanentemente a otra URL", ""),
    ]
    for i, (escenario, _) in enumerate(escenarios, 1):
        print(f"{i}. {escenario}")
        print(f"   Codigo: ")
        print()
    print("TAREA: Asigna el codigo HTTP correcto a cada escenario.")
    print()
    print("PISTA: 200, 201, 301, 400, 401, 403, 404, 500")

def ejercicio_2():
    print("=" * 50)
    print("EJERCICIO 2: Consultar codigos en httpbin")
    print("=" * 50)
    print()
    print("TAREA: Usando http.client, realiza peticiones GET a:")
    print("  - https://httpbin.org/status/200")
    print("  - https://httpbin.org/status/301")
    print("  - https://httpbin.org/status/403")
    print("  - https://httpbin.org/status/500")
    print()
    print("Para cada una, imprime el codigo de estado y el mensaje.")
    print()
    print("PISTA: HTTPSConnection, request('GET', '/status/200'), getresponse().status")

def ejercicio_3():
    print("=" * 50)
    print("EJERCICIO 3: Simular manejo de errores")
    print("=" * 50)
    print()
    print("TAREA: Dado el siguiente codigo que simula respuestas,")
    print("completa la funcion manejar_respuesta(codigo) que imprima")
    print("un mensaje adecuado para cada codigo HTTP.")
    print()

    codigos = [200, 201, 204, 301, 400, 401, 403, 404, 500, 503]
    print("Codigos a manejar:", codigos)
    print()
    print("Por ejemplo: 200 -> 'OK: Peticion exitosa'")
    print("            404 -> 'ERROR: Recurso no encontrado'")
    print()
    print("PISTA: Usa un diccionario para mapear codigos a mensajes.")

pistas = {
    "1": "1-401, 2-404, 3-201, 4-500, 5-400, 6-301",
    "2": "for codigo in [200, 301, 403, 500]: conn = http.client.HTTPSConnection('httpbin.org'); conn.request('GET', f'/status/{codigo}'); resp = conn.getresponse(); print(resp.status, resp.reason); conn.close()",
    "3": "mensajes = {200: 'OK', 201: 'Creado', 204: 'Sin contenido', 301: 'Movido permanentemente', 400: 'Mal request', 401: 'No autorizado', 403: 'Prohibido', 404: 'No encontrado', 500: 'Error interno', 503: 'Servicio no disponible'}"
}

def menu():
    print("=" * 50)
    print("HTTP STATUS CODES - EJERCICIOS")
    print("=" * 50)
    print("1 - Identificar codigos por escenario")
    print("2 - Consultar codigos en httpbin")
    print("3 - Simular manejo de errores")
    print()
    print("Usa: python ejercicios.py <numero>")
    print("     python ejercicios.py <numero> -p  (pista)")

def main():
    args = sys.argv[1:]
    if not args:
        menu()
        return
    num = args[0]
    mostrar_pista = "-p" in args
    if mostrar_pista and num in pistas:
        print("=== PISTA ===")
        print(pistas[num])
        print()
    if num == "1":
        ejercicio_1()
    elif num == "2":
        ejercicio_2()
    elif num == "3":
        ejercicio_3()
    else:
        print("Ejercicio no valido. Usa 1, 2 o 3.")

if __name__ == "__main__":
    main()
