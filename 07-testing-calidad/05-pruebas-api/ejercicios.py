"""
EJERCICIOS - Pruebas de API
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


def ejercicio_1():
    print("=" * 50)
    print(">> EJERCICIO 1: Probar GET a httpbin.org")
    print("=" * 50)
    print()
    print("Escribe una funcion test_obtener_datos() que:")
    print("  1. Haga una peticion GET a https://httpbin.org/get")
    print("  2. Verifique que el codigo de estado sea 200")
    print("  3. Verifique que la respuesta tenga el campo 'url'")
    print("  4. Verifique que 'url' sea 'https://httpbin.org/get'")
    print("  5. Verifique que la cabecera Content-Type exista")
    print()
    print("PISTA: response = requests.get(url); response.status_code; response.json()")
    print()
    print("Edita el archivo:")
    print("import requests")
    print()
    print("def test_obtener_datos():")
    print("    # --- TU CODIGO AQUI ---")


def solucion_1():
    print("=" * 50)
    print("SOLUCION 1: Probar GET a httpbin.org")
    print("=" * 50)
    print()
    print("```python")
    print("import requests")
    print()
    print("def test_obtener_datos():")
    print("    url = 'https://httpbin.org/get'")
    print("    response = requests.get(url)")
    print()
    print("    assert response.status_code == 200")
    print("    datos = response.json()")
    print("    assert 'url' in datos")
    print("    assert datos['url'] == url")
    print("    assert 'Content-Type' in response.headers")
    print("    print('GET exitoso:', datos['url'])")
    print("```")
    print()
    print("Ejecucion:")
    import requests
    url = "https://httpbin.org/get"
    response = requests.get(url)
    assert response.status_code == 200
    datos = response.json()
    assert "url" in datos
    assert datos["url"] == url
    assert "Content-Type" in response.headers
    print("  GET exitoso:", datos["url"])
    print("  Content-Type:", response.headers["Content-Type"])


def ejercicio_2():
    print("=" * 50)
    print(">> EJERCICIO 2: Probar POST con datos")
    print("=" * 50)
    print()
    print("Escribe una funcion test_enviar_datos() que:")
    print("  1. Haga una peticion POST a https://httpbin.org/post")
    print("  2. Envie datos JSON: {\"nombre\": \"Ana\", \"edad\": 25}")
    print("  3. Verifique codigo de estado 200")
    print("  4. Verifique que el servidor devuelva los datos enviados")
    print("     (deben estar en datos['json'])")
    print("  5. Verifique que 'nombre' en la respuesta sea 'Ana'")
    print()
    print("PISTA: requests.post(url, json=datos)")
    print()
    print("Edita el archivo:")
    print("def test_enviar_datos():")
    print("    # --- TU CODIGO AQUI ---")


def solucion_2():
    print("=" * 50)
    print("SOLUCION 2: Probar POST con datos")
    print("=" * 50)
    print()
    print("```python")
    print("import requests")
    print()
    print("def test_enviar_datos():")
    print("    url = 'https://httpbin.org/post'")
    print("    payload = {'nombre': 'Ana', 'edad': 25}")
    print("    response = requests.post(url, json=payload)")
    print()
    print("    assert response.status_code == 200")
    print("    datos = response.json()")
    print("    assert datos['json'] == payload")
    print("    assert datos['json']['nombre'] == 'Ana'")
    print("    print('POST exitoso:', datos['json'])")
    print("```")
    print()
    print("Ejecucion:")
    import requests
    url = "https://httpbin.org/post"
    payload = {"nombre": "Ana", "edad": 25}
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    datos = response.json()
    assert datos["json"] == payload
    assert datos["json"]["nombre"] == "Ana"
    print("  POST exitoso:", datos["json"])
    print()
    print("Tambien se puede enviar con data= en lugar de json=")
    print("  data envia como form (application/x-www-form-urlencoded)")
    print("  json envia como JSON (application/json)")


def ejercicio_3():
    print("=" * 50)
    print(">> EJERCICIO 3: Validar estructura de respuesta JSON")
    print("=" * 50)
    print()
    print("Escribe una funcion test_validar_estructura() que:")
    print("  1. Haga GET a https://httpbin.org/uuid")
    print("  2. Verifique codigo de estado 200")
    print("  3. Verifique que exista el campo 'uuid'")
    print("  4. Verifique que el uuid sea un string de 36 caracteres")
    print("     (formato tipico: 550e8400-e29b-41d4-a716-446655440000)")
    print()
    print("Luego escribe otra prueba que:")
    print("  1. Haga GET a https://httpbin.org/anything")
    print("  2. Verifique que la respuesta contenga 'method': 'GET'")
    print("  3. Verifique que el campo 'headers' exista")
    print()
    print("PISTA: len(uuid_string) == 36; datos['uuid']; datos['method']")
    print()
    print("Edita el archivo:")
    print("def test_validar_uuid():")
    print("    # --- TU CODIGO AQUI ---")
    print()
    print("def test_anything_endpoint():")
    print("    # --- TU CODIGO AQUI ---")


def solucion_3():
    print("=" * 50)
    print("SOLUCION 3: Validar estructura de respuesta JSON")
    print("=" * 50)
    print()
    print("```python")
    print("import requests")
    print()
    print("def test_validar_uuid():")
    print("    url = 'https://httpbin.org/uuid'")
    print("    response = requests.get(url)")
    print()
    print("    assert response.status_code == 200")
    print("    datos = response.json()")
    print("    assert 'uuid' in datos")
    print("    uuid = datos['uuid']")
    print("    assert isinstance(uuid, str)")
    print("    assert len(uuid) == 36")
    print("    print('UUID valido:', uuid)")
    print()
    print("def test_anything_endpoint():")
    print("    url = 'https://httpbin.org/anything'")
    print("    response = requests.get(url)")
    print()
    print("    assert response.status_code == 200")
    print("    datos = response.json()")
    print("    assert 'method' in datos")
    print("    assert datos['method'] == 'GET'")
    print("    assert 'headers' in datos")
    print("    print('Anything endpoint OK')")
    print("```")
    print()
    print("Ejecucion:")
    import requests
    url = "https://httpbin.org/uuid"
    response = requests.get(url)
    assert response.status_code == 200
    datos = response.json()
    assert "uuid" in datos
    uuid = datos["uuid"]
    assert isinstance(uuid, str)
    assert len(uuid) == 36
    print("  UUID valido:", uuid)

    url2 = "https://httpbin.org/anything"
    response2 = requests.get(url2)
    assert response2.status_code == 200
    datos2 = response2.json()
    assert datos2["method"] == "GET"
    assert "headers" in datos2
    print("  Anything endpoint OK")
    print()
    print("Validaciones comunes en APIs:")
    print("  - Tipo de datos (str, int, list, dict)")
    print("  - Campos requeridos presentes")
    print("  - Longitud de strings")
    print("  - Rangos de numeros")
    print("  - Formato de fechas")
    print("  - Estructura anidada")


def menu():
    while True:
        print()
        print("=" * 50)
        print("PRUEBAS DE API - EJERCICIOS")
        print("=" * 50)
        print("1. Probar GET a httpbin.org")
        print("2. Probar POST con datos")
        print("3. Validar estructura de respuesta JSON")
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
