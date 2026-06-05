/**
 * EJERCICIOS - Patrones Creacionales
 * Ejecuta desde raiz: python scripts/runner.py 8 1 [ejercicio]
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
            System.out.println("1. Singleton - Configuracion");
            System.out.println("2. Factory - Figuras");
            System.out.println("3. Builder - Pizza");
        }
    }

    static void ejercicio_1() {
        System.out.println(">> EJERCICIO 1: Singleton - Configuracion");
        System.out.println("-".repeat(40));
        System.out.println("Crea una clase Configuracion con instancia unica.");
        System.out.println("Debe tener: host, puerto, usuario, password.");
        System.out.println("Constructor privado, getInstance() estatico.");
        System.out.println("Demuestra que solo existe una instancia.");
        System.out.println();
        System.out.println("public class Configuracion {");
        System.out.println("    private static Configuracion instancia;");
        System.out.println("    private String host;");
        System.out.println("    private int puerto;");
        System.out.println();
        System.out.println("    private Configuracion() { ... }");
        System.out.println("    public static Configuracion getInstance() { ... }");
        System.out.println("    // ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    static void ejercicio_2() {
        System.out.println(">> EJERCICIO 2: Factory - Figuras");
        System.out.println("-".repeat(40));
        System.out.println("Crea figuras (Circulo, Cuadrado) usando un Factory.");
        System.out.println("Interface Figura con metodo dibujar().");
        System.out.println("FactoryMethod crearFigura(String tipo).");
        System.out.println();
        System.out.println("interface Figura { void dibujar(); }");
        System.out.println("class Circulo implements Figura { ... }");
        System.out.println("class Cuadrado implements Figura { ... }");
        System.out.println("class FiguraFactory {");
        System.out.println("    public static Figura crearFigura(String tipo) {");
        System.out.println("        // ==== ESCRIBE TU RESPUESTA AQUI ====");
        System.out.println("    }");
        System.out.println("}");
    }

    static void ejercicio_3() {
        System.out.println(">> EJERCICIO 3: Builder - Pizza");
        System.out.println("-".repeat(40));
        System.out.println("Construye una Pizza con Builder (masa, salsa, ingredientes).");
        System.out.println("Atributos: masa (String), salsa (String),");
        System.out.println("ingredientes (List<String>), tamaño (String).");
        System.out.println("Usa fluent interface: new Pizza.Builder().masa(\"...\")...build()");
        System.out.println();
        System.out.println("public class Pizza {");
        System.out.println("    private Pizza(Builder builder) { ... }");
        System.out.println("    public static class Builder {");
        System.out.println("        // ==== ESCRIBE TU RESPUESTA AQUI ====");
        System.out.println("    }");
        System.out.println("}");
    }
}
