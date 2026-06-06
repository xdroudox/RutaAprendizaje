/**
 * EJERCICIOS - Patrones Creacionales
 * Ejecuta desde raiz: python scripts/runner.py 8 1 [ejercicio] [-p N]
 */
public class Ejercicios {
    public static void main(String[] args) {
        if (args.length > 0 && args[0].matches("\\d+")) {
            int num = Integer.parseInt(args[0]);
            int pista = 0;
            for (int i = 1; i < args.length; i++) {
                if (args[i].equals("-p") && i + 1 < args.length) {
                    pista = Integer.parseInt(args[i + 1]);
                    break;
                }
            }
            switch (num) {
                case 1: ejercicio_1(pista); break;
                case 2: ejercicio_2(pista); break;
                case 3: ejercicio_3(pista); break;
            }
        } else {
            System.out.println("EJERCICIOS:");
            System.out.println("  🟢 Ej 1: Singleton - Configuracion");
            System.out.println("  🟡 Ej 2: Factory - Figuras");
            System.out.println("  🟡 Ej 3: Builder - Pizza");
        }
    }

    static void ejercicio_1(int pista) {
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
        if (pista > 0) {
            System.out.println("\n========================================");
            System.out.println("PISTAS:");
        }
        if (pista >= 1) {
            System.out.println("\n🟢 PISTA 1 (Basica):");
            System.out.println("  - Constructor privado: private Configuracion() {}");
            System.out.println("  - Atributo estatico: private static Configuracion instancia;");
            System.out.println("  - Metodo estatico: public static Configuracion getInstance()");
            System.out.println("  - Dentro de getInstance(): if (instancia == null) instancia = new Configuracion();");
            System.out.println("  - return instancia;");
        }
        if (pista >= 2) {
            System.out.println("\n🟡 PISTA 2 (Intermedia):");
            System.out.println("  public class Configuracion {\n" +
                "      private static Configuracion instancia;\n" +
                "      private String host = \"localhost\";\n" +
                "      private int puerto = 3306;\n" +
                "      private String usuario = \"root\";\n" +
                "      private String password = \"\";\n" +
                "      private Configuracion() {}\n" +
                "      public static Configuracion getInstance() {\n" +
                "          if (instancia == null) instancia = new Configuracion();\n" +
                "          return instancia;\n" +
                "      }\n" +
                "      public void mostrar() {\n" +
                "          System.out.println(\"Host: \" + host + \", Puerto: \" + puerto);\n" +
                "      }\n" +
                "  }");
        }
        if (pista >= 3) {
            System.out.println("\n🔴 PISTA 3 (Avanzada - casi la solucion):");
            System.out.println("  Ademas, demuestra que es la misma instancia:\n" +
                "  Configuracion c1 = Configuracion.getInstance();\n" +
                "  Configuracion c2 = Configuracion.getInstance();\n" +
                "  System.out.println(\"Misma instancia? \" + (c1 == c2));  // true\n" +
                "  c1.mostrar();");
        }
    }

