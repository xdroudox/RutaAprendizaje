# 01 - Git Avanzado

## Glosario

- **Branch / Rama**: linea independiente de desarrollo dentro de un repositorio.
- **Checkout**: cambiar entre ramas o restaurar archivos de un commit especifico.
- **Commit**: punto de control que guarda el estado del proyecto en un momento dado.
- **Conflict / Conflicto**: cuando dos ramas modifican la misma linea de un archivo y git no puede fusionarlas automaticamente.
- **HEAD**: puntero que indica en que commit estas parado actualmente.
- **Merge**: fusionar los cambios de una rama en otra.
- **Rebase**: reubicar los commits de una rama sobre la punta de otra, reescribiendo el historial.
- **Remote / Remoto**: repositorio alojado en un servidor externo (GitHub, GitLab, etc.).
- **Staging Area / Index**: area intermedia donde preparas archivos antes de confirmarlos.
- **Stash**: guardar cambios temporales sin hacer commit para trabajar en otra cosa.

## Conceptos clave

- **Flujo basico de trabajo**: working directory → `git add` → staging area → `git commit` → historial. Cada commit es un snapshot que puedes recuperar en cualquier momento.
- **Trabajo con ramas**: las ramas permiten desarrollar features, corregir bugs o experimentar sin afectar la rama principal. Crear una rama es instantaneo y liviano porque solo es un puntero a un commit.
- **Merge vs Rebase**: `merge` crea un commit extra de fusion y preserva el historial completo; `rebase` reescribe el historial para que parezca lineal, pero no se recomienda en ramas compartidas.
- **Resolucion de conflictos**: cuando ocurre un conflicto, git marca el archivo con marcadores `<<<<<<<`, `=======`, `>>>>>>>`. Debes editar el archivo, elegir que cambios conservar, luego `git add` y `git commit`.
- **Git en equipo**: ademas de merge y rebase, se usan `pull`, `push`, `fetch` y `pull requests` para colaborar en repositorios remotos.

## Comparativa

| Concepto | Git | SVN | Mercurial |
|----------|-----|-----|-----------|
| Modelo | Distribuido | Centralizado | Distribuido |
| Ramas | Livianas, son solo punteros | Copias de directorios | Livianas |
| Commit local | Si, sin conexion | No, necesita servidor | Si |
| Popularidad | Muy alta | Baja (legado) | Baja |
| Sintaxis basica | `git commit -m "msg"` | `svn commit -m "msg"` | `hg commit -m "msg"` |

| Accion | Python (poetry) | Java (Maven) | JavaScript (npm) |
|--------|----------------|--------------|------------------|
| Inicializar proyecto | `poetry new proy` | `mvn archetype:generate` | `npm init` |
| Agregar dependencia | `poetry add flask` | agregar en pom.xml | `npm install express` |
| Versionado comun | git + GitHub | git + GitHub | git + GitHub/NPM |

## Ejemplo guiado

**Objetivo**: crear un repositorio, agregar un archivo, hacer commit, crear una rama y fusionarla.

```bash
# Paso 1: Inicializar repositorio
mkdir mi-proyecto
cd mi-proyecto
git init

# Paso 2: Crear archivo y hacer primer commit
echo "# Mi proyecto" > README.md
git add README.md
git commit -m "Primer commit"

# Paso 3: Crear rama feature y trabajar en ella
git checkout -b feature/mejora
echo "print('Hola')" > app.py
git add app.py
git commit -m "Agrega app.py"

# Paso 4: Volver a main y fusionar
git checkout main
git merge feature/mejora

# Ver historial
git log --oneline --graph --all
```

## Referencia

| Comando | Descripcion |
|---------|-------------|
| `git init` | Inicializa un repositorio vacio |
| `git add <archivo>` | Agrega archivos al staging area |
| `git commit -m "mensaje"` | Confirma los cambios en el historial |
| `git status` | Muestra el estado del working directory |
| `git log --oneline --graph` | Muestra historial resumido con grafico de ramas |
| `git checkout -b <rama>` | Crea y cambia a una nueva rama |
| `git merge <rama>` | Fusiona una rama en la actual |
| `git diff` | Muestra diferencias sin stage |
| `git stash` | Guarda cambios temporales |
| `git remote add origin <url>` | Conecta repositorio local con remoto |

## Ejercicios

1. **Init, add y commit**: Crea un repositorio y realiza tu primer commit.
2. **Ramas y merge**: Crea ramas, haz cambios y fusiona.
3. **Resolver conflicto**: Simula y resuelve un conflicto de merge.

**Ejecuta**: `python scripts/runner.py 10 01 [N]`  
**Con pistas**: `python scripts/runner.py 10 01 [N] -p [1-3]`
