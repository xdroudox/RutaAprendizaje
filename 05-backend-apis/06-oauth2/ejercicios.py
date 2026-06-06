"""
EJERCICIOS - OAuth2
Ejecuta desde raiz: python scripts/runner.py 5 6 [ejercicio]

Niveles:
  🟢 Ej 1: Identificar roles OAuth2
  🟡 Ej 2: Simular flujo Authorization Code
  🔴 Ej 3: Simular flujo Client Credentials

Pistas: python scripts/runner.py 5 6 N -p [1|2|3]
"""

import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def ejercicio_1(pista=0):
    """🟢 Identificar roles OAuth2"""
    print(">> 🟢 EJERCICIO 1: Identificar roles OAuth2")
    print("-" * 50)

    entidades = [
        "Usuario final con datos en Google",
        "App web que quiere acceder a Google Drive",
        "Servidor de Google que emite tokens",
        "API de Google Drive que almacena archivos",
    ]

    roles = ["Resource Owner", "Client", "Authorization Server", "Resource Server"]

    print("Entidades:")
    for e in entidades:
        print(f"  - {e}")
    print()
    print("Roles disponibles:", roles)

    if pista == 1:
        print("\n💡 Pista 1: Cada rol responde a una pregunta:")
        print("  Resource Owner     → Quien es dueno de los datos?")
        print("  Client            → Que app quiere acceso?")
        print("  Authorization Server → Quien emite los tokens?")
        print("  Resource Server   → Quien almacena los datos?")
        return
    elif pista == 2:
        print("\n💡 Pista 2: Relacion entidad-rol:")
        print("  Usuario con datos en Google       → Resource Owner")
        print("  App web que quiere acceso         → Client")
        print("  Servidor que emite tokens         → Authorization Server")
        print("  API de Google Drive               → Resource Server")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Estructura del codigo:")
        print("  entidades = [")
        print("      ('descripcion', 'rol'),")
        print("      ...")
        print("  ]")
        print("  for entidad, rol in entidades:")
        print("      print(f'{entidad} -> {rol}')")
        return

    print("\nAsigna cada entidad a su rol OAuth2 correspondiente.")
    print("Usa una lista de tuplas (entidad, rol).")
    print("\n# ==== ESCRIBE TU CODIGO AQUI ====")


def ejercicio_2(pista=0):
    """🟡 Simular flujo Authorization Code"""
    print(">> 🟡 EJERCICIO 2: Flujo Authorization Code")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1: Pasos basicos del flujo:")
        print("  1. Usuario hace clic en 'Iniciar sesion con Google'")
        print("  2. App redirige a Auth Server con client_id y redirect_uri")
        print("  3. Usuario autentica y autoriza")
        print("  4. Auth Server devuelve authorization code")
        print("  5. App canjea code por access token")
        print("  6. App usa token para acceder a recurso")
        return
    elif pista == 2:
        print("\n💡 Pista 2: Detalles de cada paso:")
        print("  2. GET /auth?client_id=123&redirect_uri=app.com/callback&response_type=code")
        print("  4. Redirect a: redirect_uri?code=auth_code_xyz")
        print("  5. POST /token con code + client_secret")
        print("  5. Response: {access_token, refresh_token, expires_in}")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Usa una lista de strings para los pasos:")
        print("  pasos = [")
        print("      '1. Usuario hace clic...',")
        print("      '2. App redirige a...',")
        print("      ...")
        print("  ]")
        print("  for paso in pasos:")
        print("      print(paso)")
        return

    print("Simula el flujo Authorization Code paso a paso.")
    print("Describe cada paso desde el clic del usuario hasta")
    print("el acceso al recurso con el token.")
    print("\n# ==== ESCRIBE TU CODIGO AQUI ====")


def ejercicio_3(pista=0):
    """🔴 Simular flujo Client Credentials"""
    print(">> 🔴 EJERCICIO 3: Flujo Client Credentials")
    print("-" * 50)

    if pista == 1:
        print("\n💡 Pista 1: Diferencia clave con Authorization Code:")
        print("  NO interviene el usuario → NO hay pantalla de login")
        print("  Autenticacion directa app → auth server")
        return
    elif pista == 2:
        print("\n💡 Pista 2: Pasos:")
        print("  1. App se autentica con client_id + client_secret")
        print("  2. POST /token con grant_type=client_credentials")
        print("  3. Auth Server devuelve access_token")
        print("  4. App usa token para llamar a la API")
        return
    elif pista == 3:
        print("\n💡 Pista 3: Ejemplo de uso:")
        print("  Flujo Client Credentials es ideal para:")
        print("    - Microservicios que se comunican entre si")
        print("    - Cron jobs que acceden a APIs internas")
        print("    - Backend que consume APIs de terceros (sin usuario)")
        return

    print("Simula el flujo Client Credentials paso a paso.")
    print("Describe como una app de servidor se autentica")
    print("directamente contra el Authorization Server.")
    print()
    print("Diferencia clave: No interviene el usuario.")
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
