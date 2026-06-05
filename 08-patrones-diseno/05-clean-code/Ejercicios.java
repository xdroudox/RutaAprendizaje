/**
 * EJERCICIOS - Clean Code
 * Ejecuta desde raiz: python scripts/runner.py 8 5 [ejercicio]
 */
public class Ejercicios {
    public static void main(String[] args) {
        if (args.length > 0) {
            int num = Integer.parseInt(args[0]);
            switch (num) {
                case 1: ejercicio_1(); break;
                case 2: ejercicio_2(); break;
                case 3: ejercicio_3(); break;
            }
        } else {
            System.out.println("EJERCICIOS:");
            System.out.println("1. Refactorizar funcion larga en funciones pequenas (SRP)");
            System.out.println("2. Renombrar variables con nombres descriptivos");
            System.out.println("3. Eliminar codigo duplicado (DRY) extrayendo metodo");
        }
    }

    static void ejercicio_1() {
        System.out.println(">> EJERCICIO 1: SRP - Funciones pequenas");
        System.out.println("-".repeat(40));
        System.out.println("Refactoriza esta funcion siguiendo SRP:");
        System.out.println();
        System.out.println("void procesar(int[] nums) {");
        System.out.println("    int s = 0;");
        System.out.println("    for (int n : nums) s += n;");
        System.out.println("    double p = (double) s / nums.length;");
        System.out.println("    int mx = nums[0], mn = nums[0];");
        System.out.println("    for (int n : nums) {");
        System.out.println("        if (n > mx) mx = n;");
        System.out.println("        if (n < mn) mn = n;");
        System.out.println("    }");
        System.out.println("    System.out.println(\"Suma: \" + s);");
        System.out.println("    System.out.println(\"Prom: \" + p);");
        System.out.println("    System.out.println(\"Max: \" + mx);");
        System.out.println("    System.out.println(\"Min: \" + mn);");
        System.out.println("}");
        System.out.println();
        System.out.println("Extrae: calcularSuma(), calcularPromedio(),");
        System.out.println("encontrarMaximo(), encontrarMinimo()");
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    static void ejercicio_2() {
        System.out.println(">> EJERCICIO 2: Nombres descriptivos");
        System.out.println("-".repeat(40));
        System.out.println("Refactoriza renombrando variables y metodos:");
        System.out.println();
        System.out.println("double cf(double pb, double iv, double d) {");
        System.out.println("    double ci = pb * iv;");
        System.out.println("    double cd = pb * d;");
        System.out.println("    double pf = pb + ci - cd;");
        System.out.println("    return pf;");
        System.out.println("}");
        System.out.println();
        System.out.println("Sugerencia: cf -> calcularPrecioFinal");
        System.out.println("pb -> precioBase, iv -> tasaIVA, d -> descuento");
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    static void ejercicio_3() {
        System.out.println(">> EJERCICIO 3: DRY - Eliminar duplicacion");
        System.out.println("-".repeat(40));
        System.out.println("Refactoriza extrayendo metodo comun:");
        System.out.println();
        System.out.println("String emp(String n, String a) {");
        System.out.println("    return \"Nombre: \" + n + \" \" + a;");
        System.out.println("}");
        System.out.println("String cli(String n, String a) {");
        System.out.println("    return \"Nombre: \" + n + \" \" + a;");
        System.out.println("}");
        System.out.println("String prov(String n, String a) {");
        System.out.println("    return \"Nombre: \" + n + \" \" + a;");
        System.out.println("}");
        System.out.println();
        System.out.println("Extrae: String formatearNombre(String nombre, String apellido)");
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }
}
