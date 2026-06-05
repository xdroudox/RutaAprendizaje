/**
 * SOLUCIONES - Herencia
 * Ejecuta: python scripts/runner.py 2 3 [ejercicio] -s
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
        System.out.println("=== SOLUCION 1: Animal, Perro y Gato ===");
        System.out.println("class Animal {");
        System.out.println("    void hacerSonido() {");
        System.out.println("        System.out.println(\"...\");");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("class Perro extends Animal {");
        System.out.println("    @Override");
        System.out.println("    void hacerSonido() {");
        System.out.println("        System.out.println(\"Guau!\");");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("class Gato extends Animal {");
        System.out.println("    @Override");
        System.out.println("    void hacerSonido() {");
        System.out.println("        System.out.println(\"Miau!\");");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("// En el main:");
        System.out.println("Perro p = new Perro();");
        System.out.println("Gato g = new Gato();");
        System.out.println("p.hacerSonido();");
        System.out.println("g.hacerSonido();");
        System.out.println();
        System.out.println("Explicacion: extends crea la herencia. @Override sobrescribe el metodo.");
    }

    static void solucion_2() {
        System.out.println("=== SOLUCION 2: Vehiculo, Coche y Bicicleta ===");
        System.out.println("class Vehiculo {");
        System.out.println("    int velocidad;");
        System.out.println();
        System.out.println("    Vehiculo(int velocidad) {");
        System.out.println("        this.velocidad = velocidad;");
        System.out.println("    }");
        System.out.println();
        System.out.println("    void mover() {");
        System.out.println("        System.out.println(\"El vehiculo se mueve...\");");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("class Coche extends Vehiculo {");
        System.out.println("    Coche(int velocidad) {");
        System.out.println("        super(velocidad);");
        System.out.println("    }");
        System.out.println();
        System.out.println("    @Override");
        System.out.println("    void mover() {");
        System.out.println("        System.out.println(\"El coche acelera a \" + velocidad + \" km/h\");");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("class Bicicleta extends Vehiculo {");
        System.out.println("    Bicicleta(int velocidad) {");
        System.out.println("        super(velocidad);");
        System.out.println("    }");
        System.out.println();
        System.out.println("    @Override");
        System.out.println("    void mover() {");
        System.out.println("        System.out.println(\"La bicicleta pedalea a \" + velocidad + \" km/h\");");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("// En el main:");
        System.out.println("Coche c = new Coche(120);");
        System.out.println("Bicicleta b = new Bicicleta(25);");
        System.out.println("c.mover();");
        System.out.println("b.mover();");
        System.out.println();
        System.out.println("Explicacion: super() llama al constructor de la clase padre.");
    }

    static void solucion_3() {
        System.out.println("=== SOLUCION 3: Empleado, Gerente y Vendedor ===");
        System.out.println("class Empleado {");
        System.out.println("    String nombre;");
        System.out.println();
        System.out.println("    Empleado(String nombre) {");
        System.out.println("        this.nombre = nombre;");
        System.out.println("    }");
        System.out.println();
        System.out.println("    double calcularSalario() {");
        System.out.println("        return 0.0;");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("class Gerente extends Empleado {");
        System.out.println("    double bono;");
        System.out.println();
        System.out.println("    Gerente(String nombre, double bono) {");
        System.out.println("        super(nombre);");
        System.out.println("        this.bono = bono;");
        System.out.println("    }");
        System.out.println();
        System.out.println("    @Override");
        System.out.println("    double calcularSalario() {");
        System.out.println("        return 50000 + bono;");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("class Vendedor extends Empleado {");
        System.out.println("    double comision;");
        System.out.println();
        System.out.println("    Vendedor(String nombre, double comision) {");
        System.out.println("        super(nombre);");
        System.out.println("        this.comision = comision;");
        System.out.println("    }");
        System.out.println();
        System.out.println("    @Override");
        System.out.println("    double calcularSalario() {");
        System.out.println("        return 30000 + comision;");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("// En el main:");
        System.out.println("Gerente g = new Gerente(\"Ana\", 10000);");
        System.out.println("Vendedor v = new Vendedor(\"Luis\", 5000);");
        System.out.println("System.out.println(g.nombre + \": \" + g.calcularSalario());");
        System.out.println("System.out.println(v.nombre + \": \" + v.calcularSalario());");
        System.out.println();
        System.out.println("Explicacion: Cada subclase sobrescribe calcularSalario() con su propia logica.");
    }
}
