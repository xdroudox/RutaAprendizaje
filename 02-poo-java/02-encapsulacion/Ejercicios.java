/**
 * EJERCICIOS - Encapsulacion (Java)
 * Ejecuta desde raiz: python scripts/runner.py 2 2 [ejercicio]
 *
 * Niveles:
 *   🟢 Ej 1: CuentaBancaria con saldo private y validacion
 *   🟡 Ej 2: Producto con precio private y validacion
 *   🔴 Ej 3: Estudiante con notas private y promedio()
 *
 * Pistas: python scripts/runner.py 2 2 N -p [1|2|3]
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
            System.out.println("  🟢 1. CuentaBancaria con saldo private y validacion");
            System.out.println("  🟡 2. Producto con precio private y validacion");
            System.out.println("  🔴 3. Estudiante con notas private y promedio()");
            System.out.println();
            System.out.println("Ejecuta: python scripts/runner.py 2 2 [N]");
            System.out.println("Pistas:  python scripts/runner.py 2 2 N -p [1|2|3]");
        }
    }

    // -----------------------------------------------------------------------
    // 🟢 EJERCICIO 1: CuentaBancaria
    // -----------------------------------------------------------------------

    static void ejercicio_1(int pista) {
        System.out.println(">> 🟢 EJERCICIO 1: CuentaBancaria");
        System.out.println("-".repeat(50));

        if (pista == 1) {
            System.out.println("\n💡 Pista 1: Estructura basica:");
            System.out.println("  class CuentaBancaria {");
            System.out.println("      private double saldo;");
            System.out.println();
            System.out.println("      public double getSaldo() {");
            System.out.println("          return saldo;");
            System.out.println("      }");
            System.out.println("  }");
            return;
        } else if (pista == 2) {
            System.out.println("\n💡 Pista 2: Setter con validacion:");
            System.out.println("  public void setSaldo(double saldo) {");
            System.out.println("      if (saldo >= 0) {");
            System.out.println("          this.saldo = saldo;");
            System.out.println("      } else {");
            System.out.println("          System.out.println(\"Error: saldo no puede ser negativo\");");
            System.out.println("      }");
            System.out.println("  }");
            return;
        } else if (pista == 3) {
            System.out.println("\n💡 Pista 3: En el main:");
            System.out.println("  CuentaBancaria c = new CuentaBancaria();");
            System.out.println("  c.setSaldo(1000);");
            System.out.println("  System.out.println(c.getSaldo());  // 1000.0");
            System.out.println("  c.setSaldo(-50);                  // Error");
            return;
        }

        System.out.println("\nCrea las siguientes clases en un archivo Main.java:");
        System.out.println();
        System.out.println("1. Clase CuentaBancaria con atributo saldo (private double)");
        System.out.println("2. Getter getSaldo() que retorne el saldo");
        System.out.println("3. Setter setSaldo(double) que valide saldo >= 0");
        System.out.println("4. En el main, prueba con 1000 y -50");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    // -----------------------------------------------------------------------
    // 🟡 EJERCICIO 2: Producto
    // -----------------------------------------------------------------------

    static void ejercicio_2(int pista) {
        System.out.println(">> 🟡 EJERCICIO 2: Producto");
        System.out.println("-".repeat(50));

        if (pista == 1) {
            System.out.println("\n💡 Pista 1: Atributos y constructor:");
            System.out.println("  class Producto {");
            System.out.println("      private String nombre;");
            System.out.println("      private double precio;");
            System.out.println();
            System.out.println("      public Producto(String nombre, double precio) {");
            System.out.println("          this.nombre = nombre;");
            System.out.println("          setPrecio(precio);  // Reutiliza la validacion!");
            System.out.println("      }");
            System.out.println("  }");
            return;
        } else if (pista == 2) {
            System.out.println("\n💡 Pista 2: Setter con validacion:");
            System.out.println("  public void setPrecio(double precio) {");
            System.out.println("      if (precio >= 0) {");
            System.out.println("          this.precio = precio;");
            System.out.println("      } else {");
            System.out.println("          System.out.println(\"Error: precio no puede ser negativo\");");
            System.out.println("      }");
            System.out.println("  }");
            return;
        } else if (pista == 3) {
            System.out.println("\n💡 Pista 3: En el main:");
            System.out.println("  Producto p1 = new Producto(\"Laptop\", 1500);");
            System.out.println("  System.out.println(p1.getPrecio());  // 1500.0");
            System.out.println("  Producto p2 = new Producto(\"Mouse\", -50);  // Error");
            return;
        }

        System.out.println("\nCrea las siguientes clases en un archivo Main.java:");
        System.out.println();
        System.out.println("1. Clase Producto con nombre (private String) y precio (private double)");
        System.out.println("2. Constructor que reciba ambos y use setPrecio() para validar");
        System.out.println("3. Getter y setter para precio con validacion anti-negativos");
        System.out.println("4. En el main, prueba con precio valido e invalido");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    // -----------------------------------------------------------------------
    // 🔴 EJERCICIO 3: Estudiante
    // -----------------------------------------------------------------------

    static void ejercicio_3(int pista) {
        System.out.println(">> 🔴 EJERCICIO 3: Estudiante");
        System.out.println("-".repeat(50));

        if (pista == 1) {
            System.out.println("\n💡 Pista 1: Atributos y constructor:");
            System.out.println("  class Estudiante {");
            System.out.println("      private double[] notas;");
            System.out.println();
            System.out.println("      public Estudiante(double[] notas) {");
            System.out.println("          this.notas = notas;");
            System.out.println("      }");
            System.out.println("  }");
            return;
        } else if (pista == 2) {
            System.out.println("\n💡 Pista 2: Getter, setter y promedio:");
            System.out.println("  public double[] getNotas() { return notas; }");
            System.out.println("  public void setNotas(double[] notas) { this.notas = notas; }");
            System.out.println();
            System.out.println("  public double promedio() {");
            System.out.println("      double suma = 0;");
            System.out.println("      for (double n : notas) {");
            System.out.println("          suma += n;");
            System.out.println("      }");
            System.out.println("      return suma / notas.length;");
            System.out.println("  }");
            return;
        } else if (pista == 3) {
            System.out.println("\n💡 Pista 3: En el main:");
            System.out.println("  double[] notas = {7.5, 8.0, 6.5};");
            System.out.println("  Estudiante e = new Estudiante(notas);");
            System.out.println("  System.out.println(\"Promedio: \" + e.promedio());");
            return;
        }

        System.out.println("\nCrea las siguientes clases en un archivo Main.java:");
        System.out.println();
        System.out.println("1. Clase Estudiante con atributo notas (private double[])");
        System.out.println("2. Constructor que reciba el array");
        System.out.println("3. Getter, setter y metodo promedio()");
        System.out.println("4. En el main, prueba con {7.5, 8.0, 6.5}");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }
}
