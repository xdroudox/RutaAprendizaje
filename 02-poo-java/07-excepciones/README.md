# Excepciones

## Teoria

Las excepciones son eventos que interrumpen el flujo normal de un programa. Java proporciona un mecanismo robusto para manejarlas.

### Jerarquia de excepciones

```
Object
  └── Throwable
       ├── Error (errores graves, no recuperables)
       │    ├── OutOfMemoryError
       │    └── StackOverflowError
       └── Exception (recuperables)
            ├── RuntimeException (unchecked)
            │    ├── NullPointerException
            │    ├── ArithmeticException
            │    ├── ArrayIndexOutOfBoundsException
            │    └── IllegalArgumentException
            └── Otras (checked)
                 ├── IOException
                 ├── SQLException
                 └── ClassNotFoundException
```

### Checked vs Unchecked

| Tipo | Checked | Unchecked |
|------|---------|-----------|
| Verificacion | En compilacion | En ejecucion |
| Obligatorio | Si (try-catch o throws) | No |
| Heredan de | Exception (no RuntimeException) | RuntimeException |
| Ejemplos | IOException, SQLException | NullPointerException, ArithmeticException |

### try-catch-finally

```java
try {
    int resultado = 10 / 0;
} catch (ArithmeticException e) {
    System.out.println("Error: " + e.getMessage());
} finally {
    System.out.println("Bloque finally siempre se ejecuta");
}
```

### Multi-catch (Java 7+)

```java
try {
    // codigo que puede lanzar multiples excepciones
} catch (IOException | SQLException e) {
    System.out.println("Error de E/S o BD: " + e.getMessage());
}
```

### throws

Declara que un metodo puede lanzar una excepcion checked.

```java
public void leerArchivo(String ruta) throws IOException {
    FileReader fr = new FileReader(ruta);
    // ...
}
```

### throw

Lanza una excepcion manualmente.

```java
public void setEdad(int edad) {
    if (edad < 0 || edad > 150) {
        throw new IllegalArgumentException("Edad invalida: " + edad);
    }
    this.edad = edad;
}
```

### Custom exceptions

```java
class SaldoInsuficienteException extends Exception {
    public SaldoInsuficienteException(String mensaje) {
        super(mensaje);
    }
}
```

### try-with-resources (Java 7+)

Cierra automaticamente recursos que implementan AutoCloseable.

```java
try (FileReader fr = new FileReader("archivo.txt");
     BufferedReader br = new BufferedReader(fr)) {
    String linea = br.readLine();
} catch (IOException e) {
    System.out.println("Error: " + e.getMessage());
}
```

## Ejercicios

### Ejercicio 1: Division segura
Crea un programa que pida dos numeros al usuario y muestre el resultado de la division. Maneja las excepciones ArithmeticException (division por cero) y InputMismatchException (entrada no numerica). Usa un bucle hasta que el usuario introduzca datos validos.

### Ejercicio 2: Excepcion personalizada
Crea una excepcion personalizada `EdadInvalidaException`. Crea una clase `Persona` con atributo edad. El setter debe lanzar la excepcion si la edad es menor que 0 o mayor que 150. En el main, captura y maneja la excepcion.

### Ejercicio 3: try-with-resources y finally
Crea un programa que intente leer un archivo "datos.txt". Usa try-with-resources para el FileReader y BufferedReader. Si el archivo no existe, captura FileNotFoundException. Usa un bloque finally que siempre imprima "Operacion finalizada".

### Ejecuta los ejercicios

```bash
javac Ejercicios.java && java Ejercicios
```
