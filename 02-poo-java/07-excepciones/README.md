# Excepciones

## Teoria

Las excepciones son eventos que interrumpen el flujo normal del programa. Java proporciona mecanismos para manejarlas.

### try/catch

El bloque try contiene el codigo que puede lanzar una excepcion. El bloque catch la captura y la maneja.

```java
try {
    int resultado = 10 / 0;
} catch (ArithmeticException e) {
    System.out.println("No se puede dividir por cero");
}
```

### throws

La palabra clave `throws` declara que un metodo puede lanzar una excepcion.

```java
void leerArchivo() throws IOException {
    // codigo que puede lanzar IOException
}
```

### Excepciones personalizadas

Se crean extendiendo la clase Exception.

```java
class EdadInvalidaException extends Exception {
    EdadInvalidaException(String mensaje) {
        super(mensaje);
    }
}
```

### Jerarquia de excepciones

- **Throwable** (clase raiz)
  - **Exception** (excepciones recuperables)
    - RuntimeException (errores de programa)
    - IOException (errores de E/S)
  - **Error** (errores graves, no recuperables)

## Ejercicios

### Ejercicio 1: Division con try/catch
Captura ArithmeticException al dividir por cero.

**Ejecuta:** `python scripts/runner.py 2 7 1`

### Ejercicio 2: NumberFormatException
Captura error al convertir string a int con Integer.parseInt().

**Ejecuta:** `python scripts/runner.py 2 7 2`

### Ejercicio 3: Excepcion personalizada
Crea EdadInvalidaException para validar edad entre 1 y 150.

**Ejecuta:** `python scripts/runner.py 2 7 3`

## Soluciones

```bash
python scripts/runner.py 2 7 1 -s
python scripts/runner.py 2 7 2 -s
python scripts/runner.py 2 7 3 -s
```
