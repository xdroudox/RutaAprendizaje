/**
 * EJERCICIOS - Clean Code
 * Ejecuta desde raiz: python scripts/runner.py 8 5 [ejercicio] [-p N]
 */
public class Ejercicios {
    public static void main(String[] args) {
        if (args.length > 0 && args[0].matches("\\d+")) {
            int num = Integer.parseInt(args[0]);
            int pista = 0;
            for (int i = 1; i < args.length; i++) {
                if (args[i].equals("-p") && i + 1 < args.length) {
                    pista = Integer.parseInt(args[i + 1]);
                    break;
                }
            }
            switch (num) {
                case 1: ejercicio_1(pista); break;
                case 2: ejercicio_2(pista); break;
                case 3: ejercicio_3(pista); break;
            }
        } else {
            System.out.println("EJERCICIOS:");
            System.out.println("  🟢 Ej 1: Refactorizar funcion larga en funciones pequenas (SRP)");
            System.out.println("  🟡 Ej 2: Renombrar variables con nombres descriptivos");
            System.out.println("  🟡 Ej 3: Eliminar codigo duplicado (DRY) extrayendo metodo");
        }
    }

    static void ejercicio_1(int pista) {
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
        if (pista > 0) {
            System.out.println("\n========================================");
            System.out.println("PISTAS:");
        }
        if (pista >= 1) {
            System.out.println("\n🟢 PISTA 1 (Basica):");
            System.out.println("  - Crea una funcion para CADA operacion: suma, promedio, maximo, minimo");
            System.out.println("  - Cada funcion recibe int[] nums y retorna su resultado especifico");
            System.out.println("  - La funcion principal solo llama a las otras e imprime");
        }
        if (pista >= 2) {
            System.out.println("\n🟡 PISTA 2 (Intermedia):");
            System.out.println("  int calcularSuma(int[] nums) {\n" +
                "      int suma = 0;\n" +
                "      for (int n : nums) suma += n;\n" +
                "      return suma;\n" +
                "  }");
            System.out.println("  double calcularPromedio(int[] nums) {\n" +
                "      return (double) calcularSuma(nums) / nums.length;\n" +
                "  }");
            System.out.println("  int encontrarMaximo(int[] nums) {\n" +
                "      int max = nums[0];\n" +
                "      for (int n : nums) if (n > max) max = n;\n" +
                "      return max;\n" +
                "  }");
            System.out.println("  int encontrarMinimo(int[] nums) {\n" +
                "      int min = nums[0];\n" +
                "      for (int n : nums) if (n < min) min = n;\n" +
                "      return min;\n" +
                "  }");
        }
        if (pista >= 3) {
            System.out.println("\n🔴 PISTA 3 (Avanzada - casi la solucion):");
            System.out.println("  void mostrarEstadisticas(int[] nums) {\n" +
                "      System.out.println(\"Suma: \" + calcularSuma(nums));\n" +
                "      System.out.println(\"Promedio: \" + calcularPromedio(nums));\n" +
                "      System.out.println(\"Maximo: \" + encontrarMaximo(nums));\n" +
                "      System.out.println(\"Minimo: \" + encontrarMinimo(nums));\n" +
                "  }");
            System.out.println("  // Uso: mostrarEstadisticas(new int[]{15, 22, 8, 31, 17});");
        }
    }

    static void ejercicio_2(int pista) {
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
        if (pista > 0) {
            System.out.println("\n========================================");
            System.out.println("PISTAS:");
        }
        if (pista >= 1) {
            System.out.println("\n🟢 PISTA 1 (Basica):");
            System.out.println("  - El nombre del metodo debe explicar QUE hace");
            System.out.println("  - Cada variable debe tener un nombre que describa su proposito");
            System.out.println("  - cf(double pb, double iv, double d) -> calcularPrecioFinal(double precioBase, double tasaIVA, double descuento)");
        }
        if (pista >= 2) {
            System.out.println("\n🟡 PISTA 2 (Intermedia):");
            System.out.println("  double calcularPrecioFinal(double precioBase, double tasaIVA, double descuento) {\n" +
                "      double iva = precioBase * tasaIVA;\n" +
                "      double descuentoAplicado = precioBase * descuento;\n" +
                "      return precioBase + iva - descuentoAplicado;\n" +
                "  }");
        }
        if (pista >= 3) {
            System.out.println("\n🔴 PISTA 3 (Avanzada - casi la solucion):");
            System.out.println("  double precioFinal = calcularPrecioFinal(1000, 0.21, 0.10);");
            System.out.println("  System.out.println(\"Precio final: \" + precioFinal);  // 1110.0");
        }
    }

    static void ejercicio_3(int pista) {
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
        if (pista > 0) {
            System.out.println("\n========================================");
            System.out.println("PISTAS:");
        }
        if (pista >= 1) {
            System.out.println("\n🟢 PISTA 1 (Basica):");
            System.out.println("  - Los 3 metodos hacen exactamente lo mismo: formatear nombre + apellido");
            System.out.println("  - Crea un metodo privado que contenga la logica comun");
            System.out.println("  - Los 3 metodos originales llaman al nuevo metodo");
        }
        if (pista >= 2) {
            System.out.println("\n🟡 PISTA 2 (Intermedia):");
            System.out.println("  String formatearNombre(String nombre, String apellido) {\n" +
                "      return \"Nombre: \" + nombre + \" \" + apellido;\n" +
                "  }");
            System.out.println("  String emp(String n, String a) { return formatearNombre(n, a); }");
            System.out.println("  String cli(String n, String a) { return formatearNombre(n, a); }");
            System.out.println("  String prov(String n, String a) { return formatearNombre(n, a); }");
        }
        if (pista >= 3) {
            System.out.println("\n🔴 PISTA 3 (Avanzada - casi la solucion):");
            System.out.println("  System.out.println(emp(\"Juan\", \"Perez\"));   // \"Nombre: Juan Perez\"");
            System.out.println("  System.out.println(cli(\"Ana\", \"Lopez\"));   // \"Nombre: Ana Lopez\"");
            System.out.println("  System.out.println(prov(\"Luis\", \"Garcia\")); // \"Nombre: Luis Garcia\"");
            System.out.println("  // Si cambia el formato, solo hay que editar 1 metodo");
        }
    }
}
