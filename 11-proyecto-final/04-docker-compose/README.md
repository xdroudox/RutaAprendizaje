# 04 - Docker y Docker Compose

## Objetivo

Contenerizar toda la aplicacion Task Manager utilizando Docker y orquestar los servicios con docker-compose para que el proyecto se ejecute con un solo comando.

## Requisitos

- Dockerfile para la API (backend) optimizado para produccion (multi-stage build)
- Dockerfile para el frontend servido con Nginx (o servidor similar)
- Servicio de PostgreSQL en docker-compose
- Servicio de la API con dependencia del servicio de base de datos
- Servicio del frontend con dependencia del servicio de la API
- Volumen persistente para los datos de PostgreSQL
- Variables de entorno configuradas via docker-compose (.env file)
- Red interna para la comunicacion entre servicios (api, frontend, db)
- Puerto mapeado para el frontend (80) y la API (8080 o 8000)
- Healthcheck para el servicio de base de datos
- Optimizacion de capas en los Dockerfiles para reducir el tamano de las imagenes

## Pasos sugeridos

1. Crear el Dockerfile para la API (multi-stage: build + runtime)
2. Crear el Dockerfile para el frontend (build static files + servirlos con Nginx)
3. Crear el archivo .env con las variables de entorno necesarias
4. Crear el archivo docker-compose.yml con los tres servicios
5. Configurar los healthchecks y dependencias entre servicios
6. Probar que `docker-compose up` levanta toda la aplicacion correctamente
7. Probar que los datos persisten tras detener y re-iniciar los contenedores

## Checklist

- [ ] Dockerfile de la API funcional y optimizado
- [ ] Dockerfile del frontend funcional con Nginx
- [ ] docker-compose.yml con los 3 servicios (db, api, frontend)
- [ ] Variables de entorno configuradas en .env
- [ ] Volumen persistente para PostgreSQL
- [ ] Red interna configurada
- [ ] Healthcheck para PostgreSQL
- [ ] Multi-stage build implementado
- [ ] Aplicacion funciona completamente con `docker-compose up`
- [ ] Datos persistentes entre reinicios

## Tips

- Usa .dockerignore para excluir archivos innecesarios (node_modules, .git, etc.) y reducir el contexto de build
- Para el multi-stage build en Java: usa una imagen maven/gradle para compilar y una imagen jre ligera para ejecutar
- Para el multi-stage build en Python: usa una imagen pip/poetry para instalar dependencias y una imagen slim para ejecutar
- El frontend en React/Vue se construye a archivos estaticos y se sirven con Nginx, no necesitas Node en produccion
- Usa la directiva `depends_on` con `condition: service_healthy` para asegurar que la base de datos este lista antes que la API

## Recursos

- Documentacion de Docker: https://docs.docker.com/
- Documentacion de Docker Compose: https://docs.docker.com/compose/
- Multi-stage builds: https://docs.docker.com/build/building/multi-stage/
- Docker best practices: https://docs.docker.com/develop/dev-best-practices/
