# MVC, Repository e Inyeccion de Dependencias

Arquitectura de software para separar responsabilidades y facilitar el mantenimiento.

## Conceptos Basicos

- **MVC (Model-View-Controller)**: patron arquitectonico que separa la aplicacion en tres componentes: Modelo (datos), Vista (presentacion), Controlador (logica).
- **Repository**: abstrae el acceso a datos con una interfaz similar a una coleccion. Oculta los detalles de persistencia.
- **Inyeccion de Dependencias (DI)**: las dependencias se pasan desde fuera en lugar de crearlas internamente. Facilita pruebas y desacoplamiento.

## Glosario

| Termino | Definicion |
|---------|-----------|
| **Modelo** | Representa los datos y la logica de negocio |
| **Vista** | Presenta los datos al usuario (consola, web, GUI) |
| **Controlador** | Maneja las entradas del usuario y actualiza el modelo/vista |
| **Repository** | Abstraccion que centraliza el acceso a datos |
| **Inyeccion de Dependencias** | Pasar dependencias por constructor en vez de crearlas internamente |
| **Acoplamiento** | Grado de dependencia entre componentes |
| **Cohesion** | Grado en que los elementos de un modulo estan relacionados |

## Comparativa entre Lenguajes

### Java (Repository + DI)
```java
interface RepositorioUsuario {
    Usuario guardar(Usuario u);
    List<Usuario> listar();
}

class ServicioUsuario {
    private RepositorioUsuario repo;
    public ServicioUsuario(RepositorioUsuario repo) {  // DI por constructor
        this.repo = repo;
    }
}
```

### Python (Repository + DI)
```python
class ServicioUsuario:
    def __init__(self, repo):  # DI por constructor
        self._repo = repo

    def registrar(self, nombre, email):
        return self._repo.guardar(nombre, email)
```

### JavaScript (Repository + DI)
```javascript
class ServicioUsuario {
    constructor(repo) {  // DI por constructor
        this.repo = repo;
    }
    registrar(nombre, email) {
        return this.repo.guardar(nombre, email);
    }
}
```

## Ejemplo Guiado: MVC completo con DI

Paso 1: Modelo
```java
class Usuario {
    private int id;
    private String nombre;
    private String email;
    // constructor, getters...
}
```

Paso 2: Repositorio (abstraccion de datos)
```java
interface RepositorioUsuario {
    Usuario guardar(String nombre, String email);
    java.util.List<Usuario> listar();
}

class RepositorioMemoria implements RepositorioUsuario {
    private java.util.Map<Integer, Usuario> datos = new java.util.HashMap<>();
    private int contador = 1;

    public Usuario guardar(String nombre, String email) {
        Usuario u = new Usuario(contador++, nombre, email);
        datos.put(u.getId(), u);
        return u;
    }
    public java.util.List<Usuario> listar() {
        return new java.util.ArrayList<>(datos.values());
    }
}
```

Paso 3: Servicio con DI
```java
class ServicioUsuario {
    private RepositorioUsuario repo;
    public ServicioUsuario(RepositorioUsuario repo) {  // Inyeccion!
        this.repo = repo;
    }
    public Usuario registrar(String nombre, String email) {
        return repo.guardar(nombre, email);
    }
    public java.util.List<Usuario> listar() {
        return repo.listar();
    }
}
```

Paso 4: Uso
```java
RepositorioUsuario repo = new RepositorioMemoria();
ServicioUsuario servicio = new ServicioUsuario(repo);  // DI
servicio.registrar("Ana", "ana@test.com");
servicio.listar();
```

## Referencia rapida

| Componente | Responsabilidad | Ejemplo |
|------------|----------------|---------|
| **Modelo** | Datos y reglas de negocio | `class Usuario { ... }` |
| **Vista** | Presentacion al usuario | `class VistaConsola { ... }` |
| **Controlador** | Coordina modelo y vista | `class ControladorUsuario { ... }` |
| **Repository** | Acceso a datos | `class RepositorioMemoria implements RepositorioUsuario` |
| **Servicio** | Logica de negocio con DI | `class ServicioUsuario(RepositorioUsuario repo)` |

## Ejercicios

**Ejecuta:** `python scripts/runner.py 8 4 [ejercicio] [-p N]`

1. 🟢 **MVC - Modelo Usuario, repositorio en memoria, controlador**
2. 🟡 **Vista simple que muestra datos del modelo**
3. 🟡 **Inyectar dependencia (Repository) en Service**
