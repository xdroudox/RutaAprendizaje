"""
EJERCICIOS - Docker
Ejecuta desde raiz: python scripts/runner.py 10 02 [ejercicio] [-p N]
"""
import sys
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def ejercicio_1(pista=0):
    """Dockerfile: escribe un Dockerfile para una app Python"""
    print(">> EJERCICIO 1: Dockerfile para app Python")
    print("-" * 40)
    print("Crea un Dockerfile para una aplicacion Python simple.")
    print()
    print("Requisitos:")
    print("  - Usar python:3.11-slim como imagen base")
    print("  - Directorio de trabajo: /app")
    print("  - Copiar app.py y requirements.txt")
    print("  - Instalar dependencias con pip")
    print("  - Exponer puerto 5000")
    print("  - Comando de inicio: python app.py")
    print()
    print("Crea tambien app.py que muestre 'Hola Docker'.")
    print()
    print("Construye con:")
    print("  docker build -t mi-app .")
    print()
    print("# ==== ESCRIBE AQUI EL CONTENIDO DEL DOCKERFILE ====")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  FROM define la imagen base.")
        print("  WORKDIR cambia el directorio activo.")
        print("  COPY copia archivos del host al contenedor.")
        print("  RUN ejecuta comandos durante la construccion.")
        print("  EXPOSE documenta el puerto (no lo publica).")
        print("  CMD define el comando por defecto al ejecutar.")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  Estructura del Dockerfile:")
        print("    FROM python:3.11-slim")
        print("    WORKDIR /app")
        print("    COPY app.py .")
        print("    COPY requirements.txt .")
        print("    RUN pip install -r requirements.txt")
        print("    EXPOSE 5000")
        print('    CMD ["python", "app.py"]')
        print()
        print("  app.py:")
        print('    print("Hola Docker")')
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  Dockerfile completo:")
        print("    FROM python:3.11-slim")
        print("    WORKDIR /app")
        print("    COPY app.py .")
        print("    COPY requirements.txt .")
        print("    RUN pip install -r requirements.txt")
        print("    EXPOSE 5000")
        print('    CMD ["python", "app.py"]')
        print()
        print("  Crea un requirements.txt (puede estar vacio o contener flask).")
        print("  Construye: docker build -t mi-app .")
        print("  Verifica: docker images | findstr mi-app")

def ejercicio_2(pista=0):
    """Docker Compose: define servicios web + db con compose"""
    print(">> EJERCICIO 2: Docker Compose")
    print("-" * 40)
    print("Crea un archivo docker-compose.yml con dos servicios.")
    print()
    print("Servicio 'web':")
    print("  - Construir desde el directorio actual (build: .)")
    print("  - Mapear puerto 8080 del host al 5000 del contenedor")
    print()
    print("Servicio 'db':")
    print("  - Usar imagen postgres:15")
    print("  - Variable de entorno POSTGRES_PASSWORD=secret")
    print()
    print("Ejecuta:")
    print("  docker compose up -d")
    print()
    print("# ==== ESCRIBE AQUI EL CONTENIDO DEL DOCKER-COMPOSE.YML ====")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  Docker Compose usa formato YAML.")
        print("  `services:` es la clave principal (lista de servicios).")
        print("  Cada servicio tiene nombre, image/build, ports, environment.")
        print("  `build: .` usa el Dockerfile del directorio actual.")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  Estructura basica:")
        print("    services:")
        print("      web:")
        print("        build: .")
        print("        ports:")
        print("          - '8080:5000'")
        print("      db:")
        print("        image: postgres:15")
        print("        environment:")
        print("          - POSTGRES_PASSWORD=secret")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  docker-compose.yml completo:")
        print("    services:")
        print("      web:")
        print("        build: .")
        print("        ports:")
        print("          - '8080:5000'")
        print("      db:")
        print("        image: postgres:15")
        print("        environment:")
        print("          - POSTGRES_PASSWORD=secret")
        print()
        print("  Ejecuta: docker compose up -d")
        print("  Verifica: docker compose ps")

def ejercicio_3(pista=0):
    """Puertos y volumenes: ejecuta contenedor con mapeo y montaje"""
    print(">> EJERCICIO 3: Puertos y volumenes")
    print("-" * 40)
    print("Ejecuta el contenedor 'mi-app' con las siguientes opciones:")
    print()
    print("  - Puerto 5000 del contenedor mapeado al 8080 del host")
    print("  - Volumen del directorio actual a /app en el contenedor")
    print("  - Nombre del contenedor: mi-app-container")
    print("  - Modo detach (background)")
    print()
    print("Comando:")
    print("  docker run -d ^")
    print("    -p 8080:5000 ^")
    print("    -v %cd%:/app ^")
    print("    --name mi-app-container ^")
    print("    mi-app")
    print()
    print("Verifica:")
    print("  docker ps")
    print()
    print("# ==== PEGA AQUI EL OUTPUT DE docker ps ====")
    if pista:
        print("\n" + "="*40)
        print("PISTAS:")
    if pista >= 1:
        print("\n🟢 PISTA 1 (Basica):")
        print("  `-p host:contenedor` mapea puertos.")
        print("  `-v host:contenedor` monta un volumen.")
        print("  `--name` asigna un nombre al contenedor.")
        print("  `-d` ejecuta en background (detach).")
    if pista >= 2:
        print("\n🟡 PISTA 2 (Intermedia):")
        print("  En Windows usa %cd% para el directorio actual.")
        print("  En PowerShell usa ${pwd} en vez de %cd%.")
        print()
        print("  Comando completo (Windows cmd):")
        print("    docker run -d -p 8080:5000 -v %cd%:/app --name mi-app-container mi-app")
    if pista >= 3:
        print("\n🔴 PISTA 3 (Avanzada - casi la solucion):")
        print("  Comando:")
        print("    docker run -d ^")
        print("      -p 8080:5000 ^")
        print("      -v %cd%:/app ^")
        print("      --name mi-app-container ^")
        print("      mi-app")
        print()
        print("  Output de docker ps:")
        print("    CONTAINER ID   IMAGE     COMMAND             PORTS                    NAMES")
        print("    abc123...      mi-app    \"python app.py\"     0.0.0.0:8080->5000/tcp   mi-app-container")

if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3]
    pista_level = 0
    if "-p" in sys.argv:
        idx = sys.argv.index("-p")
        if idx + 1 < len(sys.argv) and sys.argv[idx + 1].isdigit():
            pista_level = int(sys.argv[idx + 1])
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num = int(sys.argv[1]) - 1
        if 0 <= num < len(ejercicios):
            ejercicios[num](pista=pista_level)
    else:
        for i, ej in enumerate(ejercicios, 1):
            print(f"  {i}. {ej.__doc__}")
