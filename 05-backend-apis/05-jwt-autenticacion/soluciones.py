"""
SOLUCIONES - JWT y Autenticacion
Ejecuta desde raiz: python scripts/runner.py 5 5 1 -s
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

def ejercicio_1():
    """Crear un JWT simple (header.payload.firma)"""
    header = {"alg": "HS256", "typ": "JWT"}
    payload = {"sub": "123", "name": "Ana", "iat": 1700000000}
    header_b64 = b64_encode(header)
    payload_b64 = b64_encode(payload)
    firma = "firma_simple"
    firma_b64 = base64.urlsafe_b64encode(firma.encode()).rstrip(b"=").decode()
    token = f"{header_b64}.{payload_b64}.{firma_b64}"
    print(f"JWT generado: {token}")

def ejercicio_2():
    """Decodificar un JWT y extraer el payload"""
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjMiLCJuYW1lIjoiQW5hIiwiaWF0IjoxNzAwMDAwMDAwfQ.firma_falsa"
    partes = token.split(".")
    header_b64, payload_b64, firma_b64 = partes
    header = b64_decode(header_b64)
    payload = b64_decode(payload_b64)
    print(f"Header: {header}")
    print(f"Payload: {payload}")
    print(f"Usuario: {payload.get('name')}")

def ejercicio_3():
    """Verificar si un JWT esta expirado"""
    import time
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjMiLCJuYW1lIjoiQW5hIiwiZXhwIjoxNzAwMDAwMDAwfQ.firma"
    payload_b64 = token.split(".")[1]
    payload = b64_decode(payload_b64)
    exp = payload.get("exp", 0)
    ahora = time.time()
    if ahora > exp:
        print(f"Token EXPIRADO (exp: {exp}, ahora: {int(ahora)})")
    else:
        print(f"Token VALIDO (exp: {exp}, ahora: {int(ahora)})")

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
