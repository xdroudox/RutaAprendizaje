"""
EJERCICIOS - JWT y Autenticacion
Ejecuta desde raiz: python scripts/runner.py 5 5 [ejercicio]
"""
import sys
import base64
import json
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Crear un JWT simple (header.payload.firma)"""
    header = {"alg": "HS256", "typ": "JWT"}
    payload = {"sub": "123", "name": "Ana", "iat": 1700000000}
    # Codifica header y payload en base64, firma con "secreto" como HMAC simple
    # Formato: base64(header).base64(payload).base64(firma)
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass

def ejercicio_2():
    """Decodificar un JWT y extraer el payload"""
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjMiLCJuYW1lIjoiQW5hIiwiaWF0IjoxNzAwMDAwMDAwfQ.firma_falsa"
    # Separa las partes, decodifica el payload de base64 a dict
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass

def ejercicio_3():
    """Verificar si un JWT esta expirado"""
    import time
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjMiLCJuYW1lIjoiQW5hIiwiZXhwIjoxNzAwMDAwMDAwfQ.firma"
    # Decodifica el payload, extrae "exp" y compara con time.time()
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
