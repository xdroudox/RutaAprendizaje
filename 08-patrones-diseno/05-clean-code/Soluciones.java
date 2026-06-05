import java.util.Arrays;

public class Soluciones {
    public static void main(String[] args) {
        if (args.length == 0) {
            for (int i = 1; i <= 3; i++) {
                System.out.println("--- Solucion " + i + " ---");
                ejecutarSolucion(i);
                System.out.println();
            }
        } else {
            int num = Integer.parseInt(args[0]);
            ejecutarSolucion(num);
        }
    }

    static void ejecutarSolucion(int n) {
        switch (n) {
            case 1: solucion_1(); break;
            case 2: solucion_2(); break;
            case 3: solucion_3(); break;
            default: System.out.println("Solucion no valida");
        }
    }

    // ============================================================
    // SOLUCION 1: Nombres y funciones pequenas
    // ============================================================
    static void solucion_1() {
        System.out.println("REFACTORIZACION: Nombres y funciones pequenas");
        System.out.println("===========================================");
        System.out.println("CODIGO ORIGINAL:");
        System.out.println("""
    public static void m(int[] a) {
        int t = 0;
        for (int i = 0; i < a.length; i++) { t = t + a[i]; }
        int p = t / a.length;
        System.out.println("Total: " + t);
        System.out.println("Promedio: " + p);
        int mx = a[0];
        int mn = a[0];
        for (int i = 0; i < a.length; i++) {
            if (a[i] > mx) mx = a[i];
            if (a[i] < mn) mn = a[i];
        }
        System.out.println("Max: " + mx);
        System.out.println("Min: " + mn);
    }
        """);
        System.out.println("CODIGO REFACTORIZADO:");
        System.out.println("""
    public static void mostrarEstadisticas(int[] numeros) {
        int total = calcularTotal(numeros);
        double promedio = calcularPromedio(numeros);
        int maximo = encontrarMaximo(numeros);
        int minimo = encontrarMinimo(numeros);
        imprimirEstadisticas(total, promedio, maximo, minimo);
    }
    
    private static int calcularTotal(int[] numeros) {
        int total = 0;
        for (int numero : numeros) {
            total += numero;
        }
        return total;
    }
    
    private static double calcularPromedio(int[] numeros) {
        return (double) calcularTotal(numeros) / numeros.length;
    }
    
    private static int encontrarMaximo(int[] numeros) {
        int maximo = numeros[0];
        for (int numero : numeros) {
            if (numero > maximo) maximo = numero;
        }
        return maximo;
    }
    
    private static int encontrarMinimo(int[] numeros) {
        int minimo = numeros[0];
        for (int numero : numeros) {
            if (numero < minimo) minimo = numero;
        }
        return minimo;
    }
    
    private static void imprimirEstadisticas(int total, double promedio,
                                              int maximo, int minimo) {
        System.out.println("Total: " + total);
        System.out.println("Promedio: " + promedio);
        System.out.println("Maximo: " + maximo);
        System.out.println("Minimo: " + minimo);
    }
        """);
        System.out.println("DEMOSTRACION:");
        int[] datos = {15, 22, 8, 31, 17, 5, 29};
        System.out.println("Array: " + Arrays.toString(datos));
        mostrarEstadisticas(datos);
    }

    public static void mostrarEstadisticas(int[] numeros) {
        int total = calcularTotal(numeros);
        double promedio = calcularPromedio(numeros);
        int maximo = encontrarMaximo(numeros);
        int minimo = encontrarMinimo(numeros);
        imprimirEstadisticas(total, promedio, maximo, minimo);
    }

    private static int calcularTotal(int[] numeros) {
        int total = 0;
        for (int numero : numeros) {
            total += numero;
        }
        return total;
    }

    private static double calcularPromedio(int[] numeros) {
        return (double) calcularTotal(numeros) / numeros.length;
    }

    private static int encontrarMaximo(int[] numeros) {
        int maximo = numeros[0];
        for (int numero : numeros) {
            if (numero > maximo) maximo = numero;
        }
        return maximo;
    }

    private static int encontrarMinimo(int[] numeros) {
        int minimo = numeros[0];
        for (int numero : numeros) {
            if (numero < minimo) minimo = numero;
        }
        return minimo;
    }

    private static void imprimirEstadisticas(int total, double promedio, int maximo, int minimo) {
        System.out.println("Total: " + total);
        System.out.println("Promedio: " + promedio);
        System.out.println("Maximo: " + maximo);
        System.out.println("Minimo: " + minimo);
    }

