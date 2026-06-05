import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def obtener_token(client_id, client_secret):
    if client_id == "mi_backend" and client_secret == "pass123":
        return {
            "access_token": "eyJhbGciOiJIUzI1NiJ9.dGVzdA.some_signature",
            "token_type": "Bearer",
            "expires_in": 3600
        }
    return None

def solucion_1():
    print("=" * 50)
    print("SOLUCION 1: Identificar roles OAuth2")
    print("=" * 50)
    print()
    print('Escenario: "Una app de fotos (FotoApp) quiere acceder a las')
    print('fotos de un usuario almacenadas en Google Fotos."')
    print()
    print("  a) El usuario dueño de las fotos:")
    print("     -> Resource Owner (propietario del recurso)")
    print()
    print("  b) FotoApp:")
    print("     -> Client (aplicacion que solicita acceso)")
    print()
    print("  c) Google (que emite el token):")
    print("     -> Authorization Server (servidor de autorizacion)")
    print()
    print("  d) Google Fotos API:")
    print("     -> Resource Server (servidor de recursos)")

def solucion_2():
    print("=" * 50)
    print("SOLUCION 2: Simular flujo Client Credentials")
    print("=" * 50)
    resultado = obtener_token("mi_backend", "pass123")
    print("Resultado con credenciales correctas:")
    print(resultado)
    print()
    resultado2 = obtener_token("mi_backend", "wrongpass")
    print("Resultado con credenciales incorrectas:")
    print(resultado2)
    print()
    print("Explicacion: En el flujo Client Credentials, la aplicacion")
    print("se autentica con su Client ID y Client Secret para obtener")
    print("un token sin intervencion del usuario.")

def solucion_3():
    print("=" * 50)
    print("SOLUCION 3: Secuencia Authorization Code")
    print("=" * 50)
    orden = [
        (1, "El usuario solicita iniciar sesion con un proveedor externo"),
        (2, "La aplicacion redirige al usuario al Auth Server"),
        (3, "El usuario inicia sesion y autoriza a la aplicacion"),
        (4, "El Auth Server devuelve un codigo de autorizacion al Client"),
        (5, "El Client intercambia el codigo por un Access Token"),
        (6, "El Client usa el Access Token para acceder a recursos"),
    ]
    for num, paso in orden:
        print(f"  {num}. {paso}")

def menu():
    print("SOLUCIONES - OAUTH2")
    print("1 - Identificar roles OAuth2")
    print("2 - Simular flujo Client Credentials")
    print("3 - Secuencia Authorization Code")

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
