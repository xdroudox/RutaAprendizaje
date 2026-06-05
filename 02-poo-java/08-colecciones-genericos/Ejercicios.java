/**
 * EJERCICIOS - Colecciones y Genericos
 * Ejecuta desde raiz: python scripts/runner.py 2 8 [ejercicio]
 */
import java.util.ArrayList;
import java.util.HashMap;

public class Ejercicios {

    public static void main(String[] args) {
        if (args.length > 0) {
            int num = Integer.parseInt(args[0]);
            switch (num) {
                case 1: ejercicio_1(); break;
                case 2: ejercicio_2(); break;
                case 3: ejercicio_3(); break;
                default: System.out.println("Ejercicio no encontrado");
            }
        } else {
            System.out.println("EJERCICIOS:");
            System.out.println("1. ArrayList<String> de nombres");
            System.out.println("2. HashMap<String, Integer> para agenda telefonica");
            System.out.println("3. Clase generica Caja<T> que guarde cualquier tipo");
        }
    }

    static void ejercicio_1() {
        System.out.println(">> EJERCICIO 1: ArrayList de nombres");
        System.out.println("-".repeat(40));
        System.out.println("Crea un ArrayList<String> de nombres.");
        System.out.println("Agrega 4 nombres con add().");
        System.out.println("Muestra todos los nombres con un bucle for-each.");
        System.out.println("Muestra el tamaño con size().");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    static void ejercicio_2() {
        System.out.println(">> EJERCICIO 2: HashMap agenda telefonica");
        System.out.println("-".repeat(40));
        System.out.println("Crea un HashMap<String, Integer> para una agenda telefonica.");
        System.out.println("Agrega 3 contactos (nombre -> telefono).");
        System.out.println("Muestra el telefono de un contacto especifico con get().");
        System.out.println("Recorre el mapa mostrando todos los contactos.");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    static void ejercicio_3() {
        System.out.println(">> EJERCICIO 3: Clase generica Caja<T>");
        System.out.println("-".repeat(40));
        System.out.println("Crea una clase generica Caja<T> que pueda guardar cualquier tipo.");
        System.out.println("Incluye:");
        System.out.println("  - Atributo privado T contenido");
        System.out.println("  - Metodo guardar(T contenido)");
        System.out.println("  - Metodo T obtener()");
        System.out.println("En el main, crea una Caja<String> y una Caja<Integer> y usalas.");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }
}
