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
            System.out.println("=== MENU - Polimorfismo ===");
            System.out.println("1. Sobrecarga de metodos (Impresora)");
            System.out.println("2. Polimorfismo con animales");
            System.out.println("3. Sistema de pagos (Pagable)");
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
        System.out.println(">> EJERCICIO 1: Sobrecarga de metodos");
        System.out.println("Crea clase Impresora con metodos sobrecargados:");
        System.out.println("  - imprimir(String texto)");
        System.out.println("  - imprimir(int numero)");
        System.out.println("  - imprimir(String texto, int veces)");
        System.out.println("  - imprimir(int[] numeros)");
        System.out.println("En el main, prueba todos los metodos.");
        System.out.println();
        System.out.println("PISTA: Misma firma = mismo nombre + diferentes parametros.");
        System.out.println("// --- TU CODIGO AQUI ---");
    }

    static void ejercicio_2() {
        System.out.println(">> EJERCICIO 2: Polimorfismo con animales");
        System.out.println("Clase base Animal con metodo hacerSonido().");
        System.out.println("Subclases Perro, Gato y Vaca que sobrescriben hacerSonido().");
        System.out.println("En el main, crea un array Animal[] y recorrelo con un bucle.");
        System.out.println();
        System.out.println("PISTA: Animal[] animales = {new Perro(), new Gato(), new Vaca()};");
        System.out.println("// --- TU CODIGO AQUI ---");
    }

    static void ejercicio_3() {
        System.out.println(">> EJERCICIO 3: Sistema de pagos");
        System.out.println("Interfaz Pagable con metodo double calcularPago().");
        System.out.println("Clase Factura: tiene montoFijo, calcularPago() devuelve el monto.");
        System.out.println("Clase Empleado: tiene salarioPorHora y horas, calcularPago() devuelve salario*horas.");
        System.out.println("En el main, crea un array Pagable[] y procesa los pagos.");
        System.out.println();
        System.out.println("PISTA: Empleado calcularPago = salarioPorHora * horas;");
        System.out.println("// --- TU CODIGO AQUI ---");
    }

    static void mostrarPista(int n) {
        String[][] pistas = {
            {
                "Pista 1: Sobrecarga = mismo nombre, diferentes parametros",
                "Pista 2: 'void imprimir(String texto)' y 'void imprimir(int numero)'",
                "Pista 3: 'void imprimir(int[] numeros)' usa for-each para imprimir"
            },
            {
                "Pista 1: Animal es la clase base con metodo hacerSonido()",
                "Pista 2: @Override en cada subclase",
                "Pista 3: for(Animal a : animales) { a.hacerSonido(); }"
            },
            {
                "Pista 1: 'interface Pagable { double calcularPago(); }'",
                "Pista 2: 'class Factura implements Pagable'",
                "Pista 3: Pagable[] pagos = {new Factura(100), new Empleado(15, 40)};"
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
