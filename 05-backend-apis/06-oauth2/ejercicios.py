import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    print("=" * 50)
    print("EJERCICIO 1: Identificar roles OAuth2")
    print("=" * 50)
    print()
    print("TAREA: Dado el siguiente escenario, identifica el rol de cada")
    print("participante segun OAuth2.")
    print()
    print('Escenario: "Una app de fotos (FotoApp) quiere acceder a las')
    print('fotos de un usuario almacenadas en Google Fotos. El usuario')
    print('inicia sesion con su cuenta de Google y autoriza a FotoApp.')
    print('Google emite un token que FotoApp usa para leer las fotos."')
    print()
    print("  a) El usuario dueño de las fotos:")
    print("  b) FotoApp:")
    print("  c) Google (que emite el token):")
    print("  d) Google Fotos API:")
    print()
    print("PISTA: Resource Owner, Client, Authorization Server, Resource Server")

def ejercicio_2():
    print("=" * 50)
    print("EJERCICIO 2: Simular flujo Client Credentials")
    print("=" * 50)
    print()
    print("TAREA: Implementa una funcion obtener_token(client_id, client_secret)")
    print("que simule el flujo Client Credentials.")
    print()
    print("Reglas:")
    print("  - Si client_id='mi_backend' y client_secret='pass123'")
    print("    retorna un dict con access_token, token_type='Bearer',")
    print("    expires_in=3600")
    print("  - Si no, retorna None")
    print()
    print("PISTA: if client_id == 'mi_backend' and client_secret == 'pass123':")

def ejercicio_3():
    print("=" * 50)
    print("EJERCICIO 3: Secuencia del flujo Authorization Code")
    print("=" * 50)
    print()
    print("TAREA: Ordena los siguientes pasos del flujo Authorization Code")
    print("numerandolos del 1 al 6.")
    print()
    pasos = [
        "El Auth Server devuelve un codigo de autorizacion al Client",
        "La aplicacion redirige al usuario al Auth Server",
        "El Client intercambia el codigo por un Access Token",
        "El usuario inicia sesion y autoriza a la aplicacion",
        "El Client usa el Access Token para acceder a recursos",
        "El usuario solicita iniciar sesion con un proveedor externo",
    ]
    for i, paso in enumerate(pasos, 1):
        print(f"  __. {paso}")
    print()
    print("PISTA: El orden logico es: solicitud -> redireccion -> login")
    print("  -> codigo -> intercambio -> uso del token.")

pistas = {
    "1": "a) Resource Owner, b) Client, c) Authorization Server, d) Resource Server",
    "2": "def obtener_token(client_id, client_secret): if client_id == 'mi_backend' and client_secret == 'pass123': return {'access_token': 'tokendemo123', 'token_type': 'Bearer', 'expires_in': 3600}; return None",
    "3": "1-sexto, 2-segundo, 3-quinto, 4-tercero, 5-sexto, 6-primero. Orden: 6, 2, 4, 1, 3, 5"
}

def menu():
    print("=" * 50)
    print("OAUTH2 - EJERCICIOS")
    print("=" * 50)
    print("1 - Identificar roles OAuth2")
    print("2 - Simular flujo Client Credentials")
    print("3 - Secuencia Authorization Code")
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
