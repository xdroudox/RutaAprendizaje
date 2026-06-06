/**
 * SOLUCIONES - Interfaces y Clases Abstractas (Java)
 * Ejecuta desde raiz: python scripts/runner.py 2 5 [ejercicio] -s
 */
public class Soluciones {

    public static void main(String[] args) {
        if (args.length > 0 && !args[0].startsWith("-")) {
            int num;
            try {
                num = Integer.parseInt(args[0]);
            } catch (NumberFormatException e) {
                System.out.println("Solucion no encontrada");
                return;
            }
            switch (num) {
                case 1: solucion_1(); break;
                case 2: solucion_2(); break;
                case 3: solucion_3(); break;
                default: System.out.println("Ejercicio no encontrado. Valores: 1-3");
            }
        } else {
            System.out.println("SOLUCIONES:");
            System.out.println("  🟢 1. Interface Volador");
            System.out.println("  🟡 2. Clase abstracta Forma");
            System.out.println("  🔴 3. Interface Reproducible");
        }
    }

    static void solucion_1() {
        System.out.println("=".repeat(50));
        System.out.println("🟢 SOLUCION 1: Interface Volador");
        System.out.println("=".repeat(50));
        System.out.println();

        System.out.println("--- CODIGO (Main.java) ---");
        System.out.println("""
interface Volador {
    void volar();
}

class Pajaro implements Volador {
    public void volar() {
        System.out.println("El pajaro vuela batiendo alas");
    }
}

class Avion implements Volador {
    public void volar() {
        System.out.println("El avion vuela con motores");
    }
}

public class Main {
    public static void main(String[] args) {
        Volador p = new Pajaro();
        Volador a = new Avion();

        p.volar();
        a.volar();
    }
}
""");

        System.out.println("--- EXPLICACION ---");
        System.out.println("""
1. `interface Volador { void volar(); }` — Define el CONTRATO.
   Cualquier clase que implemente Volador DEBE tener un metodo volar().

2. `class Pajaro implements Volador` — Pajaro FIRMA el contrato.
   Si no implementa volar(), Java da ERROR DE COMPILACION.

3. `public void volar()` — Los metodos de interface son implicitamente
   `public abstract`. La implementacion debe declararlos como `public`.

4. `Volador p = new Pajaro()` — Variable de tipo VOLADOR (la interface).
   El objeto es Pajaro. POLIMORFISMO via interface.
""");
    }

    static void solucion_2() {
        System.out.println("=".repeat(50));
        System.out.println("🟡 SOLUCION 2: Clase abstracta Forma");
        System.out.println("=".repeat(50));
        System.out.println();

        System.out.println("--- CODIGO (Main.java) ---");
        System.out.println("""
abstract class Forma {
    abstract double area();

    void info() {
        System.out.println("Soy una forma");
    }
}

class Circulo extends Forma {
    double radio;

    Circulo(double radio) {
        this.radio = radio;
    }

    double area() {
        return Math.PI * radio * radio;
    }
}

class Rectangulo extends Forma {
    double base;
    double altura;

    Rectangulo(double base, double altura) {
        this.base = base;
        this.altura = altura;
    }

    double area() {
        return base * altura;
    }
}

public class Main {
    public static void main(String[] args) {
        Forma c = new Circulo(5);
        Forma r = new Rectangulo(4, 6);

        System.out.println("Circulo area: " + c.area());
        c.info();

        System.out.println("Rectangulo area: " + r.area());
        r.info();
    }
}
""");

        System.out.println("--- EXPLICACION ---");
        System.out.println("""
1. `abstract class Forma` — NO se puede instanciar. new Forma() da ERROR.
   Solo sirve como base para otras clases.

2. `abstract double area();` — Metodo ABSTRACT: sin cuerpo, solo la firma.
   OBLIGA a las subclases a implementarlo.

3. `void info()` — Metodo CONCRETO: tiene implementacion completa.
   Las subclases lo HEREDAN sin necesidad de reescribirlo.

4. `class Circulo extends Forma` — Circulo hereda de Forma.
   DEBE implementar area(), si no, Circulo tambien debe ser abstract.

5. `c.info()` — Aunque Circulo no definio info(), lo hereda de Forma.
   Imprime "Soy una forma" para cualquier forma que lo llame.
""");
    }

    static void solucion_3() {
        System.out.println("=".repeat(50));
        System.out.println("🔴 SOLUCION 3: Interface Reproducible");
        System.out.println("=".repeat(50));
        System.out.println();

        System.out.println("--- CODIGO (Main.java) ---");
        System.out.println("""
interface Reproducible {
    void reproducir();
}

class Musica implements Reproducible {
    public void reproducir() {
        System.out.println("Reproduciendo cancion...");
    }
}

class Video implements Reproducible {
    public void reproducir() {
        System.out.println("Reproduciendo video...");
    }
}

public class Main {
    public static void main(String[] args) {
        Reproducible[] lista = {new Musica(), new Video()};

        for (Reproducible r : lista) {
            r.reproducir();
        }
    }
}
""");

        System.out.println("--- EXPLICACION ---");
        System.out.println("""
1. `interface Reproducible` — Define la capacidad de "ser reproducido".
   Cualquier clase que implemente Reproducible adquiere esta capacidad.

2. Musica y Video NO estan relacionadas por herencia, pero AMBAS
   implementan Reproducible. La interface las une polimorficamente.

3. `Reproducible[] lista = {new Musica(), new Video()};` — Array de
   interface. Puede contener objetos de CLASES NO RELACIONADAS entre si,
   siempre que todas implementen Reproducible.

4. Las interfaces permiten POLIMORFISMO ENTRE CLASES NO RELACIONADAS
   por herencia. Eso no se puede lograr solo con clases abstractas.
""");
    }
}
