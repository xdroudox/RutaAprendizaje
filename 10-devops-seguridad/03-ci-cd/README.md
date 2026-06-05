# 03 - CI/CD

## Conceptos clave

- **CI (Integracion Continua)**: integrar codigo frecuentemente con builds y tests automaticos.
- **CD (Despliegue Continuo)**: desplegar automaticamente a produccion tras pasar CI.
- **Pipeline**: secuencia de etapas (build, test, deploy).
- **GitHub Actions**: plataforma CI/CD integrada en GitHub.

## Estructura de un workflow YAML

```yaml
name: CI
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Instalar dependencias
        run: pip install -r requirements.txt
      - name: Ejecutar tests
        run: pytest
```
