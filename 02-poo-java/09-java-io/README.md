# Java I/O

## Teoria

Java I/O (Input/Output) proporciona clases para leer y escribir datos en archivos, la consola y otros flujos de entrada/salida.

### File

La clase `File` representa una ruta de archivo o directorio.

```java
File archivo = new File("datos.txt");
archivo.exists();       // si existe
archivo.isFile();       // si es archivo
archivo.isDirectory();  // si es directorio
archivo.length();       // tamano en bytes
archivo.getName();      // nombre del archivo
archivo.getAbsolutePath(); // ruta absoluta
archivo.delete();       // eliminar
```

### FileReader y BufferedReader

Lectura de archivos de texto.

```java
try (BufferedReader br = new BufferedReader(new FileReader("archivo.txt"))) {
    String linea;
    while ((linea = br.readLine()) != null) {
        System.out.println(linea);
    }
} catch (IOException e) {
    e.printStackTrace();
}
```

### FileWriter y BufferedWriter

Escritura en archivos de texto.

```java
try (BufferedWriter bw = new BufferedWriter(new FileWriter("salida.txt"))) {
    bw.write("Linea 1");
    bw.newLine();
    bw.write("Linea 2");
} catch (IOException e) {
    e.printStackTrace();
}
```

### FileWriter con append

```java
// Segundo parametro true = modo append (anadir al final)
try (BufferedWriter bw = new BufferedWriter(new FileWriter("log.txt", true))) {
    bw.write("Nueva entrada de log");
    bw.newLine();
}
```

### Scanner

Lee datos de entrada desde la consola o archivos.

```java
// Desde consola
Scanner sc = new Scanner(System.in);
System.out.print("Nombre: ");
String nombre = sc.nextLine();

// Desde archivo
try (Scanner scArchivo = new Scanner(new File("datos.txt"))) {
    while (scArchivo.hasNextLine()) {
        String linea = scArchivo.nextLine();
        System.out.println(linea);
    }
}
```

### try-with-resources

Cierra automaticamente los recursos que implementan `AutoCloseable`.

```java
try (BufferedReader br = new BufferedReader(new FileReader("archivo.txt"));
     BufferedWriter bw = new BufferedWriter(new FileWriter("copia.txt"))) {
    String linea;
    while ((linea = br.readLine()) != null) {
        bw.write(linea);
        bw.newLine();
    }
} catch (IOException e) {
    System.out.println("Error: " + e.getMessage());
}
```

### Flujo tipico de lectura

```
Archivo -> FileReader -> BufferedReader -> Programa
    (bytes)    (caracteres)   (buffer/líneas)
```

### Flujo tipico de escritura

```
Programa -> BufferedWriter -> FileWriter -> Archivo
```

## Ejercicios

### Ejercicio 1: Leer y mostrar archivo
Crea un programa que pida al usuario el nombre de un archivo, lo lea linea por linea con BufferedReader y muestre su contenido. Si el archivo no existe, captura la excepcion y muestra un mensaje de error.

### Ejercicio 2: Escribir en archivo
Crea un programa que pida al usuario que escriba lineas de texto. Cada linea se guarda en un archivo "notas.txt" usando BufferedWriter. El programa termina cuando el usuario escribe "salir".

### Ejercicio 3: Copiar archivo con try-with-resources
Crea un programa que copie el contenido de "origen.txt" a "destino.txt". Usa try-with-resources con BufferedReader y BufferedWriter. Muestra cuantos caracteres se copiaron.

### Ejecuta los ejercicios

```bash
javac Ejercicios.java && java Ejercicios
```
