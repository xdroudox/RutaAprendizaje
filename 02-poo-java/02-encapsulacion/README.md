# Encapsulacion

## Teoria

La encapsulacion protege los datos de un objeto ocultando su implementacion interna. Se logra usando modificadores de acceso (private) y metodos publicos (getters/setters).

### Modificadores de acceso

| Modificador | Acceso desde la misma clase | Acceso desde el mismo paquete | Acceso desde subclases | Acceso desde cualquier lugar |
|------------|:---------------------------:|:-----------------------------:|:----------------------:|:---------------------------:|
| private | Si | No | No | No |
| default | Si | Si | No | No |
| protected | Si | Si | Si | No |
| public | Si | Si | Si | Si |

### Getters y Setters

Los getters obtienen el valor de un atributo privado. Los setters permiten modificarlo con validaciones.

```java
public class Persona {
    private int edad;

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        if (edad >= 0) {
            this.edad = edad;
        }
    }
}
```

### Beneficios

- Control sobre la modificacion de datos (validaciones)
- Ocultacion de la implementacion interna
- Mayor seguridad y mantenibilidad

## Ejercicios

### Ejercicio 1: CuentaBancaria
Crea una clase con saldo private, getter y setter con validacion (no negativos).

**Ejecuta:** `python scripts/runner.py 2 2 1`

### Ejercicio 2: Producto
Crea una clase Producto con precio private. El setter debe rechazar precios negativos.

**Ejecuta:** `python scripts/runner.py 2 2 2`

### Ejercicio 3: Estudiante
Crea una clase Estudiante con notas private (double[]). Incluye metodo promedio().

**Ejecuta:** `python scripts/runner.py 2 2 3`

## Soluciones

```bash
python scripts/runner.py 2 2 1 -s
python scripts/runner.py 2 2 2 -s
python scripts/runner.py 2 2 3 -s
```
