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
            System.out.println("=== PATRONES CREACIONALES - EJERCICIOS ===");
            System.out.println("1. Singleton - Logger");
            System.out.println("2. Factory Method - Figuras");
            System.out.println("3. Builder - Computadora");
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

    // Singleton - Logger
    static void ejercicio_1() {
        System.out.println("=== EJERCICIO 1: Singleton - Logger ===");
        System.out.println("Crea una clase Logger que implemente el patron Singleton.");
        System.out.println("Debe tener un metodo log(String mensaje) que imprima con");
        System.out.println("fecha y hora actual, y un metodo getInstance() estatico.");
        System.out.println();
        System.out.println("Requisitos:");
        System.out.println("- Constructor privado");
        System.out.println("- Unico punto de acceso estatico");
        System.out.println("- Metodo log() con timestamp");
        System.out.println("- Demostrar que solo existe una instancia");
        System.out.println();
        System.out.println("Pista: Usa 'javac Ejercicios.java && java Ejercicios 1 -p'");
    }

    // Factory Method - Figuras
    static void ejercicio_2() {
        System.out.println("=== EJERCICIO 2: Factory Method - Figuras ===");
        System.out.println("Implementa un factory method para crear figuras geometricas.");
        System.out.println("Debe soportar: Circulo, Cuadrado y Triangulo.");
        System.out.println();
        System.out.println("Requisitos:");
        System.out.println("- Interface Figura con metodo dibujar()");
        System.out.println("- Tres clases concretas que implementen Figura");
        System.out.println("- Clase FiguraFactory con metodo crearFigura(String tipo)");
        System.out.println("- Usar Scanner para que el usuario elija la figura");
        System.out.println();
        System.out.println("Pista: Usa 'javac Ejercicios.java && java Ejercicios 2 -p'");
    }

    // Builder - Computadora
    static void ejercicio_3() {
        System.out.println("=== EJERCICIO 3: Builder - Computadora ===");
        System.out.println("Crea una clase Computadora usando el patron Builder.");
        System.out.println("Atributos: CPU, RAM, almacenamiento, tarjeta grafica,");
        System.out.println("y sistema operativo (todos opcionales con valores por defecto).");
        System.out.println();
        System.out.println("Requisitos:");
        System.out.println("- Constructor privado de Computadora");
        System.out.println("- Clase Builder interna estatica");
        System.out.println("- Cada setter del Builder devuelve this (fluent interface)");
        System.out.println("- Metodo build() que crea la Computadora");
        System.out.println("- toString() que muestre la configuracion");
        System.out.println();
        System.out.println("Pista: Usa 'javac Ejercicios.java && java Ejercicios 3 -p'");
    }

    static void mostrarPista(int n) {
        String[] pistas = {
            "", // indice 0 no usado
            "PISTA 1: Declara un campo 'private static Logger instancia'. El constructor debe ser private. " +
            "En getInstance() usa 'if (instancia == null) instancia = new Logger(); return instancia;'. " +
            "Usa java.time.LocalDateTime.now() para el timestamp.",
            "PISTA 2: Crea la interfaz 'Figura' con metodo 'void dibujar()'. " +
            "Cada clase concreta implementa Figura. En FiguraFactory usa un switch o if-else. " +
            "Usa scanner.nextLine() para leer el tipo y pasar a FiguraFactory.crearFigura().",
            "PISTA 3: La clase Computadora tiene constructor privado que recibe Builder. " +
            "Builder tiene los mismos atributos con valores por defecto (CPU='i5', RAM=8, etc.). " +
            "Cada metodo setter retorna 'this' para encadenar llamadas. " +
            "Ejemplo: new Computadora.Builder().cpu(\"i7\").ram(16).build();"
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
