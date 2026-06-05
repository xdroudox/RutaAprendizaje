/**
 * EJERCICIOS - Patrones de Comportamiento
 * Ejecuta desde raiz: python scripts/runner.py 8 3 [ejercicio]
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
            System.out.println("1. Observer - Editorial notifica suscriptores");
            System.out.println("2. Strategy - Ordenar lista con diferentes estrategias");
            System.out.println("3. Template Method - Procesar datos con plantilla");
        }
    }

    static void ejercicio_1() {
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
    }

    static void ejercicio_2() {
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
    }

    static void ejercicio_3() {
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
    }
}
