"""
SOLUCIONES - Docker
Ejecuta desde raiz: python scripts/runner.py 10 02 [ejercicio] solucion
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    """Escribe un Dockerfile simple para una app Python"""
    print(">> SOLUCION 1: Dockerfile para app Python")
    print("-" * 40)
    print("Contenido de Dockerfile:")
    print()
    print("  FROM python:3.11-slim")
    print("  WORKDIR /app")
    print("  COPY app.py .")
    print("  COPY requirements.txt .")
    print("  RUN pip install -r requirements.txt")
    print("  EXPOSE 5000")
    print('  CMD ["python", "app.py"]')
    print()
    print("Contenido de app.py:")
    print('  print("Hola Docker")')
    print()
    print("Construir:")
    print("  docker build -t mi-app .")

def solucion_2():
    """Construye y ejecuta un contenedor con docker-compose"""
    print(">> SOLUCION 2: Docker Compose")
    print("-" * 40)
    print("Contenido de docker-compose.yml:")
    print()
    print("  services:")
    print("    web:")
    print("      build: .")
    print("      ports:")
    print("        - '8080:5000'")
    print("    db:")
    print("      image: postgres:15")
    print("      environment:")
    print("        - POSTGRES_PASSWORD=secret")
    print()
    print("Ejecutar:")
    print("  docker compose up -d")

def solucion_3():
    """Publica un puerto y monta un volumen"""
    print(">> SOLUCION 3: Puertos y volumenes")
    print("-" * 40)
    print("Comando ejecutado:")
    print()
    print("  docker run -d ^")
    print("    -p 8080:5000 ^")
    print("    -v %cd%:/app ^")
    print("    --name mi-app-container ^")
    print("    mi-app")
    print()
    print("Output de docker ps:")
    print("  CONTAINER ID   IMAGE     COMMAND             CREATED         STATUS         PORTS                    NAMES")
    print("  abcdef123456   mi-app    \"python app.py\"     5 seconds ago   Up 5 seconds   0.0.0.0:8080->5000/tcp   mi-app-container")
    print()
    print("Explicacion:")
    print("  -p 8080:5000 mapea el puerto del host al contenedor.")
    print("  -v %cd%:/app monta el directorio actual como volumen.")
    print("  -d ejecuta en segundo plano.")

if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            print(f">> SOLUCION {num + 1}: {soluciones[num].__doc__}")
            print("-" * 40)
            soluciones[num]()
    else:
        for i, sol in enumerate(soluciones, 1):
            print(f"  {i}. {sol.__doc__}")
