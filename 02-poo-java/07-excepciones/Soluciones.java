import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Soluciones {
    public static void main(String[] args) {
        if (args.length > 0) {
            int n = Integer.parseInt(args[0]);
            switch (n) {
                case 1: solucion_1(); break;
                case 2: solucion_2(); break;
                case 3: solucion_3(args); break;
                default: System.out.println("Solucion no encontrada");
            }
        } else {
            System.out.println("Soluciones disponibles: 1, 2, 3");
        }
    }

    static void solucion_1() {
        System.out.println("=== SOLUCION 1: Division segura ===");
        System.out.println("Scanner sc = new Scanner(System.in);");
        System.out.println("int a = 0, b = 0;");
        System.out.println("boolean valido = false;");
        System.out.println("while (!valido) {");
        System.out.println("    try {");
        System.out.println("        System.out.print(\"Ingresa numerador: \");");
        System.out.println("        a = sc.nextInt();");
        System.out.println("        System.out.print(\"Ingresa denominador: \");");
        System.out.println("        b = sc.nextInt();");
        System.out.println("        System.out.println(\"Resultado: \" + (a / b));");
        System.out.println("        valido = true;");
        System.out.println("    } catch (ArithmeticException e) {");
        System.out.println("        System.out.println(\"Error: No se puede dividir por cero\");");
        System.out.println("    } catch (InputMismatchException e) {");
        System.out.println("        System.out.println(\"Error: Debes ingresar numeros enteros\");");
        System.out.println("        sc.next(); // Limpiar buffer");
        System.out.println("    }");
        System.out.println("}");
        System.out.println("sc.close();");
        System.out.println();
        System.out.println("Explicacion: Multi-catch permite capturar diferentes excepciones.");
        System.out.println("El bucle while repite hasta que la operacion sea exitosa.");
    }

    static void solucion_2() {
        System.out.println("=== SOLUCION 2: Excepcion personalizada ===");
        System.out.println("class EdadInvalidaException extends Exception {");
        System.out.println("    public EdadInvalidaException(String mensaje) {");
        System.out.println("        super(mensaje);");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("class Persona {");
        System.out.println("    private int edad;");
        System.out.println();
        System.out.println("    public void setEdad(int edad) throws EdadInvalidaException {");
        System.out.println("        if (edad < 0 || edad > 150) {");
        System.out.println("            throw new EdadInvalidaException(\"Edad fuera de rango: \" + edad);");
        System.out.println("        }");
        System.out.println("        this.edad = edad;");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("public class Main {");
        System.out.println("    public static void main(String[] args) {");
        System.out.println("        Persona p = new Persona();");
        System.out.println("        try {");
        System.out.println("            p.setEdad(-5);");
        System.out.println("        } catch (EdadInvalidaException e) {");
        System.out.println("            System.out.println(\"Error: \" + e.getMessage());");
        System.out.println("        }");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: EdadInvalidaException extiende Exception (checked).");
        System.out.println("El setter declara 'throws' y lanza la excepcion con 'throw'.");
    }

    static void solucion_3(String[] args) {
        System.out.println("=== SOLUCION 3: try-with-resources y finally ===");
        System.out.println("String nombreArchivo = \"datos.txt\";");
        System.out.println("try (BufferedReader br = new BufferedReader(new FileReader(nombreArchivo))) {");
        System.out.println("    String linea;");
        System.out.println("    while ((linea = br.readLine()) != null) {");
        System.out.println("        System.out.println(linea);");
        System.out.println("    }");
        System.out.println("} catch (FileNotFoundException e) {");
        System.out.println("    System.out.println(\"Archivo no encontrado: \" + nombreArchivo);");
        System.out.println("} catch (IOException e) {");
        System.out.println("    System.out.println(\"Error de lectura: \" + e.getMessage());");
        System.out.println("} finally {");
        System.out.println("    System.out.println(\"Operacion finalizada\");");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: try-with-resources cierra BufferedReader automaticamente.");
        System.out.println("finally se ejecuta siempre, haya o no excepcion.");
    }
}
