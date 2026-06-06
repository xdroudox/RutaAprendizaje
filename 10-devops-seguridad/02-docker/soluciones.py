"""
SOLUCIONES - Docker
Ejecuta desde raiz: python scripts/runner.py 10 02 [ejercicio] -s
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def solucion_1():
    """Dockerfile: escribe un Dockerfile para una app Python"""
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
    print("Contenido de requirements.txt (puede estar vacio):")
    print()
    print("Construir:")
    print("  docker build -t mi-app .")
    print()
    print("Explicacion:")
    print("  FROM: imagen base con Python 3.11 optimizada.")
    print("  WORKDIR: establece /app como directorio activo.")
    print("  COPY: copia archivos del proyecto al contenedor.")
    print("  RUN: instala dependencias durante el build.")
    print("  EXPOSE: documenta el puerto (no lo abre).")
    print("  CMD: comando que se ejecuta al arrancar el contenedor.")

def solucion_2():
    """Docker Compose: define servicios web + db con compose"""
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
    print()
    print("Verificar:")
    print("  docker compose ps")
    print()
    print("Explicacion:")
    print("  `build: .` construye la imagen desde el Dockerfile local.")
    print("  `ports` mapea el puerto del host al contenedor.")
    print("  `image: postgres:15` usa una imagen oficial de Docker Hub.")
    print("  `environment` pasa variables de entorno al contenedor.")
    print("  Con `up -d` se levantan ambos servicios simultaneamente.")

def solucion_3():
    """Puertos y volumenes: ejecuta contenedor con mapeo y montaje"""
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
    print("  `-p 8080:5000` mapea el puerto 8080 del host al 5000 del contenedor.")
    print("  `-v %cd%:/app` monta el directorio actual en /app (sincronizado).")
    print("  `--name` asigna un nombre para facilitar la gestion.")
    print("  `-d` ejecuta el contenedor en segundo plano.")

if __name__ == "__main__":
    soluciones = [solucion_1, solucion_2, solucion_3]
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(soluciones):
            soluciones[num]()
    else:
        for i, sol in enumerate(soluciones, 1):
            print(f"  {i}. {sol.__doc__}")
