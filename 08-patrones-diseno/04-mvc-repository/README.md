# MVC, Repository e Inyeccion de Dependencias

## MVC (Model-View-Controller)

**Intencion:** Separar la logica de negocio (Modelo) de la presentacion (Vista) a traves de un controlador que gestiona la interaccion.

**Problema:** El codigo de interfaz de usuario se mezcla con la logica de negocio, haciendo el sistema dificil de mantener y probar.

**Estructura:**
- **Modelo**: Datos y logica de negocio
- **Vista**: Presentacion al usuario (consola en este caso)
- **Controlador**: Maneja entrada del usuario, actualiza el modelo y la vista

**Cuando usar:**
- Cuando necesitas separar responsabilidades en una aplicacion con interfaz de usuario
- Cuando quieres que la logica de negocio sea independiente de la presentacion

## Repository

**Intencion:** Abstraer el acceso a datos, proporcionando una interfaz de coleccion para las entidades del dominio.

**Problema:** El codigo de acceso a datos esta disperso y acoplado a la fuente de datos especifica.

**Estructura:**
- Interfaz Repository con metodos CRUD (create, read, update, delete)
- Implementacion concreta del repositorio (en memoria, JDBC, JPA, etc.)

**Cuando usar:**
- Cuando necesitas abstraer el almacenamiento de datos
- Cuando quieres cambiar la fuente de datos sin afectar la logica de negocio

## Inyeccion de Dependencias

**Intencion:** Proporcionar las dependencias a una clase desde el exterior, en lugar de que la clase las cree por si misma.

**Problema:** Las clases crean sus propias dependencias, generando acoplamiento fuerte y dificultando las pruebas.

**Tipos:**
- Constructor Injection: se pasan por el constructor
- Setter Injection: se asignan via setters
- Interface Injection: se pasan via un metodo de interfaz

**Ejemplo:**
```java
// Sin DI
class Servicio {
    private Repositorio repo = new RepositorioMemoria();
}

// Con DI
class Servicio {
    private Repositorio repo;
    public Servicio(Repositorio repo) { this.repo = repo; }
}
```

## Ejecuta

```
javac Ejercicios.java && java Ejercicios 1
javac Ejercicios.java && java Ejercicios 1 -p
javac Ejercicios.java && java Ejercicios -s 1
```
