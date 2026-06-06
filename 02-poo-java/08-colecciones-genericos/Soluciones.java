/**
 * SOLUCIONES - Colecciones y Genericos (Java)
 * Ejecuta desde raiz: python scripts/runner.py 2 8 [ejercicio] -s
 */
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Soluciones {

    public static void main(String[] args) {
        if (args.length > 0 && !args[0].startsWith("-")) {
            int num;
            try {
                num = Integer.parseInt(args[0]);
            } catch (NumberFormatException e) {
                System.out.println("Solucion no encontrada");
                return;
            }
            switch (num) {
                case 1: solucion_1(); break;
                case 2: solucion_2(); break;
                case 3: solucion_3(); break;
                default: System.out.println("Ejercicio no encontrado. Valores: 1-3");
            }
        } else {
            System.out.println("SOLUCIONES:");
            System.out.println("  🟢 1. ArrayList de nombres");
            System.out.println("  🟡 2. HashMap agenda telefonica");
            System.out.println("  🔴 3. Clase generica Caja<T>");
        }
    }

    static void solucion_1() {
        System.out.println("=".repeat(50));
        System.out.println("🟢 SOLUCION 1: ArrayList de nombres");
        System.out.println("=".repeat(50));
        System.out.println();

        System.out.println("--- CODIGO (Main.java) ---");
        System.out.println("""
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> nombres = new ArrayList<>();

        nombres.add("Ana");
        nombres.add("Luis");
        nombres.add("Carlos");
        nombres.add("Marta");

        System.out.println("Total de nombres: " + nombres.size());

        for (String n : nombres) {
            System.out.println(n);
        }
    }
}
""");

        System.out.println("--- EXPLICACION ---");
        System.out.println("""
1. `ArrayList<String> nombres = new ArrayList<>();` — Crea una lista
   vacia de Strings. El diamante `<>` infiere el tipo de la izquierda.

2. `nombres.add("Ana")` — Agrega al FINAL de la lista. La lista crece
   automaticamente. Sin limite fijo.

3. `nombres.size()` — Devuelve la cantidad de elementos (4).
   NO confundir con `length` de arrays.

4. `for (String n : nombres)` — For-each: recorre CADA elemento de la
   coleccion. No necesitas indice.

5. `get(0)` devuelve "Ana", `get(1)` devuelve "Luis", etc.
""");
    }

    static void solucion_2() {
        System.out.println("=".repeat(50));
        System.out.println("🟡 SOLUCION 2: HashMap agenda telefonica");
        System.out.println("=".repeat(50));
        System.out.println();

        System.out.println("--- CODIGO (Main.java) ---");
        System.out.println("""
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        HashMap<String, Integer> agenda = new HashMap<>();

        agenda.put("Ana", 123456789);
        agenda.put("Luis", 987654321);
        agenda.put("Marta", 555123456);

        System.out.println("Telefono de Ana: " + agenda.get("Ana"));

        for (Map.Entry<String, Integer> e : agenda.entrySet()) {
            System.out.println(e.getKey() + ": " + e.getValue());
        }
    }
}
""");

        System.out.println("--- EXPLICACION ---");
        System.out.println("""
1. `HashMap<String, Integer>` — Clave = String (nombre), Valor = Integer (telefono).
   Cada clave es UNICA. Si repites clave, se sobrescribe.

2. `put("Ana", 123456789)` — Agrega el par clave-valor.

3. `get("Ana")` — Busca por clave y devuelve el valor. Si la clave no
   existe, devuelve null.

4. `entrySet()` — Devuelve un conjunto de TODAS las entradas.
   Cada entrada es un Map.Entry con getKey() y getValue().

5. `e.getKey()` devuelve "Ana", e.getValue() devuelve 123456789.
   El orden NO esta garantizado (HashMap no ordena).
""");
    }

    static void solucion_3() {
        System.out.println("=".repeat(50));
        System.out.println("🔴 SOLUCION 3: Clase generica Caja<T>");
        System.out.println("=".repeat(50));
        System.out.println();

        System.out.println("--- CODIGO (Main.java) ---");
        System.out.println("""
class Caja<T> {
    private T contenido;

    public void guardar(T contenido) {
        this.contenido = contenido;
    }

    public T obtener() {
        return contenido;
    }
}

public class Main {
    public static void main(String[] args) {
        Caja<String> cajaStr = new Caja<>();
        cajaStr.guardar("Hola");
        String texto = cajaStr.obtener();
        System.out.println(texto);

        Caja<Integer> cajaInt = new Caja<>();
        cajaInt.guardar(42);
        int numero = cajaInt.obtener();
        System.out.println(numero);
    }
}
""");

        System.out.println("--- EXPLICACION ---");
        System.out.println("""
1. `class Caja<T>` — T es un PARAMETRO DE TIPO. Al crear una Caja,
   defines que tipo va a guardar.

2. `Caja<String>` — T = String. El compilador TRATA a Caja como si
   T fuera String. `guardar(String)`, `obtener() -> String`.

3. `Caja<Integer>` — T = Integer. `guardar(Integer)`, `obtener() -> Integer`.

4. SIN genericos, tendriamos que hacer casting:
   `String texto = (String) caja.obtener();` y arriesgarnos a errores
   en ejecucion. CON genericos, el compilador verifica los tipos.

5. `Integer` es la clase wrapper de `int`. El autoboxing convierte
   automaticamente: `cajaInt.guardar(42)` funciona aunque 42 es un int.
""");
    }
}
