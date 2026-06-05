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
            System.out.println("=== MENU - Encapsulacion ===");
            System.out.println("1. Clase Empleado encapsulada");
            System.out.println("2. Clase Libro con validacion");
            System.out.println("3. CuentaAhorros JavaBeans");
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
        System.out.println(">> EJERCICIO 1: Clase Empleado encapsulada");
        System.out.println("Crea clase Empleado con atributos privados: nombre, salario, departamento.");
        System.out.println("Getters y setters con validacion:");
        System.out.println("  - salario no puede ser negativo");
        System.out.println("  - departamento no puede estar vacio");
        System.out.println("En el main, crea un empleado, asigna valores y muestra datos.");
        System.out.println();
        System.out.println("PISTA: Usa private para los atributos.");
        System.out.println("// --- TU CODIGO AQUI ---");
    }

    static void ejercicio_2() {
        System.out.println(">> EJERCICIO 2: Clase Libro con validacion");
        System.out.println("Crea clase Libro con atributos privados: titulo, autor, isbn, anioPublicacion.");
        System.out.println("Validaciones en setters:");
        System.out.println("  - titulo no vacio");
        System.out.println("  - isbn debe tener 13 caracteres");
        System.out.println("  - anioPublicacion <= anio actual");
        System.out.println();
        System.out.println("PISTA: Usa length() para validar el isbn.");
        System.out.println("// --- TU CODIGO AQUI ---");
    }

    static void ejercicio_3() {
        System.out.println(">> EJERCICIO 3: CuentaAhorros JavaBeans");
        System.out.println("Crea clase CuentaAhorros siguiendo el patron JavaBeans:");
        System.out.println("  - Constructor sin argumentos");
        System.out.println("  - Atributos privados: numeroCuenta, titular, saldo, tasaInteres");
        System.out.println("  - Getters y setters para todos");
        System.out.println("  - Metodo aplicarInteres() que incremente saldo segun tasa");
        System.out.println();
        System.out.println("PISTA: saldo += saldo * tasaInteres / 100");
        System.out.println("// --- TU CODIGO AQUI ---");
    }

    static void mostrarPista(int n) {
        String[][] pistas = {
            {
                "Pista 1: Declara 'private String nombre;' etc.",
                "Pista 2: Getter: 'public String getNombre() { return nombre; }'",
                "Pista 3: Setter: 'public void setNombre(String nombre) { this.nombre = nombre; }'"
            },
            {
                "Pista 1: En setTitulo verifica if(titulo != null && !titulo.isEmpty())",
                "Pista 2: En setIsbn verifica if(isbn.length() == 13)",
                "Pista 3: Usa java.time.Year.now().getValue() para el anio actual"
            },
            {
                "Pista 1: Constructor vacio: 'public CuentaAhorros() {}'",
                "Pista 2: aplicarInteres: 'saldo += saldo * tasaInteres / 100;'",
                "Pista 3: Sigue el patron: atributos privados, getters/setters publicos"
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
