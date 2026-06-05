import sys, json, base64, hashlib

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    print("=" * 50)
    print("EJERCICIO 1: Decodificar un JWT")
    print("=" * 50)
    jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkFuYSBMb3BleiIsImlhdCI6MTUxNjIzOTAyMiwiZXhwIjoxNTE2MjQyNjIyfQ.XYZ123"
    print("JWT:", jwt)
    print()
    print("TAREA: Separa las tres partes del JWT (header, payload, firma)")
    print("y decodifica header y payload de base64url a texto legible.")
    print()
    print("PISTA: jwt.split('.'); base64.urlsafe_b64decode(parte + '==')")

def ejercicio_2():
    print("=" * 50)
    print("EJERCICIO 2: Generar un JWT")
    print("=" * 50)
    print()
    print("TAREA: Crea una funcion generar_jwt(payload, secreto) que:")
    print("  1. Cree un header con alg='HS256' y typ='JWT'")
    print("  2. Codifique header y payload en base64url")
    print("  3. Genere una firma SHA256 de header.payload + secreto")
    print("  4. Retorne el JWT completo")
    print()
    payload = {"sub": "42", "name": "Carlos Ruiz", "rol": "admin"}
    secreto = "mi_secreto_super_seguro"
    print(f"Payload: {payload}")
    print(f"Secreto: {secreto}")
    print()
    print("PISTA: Usa base64.urlsafe_b64encode y hashlib.sha256")

def ejercicio_3():
    print("=" * 50)
    print("EJERCICIO 3: Verificar un JWT")
    print("=" * 50)
    print()
    print("TAREA: Crea una funcion verificar_jwt(jwt, secreto) que:")
    print("  1. Separe las tres partes del JWT")
    print("  2. Recalcule la firma con el secreto")
    print("  3. Compare la firma calculada con la firma del token")
    print("  4. Retorne True si es valido, False si no")
    print()
    jwt_valido = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0MiIsIm5hbWUiOiJDYXJsb3MgUnVpeiIsInJvbCI6ImFkbWluIn0.abc123firma"
    secreto = "mi_secreto_super_seguro"
    print("JWT:", jwt_valido)
    print("Secreto:", secreto)
    print()
    print("PISTA: Calcula header_b64 + '.' + payload_b64 + secreto, luego SHA256")

pistas = {
    "1": "partes = jwt.split('.'); header_json = base64.urlsafe_b64decode(partes[0] + '=='); payload_json = base64.urlsafe_b64decode(partes[1] + '=='); print(header_json.decode()); print(payload_json.decode())",
    "2": "header_b64 = base64.urlsafe_b64encode(json.dumps(header).encode()).rstrip(b'=').decode(); payload_b64 = base64.urlsafe_b64encode(json.dumps(payload).encode()).rstrip(b'=').decode(); firma = hashlib.sha256((header_b64 + '.' + payload_b64 + secreto).encode()).hexdigest(); return f'{header_b64}.{payload_b64}.{firma}'",
    "3": "partes = jwt.split('.'); firma_calc = hashlib.sha256((partes[0] + '.' + partes[1] + secreto).encode()).hexdigest(); return firma_calc == partes[2]"
}

def menu():
    print("=" * 50)
    print("JWT Y AUTENTICACION - EJERCICIOS")
    print("=" * 50)
    print("1 - Decodificar un JWT")
    print("2 - Generar un JWT")
    print("3 - Verificar un JWT")
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
