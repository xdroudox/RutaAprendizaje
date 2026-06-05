# 02 - Docker

## Conceptos clave

- **Imagen**: plantilla inmmutable para crear contenedores.
- **Contenedor**: instancia en ejecucion de una imagen.
- **Dockerfile**: receta para construir una imagen.
- **Volumen**: persistencia de datos fuera del contenedor.
- **Puertos**: mapeo de puertos host-contenedor.
- **Docker Compose**: orquestacion multi-contenedor.

## Comandos esenciales

| Comando | Descripcion |
|---------|-------------|
| `docker build -t nombre .` | Construir imagen |
| `docker run -p 8080:80 nombre` | Ejecutar contenedor |
| `docker ps` | Listar contenedores activos |
| `docker compose up -d` | Levantar servicios |