    // ============================================================
    // SOLUCION 2: Principio DRY
    // ============================================================
    static void solucion_2() {
        System.out.println("REFACTORIZACION: Principio DRY");
        System.out.println("==============================");
        System.out.println("CODIGO ORIGINAL (3 metodos con codigo repetido):");
        System.out.println("""
    String procesarEmpleado(String n, String a, String c, double s) {
        double sn = s * 0.85;
        double sa = s * 1.10;
        return "Nombre: " + n + " " + a;
    }
    String procesarCliente(String n, String a, String c) {
        double sn = 100 * 0.85;
        double sa = 100 * 1.10;
        return "Nombre: " + n + " " + a;
    }
    String procesarProveedor(String n, String a) {
        double sn = 1000 * 0.85;
        double sa = 1000 * 1.10;
        return "Nombre: " + n + " " + a;
    }
        """);
        System.out.println("CODIGO REFACTORIZADO (DRY aplicado):");
        System.out.println("""
    public static String formatearNombre(String nombre, String apellido) {
        return "Nombre: " + nombre + " " + apellido;
    }
    
    public static double calcularSueldoNeto(double sueldoBase) {
        return sueldoBase * 0.85;
    }
    
    public static double calcularSueldoAnual(double sueldoBase) {
        return sueldoBase * 1.10;
    }
    
    public static String procesarEmpleado(String nombre, String apellido,
                                           String cargo, double sueldo) {
        double neto = calcularSueldoNeto(sueldo);
        double anual = calcularSueldoAnual(sueldo);
        return formatearNombre(nombre, apellido) +
               " | Neto: " + neto + " | Anual: " + anual;
    }
    
    public static String procesarCliente(String nombre, String apellido,
                                          String categoria) {
        double neto = calcularSueldoNeto(100);
        double anual = calcularSueldoAnual(100);
        return formatearNombre(nombre, apellido) +
               " | Neto: " + neto + " | Anual: " + anual;
    }
    
    public static String procesarProveedor(String nombre, String apellido) {
        double neto = calcularSueldoNeto(1000);
        double anual = calcularSueldoAnual(1000);
        return formatearNombre(nombre, apellido) +
               " | Neto: " + neto + " | Anual: " + anual;
    }
        """);
        System.out.println("DEMOSTRACION:");
        System.out.println(procesarEmpleado("Juan", "Perez", "Ingeniero", 50000));
        System.out.println(procesarCliente("Maria", "Lopez", "Premium"));
        System.out.println(procesarProveedor("Carlos", "Gomez"));
    }

    public static String formatearNombre(String nombre, String apellido) {
        return "Nombre: " + nombre + " " + apellido;
    }

    public static double calcularSueldoNeto(double sueldoBase) {
        return sueldoBase * 0.85;
    }

    public static double calcularSueldoAnual(double sueldoBase) {
        return sueldoBase * 1.10;
    }

    public static String procesarEmpleado(String nombre, String apellido, String cargo, double sueldo) {
        double neto = calcularSueldoNeto(sueldo);
        double anual = calcularSueldoAnual(sueldo);
        return formatearNombre(nombre, apellido) + " | Neto: " + neto + " | Anual: " + anual;
    }

    public static String procesarCliente(String nombre, String apellido, String categoria) {
        double neto = calcularSueldoNeto(100);
        double anual = calcularSueldoAnual(100);
        return formatearNombre(nombre, apellido) + " | Neto: " + neto + " | Anual: " + anual;
    }

    public static String procesarProveedor(String nombre, String apellido) {
        double neto = calcularSueldoNeto(1000);
        double anual = calcularSueldoAnual(1000);
        return formatearNombre(nombre, apellido) + " | Neto: " + neto + " | Anual: " + anual;
    }

    // ============================================================
    // SOLUCION 3: Comentarios y claridad
    // ============================================================
    static void solucion_3() {
        System.out.println("REFACTORIZACION: Comentarios y claridad");
        System.out.println("=======================================");
        System.out.println("CODIGO ORIGINAL (lleno de comentarios superfluos):");
        System.out.println("""
    // calcula el precio final del producto
    double cf(double pb, double iv, double d) {
        // calcula el IVA
        double ci = pb * iv;
        // calcula el descuento
        double cd = pb * d;
        // precio final = precio base + iva - descuento
        double pf = pb + ci - cd;
        return pf;
    }
        """);
        System.out.println("CODIGO REFACTORIZADO (autoexplicativo):");
        System.out.println("""
    public static double calcularPrecioFinal(
            double precioBase, double tasaIVA, double tasaDescuento) {
        double iva = calcularIVA(precioBase, tasaIVA);
        double descuento = calcularDescuento(precioBase, tasaDescuento);
        return precioBase + iva - descuento;
    }
    
    private static double calcularIVA(double precioBase, double tasaIVA) {
        return precioBase * tasaIVA;
    }
    
    private static double calcularDescuento(double precioBase, double tasaDescuento) {
        return precioBase * tasaDescuento;
    }
        """);
        System.out.println("DEMOSTRACION:");
        double precio = 1000.0;
        double iva = 0.21;
        double desc = 0.10;
        double resultado = calcularPrecioFinal(precio, iva, desc);
        System.out.println("Precio base: " + precio);
        System.out.println("IVA (21%): " + (precio * iva));
        System.out.println("Descuento (10%): " + (precio * desc));
        System.out.println("Precio final: " + resultado);
    }

    public static double calcularPrecioFinal(double precioBase, double tasaIVA, double tasaDescuento) {
        double iva = calcularIVA(precioBase, tasaIVA);
        double descuento = calcularDescuento(precioBase, tasaDescuento);
        return precioBase + iva - descuento;
    }

    private static double calcularIVA(double precioBase, double tasaIVA) {
        return precioBase * tasaIVA;
    }

    private static double calcularDescuento(double precioBase, double tasaDescuento) {
        return precioBase * tasaDescuento;
    }
}
