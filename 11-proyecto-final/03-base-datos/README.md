# 03 - Base de Datos y Migraciones

## Objetivo

Disenar el esquema de base de datos relacional para la aplicacion Task Manager y crear las migraciones SQL necesarias para inicializar y versionar la base de datos.

## Requisitos

- Usar PostgreSQL como motor de base de datos
- Tabla `usuarios` con campos: id (UUID o SERIAL), nombre_usuario, email, contrasena_hash, fecha_creacion, fecha_actualizacion
- Tabla `tareas` con campos: id (UUID o SERIAL), titulo, descripcion, completada (boolean, default false), categoria, etiquetas (array de texto o tabla separada), usuario_id (FK a usuarios), fecha_creacion, fecha_actualizacion
- Relacion: un usuario tiene muchas tareas (one-to-many)
- Indices apropiados para busquedas frecuentes (email en usuarios, usuario_id y categoria en tareas)
- Migraciones SQL versionadas (archivos con numeros secuenciales: 001_crear_usuarios.sql, 002_crear_tareas.sql, etc.)
- Script de seed data para desarrollo con datos de ejemplo
- Restricciones de integridad: NOT NULL donde corresponda, UNIQUE en email y nombre_usuario, FK con ON DELETE CASCADE

## Pasos sugeridos

1. Disenar el esquema entidad-relacion en papel o con una herramienta (dbdiagram.io, draw.io)
2. Crear la migracion 001 con la tabla usuarios
3. Crear la migracion 002 con la tabla tareas y sus relaciones
4. Crear la migracion 003 con indices adicionales
5. Crear un script de seed con datos de ejemplo (2-3 usuarios, 5-10 tareas cada uno)
6. Crear un script de rollback para cada migracion (opcional pero recomendado)
7. Probar las migraciones ejecutandolas en orden contra una base de datos local

## Checklist

- [ ] Esquema de base de datos disenado
- [ ] Migracion 001: tabla usuarios creada con campos correctos
- [ ] Migracion 002: tabla tareas creada con FK a usuarios
- [ ] Migracion 003: indices creados para optimizar busquedas
- [ ] Restricciones UNIQUE en email y nombre_usuario
- [ ] Restriccion FK con ON DELETE CASCADE
- [ ] Script de seed con datos de ejemplo funcional
- [ ] Todas las migraciones se ejecutan sin errores
- [ ] Rollback scripts disponibles (opcional)

## Tips

- Usa UUID como clave primaria para evitar problemas de seguridad con IDs secuenciales
- Para las migraciones puedes hacerlas manualmente con archivos SQL, o con herramientas como Flyway, Liquibase o Alembic (si usas Python)
- El tipo ARRAY en PostgreSQL es util para las etiquetas, pero tambien puedes crear una tabla intermedia tareas_etiquetas si prefieres normalizar
- Incluye los campos fecha_creacion y fecha_actualizacion en todas las tablas con DEFAULT NOW() y triggers o logica de aplicacion para actualizar
- Prueba las migraciones tanto hacia adelante como hacia atras (rollback)

## Recursos

- Documentacion de PostgreSQL: https://www.postgresql.org/docs/
- Flyway: https://flywaydb.org/
- Liquibase: https://www.liquibase.com/
- dbdiagram.io: https://dbdiagram.io/
