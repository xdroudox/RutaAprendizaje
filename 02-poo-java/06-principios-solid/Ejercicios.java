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
            System.out.println("=== MENU - Principios SOLID ===");
            System.out.println("1. SRP - Refactorizar Pedido");
            System.out.println("2. OCP - Sistema de descuentos");
            System.out.println("3. DIP - Sistema de notificaciones");
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
        System.out.println(">> EJERCICIO 1: SRP - Refactorizar Pedido");
        System.out.println("La clase Pedido viola SRP porque hace demasiadas cosas.");
        System.out.println("Refactoriza en al menos 3 clases:");
        System.out.println("  - Pedido: solo datos y calculo de total");
        System.out.println("  - PedidoDAO: persistencia en BD");
        System.out.println("  - FacturaService: imprimir factura y enviar email");
        System.out.println();
        System.out.println("PISTA: Separa cada responsabilidad en una clase distinta.");
        System.out.println("// --- TU CODIGO AQUI ---");
    }

    static void ejercicio_2() {
        System.out.println(">> EJERCICIO 2: OCP - Sistema de descuentos");
        System.out.println("Crea un sistema de descuentos que cumpla OCP.");
        System.out.println("Define una interfaz Descuento con metodo aplicar(double monto).");
        System.out.println("Implementa: DescuentoNormal (0%), DescuentoPremium (10%), DescuentoVIP (25%).");
        System.out.println("Crea una clase CalculadoraDescuento que acepte cualquier Descuento.");
        System.out.println();
        System.out.println("PISTA: 'interface Descuento { double aplicar(double monto); }'");
        System.out.println("// --- TU CODIGO AQUI ---");
    }

    static void ejercicio_3() {
        System.out.println(">> EJERCICIO 3: DIP - Sistema de notificaciones");
        System.out.println("Crea un sistema que cumpla DIP:");
        System.out.println("  - Interfaz Notificador con metodo void enviar(String mensaje)");
        System.out.println("  - EmailNotificador implementa Notificador");
        System.out.println("  - SMSNotificador implementa Notificador");
        System.out.println("  - ServicioNotificacion recibe un Notificador por constructor (inyeccion)");
        System.out.println("En el main, prueba con ambos tipos.");
        System.out.println();
        System.out.println("PISTA: La clase de alto nivel depende de la abstraccion, no de la implementacion.");
        System.out.println("// --- TU CODIGO AQUI ---");
    }

    static void mostrarPista(int n) {
        String[][] pistas = {
            {
                "Pista 1: Pedido: atributos, calcularTotal().",
                "Pista 2: PedidoDAO: guardar(Pedido p), obtener(int id).",
                "Pista 3: FacturaService: imprimir(Pedido p), enviarEmail(Pedido p)."
            },
            {
                "Pista 1: 'interface Descuento { double aplicar(double monto); }'",
                "Pista 2: 'class DescuentoVIP implements Descuento'",
                "Pista 3: 'class CalculadoraDescuento { double calcular(Descuento d, double monto) { return d.aplicar(monto); } }'"
            },
            {
                "Pista 1: 'interface Notificador { void enviar(String msg); }'",
                "Pista 2: 'class EmailNotificador implements Notificador'",
                "Pista 3: 'class ServicioNotificacion { private Notificador n; public ServicioNotificacion(Notificador n) { this.n = n; } }'"
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
