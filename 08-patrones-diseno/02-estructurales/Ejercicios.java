/**
 * EJERCICIOS - Patrones Estructurales
 * Ejecuta desde raiz: python scripts/runner.py 8 2 [ejercicio] [-p N]
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
            System.out.println("  🟢 Ej 1: Adapter - EnchufeEuropeo a EnchufeAmericano");
            System.out.println("  🟡 Ej 2: Decorator - Cafe con extras");
            System.out.println("  🟡 Ej 3: Proxy - Control de acceso a Documento");
        }
    }

    static void ejercicio_1(int pista) {
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
        if (pista > 0) {
            System.out.println("\n========================================");
            System.out.println("PISTAS:");
        }
        if (pista >= 1) {
            System.out.println("\n🟢 PISTA 1 (Basica):");
            System.out.println("  - El Adaptador implementa EnchufeAmericano (la interfaz que el cliente espera)");
            System.out.println("  - Recibe un EnchufeEuropeo en el constructor");
            System.out.println("  - En plugIn(), llama a enchufe.conectar()");
        }
        if (pista >= 2) {
            System.out.println("\n🟡 PISTA 2 (Intermedia):");
            System.out.println("  class EnchufeEuropeoConcreto implements EnchufeEuropeo {\n" +
                "      public void conectar() {\n" +
                "          System.out.println(\"Conectado a 220V (clavija redonda)\");\n" +
                "      }\n" +
                "  }");
            System.out.println("  class Adaptador implements EnchufeAmericano {\n" +
                "      private EnchufeEuropeo enchufe;\n" +
                "      public Adaptador(EnchufeEuropeo e) { this.enchufe = e; }\n" +
                "      public void plugIn() {\n" +
                "          System.out.println(\"Adaptador: convirtiendo...\");\n" +
                "          enchufe.conectar();\n" +
                "      }\n" +
                "  }");
        }
        if (pista >= 3) {
            System.out.println("\n🔴 PISTA 3 (Avanzada - casi la solucion):");
            System.out.println("  EnchufeEuropeo euro = new EnchufeEuropeoConcreto();");
            System.out.println("  EnchufeAmericano adapter = new Adaptador(euro);");
            System.out.println("  adapter.plugIn();  // Usa la interfaz americana pero conecta europeo");
        }
    }

    static void ejercicio_2(int pista) {
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
        if (pista > 0) {
            System.out.println("\n========================================");
            System.out.println("PISTAS:");
        }
        if (pista >= 1) {
            System.out.println("\n🟢 PISTA 1 (Basica):");
            System.out.println("  - BebidaDecorator es abstracta, tiene un atributo Bebida protegido");
            System.out.println("  - Leche extiende BebidaDecorator, recibe Bebida en constructor");
            System.out.println("  - costo() = bebida.costo() + 0.5");
            System.out.println("  - descripcion() = bebida.descripcion() + \", leche\"");
        }
        if (pista >= 2) {
            System.out.println("\n🟡 PISTA 2 (Intermedia):");
            System.out.println("  abstract class BebidaDecorator implements Bebida {\n" +
                "      protected Bebida bebida;\n" +
                "      public BebidaDecorator(Bebida b) { this.bebida = b; }\n" +
                "  }");
            System.out.println("  class Leche extends BebidaDecorator {\n" +
                "      public Leche(Bebida b) { super(b); }\n" +
                "      public double costo() { return bebida.costo() + 0.5; }\n" +
                "      public String descripcion() { return bebida.descripcion() + \", leche\"; }\n" +
                "  }");
            System.out.println("  class Azucar extends BebidaDecorator {\n" +
                "      public Azucar(Bebida b) { super(b); }\n" +
                "      public double costo() { return bebida.costo() + 0.2; }\n" +
                "      public String descripcion() { return bebida.descripcion() + \", azucar\"; }\n" +
                "  }");
        }
        if (pista >= 3) {
            System.out.println("\n🔴 PISTA 3 (Avanzada - casi la solucion):");
            System.out.println("  Bebida cafe = new Azucar(new Leche(new CafeSimple()));");
            System.out.println("  System.out.println(cafe.descripcion() + \" = $\" + cafe.costo());");
            System.out.println("  // \"Cafe simple, leche, azucar = $2.7\"");
        }
    }

    static void ejercicio_3(int pista) {
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
        if (pista > 0) {
            System.out.println("\n========================================");
            System.out.println("PISTAS:");
        }
        if (pista >= 1) {
            System.out.println("\n🟢 PISTA 1 (Basica):");
            System.out.println("  - ProxyDocumento tiene DocumentoReal, usuario y rol");
            System.out.println("  - En mostrar(), verifica si el rol es \"admin\"");
            System.out.println("  - Si es admin, muestra el documento real");
            System.out.println("  - Si no, muestra \"Acceso denegado\"");
        }
        if (pista >= 2) {
            System.out.println("\n🟡 PISTA 2 (Intermedia):");
            System.out.println("  class ProxyDocumento implements Documento {\n" +
                "      private DocumentoReal doc;\n" +
                "      private String usuario;\n" +
                "      private String rol;\n" +
                "      public ProxyDocumento(String contenido, String u, String r) {\n" +
                "          this.doc = new DocumentoReal(contenido);\n" +
                "          this.usuario = u;\n" +
                "          this.rol = r;\n" +
                "      }\n" +
                "      public void mostrar() {\n" +
                "          if (\"admin\".equalsIgnoreCase(rol)) {\n" +
                "              System.out.println(\"Acceso concedido a \" + usuario);\n" +
                "              doc.mostrar();\n" +
                "          } else {\n" +
                "              System.out.println(\"Acceso DENEGADO para \" + usuario);\n" +
                "          }\n" +
                "      }\n" +
                "  }");
        }
        if (pista >= 3) {
            System.out.println("\n🔴 PISTA 3 (Avanzada - casi la solucion):");
            System.out.println("  new ProxyDocumento(\"Secreto\", \"Juan\", \"admin\").mostrar();");
            System.out.println("  new ProxyDocumento(\"Secreto\", \"Pedro\", \"invitado\").mostrar();");
        }
    }
}
