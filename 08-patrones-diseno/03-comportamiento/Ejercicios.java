import java.util.Scanner;

public class Ejercicios {
    public static void main(String[] args) {
        if (args.length == 0) {
            menu();
        } else if (args[0].equals("-s") && args.length > 1) {
            mostrarSolucion(Integer.parseInt(args[1]));
        } else {
            int num = Integer.parseInt(args[0]);
            if (args.length > 1 && args[1].equals("-p")) {
                mostrarPista(num);
            } else {
                ejecutarEjercicio(num);
            }
        }
    }

    static void menu() {
        Scanner sc = new Scanner(System.in);
        int opcion;
        do {
            System.out.println("=== PATRONES DE COMPORTAMIENTO - EJERCICIOS ===");
            System.out.println("1. Observer - Notificaciones");
            System.out.println("2. Strategy - Ordenamiento");
            System.out.println("3. Template Method - Procesamiento de Datos");
            System.out.println("0. Salir");
            System.out.print("Selecciona un ejercicio: ");
            opcion = sc.nextInt();
            if (opcion > 0 && opcion <= 3) {
                ejecutarEjercicio(opcion);
            }
        } while (opcion != 0);
        sc.close();
    }

    static void ejecutarEjercicio(int n) {
        switch (n) {
            case 1: ejercicio_1(); break;
            case 2: ejercicio_2(); break;
            case 3: ejercicio_3(); break;
            default: System.out.println("Ejercicio no valido");
        }
    }

    // Observer - Notificaciones
    static void ejercicio_1() {
        System.out.println("=== EJERCICIO 1: Observer - Notificaciones ===");
        System.out.println("Implementa un sistema de notificaciones donde un");
        System.out.println("canal de noticias notifique a multiples suscriptores.");
        System.out.println();
        System.out.println("Requisitos:");
        System.out.println("- Interface Suscriptor con metodo actualizar(String noticia)");
        System.out.println("- Clase CanalNoticias que mantiene una lista de suscriptores");
        System.out.println("- Metodos suscribir(), desuscribir() y publicarNoticia()");
        System.out.println("- Al menos 3 tipos de suscriptores: Email, SMS, App");
        System.out.println("- Cada suscriptor imprime la noticia a su manera");
        System.out.println();
        System.out.println("Pista: Usa 'javac Ejercicios.java && java Ejercicios 1 -p'");
    }

    // Strategy - Ordenamiento
    static void ejercicio_2() {
        System.out.println("=== EJERCICIO 2: Strategy - Ordenamiento ===");
        System.out.println("Implementa diferentes algoritmos de ordenamiento");
        System.out.println("usando el patron Strategy.");
        System.out.println();
        System.out.println("Requisitos:");
        System.out.println("- Interface EstrategiaOrdenamiento con metodo ordenar(int[])");
        System.out.println("- Implementa: BubbleSort y QuickSort");
        System.out.println("- Clase ContextoOrdenamiento que usa la estrategia");
        System.out.println("- El usuario puede elegir el algoritmo en tiempo de ejecucion");
        System.out.println("- Mostrar el array antes y despues de ordenar");
        System.out.println();
        System.out.println("Pista: Usa 'javac Ejercicios.java && java Ejercicios 2 -p'");
    }

    // Template Method - Procesamiento de Datos
    static void ejercicio_3() {
        System.out.println("=== EJERCICIO 3: Template Method - Procesamiento de Datos ===");
        System.out.println("Crea un procesador de datos con el patron Template Method.");
        System.out.println("Define el esqueleto del algoritmo y deja pasos a las subclases.");
        System.out.println();
        System.out.println("Requisitos:");
        System.out.println("- Clase abstracta ProcesadorDatos con metodo plantilla procesar()");
        System.out.println("- Pasos: leerDatos(), transformar(), guardar()");
        System.out.println("- Implementa ProcesadorCSV y ProcesadorJSON");
        System.out.println("- El paso guardar() puede tener implementacion por defecto");
        System.out.println("- Cada procesador implementa leer() y transformar() de forma distinta");
        System.out.println();
        System.out.println("Pista: Usa 'javac Ejercicios.java && java Ejercicios 3 -p'");
    }

    static void mostrarPista(int n) {
        String[] pistas = {
            "",
            "PISTA 1: Suscriptor tiene 'void actualizar(String noticia)'. " +
            "CanalNoticias tiene 'List<Suscriptor> suscriptores' y 'publicarNoticia(String n)'. " +
            "EmailSuscriptor imprime 'Email: ...', SMS imprime 'SMS: ...', App imprime 'App: ...'.",
            "PISTA 2: EstrategiaOrdenamiento con 'void ordenar(int[] arr)'. " +
            "BubbleSort: dos bucles anidados intercambiando adyacentes. " +
            "QuickSort: escoger pivote, particionar, recursion. " +
            "ContextoOrdenamiento tiene setStrategy() y ejecutar().",
            "PISTA 3: ProcesadorDatos tiene 'public final void procesar()' que llama " +
            "a leerDatos(), transformar(), guardar(). " +
            "ProcesadorCSV: leer simula datos CSV, transformar convierte a mayusculas. " +
            "ProcesadorJSON: leer simula datos JSON, transformar parsea campos."
        };
        if (n >= 1 && n <= 3) {
            System.out.println(pistas[n]);
        }
    }

    static void mostrarSolucion(int n) {
        if (n >= 1 && n <= 3) {
            Soluciones.main(new String[]{String.valueOf(n)});
        }
    }
}
