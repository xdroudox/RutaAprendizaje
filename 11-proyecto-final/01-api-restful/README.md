# 01 - API RESTful con Autenticacion JWT

## Objetivo

Construir una API RESTful para la aplicacion Task Manager que permita registro de usuarios, inicio de sesion con JWT y operaciones CRUD sobre tareas. Puedes elegir entre Java Spring Boot o Python FastAPI como tecnologia principal.

## Requisitos

- Endpoint de registro de usuario (POST /api/auth/register)
- Endpoint de inicio de sesion (POST /api/auth/login) que retorna un token JWT
- Middleware de autenticacion JWT para proteger los endpoints de tareas
- CRUD completo de tareas: GET /api/tasks, POST /api/tasks, GET /api/tasks/{id}, PUT /api/tasks/{id}, DELETE /api/tasks/{id}
- Las tareas deben pertenecer a un usuario (relacion many-to-one)
- Las tareas deben tener: id, titulo, descripcion, completada (booleano), categoria, etiquetas, fecha de creacion, fecha de actualizacion
- Endpoint para filtrar tareas por categoria y por estado (completada/pendiente)
- Manejo de errores con codigos HTTP apropiados (400, 401, 403, 404, 500)
- Validacion de datos de entrada en todos los endpoints
- Paginacion en el listado de tareas

## Pasos sugeridos

1. Inicializar el proyecto con tu tecnologia elegida (Spring Initializr o FastAPI con poetry/pip)
2. Configurar la conexion a la base de datos (PostgreSQL recomendado)
3. Crear el modelo de Usuario con los campos necesarios
4. Implementar el registro de usuario con hash de contrasena (bcrypt)
5. Implementar el inicio de sesion y generacion de tokens JWT
6. Crear el modelo de Tarea con relaciones y validaciones
7. Implementar los endpoints CRUD para tareas
8. Agregar el middleware de autenticacion JWT
9. Agregar filtros, paginacion y ordenamiento
10. Implementar manejo de errores global
11. Probar manualmente con Postman/Insomnia o con tests automatizados

## Checklist

- [ ] Proyecto inicializado con la tecnologia elegida
- [ ] Modelo de Usuario implementado
- [ ] Endpoints de autenticacion funcionando (register/login)
- [ ] Token JWT generado y validado correctamente
- [ ] Modelo de Tarea implementado con validaciones
- [ ] CRUD de tareas protegido con JWT
- [ ] Filtros por categoria y estado funcionando
- [ ] Paginacion implementada
- [ ] Manejo de errores con codigos HTTP adecuados
- [ ] Codigo organizado en capas (controllers, services, repositories/models)

## Tips

- Usa variables de entorno para la configuracion (base de datos, secreto JWT, etc.)
- Para JWT en Spring Boot usa la libreria jjwt o spring-security; en FastAPI usa pyjwt
- El hash de contrasena: en Spring Boot usa BCryptPasswordEncoder; en FastAPI usa passlib con bcrypt
- Manten el secreto JWT en una variable de entorno, nunca hardcodeado
- Usa DTOs para las peticiones y respuestas, no expongas las entidades directamente

## Recursos

- Documentacion de Spring Boot: https://spring.io/projects/spring-boot
- Documentacion de FastAPI: https://fastapi.tiangolo.com/
- Documentacion de JWT: https://jwt.io/introduction
- Bcrypt: https://en.wikipedia.org/wiki/Bcrypt
