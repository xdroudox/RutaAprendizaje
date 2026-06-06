/**
 * EJERCICIOS - Interfaces y Clases Abstractas (Java)
 * Ejecuta desde raiz: python scripts/runner.py 2 5 [ejercicio]
 *
 * Niveles:
 *   🟢 Ej 1: Interface Volador con Pajaro y Avion
 *   🟡 Ej 2: Clase abstracta Forma con Circulo y Rectangulo
 *   🔴 Ej 3: Interface Reproducible con Musica y Video
 *
 * Pistas: python scripts/runner.py 2 5 N -p [1|2|3]
 */
public class Ejercicios {

    public static void main(String[] args) {
        int pista = 0;
        for (int i = 0; i < args.length; i++) {
            if (args[i].equals("-p") && i + 1 < args.length) {
                try {
                    pista = Integer.parseInt(args[i + 1]);
                } catch (NumberFormatException e) {
                    pista = 0;
                }
            }
        }

        if (args.length > 0 && !args[0].startsWith("-")) {
            int num;
            try {
                num = Integer.parseInt(args[0]);
            } catch (NumberFormatException e) {
                System.out.println("Ejercicio no encontrado");
                return;
            }
            switch (num) {
                case 1: ejercicio_1(pista); break;
                case 2: ejercicio_2(pista); break;
                case 3: ejercicio_3(pista); break;
                default: System.out.println("Ejercicio no encontrado. Valores: 1-3");
            }
        } else {
            System.out.println("EJERCICIOS:");
            System.out.println("  🟢 1. Interface Volador con Pajaro y Avion");
            System.out.println("  🟡 2. Clase abstracta Forma con area()");
            System.out.println("  🔴 3. Interface Reproducible con Musica y Video");
            System.out.println();
            System.out.println("Ejecuta: python scripts/runner.py 2 5 [N]");
            System.out.println("Pistas:  python scripts/runner.py 2 5 N -p [1|2|3]");
        }
    }

    // -----------------------------------------------------------------------
    // 🟢 EJERCICIO 1: Interface Volador
    // -----------------------------------------------------------------------

    static void ejercicio_1(int pista) {
        System.out.println(">> 🟢 EJERCICIO 1: Interface Volador");
        System.out.println("-".repeat(50));

        if (pista == 1) {
            System.out.println("\n💡 Pista 1: Define la interface:");
            System.out.println("  interface Volador {");
            System.out.println("      void volar();");
            System.out.println("  }");
            return;
        } else if (pista == 2) {
            System.out.println("\n💡 Pista 2: Implementa en Pajaro y Avion:");
            System.out.println("  class Pajaro implements Volador {");
            System.out.println("      public void volar() { System.out.println(\"...batiendo alas\"); }");
            System.out.println("  }");
            System.out.println("  class Avion implements Volador {");
            System.out.println("      public void volar() { System.out.println(\"...con motores\"); }");
            System.out.println("  }");
            return;
        } else if (pista == 3) {
            System.out.println("\n💡 Pista 3: En el main:");
            System.out.println("  Volador p = new Pajaro();");
            System.out.println("  Volador a = new Avion();");
            System.out.println("  p.volar();");
            System.out.println("  a.volar();");
            return;
        }

        System.out.println("\nCrea las siguientes clases en un archivo Main.java:");
        System.out.println();
        System.out.println("1. Interface Volador con metodo volar()");
        System.out.println("2. Pajaro implements Volador: volar() imprime mensaje");
        System.out.println("3. Avion implements Volador: volar() imprime mensaje");
        System.out.println("4. En el main, crea ambos y llama a volar()");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    // -----------------------------------------------------------------------
    // 🟡 EJERCICIO 2: Clase abstracta Forma
    // -----------------------------------------------------------------------

    static void ejercicio_2(int pista) {
        System.out.println(">> 🟡 EJERCICIO 2: Clase abstracta Forma");
        System.out.println("-".repeat(50));

        if (pista == 1) {
            System.out.println("\n💡 Pista 1: Clase abstracta Forma:");
            System.out.println("  abstract class Forma {");
            System.out.println("      abstract double area();");
            System.out.println("      void info() { System.out.println(\"Soy una forma\"); }");
            System.out.println("  }");
            return;
        } else if (pista == 2) {
            System.out.println("\n💡 Pista 2: Circulo y Rectangulo heredan:");
            System.out.println("  class Circulo extends Forma {");
            System.out.println("      double radio;");
            System.out.println("      Circulo(double r) { this.radio = r; }");
            System.out.println("      double area() { return Math.PI * radio * radio; }");
            System.out.println("  }");
            System.out.println("  class Rectangulo extends Forma {");
            System.out.println("      double base, altura;");
            System.out.println("      Rectangulo(double b, double a) { this.base = b; this.altura = a; }");
            System.out.println("      double area() { return base * altura; }");
            System.out.println("  }");
            return;
        } else if (pista == 3) {
            System.out.println("\n💡 Pista 3: En el main:");
            System.out.println("  Forma c = new Circulo(5);");
            System.out.println("  Forma r = new Rectangulo(4, 6);");
            System.out.println("  System.out.println(c.area());");
            System.out.println("  c.info();");
            System.out.println("  System.out.println(r.area());");
            System.out.println("  r.info();");
            return;
        }

        System.out.println("\nCrea las siguientes clases en un archivo Main.java:");
        System.out.println();
        System.out.println("1. Clase abstracta Forma con area() abstracto e info() concreto");
        System.out.println("2. Circulo extends Forma con radio y area()");
        System.out.println("3. Rectangulo extends Forma con base, altura y area()");
        System.out.println("4. En el main, demuestra polimorfismo");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    // -----------------------------------------------------------------------
    // 🔴 EJERCICIO 3: Interface Reproducible
    // -----------------------------------------------------------------------

    static void ejercicio_3(int pista) {
        System.out.println(">> 🔴 EJERCICIO 3: Interface Reproducible");
        System.out.println("-".repeat(50));

        if (pista == 1) {
            System.out.println("\n💡 Pista 1: Define la interface:");
            System.out.println("  interface Reproducible {");
            System.out.println("      void reproducir();");
            System.out.println("  }");
            return;
        } else if (pista == 2) {
            System.out.println("\n💡 Pista 2: Implementaciones:");
            System.out.println("  class Musica implements Reproducible {");
            System.out.println("      public void reproducir() { System.out.println(\"Reproduciendo cancion...\"); }");
            System.out.println("  }");
            System.out.println("  class Video implements Reproducible {");
            System.out.println("      public void reproducir() { System.out.println(\"Reproduciendo video...\"); }");
            System.out.println("  }");
            return;
        } else if (pista == 3) {
            System.out.println("\n💡 Pista 3: Array polimorfico:");
            System.out.println("  Reproducible[] lista = {new Musica(), new Video()};");
            System.out.println("  for (Reproducible r : lista) {");
            System.out.println("      r.reproducir();");
            System.out.println("  }");
            return;
        }

        System.out.println("\nCrea las siguientes clases en un archivo Main.java:");
        System.out.println();
        System.out.println("1. Interface Reproducible con metodo reproducir()");
        System.out.println("2. Musica implements Reproducible");
        System.out.println("3. Video implements Reproducible");
        System.out.println("4. Array Reproducible[] con ambos, bucle llamando a reproducir()");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }
}
