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
            System.out.println("=== CLEAN CODE - EJERCICIOS DE REFACTORIZACION ===");
            System.out.println("1. Nombres y funciones pequenas");
            System.out.println("2. Principio DRY");
            System.out.println("3. Comentarios y claridad");
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

    // Nombres y funciones pequenas
    static void ejercicio_1() {
        System.out.println("=== EJERCICIO 1: Nombres y funciones pequenas ===");
        System.out.println("Refactoriza el siguiente codigo para que tenga nombres");
        System.out.println("significativos y funciones pequenas:");
        System.out.println();
        System.out.println("  // Codigo original:");
        System.out.println("  public static void m(int[] a) {");
        System.out.println("    int t = 0;");
        System.out.println("    for (int i = 0; i < a.length; i++) {");
        System.out.println("      t = t + a[i];");
        System.out.println("    }");
        System.out.println("    int p = t / a.length;");
        System.out.println("    System.out.println(\"Total: \" + t);");
        System.out.println("    System.out.println(\"Promedio: \" + p);");
        System.out.println("    int mx = a[0];");
        System.out.println("    int mn = a[0];");
        System.out.println("    for (int i = 0; i < a.length; i++) {");
        System.out.println("      if (a[i] > mx) mx = a[i];");
        System.out.println("      if (a[i] < mn) mn = a[i];");
        System.out.println("    }");
        System.out.println("    System.out.println(\"Max: \" + mx);");
        System.out.println("    System.out.println(\"Min: \" + mn);");
        System.out.println("  }");
        System.out.println();
        System.out.println("Requisitos:");
        System.out.println("- Extraer metodos con nombres claros");
        System.out.println("- Renombrar variables con nombres significativos");
        System.out.println("- Cada metodo debe hacer una sola cosa");
        System.out.println();
        System.out.println("Pista: Usa 'javac Ejercicios.java && java Ejercicios 1 -p'");
    }

    // Principio DRY
    static void ejercicio_2() {
        System.out.println("=== EJERCICIO 2: Principio DRY ===");
        System.out.println("Refactoriza el siguiente codigo que viola DRY:");
        System.out.println();
        System.out.println("  String procesarEmpleado(String n, String a, String c, double s) {");
        System.out.println("    double sn = s * 0.85;");
        System.out.println("    double sa = s * 1.10;");
        System.out.println("    return \"Nombre: \" + n + \" \" + a;");
        System.out.println("  }");
        System.out.println();
        System.out.println("  String procesarCliente(String n, String a, String c) {");
        System.out.println("    double sn = 100 * 0.85;");
        System.out.println("    double sa = 100 * 1.10;");
        System.out.println("    return \"Nombre: \" + n + \" \" + a;");
        System.out.println("  }");
        System.out.println();
        System.out.println("  String procesarProveedor(String n, String a) {");
        System.out.println("    double sn = 1000 * 0.85;");
        System.out.println("    double sa = 1000 * 1.10;");
        System.out.println("    return \"Nombre: \" + n + \" \" + a;");
        System.out.println("  }");
        System.out.println();
        System.out.println("Requisitos:");
        System.out.println("- Eliminar codigo repetido");
        System.out.println("- Extraer metodos comunes");
        System.out.println("- Usar parametros para valores variables");
        System.out.println();
        System.out.println("Pista: Usa 'javac Ejercicios.java && java Ejercicios 2 -p'");
    }

    // Comentarios y claridad
    static void ejercicio_3() {
        System.out.println("=== EJERCICIO 3: Comentarios y claridad ===");
        System.out.println("Refactoriza el siguiente codigo reemplazando los");
        System.out.println("comentarios con codigo que se explique por si mismo:");
        System.out.println();
        System.out.println("  // calcula el precio final del producto");
        System.out.println("  double cf(double pb, double iv, double d) {");
        System.out.println("    // calcula el IVA");
        System.out.println("    double ci = pb * iv;");
        System.out.println("    // calcula el descuento");
        System.out.println("    double cd = pb * d;");
        System.out.println("    // precio final = precio base + iva - descuento");
        System.out.println("    double pf = pb + ci - cd;");
        System.out.println("    return pf;");
        System.out.println("  }");
        System.out.println();
        System.out.println("Requisitos:");
        System.out.println("- Renombrar metodo y parametros claramente");
        System.out.println("- Eliminar comentarios innecesarios");
        System.out.println("- El codigo debe ser autoexplicativo");
        System.out.println("- Extraer: calcularIVA, calcularDescuento si aplica");
        System.out.println();
        System.out.println("Pista: Usa 'javac Ejercicios.java && java Ejercicios 3 -p'");
    }

    static void mostrarPista(int n) {
        String[] pistas = {
            "",
            "PISTA 1: Renombra 'm' a 'mostrarEstadisticas'. " +
            "'a' -> 'numeros', 't' -> 'total', 'p' -> 'promedio', " +
            "'mx' -> 'maximo', 'mn' -> 'minimo'. " +
            "Extrae: calcularTotal(), calcularPromedio(), encontrarMaximo(), " +
            "encontrarMinimo(). Cada metodo hace una sola cosa.",
            "PISTA 2: Observa que las tres funciones formatean el nombre igual. " +
            "Extrae: formatearNombre(nombre, apellido). " +
            "Tambien calculan sn y sa igual pero con diferentes bases. " +
            "Extrae: calcularSueldoNeto(sueldoBase) y calcularSueldoAnual(sueldoBase). " +
            "Cada funcion especifica solo llama a los metodos comunes.",
            "PISTA 3: Renombra 'cf' a 'calcularPrecioFinal'. " +
            "'pb' -> 'precioBase', 'iv' -> 'tasaIVA', 'd' -> 'tasaDescuento'. " +
            "'ci' -> 'iva', 'cd' -> 'descuento', 'pf' -> 'precioFinal'. " +
            "Elimina los comentarios, el codigo con buenos nombres ya se explica solo. " +
            "Opcional: extrae calcularIVA() y calcularDescuento()."
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