    static void ejercicio_2(int pista) {
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
        if (pista > 0) {
            System.out.println("\n========================================");
            System.out.println("PISTAS:");
        }
        if (pista >= 1) {
            System.out.println("\n🟢 PISTA 1 (Basica):");
            System.out.println("  - Crea interface Figura con metodo void dibujar()");
            System.out.println("  - Circulo y Cuadrado implementan Figura");
            System.out.println("  - FiguraFactory.crearFigura(String tipo) usa if/else o switch");
            System.out.println("    para retornar la clase correcta segun el tipo");
            System.out.println("  - Lanza IllegalArgumentException si el tipo no existe");
        }
        if (pista >= 2) {
            System.out.println("\n🟡 PISTA 2 (Intermedia):");
            System.out.println("  interface Figura { void dibujar(); }");
            System.out.println("  class Circulo implements Figura {\n" +
                "      public void dibujar() { System.out.println(\"Dibujando Circulo\"); }\n" +
                "  }");
            System.out.println("  class Cuadrado implements Figura {\n" +
                "      public void dibujar() { System.out.println(\"Dibujando Cuadrado\"); }\n" +
                "  }");
            System.out.println("  class FiguraFactory {\n" +
                "      public static Figura crearFigura(String tipo) {\n" +
                "          if (tipo.equalsIgnoreCase(\"circulo\")) return new Circulo();\n" +
                "          if (tipo.equalsIgnoreCase(\"cuadrado\")) return new Cuadrado();\n" +
                "          throw new IllegalArgumentException(\"Figura desconocida: \" + tipo);\n" +
                "      }\n" +
                "  }");
        }
        if (pista >= 3) {
            System.out.println("\n🔴 PISTA 3 (Avanzada - casi la solucion):");
            System.out.println("  Figura f1 = FiguraFactory.crearFigura(\"circulo\");");
            System.out.println("  Figura f2 = FiguraFactory.crearFigura(\"cuadrado\");");
            System.out.println("  f1.dibujar();  // \"Dibujando Circulo\"");
            System.out.println("  f2.dibujar();  // \"Dibujando Cuadrado\"");
        }
    }

    static void ejercicio_3(int pista) {
        System.out.println(">> EJERCICIO 3: Builder - Pizza");
        System.out.println("-".repeat(40));
        System.out.println("Construye una Pizza con Builder (masa, salsa, ingredientes).");
        System.out.println("Atributos: masa (String), salsa (String),");
        System.out.println("ingredientes (List<String>), tamano (String).");
        System.out.println("Usa fluent interface: new Pizza.Builder().masa(\"...\")...build()");
        System.out.println();
        System.out.println("public class Pizza {");
        System.out.println("    private Pizza(Builder builder) { ... }");
        System.out.println("    public static class Builder {");
        System.out.println("        // ==== ESCRIBE TU RESPUESTA AQUI ====");
        System.out.println("    }");
        System.out.println("}");
        if (pista > 0) {
            System.out.println("\n========================================");
            System.out.println("PISTAS:");
        }
        if (pista >= 1) {
            System.out.println("\n🟢 PISTA 1 (Basica):");
            System.out.println("  - Builder es una clase interna ESTATICA con los mismos atributos que Pizza");
            System.out.println("  - Cada metodo setter retorna 'this' (fluent interface)");
            System.out.println("  - Metodo build() crea la Pizza con new Pizza(this)");
            System.out.println("  - El constructor de Pizza recibe Builder y copia los atributos");
        }
        if (pista >= 2) {
            System.out.println("\n🟡 PISTA 2 (Intermedia):");
            System.out.println("  public static class Builder {\n" +
                "      private String masa = \"fina\";\n" +
                "      private String salsa = \"tomate\";\n" +
                "      private String ingredientes = \"queso\";\n" +
                "      private String tamano = \"mediana\";\n" +
                "      public Builder masa(String m) { this.masa = m; return this; }\n" +
                "      public Builder salsa(String s) { this.salsa = s; return this; }\n" +
                "      public Builder ingredientes(String i) { this.ingredientes = i; return this; }\n" +
                "      public Builder tamano(String t) { this.tamano = t; return this; }\n" +
                "      public Pizza build() { return new Pizza(this); }\n" +
                "  }");
        }
        if (pista >= 3) {
            System.out.println("\n🔴 PISTA 3 (Avanzada - casi la solucion):");
            System.out.println("  Pizza p = new Pizza.Builder()\n" +
                "      .masa(\"gruesa\")\n" +
                "      .salsa(\"barbacoa\")\n" +
                "      .ingredientes(\"queso, pepperoni\")\n" +
                "      .tamano(\"familiar\")\n" +
                "      .build();\n" +
                "  System.out.println(p);");
        }
    }
}
