# MVC, Repository e Inyeccion de Dependencias

## MVC (Model-View-Controller)

Separa logica de negocio (Modelo), presentacion (Vista) y control (Controlador).

## Repository

Abstrae el acceso a datos con una interfaz de coleccion.

```java
interface RepositorioUsuario {
    Usuario guardar(Usuario u);
    List<Usuario> listar();
}
```

## Inyeccion de Dependencias

Las dependencias se pasan desde fuera, no se crean internamente.

```java
class ServicioUsuario {
    private RepositorioUsuario repo;
    public ServicioUsuario(RepositorioUsuario repo) {
        this.repo = repo;  // Inyectado!
    }
}
```

## Ejercicios

1. **Crear modelo Usuario, repositorio en memoria, controlador**
   **Ejecuta:** `python scripts/runner.py 8 4 1`

2. **Vista simple que muestra datos del modelo**
   **Ejecuta:** `python scripts/runner.py 8 4 2`

3. **Inyectar dependencia (Repository) en Service**
   **Ejecuta:** `python scripts/runner.py 8 4 3`
