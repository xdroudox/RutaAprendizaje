/**
 * SOLUCIONES - Clean Code
 * Ejecuta desde raiz: python scripts/runner.py 8 5 [ejercicio]
 */
public class Soluciones {
    public static void main(String[] args) {
        if (args.length > 0) {
            int num = Integer.parseInt(args[0]);
            switch (num) {
                case 1: ejercicio_1(); break;
                case 2: ejercicio_2(); break;
                case 3: ejercicio_3(); break;
            }
        } else {
            for (int i = 1; i <= 3; i++) {
                System.out.println("  " + i + ". [Solucion " + i + "]");
            }
        }
    }

    static void ejercicio_1() {
        System.out.println(">> SOLUCION 1: SRP - Funciones pequenas");
        System.out.println("-".repeat(40));

        int[] datos = {15, 22, 8, 31, 17};

        int suma = 0;
        for (int n : datos) suma += n;
        double promedio = (double) suma / datos.length;
        int maximo = datos[0], minimo = datos[0];
        for (int n : datos) {
            if (n > maximo) maximo = n;
            if (n < minimo) minimo = n;
        }

        System.out.println("Suma: " + suma);
        System.out.println("Promedio: " + promedio);
        System.out.println("Maximo: " + maximo);
        System.out.println("Minimo: " + minimo);
        System.out.println();
        System.out.println("Codigo refactorizado:");
        System.out.println("  int calcularSuma(int[] nums) { ... }");
        System.out.println("  double calcularPromedio(int[] nums) { ... }");
        System.out.println("  int encontrarMaximo(int[] nums) { ... }");
        System.out.println("  int encontrarMinimo(int[] nums) { ... }");
        System.out.println("  void mostrarEstadisticas(int[] nums) { ... }");
    }

    static void ejercicio_2() {
        System.out.println(">> SOLUCION 2: Nombres descriptivos");
        System.out.println("-".repeat(40));
        System.out.println("Codigo original:");
        System.out.println("  double cf(double pb, double iv, double d) { ... }");
        System.out.println();
        System.out.println("Codigo refactorizado:");
        System.out.println("  double calcularPrecioFinal(double precioBase,");
        System.out.println("        double tasaIVA, double descuento) {");
        System.out.println("      double iva = precioBase * tasaIVA;");
        System.out.println("      double desc = precioBase * descuento;");
        System.out.println("      return precioBase + iva - desc;");
        System.out.println("  }");
        System.out.println();
        double precioFinal = 1000 + (1000 * 0.21) - (1000 * 0.10);
        System.out.println("Ejemplo: precioBase=1000, IVA=21%, desc=10%");
        System.out.println("Precio final: " + precioFinal);
    }

    static void ejercicio_3() {
        System.out.println(">> SOLUCION 3: DRY - Eliminar duplicacion");
        System.out.println("-".repeat(40));
        System.out.println("Codigo original (3 metodos identicos):");
        System.out.println("  String emp(String n, String a) { ... }");
        System.out.println("  String cli(String n, String a) { ... }");
        System.out.println("  String prov(String n, String a) { ... }");
        System.out.println();
        System.out.println("Codigo refactorizado (DRY):");
        System.out.println("  String formatearNombre(String nombre, String apellido) {");
        System.out.println("      return \"Nombre: \" + nombre + \" \" + apellido;");
        System.out.println("  }");
        System.out.println();
        System.out.println("  String emp(String n, String a) { return formatearNombre(n, a); }");
        System.out.println("  String cli(String n, String a) { return formatearNombre(n, a); }");
        System.out.println("  String prov(String n, String a) { return formatearNombre(n, a); }");
        System.out.println();
        String res = "Nombre: Juan Perez";
        System.out.println("Ejemplo: " + res);
    }
}
