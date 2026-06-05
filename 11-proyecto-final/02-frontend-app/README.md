# 02 - Frontend App

## Objetivo

Construir una interfaz de usuario web que consuma la API RESTful del modulo 01. Puedes usar HTML/CSS/JS vanilla o un framework como React. La aplicacion debe permitir registrarse, iniciar sesion y gestionar tareas (crear, leer, actualizar, eliminar).

## Requisitos

- Pantalla de registro con formulario (nombre de usuario, email, contrasena)
- Pantalla de inicio de sesion con formulario (email, contrasena)
- Almacenamiento del token JWT en localStorage o sessionStorage
- Envio del token JWT en el header Authorization para peticiones autenticadas
- Pantalla principal con listado de tareas del usuario autenticado
- Formulario para crear nuevas tareas (titulo, descripcion, categoria, etiquetas)
- Capacidad de marcar tareas como completadas/pendientes (toggle)
- Capacidad de editar tareas existentes
- Capacidad de eliminar tareas con confirmacion
- Filtros para mostrar tareas por categoria y por estado (completada/pendiente)
- Cierre de sesion que elimina el token y redirige al login
- Diseño responsivo (funciona en movil y escritorio)
- Manejo de errores de la API con mensajes para el usuario

## Pasos sugeridos

1. Elegir tecnologia (HTML/CSS/JS vanilla o React con Vite)
2. Crear la estructura basica del proyecto
3. Implementar los componentes/paginas de registro y login
4. Implementar la logica de almacenamiento y envio del token JWT
5. Implementar la pagina principal con listado de tareas
6. Implementar el formulario de creacion de tareas
7. Implementar la edicion y eliminacion de tareas
8. Agregar los filtros por categoria y estado
9. Agregar diseño responsivo con CSS (puedes usar Bootstrap, Tailwind o CSS propio)
10. Probar la integracion con la API

## Checklist

- [ ] Pantalla de registro funcional
- [ ] Pantalla de login funcional
- [ ] Token JWT almacenado y enviado correctamente
- [ ] Listado de tareas del usuario autenticado
- [ ] Creacion de tareas funcionando
- [ ] Edicion de tareas funcionando
- [ ] Eliminacion de tareas con confirmacion
- [ ] Toggle completada/pendiente funcionando
- [ ] Filtros por categoria y estado funcionando
- [ ] Cierre de sesion funcionando
- [ ] Diseño responsivo
- [ ] Manejo de errores visible para el usuario

## Tips

- Si usas React, organiza el estado global con Context API o useState + useEffect
- Para las peticiones HTTP puedes usar fetch nativo o axios
- Define una URL base de la API en una variable de entorno para facilitar el cambio entre desarrollo y produccion
- Muestra indicadores de carga (spinner/skeleton) mientras se esperan respuestas de la API
- Valida los formularios del lado del cliente antes de enviarlos a la API

## Recursos

- Documentacion de React: https://react.dev/
- Documentacion de Vite: https://vitejs.dev/
- Bootstrap: https://getbootstrap.com/
- Tailwind CSS: https://tailwindcss.com/
- Axios: https://axios-http.com/
