"""
SOLUCIONES - JWT y Autenticacion
Ejecuta: python scripts/runner.py 5 5 [ejercicio] -s
"""

import sys
import base64
import json
import time

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


def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: Crear JWT simple")
    print("=" * 50)

    header = {"alg": "HS256", "typ": "JWT"}
    payload = {"sub": "123", "name": "Ana", "iat": 1700000000}

    print("--- CODIGO ---")
    print("header_b64 = b64_encode(header)")
    print("payload_b64 = b64_encode(payload)")
    print("firma_b64 = base64.urlsafe_b64encode(b'firma_simple').rstrip(b'=').decode()")
    print("token = f'{header_b64}.{payload_b64}.{firma_b64}'")
    print()

    header_b64 = b64_encode(header)
    payload_b64 = b64_encode(payload)
    firma = "firma_simple"
    firma_b64 = base64.urlsafe_b64encode(firma.encode()).rstrip(b"=").decode()
    token = f"{header_b64}.{payload_b64}.{firma_b64}"

    print("--- RESULTADO ---")
    print(f"  JWT: {token}")
    print(f"  Header (decod): {b64_decode(header_b64)}")
    print(f"  Payload (decod): {b64_decode(payload_b64)}")

    print()
    print("--- EXPLICACION ---")
    print("""
Construccion de un JWT:

  1. Convertir header y payload JSON a string
  2. Codificar a Base64 URL-safe (sin padding '=')
  3. Firmar con clave secreta usando HMAC
  4. Concatenar: header.payload.firma

Base64 URL-safe reemplaza:
  '+' → '-'   '/' → '_'   y quita el padding '='

En produccion se usa una libreria como PyJWT:
  import jwt
  token = jwt.encode(payload, 'secreto', algorithm='HS256')
  datos = jwt.decode(token, 'secreto', algorithms=['HS256'])
""")


def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: Decodificar JWT y extraer payload")
    print("=" * 50)

    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjMiLCJuYW1lIjoiQW5hIiwiaWF0IjoxNzAwMDAwMDAwfQ.firma_falsa"

    print("--- CODIGO ---")
    print("partes = token.split('.')")
    print("header = b64_decode(partes[0])")
    print("payload = b64_decode(partes[1])")
    print()

    partes = token.split(".")
    header = b64_decode(partes[0])
    payload = b64_decode(partes[1])

    print("--- RESULTADO ---")
    print(f"  Header:  {header}")
    print(f"  Payload: {payload}")
    print(f"  Usuario: {payload.get('name')}")

    print()
    print("--- EXPLICACION ---")
    print("""
Decodificar un JWT (sin verificar firma):

  1. Separar por '.' → [header, payload, firma]
  2. Decodificar cada parte de Base64 URL-safe
  3. Convertir JSON string a dict

Nota: CUALQUIERA puede decodificar un JWT. La seguridad
esta en que NADIE puede MODIFICARLO sin la clave secreta
(la firma no coincidiria).

Siempre verifica la firma en el servidor antes de confiar
en los claims del payload.
""")


def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: Verificar expiracion de JWT")
    print("=" * 50)

    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjMiLCJuYW1lIjoiQW5hIiwiZXhwIjoxNzAwMDAwMDAwfQ.firma"

    print("--- CODIGO ---")
    print("payload = b64_decode(token.split('.')[1])")
    print("exp = payload.get('exp', 0)")
    print("ahora = time.time()")
    print("if ahora > exp:")
    print("    print('Token EXPIRADO')")
    print("else:")
    print("    print('Token VALIDO')")
    print()

    payload = b64_decode(token.split(".")[1])
    exp = payload.get("exp", 0)
    ahora = time.time()

    print("--- RESULTADO ---")
    print(f"  exp:   {exp}")
    print(f"  ahora: {int(ahora)}")
    if ahora > exp:
        print("  Estado: EXPIRADO")
    else:
        print("  Estado: VALIDO")

    print()
    print("--- EXPLICACION ---")
    print("""
El claim 'exp' (expiration) es un timestamp Unix.
Si el tiempo actual supera 'exp', el token expiro.

Practicas recomendadas:
  - exp suele ser 15-60 minutos desde iat
  - Usar refresh tokens para sesiones largas
  - Siempre verificar exp en el servidor

Ejemplo con PyJWT (verifica exp automaticamente):
  import jwt
  try:
      datos = jwt.decode(token, 'secreto', algorithms=['HS256'])
  except jwt.ExpiredSignatureError:
      print('Token expirado')
""")


if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
