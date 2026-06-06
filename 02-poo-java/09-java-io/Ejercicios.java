/**
 * EJERCICIOS - Java I/O (Java)
 * Ejecuta desde raiz: python scripts/runner.py 2 9 [ejercicio]
 *
 * Niveles:
 *   🟢 Ej 1: Escribir archivo con FileWriter
 *   🟡 Ej 2: Leer archivo con BufferedReader
 *   🔴 Ej 3: Copiar archivo caracter por caracter
 *
 * Pistas: python scripts/runner.py 2 9 N -p [1|2|3]
 */
import java.io.*;

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
            System.out.println("  🟢 1. Escribir archivo con FileWriter");
            System.out.println("  🟡 2. Leer archivo con BufferedReader");
            System.out.println("  🔴 3. Copiar archivo caracter por caracter");
            System.out.println();
            System.out.println("Ejecuta: python scripts/runner.py 2 9 [N]");
            System.out.println("Pistas:  python scripts/runner.py 2 9 N -p [1|2|3]");
        }
    }

    // -----------------------------------------------------------------------
    // 🟢 EJERCICIO 1: Escribir archivo
    // -----------------------------------------------------------------------

    static void ejercicio_1(int pista) {
        System.out.println(">> 🟢 EJERCICIO 1: Escribir archivo con FileWriter");
        System.out.println("-".repeat(50));

        if (pista == 1) {
            System.out.println("\n💡 Pista 1: Usa FileWriter con try-with-resources:");
            System.out.println("  try (FileWriter fw = new FileWriter(\"salida.txt\")) {");
            System.out.println("      fw.write(\"Hola mundo\");");
            System.out.println("      System.out.println(\"Archivo escrito correctamente\");");
            System.out.println("  } catch (IOException e) {");
            System.out.println("      System.out.println(\"Error: \" + e.getMessage());");
            System.out.println("  }");
            return;
        } else if (pista == 2) {
            System.out.println("\n💡 Pista 2: FileWriter sin segundo argumento SOBRESCRIBE.");
            return;
        } else if (pista == 3) {
            System.out.println("\n💡 Pista 3: Necesitas estos imports:");
            System.out.println("  import java.io.FileWriter;");
            System.out.println("  import java.io.IOException;");
            return;
        }

        System.out.println("\nCrea el codigo en un archivo Main.java:");
        System.out.println();
        System.out.println("1. Importa FileWriter e IOException");
        System.out.println("2. try-with-resources: escribe \"Hola mundo\" en salida.txt");
        System.out.println("3. Captura IOException y muestra el error");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    // -----------------------------------------------------------------------
    // 🟡 EJERCICIO 2: Leer archivo
    // -----------------------------------------------------------------------

    static void ejercicio_2(int pista) {
        System.out.println(">> 🟡 EJERCICIO 2: Leer archivo con BufferedReader");
        System.out.println("-".repeat(50));

        if (pista == 1) {
            System.out.println("\n💡 Pista 1: BufferedReader + FileReader:");
            System.out.println("  try (BufferedReader br = new BufferedReader(new FileReader(\"salida.txt\"))) {");
            System.out.println("      String linea;");
            System.out.println("      while ((linea = br.readLine()) != null) {");
            System.out.println("          System.out.println(linea);");
            System.out.println("      }");
            System.out.println("  } catch (IOException e) {");
            System.out.println("      System.out.println(\"Error: \" + e.getMessage());");
            System.out.println("  }");
            return;
        } else if (pista == 2) {
            System.out.println("\n💡 Pista 2: readLine() devuelve null al final del archivo.");
            return;
        } else if (pista == 3) {
            System.out.println("\n💡 Pista 3: Necesitas estos imports:");
            System.out.println("  import java.io.BufferedReader;");
            System.out.println("  import java.io.FileReader;");
            System.out.println("  import java.io.IOException;");
            return;
        }

        System.out.println("\nCrea el codigo en un archivo Main.java:");
        System.out.println();
        System.out.println("1. Importa BufferedReader, FileReader, IOException");
        System.out.println("2. Lee salida.txt linea por linea con readLine()");
        System.out.println("3. Muestra cada linea");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    // -----------------------------------------------------------------------
    // 🔴 EJERCICIO 3: Copiar archivo
    // -----------------------------------------------------------------------

    static void ejercicio_3(int pista) {
        System.out.println(">> 🔴 EJERCICIO 3: Copiar archivo");
        System.out.println("-".repeat(50));

        if (pista == 1) {
            System.out.println("\n💡 Pista 1: Dos recursos en el try:");
            System.out.println("  try (FileReader fr = new FileReader(\"origen.txt\");");
            System.out.println("       FileWriter fw = new FileWriter(\"destino.txt\")) {");
            System.out.println("      int c;");
            System.out.println("      while ((c = fr.read()) != -1) {");
            System.out.println("          fw.write(c);");
            System.out.println("      }");
            System.out.println("      System.out.println(\"Archivo copiado correctamente\");");
            System.out.println("  } catch (IOException e) {");
            System.out.println("      System.out.println(\"Error: \" + e.getMessage());");
            System.out.println("  }");
            return;
        } else if (pista == 2) {
            System.out.println("\n💡 Pista 2: read() devuelve -1 al final del archivo.");
            System.out.println("  Usa int (no char) porque -1 no es un caracter valido.");
            return;
        } else if (pista == 3) {
            System.out.println("\n💡 Pista 3: Necesitas estos imports:");
            System.out.println("  import java.io.FileReader;");
            System.out.println("  import java.io.FileWriter;");
            System.out.println("  import java.io.IOException;");
            return;
        }

        System.out.println("\nCrea el codigo en un archivo Main.java:");
        System.out.println();
        System.out.println("1. Dos recursos: FileReader y FileWriter en el try");
        System.out.println("2. Lee caracter por caracter con read()");
        System.out.println("3. Escribe cada caracter con write()");
        System.out.println("4. -1 = fin de archivo");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }
}
