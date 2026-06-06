/**
 * EJERCICIOS - Polimorfismo (Java)
 * Ejecuta desde raiz: python scripts/runner.py 2 4 [ejercicio]
 *
 * Niveles:
 *   🟢 Ej 1: Sobrecarga de sumar() con 2 y 3 parametros
 *   🟡 Ej 2: Array polimorfico de Animales con hacerSonido()
 *   🔴 Ej 3: Figura, Circulo y Rectangulo con area()
 *
 * Pistas: python scripts/runner.py 2 4 N -p [1|2|3]
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
            System.out.println("  🟢 1. Sobrecarga de sumar() con 2 y 3 parametros");
            System.out.println("  🟡 2. Array polimorfico de Animales");
            System.out.println("  🔴 3. Figura, Circulo y Rectangulo");
            System.out.println();
            System.out.println("Ejecuta: python scripts/runner.py 2 4 [N]");
            System.out.println("Pistas:  python scripts/runner.py 2 4 N -p [1|2|3]");
        }
    }

    // -----------------------------------------------------------------------
    // 🟢 EJERCICIO 1: Sobrecarga de sumar()
    // -----------------------------------------------------------------------

    static void ejercicio_1(int pista) {
        System.out.println(">> 🟢 EJERCICIO 1: Sobrecarga de sumar()");
        System.out.println("-".repeat(50));

        if (pista == 1) {
            System.out.println("\n💡 Pista 1: Define la clase Calculadora con dos metodos:");
            System.out.println("  class Calculadora {");
            System.out.println("      int sumar(int a, int b) {");
            System.out.println("          return a + b;");
            System.out.println("      }");
            System.out.println("      int sumar(int a, int b, int c) {");
            System.out.println("          return a + b + c;");
            System.out.println("      }");
            System.out.println("  }");
            return;
        } else if (pista == 2) {
            System.out.println("\n💡 Pista 2: En el main, crea una Calculadora:");
            System.out.println("  Calculadora calc = new Calculadora();");
            return;
        } else if (pista == 3) {
            System.out.println("\n💡 Pista 3: Prueba ambos metodos:");
            System.out.println("  System.out.println(calc.sumar(3, 4));     // 7");
            System.out.println("  System.out.println(calc.sumar(3, 4, 5)); // 12");
            return;
        }

        System.out.println("\nCrea las siguientes clases en un archivo Main.java:");
        System.out.println();
        System.out.println("1. Clase Calculadora con metodo sumar(int a, int b)");
        System.out.println("2. Sobrecarga: sumar(int a, int b, int c)");
        System.out.println("3. En el main, prueba ambos metodos e imprime resultados");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    // -----------------------------------------------------------------------
    // 🟡 EJERCICIO 2: Array polimorfico de Animales
    // -----------------------------------------------------------------------

    static void ejercicio_2(int pista) {
        System.out.println(">> 🟡 EJERCICIO 2: Array polimorfico de Animales");
        System.out.println("-".repeat(50));

        if (pista == 1) {
            System.out.println("\n💡 Pista 1: Define las clases Animal, Perro y Gato:");
            System.out.println("  class Animal {");
            System.out.println("      void hacerSonido() { System.out.println(\"...\"); }");
            System.out.println("  }");
            System.out.println("  class Perro extends Animal {");
            System.out.println("      @Override void hacerSonido() { System.out.println(\"Guau!\"); }");
            System.out.println("  }");
            System.out.println("  class Gato extends Animal {");
            System.out.println("      @Override void hacerSonido() { System.out.println(\"Miau!\"); }");
            System.out.println("  }");
            return;
        } else if (pista == 2) {
            System.out.println("\n💡 Pista 2: Crea el array polimorfico:");
            System.out.println("  Animal[] animales = new Animal[2];");
            System.out.println("  animales[0] = new Perro();");
            System.out.println("  animales[1] = new Gato();");
            return;
        } else if (pista == 3) {
            System.out.println("\n💡 Pista 3: Recorre el array con un for-each:");
            System.out.println("  for (Animal a : animales) {");
            System.out.println("      a.hacerSonido();  // Dynamic dispatch!");
            System.out.println("  }");
            return;
        }

        System.out.println("\nUsando las clases Animal, Perro y Gato del tema de herencia:");
        System.out.println();
        System.out.println("1. Define Animal con hacerSonido()");
        System.out.println("2. Perro y Gato heredan y sobrescriben");
        System.out.println("3. Crea Animal[] con un Perro y un Gato");
        System.out.println("4. Recorre con for y llama a hacerSonido()");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    // -----------------------------------------------------------------------
    // 🔴 EJERCICIO 3: Figura, Circulo y Rectangulo
    // -----------------------------------------------------------------------

    static void ejercicio_3(int pista) {
        System.out.println(">> 🔴 EJERCICIO 3: Figura, Circulo y Rectangulo");
        System.out.println("-".repeat(50));

        if (pista == 1) {
            System.out.println("\n💡 Pista 1: Clase base Figura:");
            System.out.println("  class Figura {");
            System.out.println("      double area() { return 0.0; }");
            System.out.println("  }");
            return;
        } else if (pista == 2) {
            System.out.println("\n💡 Pista 2: Subclases con @Override:");
            System.out.println("  class Circulo extends Figura {");
            System.out.println("      double radio;");
            System.out.println("      Circulo(double r) { this.radio = r; }");
            System.out.println("      @Override double area() { return Math.PI * radio * radio; }");
            System.out.println("  }");
            System.out.println("  class Rectangulo extends Figura {");
            System.out.println("      double base, altura;");
            System.out.println("      Rectangulo(double b, double a) { this.base = b; this.altura = a; }");
            System.out.println("      @Override double area() { return base * altura; }");
            System.out.println("  }");
            return;
        } else if (pista == 3) {
            System.out.println("\n💡 Pista 3: Array polimorfico y bucle:");
            System.out.println("  Figura[] figuras = new Figura[2];");
            System.out.println("  figuras[0] = new Circulo(5);");
            System.out.println("  figuras[1] = new Rectangulo(4, 6);");
            System.out.println("  for (Figura f : figuras) {");
            System.out.println("      System.out.println(\"Area: \" + f.area());");
            System.out.println("  }");
            return;
        }

        System.out.println("\nCrea las siguientes clases en un archivo Main.java:");
        System.out.println();
        System.out.println("1. Clase Figura con metodo area() que retorne 0.0");
        System.out.println("2. Circulo hereda, atributo radio, area() = PI * r^2");
        System.out.println("3. Rectangulo hereda, atributos base y altura, area() = b * a");
        System.out.println("4. Array Figura[] con ambos, bucle mostrando areas");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }
}
