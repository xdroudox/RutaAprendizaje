/**
 * SOLUCIONES - Java I/O
 * Ejecuta: python scripts/runner.py 2 9 [ejercicio] -s
 */
import java.io.*;

public class Soluciones {

    public static void main(String[] args) {
        if (args.length > 0) {
            int num = Integer.parseInt(args[0]);
            switch (num) {
                case 1: solucion_1(); break;
                case 2: solucion_2(); break;
                case 3: solucion_3(); break;
                default: System.out.println("Solucion no encontrada");
            }
        } else {
            System.out.println("Soluciones disponibles: 1, 2, 3");
        }
    }

    static void solucion_1() {
        System.out.println("=== SOLUCION 1: Escribir archivo ===");
        System.out.println("try (FileWriter fw = new FileWriter(\"salida.txt\")) {");
        System.out.println("    fw.write(\"Hola mundo\");");
        System.out.println("    System.out.println(\"Archivo escrito correctamente\");");
        System.out.println("} catch (IOException e) {");
        System.out.println("    System.out.println(\"Error: \" + e.getMessage());");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: FileWriter escribe caracteres a un archivo.");
        System.out.println("try-with-resources cierra el recurso automaticamente.");
    }

    static void solucion_2() {
        System.out.println("=== SOLUCION 2: Leer archivo ===");
        System.out.println("try (BufferedReader br = new BufferedReader(new FileReader(\"salida.txt\"))) {");
        System.out.println("    String linea;");
        System.out.println("    while ((linea = br.readLine()) != null) {");
        System.out.println("        System.out.println(linea);");
        System.out.println("    }");
        System.out.println("} catch (IOException e) {");
        System.out.println("    System.out.println(\"Error: \" + e.getMessage());");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: BufferedReader lee texto eficientemente linea por linea.");
        System.out.println("readLine() retorna null cuando se llega al final del archivo.");
    }

    static void solucion_3() {
        System.out.println("=== SOLUCION 3: Copiar archivo ===");
        System.out.println("try (FileReader fr = new FileReader(\"origen.txt\");");
        System.out.println("     FileWriter fw = new FileWriter(\"destino.txt\")) {");
        System.out.println("    int c;");
        System.out.println("    while ((c = fr.read()) != -1) {");
        System.out.println("        fw.write(c);");
        System.out.println("    }");
        System.out.println("    System.out.println(\"Archivo copiado correctamente\");");
        System.out.println("} catch (IOException e) {");
        System.out.println("    System.out.println(\"Error: \" + e.getMessage());");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: read() devuelve -1 al final del archivo.");
        System.out.println("Se lee y escribe caracter por caracter.");
    }
}
