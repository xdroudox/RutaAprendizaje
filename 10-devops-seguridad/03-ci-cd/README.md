# 03 - CI/CD

## Glosario

- **Build**: proceso de compilar, empaquetar y verificar que el codigo fuente funcione.
- **CD (Continuous Deployment / Despliegue Continuo)**: cada cambio que pasa CI se despliega automaticamente a produccion.
- **CI (Continuous Integration / Integracion Continua)**: integrar codigo frecuentemente, ejecutando builds y tests automaticos.
- **Deploy / Despliegue**: publicar una nueva version de la aplicacion en un entorno (dev, staging, produccion).
- **GitHub Actions**: plataforma CI/CD integrada en GitHub que usa workflows basados en YAML.
- **Job**: unidad de trabajo dentro de un workflow (puede contener multiples steps).
- **Linter**: herramienta que analiza el codigo en busca de errores, malas practicas o estilo inconsistente.
- **Pipeline**: secuencia automatizada de etapas (build → test → deploy).
- **Runner**: maquina que ejecuta los jobs de GitHub Actions (ubuntu-latest, windows-latest, self-hosted).
- **Step**: accion individual dentro de un job (ej: checkout, instalar dependencias, ejecutar tests).

## Conceptos clave

- **CI (Integracion Continua)**: los desarrolladores integran codigo varias veces al dia. Cada integracion es verificada con build automatico y tests. Si algo falla, se detecta al instante.
- **CD (Despliegue Continuo)**: una vez que el codigo pasa CI, se despliega automaticamente a produccion sin intervencion manual. Reduce el tiempo entre escribir codigo y que los usuarios lo vean.
- **Workflow de GitHub Actions**: archivo YAML en `.github/workflows/` que define uno o mas jobs. Se dispara con eventos (`push`, `pull_request`, `schedule`).
- **Jobs y dependencias**: los jobs se ejecutan en paralelo por defecto. Con `needs:` puedes secuenciarlos (ej: deploy solo si test pasa).
- **Estrategias de deploy**: blue-green, rolling update, canary releases. GitHub Actions permite integrar con AWS, Azure, GCP, Docker Hub, etc.

## Comparativa

| Aspecto | GitHub Actions | GitLab CI/CD | Jenkins |
|---------|---------------|--------------|---------|
| Configuracion | YAML en `.github/workflows/` | YAML (`.gitlab-ci.yml`) | Groovy (Jenkinsfile) o UI |
| Hosting | GitHub (nube) | GitLab (nube o self-hosted) | Self-hosted |
| Runners | ubuntu, windows, macos | linux, windows, macos | Cualquier SO |
| Facilidad de uso | Alta | Media | Baja (curva alta) |
| Ecosistema | Marketplace de acciones | CI integrado con repos | Muchos plugins |

| Lenguaje | Test | Linter | Build tool |
|----------|------|--------|------------|
| Python | `pytest` | `ruff` | `pip` / `poetry` |
| Java | `mvn test` | `checkstyle` / `pmd` | `mvn package` |
| JavaScript | `npm test` | `eslint` | `npm run build` |

## Ejemplo guiado

**Objetivo**: crear un workflow de GitHub Actions que ejecute tests y despliegue automaticamente.

```yaml
# .github/workflows/ci.yml
name: CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: pytest
      - run: pip install ruff && ruff check .
  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - run: echo "Desplegando a produccion..."
```

## Referencia

| Concepto | Sintaxis / Ejemplo |
|----------|-------------------|
| Trigger por push | `on: push: branches: [main]` |
| Trigger por PR | `on: pull_request: branches: [main]` |
| Trigger manual | `on: workflow_dispatch` |
| Trigger programado | `on: schedule: - cron: '0 6 * * *'` |
| Job con steps | `jobs: test: runs-on: ubuntu-latest steps:` |
| Dependencia entre jobs | `deploy: needs: test` |
| Condicion | `if: github.ref == 'refs/heads/main'` |
| Accion oficial | `uses: actions/checkout@v4` |
| Variables de entorno | `env: MY_VAR: value` |
| Secretos | `${{ secrets.MY_SECRET }}` |

## Ejercicios

1. **Workflow basico**: Crea un workflow YAML con build y test para Python.
2. **Agregar linting**: Anade un paso de linting al workflow.
3. **Deploy a produccion**: Crea un pipeline CI/CD completo con deploy condicional.

**Ejecuta**: `python scripts/runner.py 10 03 [N]`  
**Con pistas**: `python scripts/runner.py 10 03 [N] -p [1-3]`
