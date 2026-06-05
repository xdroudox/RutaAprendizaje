/**
 * SOLUCIONES - Clases y Objetos
 * Ejecuta: python scripts/runner.py 2 1 [ejercicio] -s
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
        System.out.println("=== SOLUCION 1: Clase Persona ===");
        System.out.println("class Persona {");
        System.out.println("    String nombre;");
        System.out.println("    int edad;");
        System.out.println();
        System.out.println("    Persona(String nombre, int edad) {");
        System.out.println("        this.nombre = nombre;");
        System.out.println("        this.edad = edad;");
        System.out.println("    }");
        System.out.println();
        System.out.println("    void mostrarDatos() {");
        System.out.println("        System.out.println(\"Nombre: \" + nombre);");
        System.out.println("        System.out.println(\"Edad: \" + edad);");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("// En el main:");
        System.out.println("Persona p1 = new Persona(\"Ana\", 25);");
        System.out.println("Persona p2 = new Persona(\"Luis\", 30);");
        System.out.println("p1.mostrarDatos();");
        System.out.println("p2.mostrarDatos();");
        System.out.println();
        System.out.println("Explicacion: La clase define el molde. new crea objetos.");
        System.out.println("this.nombre distingue el atributo del parametro.");
    }

    static void solucion_2() {
        System.out.println("=== SOLUCION 2: Clase Rectangulo ===");
        System.out.println("class Rectangulo {");
        System.out.println("    double base;");
        System.out.println("    double altura;");
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
        System.out.println("Rectangulo r = new Rectangulo(5, 3);");
        System.out.println("System.out.println(\"Area: \" + r.area());");
        System.out.println();
        System.out.println("Explicacion: area() es un metodo que calcula y retorna un valor.");
    }

    static void solucion_3() {
        System.out.println("=== SOLUCION 3: Clase Libro ===");
        System.out.println("class Libro {");
        System.out.println("    String titulo;");
        System.out.println("    String autor;");
        System.out.println("    int paginas;");
        System.out.println();
        System.out.println("    Libro(String titulo, String autor, int paginas) {");
        System.out.println("        this.titulo = titulo;");
        System.out.println("        this.autor = autor;");
        System.out.println("        this.paginas = paginas;");
        System.out.println("    }");
        System.out.println();
        System.out.println("    boolean esLargo() {");
        System.out.println("        return paginas > 300;");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("// En el main:");
        System.out.println("Libro l1 = new Libro(\"Don Quijote\", \"Cervantes\", 500);");
        System.out.println("Libro l2 = new Libro(\"Platero\", \"Jimenez\", 150);");
        System.out.println("System.out.println(l1.titulo + \" es largo? \" + l1.esLargo());");
        System.out.println("System.out.println(l2.titulo + \" es largo? \" + l2.esLargo());");
        System.out.println();
        System.out.println("Explicacion: esLargo() retorna boolean. paginas > 300 es una expresion logica.");
    }
}
