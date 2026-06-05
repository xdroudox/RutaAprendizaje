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
            System.out.println("=== MENU - Clases y Objetos ===");
            System.out.println("1. Crear clase Persona");
            System.out.println("2. Clase Rectangulo");
            System.out.println("3. Clase CuentaBancaria");
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

    // =============================================
    // EJERCICIO 1: Crear clase Persona
    // =============================================
    static void ejercicio_1() {
        System.out.println(">> EJERCICIO 1: Crear clase Persona");
        System.out.println("Crea una clase Persona con atributos: nombre, edad, dni.");
        System.out.println("Incluye un constructor que inicialice los tres atributos.");
        System.out.println("Incluye un metodo mostrarDatos() que imprima los datos.");
        System.out.println("En el main, crea dos personas y muestra sus datos.");
        System.out.println();
        System.out.println("PISTA: Usa this.nombre = nombre en el constructor.");
        System.out.println("// --- TU CODIGO AQUI ---");
    }

    // =============================================
    // EJERCICIO 2: Clase Rectangulo
    // =============================================
    static void ejercicio_2() {
        System.out.println(">> EJERCICIO 2: Clase Rectangulo");
        System.out.println("Crea una clase Rectangulo con atributos base y altura.");
        System.out.println("Incluye:");
        System.out.println("  - Constructor con parametros");
        System.out.println("  - calcularArea() que retorne double");
        System.out.println("  - calcularPerimetro() que retorne double");
        System.out.println("  - esCuadrado() que retorne boolean");
        System.out.println();
        System.out.println("PISTA: Perimetro = 2 * (base + altura)");
        System.out.println("// --- TU CODIGO AQUI ---");
    }

    // =============================================
    // EJERCICIO 3: Clase CuentaBancaria
    // =============================================
    static void ejercicio_3() {
        System.out.println(">> EJERCICIO 3: Clase CuentaBancaria");
        System.out.println("Crea una clase CuentaBancaria con titular, saldo, numeroCuenta.");
        System.out.println("Incluye:");
        System.out.println("  - Constructor que reciba titular y genere num. cuenta aleatorio");
        System.out.println("  - depositar(double) que incremente el saldo");
        System.out.println("  - retirar(double) que decremente el saldo si hay fondos");
        System.out.println("  - mostrarInfo() que muestre los datos");
        System.out.println();
        System.out.println("PISTA: Usa Math.random() para generar el numero de cuenta.");
        System.out.println("// --- TU CODIGO AQUI ---");
    }

    // =============================================
    // PISTAS
    // =============================================
    static void mostrarPista(int n) {
        String[][] pistas = {
            {
                "Pista 1: La clase se declara con 'public class Persona'",
                "Pista 2: El constructor tiene el mismo nombre que la clase",
                "Pista 3: Usa this para diferenciar atributos de parametros"
            },
            {
                "Pista 1: Usa double para base y altura",
                "Pista 2: Area = base * altura; Perimetro = 2*(base+altura)",
                "Pista 3: esCuadrado retorna base == altura"
            },
            {
                "Pista 1: Usa String para titular, double para saldo, String para numCuenta",
                "Pista 2: Math.random() genera un numero entre 0.0 y 1.0",
                "Pista 3: En retirar, verifica si hay saldo suficiente"
            }
        };
        if (n >= 1 && n <= pistas.length) {
            for (String p : pistas[n - 1]) {
                System.out.println(p);
            }
        }
    }

    // =============================================
    // SOLUCIONES
    // =============================================
    static void mostrarSolucion(int n) {
        Soluciones.main(new String[]{String.valueOf(n)});
    }
}
