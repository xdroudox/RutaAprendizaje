# Java I/O

**Java I/O** (Input/Output) permite leer y escribir datos desde y hacia archivos, consola, redes y otros dispositivos. Es esencial para cualquier aplicacion que necesite persistencia de datos.

---

## 1. TEORIA

### 1.1 Que es I/O?

I/O = Entrada/Salida. En Java, se maneja a traves de **flujos (streams)** que son canales de datos.

```
Archivo en disco → [Flujo de entrada] → Programa
Programa → [Flujo de salida] → Archivo en disco
```

### 1.2 FileWriter — Escribir archivos

`FileWriter` es la clase mas simple para ESCRIBIR caracteres en un archivo.

```java
import java.io.FileWriter;
import java.io.IOException;

try (FileWriter fw = new FileWriter("salida.txt")) {
    fw.write("Hola mundo");
    fw.write("\nSegunda linea");
    System.out.println("Archivo escrito correctamente");
} catch (IOException e) {
    System.out.println("Error: " + e.getMessage());
}
```

**Explicacion:**

| Codigo | Que hace |
|--------|----------|
| `FileWriter fw = new FileWriter("salida.txt")` | Crea un flujo hacia el archivo. Si no existe, lo crea. Si existe, lo SOBREESCRIBE |
| `fw.write("Hola mundo")` | Escribe el texto en el archivo |
| `fw.write("\n")` | Salto de linea (en Windows usa `\r\n`) |
| `try (...) { ... }` | try-with-resources: CIERRA el recurso automaticamente al salir del bloque |
| `catch (IOException e)` | Captura errores de E/S (permisos, disco lleno, etc.) |

**Modos de FileWriter:**
- `new FileWriter("archivo.txt")` — Sobrescribe si existe
- `new FileWriter("archivo.txt", true)` — Agrega al final (append)

### 1.3 FileReader y BufferedReader — Leer archivos

`FileReader` lee caracteres. `BufferedReader` agrega un BUFFER para leer linea por linea, que es mas eficiente.

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

try (BufferedReader br = new BufferedReader(new FileReader("salida.txt"))) {
    String linea;
    while ((linea = br.readLine()) != null) {
        System.out.println(linea);  // Procesar cada linea
    }
} catch (IOException e) {
    System.out.println("Error: " + e.getMessage());
}
```

**Explicacion:**

| Codigo | Que hace |
|--------|----------|
| `new FileReader("salida.txt")` | Abre el archivo para lectura |
| `new BufferedReader(FileReader)` | Envuelve el FileReader con un buffer para leer linea por linea |
| `br.readLine()` | Lee UNA linea del archivo (sin el salto de linea) |
| `while ((linea = br.readLine()) != null)` | Lee hasta que readLine() devuelve null (fin de archivo) |

**El patron `while ((linea = br.readLine()) != null)` es MUY comun en Java.** Significa:
1. Lee una linea
2. Asignala a `linea`
3. Si no es null, ejecuta el cuerpo del while
4. Repite

### 1.4 try-with-resources

Disponible desde Java 7. Declara recursos que se CIERRAN AUTOMATICAMENTE.

```java
// SIN try-with-resources (Java 6 y anterior):
FileWriter fw = null;
try {
    fw = new FileWriter("archivo.txt");
    fw.write("contenido");
} catch (IOException e) {
    System.out.println("Error: " + e.getMessage());
} finally {
    if (fw != null) {
        try { fw.close(); } catch (IOException e) { }
    }
}

