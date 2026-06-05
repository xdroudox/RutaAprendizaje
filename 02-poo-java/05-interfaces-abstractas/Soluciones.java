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
        System.out.println("=== SOLUCION 1: Interfaz Dibujable ===");
        System.out.println("interface Dibujable {");
        System.out.println("    void dibujar();");
        System.out.println("    void cambiarColor(String color);");
        System.out.println("}");
        System.out.println();
        System.out.println("class Circulo implements Dibujable {");
        System.out.println("    private double radio;");
        System.out.println("    private String color = \"rojo\";");
        System.out.println("    public Circulo(double radio) { this.radio = radio; }");
        System.out.println("    @Override");
        System.out.println("    public void dibujar() {");
        System.out.println("        System.out.println(\"Dibujando circulo de color \" + color);");
        System.out.println("    }");
        System.out.println("    @Override");
        System.out.println("    public void cambiarColor(String color) { this.color = color; }");
        System.out.println("}");
        System.out.println();
        System.out.println("class Rectangulo implements Dibujable {");
        System.out.println("    private double base, altura;");
        System.out.println("    private String color = \"azul\";");
        System.out.println("    public Rectangulo(double base, double altura) {");
        System.out.println("        this.base = base; this.altura = altura;");
        System.out.println("    }");
        System.out.println("    @Override");
        System.out.println("    public void dibujar() {");
        System.out.println("        System.out.println(\"Dibujando rectangulo de color \" + color);");
        System.out.println("    }");
        System.out.println("    @Override");
        System.out.println("    public void cambiarColor(String color) { this.color = color; }");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: La interfaz define el contrato. Cada clase implementa");
        System.out.println("los metodos a su manera. Pueden tener sus propios atributos adicionales.");
    }

    static void solucion_2() {
        System.out.println("=== SOLUCION 2: Clase abstracta Animal ===");
        System.out.println("abstract class Animal {");
        System.out.println("    protected String nombre;");
        System.out.println();
        System.out.println("    public Animal(String nombre) { this.nombre = nombre; }");
        System.out.println();
        System.out.println("    public void dormir() {");
        System.out.println("        System.out.println(nombre + \" esta durmiendo\");");
        System.out.println("    }");
        System.out.println();
        System.out.println("    public abstract void hacerSonido();");
        System.out.println("}");
        System.out.println();
        System.out.println("class Perro extends Animal {");
        System.out.println("    public Perro(String nombre) { super(nombre); }");
        System.out.println("    @Override");
        System.out.println("    public void hacerSonido() {");
        System.out.println("        System.out.println(nombre + \" dice: Guau\");");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("class Gato extends Animal {");
        System.out.println("    public Gato(String nombre) { super(nombre); }");
        System.out.println("    @Override");
        System.out.println("    public void hacerSonido() {");
        System.out.println("        System.out.println(nombre + \" dice: Miau\");");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: Animal es abstracta porque tiene un metodo abstracto.");
        System.out.println("dormir() es concreto y se hereda. hacerSonido() debe implementarse.");
    }

    static void solucion_3() {
        System.out.println("=== SOLUCION 3: Multiple implementacion ===");
        System.out.println("interface Nadador {");
        System.out.println("    void nadar();");
        System.out.println("}");
        System.out.println();
        System.out.println("interface Caminador {");
        System.out.println("    void caminar();");
        System.out.println("}");
        System.out.println();
        System.out.println("class Pato implements Nadador, Caminador {");
        System.out.println("    @Override");
        System.out.println("    public void nadar() {");
        System.out.println("        System.out.println(\"El pato esta nadando\");");
        System.out.println("    }");
        System.out.println("    @Override");
        System.out.println("    public void caminar() {");
        System.out.println("        System.out.println(\"El pato esta caminando\");");
        System.out.println("    }");
        System.out.println("    public void volar() {");
        System.out.println("        System.out.println(\"El pato esta volando\");");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("public class Main {");
        System.out.println("    public static void main(String[] args) {");
        System.out.println("        Pato pato = new Pato();");
        System.out.println("        pato.nadar();");
        System.out.println("        pato.caminar();");
        System.out.println("        pato.volar();");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: Java permite implementar multiples interfaces.");
        System.out.println("Pato implementa Nadador y Caminador, y anade su propio metodo volar().");
    }
}
