"""
EJERCICIOS - OAuth2
Ejecuta desde raiz: python scripts/runner.py 5 6 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Identificar roles en OAuth2"""
    entidades = [
        "Usuario final con datos en Google",
        "App web que quiere acceder a Google Drive",
        "Servidor de Google que emite tokens",
        "API de Google Drive que almacena archivos",
    ]
    roles = ["Resource Owner", "Client", "Authorization Server", "Resource Server"]
    # Asigna cada entidad a su rol
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass

def ejercicio_2():
    """Simular flujo Authorization Code paso a paso"""
    # Imprime los pasos del flujo:
    # 1. Usuario hace clic en "Iniciar sesion con Google"
    # 2. Redirige a auth server con client_id y redirect_uri
    # 3. Usuario autentica y autoriza
    # 4. Auth server devuelve authorization code
    # 5. Cliente canjea code por access token
    # 6. Cliente usa token para acceder a recurso
    # ==== ESCRIBE TU RESPUESTA AQUI ====
    pass

def ejercicio_3():
    """Simular flujo Client Credentials"""
    # Simula el flujo client_credentials:
    # Cliente se autentica con client_id + client_secret
    # Obtiene access token directamente
    # Usa el token para llamar a la API
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
