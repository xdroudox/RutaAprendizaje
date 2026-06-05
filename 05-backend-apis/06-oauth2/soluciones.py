"""
SOLUCIONES - OAuth2
Ejecuta desde raiz: python scripts/runner.py 5 6 1 -s
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Identificar roles en OAuth2"""
    entidades = [
        ("Usuario final con datos en Google", "Resource Owner"),
        ("App web que quiere acceder a Google Drive", "Client"),
        ("Servidor de Google que emite tokens", "Authorization Server"),
        ("API de Google Drive que almacena archivos", "Resource Server"),
    ]
    for entidad, rol in entidades:
        print(f"  {entidad:55s} -> {rol}")

def ejercicio_2():
    """Simular flujo Authorization Code paso a paso"""
    print("=== FLUJO AUTHORIZATION CODE ===")
    pasos = [
        "1. Usuario hace clic en 'Iniciar sesion con Google'",
        "2. App redirige a Authorization Server?client_id=123&redirect_uri=app.com/callback&response_type=code",
        "3. Usuario ingresa credenciales y autoriza los permisos solicitados",
        "4. Authorization Server redirige a redirect_uri?code=auth_code_xyz",
        "5. App envia POST a Authorization Server con code + client_secret",
        "6. Authorization Server devuelve {access_token, refresh_token, expires_in}",
        "7. App usa access_token en header Authorization: Bearer <token>",
        "8. Resource Server valida token y devuelve los datos solicitados",
    ]
    for paso in pasos:
        print(paso)

def ejercicio_3():
    """Simular flujo Client Credentials"""
    print("=== FLUJO CLIENT CREDENTIALS ===")
    pasos = [
        "1. App de servidor se autentica con client_id + client_secret",
        "2. Envia POST a Authorization Server /token con grant_type=client_credentials",
        "3. Authorization Server valida credenciales y devuelve access_token",
        "4. App usa access_token para llamar a la API interna",
        "5. Resource Server verifica token y responde con datos",
    ]
    for paso in pasos:
        print(paso)
    print()
    print("Diferencia clave: No interviene el usuario. Solo maquina a maquina.")

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