// CON try-with-resources (Java 7+):
try (FileWriter fw = new FileWriter("archivo.txt")) {
    fw.write("contenido");
} catch (IOException e) {
    System.out.println("Error: " + e.getMessage());
}
// fw se cierra AUTOMATICAMENTE aqui
```

**Puedes declarar MULTIPLES recursos en el try:**

```java
try (FileReader fr = new FileReader("origen.txt");
     FileWriter fw = new FileWriter("destino.txt")) {
    int c;
    while ((c = fr.read()) != -1) {
        fw.write(c);
    }
} catch (IOException e) {
    System.out.println("Error: " + e.getMessage());
}
// fr y fw se cierran automaticamente (en orden inverso)
```

### 1.5 Flujos principales

| Clase | Lee/Escribe | Proposito |
|-------|-------------|-----------|
| `FileReader` | Lee | Caracteres de un archivo |
| `FileWriter` | Escribe | Caracteres a un archivo |
| `BufferedReader` | Lee | Lectura eficiente linea por linea |
| `BufferedWriter` | Escribe | Escritura eficiente con buffer |
| `InputStream` | Lee | Bytes (archivos binarios) |
| `OutputStream` | Escribe | Bytes (archivos binarios) |
| `PrintWriter` | Escribe | Metodos print() y println() a archivos |

---

## 2. GLOSARIO DEL TEMA

| Termino | Definicion | Ejemplo |
|---------|------------|---------|
| **I/O** | Input/Output, entrada y salida de datos | Leer/escribir archivos |
| **Stream** | Flujo de datos que fluye entre origen y destino | `FileReader`, `FileWriter` |
| **FileReader** | Lee caracteres de un archivo | `new FileReader("archivo.txt")` |
| **FileWriter** | Escribe caracteres a un archivo | `new FileWriter("archivo.txt")` |
| **BufferedReader** | Lee texto eficientemente con buffer | `new BufferedReader(FileReader)` |
| **readLine()** | Lee una linea de texto, null si es fin de archivo | `br.readLine()` |
| **try-with-resources** | Cierra recursos automaticamente | `try (FileWriter fw = ...)` |
| **IOException** | Excepcion de entrada/salida | `catch (IOException e)` |
| **Buffer** | Memoria temporal para optimizar lecturas/escrituras | BufferedReader usa buffer |

---

## 3. COMPARATIVA ENTRE LENGUAJES

### Escribir archivo

| Java | Python | JavaScript (Node.js) |
|------|--------|----------------------|
| `try (FileWriter fw = new FileWriter("f.txt")) {` | `with open("f.txt", "w") as f:` | `fs.writeFileSync("f.txt", "texto");` |
| `    fw.write("texto");` | `    f.write("texto")` | |
| `} catch (IOException e) { ... }` | `except IOError as e: ...` | `try { ... } catch (e) { ... }` |

### Leer archivo

| Java | Python | JS (Node.js) |
|------|--------|--------------|
| `try (BufferedReader br = new BufferedReader(` | `with open("f.txt") as f:` | `fs.readFileSync("f.txt", "utf8");` |
| `        new FileReader("f.txt"))) {` | `    for linea in f:` | |
| `    while ((l = br.readLine()) != null) {` | `        print(linea)` | |
| `        System.out.println(l);` | | |
| `    }` | | |

**Diferencias clave:**
- **Java**: Verboso pero explicito. try-with-resources simplifica el cierre. Diferencia entre bytes y caracteres
- **Python**: `with open()` es mas simple. No diferencia entre bytes y caracteres (Python 3+ lo hace)
- **JavaScript**: Async por defecto. `fs.readFileSync()` para sync, `fs.readFile()` para async

---

## 4. EJEMPLO GUIADO

### Problema: Copiar archivo de texto

> "Crea un programa que copie el contenido de `origen.txt` a `destino.txt` caracter por caracter usando FileReader y FileWriter con try-with-resources."

---

**Paso 1: Analizar**
- `FileReader` para leer de origen.txt
- `FileWriter` para escribir en destino.txt
- Leer caracter por caracter con `read()`
- `read()` devuelve -1 cuando llega al final del archivo

**Paso 2: Pseudocodigo**
```
INTENTAR CON FileReader fr = abrir("origen.txt")
         Y FileWriter fw = abrir("destino.txt"):
    int c = fr.read()        // Lee el primer caracter
    MIENTRAS c != -1:        // -1 = fin de archivo
        fw.write(c)          // Escribe el caracter
        c = fr.read()        // Lee el siguiente
    imprimir "Archivo copiado correctamente"
CAPTURAR IOException e:
    imprimir "Error: " + e.getMessage()
// fr y fw se cierran automaticamente
```

**Paso 3: Codigo completo**
```java
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        try (FileReader fr = new FileReader("origen.txt");
             FileWriter fw = new FileWriter("destino.txt")) {

            int c;  // read() devuelve int, no char
            while ((c = fr.read()) != -1) {
                fw.write(c);
            }

            System.out.println("Archivo copiado correctamente");

        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
```

**Explicacion:**

| Linea | Explicacion |
|-------|-------------|
| `FileReader fr = new FileReader("origen.txt")` | Abre origen.txt para LECTURA. Si no existe, lanza FileNotFoundException |
| `FileWriter fw = new FileWriter("destino.txt")` | Abre destino.txt para ESCRITURA. Si no existe, lo crea. Si existe, lo SOBRESCRIBE |
| `int c` | `read()` devuelve un `int` (no `char`) para poder devolver -1 como marcador de fin |
| `(c = fr.read()) != -1` | Lee un caracter. Si es -1, se acabo el archivo |
| `fw.write(c)` | Escribe ese caracter en el destino |
| `catch (IOException e)` | Captura cualquier error de E/S (archivo no encontrado, permisos, etc.) |

**Paso 4: Probar**
```
$ echo "Hola mundo!" > origen.txt
$ java Main
Archivo copiado correctamente
$ cat destino.txt
Hola mundo!
```

---

## 5. EJERCICIOS

### 🟢 Ejercicio 1: Escribir archivo (Basico)

Usa `FileWriter` con try-with-resources para escribir "Hola mundo" en un archivo llamado `salida.txt`. Muestra "Archivo escrito correctamente" al finalizar.

**Ejecuta:** `python scripts/runner.py 2 9 1`

---

### 🟡 Ejercicio 2: Leer archivo (Intermedio)

Usa `BufferedReader` y `FileReader` para leer el archivo `salida.txt`. Lee linea por linea con `readLine()` y muestralas en consola. (Asume que el archivo del ejercicio 1 ya existe.)

**Ejecuta:** `python scripts/runner.py 2 9 2`

---

### 🔴 Ejercicio 3: Copiar archivo (Avanzado)

Usa `FileReader` y `FileWriter` para copiar el contenido de `origen.txt` a `destino.txt` caracter por caracter. Muestra "Archivo copiado correctamente".

**Ejecuta:** `python scripts/runner.py 2 9 3`

---

## Soluciones

```bash
python scripts/runner.py 2 9 1 -s
python scripts/runner.py 2 9 2 -s
python scripts/runner.py 2 9 3 -s
```
