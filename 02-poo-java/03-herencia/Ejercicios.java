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
            System.out.println("=== MENU - Herencia ===");
            System.out.println("1. Jerarquia de vehiculos");
            System.out.println("2. Sistema de empleados");
            System.out.println("3. Figuras geometricas");
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
        System.out.println(">> EJERCICIO 1: Jerarquia de vehiculos");
        System.out.println("Crea clase base Vehiculo con: marca, modelo, velocidadMaxima.");
        System.out.println("Metodo acelerar() que imprima \"El vehiculo acelera\".");
        System.out.println("Subclase Coche: anade numPuertas, sobrescribe acelerar().");
        System.out.println("Subclase Moto: anade tipoManillar, sobrescribe acelerar().");
        System.out.println();
        System.out.println("PISTA: Usa extends Vehiculo y super(marca, modelo, velMax).");
        System.out.println("// --- TU CODIGO AQUI ---");
    }

    static void ejercicio_2() {
        System.out.println(">> EJERCICIO 2: Sistema de empleados");
        System.out.println("Clase base Empleado con: nombre, salario, calcularBono().");
        System.out.println("Subclase Gerente: bono = salario * 0.20");
        System.out.println("Subclase Desarrollador: bono = salario * 0.10");
        System.out.println("Usa super(nombre, salario) en los constructores.");
        System.out.println();
        System.out.println("PISTA: Usa @Override en calcularBono() de cada subclase.");
        System.out.println("// --- TU CODIGO AQUI ---");
    }

    static void ejercicio_3() {
        System.out.println(">> EJERCICIO 3: Figuras geometricas");
        System.out.println("Clase abstracta Figura con metodo abstracto calcularArea().");
        System.out.println("Circulo: atributo radio, area = PI * radio^2.");
        System.out.println("Rectangulo: atributos base y altura, area = base * altura.");
        System.out.println();
        System.out.println("PISTA: Usa Math.PI para Circulo.");
        System.out.println("// --- TU CODIGO AQUI ---");
    }

    static void mostrarPista(int n) {
        String[][] pistas = {
            {
                "Pista 1: 'class Vehiculo { protected String marca; ... }'",
                "Pista 2: 'class Coche extends Vehiculo { ... }'",
                "Pista 3: 'super(marca, modelo, velocidadMaxima)' en el constructor"
            },
            {
                "Pista 1: 'class Empleado { protected String nombre; protected double salario; }'",
                "Pista 2: 'class Gerente extends Empleado { ... }'",
                "Pista 3: '@Override public double calcularBono() { return salario * 0.20; }'"
            },
            {
                "Pista 1: 'abstract class Figura { public abstract double calcularArea(); }'",
                "Pista 2: 'class Circulo extends Figura { private double radio; }'",
                "Pista 3: 'return Math.PI * radio * radio;'"
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
