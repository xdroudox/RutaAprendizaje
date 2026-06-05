# 05 - Estrategia de Pruebas

## Objetivo

Disenar e implementar una estrategia de pruebas completa para la aplicacion Task Manager, cubriendo tests unitarios, de integracion y end-to-end (e2e).

## Requisitos

- Tests unitarios para los servicios/modelos de la API (logica de negocio)
- Tests de integracion para los endpoints de la API (usando base de datos de prueba)
- Tests de integracion para la autenticacion JWT (registro, login, token invalido, expirado)
- Tests para el frontend (al menos los componentes principales o funciones)
- Test end-to-end que cubra el flujo completo: registro -> login -> crear tarea -> listar tareas -> marcar completada -> eliminar tarea
- Configuracion de base de datos de prueba separada (puede ser H2 en memoria para Java o SQLite para Python, o una base de datos PostgreSQL dedicada para tests)
- Los tests deben ejecutarse con un solo comando (por ejemplo: `mvn test`, `pytest`, `npm test`)
- Reporte de cobertura de codigo (opcional pero recomendado)

## Pasos sugeridos

1. Configurar el framework de tests para la API (JUnit 5 + Mockito para Java, pytest para Python)
2. Escribir tests unitarios para los servicios (logica de creacion de tareas, validaciones, etc.)
3. Escribir tests de integracion para los endpoints de autenticacion
4. Escribir tests de integracion para el CRUD de tareas
5. Configurar tests del frontend (Jest + React Testing Library para React, o pruebas manuales con cypress si es JS vanilla)
6. Escribir un test e2e con Playwright o Cypress que cubra el flujo completo
7. Ejecutar todos los tests y verificar que pasan
8. (Opcional) Configurar reporte de cobertura

## Checklist

- [ ] Framework de tests configurado para la API
- [ ] Tests unitarios de servicios/logica de negocio
- [ ] Tests de integracion de autenticacion
- [ ] Tests de integracion de CRUD de tareas
- [ ] Tests del frontend (componentes principales)
- [ ] Test e2e del flujo completo
- [ ] Base de datos de prueba configurada
- [ ] Todos los tests pasan correctamente
- [ ] Los tests se ejecutan con un solo comando

## Tips

- Usa una base de datos en memoria para los tests de integracion de la API (H2 para Java, motor SQLite para Python, o testcontainers para PostgreSQL real)
- Para los tests de la API con autenticacion, genera un token JWT de prueba en el setup de cada test
- Usa fixtures o factories para crear datos de prueba de manera rapida y consistente
- Para los tests e2e, asegurate de que la API y el frontend esten corriendo antes de ejecutarlos
- No tests de la base de datos real de desarrollo; usa siempre una base de datos separada para pruebas

## Recursos

- JUnit 5: https://junit.org/junit5/
- Mockito: https://site.mockito.org/
- pytest: https://docs.pytest.org/
- Jest: https://jestjs.io/
- React Testing Library: https://testing-library.com/react
- Playwright: https://playwright.dev/
- Cypress: https://www.cypress.io/
- Testcontainers: https://testcontainers.com/
