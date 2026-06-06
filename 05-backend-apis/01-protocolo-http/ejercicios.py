"""
EJERCICIOS - Protocolo HTTP
Ejecuta desde raiz: python scripts/runner.py 5 1 [ejercicio]

Niveles:
  🟢 Ej 1: Construir URL desde componentes
  🟡 Ej 2: Simular request HTTP como diccionario
  🔴 Ej 3: Parsear response HTTP desde string

Pistas: python scripts/runner.py 5 1 N -p [1|2|3]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1(pista=0):
    """🟢 Construir URL desde componentes"""
    print(">> 🟢 EJERCICIO 1: Construir URL desde componentes")
    print("-" * 50)

    scheme = "https"
    host = "api.ejemplo.com"
    path = "/usuarios"
    params = {"rol": "admin", "edad": "25"}

    print(f"Componentes:")
    print(f"  scheme: {scheme}")
    print(f"  host:   {host}")
    print(f"  path:   {path}")
    print(f"  params: {params}")

    if pista == 1:
        print("\n💡 Pista 1: Una URL se construye como:")
        print("  url = f'{scheme}://{host}{path}?{query}'")
        return
    elif pista == 2:
        print("\n💡 Pista 2: Convierte params a query string:")
        print("  query = '&'.join(f'{k}={v}' for k, v in params.items())")
        return
    elif pista == 3:
        print("\n💡 Pista 3: URL esperada:")
        print("  https://api.ejemplo.com/usuarios?rol=admin&edad=25")
        return

    print("\nConstruye la URL completa a partir de los componentes.")
    print("Resultado esperado: https://api.ejemplo.com/usuarios?rol=admin&edad=25")
    print("\n# ==== ESCRIBE TU CODIGO AQUI ====")


def ejercicio_2(pista=0):
    """🟡 Simular request HTTP como diccionario"""
    print(">> 🟡 EJERCICIO 2: Simular request HTTP")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1: Un request HTTP tiene 4 partes principales:")
        print("  - method: POST")
        print("  - path: /api/usuarios")
        print("  - headers: dict con Content-Type, Authorization, etc.")
        print("  - body: string con JSON")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  headers = {")
        print("      'Content-Type': 'application/json',")
        print("      'Authorization': 'Bearer token123'")
        print("  }")
        print("  body = '{\"nombre\": \"Ana\", \"email\": \"ana@ejemplo.com\"}'")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Diccionario completo:")
        print("  request = {")
        print("      'method': 'POST',")
        print("      'path': '/api/usuarios',")
        print("      'headers': {...},")
        print("      'body': '...'")
        print("  }")
        print("  for k, v in request.items():")
        print("      print(f'{k}: {v}')")
        return

    print("Crea un diccionario que represente un request HTTP.")
    print("Debe incluir:")
    print("  - method: POST")
    print("  - path: /api/usuarios")
    print("  - headers (Content-Type, Authorization)")
    print("  - body (JSON string con nombre y email)")
    print()
    print("Luego imprime cada parte del request.")
    print("\n# ==== ESCRIBE TU CODIGO AQUI ====")


def ejercicio_3(pista=0):
    """🔴 Parsear response HTTP desde string"""
    print(">> 🔴 EJERCICIO 3: Parsear response HTTP")
    print("-" * 50)

    response_str = "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{\"id\": 1, \"nombre\": \"Ana\"}"

    print(f"Response string:")
    print(repr(response_str))

    if pista == 1:
        print("\n💡 Pista 1: Separa linea inicial del resto:")
        print("  linea_inicial, resto = response_str.split('\\r\\n', 1)")
        print("  La linea inicial contiene: version, status_code, mensaje")
        return
    elif pista == 2:
        print("\n💡 Pista 2:")
        print("  partes = linea_inicial.split(' ')")
        print("  version = partes[0]     # HTTP/1.1")
        print("  status_code = int(partes[1])  # 200")
        print("  mensaje = partes[2]     # OK")
        print()
        print("  encabezados, body = resto.split('\\r\\n\\r\\n', 1)")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Parseo de encabezados:")
        print("  headers = {}")
        print("  for linea in encabezados.split('\\r\\n'):")
        print("      if ': ' in linea:")
        print("          k, v = linea.split(': ', 1)")
        print("          headers[k] = v")
        print()
        print("Resultado esperado:")
        print("  Status: 200 OK")
        print("  Headers: {'Content-Type': 'application/json'}")
        print("  Body: {\"id\": 1, \"nombre\": \"Ana\"}")
        return

    print("\nExtrae de este string de respuesta HTTP:")
    print("  1. Status code y mensaje")
    print("  2. Headers (como diccionario)")
    print("  3. Body (como string)")
    print("\n# ==== ESCRIBE TU CODIGO AQUI ====")


if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            pista = 0
            if "-p" in sys.argv:
                idx = sys.argv.index("-p")
                if idx + 1 < len(sys.argv) and sys.argv[idx + 1].isdigit():
                    pista = int(sys.argv[idx + 1])
            ejercicios[num](pista)
    else:
        print("EJERCICIOS:")
        for i, ej in enumerate(ejercicios, 1):
            doc = ej.__doc__ or ""
            print(f"  {i}. {doc}")
