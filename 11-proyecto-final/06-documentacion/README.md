# 06 - Documentacion

## Objetivo

Crear la documentacion completa del proyecto Task Manager, incluyendo la especificacion OpenAPI/Swagger de la API, un README principal del proyecto, y una guia de despliegue para produccion.

## Requisitos

- Documentacion de la API con OpenAPI 3.0 (Swagger) que incluya todos los endpoints, modelos de datos, esquemas de peticion/respuesta y ejemplos
- Interfaz Swagger UI accesible desde el navegador en entorno de desarrollo
- README.md principal en la raiz del proyecto con: descripcion, tecnologias usadas, instrucciones de instalacion y ejecucion, estructura del proyecto, y enlaces a documentacion adicional
- Archivo de configuracion de postman o insomnia con las colecciones de peticiones (opcional)
- Guia de despliegue en produccion que incluya: requisitos del servidor, variables de entorno necesarias, pasos para desplegar con docker-compose en un VPS, configuracion de dominio y SSL con Let's Encrypt y Nginx reverse proxy
- La guia de despliegue debe estar en un archivo DEPLOY.md en la raiz del proyecto

## Pasos sugeridos

1. Anotar los endpoints de la API con decoradores/etiquetas de OpenAPI (en FastAPI es automatico; en Spring Boot usa springdoc-openapi)
2. Verificar que Swagger UI se carga correctamente en /swagger-ui.html o /docs
3. Escribir el README.md principal del proyecto
4. Escribir la guia de despliegue DEPLOY.md
5. (Opcional) Exportar coleccion de Postman/Insomnia con todas las peticiones
6. Revisar que toda la documentacion sea clara y completa

## Checklist

- [ ] Documentacion OpenAPI completa con todos los endpoints
- [ ] Swagger UI accesible y funcional
- [ ] README.md principal creado con toda la informacion necesaria
- [ ] DEPLOY.md con guia de despliegue en produccion
- [ ] Variables de entorno documentadas
- [ ] Instrucciones de instalacion claras y probadas
- [ ] (Opcional) Coleccion de Postman/Insomnia exportada

## Tips

- Si usas Spring Boot, agrega la dependencia springdoc-openapi-starter-webmvc-ui y accede a /swagger-ui.html
- Si usas FastAPI, la documentacion OpenAPI se genera automaticamente en /docs y /redoc
- En el README incluye una seccion de "Requisitos previos" (Docker, Node.js, Java/Python, etc.)
- En el DEPLOY.md especifica claramente los pasos para configurar un servidor Ubuntu/Debian desde cero
- Para SSL, recomienda Certbot con Let's Encrypt y Nginx como reverse proxy
- Incluye ejemplos de archivos .env para desarrollo y produccion

## Recursos

- OpenAPI Specification: https://swagger.io/specification/
- Swagger UI: https://swagger.io/tools/swagger-ui/
- Springdoc OpenAPI: https://springdoc.org/
- FastAPI Automatic Docs: https://fastapi.tiangolo.com/features/#automatic-docs
- Let's Encrypt: https://letsencrypt.org/
- Certbot: https://certbot.eff.org/
