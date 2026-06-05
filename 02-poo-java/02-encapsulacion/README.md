# Encapsulacion

## Teoria

La encapsulacion es el mecanismo que restringe el acceso directo a los atributos de una clase, protegiendo los datos y permitiendo su acceso solo a traves de metodos publicos (getters y setters).

### Modificadores de acceso

| Modificador | Clase | Paquete | Subclase | Mundo |
|-------------|-------|---------|----------|-------|
| `private` | Si | No | No | No |
| `default` | Si | Si | No | No |
| `protected` | Si | Si | Si | No |
| `public` | Si | Si | Si | Si |

### Ejemplo con encapsulacion

```java
public class Persona {
    private String nombre;
    private int edad;

    // Getter
    public String getNombre() {
        return nombre;
    }

    // Setter con validacion
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        if (edad > 0 && edad < 150) {
            this.edad = edad;
        }
    }
}
```

### JavaBeans Pattern

El patron JavaBeans establece convenciones para las clases:
- Atributos privados
- Constructor sin argumentos
- Getters y setters publicos
- Implementar Serializable (opcional)

```java
public class Producto {
    private String codigo;
    private double precio;

    public Producto() { }

    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        if (precio >= 0) {
            this.precio = precio;
        }
    }
}
```

## Ejercicios

### Ejercicio 1: Clase Empleado encapsulada
Crea una clase Empleado con atributos privados: nombre, salario y departamento. Implementa getters y setters con validacion: el salario no puede ser negativo ni el departamento vacio. En el main, crea un empleado, asigna valores y muestra los datos.

### Ejercicio 2: Clase Libro con validacion
Crea una clase Libro con atributos privados: titulo, autor, isbn, anioPublicacion. Los setters deben validar:
- titulo no vacio
- isbn debe tener 13 caracteres
- anioPublicacion no puede ser futuro

### Ejercicio 3: Sistema de Cuenta con JavaBeans
Crea una clase CuentaAhorros siguiendo el patron JavaBeans con: numeroCuenta, titular, saldo, tasaInteres. Incluye constructor sin argumentos, getters/setters, y un metodo `aplicarInteres()` que incremente el saldo segun la tasa.

### Ejecuta los ejercicios

```bash
javac Ejercicios.java && java Ejercicios
```
