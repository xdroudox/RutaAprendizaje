/**
 * SOLUCIONES - Colecciones y Genericos
 * Ejecuta: python scripts/runner.py 2 8 [ejercicio] -s
 */
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Soluciones {

    public static void main(String[] args) {
        if (args.length > 0) {
            int num = Integer.parseInt(args[0]);
            switch (num) {
                case 1: solucion_1(); break;
                case 2: solucion_2(); break;
                case 3: solucion_3(); break;
                default: System.out.println("Solucion no encontrada");
            }
        } else {
            System.out.println("Soluciones disponibles: 1, 2, 3");
        }
    }

    static void solucion_1() {
        System.out.println("=== SOLUCION 1: ArrayList de nombres ===");
        System.out.println("ArrayList<String> nombres = new ArrayList<>();");
        System.out.println("nombres.add(\"Ana\");");
        System.out.println("nombres.add(\"Luis\");");
        System.out.println("nombres.add(\"Carlos\");");
        System.out.println("nombres.add(\"Marta\");");
        System.out.println();
        System.out.println("System.out.println(\"Total: \" + nombres.size());");
        System.out.println("for (String n : nombres) {");
        System.out.println("    System.out.println(n);");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: ArrayList es una coleccion que permite elementos duplicados.");
    }

    static void solucion_2() {
        System.out.println("=== SOLUCION 2: HashMap agenda telefonica ===");
        System.out.println("HashMap<String, Integer> agenda = new HashMap<>();");
        System.out.println("agenda.put(\"Ana\", 123456789);");
        System.out.println("agenda.put(\"Luis\", 987654321);");
        System.out.println("agenda.put(\"Marta\", 555123456);");
        System.out.println();
        System.out.println("System.out.println(\"Telefono de Ana: \" + agenda.get(\"Ana\"));");
        System.out.println();
        System.out.println("for (Map.Entry<String, Integer> e : agenda.entrySet()) {");
        System.out.println("    System.out.println(e.getKey() + \": \" + e.getValue());");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: HashMap almacena pares clave-valor. Las claves son unicas.");
    }

    static void solucion_3() {
        System.out.println("=== SOLUCION 3: Clase generica Caja<T> ===");
        System.out.println("class Caja<T> {");
        System.out.println("    private T contenido;");
        System.out.println();
        System.out.println("    public void guardar(T contenido) {");
        System.out.println("        this.contenido = contenido;");
        System.out.println("    }");
        System.out.println();
        System.out.println("    public T obtener() {");
        System.out.println("        return contenido;");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("// En el main:");
        System.out.println("Caja<String> cajaString = new Caja<>();");
        System.out.println("cajaString.guardar(\"Hola\");");
        System.out.println("System.out.println(cajaString.obtener());");
        System.out.println();
        System.out.println("Caja<Integer> cajaInt = new Caja<>();");
        System.out.println("cajaInt.guardar(42);");
        System.out.println("System.out.println(cajaInt.obtener());");
        System.out.println();
        System.out.println("Explicacion: <T> es un parametro de tipo. La clase funciona con cualquier tipo.");
    }
}
