/**
 * SOLUCIONES - Polimorfismo
 * Ejecuta: python scripts/runner.py 2 4 [ejercicio] -s
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
        System.out.println("=== SOLUCION 1: Sobrecarga de sumar() ===");
        System.out.println("class Calculadora {");
        System.out.println("    int sumar(int a, int b) {");
        System.out.println("        return a + b;");
        System.out.println("    }");
        System.out.println();
        System.out.println("    int sumar(int a, int b, int c) {");
        System.out.println("        return a + b + c;");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("// En el main:");
        System.out.println("Calculadora calc = new Calculadora();");
        System.out.println("System.out.println(calc.sumar(3, 4));");
        System.out.println("System.out.println(calc.sumar(3, 4, 5));");
        System.out.println();
        System.out.println("Explicacion: La sobrecarga permite mismo nombre con distintos parametros.");
    }

    static void solucion_2() {
        System.out.println("=== SOLUCION 2: Array polimorfico de Animales ===");
        System.out.println("Animal[] animales = new Animal[2];");
        System.out.println("animales[0] = new Perro();");
        System.out.println("animales[1] = new Gato();");
        System.out.println();
        System.out.println("for (Animal a : animales) {");
        System.out.println("    a.hacerSonido();");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: El array es de tipo Animal pero contiene objetos Perro y Gato.");
        System.out.println("Java llama al metodo adecuado segun el tipo real del objeto (dynamic dispatch).");
    }

    static void solucion_3() {
        System.out.println("=== SOLUCION 3: Figura, Circulo y Rectangulo ===");
        System.out.println("class Figura {");
        System.out.println("    double area() {");
        System.out.println("        return 0.0;");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("class Circulo extends Figura {");
        System.out.println("    double radio;");
        System.out.println();
        System.out.println("    Circulo(double radio) {");
        System.out.println("        this.radio = radio;");
        System.out.println("    }");
        System.out.println();
        System.out.println("    @Override");
        System.out.println("    double area() {");
        System.out.println("        return Math.PI * radio * radio;");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("class Rectangulo extends Figura {");
        System.out.println("    double base, altura;");
        System.out.println();
        System.out.println("    Rectangulo(double base, double altura) {");
        System.out.println("        this.base = base;");
        System.out.println("        this.altura = altura;");
        System.out.println("    }");
        System.out.println();
        System.out.println("    @Override");
        System.out.println("    double area() {");
        System.out.println("        return base * altura;");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("// En el main:");
        System.out.println("Figura[] figuras = new Figura[2];");
        System.out.println("figuras[0] = new Circulo(5);");
        System.out.println("figuras[1] = new Rectangulo(4, 6);");
        System.out.println("for (Figura f : figuras) {");
        System.out.println("    System.out.println(\"Area: \" + f.area());");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: Cada subclase tiene su propia implementacion de area().");
    }
}
