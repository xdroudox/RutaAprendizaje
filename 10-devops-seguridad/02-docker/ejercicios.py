"""
EJERCICIOS - Docker
Ejecuta desde raiz: python scripts/runner.py 10 02 [ejercicio]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1():
    """Escribe un Dockerfile simple para una app Python"""
    print(">> EJERCICIO 1: Dockerfile para app Python")
    print("-" * 40)
    print("Crea un Dockerfile con las siguientes caracteristicas:")
    print()
    print("  - FROM python:3.11-slim")
    print("  - WORKDIR /app")
    print("  - COPIAR app.py y requirements.txt")
    print("  - EJECUTAR pip install -r requirements.txt")
    print("  - EXPONER puerto 5000")
    print("  - CMD para ejecutar app.py")
    print()
    print("Crea tambien app.py con: print('Hola Docker')")
    print()
    print("Construye con: docker build -t mi-app .")
    print("# ==== ESCRIBE AQUI EL CONTENIDO DEL Dockerfile ====")

def ejercicio_2():
    """Construye y ejecuta un contenedor con docker-compose"""
    print(">> EJERCICIO 2: Docker Compose")
    print("-" * 40)
    print("Crea un archivo docker-compose.yml con dos servicios:")
    print()
    print("  Servicio 'web':")
    print("    - build: .")
    print("    - ports: '8080:5000'")
    print()
    print("  Servicio 'db':")
    print("    - image: postgres:15")
    print("    - environment: POSTGRES_PASSWORD=secret")
    print()
    print("Ejecuta: docker compose up -d")
    print("# ==== ESCRIBE AQUI EL CONTENIDO DEL docker-compose.yml ====")

def ejercicio_3():
    """Publica un puerto y monta un volumen"""
    print(">> EJERCICIO 3: Puertos y volumenes")
    print("-" * 40)
    print("Ejecuta el contenedor mi-app con:")
    print()
    print("  - Puerto 5000 del contenedor mapeado al 8080 del host")
    print("  - Volumen del directorio actual a /app en el contenedor")
    print("  - Nombre: mi-app-container")
    print("  - Modo detach (-d)")
    print()
    print("Ejecuta:")
    print("  docker run -d \\")
    print("    -p 8080:5000 \\")
    print("    -v %cd%:/app \\")
    print("    --name mi-app-container \\")
    print("    mi-app")
    print()
    print("# ==== PEGA AQUI EL OUTPUT DE docker ps ====")

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            print(f">> EJERCICIO {num + 1}: {ejercicios[num].__doc__}")
            print("-" * 40)
            ejercicios[num]()
    else:
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
