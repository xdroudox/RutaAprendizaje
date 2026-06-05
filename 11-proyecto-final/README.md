# Nivel 11 - Proyecto Final: Task Manager API + Frontend

## Objetivo

Construir una aplicacion full-stack de gestion de tareas (Task Manager) que integre todos los conocimientos adquiridos en los niveles anteriores. El proyecto incluye una API RESTful con autenticacion JWT, un frontend web que consume la API, una base de datos relacional, contenerizacion con Docker, un pipeline de tests y documentacion completa.

## Estructura del proyecto

```
11-proyecto-final/
├── 01-api-restful/        # Especificacion de la API REST
├── 02-frontend-app/       # Especificacion del frontend
├── 03-base-datos/         # Diseno de esquema y migraciones SQL
├── 04-docker-compose/     # Configuracion Docker y docker-compose
├── 05-tests/              # Estrategia de pruebas
└── 06-documentacion/      # Documentacion OpenAPI, README y guia de despliegue
```

## Sub-modulos

Cada sub-modulo contiene un archivo README.md con lineamientos y especificaciones que debes seguir para construir la aplicacion completa. No son ejercicios paso a paso, sino guias que definen los requisitos y te orientan en la implementacion.

## Requisitos generales

- Todo el codigo debe estar en un repositorio Git con commits frecuentes y descriptivos
- El proyecto debe ejecutarse completamente con `docker-compose up`
- La API debe estar documentada con OpenAPI/Swagger
- El frontend debe ser responsivo y funcional
- Los tests deben cubrir al menos los casos de uso principales
- El codigo debe seguir buenas practicas: principios SOLID, clean code, manejo de errores

## Checklist del nivel

- [ ] API RESTful con JWT implementada y funcional
- [ ] Frontend que consume la API y permite gestionar tareas
- [ ] Base de datos con migraciones y seed data
- [ ] Docker-compose funcionando con todos los servicios
- [ ] Suite de tests (unitarios, integracion, e2e)
- [ ] Documentacion completa (OpenAPI, README, guia de despliegue)
