/**
 * EJERCICIOS - Principios SOLID (Java)
 * Ejecuta desde raiz: python scripts/runner.py 2 6 [ejercicio]
 *
 * Niveles:
 *   🟢 Ej 1: SRP - Reporte e Impresora
 *   🟡 Ej 2: OCP - Sistema de descuentos
 *   🔴 Ej 3: DIP - Servicio con inyeccion de dependencia
 *
 * Pistas: python scripts/runner.py 2 6 N -p [1|2|3]
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
            System.out.println("  🟢 1. SRP: Reporte e Impresora");
            System.out.println("  🟡 2. OCP: Sistema de descuentos");
            System.out.println("  🔴 3. DIP: Servicio con inyeccion de dependencia");
            System.out.println();
            System.out.println("Ejecuta: python scripts/runner.py 2 6 [N]");
            System.out.println("Pistas:  python scripts/runner.py 2 6 N -p [1|2|3]");
        }
    }

    // -----------------------------------------------------------------------
    // 🟢 EJERCICIO 1: SRP
    // -----------------------------------------------------------------------

    static void ejercicio_1(int pista) {
        System.out.println(">> 🟢 EJERCICIO 1: SRP - Single Responsibility Principle");
        System.out.println("-".repeat(50));

        if (pista == 1) {
            System.out.println("\n💡 Pista 1: Clase Reporte solo con datos:");
            System.out.println("  class Reporte {");
            System.out.println("      String titulo;");
            System.out.println("      String contenido;");
            System.out.println("      Reporte(String titulo, String contenido) {");
            System.out.println("          this.titulo = titulo;");
            System.out.println("          this.contenido = contenido;");
            System.out.println("      }");
            System.out.println("  }");
            return;
        } else if (pista == 2) {
            System.out.println("\n💡 Pista 2: Clase Impresora separada:");
            System.out.println("  class Impresora {");
            System.out.println("      static void imprimir(Reporte r) {");
            System.out.println("          System.out.println(r.titulo);");
            System.out.println("          System.out.println(\"---\");");
            System.out.println("          System.out.println(r.contenido);");
            System.out.println("      }");
            System.out.println("  }");
            return;
        } else if (pista == 3) {
            System.out.println("\n💡 Pista 3: En el main:");
            System.out.println("  Reporte r = new Reporte(\"Ventas\", \"Resumen del mes\");");
            System.out.println("  Impresora.imprimir(r);");
            return;
        }

        System.out.println("\nCrea las siguientes clases en un archivo Main.java:");
        System.out.println();
        System.out.println("1. Clase Reporte con atributos titulo y contenido");
        System.out.println("2. Clase Impresora con metodo estatico imprimir(Reporte r)");
        System.out.println("3. En el main, crea un Reporte e imprimelo");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    // -----------------------------------------------------------------------
    // 🟡 EJERCICIO 2: OCP
    // -----------------------------------------------------------------------

    static void ejercicio_2(int pista) {
        System.out.println(">> 🟡 EJERCICIO 2: OCP - Open/Closed Principle");
        System.out.println("-".repeat(50));

        if (pista == 1) {
            System.out.println("\n💡 Pista 1: Interface Descuento:");
            System.out.println("  interface Descuento {");
            System.out.println("      double aplicar(double precio);");
            System.out.println("  }");
            return;
        } else if (pista == 2) {
            System.out.println("\n💡 Pista 2: Implementaciones:");
            System.out.println("  class DescuentoPorcentaje implements Descuento {");
            System.out.println("      double porcentaje;");
            System.out.println("      DescuentoPorcentaje(double p) { this.porcentaje = p; }");
            System.out.println("      public double aplicar(double p) { return p * (1 - porcentaje/100); }");
            System.out.println("  }");
            System.out.println("  class DescuentoFijo implements Descuento {");
            System.out.println("      double cantidad;");
            System.out.println("      DescuentoFijo(double c) { this.cantidad = c; }");
            System.out.println("      public double aplicar(double p) { return Math.max(0, p - cantidad); }");
            System.out.println("  }");
            return;
        } else if (pista == 3) {
            System.out.println("\n💡 Pista 3: CalculadoraPrecio y main:");
            System.out.println("  class CalculadoraPrecio {");
            System.out.println("      double calcular(double precio, Descuento d) { return d.aplicar(precio); }");
            System.out.println("  }");
            System.out.println("  // Main:");
            System.out.println("  CalculadoraPrecio calc = new CalculadoraPrecio();");
            System.out.println("  System.out.println(calc.calcular(100, new DescuentoPorcentaje(10)));");
            System.out.println("  System.out.println(calc.calcular(100, new DescuentoFijo(15)));");
            return;
        }

        System.out.println("\nCrea las siguientes clases en un archivo Main.java:");
        System.out.println();
        System.out.println("1. Interface Descuento con metodo aplicar(double)");
        System.out.println("2. DescuentoPorcentaje: aplica % de descuento");
        System.out.println("3. DescuentoFijo: resta cantidad fija");
        System.out.println("4. CalculadoraPrecio con calcular(precio, descuento)");
        System.out.println("5. En el main, prueba ambos descuentos");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    // -----------------------------------------------------------------------
    // 🔴 EJERCICIO 3: DIP
    // -----------------------------------------------------------------------

    static void ejercicio_3(int pista) {
        System.out.println(">> 🔴 EJERCICIO 3: DIP - Dependency Inversion Principle");
        System.out.println("-".repeat(50));

        if (pista == 1) {
            System.out.println("\n💡 Pista 1: Interface BaseDatos:");
            System.out.println("  interface BaseDatos {");
            System.out.println("      void guardar(String dato);");
            System.out.println("  }");
            return;
        } else if (pista == 2) {
            System.out.println("\n💡 Pista 2: Implementaciones concretas:");
            System.out.println("  class BaseDatosMySQL implements BaseDatos {");
            System.out.println("      public void guardar(String dato) { System.out.println(\"MySQL: \" + dato); }");
            System.out.println("  }");
            System.out.println("  class BaseDatosArchivo implements BaseDatos {");
            System.out.println("      public void guardar(String dato) { System.out.println(\"Archivo: \" + dato); }");
            System.out.println("  }");
            return;
        } else if (pista == 3) {
            System.out.println("\n💡 Pista 3: Servicio con inyeccion de dependencia:");
            System.out.println("  class Servicio {");
            System.out.println("      private BaseDatos db;");
            System.out.println("      Servicio(BaseDatos db) { this.db = db; }");
            System.out.println("      void procesar(String dato) { db.guardar(dato); }");
            System.out.println("  }");
            System.out.println("  // Main:");
            System.out.println("  Servicio s1 = new Servicio(new BaseDatosMySQL());");
            System.out.println("  s1.procesar(\"datos\");");
            System.out.println("  Servicio s2 = new Servicio(new BaseDatosArchivo());");
            System.out.println("  s2.procesar(\"datos\");");
            return;
        }

        System.out.println("\nCrea las siguientes clases en un archivo Main.java:");
        System.out.println();
        System.out.println("1. Interface BaseDatos con metodo guardar(String)");
        System.out.println("2. BaseDatosMySQL que implemente BaseDatos");
        System.out.println("3. BaseDatosArchivo que implemente BaseDatos");
        System.out.println("4. Servicio que reciba BaseDatos por constructor (DIP!)");
        System.out.println("5. En el main, prueba con ambas implementaciones");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }
}
