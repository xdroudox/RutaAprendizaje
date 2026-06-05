/**
 * SOLUCIONES - Encapsulacion
 * Ejecuta: python scripts/runner.py 2 2 [ejercicio] -s
 */
public class Soluciones {

    public static void main(String[] args) {
        if (args.length > 0) {
            int num = Integer.parseInt(args[0]);
            switch (num) {
                case 1: solucion_1(); break;
                case 2: solucion_2(); break;
                case 3: solucion_3(); break;
                default: System.out.println("Solucion no encontrada");
            }
        } else {
            System.out.println("Soluciones disponibles: 1, 2, 3");
        }
    }

    static void solucion_1() {
        System.out.println("=== SOLUCION 1: CuentaBancaria ===");
        System.out.println("class CuentaBancaria {");
        System.out.println("    private double saldo;");
        System.out.println();
        System.out.println("    public double getSaldo() {");
        System.out.println("        return saldo;");
        System.out.println("    }");
        System.out.println();
        System.out.println("    public void setSaldo(double saldo) {");
        System.out.println("        if (saldo >= 0) {");
        System.out.println("            this.saldo = saldo;");
        System.out.println("        } else {");
        System.out.println("            System.out.println(\"Error: saldo no puede ser negativo\");");
        System.out.println("        }");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("// En el main:");
        System.out.println("CuentaBancaria c = new CuentaBancaria();");
        System.out.println("c.setSaldo(1000);");
        System.out.println("System.out.println(c.getSaldo());");
        System.out.println("c.setSaldo(-50); // Error");
        System.out.println();
        System.out.println("Explicacion: private oculta el atributo. El setter valida antes de asignar.");
    }

    static void solucion_2() {
        System.out.println("=== SOLUCION 2: Producto ===");
        System.out.println("class Producto {");
        System.out.println("    private String nombre;");
        System.out.println("    private double precio;");
        System.out.println();
        System.out.println("    public Producto(String nombre, double precio) {");
        System.out.println("        this.nombre = nombre;");
        System.out.println("        setPrecio(precio);");
        System.out.println("    }");
        System.out.println();
        System.out.println("    public double getPrecio() {");
        System.out.println("        return precio;");
        System.out.println("    }");
        System.out.println();
        System.out.println("    public void setPrecio(double precio) {");
        System.out.println("        if (precio >= 0) {");
        System.out.println("            this.precio = precio;");
        System.out.println("        } else {");
        System.out.println("            System.out.println(\"Error: precio no puede ser negativo\");");
        System.out.println("        }");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: El constructor usa el setter para reutilizar la validacion.");
    }

    static void solucion_3() {
        System.out.println("=== SOLUCION 3: Estudiante ===");
        System.out.println("class Estudiante {");
        System.out.println("    private double[] notas;");
        System.out.println();
        System.out.println("    public Estudiante(double[] notas) {");
        System.out.println("        this.notas = notas;");
        System.out.println("    }");
        System.out.println();
        System.out.println("    public double[] getNotas() {");
        System.out.println("        return notas;");
        System.out.println("    }");
        System.out.println();
        System.out.println("    public void setNotas(double[] notas) {");
        System.out.println("        this.notas = notas;");
        System.out.println("    }");
        System.out.println();
        System.out.println("    public double promedio() {");
        System.out.println("        double suma = 0;");
        System.out.println("        for (double n : notas) {");
        System.out.println("            suma += n;");
        System.out.println("        }");
        System.out.println("        return suma / notas.length;");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("// En el main:");
        System.out.println("double[] notas = {7.5, 8.0, 6.5};");
        System.out.println("Estudiante e = new Estudiante(notas);");
        System.out.println("System.out.println(\"Promedio: \" + e.promedio());");
        System.out.println();
        System.out.println("Explicacion: promedio() itera el array privado y calcula la media.");
    }
}
