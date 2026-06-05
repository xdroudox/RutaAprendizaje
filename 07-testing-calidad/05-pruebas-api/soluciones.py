"""
SOLUCIONES - Pruebas de API
Ejecuta: python soluciones.py [numero]

Uso:
  python soluciones.py    -> Menu
  python soluciones.py 1  -> Solucion del ejercicio 1
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


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
    print("Ejecucion con comprobacion:")
    import requests
    url = "https://httpbin.org/get"
    response = requests.get(url)
    assert response.status_code == 200
    datos = response.json()
    assert "url" in datos
    assert datos["url"] == url
    assert "Content-Type" in response.headers
    print("  Status:", response.status_code)
    print("  URL:", datos["url"])
    print("  Content-Type:", response.headers["Content-Type"])
    print()
    print("Otros endpoints utiles de httpbin.org:")
    print("  - /ip          -> Devuelve tu IP")
    print("  - /headers     -> Devuelve tus cabeceras")
    print("  - /status/404  -> Devuelve 404")
    print("  - /delay/3     -> Respuesta con 3s de retardo")


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
    url = "https://httpbin.org/post"
    payload = {"nombre": "Ana", "edad": 25}
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    datos = response.json()
    assert datos["json"] == payload
    assert datos["json"]["nombre"] == "Ana"
    print("  Status:", response.status_code)
    print("  Datos recibidos:", datos["json"])
    print()
    print("requests.post(url, json=...) vs data=...:")
    print("  json: Envia Content-Type: application/json")
    print("  data: Envia Content-Type: application/x-www-form-urlencoded")


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
    print("    assert response.status_code == 200")
    print("    datos = response.json()")
    print("    assert 'uuid' in datos")
    print("    uuid = datos['uuid']")
    print("    assert isinstance(uuid, str)")
    print("    assert len(uuid) == 36")
    print()
    print("def test_anything_endpoint():")
    print("    url = 'https://httpbin.org/anything'")
    print("    response = requests.get(url)")
    print("    assert response.status_code == 200")
    print("    datos = response.json()")
    print("    assert datos['method'] == 'GET'")
    print("    assert 'headers' in datos")
    print("```")
    print()
    print("Ejecucion:")
    import requests

    print("  Probando /uuid...")
    response = requests.get("https://httpbin.org/uuid")
    assert response.status_code == 200
    datos = response.json()
    assert "uuid" in datos
    uuid = datos["uuid"]
    assert isinstance(uuid, str)
    assert len(uuid) == 36
    print("    UUID:", uuid)
    print("    Tipo: string, Longitud: 36 caracteres")

    print("  Probando /anything...")
    response2 = requests.get("https://httpbin.org/anything")
    assert response2.status_code == 200
    datos2 = response2.json()
    assert datos2["method"] == "GET"
    assert "headers" in datos2
    print("    Method:", datos2["method"])
    print("    Headers presentes:", len(datos2["headers"]), "cabeceras")
    print()
    print("Validacion avanzada con esquemas:")
    print("  Para APIs complejas, usa librerias como:")
    print("  - jsonschema: valida contra un esquema JSON")
    print("  - pydantic: define modelos con validacion")
    print("  - marshmallow: deserializacion y validacion")


def menu():
    while True:
        print()
        print("=" * 50)
        print("SOLUCIONES - Pruebas de API")
        print("=" * 50)
        print("1. Probar GET a httpbin.org")
        print("2. Probar POST con datos")
        print("3. Validar estructura de respuesta JSON")
        print("0. Salir")
        print()

        opcion = input("Ver solucion: ")

        soluciones = {"1": solucion_1, "2": solucion_2, "3": solucion_3}

        if opcion in soluciones:
            soluciones[opcion]()
            input("Presiona ENTER para continuar...")
        elif opcion == "0":
            print("Sigue asi!")
            break
        else:
            print("Opcion invalida")


def main():
    args = sys.argv[1:]
    if args and args[0].isdigit():
        [solucion_1, solucion_2, solucion_3][int(args[0]) - 1]()
    else:
        menu()


if __name__ == "__main__":
    main()
