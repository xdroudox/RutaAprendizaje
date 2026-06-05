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
        System.out.println("=== SOLUCION 1: Clase Persona ===");
        System.out.println("public class Persona {");
        System.out.println("    String nombre;");
        System.out.println("    int edad;");
        System.out.println("    String dni;");
        System.out.println();
        System.out.println("    public Persona(String nombre, int edad, String dni) {");
        System.out.println("        this.nombre = nombre;");
        System.out.println("        this.edad = edad;");
        System.out.println("        this.dni = dni;");
        System.out.println("    }");
        System.out.println();
        System.out.println("    void mostrarDatos() {");
        System.out.println("        System.out.println(\"Nombre: \" + nombre);");
        System.out.println("        System.out.println(\"Edad: \" + edad);");
        System.out.println("        System.out.println(\"DNI: \" + dni);");
        System.out.println("    }");
        System.out.println();
        System.out.println("    public static void main(String[] args) {");
        System.out.println("        Persona p1 = new Persona(\"Ana\", 25, \"12345678A\");");
        System.out.println("        Persona p2 = new Persona(\"Luis\", 30, \"87654321B\");");
        System.out.println("        p1.mostrarDatos();");
        System.out.println("        p2.mostrarDatos();");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: La clase Persona define el molde. Cada objeto es una instancia.");
        System.out.println("El constructor inicializa los atributos. this distingue parametro de atributo.");
    }

    static void solucion_2() {
        System.out.println("=== SOLUCION 2: Clase Rectangulo ===");
        System.out.println("public class Rectangulo {");
        System.out.println("    double base;");
        System.out.println("    double altura;");
        System.out.println();
        System.out.println("    public Rectangulo(double base, double altura) {");
        System.out.println("        this.base = base;");
        System.out.println("        this.altura = altura;");
        System.out.println("    }");
        System.out.println();
        System.out.println("    double calcularArea() {");
        System.out.println("        return base * altura;");
        System.out.println("    }");
        System.out.println();
        System.out.println("    double calcularPerimetro() {");
        System.out.println("        return 2 * (base + altura);");
        System.out.println("    }");
        System.out.println();
        System.out.println("    boolean esCuadrado() {");
        System.out.println("        return base == altura;");
        System.out.println("    }");
        System.out.println();
        System.out.println("    public static void main(String[] args) {");
        System.out.println("        Rectangulo r = new Rectangulo(5, 5);");
        System.out.println("        System.out.println(\"Area: \" + r.calcularArea());");
        System.out.println("        System.out.println(\"Perimetro: \" + r.calcularPerimetro());");
        System.out.println("        System.out.println(\"Es cuadrado: \" + r.esCuadrado());");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: Metodos calcularArea y calcularPerimetro usan formulas matematicas.");
        System.out.println("esCuadrado compara base con altura usando ==.");
    }

    static void solucion_3() {
        System.out.println("=== SOLUCION 3: Clase CuentaBancaria ===");
        System.out.println("public class CuentaBancaria {");
        System.out.println("    String titular;");
        System.out.println("    double saldo;");
        System.out.println("    String numeroCuenta;");
        System.out.println();
        System.out.println("    public CuentaBancaria(String titular) {");
        System.out.println("        this.titular = titular;");
        System.out.println("        this.saldo = 0.0;");
        System.out.println("        this.numeroCuenta = \"ES\" + (int)(Math.random() * 1000000000);");
        System.out.println("    }");
        System.out.println();
        System.out.println("    void depositar(double cantidad) {");
        System.out.println("        saldo += cantidad;");
        System.out.println("        System.out.println(\"Depositado: \" + cantidad);");
        System.out.println("    }");
        System.out.println();
        System.out.println("    void retirar(double cantidad) {");
        System.out.println("        if (cantidad <= saldo) {");
        System.out.println("            saldo -= cantidad;");
        System.out.println("            System.out.println(\"Retirado: \" + cantidad);");
        System.out.println("        } else {");
        System.out.println("            System.out.println(\"Saldo insuficiente\");");
        System.out.println("        }");
        System.out.println("    }");
        System.out.println();
        System.out.println("    void mostrarInfo() {");
        System.out.println("        System.out.println(\"Titular: \" + titular);");
        System.out.println("        System.out.println(\"Cuenta: \" + numeroCuenta);");
        System.out.println("        System.out.println(\"Saldo: \" + saldo);");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: El constructor genera un numero de cuenta aleatorio.");
        System.out.println("retirar verifica fondos antes de decrementar el saldo.");
    }
}
