import sys, json, base64, hashlib

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def generar_jwt(payload, secreto):
    header = {"alg": "HS256", "typ": "JWT"}
    header_b64 = base64.urlsafe_b64encode(json.dumps(header, separators=(",", ":")).encode()).rstrip(b"=").decode()
    payload_b64 = base64.urlsafe_b64encode(json.dumps(payload, separators=(",", ":")).encode()).rstrip(b"=").decode()
    firma_input = f"{header_b64}.{payload_b64}{secreto}".encode()
    firma = hashlib.sha256(firma_input).hexdigest()
    return f"{header_b64}.{payload_b64}.{firma}"

def verificar_jwt(jwt, secreto):
    partes = jwt.split(".")
    if len(partes) != 3:
        return False
    firma_calc = hashlib.sha256(f"{partes[0]}.{partes[1]}{secreto}".encode()).hexdigest()
    return firma_calc == partes[2]

def solucion_1():
    print("=" * 50)
    print("SOLUCION 1: Decodificar un JWT")
    print("=" * 50)
    jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkFuYSBMb3BleiIsImlhdCI6MTUxNjIzOTAyMiwiZXhwIjoxNTE2MjQyNjIyfQ.XYZ123"
    partes = jwt.split(".")
    print("Partes del JWT:")
    for i, etiqueta in enumerate(["Header", "Payload", "Signature"]):
        print(f"  {etiqueta}: {partes[i]}")
    print()
    header_dec = json.loads(base64.urlsafe_b64decode(partes[0] + "==").decode())
    payload_dec = json.loads(base64.urlsafe_b64decode(partes[1] + "==").decode())
    print("Header decodificado:")
    print(json.dumps(header_dec, indent=2))
    print()
    print("Payload decodificado:")
    print(json.dumps(payload_dec, indent=2))

def solucion_2():
    print("=" * 50)
    print("SOLUCION 2: Generar un JWT")
    print("=" * 50)
    payload = {"sub": "42", "name": "Carlos Ruiz", "rol": "admin"}
    secreto = "mi_secreto_super_seguro"
    jwt = generar_jwt(payload, secreto)
    print("JWT generado:")
    print(jwt)
    print()
    print("Partes:")
    for i, etiqueta in enumerate(["Header", "Payload", "Signature"]):
        print(f"  {etiqueta}: {jwt.split('.')[i]}")

def solucion_3():
    print("=" * 50)
    print("SOLUCION 3: Verificar un JWT")
    print("=" * 50)
    payload = {"sub": "42", "name": "Carlos Ruiz", "rol": "admin"}
    secreto = "mi_secreto_super_seguro"
    jwt = generar_jwt(payload, secreto)
    print("JWT generado:", jwt)
    print()
    valido = verificar_jwt(jwt, secreto)
    print(f"Verificacion con secreto correcto: {valido}")
    print()
    falso = verificar_jwt(jwt, "otro_secreto")
    print(f"Verificacion con secreto incorrecto: {falso}")
    print()
    print("Explicacion: la firma se calcula con el secreto, por lo que")
    print("cambiar el secreto produce una firma diferente.")

def menu():
    print("SOLUCIONES - JWT Y AUTENTICACION")
    print("1 - Decodificar un JWT")
    print("2 - Generar un JWT")
    print("3 - Verificar un JWT")

def main():
    args = sys.argv[1:]
    if not args:
        menu()
        return
    num = args[0]
    if num == "1":
        solucion_1()
    elif num == "2":
        solucion_2()
    elif num == "3":
        solucion_3()
    else:
        print("Solucion no valida. Usa 1, 2 o 3.")

if __name__ == "__main__":
    main()
