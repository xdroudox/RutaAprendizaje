"""
EJERCICIOS - JWT y Autenticacion
Ejecuta desde raiz: python scripts/runner.py 5 5 [ejercicio]

Niveles:
  🟢 Ej 1: Crear JWT simple (header.payload.firma)
  🟡 Ej 2: Decodificar JWT y extraer payload
  🔴 Ej 3: Verificar expiracion de JWT

Pistas: python scripts/runner.py 5 5 N -p [1|2|3]
"""

import sys
import base64
import json

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def b64_encode(data):
    return base64.urlsafe_b64encode(json.dumps(data).encode()).rstrip(b"=").decode()


def b64_decode(data):
    padding = 4 - len(data) % 4
    if padding != 4:
        data += "=" * padding
    return json.loads(base64.urlsafe_b64decode(data).decode())


def ejercicio_1(pista=0):
    """🟢 Crear JWT simple (header.payload.firma)"""
    print(">> 🟢 EJERCICIO 1: Crear JWT simple")
    print("-" * 50)

    header = {"alg": "HS256", "typ": "JWT"}
    payload = {"sub": "123", "name": "Ana", "iat": 1700000000}

    print(f"Header:  {header}")
    print(f"Payload: {payload}")
    print()
    print("Formato: base64(header).base64(payload).base64(firma)")

    if pista == 1:
        print("\n💡 Pista 1: Codifica header y payload a Base64 URL-safe:")
        print("  header_b64 = base64.urlsafe_b64encode(json.dumps(header).encode())")
        print("  header_b64 = header_b64.rstrip(b'=').decode()")
        return
    elif pista == 2:
        print("\n💡 Pista 2: Funcion auxiliar:")
        print("  def b64_encode(data):")
        print("      return base64.urlsafe_b64encode(")
        print("          json.dumps(data).encode()).rstrip(b'=').decode()")
        print()
        print("  token = f'{b64_encode(header)}.{b64_encode(payload)}.{firma_b64}'")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Token JWT esperado:")
        print("  eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9")
        print("  .eyJzdWIiOiAiMTIzIiwgIm5hbWUiOiAiQW5hIiwgImlhdCI6IDE3MDAwMDAwMDB9")
        print("  .<firma_en_base64>")
        return

    print("\nConvierte header y payload a Base64 URL-safe y construye el token.")
    print("Usa 'firma_simple' como firma (tambien en Base64).")
    print("\n# ==== ESCRIBE TU CODIGO AQUI ====")


def ejercicio_2(pista=0):
    """🟡 Decodificar JWT y extraer payload"""
    print(">> 🟡 EJERCICIO 2: Decodificar JWT")
    print("-" * 50)

    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjMiLCJuYW1lIjoiQW5hIiwiaWF0IjoxNzAwMDAwMDAwfQ.firma_falsa"

    print(f"Token: {token[:50]}...")

    if pista == 1:
        print("\n💡 Pista 1: Separa las partes del token:")
        print("  partes = token.split('.')")
        print("  header_b64 = partes[0]")
        print("  payload_b64 = partes[1]")
        print("  firma_b64 = partes[2]")
        return
    elif pista == 2:
        print("\n💡 Pista 2: Decodifica Base64 a dict:")
        print("  def b64_decode(data):")
        print("      padding = 4 - len(data) % 4")
        print("      if padding != 4:")
        print("          data += '=' * padding")
        print("      return json.loads(base64.urlsafe_b64decode(data).decode())")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Resultado esperado:")
        print("  Header:  {'alg': 'HS256', 'typ': 'JWT'}")
        print("  Payload: {'sub': '123', 'name': 'Ana', 'iat': 1700000000}")
        print("  Usuario: Ana")
        return

    print("\nSepara el token en sus 3 partes y decodifica el payload.")
    print("Extrae e imprime: header, payload, y el nombre del usuario.")
    print("\n# ==== ESCRIBE TU CODIGO AQUI ====")


def ejercicio_3(pista=0):
    """🔴 Verificar expiracion de JWT"""
    print(">> 🔴 EJERCICIO 3: Verificar expiracion de JWT")
    print("-" * 50)

    import time
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjMiLCJuYW1lIjoiQW5hIiwiZXhwIjoxNzAwMDAwMDAwfQ.firma"

    print(f"Token: {token[:50]}...")
    print(f"Hora actual: {int(time.time())}")

    if pista == 1:
        print("\n💡 Pista 1: Decodifica el payload y extrae 'exp':")
        print("  payload = b64_decode(token.split('.')[1])")
        print("  exp = payload.get('exp', 0)")
        return
    elif pista == 2:
        print("\n💡 Pista 2: Compara exp con el tiempo actual:")
        print("  ahora = time.time()")
        print("  if ahora > exp:")
        print("      print('Token EXPIRADO')")
        print("  else:")
        print("      print('Token VALIDO')")
        return
    elif pista == 3:
        print("\n💡 Pista 3: El token tiene exp = 1700000000")
        print("  Si la hora actual > 1700000000, el token expiro")
        print("  Para probar un token valido, usa exp futuro:")
        print("  payload = {'sub': '123', 'name': 'Ana', 'exp': int(time.time()) + 3600}")
        return

    print("\nDecodifica el payload, extrae el claim 'exp' y comprueba")
    print("si el token ha expirado comparando con time.time().")
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
