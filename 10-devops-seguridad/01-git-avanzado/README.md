# 01 - Git Avanzado

## Conceptos clave

- **Branching**: ramas para desarrollo paralelo.
- **Merge**: integrar cambios de una rama a otra.
- **Rebase**: reubicar commits sobre otra base.
- **Conflictos**: cuando dos cambios modifican la misma linea.
- **Stash**: guardar cambios temporalmente.
- **Cherry-pick**: aplicar commits especificos.

## Flujo recomendado

1. Crear una rama por feature (`git checkout -b feature/nueva`).
2. Trabajar y commitear.
3. Actualizar con main (`git rebase main` o `git merge main`).
4. Resolver conflictos si existen.
5. Fusionar a main con `git merge --no-ff`.
