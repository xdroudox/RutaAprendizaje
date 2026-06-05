import java.io.*;
import java.util.Scanner;

public class Soluciones {
    public static void main(String[] args) {
        if (args.length > 0) {
            int n = Integer.parseInt(args[0]);
            switch (n) {
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
        System.out.println("=== SOLUCION 1: Leer y mostrar archivo ===");
        System.out.println("Scanner sc = new Scanner(System.in);");
        System.out.println("System.out.print(\"Nombre del archivo: \");");
        System.out.println("String nombreArchivo = sc.nextLine();");
        System.out.println("sc.close();");
        System.out.println();
        System.out.println("try (BufferedReader br = new BufferedReader(new FileReader(nombreArchivo))) {");
        System.out.println("    String linea;");
        System.out.println("    System.out.println(\"Contenido de \" + nombreArchivo + \":\");");
        System.out.println("    while ((linea = br.readLine()) != null) {");
        System.out.println("        System.out.println(linea);");
        System.out.println("    }");
        System.out.println("} catch (FileNotFoundException e) {");
        System.out.println("    System.out.println(\"Error: El archivo '\" + nombreArchivo + \"' no existe\");");
        System.out.println("} catch (IOException e) {");
        System.out.println("    System.out.println(\"Error de lectura: \" + e.getMessage());");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: FileReader abre el archivo, BufferedReader lo lee por lineas.");
        System.out.println("try-with-resources cierra automaticamente el recurso.");
    }

    static void solucion_2() {
        System.out.println("=== SOLUCION 2: Escribir en archivo ===");
        System.out.println("Scanner sc = new Scanner(System.in);");
        System.out.println();
        System.out.println("try (BufferedWriter bw = new BufferedWriter(new FileWriter(\"notas.txt\"))) {");
        System.out.println("    System.out.println(\"Escribe lineas de texto (escribe 'salir' para terminar):\");");
        System.out.println("    String linea = \"\";");
        System.out.println("    while (!linea.equals(\"salir\")) {");
        System.out.println("        linea = sc.nextLine();");
        System.out.println("        if (!linea.equals(\"salir\")) {");
        System.out.println("            bw.write(linea);");
        System.out.println("            bw.newLine();");
        System.out.println("        }");
        System.out.println("    }");
        System.out.println("    System.out.println(\"Notas guardadas en notas.txt\");");
        System.out.println("} catch (IOException e) {");
        System.out.println("    System.out.println(\"Error: \" + e.getMessage());");
        System.out.println("}");
        System.out.println("sc.close();");
        System.out.println();
        System.out.println("Explicacion: BufferedWriter escribe texto en el archivo.");
        System.out.println("newLine() anade un salto de linea. Modo append=false sobrescribe.");
    }

    static void solucion_3() {
        System.out.println("=== SOLUCION 3: Copiar archivo ===");
        System.out.println("String origen = \"origen.txt\";");
        System.out.println("String destino = \"destino.txt\";");
        System.out.println("int totalCaracteres = 0;");
        System.out.println();
        System.out.println("try (BufferedReader br = new BufferedReader(new FileReader(origen));");
        System.out.println("     BufferedWriter bw = new BufferedWriter(new FileWriter(destino))) {");
        System.out.println("    String linea;");
        System.out.println("    while ((linea = br.readLine()) != null) {");
        System.out.println("        bw.write(linea);");
        System.out.println("        bw.newLine();");
        System.out.println("        totalCaracteres += linea.length();");
        System.out.println("    }");
        System.out.println("    System.out.println(\"Archivo copiado exitosamente.\");");
        System.out.println("    System.out.println(\"Caracteres copiados: \" + totalCaracteres);");
        System.out.println("} catch (FileNotFoundException e) {");
        System.out.println("    System.out.println(\"Error: El archivo '\" + origen + \"' no existe\");");
        System.out.println("} catch (IOException e) {");
        System.out.println("    System.out.println(\"Error: \" + e.getMessage());");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: try-with-resources con dos recursos separados por punto y coma.");
        System.out.println("Lee de BufferedReader y escribe en BufferedWriter simultaneamente.");
    }
}
