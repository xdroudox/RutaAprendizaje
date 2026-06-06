/**
 * EJERCICIOS - Clases y Objetos (Java)
 * Ejecuta desde raiz: python scripts/runner.py 2 1 [ejercicio]
 *
 * Niveles:
 *   🟢 Ej 1: Persona con mostrarDatos()
 *   🟡 Ej 2: Rectangulo con area()
 *   🔴 Ej 3: Libro con esLargo()
 *
 * Pistas: python scripts/runner.py 2 1 N -p [1|2|3]
 */
public class Ejercicios {

    public static void main(String[] args) {
        // Detectar pistas
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
            System.out.println("  🟢 1. Persona con mostrarDatos()");
            System.out.println("  🟡 2. Rectangulo con area()");
            System.out.println("  🔴 3. Libro con esLargo()");
            System.out.println();
            System.out.println("Ejecuta: python scripts/runner.py 2 1 [N]");
            System.out.println("Pistas:  python scripts/runner.py 2 1 N -p [1|2|3]");
        }
    }

    // -----------------------------------------------------------------------
    // 🟢 EJERCICIO 1: Clase Persona
    // -----------------------------------------------------------------------

    static void ejercicio_1(int pista) {
        System.out.println(">> 🟢 EJERCICIO 1: Clase Persona");
        System.out.println("-".repeat(50));

        if (pista == 1) {
            System.out.println("\n💡 Pista 1: Estructura basica de la clase:");
            System.out.println("  class Persona {");
            System.out.println("      String nombre;");
            System.out.println("      int edad;");
            System.out.println();
            System.out.println("      Persona(String nombre, int edad) {");
            System.out.println("          this.nombre = nombre;");
            System.out.println("          this.edad = edad;");
            System.out.println("      }");
            System.out.println("  }");
            return;
        } else if (pista == 2) {
            System.out.println("\n💡 Pista 2: El metodo mostrarDatos():");
            System.out.println("  void mostrarDatos() {");
            System.out.println("      System.out.println(\"Nombre: \" + nombre);");
            System.out.println("      System.out.println(\"Edad: \" + edad);");
            System.out.println("  }");
            return;
        } else if (pista == 3) {
            System.out.println("\n💡 Pista 3: En el main:");
            System.out.println("  Persona p1 = new Persona(\"Ana\", 25);");
            System.out.println("  Persona p2 = new Persona(\"Luis\", 30);");
            System.out.println("  p1.mostrarDatos();");
            System.out.println("  p2.mostrarDatos();");
            return;
        }

        System.out.println("\nCrea las siguientes clases en un archivo Main.java:");
        System.out.println();
        System.out.println("1. Clase Persona con atributos nombre (String) y edad (int)");
        System.out.println("2. Constructor que inicialice ambos usando this");
        System.out.println("3. Metodo mostrarDatos() que imprima nombre y edad");
        System.out.println("4. En el main, crea dos personas y llama a mostrarDatos()");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    // -----------------------------------------------------------------------
    // 🟡 EJERCICIO 2: Clase Rectangulo
    // -----------------------------------------------------------------------

    static void ejercicio_2(int pista) {
        System.out.println(">> 🟡 EJERCICIO 2: Clase Rectangulo");
        System.out.println("-".repeat(50));

        if (pista == 1) {
            System.out.println("\n💡 Pista 1: Atributos y constructor:");
            System.out.println("  class Rectangulo {");
            System.out.println("      double base;");
            System.out.println("      double altura;");
            System.out.println();
            System.out.println("      Rectangulo(double base, double altura) {");
            System.out.println("          this.base = base;");
            System.out.println("          this.altura = altura;");
            System.out.println("      }");
            System.out.println("  }");
            return;
        } else if (pista == 2) {
            System.out.println("\n💡 Pista 2: El metodo area():");
            System.out.println("  double area() {");
            System.out.println("      return base * altura;");
            System.out.println("  }");
            System.out.println("  Recuerda: double porque base y altura son double");
            return;
        } else if (pista == 3) {
            System.out.println("\n💡 Pista 3: En el main:");
            System.out.println("  Rectangulo r = new Rectangulo(5, 3);");
            System.out.println("  System.out.println(\"Area: \" + r.area());  // 15.0");
            return;
        }

        System.out.println("\nCrea las siguientes clases en un archivo Main.java:");
        System.out.println();
        System.out.println("1. Clase Rectangulo con atributos base (double) y altura (double)");
        System.out.println("2. Constructor con parametros");
        System.out.println("3. Metodo area() que retorne base * altura");
        System.out.println("4. En el main, crea un rectangulo de 5x3 e imprime su area");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    // -----------------------------------------------------------------------
    // 🔴 EJERCICIO 3: Clase Libro
    // -----------------------------------------------------------------------

    static void ejercicio_3(int pista) {
        System.out.println(">> 🔴 EJERCICIO 3: Clase Libro");
        System.out.println("-".repeat(50));

        if (pista == 1) {
            System.out.println("\n💡 Pista 1: Atributos y constructor:");
            System.out.println("  class Libro {");
            System.out.println("      String titulo;");
            System.out.println("      String autor;");
            System.out.println("      int paginas;");
            System.out.println();
            System.out.println("      Libro(String titulo, String autor, int paginas) {");
            System.out.println("          this.titulo = titulo;");
            System.out.println("          this.autor = autor;");
            System.out.println("          this.paginas = paginas;");
            System.out.println("      }");
            System.out.println("  }");
            return;
        } else if (pista == 2) {
            System.out.println("\n💡 Pista 2: Metodo esLargo() retorna boolean:");
            System.out.println("  boolean esLargo() {");
            System.out.println("      return paginas > 300;");
            System.out.println("  }");
            return;
        } else if (pista == 3) {
            System.out.println("\n💡 Pista 3: En el main:");
            System.out.println("  Libro l1 = new Libro(\"Don Quijote\", \"Cervantes\", 500);");
            System.out.println("  Libro l2 = new Libro(\"Platero\", \"Jimenez\", 150);");
            System.out.println("  System.out.println(l1.titulo + \" es largo? \" + l1.esLargo());");
            System.out.println("  System.out.println(l2.titulo + \" es largo? \" + l2.esLargo());");
            return;
        }

        System.out.println("\nCrea las siguientes clases en un archivo Main.java:");
        System.out.println();
        System.out.println("1. Clase Libro con titulo (String), autor (String), paginas (int)");
        System.out.println("2. Constructor que inicialice todo");
        System.out.println("3. Metodo esLargo() que retorne true si paginas > 300");
        System.out.println("4. En el main, crea dos libros y muestra si son largos");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }
}
