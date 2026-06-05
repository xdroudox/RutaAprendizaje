import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Soluciones {
    public static void main(String[] args) {
        if (args.length == 0) {
            for (int i = 1; i <= 3; i++) {
                System.out.println("--- Solucion " + i + " ---");
                ejecutarSolucion(i);
                System.out.println();
            }
        } else {
            int num = Integer.parseInt(args[0]);
            ejecutarSolucion(num);
        }
    }

    static void ejecutarSolucion(int n) {
        switch (n) {
            case 1: solucion_1(); break;
            case 2: solucion_2(); break;
            case 3: solucion_3(); break;
            default: System.out.println("Solucion no valida");
        }
    }

    // ============================================================
    // SOLUCION 1: Observer - Notificaciones
    // ============================================================
    interface Suscriptor {
        void actualizar(String noticia);
    }

    static class EmailSuscriptor implements Suscriptor {
        private String email;

        public EmailSuscriptor(String email) {
            this.email = email;
        }

        public void actualizar(String noticia) {
            System.out.println("EMAIL a " + email + ": Nueva noticia - " + noticia);
        }
    }

    static class SMSsuscriptor implements Suscriptor {
        private String telefono;

        public SMSsuscriptor(String telefono) {
            this.telefono = telefono;
        }

        public void actualizar(String noticia) {
            System.out.println("SMS a " + telefono + ": " + noticia);
        }
    }

    static class AppSuscriptor implements Suscriptor {
        private String nombreApp;

        public AppSuscriptor(String nombreApp) {
            this.nombreApp = nombreApp;
        }

        public void actualizar(String noticia) {
            System.out.println("PUSH [" + nombreApp + "]: " + noticia);
        }
    }

    static class CanalNoticias {
        private List<Suscriptor> suscriptores = new ArrayList<>();

        public void suscribir(Suscriptor s) {
            suscriptores.add(s);
            System.out.println("Nuevo suscriptor anadido.");
        }

        public void desuscribir(Suscriptor s) {
            suscriptores.remove(s);
            System.out.println("Suscriptor eliminado.");
        }

        public void publicarNoticia(String noticia) {
            System.out.println("PUBLICANDO NOTICIA: " + noticia);
            for (Suscriptor s : suscriptores) {
                s.actualizar(noticia);
            }
        }
    }

    static void solucion_1() {
        System.out.println("IMPLEMENTACION: Observer - Notificaciones");
        System.out.println("=========================================");
        System.out.println("""
    interface Suscriptor { void actualizar(String noticia); }
    
    class CanalNoticias {
        private List<Suscriptor> suscriptores = new ArrayList<>();
        
        public void suscribir(Suscriptor s) { suscriptores.add(s); }
        public void desuscribir(Suscriptor s) { suscriptores.remove(s); }
        public void publicarNoticia(String noticia) {
            for (Suscriptor s : suscriptores) {
                s.actualizar(noticia);
            }
        }
    }
    // EmailSuscriptor, SMSsuscriptor, AppSuscriptor implementan Suscriptor
        """);
        System.out.println("DEMOSTRACION:");
        CanalNoticias canal = new CanalNoticias();
        Suscriptor email = new EmailSuscriptor("javier@email.com");
        Suscriptor sms = new SMSsuscriptor("555-1234");
        Suscriptor app = new AppSuscriptor("NoticiasApp");
        canal.suscribir(email);
        canal.suscribir(sms);
        canal.suscribir(app);
        canal.publicarNoticia("Lanzamiento del nuevo framework Java 21");
        System.out.println();
        canal.desuscribir(sms);
        canal.publicarNoticia("Actualizacion de seguridad importante");
    }

    // ============================================================
    // SOLUCION 2: Strategy - Ordenamiento
    // ============================================================
    interface EstrategiaOrdenamiento {
        void ordenar(int[] arr);
    }

    static class BubbleSort implements EstrategiaOrdenamiento {
        public void ordenar(int[] arr) {
            int n = arr.length;
            for (int i = 0; i < n - 1; i++) {
                for (int j = 0; j < n - i - 1; j++) {
                    if (arr[j] > arr[j + 1]) {
                        int tmp = arr[j];
                        arr[j] = arr[j + 1];
                        arr[j + 1] = tmp;
                    }
                }
            }
        }
    }

    static class QuickSort implements EstrategiaOrdenamiento {
        public void ordenar(int[] arr) {
            quickSort(arr, 0, arr.length - 1);
        }

        private void quickSort(int[] arr, int low, int high) {
            if (low < high) {
                int pi = partition(arr, low, high);
                quickSort(arr, low, pi - 1);
                quickSort(arr, pi + 1, high);
            }
        }

        private int partition(int[] arr, int low, int high) {
            int pivot = arr[high];
            int i = low - 1;
            for (int j = low; j < high; j++) {
                if (arr[j] < pivot) {
                    i++;
                    int tmp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = tmp;
                }
            }
            int tmp = arr[i + 1];
            arr[i + 1] = arr[high];
            arr[high] = tmp;
            return i + 1;
        }
    }

    static class ContextoOrdenamiento {
        private EstrategiaOrdenamiento estrategia;

        public void setEstrategia(EstrategiaOrdenamiento e) {
            this.estrategia = e;
        }

        public void ejecutar(int[] arr) {
            if (estrategia == null) {
                System.out.println("Error: No hay estrategia definida");
                return;
            }
            estrategia.ordenar(arr);
        }
    }

    static void solucion_2() {
        System.out.println("IMPLEMENTACION: Strategy - Ordenamiento");
        System.out.println("=======================================");
        System.out.println("""
    interface EstrategiaOrdenamiento { void ordenar(int[] arr); }
    
    class BubbleSort implements EstrategiaOrdenamiento {
        public void ordenar(int[] arr) {
            // Dos bucles, intercambiar adyacentes
        }
    }
    
    class QuickSort implements EstrategiaOrdenamiento {
        public void ordenar(int[] arr) {
            quickSort(arr, 0, arr.length - 1);
        }
        // Particion y recursion
    }
    
    class ContextoOrdenamiento {
        private EstrategiaOrdenamiento estrategia;
        public void setEstrategia(EstrategiaOrdenamiento e) { this.estrategia = e; }
        public void ejecutar(int[] arr) { estrategia.ordenar(arr); }
    }
        """);
        System.out.println("DEMOSTRACION:");
        int[] datos = {64, 34, 25, 12, 22, 11, 90};
        System.out.println("Array original: " + Arrays.toString(datos));

        ContextoOrdenamiento contexto = new ContextoOrdenamiento();
        contexto.setEstrategia(new BubbleSort());
        int[] copia1 = Arrays.copyOf(datos, datos.length);
        contexto.ejecutar(copia1);
        System.out.println("BubbleSort: " + Arrays.toString(copia1));

        contexto.setEstrategia(new QuickSort());
        int[] copia2 = Arrays.copyOf(datos, datos.length);
        contexto.ejecutar(copia2);
        System.out.println("QuickSort: " + Arrays.toString(copia2));
    }

    // ============================================================
    // SOLUCION 3: Template Method - Procesamiento de Datos
    // ============================================================
    static abstract class ProcesadorDatos {
        public final void procesar() {
            System.out.println("--- Iniciando procesamiento ---");
            leerDatos();
            transformar();
            guardar();
            System.out.println("--- Procesamiento completado ---");
        }

        protected abstract void leerDatos();
        protected abstract void transformar();

        protected void guardar() {
            System.out.println("Guardando datos en base de datos...");
        }
    }

    static class ProcesadorCSV extends ProcesadorDatos {
        private String datos;

        protected void leerDatos() {
            System.out.println("Leyendo archivo CSV...");
            datos = "nombre,edad\nJuan,30\nMaria,25";
        }

        protected void transformar() {
            System.out.println("Transformando datos CSV a mayusculas...");
            datos = datos.toUpperCase();
            System.out.println("Datos transformados:\n" + datos);
        }
    }

    static class ProcesadorJSON extends ProcesadorDatos {
        private String datos;

        protected void leerDatos() {
            System.out.println("Leyendo archivo JSON...");
            datos = "{\"usuarios\":[{\"id\":1,\"nombre\":\"Juan\"},{\"id\":2,\"nombre\":\"Ana\"}]}";
        }

        protected void transformar() {
            System.out.println("Parseando JSON y extrayendo nombres...");
            datos = datos.replace("{", "").replace("}", "")
                         .replace("\"", "").replace("[", "").replace("]", "");
            System.out.println("Datos procesados:\n" + datos);
        }

        protected void guardar() {
            System.out.println("Guardando datos en base de datos NoSQL...");
        }
    }

    static void solucion_3() {
        System.out.println("IMPLEMENTACION: Template Method - Procesamiento de Datos");
        System.out.println("=======================================================");
        System.out.println("""
    abstract class ProcesadorDatos {
        public final void procesar() {
            leerDatos();
            transformar();
            guardar();
        }
        protected abstract void leerDatos();
        protected abstract void transformar();
        protected void guardar() { /* default */ }
    }
    
    class ProcesadorCSV extends ProcesadorDatos { ... }
    class ProcesadorJSON extends ProcesadorDatos { ... }
        """);
        System.out.println("DEMOSTRACION:");
        ProcesadorDatos csv = new ProcesadorCSV();
        csv.procesar();
        System.out.println();
        ProcesadorDatos json = new ProcesadorJSON();
        json.procesar();
    }
}
