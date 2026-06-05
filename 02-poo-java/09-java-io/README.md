# Java I/O

## Teoria

Java I/O (Input/Output) permite leer y escribir datos desde/hacia archivos, consola, redes, etc.

### FileWriter

Escribe caracteres a un archivo.

```java
try (FileWriter fw = new FileWriter("archivo.txt")) {
    fw.write("Hola mundo");
} catch (IOException e) {
    System.out.println("Error: " + e.getMessage());
}
```

### FileReader y BufferedReader

Lee caracteres de un archivo. BufferedReader anade buffer para mayor eficiencia.

```java
try (BufferedReader br = new BufferedReader(new FileReader("archivo.txt"))) {
    String linea;
    while ((linea = br.readLine()) != null) {
        System.out.println(linea);
    }
} catch (IOException e) {
    System.out.println("Error: " + e.getMessage());
}
```

### try-with-resources

Declara recursos que se cierran automaticamente al final del bloque. Disponible desde Java 7.

```java
try (FileWriter fw = new FileWriter("archivo.txt")) {
    fw.write("contenido");
} catch (IOException e) {
    // manejo de error
}
// fw se cierra automaticamente aqui
```

### Flujos (Streams)

| Clase | Proposito |
|-------|-----------|
| FileReader | Lee caracteres de un archivo |
| FileWriter | Escribe caracteres a un archivo |
| BufferedReader | Lee texto con buffer |
| BufferedWriter | Escribe texto con buffer |
| InputStream | Lee bytes |
| OutputStream | Escribe bytes |

## Ejercicios

### Ejercicio 1: Escribir archivo
Usa FileWriter para escribir "Hola mundo" en salida.txt.

**Ejecuta:** `python scripts/runner.py 2 9 1`

### Ejercicio 2: Leer archivo
Usa BufferedReader para leer y mostrar el contenido de salida.txt.

**Ejecuta:** `python scripts/runner.py 2 9 2`

### Ejercicio 3: Copiar archivo
Copia el contenido de origen.txt a destino.txt caracter por caracter.

**Ejecuta:** `python scripts/runner.py 2 9 3`

## Soluciones

```bash
python scripts/runner.py 2 9 1 -s
python scripts/runner.py 2 9 2 -s
python scripts/runner.py 2 9 3 -s
```
