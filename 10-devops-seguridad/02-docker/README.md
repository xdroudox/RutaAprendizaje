# 02 - Docker

## Glosario

- **Contenedor**: instancia ligera y portable que ejecuta una aplicacion con todo lo necesario.
- **Dockerfile**: archivo de texto con instrucciones para construir una imagen.
- **Entrypoint**: comando que se ejecuta al iniciar el contenedor.
- **Imagen**: plantilla inmutable y liviana (basada en capas) usada para crear contenedores.
- **Orquestacion**: gestion automatica de multiples contenedores (escalado, redes, etc.).
- **Puerto**: canal de comunicacion; se mapea un puerto del host al contenedor (`-p 8080:80`).
- **Registry**: repositorio de imagenes (Docker Hub, GitHub Container Registry, etc.).
- **Volumen**: mecanismo para persistir datos fuera del sistema de archivos del contenedor.

## Conceptos clave

- **Imagen vs Contenedor**: la imagen es la receta (READ-ONLY); el contenedor es la receta ejecutandose (READ-WRITE). Puedes crear multiples contenedores desde una misma imagen.
- **Capas (layers)**: cada instruccion en un Dockerfile (`FROM`, `RUN`, `COPY`) crea una capa. Docker cachea las capas para acelerar builds. Si una capa no cambia, reusa la cache.
- **Volumenes**: los datos dentro de un contenedor desaparecen al eliminarlo. Los volumenes montan directorios del host dentro del contenedor para persistir datos (bases de datos, logs, uploads).
- **Puertos**: por defecto los contenedores estan aislados. Con `-p host:contenedor` expones un puerto para que sea accesible desde el host.
- **Docker Compose**: define y ejecuta aplicaciones multi-contenedor con un solo archivo YAML. Ideal para desarrollo local con base de datos, cache, colas, etc.

## Comparativa

| Aspecto | Docker | Maquina Virtual (VM) | Podman |
|---------|--------|----------------------|--------|
| Aislamiento | A nivel de proceso (kernel compartido) | Hipervisor, kernel propio | Similar a Docker, daemon-less |
| Arranque | Segundos | Minutos | Segundos |
| Tamanio | MB | GB | MB |
| Consumo | Ligero | Pesado | Ligero |
| Popularidad | Muy alta | Alta (infraestructura) | Creciente |

| Lenguaje | Build | Ejecucion | Dockerfile tipico |
|----------|-------|-----------|-------------------|
| Python | `pip install` | `python app.py` | `FROM python:3.11-slim` |
| Java | `mvn package` | `java -jar app.jar` | `FROM openjdk:17-jdk-slim` |
| JavaScript | `npm ci` | `node server.js` | `FROM node:18-alpine` |

## Ejemplo guiado

**Objetivo**: crear una app Python simple, dockerizarla y ejecutarla con volumen.

```dockerfile
# Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY app.py .
RUN pip install flask
EXPOSE 5000
CMD ["python", "app.py"]
```

```python
# app.py
from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Hola Docker!"
app.run(host="0.0.0.0", port=5000)
```

```bash
# Construir y ejecutar
docker build -t mi-app .
docker run -d -p 8080:5000 --name mi-app-container mi-app
# Visita http://localhost:8080
# Detener
docker stop mi-app-container && docker rm mi-app-container
```

## Referencia

| Comando | Descripcion |
|---------|-------------|
| `docker build -t nombre .` | Construye imagen desde Dockerfile |
| `docker run -d -p 8080:80 nombre` | Ejecuta contenedor en background |
| `docker ps` | Lista contenedores activos |
| `docker ps -a` | Lista todos los contenedores |
| `docker images` | Lista imagenes locales |
| `docker stop <id>` | Detiene un contenedor |
| `docker rm <id>` | Elimina un contenedor |
| `docker compose up -d` | Levanta servicios definidos en YAML |
| `docker compose down` | Detiene y elimina servicios |
| `docker logs <id>` | Muestra logs del contenedor |

## Ejercicios

1. **Dockerfile**: Escribe un Dockerfile para una app Python simple.
2. **Docker Compose**: Define servicios (web + db) con docker-compose.yml.
3. **Puertos y volumenes**: Ejecuta un contenedor mapeando puertos y montando un volumen.

**Ejecuta**: `python scripts/runner.py 10 02 [N]`  
**Con pistas**: `python scripts/runner.py 10 02 [N] -p [1-3]`
