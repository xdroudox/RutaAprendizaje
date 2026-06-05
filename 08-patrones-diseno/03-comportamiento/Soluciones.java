/**
 * SOLUCIONES - Patrones de Comportamiento
 * Ejecuta desde raiz: python scripts/runner.py 8 3 [ejercicio]
 */
public class Soluciones {
    public static void main(String[] args) {
        if (args.length > 0) {
            int num = Integer.parseInt(args[0]);
            switch (num) {
                case 1: ejercicio_1(); break;
                case 2: ejercicio_2(); break;
                case 3: ejercicio_3(); break;
            }
        } else {
            for (int i = 1; i <= 3; i++) {
                System.out.println("  " + i + ". [Solucion " + i + "]");
            }
        }
    }

    static void ejercicio_1() {
        System.out.println(">> SOLUCION 1: Observer - Editorial");
        System.out.println("-".repeat(40));

        java.util.List<String> notificaciones = new java.util.ArrayList<>();

        interface Suscriptor {
            void notificar(String noticia);
        }

        class SuscriptorEmail implements Suscriptor {
            private String email;
            public SuscriptorEmail(String e) { this.email = e; }
            public void notificar(String noticia) {
                notificaciones.add("EMAIL a " + email + ": " + noticia);
            }
        }

        class Editorial {
            private java.util.List<Suscriptor> suscriptores = new java.util.ArrayList<>();
            public void suscribir(Suscriptor s) { suscriptores.add(s); }
            public void publicar(String noticia) {
                for (Suscriptor s : suscriptores) {
                    s.notificar(noticia);
                }
            }
        }

        Editorial ed = new Editorial();
        ed.suscribir(new SuscriptorEmail("a@test.com"));
        ed.suscribir(new SuscriptorEmail("b@test.com"));
        ed.publicar("Nuevo libro de Java 21!");
        notificaciones.forEach(System.out::println);
    }

    static void ejercicio_2() {
        System.out.println(">> SOLUCION 2: Strategy - Ordenamiento");
        System.out.println("-".repeat(40));

        interface EstrategiaOrdenamiento {
            void ordenar(int[] arr);
        }

        class BubbleSort implements EstrategiaOrdenamiento {
            public void ordenar(int[] arr) {
                for (int i = 0; i < arr.length - 1; i++) {
                    for (int j = 0; j < arr.length - i - 1; j++) {
                        if (arr[j] > arr[j + 1]) {
                            int tmp = arr[j];
                            arr[j] = arr[j + 1];
                            arr[j + 1] = tmp;
                        }
                    }
                }
            }
        }

        class QuickSort implements EstrategiaOrdenamiento {
            public void ordenar(int[] arr) {
                java.util.Arrays.sort(arr);
            }
        }

        class Contexto {
            private EstrategiaOrdenamiento estrategia;
            public void setEstrategia(EstrategiaOrdenamiento e) { this.estrategia = e; }
            public void ejecutar(int[] arr) { estrategia.ordenar(arr); }
        }

        int[] datos = {5, 2, 8, 1, 9};
        Contexto ctx = new Contexto();
        ctx.setEstrategia(new BubbleSort());
        ctx.ejecutar(datos);
        System.out.print("BubbleSort: ");
        for (int n : datos) System.out.print(n + " ");
        System.out.println();
    }

    static void ejercicio_3() {
        System.out.println(">> SOLUCION 3: Template Method");
        System.out.println("-".repeat(40));

        abstract class ProcesadorDatos {
            public final void procesar() {
                leer();
                transformar();
                guardar();
            }
            protected abstract void leer();
            protected abstract void transformar();
            protected void guardar() {
                System.out.println("Guardando datos...");
            }
        }

        class ProcesadorCSV extends ProcesadorDatos {
            private String datos;
            protected void leer() {
                datos = "nombre,edad";
                System.out.println("Leyendo CSV: " + datos);
            }
            protected void transformar() {
                datos = datos.toUpperCase();
                System.out.println("Transformado: " + datos);
            }
        }

        ProcesadorDatos p = new ProcesadorCSV();
        p.procesar();
    }
}
