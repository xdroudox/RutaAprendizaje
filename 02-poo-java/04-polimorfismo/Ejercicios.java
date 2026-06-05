/**
 * EJERCICIOS - Polimorfismo
 * Ejecuta desde raiz: python scripts/runner.py 2 4 [ejercicio]
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
            System.out.println("1. Sobrecarga: metodo sumar() con 2 y 3 parametros");
            System.out.println("2. Array polimorfico de Animal llamando a hacerSonido()");
            System.out.println("3. Clase Figura con area(), Circulo y Rectangulo");
        }
    }

    static void ejercicio_1() {
        System.out.println(">> EJERCICIO 1: Sobrecarga de sumar()");
        System.out.println("-".repeat(40));
        System.out.println("Crea una clase Calculadora con dos metodos sumar:");
        System.out.println("  - sumar(int a, int b) que retorne a + b");
        System.out.println("  - sumar(int a, int b, int c) que retorne a + b + c");
        System.out.println("En el main, crea una Calculadora y prueba ambos metodos.");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    static void ejercicio_2() {
        System.out.println(">> EJERCICIO 2: Array polimorfico de Animales");
        System.out.println("-".repeat(40));
        System.out.println("Usando las clases Animal, Perro y Gato del modulo de herencia:");
        System.out.println("Crea un array de tipo Animal[] con un Perro y un Gato.");
        System.out.println("Recorre el array con un bucle for llamando a hacerSonido().");
        System.out.println("Cada animal ejecutara su propia version del metodo.");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    static void ejercicio_3() {
        System.out.println(">> EJERCICIO 3: Figura, Circulo y Rectangulo");
        System.out.println("-".repeat(40));
        System.out.println("Crea una clase Figura con metodo area() que retorne 0.0.");
        System.out.println("Crea Circulo que herede de Figura, con atributo radio,");
        System.out.println("y area() retorne Math.PI * radio * radio.");
        System.out.println("Crea Rectangulo que herede de Figura, con base y altura,");
        System.out.println("y area() retorne base * altura.");
        System.out.println("En el main, crea un array de Figura[] con un circulo y un");
        System.out.println("rectangulo, y muestra el area de cada uno.");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }
}
