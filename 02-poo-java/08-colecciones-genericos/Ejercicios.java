/**
 * EJERCICIOS - Colecciones y Genericos (Java)
 * Ejecuta desde raiz: python scripts/runner.py 2 8 [ejercicio]
 *
 * Niveles:
 *   🟢 Ej 1: ArrayList<String> de nombres
 *   🟡 Ej 2: HashMap<String, Integer> agenda telefonica
 *   🔴 Ej 3: Clase generica Caja<T>
 *
 * Pistas: python scripts/runner.py 2 8 N -p [1|2|3]
 */
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

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
            System.out.println("  🟢 1. ArrayList de nombres");
            System.out.println("  🟡 2. HashMap agenda telefonica");
            System.out.println("  🔴 3. Clase generica Caja<T>");
            System.out.println();
            System.out.println("Ejecuta: python scripts/runner.py 2 8 [N]");
            System.out.println("Pistas:  python scripts/runner.py 2 8 N -p [1|2|3]");
        }
    }

    // -----------------------------------------------------------------------
    // 🟢 EJERCICIO 1: ArrayList de nombres
    // -----------------------------------------------------------------------

    static void ejercicio_1(int pista) {
        System.out.println(">> 🟢 EJERCICIO 1: ArrayList de nombres");
        System.out.println("-".repeat(50));

        if (pista == 1) {
            System.out.println("\n💡 Pista 1: Importa y crea el ArrayList:");
            System.out.println("  import java.util.ArrayList;");
            System.out.println("  ArrayList<String> nombres = new ArrayList<>();");
            return;
        } else if (pista == 2) {
            System.out.println("\n💡 Pista 2: Agrega elementos y muestra:");
            System.out.println("  nombres.add(\"Ana\");");
            System.out.println("  nombres.add(\"Luis\");");
            System.out.println("  // ... agrega 4 en total");
            System.out.println("  System.out.println(\"Total: \" + nombres.size());");
            return;
        } else if (pista == 3) {
            System.out.println("\n💡 Pista 3: Recorre con for-each:");
            System.out.println("  for (String n : nombres) {");
            System.out.println("      System.out.println(n);");
            System.out.println("  }");
            return;
        }

        System.out.println("\nCrea el codigo en un archivo Main.java:");
        System.out.println();
        System.out.println("1. Crea un ArrayList<String> de nombres");
        System.out.println("2. Agrega 4 nombres con add()");
        System.out.println("3. Muestra el tamaño con size()");
        System.out.println("4. Recorre con for-each mostrando cada nombre");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    // -----------------------------------------------------------------------
    // 🟡 EJERCICIO 2: HashMap agenda telefonica
    // -----------------------------------------------------------------------

    static void ejercicio_2(int pista) {
        System.out.println(">> 🟡 EJERCICIO 2: HashMap agenda telefonica");
        System.out.println("-".repeat(50));

        if (pista == 1) {
            System.out.println("\n💡 Pista 1: Importa y crea el HashMap:");
            System.out.println("  import java.util.HashMap;");
            System.out.println("  import java.util.Map;");
            System.out.println("  HashMap<String, Integer> agenda = new HashMap<>();");
            return;
        } else if (pista == 2) {
            System.out.println("\n💡 Pista 2: Agrega contactos:");
            System.out.println("  agenda.put(\"Ana\", 123456789);");
            System.out.println("  agenda.put(\"Luis\", 987654321);");
            System.out.println("  agenda.put(\"Marta\", 555123456);");
            System.out.println("  System.out.println(\"Telefono de Ana: \" + agenda.get(\"Ana\"));");
            return;
        } else if (pista == 3) {
            System.out.println("\n💡 Pista 3: Recorre el mapa:");
            System.out.println("  for (Map.Entry<String, Integer> e : agenda.entrySet()) {");
            System.out.println("      System.out.println(e.getKey() + \": \" + e.getValue());");
            System.out.println("  }");
            return;
        }

        System.out.println("\nCrea el codigo en un archivo Main.java:");
        System.out.println();
        System.out.println("1. Crea un HashMap<String, Integer>");
        System.out.println("2. Agrega 3 contactos con put()");
        System.out.println("3. Muestra telefono de un contacto con get()");
        System.out.println("4. Recorre con entrySet() mostrando todos");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    // -----------------------------------------------------------------------
    // 🔴 EJERCICIO 3: Clase generica Caja<T>
    // -----------------------------------------------------------------------

    static void ejercicio_3(int pista) {
        System.out.println(">> 🔴 EJERCICIO 3: Clase generica Caja<T>");
        System.out.println("-".repeat(50));

        if (pista == 1) {
            System.out.println("\n💡 Pista 1: Define la clase generica:");
            System.out.println("  class Caja<T> {");
            System.out.println("      private T contenido;");
            System.out.println("      public void guardar(T contenido) { this.contenido = contenido; }");
            System.out.println("      public T obtener() { return contenido; }");
            System.out.println("  }");
            return;
        } else if (pista == 2) {
            System.out.println("\n💡 Pista 2: T es un placeholder. Al usarlo, se define:");
            System.out.println("  Caja<String> cs = new Caja<>();  // T = String");
            System.out.println("  Caja<Integer> ci = new Caja<>();  // T = Integer");
            return;
        } else if (pista == 3) {
            System.out.println("\n💡 Pista 3: En el main:");
            System.out.println("  Caja<String> cajaStr = new Caja<>();");
            System.out.println("  cajaStr.guardar(\"Hola\");");
            System.out.println("  String texto = cajaStr.obtener();  // Sin casting!");
            System.out.println("  System.out.println(texto);");
            System.out.println();
            System.out.println("  Caja<Integer> cajaInt = new Caja<>();");
            System.out.println("  cajaInt.guardar(42);");
            System.out.println("  int num = cajaInt.obtener();  // Sin casting!");
            System.out.println("  System.out.println(num);");
            return;
        }

        System.out.println("\nCrea el codigo en un archivo Main.java:");
        System.out.println();
        System.out.println("1. Clase generica Caja<T> con guardar() y obtener()");
        System.out.println("2. En el main, Caja<String> con texto");
        System.out.println("3. Caja<Integer> con numero entero");
        System.out.println("4. Muestra los valores (sin casting!)");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }
}
