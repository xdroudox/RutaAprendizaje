/**
 * SOLUCIONES - Java I/O (Java)
 * Ejecuta desde raiz: python scripts/runner.py 2 9 [ejercicio] -s
 */
import java.io.*;

public class Soluciones {

    public static void main(String[] args) {
        if (args.length > 0 && !args[0].startsWith("-")) {
            int num;
            try {
                num = Integer.parseInt(args[0]);
            } catch (NumberFormatException e) {
                System.out.println("Solucion no encontrada");
                return;
            }
            switch (num) {
                case 1: solucion_1(); break;
                case 2: solucion_2(); break;
                case 3: solucion_3(); break;
                default: System.out.println("Ejercicio no encontrado. Valores: 1-3");
            }
        } else {
            System.out.println("SOLUCIONES:");
            System.out.println("  🟢 1. Escribir archivo con FileWriter");
            System.out.println("  🟡 2. Leer archivo con BufferedReader");
            System.out.println("  🔴 3. Copiar archivo caracter por caracter");
        }
    }

    static void solucion_1() {
        System.out.println("=".repeat(50));
        System.out.println("🟢 SOLUCION 1: Escribir archivo");
        System.out.println("=".repeat(50));
        System.out.println();

        System.out.println("--- CODIGO (Main.java) ---");
        System.out.println("""
import java.io.FileWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        try (FileWriter fw = new FileWriter("salida.txt")) {
            fw.write("Hola mundo");
            System.out.println("Archivo escrito correctamente");
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
""");

        System.out.println("--- EXPLICACION ---");
        System.out.println("""
1. `FileWriter fw = new FileWriter("salida.txt")` — Abre el archivo para
   escritura. Si no existe, lo crea. Si existe, lo SOBRESCRIBE.

2. `fw.write("Hola mundo")` — Escribe el texto en el archivo.

3. try-with-resources: al salir del bloque, Java CIERRA automaticamente
   el FileWriter. Sin esto, los datos podrian no guardarse (el buffer
   necesita flush/close para escribir al disco).

4. `catch (IOException e)` — Captura errores como permisos denegados,
   disco lleno, ruta invalida, etc.
""");
    }

    static void solucion_2() {
        System.out.println("=".repeat(50));
        System.out.println("🟡 SOLUCION 2: Leer archivo");
        System.out.println("=".repeat(50));
        System.out.println();

        System.out.println("--- CODIGO (Main.java) ---");
        System.out.println("""
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        try (BufferedReader br = new BufferedReader(new FileReader("salida.txt"))) {
            String linea;
            while ((linea = br.readLine()) != null) {
                System.out.println(linea);
            }
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
""");

        System.out.println("--- EXPLICACION ---");
        System.out.println("""
1. `BufferedReader br = new BufferedReader(new FileReader("salida.txt"))` —
   Envuelve un FileReader en un BufferedReader para leer LINEA por linea.

2. `String linea;` — Variable que almacenara cada linea leida.

3. `while ((linea = br.readLine()) != null)` — Lee una linea, la asigna
   a `linea`, y verifica si no es null. Cuando readLine() devuelve null,
   significa que llegamos al FINAL DEL ARCHIVO.

4. `System.out.println(linea)` — Muestra la linea en consola.
   readLine() NO incluye el salto de linea, lo agrega println().
""");
    }

    static void solucion_3() {
        System.out.println("=".repeat(50));
        System.out.println("🔴 SOLUCION 3: Copiar archivo");
        System.out.println("=".repeat(50));
        System.out.println();

        System.out.println("--- CODIGO (Main.java) ---");
        System.out.println("""
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        try (FileReader fr = new FileReader("origen.txt");
             FileWriter fw = new FileWriter("destino.txt")) {

            int c;
            while ((c = fr.read()) != -1) {
                fw.write(c);
            }

            System.out.println("Archivo copiado correctamente");

        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
""");

        System.out.println("--- EXPLICACION ---");
        System.out.println("""
1. `FileReader fr = new FileReader("origen.txt")` — Abre origen.txt para
   lectura. Si no existe, lanza FileNotFoundException (subclase de IOException).

2. `FileWriter fw = new FileWriter("destino.txt")` — Abre destino.txt para
   escritura. Sobrescribe si existe.

3. `int c` — read() devuelve INT (0-65535) para caracteres, o -1 para fin.
   No puede ser char porque char no puede representar -1.

4. `(c = fr.read()) != -1` — Lee un caracter. -1 = fin de archivo.

5. `fw.write(c)` — Escribe el caracter en el destino.

6. try-with-resources con DOS recursos separados por punto y coma.
   Se cierran en orden INVERSO: primero fw, luego fr.
""");
    }
}
