/**
 * EJERCICIOS - Java I/O
 * Ejecuta desde raiz: python scripts/runner.py 2 9 [ejercicio]
 */
import java.io.*;

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
            System.out.println("1. Escribir texto a un archivo con FileWriter");
            System.out.println("2. Leer contenido de un archivo con BufferedReader");
            System.out.println("3. Copiar un archivo a otro");
        }
    }

    static void ejercicio_1() {
        System.out.println(">> EJERCICIO 1: Escribir archivo con FileWriter");
        System.out.println("-".repeat(40));
        System.out.println("Usa FileWriter para escribir \"Hola mundo\" en un archivo");
        System.out.println("llamado \"salida.txt\".");
        System.out.println("Usa try-with-resources para asegurar que el recurso se cierre.");
        System.out.println("Muestra \"Archivo escrito correctamente\" al finalizar.");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    static void ejercicio_2() {
        System.out.println(">> EJERCICIO 2: Leer archivo con BufferedReader");
        System.out.println("-".repeat(40));
        System.out.println("Usa BufferedReader y FileReader para leer el archivo \"salida.txt\"");
        System.out.println("(creado en el ejercicio anterior).");
        System.out.println("Lee linea por linea con readLine() y muestralas en consola.");
        System.out.println("Usa try-with-resources.");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }

    static void ejercicio_3() {
        System.out.println(">> EJERCICIO 3: Copiar archivo");
        System.out.println("-".repeat(40));
        System.out.println("Usa FileReader y FileWriter (o BufferedReader/BufferedWriter)");
        System.out.println("para copiar el contenido de \"origen.txt\" a \"destino.txt\".");
        System.out.println("Lee caracter por caracter (read()) y escribelos en el destino.");
        System.out.println("Muestra \"Archivo copiado correctamente\" al finalizar.");
        System.out.println();
        System.out.println("// ==== ESCRIBE TU RESPUESTA AQUI ====");
    }
}
