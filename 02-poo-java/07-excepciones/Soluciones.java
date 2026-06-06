/**
 * SOLUCIONES - Excepciones (Java)
 * Ejecuta desde raiz: python scripts/runner.py 2 7 [ejercicio] -s
 */
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
            System.out.println("  🟢 1. Division con try/catch");
            System.out.println("  🟡 2. NumberFormatException");
            System.out.println("  🔴 3. Excepcion personalizada");
        }
    }

    static void solucion_1() {
        System.out.println("=".repeat(50));
        System.out.println("🟢 SOLUCION 1: Division con try/catch");
        System.out.println("=".repeat(50));
        System.out.println();

        System.out.println("--- CODIGO (Main.java) ---");
        System.out.println("""
public class Main {
    public static void main(String[] args) {
        int a = 10, b = 0;

        try {
            int resultado = a / b;
            System.out.println("Resultado: " + resultado);
        } catch (ArithmeticException e) {
            System.out.println("Error: No se puede dividir por cero");
        }

        System.out.println("El programa continua...");
    }
}
""");

        System.out.println("--- EXPLICACION ---");
        System.out.println("""
1. `int resultado = a / b` — Cuando b=0, Java lanza ArithmeticException.
   La linea NO se ejecuta, el flujo salta al catch.

2. `catch (ArithmeticException e)` — Captura la excepcion. El bloque
   catch contiene el codigo para manejar el error.

3. `"El programa continua..."` — Se ejecuta DESPUES del try/catch.
   SIN try/catch, el programa habria terminado en la division por cero.

4. `e.getMessage()` devolveria "/ by zero". Podriamos usarlo en vez
   de nuestro mensaje personalizado si quisieramos.
""");
    }

    static void solucion_2() {
        System.out.println("=".repeat(50));
        System.out.println("🟡 SOLUCION 2: NumberFormatException");
        System.out.println("=".repeat(50));
        System.out.println();

        System.out.println("--- CODIGO (Main.java) ---");
        System.out.println("""
public class Main {
    public static void main(String[] args) {
        String numero = "abc";

        try {
            int valor = Integer.parseInt(numero);
            System.out.println("Numero: " + valor);
        } catch (NumberFormatException e) {
            System.out.println("Error: '" + numero + "' no es un numero valido");
        }
    }
}
""");

        System.out.println("--- EXPLICACION ---");
        System.out.println("""
1. `Integer.parseInt("abc")` — Intenta convertir "abc" a entero.
   Como "abc" no es un numero, lanza NumberFormatException.

2. `catch (NumberFormatException e)` — Captura especificamente errores
   de conversion numerica.

3. Podriamos usar `e.getMessage()` para obtener el mensaje original:
   \"For input string: \\\"abc\\\"\"

4. `Integer.parseInt("123")` funcionaria bien y devolveria 123.
   Siempre que trabajes con entrada del usuario, usa try/catch para
   evitar que el programa termine por una entrada incorrecta.
""");
    }

    static void solucion_3() {
        System.out.println("=".repeat(50));
        System.out.println("🔴 SOLUCION 3: Excepcion personalizada");
        System.out.println("=".repeat(50));
        System.out.println();

        System.out.println("--- CODIGO (Main.java) ---");
        System.out.println("""
class EdadInvalidaException extends Exception {
    EdadInvalidaException(String mensaje) {
        super(mensaje);
    }
}

public class Main {

    static void validarEdad(int edad) throws EdadInvalidaException {
        if (edad <= 0 || edad > 150) {
            throw new EdadInvalidaException("Edad " + edad + " no es valida");
        }
        System.out.println("Edad valida: " + edad);
    }

    public static void main(String[] args) {
        try {
            validarEdad(25);
            validarEdad(-5);
        } catch (EdadInvalidaException e) {
            System.out.println(e.getMessage());
        }
    }
}
""");

        System.out.println("--- EXPLICACION ---");
        System.out.println("""
1. `class EdadInvalidaException extends Exception` — Creamos nuestra
   PROPIA excepcion. Al extender Exception, es una CHECKED exception:
   el compilador obliga a manejarla con try/catch o declarar throws.

2. `super(mensaje)` — Llama al constructor de Exception que guarda el
   mensaje. Luego podemos recuperarlo con getMessage().

3. `throw new EdadInvalidaException(...)` — Lanzamos la excepcion
   cuando la edad no es valida. `new` crea el objeto, `throw` lo lanza.

4. `throws EdadInvalidaException` — Declaracion OBLIGATORIA en el
   metodo que lanza una checked exception. Sin esto, no compila.

5. `e.getMessage()` — Recupera el mensaje que pasamos al constructor:
   "Edad -5 no es valida"
""");
    }
}
