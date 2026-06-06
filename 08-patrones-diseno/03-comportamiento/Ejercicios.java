/**
 * EJERCICIOS - Patrones de Comportamiento
 * Ejecuta desde raiz: python scripts/runner.py 8 3 [ejercicio] [-p N]
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
            System.out.println("  🟢 Ej 1: Observer - Editorial notifica suscriptores");
            System.out.println("  🟡 Ej 2: Strategy - Ordenar lista con diferentes estrategias");
            System.out.println("  🟡 Ej 3: Template Method - Procesar datos con plantilla");
        }
    }

    static void ejercicio_1(int pista) {
        System.out.println(">> EJERCICIO 1: Observer - Editorial");
        System.out.println("-".repeat(40));
        System.out.println("Una Editorial publica noticias. Los suscriptores");
        System.out.println("reciben las noticias automaticamente.");
        System.out.println();
        System.out.println("interface Suscriptor { void notificar(String noticia); }");
        System.out.println("class Editorial {");
        System.out.println("    private List<Suscriptor> suscriptores = new ArrayList<>();");
        System.out.println("    public void suscribir(Suscriptor s) { ... }");
        System.out.println("    public void publicar(String noticia) { ... }");
        System.out.println("    // ==== ESCRIBE TU RESPUESTA AQUI ====");
        System.out.println("}");
        if (pista > 0) {
            System.out.println("\n========================================");
            System.out.println("PISTAS:");
        }
        if (pista >= 1) {
            System.out.println("\n🟢 PISTA 1 (Basica):");
            System.out.println("  - Editorial mantiene una lista de suscriptores");
            System.out.println("  - suscribir(Suscriptor s): agrega s a la lista");
            System.out.println("  - publicar(String noticia): recorre la lista y llama a s.notificar(noticia)");
            System.out.println("  - Suscriptor puede ser una interfaz o clase abstracta");
        }
        if (pista >= 2) {
            System.out.println("\n🟡 PISTA 2 (Intermedia):");
            System.out.println("  interface Suscriptor { void notificar(String noticia); }");
            System.out.println("  class SuscriptorEmail implements Suscriptor {\n" +
                "      private String email;\n" +
                "      public SuscriptorEmail(String e) { this.email = e; }\n" +
                "      public void notificar(String noticia) {\n" +
                "          System.out.println(\"EMAIL a \" + email + \": \" + noticia);\n" +
                "      }\n" +
                "  }");
            System.out.println("  class Editorial {\n" +
                "      private java.util.List<Suscriptor> suscriptores = new java.util.ArrayList<>();\n" +
                "      public void suscribir(Suscriptor s) { suscriptores.add(s); }\n" +
                "      public void publicar(String noticia) {\n" +
                "          for (Suscriptor s : suscriptores) s.notificar(noticia);\n" +
                "      }\n" +
                "  }");
        }
        if (pista >= 3) {
            System.out.println("\n🔴 PISTA 3 (Avanzada - casi la solucion):");
            System.out.println("  Editorial ed = new Editorial();");
            System.out.println("  ed.suscribir(new SuscriptorEmail(\"a@test.com\"));");
            System.out.println("  ed.suscribir(new SuscriptorEmail(\"b@test.com\"));");
            System.out.println("  ed.publicar(\"Nuevo libro de Java 21!\");");
            System.out.println("  // Ambos suscriptores reciben la noticia");
        }
    }

    static void ejercicio_2(int pista) {
        System.out.println(">> EJERCICIO 2: Strategy - Ordenamiento");
        System.out.println("-".repeat(40));
        System.out.println("Implementa diferentes estrategias de ordenamiento");
        System.out.println("(BubbleSort, QuickSort) intercambiables.");
        System.out.println();
        System.out.println("interface EstrategiaOrdenamiento { void ordenar(int[] arr); }");
        System.out.println("class BubbleSort implements EstrategiaOrdenamiento { ... }");
        System.out.println("class QuickSort implements EstrategiaOrdenamiento { ... }");
        System.out.println("class Contexto {");
        System.out.println("    private EstrategiaOrdenamiento estrategia;");
        System.out.println("    public void setEstrategia(EstrategiaOrdenamiento e) { ... }");
        System.out.println("    public void ejecutar(int[] arr) { ... }");
        System.out.println("    // ==== ESCRIBE TU RESPUESTA AQUI ====");
        System.out.println("}");
        if (pista > 0) {
            System.out.println("\n========================================");
            System.out.println("PISTAS:");
        }
        if (pista >= 1) {
            System.out.println("\n🟢 PISTA 1 (Basica):");
            System.out.println("  - BubbleSort: dos bucles anidados, intercambia si arr[j] > arr[j+1]");
            System.out.println("  - QuickSort: puedes usar java.util.Arrays.sort(arr) como simplificacion");
            System.out.println("  - Contexto tiene setEstrategia() y ejecutar() que llama a estrategia.ordenar()");
        }
        if (pista >= 2) {
            System.out.println("\n🟡 PISTA 2 (Intermedia):");
            System.out.println("  class BubbleSort implements EstrategiaOrdenamiento {\n" +
                "      public void ordenar(int[] arr) {\n" +
                "          for (int i = 0; i < arr.length - 1; i++)\n" +
                "              for (int j = 0; j < arr.length - i - 1; j++)\n" +
                "                  if (arr[j] > arr[j + 1]) {\n" +
                "                      int tmp = arr[j]; arr[j] = arr[j+1]; arr[j+1] = tmp;\n" +
                "                  }\n" +
                "      }\n" +
                "  }");
            System.out.println("  class QuickSort implements EstrategiaOrdenamiento {\n" +
                "      public void ordenar(int[] arr) { java.util.Arrays.sort(arr); }\n" +
                "  }");
            System.out.println("  class Contexto {\n" +
                "      private EstrategiaOrdenamiento estrategia;\n" +
                "      public void setEstrategia(EstrategiaOrdenamiento e) { this.estrategia = e; }\n" +
                "      public void ejecutar(int[] arr) { estrategia.ordenar(arr); }\n" +
                "  }");
        }
        if (pista >= 3) {
            System.out.println("\n🔴 PISTA 3 (Avanzada - casi la solucion):");
            System.out.println("  int[] datos = {5, 2, 8, 1, 9};");
            System.out.println("  Contexto ctx = new Contexto();");
            System.out.println("  ctx.setEstrategia(new BubbleSort());");
            System.out.println("  ctx.ejecutar(datos);");
            System.out.println("  // Cambiar estrategia en tiempo real:");
            System.out.println("  ctx.setEstrategia(new QuickSort());");
        }
    }

    static void ejercicio_3(int pista) {
        System.out.println(">> EJERCICIO 3: Template Method");
        System.out.println("-".repeat(40));
        System.out.println("Define el esqueleto de un algoritmo de procesamiento");
        System.out.println("de datos. Pasos: leer, procesar, guardar.");
        System.out.println();
        System.out.println("abstract class ProcesadorDatos {");
        System.out.println("    public final void procesar() {");
        System.out.println("        leer();");
        System.out.println("        transformar();");
        System.out.println("        guardar();");
        System.out.println("    }");
        System.out.println("    protected abstract void leer();");
        System.out.println("    protected abstract void transformar();");
        System.out.println("    protected void guardar() { /* default */ }");
        System.out.println("    // ==== ESCRIBE TU RESPUESTA AQUI ====");
        System.out.println("}");
        if (pista > 0) {
            System.out.println("\n========================================");
            System.out.println("PISTAS:");
        }
        if (pista >= 1) {
            System.out.println("\n🟢 PISTA 1 (Basica):");
            System.out.println("  - El metodo procesar() es final (no se puede sobrescribir)");
            System.out.println("  - leer() y transformar() son abstractos (cada subclase los implementa)");
            System.out.println("  - guardar() tiene implementacion por defecto (opcional sobrescribir)");
        }
        if (pista >= 2) {
            System.out.println("\n🟡 PISTA 2 (Intermedia):");
            System.out.println("  abstract class ProcesadorDatos {\n" +
                "      public final void procesar() {\n" +
                "          leer(); transformar(); guardar();\n" +
                "      }\n" +
                "      protected abstract void leer();\n" +
                "      protected abstract void transformar();\n" +
                "      protected void guardar() {\n" +
                "          System.out.println(\"Guardando datos...\");\n" +
                "      }\n" +
                "  }");
            System.out.println("  class ProcesadorCSV extends ProcesadorDatos {\n" +
                "      private String datos;\n" +
                "      protected void leer() {\n" +
                "          datos = \"nombre,edad\";\n" +
                "          System.out.println(\"Leyendo CSV: \" + datos);\n" +
                "      }\n" +
                "      protected void transformar() {\n" +
                "          datos = datos.toUpperCase();\n" +
                "          System.out.println(\"Transformado: \" + datos);\n" +
                "      }\n" +
                "  }");
        }
        if (pista >= 3) {
            System.out.println("\n🔴 PISTA 3 (Avanzada - casi la solucion):");
            System.out.println("  ProcesadorDatos p = new ProcesadorCSV();");
            System.out.println("  p.procesar();");
            System.out.println("  // Output: Leyendo CSV: nombre,edad");
            System.out.println("  //         Transformado: NOMBRE,EDAD");
            System.out.println("  //         Guardando datos...");
        }
    }
}
