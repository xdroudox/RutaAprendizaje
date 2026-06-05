/**
 * SOLUCIONES - Excepciones
 * Ejecuta: python scripts/runner.py 2 7 [ejercicio] -s
 */
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
        System.out.println("=== SOLUCION 1: Division con try/catch ===");
        System.out.println("int a = 10, b = 0;");
        System.out.println("try {");
        System.out.println("    int resultado = a / b;");
        System.out.println("    System.out.println(\"Resultado: \" + resultado);");
        System.out.println("} catch (ArithmeticException e) {");
        System.out.println("    System.out.println(\"Error: No se puede dividir por cero\");");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: try/catch captura la excepcion y evita que el programa termine.");
    }

    static void solucion_2() {
        System.out.println("=== SOLUCION 2: NumberFormatException ===");
        System.out.println("String numero = \"abc\";");
        System.out.println("try {");
        System.out.println("    int valor = Integer.parseInt(numero);");
        System.out.println("    System.out.println(\"Numero: \" + valor);");
        System.out.println("} catch (NumberFormatException e) {");
        System.out.println("    System.out.println(\"Error: '\" + numero + \"' no es un numero valido\");");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: Integer.parseInt() lanza NumberFormatException si el formato no es valido.");
    }

    static void solucion_3() {
        System.out.println("=== SOLUCION 3: Excepcion personalizada ===");
        System.out.println("class EdadInvalidaException extends Exception {");
        System.out.println("    EdadInvalidaException(String mensaje) {");
        System.out.println("        super(mensaje);");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("static void validarEdad(int edad) throws EdadInvalidaException {");
        System.out.println("    if (edad <= 0 || edad > 150) {");
        System.out.println("        throw new EdadInvalidaException(\"Edad \" + edad + \" no es valida\");");
        System.out.println("    }");
        System.out.println("    System.out.println(\"Edad valida: \" + edad);");
        System.out.println("}");
        System.out.println();
        System.out.println("// En el main:");
        System.out.println("try { validarEdad(25); } catch (EdadInvalidaException e) {");
        System.out.println("    System.out.println(e.getMessage());");
        System.out.println("}");
        System.out.println("try { validarEdad(-5); } catch (EdadInvalidaException e) {");
        System.out.println("    System.out.println(e.getMessage());");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: Las excepciones personalizadas extienden Exception y permiten");
        System.out.println("crear errores especificos de la aplicacion.");
    }
}
