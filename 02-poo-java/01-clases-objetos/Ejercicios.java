/**
 * EJERCICIOS - Clases y Objetos
 * Ejecuta desde raiz: python scripts/runner.py 2 1 [ejercicio]
 */
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
            System.out.println("1. Crear clase Persona con mostrarDatos()");
            System.out.println("2. Crear clase Rectangulo con area()");
            System.out.println("3. Crear clase Libro con esLargo()");
        }
    }

    static void ejercicio_1() {
        System.out.println(">> EJERCICIO 1: Clase Persona");
        System.out.println("-".repeat(40));
        System.out.println("Crea una clase Persona con atributos nombre (String) y edad (int).");
        System.out.println("Incluye un constructor que inicialice ambos atributos usando this.");
        System.out.println("Incluye un metodo mostrarDatos() que imprima nombre y edad.");
        System.out.println("En el main, crea dos personas y llama a mostrarDatos().");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    static void ejercicio_2() {
        System.out.println(">> EJERCICIO 2: Clase Rectangulo");
        System.out.println("-".repeat(40));
        System.out.println("Crea una clase Rectangulo con atributos base (double) y altura (double).");
        System.out.println("Incluye un constructor con parametros.");
        System.out.println("Incluye un metodo area() que retorne base * altura.");
        System.out.println("En el main, crea un rectangulo de 5x3 e imprime su area.");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    static void ejercicio_3() {
        System.out.println(">> EJERCICIO 3: Clase Libro");
        System.out.println("-".repeat(40));
        System.out.println("Crea una clase Libro con atributos titulo (String), autor (String) y");
        System.out.println("paginas (int). Incluye constructor y metodo esLargo() que retorne");
        System.out.println("true si el libro tiene mas de 300 paginas.");
        System.out.println("En el main, crea dos libros y muestra si son largos.");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }
}
