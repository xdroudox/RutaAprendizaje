/**
 * SOLUCIONES - Interfaces y Clases Abstractas
 * Ejecuta: python scripts/runner.py 2 5 [ejercicio] -s
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
        System.out.println("=== SOLUCION 1: Interface Volador ===");
        System.out.println("interface Volador {");
        System.out.println("    void volar();");
        System.out.println("}");
        System.out.println();
        System.out.println("class Pajaro implements Volador {");
        System.out.println("    public void volar() {");
        System.out.println("        System.out.println(\"El pajaro vuela batiendo alas\");");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("class Avion implements Volador {");
        System.out.println("    public void volar() {");
        System.out.println("        System.out.println(\"El avion vuela con motores\");");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("// En el main:");
        System.out.println("Volador p = new Pajaro();");
        System.out.println("Volador a = new Avion();");
        System.out.println("p.volar();");
        System.out.println("a.volar();");
        System.out.println();
        System.out.println("Explicacion: implements vincula una clase a una interface.");
        System.out.println("Los metodos de interface son public por defecto.");
    }

    static void solucion_2() {
        System.out.println("=== SOLUCION 2: Clase abstracta Forma ===");
        System.out.println("abstract class Forma {");
        System.out.println("    abstract double area();");
        System.out.println();
        System.out.println("    void info() {");
        System.out.println("        System.out.println(\"Soy una forma\");");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("class Circulo extends Forma {");
        System.out.println("    double radio;");
        System.out.println();
        System.out.println("    Circulo(double radio) {");
        System.out.println("        this.radio = radio;");
        System.out.println("    }");
        System.out.println();
        System.out.println("    double area() {");
        System.out.println("        return Math.PI * radio * radio;");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("class Rectangulo extends Forma {");
        System.out.println("    double base, altura;");
        System.out.println();
        System.out.println("    Rectangulo(double base, double altura) {");
        System.out.println("        this.base = base;");
        System.out.println("        this.altura = altura;");
        System.out.println("    }");
        System.out.println();
        System.out.println("    double area() {");
        System.out.println("        return base * altura;");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("// En el main:");
        System.out.println("Forma c = new Circulo(5);");
        System.out.println("Forma r = new Rectangulo(4, 6);");
        System.out.println("System.out.println(c.area());");
        System.out.println("c.info();");
        System.out.println("System.out.println(r.area());");
        System.out.println("r.info();");
        System.out.println();
        System.out.println("Explicacion: abstract obliga a las subclases a implementar area().");
        System.out.println("info() es concreto y se hereda directamente.");
    }

    static void solucion_3() {
        System.out.println("=== SOLUCION 3: Interface Reproducible ===");
        System.out.println("interface Reproducible {");
        System.out.println("    void reproducir();");
        System.out.println("}");
        System.out.println();
        System.out.println("class Musica implements Reproducible {");
        System.out.println("    public void reproducir() {");
        System.out.println("        System.out.println(\"Reproduciendo cancion...\");");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("class Video implements Reproducible {");
        System.out.println("    public void reproducir() {");
        System.out.println("        System.out.println(\"Reproduciendo video...\");");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("// En el main:");
        System.out.println("Reproducible[] lista = {new Musica(), new Video()};");
        System.out.println("for (Reproducible r : lista) {");
        System.out.println("    r.reproducir();");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: Las interfaces permiten polimorfismo entre clases no relacionadas.");
    }
}
