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
            System.out.println("=== MENU - Interfaces y Abstractas ===");
            System.out.println("1. Interfaz Dibujable");
            System.out.println("2. Clase abstracta Animal");
            System.out.println("3. Multiple implementacion (Pato)");
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
        System.out.println(">> EJERCICIO 1: Interfaz Dibujable");
        System.out.println("Crea interfaz Dibujable con metodos:");
        System.out.println("  - void dibujar()");
        System.out.println("  - void cambiarColor(String color)");
        System.out.println("Implementala en Circulo (atributo: radio) y Rectangulo (base, altura).");
        System.out.println("dibujar() debe imprimir \"Dibujando [forma] de color [color]\".");
        System.out.println();
        System.out.println("PISTA: 'interface Dibujable { void dibujar(); void cambiarColor(String c); }'");
        System.out.println("// --- TU CODIGO AQUI ---");
    }

    static void ejercicio_2() {
        System.out.println(">> EJERCICIO 2: Clase abstracta Animal");
        System.out.println("Clase abstracta Animal con:");
        System.out.println("  - Atributo: nombre (protected)");
        System.out.println("  - Constructor que recibe nombre");
        System.out.println("  - Metodo concreto: dormir()");
        System.out.println("  - Metodo abstracto: hacerSonido()");
        System.out.println("Subclases Perro y Gato implementan hacerSonido().");
        System.out.println();
        System.out.println("PISTA: 'abstract class Animal { public abstract void hacerSonido(); }'");
        System.out.println("// --- TU CODIGO AQUI ---");
    }

    static void ejercicio_3() {
        System.out.println(">> EJERCICIO 3: Multiple implementacion");
        System.out.println("Interfaz Nadador: void nadar()");
        System.out.println("Interfaz Caminador: void caminar()");
        System.out.println("Clase Pato implementa ambas interfaces.");
        System.out.println("Ademas Pato tiene su propio metodo: void volar().");
        System.out.println("En el main, crea un Pato y llama a los 3 metodos.");
        System.out.println();
        System.out.println("PISTA: 'class Pato implements Nadador, Caminador'");
        System.out.println("// --- TU CODIGO AQUI ---");
    }

    static void mostrarPista(int n) {
        String[][] pistas = {
            {
                "Pista 1: Interfaz: todos los metodos son public abstract implicito",
                "Pista 2: 'class Circulo implements Dibujable { ... }'",
                "Pista 3: 'implements' no 'extends' para interfaces"
            },
            {
                "Pista 1: Clase abstracta: 'public abstract class Animal'",
                "Pista 2: Metodo abstracto: 'public abstract void hacerSonido();'",
                "Pista 3: 'class Perro extends Animal { @Override public void hacerSonido() {...} }'"
            },
            {
                "Pista 1: 'interface Nadador { void nadar(); }'",
                "Pista 2: 'interface Caminador { void caminar(); }'",
                "Pista 3: 'class Pato implements Nadador, Caminador' (separado por coma)"
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
