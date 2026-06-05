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
            System.out.println("=== PATRONES ESTRUCTURALES - EJERCICIOS ===");
            System.out.println("1. Adapter - Enchufes");
            System.out.println("2. Decorator - Cafe");
            System.out.println("3. Proxy - Control de Acceso");
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

    // Adapter - Enchufes
    static void ejercicio_1() {
        System.out.println("=== EJERCICIO 1: Adapter - Enchufes ===");
        System.out.println("Implementa un adaptador que permita conectar un");
        System.out.println("enchufe europeo (220V, clavija redonda) en un");
        System.out.println("tomacorriente americano (110V, clavija plana).");
        System.out.println();
        System.out.println("Requisitos:");
        System.out.println("- Interface EnchufeEuropeo con metodo conectar()");
        System.out.println("- Interface EnchufeAmericano con metodo plugIn()");
        System.out.println("- Clase AdaptadorEuropeoAamericano que implemente EnchufeAmericano");
        System.out.println("- El adaptador debe permitir cualquier enchufe europeo");
        System.out.println();
        System.out.println("Pista: Usa 'javac Ejercicios.java && java Ejercicios 1 -p'");
    }

    // Decorator - Cafe
    static void ejercicio_2() {
        System.out.println("=== EJERCICIO 2: Decorator - Cafe ===");
        System.out.println("Implementa un sistema de cafe con ingredientes");
        System.out.println("adicionales usando el patron Decorator.");
        System.out.println();
        System.out.println("Requisitos:");
        System.out.println("- Interface Bebida con costo() y descripcion()");
        System.out.println("- Clase base CafeSimple");
        System.out.println("- Decoradores: Leche, Azucar, Crema, Chocolate");
        System.out.println("- Cada decorador anade su costo y modifica la descripcion");
        System.out.println("- Demostrar combinaciones (cafe con leche y azucar, etc.)");
        System.out.println();
        System.out.println("Pista: Usa 'javac Ejercicios.java && java Ejercicios 2 -p'");
    }

    // Proxy - Control de Acceso
    static void ejercicio_3() {
        System.out.println("=== EJERCICIO 3: Proxy - Control de Acceso ===");
        System.out.println("Implementa un proxy de control de acceso que");
        System.out.println("verifique credenciales antes de delegar en el objeto real.");
        System.out.println();
        System.out.println("Requisitos:");
        System.out.println("- Interface Servicio con metodo ejecutar()");
        System.out.println("- Clase ServicioReal que ejecuta la accion");
        System.out.println("- Clase ProxyServicio que verifica autenticacion");
        System.out.println("- Solo usuarios autenticados pueden ejecutar");
        System.out.println("- Usar una lista simple de usuarios validos");
        System.out.println();
        System.out.println("Pista: Usa 'javac Ejercicios.java && java Ejercicios 3 -p'");
    }

    static void mostrarPista(int n) {
        String[] pistas = {
            "",
            "PISTA 1: Crea 'interface EnchufeEuropeo { void conectar(); }' " +
            "y 'interface EnchufeAmericano { void plugIn(); }'. " +
            "El adaptador recibe un EnchufeEuropeo en el constructor y llama a " +
            "conectar() desde plugIn(). Crea una clase Lavadora que implemente EnchufeEuropeo.",
            "PISTA 2: Crea 'interface Bebida { double costo(); String descripcion(); }'. " +
            "CafeSimple implements Bebida. El decorador abstracto implementa Bebida " +
            "y tiene un campo Bebida protegido. Cada decorador concreto extiende " +
            "el decorador y modifica costo() y descripcion().",
            "PISTA 3: Crea 'interface Servicio { void ejecutar(String usuario); }'. " +
            "ServicioReal ejecuta imprimiendo 'Ejecutando...'. " +
            "ProxyServicio tiene un Set<String> de usuarios validos y un ServicioReal. " +
            "Si el usuario esta en el set, delega; si no, deniega el acceso."
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
