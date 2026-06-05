/**
 * EJERCICIOS - Patrones Estructurales
 * Ejecuta desde raiz: python scripts/runner.py 8 2 [ejercicio]
 */
public class Ejercicios {
    public static void main(String[] args) {
        if (args.length > 0) {
            int num = Integer.parseInt(args[0]);
            switch (num) {
                case 1: ejercicio_1(); break;
                case 2: ejercicio_2(); break;
                case 3: ejercicio_3(); break;
            }
        } else {
            System.out.println("EJERCICIOS:");
            System.out.println("1. Adapter - EnchufeEuropeo a EnchufeAmericano");
            System.out.println("2. Decorator - Cafe con extras");
            System.out.println("3. Proxy - Control de acceso a Documento");
        }
    }

    static void ejercicio_1() {
        System.out.println(">> EJERCICIO 1: Adapter - Enchufes");
        System.out.println("-".repeat(40));
        System.out.println("Convierte la interfaz EnchufeEuropeo (conectar())");
        System.out.println("a EnchufeAmericano (plugIn()) usando un Adapter.");
        System.out.println();
        System.out.println("interface EnchufeEuropeo { void conectar(); }");
        System.out.println("interface EnchufeAmericano { void plugIn(); }");
        System.out.println("class Adaptador implements EnchufeAmericano {");
        System.out.println("    private EnchufeEuropeo enchufe;");
        System.out.println("    // ==== ESCRIBE TU RESPUESTA AQUI ====");
        System.out.println("}");
    }

    static void ejercicio_2() {
        System.out.println(">> EJERCICIO 2: Decorator - Cafe");
        System.out.println("-".repeat(40));
        System.out.println("Agrega extras a un Cafe usando Decorator.");
        System.out.println("Interface Bebida con costo() y descripcion().");
        System.out.println("Decoradores: Leche, Azucar.");
        System.out.println();
        System.out.println("interface Bebida { double costo(); String descripcion(); }");
        System.out.println("class CafeSimple implements Bebida { ... }");
        System.out.println("abstract class BebidaDecorator implements Bebida { ... }");
        System.out.println("class Leche extends BebidaDecorator {");
        System.out.println("    // ==== ESCRIBE TU RESPUESTA AQUI ====");
        System.out.println("}");
    }

    static void ejercicio_3() {
        System.out.println(">> EJERCICIO 3: Proxy - Control de Acceso");
        System.out.println("-".repeat(40));
        System.out.println("Crea un Proxy que controle el acceso a un Documento.");
        System.out.println("Solo usuarios con rol 'admin' pueden acceder.");
        System.out.println();
        System.out.println("interface Documento { void mostrar(); }");
        System.out.println("class DocumentoReal implements Documento { ... }");
        System.out.println("class ProxyDocumento implements Documento {");
        System.out.println("    private String usuario;");
        System.out.println("    // ==== ESCRIBE TU RESPUESTA AQUI ====");
        System.out.println("}");
    }
}
