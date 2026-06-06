/**
 * EJERCICIOS - Herencia (Java)
 * Ejecuta desde raiz: python scripts/runner.py 2 3 [ejercicio]
 *
 * Niveles:
 *   🟢 Ej 1: Animal, Perro y Gato (herencia basica)
 *   🟡 Ej 2: Vehiculo, Coche y Bicicleta (herencia con atributos)
 *   🔴 Ej 3: Empleado, Gerente y Vendedor (herencia con calculos)
 *
 * Pistas: python scripts/runner.py 2 3 N -p [1|2|3]
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

        if (args.length > 0) {
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
            System.out.println("  🟢 1. Animal, Perro y Gato con herencia");
            System.out.println("  🟡 2. Vehiculo, Coche y Bicicleta con herencia");
            System.out.println("  🔴 3. Empleado, Gerente y Vendedor con herencia");
            System.out.println();
            System.out.println("Ejecuta: python scripts/runner.py 2 3 [N]");
            System.out.println("Pistas:  python scripts/runner.py 2 3 N -p [1|2|3]");
        }
    }

    // -----------------------------------------------------------------------
    // 🟢 EJERCICIO 1: Animal, Perro y Gato
    // -----------------------------------------------------------------------

    static void ejercicio_1(int pista) {
        System.out.println(">> 🟢 EJERCICIO 1: Animal, Perro y Gato");
        System.out.println("-".repeat(50));

        if (pista == 1) {
            System.out.println("\n💡 Pista 1: Crea la clase Animal con un metodo hacerSonido():");
            System.out.println("  class Animal {");
            System.out.println("      void hacerSonido() {");
            System.out.println("          System.out.println(\"...\");");
            System.out.println("      }");
            System.out.println("  }");
            return;
        } else if (pista == 2) {
            System.out.println("\n💡 Pista 2: Las subclases usan extends y @Override:");
            System.out.println("  class Perro extends Animal {");
            System.out.println("      @Override");
            System.out.println("      void hacerSonido() {");
            System.out.println("          System.out.println(\"Guau!\");");
            System.out.println("      }");
            System.out.println("  }");
            return;
        } else if (pista == 3) {
            System.out.println("\n💡 Pista 3: En el main, crea objetos:");
            System.out.println("  Animal miPerro = new Perro();");
            System.out.println("  Animal miGato = new Gato();");
            System.out.println("  miPerro.hacerSonido();");
            System.out.println("  miGato.hacerSonido();");
            return;
        }

        System.out.println("\nCrea las siguientes clases en un archivo Main.java:");
        System.out.println();
        System.out.println("1. Clase Animal con metodo hacerSonido() que imprima \"...\"");
        System.out.println("2. Clase Perro que EXTENDS Animal y sobrescriba hacerSonido()");
        System.out.println("   imprimiendo \"Guau!\"");
        System.out.println("3. Clase Gato que EXTENDS Animal y sobrescriba haciendo \"Miau!\"");
        System.out.println("4. En el main, crea un Perro y un Gato y llama a hacerSonido()");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    // -----------------------------------------------------------------------
    // 🟡 EJERCICIO 2: Vehiculo, Coche y Bicicleta
    // -----------------------------------------------------------------------

    static void ejercicio_2(int pista) {
        System.out.println(">> 🟡 EJERCICIO 2: Vehiculo, Coche y Bicicleta");
        System.out.println("-".repeat(50));

        if (pista == 1) {
            System.out.println("\n💡 Pista 1: Vehiculo tiene un atributo velocidad y metodo mover():");
            System.out.println("  class Vehiculo {");
            System.out.println("      int velocidad;");
            System.out.println("      Vehiculo(int velocidad) {");
            System.out.println("          this.velocidad = velocidad;");
            System.out.println("      }");
            System.out.println("      void mover() {");
            System.out.println("          System.out.println(\"El vehiculo se mueve...\");");
            System.out.println("      }");
            System.out.println("  }");
            return;
        } else if (pista == 2) {
            System.out.println("\n💡 Pista 2: Las subclases usan super(velocidad):");
            System.out.println("  class Coche extends Vehiculo {");
            System.out.println("      Coche(int velocidad) {");
            System.out.println("          super(velocidad);");
            System.out.println("      }");
            return;
        } else if (pista == 3) {
            System.out.println("\n💡 Pista 3: En el main:");
            System.out.println("  Vehiculo coche = new Coche(120);");
            System.out.println("  Vehiculo bici = new Bicicleta(25);");
            System.out.println("  coche.mover();  // \"El coche acelera a 120 km/h\"");
            System.out.println("  bici.mover();   // \"La bicicleta pedalea a 25 km/h\"");
            return;
        }

        System.out.println("\nCrea las siguientes clases en un archivo Main.java:");
        System.out.println();
        System.out.println("1. Clase Vehiculo con atributo velocidad (int) y metodo mover()");
        System.out.println("   que imprima \"El vehiculo se mueve...\"");
        System.out.println("2. Clase Coche que sobrescriba mover() imprimiendo");
        System.out.println("   \"El coche acelera a \" + velocidad + \" km/h\"");
        System.out.println("3. Clase Bicicleta que sobrescriba mover() imprimiendo");
        System.out.println("   \"La bicicleta pedalea a \" + velocidad + \" km/h\"");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    // -----------------------------------------------------------------------
    // 🔴 EJERCICIO 3: Empleado, Gerente y Vendedor
    // -----------------------------------------------------------------------

    static void ejercicio_3(int pista) {
        System.out.println(">> 🔴 EJERCICIO 3: Empleado, Gerente y Vendedor");
        System.out.println("-".repeat(50));

        if (pista == 1) {
            System.out.println("\n💡 Pista 1: Empleado tiene nombre y calcularSalario():");
            System.out.println("  class Empleado {");
            System.out.println("      String nombre;");
            System.out.println("      Empleado(String nombre) {");
            System.out.println("          this.nombre = nombre;");
            System.out.println("      }");
            System.out.println("      double calcularSalario() {");
            System.out.println("          return 0.0;");
            System.out.println("      }");
            System.out.println("  }");
            return;
        } else if (pista == 2) {
            System.out.println("\n💡 Pista 2: Gerente agrega bono y sobrescribe:");
            System.out.println("  class Gerente extends Empleado {");
            System.out.println("      double bono;");
            System.out.println("      Gerente(String nombre, double bono) {");
            System.out.println("          super(nombre);");
            System.out.println("          this.bono = bono;");
            System.out.println("      }");
            System.out.println("      @Override");
            System.out.println("      double calcularSalario() {");
            System.out.println("          return 50000 + bono;");
            System.out.println("      }");
            System.out.println("  }");
            return;
        } else if (pista == 3) {
            System.out.println("\n💡 Pista 3: En el main:");
            System.out.println("  Empleado gerente = new Gerente(\"Ana\", 10000);");
            System.out.println("  Empleado vendedor = new Vendedor(\"Luis\", 5000);");
            System.out.println("  System.out.println(gerente.calcularSalario());  // 60000.0");
            System.out.println("  System.out.println(vendedor.calcularSalario()); // 35000.0");
            return;
        }

        System.out.println("\nCrea las siguientes clases en un archivo Main.java:");
        System.out.println();
        System.out.println("1. Clase Empleado con atributo nombre y metodo");
        System.out.println("   calcularSalario() que retorne 0.0");
        System.out.println("2. Gerente hereda, con atributo bono,");
        System.out.println("   calcularSalario() retorna 50000 + bono");
        System.out.println("3. Vendedor hereda, con atributo comision,");
        System.out.println("   calcularSalario() retorna 30000 + comision");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }
}
