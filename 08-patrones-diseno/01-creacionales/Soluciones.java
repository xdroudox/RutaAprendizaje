/**
 * SOLUCIONES - Patrones Creacionales
 * Ejecuta desde raiz: python scripts/runner.py 8 1 [ejercicio]
 */
public class Soluciones {
    public static void main(String[] args) {
        if (args.length > 0) {
            int num = Integer.parseInt(args[0]);
            switch (num) {
                case 1: ejercicio_1(); break;
                case 2: ejercicio_2(); break;
                case 3: ejercicio_3(); break;
            }
        } else {
            for (int i = 1; i <= 3; i++) {
                System.out.println("  " + i + ". [Solucion " + i + "]");
            }
        }
    }

    static void ejercicio_1() {
        System.out.println(">> SOLUCION 1: Singleton - Configuracion");
        System.out.println("-".repeat(40));

        class Configuracion {
            private static Configuracion instancia;
            private String host = "localhost";
            private int puerto = 3306;
            private String usuario = "root";
            private String password = "";

            private Configuracion() {}

            public static Configuracion getInstance() {
                if (instancia == null) {
                    instancia = new Configuracion();
                }
                return instancia;
            }

            public void mostrar() {
                System.out.println("Host: " + host + ", Puerto: " + puerto
                    + ", Usuario: " + usuario);
            }
        }

        Configuracion c1 = Configuracion.getInstance();
        Configuracion c2 = Configuracion.getInstance();
        System.out.println("Misma instancia? " + (c1 == c2));
        c1.mostrar();
    }

    static void ejercicio_2() {
        System.out.println(">> SOLUCION 2: Factory - Figuras");
        System.out.println("-".repeat(40));

        interface Figura { void dibujar(); }

        class Circulo implements Figura {
            public void dibujar() { System.out.println("Dibujando Circulo"); }
        }

        class Cuadrado implements Figura {
            public void dibujar() { System.out.println("Dibujando Cuadrado"); }
        }

        class FiguraFactory {
            public static Figura crearFigura(String tipo) {
                if (tipo.equalsIgnoreCase("circulo")) return new Circulo();
                if (tipo.equalsIgnoreCase("cuadrado")) return new Cuadrado();
                throw new IllegalArgumentException("Figura desconocida: " + tipo);
            }
        }

        Figura f1 = FiguraFactory.crearFigura("circulo");
        Figura f2 = FiguraFactory.crearFigura("cuadrado");
        f1.dibujar();
        f2.dibujar();
    }

    static void ejercicio_3() {
        System.out.println(">> SOLUCION 3: Builder - Pizza");
        System.out.println("-".repeat(40));

        class Pizza {
            private String masa;
            private String salsa;
            private String ingredientes;
            private String tamano;

            private Pizza(Builder b) {
                this.masa = b.masa;
                this.salsa = b.salsa;
                this.ingredientes = b.ingredientes;
                this.tamano = b.tamano;
            }

            public String toString() {
                return "Pizza{" + tamano + ", " + masa + ", " + salsa
                    + ", ingredientes=" + ingredientes + "}";
            }

            static class Builder {
                private String masa = "fina";
                private String salsa = "tomate";
                private String ingredientes = "queso";
                private String tamano = "mediana";

                Builder masa(String m) { this.masa = m; return this; }
                Builder salsa(String s) { this.salsa = s; return this; }
                Builder ingredientes(String i) { this.ingredientes = i; return this; }
                Builder tamano(String t) { this.tamano = t; return this; }
                Pizza build() { return new Pizza(this); }
            }
        }

        Pizza p1 = new Pizza.Builder().build();
        Pizza p2 = new Pizza.Builder()
            .masa("gruesa")
            .salsa("barbacoa")
            .ingredientes("queso, pepperoni, champinones")
            .tamano("familiar")
            .build();
        System.out.println("Basica: " + p1);
        System.out.println("Personalizada: " + p2);
    }
}
