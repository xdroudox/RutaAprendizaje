/**
 * EJERCICIOS - Excepciones (Java)
 * Ejecuta desde raiz: python scripts/runner.py 2 7 [ejercicio]
 *
 * Niveles:
 *   🟢 Ej 1: Division con try/catch (ArithmeticException)
 *   🟡 Ej 2: NumberFormatException con Integer.parseInt()
 *   🔴 Ej 3: Excepcion personalizada EdadInvalidaException
 *
 * Pistas: python scripts/runner.py 2 7 N -p [1|2|3]
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
            System.out.println("  🟢 1. Division con try/catch");
            System.out.println("  🟡 2. NumberFormatException");
            System.out.println("  🔴 3. Excepcion personalizada");
            System.out.println();
            System.out.println("Ejecuta: python scripts/runner.py 2 7 [N]");
            System.out.println("Pistas:  python scripts/runner.py 2 7 N -p [1|2|3]");
        }
    }

    // -----------------------------------------------------------------------
    // 🟢 EJERCICIO 1: Division con try/catch
    // -----------------------------------------------------------------------

    static void ejercicio_1(int pista) {
        System.out.println(">> 🟢 EJERCICIO 1: Division con try/catch");
        System.out.println("-".repeat(50));

        if (pista == 1) {
            System.out.println("\n💡 Pista 1: Divide dos enteros dentro de un try:");
            System.out.println("  int a = 10, b = 0;");
            System.out.println("  try {");
            System.out.println("      int resultado = a / b;");
            System.out.println("      System.out.println(\"Resultado: \" + resultado);");
            System.out.println("  } catch (ArithmeticException e) {");
            System.out.println("      System.out.println(\"Error: No se puede dividir por cero\");");
            System.out.println("  }");
            return;
        } else if (pista == 2) {
            System.out.println("\n💡 Pista 2: Usa ArithmeticException en el catch.");
            System.out.println("  Es la excepcion que Java lanza cuando divides por cero.");
            System.out.println("  Si usas Exception (la general), tambien funciona, pero");
            System.out.println("  es mejor usar la mas especifica.");
            return;
        } else if (pista == 3) {
            System.out.println("\n💡 Pista 3: Prueba ambos casos:");
            System.out.println("  System.out.println(dividir(10, 2));  // 5");
            System.out.println("  System.out.println(dividir(10, 0));  // Error");
            return;
        }

        System.out.println("\nCrea el codigo en un archivo Main.java:");
        System.out.println();
        System.out.println("1. Divide dos enteros (10 / 0 para provocar error)");
        System.out.println("2. Envuelve en try/catch con ArithmeticException");
        System.out.println("3. Muestra un mensaje de error en el catch");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    // -----------------------------------------------------------------------
    // 🟡 EJERCICIO 2: NumberFormatException
    // -----------------------------------------------------------------------

    static void ejercicio_2(int pista) {
        System.out.println(">> 🟡 EJERCICIO 2: NumberFormatException");
        System.out.println("-".repeat(50));

        if (pista == 1) {
            System.out.println("\n💡 Pista 1: Usa Integer.parseInt() dentro de try:");
            System.out.println("  String numero = \"abc\";");
            System.out.println("  try {");
            System.out.println("      int valor = Integer.parseInt(numero);");
            System.out.println("      System.out.println(\"Numero: \" + valor);");
            System.out.println("  } catch (NumberFormatException e) {");
            System.out.println("      System.out.println(\"Error: formato invalido\");");
            System.out.println("  }");
            return;
        } else if (pista == 2) {
            System.out.println("\n💡 Pista 2: Integer.parseInt() convierte String a int.");
            System.out.println("  Lance NumberFormatException si el String no es un numero.");
            System.out.println("  \"123\" -> 123.  \"abc\" -> NumberFormatException.");
            return;
        } else if (pista == 3) {
            System.out.println("\n💡 Pista 3: Prueba ambos casos:");
            System.out.println("  String valido = \"123\";");
            System.out.println("  String invalido = \"abc\";");
            return;
        }

        System.out.println("\nCrea el codigo en un archivo Main.java:");
        System.out.println();
        System.out.println("1. Define un String con valor \"abc\"");
        System.out.println("2. Intenta convertirlo con Integer.parseInt()");
        System.out.println("3. Captura NumberFormatException");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    // -----------------------------------------------------------------------
    // 🔴 EJERCICIO 3: Excepcion personalizada
    // -----------------------------------------------------------------------

    static void ejercicio_3(int pista) {
        System.out.println(">> 🔴 EJERCICIO 3: Excepcion personalizada");
        System.out.println("-".repeat(50));

        if (pista == 1) {
            System.out.println("\n💡 Pista 1: Define la excepcion personalizada:");
            System.out.println("  class EdadInvalidaException extends Exception {");
            System.out.println("      EdadInvalidaException(String mensaje) {");
            System.out.println("          super(mensaje);");
            System.out.println("      }");
            System.out.println("  }");
            return;
        } else if (pista == 2) {
            System.out.println("\n💡 Pista 2: Metodo validarEdad:");
            System.out.println("  static void validarEdad(int edad) throws EdadInvalidaException {");
            System.out.println("      if (edad <= 0 || edad > 150) {");
            System.out.println("          throw new EdadInvalidaException(\"Edad \" + edad + \" no valida\");");
            System.out.println("      }");
            System.out.println("      System.out.println(\"Edad valida: \" + edad);");
            System.out.println("  }");
            return;
        } else if (pista == 3) {
            System.out.println("\n💡 Pista 3: En el main:");
            System.out.println("  try { validarEdad(25); } catch (EdadInvalidaException e) {");
            System.out.println("      System.out.println(e.getMessage());");
            System.out.println("  }");
            System.out.println("  try { validarEdad(-5); } catch (EdadInvalidaException e) {");
            System.out.println("      System.out.println(e.getMessage());");
            System.out.println("  }");
            return;
        }

        System.out.println("\nCrea el codigo en un archivo Main.java:");
        System.out.println();
        System.out.println("1. Clase EdadInvalidaException extends Exception");
        System.out.println("2. Metodo validarEdad(int) que la lance si es invalida");
        System.out.println("3. En el main, prueba con 25 y -5");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }
}
