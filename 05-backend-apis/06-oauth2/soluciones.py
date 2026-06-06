"""
SOLUCIONES - OAuth2
Ejecuta: python scripts/runner.py 5 6 [ejercicio] -s
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def solucion_1():
    print("=" * 50)
    print("🟢 SOLUCION 1: Identificar roles OAuth2")
    print("=" * 50)

    print("--- RESULTADO ---")
    entidades = [
        ("Usuario final con datos en Google", "Resource Owner"),
        ("App web que quiere acceder a Google Drive", "Client"),
        ("Servidor de Google que emite tokens", "Authorization Server"),
        ("API de Google Drive que almacena archivos", "Resource Server"),
    ]
    for entidad, rol in entidades:
        print(f"  {entidad:55s} -> {rol}")

    print()
    print("--- EXPLICACION ---")
    print("""
Los 4 roles de OAuth2:

  Resource Owner    → Dueno de los datos (usuario)
  Client            → App que solicita acceso
  Authorization Server → Emite tokens tras autenticar
  Resource Server   → Aloja los recursos protegidos

El Client NUNCA ve las credenciales del Resource Owner.
Solo recibe un token temporal con permisos limitados.
""")


def solucion_2():
    print("=" * 50)
    print("🟡 SOLUCION 2: Flujo Authorization Code")
    print("=" * 50)

    print("--- RESULTADO ---")
    pasos = [
        "1. Usuario hace clic en 'Iniciar sesion con Google'",
        "2. App redirige a: https://accounts.google.com/o/oauth2/auth?client_id=123&redirect_uri=app.com/callback&response_type=code&scope=drive.readonly",
        "3. Usuario ingresa credenciales y autoriza los permisos solicitados",
        "4. Auth Server redirige a: app.com/callback?code=auth_code_xyz",
        "5. App envia POST /token con code + client_secret",
        "6. Auth Server devuelve {access_token, refresh_token, expires_in}",
        "7. App usa access_token en header: Authorization: Bearer <token>",
        "8. Resource Server valida token y devuelve los datos solicitados",
    ]
    for paso in pasos:
        print(f"  {paso}")

    print()
    print("--- EXPLICACION ---")
    print("""
El flujo Authorization Code es el mas seguro para apps web:

  - El code es de un solo uso y expira en minutos
  - El code se canjea por token en canal seguro (server-to-server)
  - El client_secret nunca se expone al navegador
  - Se puede obtener un refresh_token para sesiones largas

PKCE (Proof Key for Code Exchange) extiende este flujo
para apps moviles y SPA que no pueden guardar un secreto.
""")


def solucion_3():
    print("=" * 50)
    print("🔴 SOLUCION 3: Flujo Client Credentials")
    print("=" * 50)

    print("--- RESULTADO ---")
    pasos = [
        "1. App de servidor se autentica con client_id + client_secret",
        "2. Envia POST a Authorization Server /token",
        "3. Body: grant_type=client_credentials&client_id=...&client_secret=...",
        "4. Auth Server valida credenciales y devuelve access_token",
        "5. App usa access_token en header: Authorization: Bearer <token>",
        "6. Resource Server verifica token y responde con datos",
    ]
    for paso in pasos:
        print(f"  {paso}")

    print()
    print("--- EXPLICACION ---")
    print("""
El flujo Client Credentials es para comunicacion server-to-server:

  Diferencia clave: NO interviene el usuario.
  La app se autentica directamente con sus propias credenciales.

  Casos de uso:
    - Microservicios que se comunican entre si
    - Batch jobs / cron jobs que acceden a APIs
    - Backend que consume APIs de terceros sin usuario

  No emite refresh_token porque el client puede pedir uno nuevo
  cuando quiera (tiene las credenciales).
""")


if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
