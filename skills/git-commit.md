---
name: git-commit
description: Creates conventional commits with bilingual (EN/ES) messages. Run this at the end of any work session to commit changes with proper conventional commit naming, a single-sentence description, and an explanation of the reasoning behind the change.
---

# Git Commit Skill

Generates professional commits siguiendo **Conventional Commits** con descripcion bilingue (ingles/espanol), mas una seccion de razon del cambio.

## Cuando usar esta skill

Al final de cualquier sesion de trabajo donde hayas hecho cambios en el repositorio y necesites comitear.

## Formato del commit

```
tipo(scope): descripcion del cambio

Razon: explicacion de por que se hizo el cambio
```

## Tipos de commit (Conventional Commits)

| Tipo | Cuando usarlo |
|------|---------------|
| `feat` | Nueva funcionalidad |
| `fix` | Correccion de bug |
| `docs` | Cambios en documentacion |
| `refactor` | Refactorizacion sin cambiar funcionamiento |
| `chore` | Mantenimiento, configuracion, tareas |
| `style` | Cambios de formato, estilo |
| `test` | Agregar o modificar tests |
| `perf` | Mejoras de rendimiento |

## Instrucciones

### Paso 1: Revisar cambios

Ejecuta los siguientes comandos para entender que se modifico:

```bash
git status
git diff --stat
```

### Paso 2: Identificar el tipo y scope

- Determina el **tipo** segun la tabla de arriba
- Determina el **scope** (el modulo/area afectada, ej: `nivel1`, `runner`, `README`)

### Paso 3: Construir versiones del mensaje

Redacta DOS versiones en UNA SOLA ORACION cada una:

- **Version EN**: en ingles
- **Version ES**: en espanol

Ejemplos:

- Version EN: `feat(nivel5): add JWT authentication exercises`
  Version ES: `feat(nivel5): agrega ejercicios de autenticacion JWT`
- Version EN: `fix(runner): resolve encoding error on Windows terminal`
  Version ES: `fix(runner): corrige error de encoding en terminal Windows`
- Version EN: `docs(roadmap): update skills tree with completed modules`
  Version ES: `docs(roadmap): actualiza arbol de habilidades con modulos completados`

### Paso 4: Agregar la razon del cambio

Anade una linea `Razon:` que explique brevemente POR QUE se hizo el cambio (contexto, problema que resuelve, decision arquitectonica).

### Paso 5: Preguntar al usuario

Muestra las dos versiones al usuario con la razon y preguntale:
- Que version prefiere (EN o ES)?
- Si esta de acuerdo con el mensaje y la razon?

Usa la herramienta `question` para esto.

### Paso 6: Staging y commit

Una vez que el usuario apruebe, ejecuta:

```bash
git add .
git commit -m "tipo(scope): descripcion aprobada

Razon: explicacion breve del por que"
```

Usa `git add .` en vez de `git add -A` a menos que haya archivos eliminados intencionalmente. Si los hay, preguntale al usuario si debe stagear las eliminaciones.

## Ejemplo de interaccion

```
Usuario: haz el commit de estos cambios
Asistente: [revisa cambios y propone]

Version EN: `refactor(roadmap): restructure exercises across all modules`
Version ES: `refactor(roadmap): reestructura ejercicios en todos los modulos`

Razon: simplificar los ejercicios para enfocarse en conceptos clave

Que version prefieres y estas de acuerdo?
```

## Notas

- Las versiones EN y ES se muestran por separado para que el usuario elija
- NO combinar idiomas en una sola linea con `|`
- Esperar la aprobacion del usuario antes de ejecutar el commit
- Si hay archivos eliminados, preguntar si debe incluirse en el stage
- Si hay multiples cambios no relacionados, separa en commits independientes
- La razon explica el contexto, no repite lo que ya dice el mensaje
