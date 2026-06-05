public class Soluciones {
    public static void main(String[] args) {
        if (args.length > 0) {
            int n = Integer.parseInt(args[0]);
            switch (n) {
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
        System.out.println("=== SOLUCION 1: Sobrecarga de metodos ===");
        System.out.println("class Impresora {");
        System.out.println("    void imprimir(String texto) {");
        System.out.println("        System.out.println(texto);");
        System.out.println("    }");
        System.out.println();
        System.out.println("    void imprimir(int numero) {");
        System.out.println("        System.out.println(numero);");
        System.out.println("    }");
        System.out.println();
        System.out.println("    void imprimir(String texto, int veces) {");
        System.out.println("        for (int i = 0; i < veces; i++) {");
        System.out.println("            System.out.println(texto);");
        System.out.println("        }");
        System.out.println("    }");
        System.out.println();
        System.out.println("    void imprimir(int[] numeros) {");
        System.out.println("        for (int n : numeros) {");
        System.out.println("            System.out.println(n);");
        System.out.println("        }");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("public class Main {");
        System.out.println("    public static void main(String[] args) {");
        System.out.println("        Impresora i = new Impresora();");
        System.out.println("        i.imprimir(\"Hola\");");
        System.out.println("        i.imprimir(42);");
        System.out.println("        i.imprimir(\"Hola\", 3);");
        System.out.println("        i.imprimir(new int[]{1,2,3,4});");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: La sobrecarga permite multiples versiones del mismo metodo.");
        System.out.println("El compilador selecciona la version segun los argumentos proporcionados.");
    }

    static void solucion_2() {
        System.out.println("=== SOLUCION 2: Polimorfismo con animales ===");
        System.out.println("class Animal {");
        System.out.println("    void hacerSonido() {");
        System.out.println("        System.out.println(\"El animal hace un sonido\");");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("class Perro extends Animal {");
        System.out.println("    @Override");
        System.out.println("    void hacerSonido() { System.out.println(\"Guau\"); }");
        System.out.println("}");
        System.out.println("class Gato extends Animal {");
        System.out.println("    @Override");
        System.out.println("    void hacerSonido() { System.out.println(\"Miau\"); }");
        System.out.println("}");
        System.out.println("class Vaca extends Animal {");
        System.out.println("    @Override");
        System.out.println("    void hacerSonido() { System.out.println(\"Muu\"); }");
        System.out.println("}");
        System.out.println();
        System.out.println("public class Main {");
        System.out.println("    public static void main(String[] args) {");
        System.out.println("        Animal[] animales = {new Perro(), new Gato(), new Vaca()};");
        System.out.println("        for (Animal a : animales) {");
        System.out.println("            a.hacerSonido();");
        System.out.println("        }");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: Dynamic dispatch ejecuta el metodo de la clase real,");
        System.out.println("no del tipo de la referencia. Polimorfismo en accion.");
    }

    static void solucion_3() {
        System.out.println("=== SOLUCION 3: Sistema de pagos ===");
        System.out.println("interface Pagable {");
        System.out.println("    double calcularPago();");
        System.out.println("}");
        System.out.println();
        System.out.println("class Factura implements Pagable {");
        System.out.println("    private double montoFijo;");
        System.out.println("    public Factura(double montoFijo) { this.montoFijo = montoFijo; }");
        System.out.println("    @Override");
        System.out.println("    public double calcularPago() { return montoFijo; }");
        System.out.println("}");
        System.out.println();
        System.out.println("class Empleado implements Pagable {");
        System.out.println("    private double salarioPorHora;");
        System.out.println("    private int horas;");
        System.out.println("    public Empleado(double salarioPorHora, int horas) {");
        System.out.println("        this.salarioPorHora = salarioPorHora;");
        System.out.println("        this.horas = horas;");
        System.out.println("    }");
        System.out.println("    @Override");
        System.out.println("    public double calcularPago() { return salarioPorHora * horas; }");
        System.out.println("}");
        System.out.println();
        System.out.println("public class Main {");
        System.out.println("    public static void main(String[] args) {");
        System.out.println("        Pagable[] pagos = {new Factura(250.0), new Empleado(15.5, 40)};");
        System.out.println("        double total = 0;");
        System.out.println("        for (Pagable p : pagos) {");
        System.out.println("            total += p.calcularPago();");
        System.out.println("        }");
        System.out.println("        System.out.println(\"Total a pagar: \" + total);");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: La interfaz Pagable define un contrato comun.");
        System.out.println("Cada clase implementa calcularPago() a su manera. Polimorfismo via interfaz.");
    }
}
