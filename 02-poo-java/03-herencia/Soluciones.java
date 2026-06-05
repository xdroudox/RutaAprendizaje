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
        System.out.println("=== SOLUCION 1: Jerarquia de vehiculos ===");
        System.out.println("class Vehiculo {");
        System.out.println("    protected String marca;");
        System.out.println("    protected String modelo;");
        System.out.println("    protected int velocidadMaxima;");
        System.out.println();
        System.out.println("    public Vehiculo(String marca, String modelo, int velocidadMaxima) {");
        System.out.println("        this.marca = marca;");
        System.out.println("        this.modelo = modelo;");
        System.out.println("        this.velocidadMaxima = velocidadMaxima;");
        System.out.println("    }");
        System.out.println();
        System.out.println("    public void acelerar() {");
        System.out.println("        System.out.println(\"El vehiculo acelera\");");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("class Coche extends Vehiculo {");
        System.out.println("    private int numPuertas;");
        System.out.println();
        System.out.println("    public Coche(String marca, String modelo, int velMax, int numPuertas) {");
        System.out.println("        super(marca, modelo, velMax);");
        System.out.println("        this.numPuertas = numPuertas;");
        System.out.println("    }");
        System.out.println();
        System.out.println("    @Override");
        System.out.println("    public void acelerar() {");
        System.out.println("        System.out.println(\"El coche \" + marca + \" acelera con \" + numPuertas + \" puertas\");");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("class Moto extends Vehiculo {");
        System.out.println("    private String tipoManillar;");
        System.out.println();
        System.out.println("    public Moto(String marca, String modelo, int velMax, String tipoManillar) {");
        System.out.println("        super(marca, modelo, velMax);");
        System.out.println("        this.tipoManillar = tipoManillar;");
        System.out.println("    }");
        System.out.println();
        System.out.println("    @Override");
        System.out.println("    public void acelerar() {");
        System.out.println("        System.out.println(\"La moto \" + marca + \" acelera con manillar \" + tipoManillar);");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: Coche y Moto heredan de Vehiculo con extends.");
        System.out.println("super() llama al constructor de la superclase. @Override sobrescribe metodos.");
    }

    static void solucion_2() {
        System.out.println("=== SOLUCION 2: Sistema de empleados ===");
        System.out.println("class Empleado {");
        System.out.println("    protected String nombre;");
        System.out.println("    protected double salario;");
        System.out.println();
        System.out.println("    public Empleado(String nombre, double salario) {");
        System.out.println("        this.nombre = nombre;");
        System.out.println("        this.salario = salario;");
        System.out.println("    }");
        System.out.println();
        System.out.println("    public double calcularBono() { return 0; }");
        System.out.println("}");
        System.out.println();
        System.out.println("class Gerente extends Empleado {");
        System.out.println("    public Gerente(String nombre, double salario) {");
        System.out.println("        super(nombre, salario);");
        System.out.println("    }");
        System.out.println();
        System.out.println("    @Override");
        System.out.println("    public double calcularBono() {");
        System.out.println("        return salario * 0.20;");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("class Desarrollador extends Empleado {");
        System.out.println("    public Desarrollador(String nombre, double salario) {");
        System.out.println("        super(nombre, salario);");
        System.out.println("    }");
        System.out.println();
        System.out.println("    @Override");
        System.out.println("    public double calcularBono() {");
        System.out.println("        return salario * 0.10;");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: Cada subclase sobrescribe calcularBono() con su propio porcentaje.");
        System.out.println("super(nombre, salario) reutiliza el constructor de Empleado.");
    }

    static void solucion_3() {
        System.out.println("=== SOLUCION 3: Figuras geometricas ===");
        System.out.println("abstract class Figura {");
        System.out.println("    public abstract double calcularArea();");
        System.out.println("}");
        System.out.println();
        System.out.println("class Circulo extends Figura {");
        System.out.println("    private double radio;");
        System.out.println();
        System.out.println("    public Circulo(double radio) { this.radio = radio; }");
        System.out.println();
        System.out.println("    @Override");
        System.out.println("    public double calcularArea() {");
        System.out.println("        return Math.PI * radio * radio;");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("class Rectangulo extends Figura {");
        System.out.println("    private double base;");
        System.out.println("    private double altura;");
        System.out.println();
        System.out.println("    public Rectangulo(double base, double altura) {");
        System.out.println("        this.base = base;");
        System.out.println("        this.altura = altura;");
        System.out.println("    }");
        System.out.println();
        System.out.println("    @Override");
        System.out.println("    public double calcularArea() {");
        System.out.println("        return base * altura;");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: Figura es abstracta y define el contrato calcularArea().");
        System.out.println("Circulo y Rectangulo implementan el metodo con sus formulas especificas.");
    }
}
