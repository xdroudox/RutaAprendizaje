/**
 * EJERCICIOS - Excepciones
 * Ejecuta desde raiz: python scripts/runner.py 2 7 [ejercicio]
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
            System.out.println("1. Division con try/catch para ArithmeticException");
            System.out.println("2. NumberFormatException al convertir string a int");
            System.out.println("3. Excepcion personalizada EdadInvalidaException");
        }
    }

    static void ejercicio_1() {
        System.out.println(">> EJERCICIO 1: Division con try/catch");
        System.out.println("-".repeat(40));
        System.out.println("Escribe un programa que divida dos numeros enteros.");
        System.out.println("Usa try/catch para capturar ArithmeticException si se divide por cero.");
        System.out.println("En el catch, imprime \"Error: No se puede dividir por cero\".");
        System.out.println("Prueba con 10 / 2 y con 10 / 0.");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    static void ejercicio_2() {
        System.out.println(">> EJERCICIO 2: NumberFormatException");
        System.out.println("-".repeat(40));
        System.out.println("Pide al usuario que introduzca un numero entero (usa un String fijo).");
        System.out.println("Intenta convertir el String a int con Integer.parseInt().");
        System.out.println("Captura NumberFormatException si la conversion falla.");
        System.out.println("Prueba con \"123\" (valido) y con \"abc\" (invalido).");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    static void ejercicio_3() {
        System.out.println(">> EJERCICIO 3: Excepcion personalizada");
        System.out.println("-".repeat(40));
        System.out.println("Crea una clase EdadInvalidaException que extienda Exception.");
        System.out.println("Crea un metodo validarEdad(int edad) que lance EdadInvalidaException");
        System.out.println("si la edad es menor o igual a 0 o mayor a 150.");
        System.out.println("En el main, llama a validarEdad con diferentes valores y captura la excepcion.");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }
}
