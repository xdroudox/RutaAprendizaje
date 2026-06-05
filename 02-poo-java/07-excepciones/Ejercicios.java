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
        while (true) {
            System.out.println("=== MENU - Excepciones ===");
            System.out.println("1. Division segura");
            System.out.println("2. Excepcion personalizada (Edad)");
            System.out.println("3. try-with-resources y finally");
            System.out.println("0. Salir");
            System.out.print("Selecciona un ejercicio: ");
            String opt = sc.nextLine();
            if (opt.equals("0")) break;
            try {
                int n = Integer.parseInt(opt);
                ejecutarEjercicio(n);
            } catch (NumberFormatException e) {
                System.out.println("Opcion invalida");
            }
        }
        sc.close();
    }

    static void ejecutarEjercicio(int n) {
        switch (n) {
            case 1: ejercicio_1(); break;
            case 2: ejercicio_2(); break;
            case 3: ejercicio_3(); break;
            default: System.out.println("Ejercicio no encontrado");
        }
    }

    static void ejercicio_1() {
        System.out.println(">> EJERCICIO 1: Division segura");
        System.out.println("Programa que pide 2 numeros y muestra la division.");
        System.out.println("Maneja las excepciones:");
        System.out.println("  - ArithmeticException (dividir por cero)");
        System.out.println("  - InputMismatchException (entrada no numerica)");
        System.out.println("Repite hasta que los datos sean validos.");
        System.out.println();
        System.out.println("PISTA: Usa try-catch dentro de un while(true).");
        System.out.println("// --- TU CODIGO AQUI ---");
    }

    static void ejercicio_2() {
        System.out.println(">> EJERCICIO 2: Excepcion personalizada");
        System.out.println("Crea EdadInvalidaException extends Exception.");
        System.out.println("Clase Persona con atributo edad.");
        System.out.println("El setter lanza EdadInvalidaException si edad < 0 o > 150.");
        System.out.println("En el main, captura y maneja la excepcion.");
        System.out.println();
        System.out.println("PISTA: 'class EdadInvalidaException extends Exception'");
        System.out.println("// --- TU CODIGO AQUI ---");
    }

    static void ejercicio_3() {
        System.out.println(">> EJERCICIO 3: try-with-resources y finally");
        System.out.println("Programa que intenta leer un archivo 'datos.txt'.");
        System.out.println("Usa try-with-resources para FileReader y BufferedReader.");
        System.out.println("Captura FileNotFoundException si el archivo no existe.");
        System.out.println("Usa finally que siempre imprima \"Operacion finalizada\".");
        System.out.println();
        System.out.println("PISTA: 'try (FileReader fr = new FileReader(\"datos.txt\"); ...)'");
        System.out.println("// --- TU CODIGO AQUI ---");
    }

    static void mostrarPista(int n) {
        String[][] pistas = {
            {
                "Pista 1: try { int r = a / b; } catch (ArithmeticException e) { ... }",
                "Pista 2: Usa Scanner con hasNextInt() o try-catch con InputMismatchException",
                "Pista 3: 'while (true) { try { ... break; } catch (...) { ... } }'"
            },
            {
                "Pista 1: 'class EdadInvalidaException extends Exception { public EdadInvalidaException(String msg) { super(msg); } }'",
                "Pista 2: 'if (edad < 0) throw new EdadInvalidaException(...)'",
                "Pista 3: 'try { p.setEdad(-5); } catch (EdadInvalidaException e) { ... }'"
            },
            {
                "Pista 1: 'try (BufferedReader br = new BufferedReader(new FileReader(\"datos.txt\")))'",
                "Pista 2: 'catch (FileNotFoundException e) { ... }'",
                "Pista 3: 'finally { System.out.println(\"Operacion finalizada\"); }'"
            }
        };
        if (n >= 1 && n <= pistas.length) {
            for (String p : pistas[n - 1]) {
                System.out.println(p);
            }
        }
    }

    static void mostrarSolucion(int n) {
        Soluciones.main(new String[]{String.valueOf(n)});
    }
}
