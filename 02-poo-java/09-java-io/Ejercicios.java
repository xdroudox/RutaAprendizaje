import java.util.Scanner;

public class Ejercicios {
    public static void main(String[] args) {
        if (args.length == 0) {
            menu();
        } else if (args[0].equals("-s") && args.length > 1) {
            mostrarSolucion(Integer.parseInt(args[1]));
        } else {
            int num = Integer.parseInt(args[0]);
            if (args.length > 1 && args[1].equals("-p")) {
                mostrarPista(num);
            } else {
                ejecutarEjercicio(num);
            }
        }
    }

    static void menu() {
        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.println("=== MENU - Java I/O ===");
            System.out.println("1. Leer y mostrar archivo");
            System.out.println("2. Escribir en archivo");
            System.out.println("3. Copiar archivo");
            System.out.println("0. Salir");
            System.out.print("Selecciona un ejercicio: ");
            String opt = sc.nextLine();
            if (opt.equals("0")) break;
            try {
                int n = Integer.parseInt(opt);
                ejecutarEjercicio(n);
            } catch (NumberFormatException e) {
                System.out.println("Opcion invalida");
            }
        }
        sc.close();
    }

    static void ejecutarEjercicio(int n) {
        switch (n) {
            case 1: ejercicio_1(); break;
            case 2: ejercicio_2(); break;
            case 3: ejercicio_3(); break;
            default: System.out.println("Ejercicio no encontrado");
        }
    }

    static void ejercicio_1() {
        System.out.println(">> EJERCICIO 1: Leer y mostrar archivo");
        System.out.println("Programa que pide el nombre de un archivo al usuario.");
        System.out.println("Lee linea por linea con BufferedReader.");
        System.out.println("Muestra el contenido en consola.");
        System.out.println("Si no existe, captura la excepcion.");
        System.out.println();
        System.out.println("PISTA: 'new BufferedReader(new FileReader(nombre))'");
        System.out.println("// --- TU CODIGO AQUI ---");
    }

    static void ejercicio_2() {
        System.out.println(">> EJERCICIO 2: Escribir en archivo");
        System.out.println("Programa que pide al usuario escribir lineas de texto.");
        System.out.println("Cada linea se guarda en 'notas.txt' con BufferedWriter.");
        System.out.println("Termina cuando el usuario escribe 'salir'.");
        System.out.println();
        System.out.println("PISTA: Usa bw.write(linea) y bw.newLine().");
        System.out.println("// --- TU CODIGO AQUI ---");
    }

    static void ejercicio_3() {
        System.out.println(">> EJERCICIO 3: Copiar archivo");
        System.out.println("Copia el contenido de 'origen.txt' a 'destino.txt'.");
        System.out.println("Usa try-with-resources con BufferedReader y BufferedWriter.");
        System.out.println("Muestra cuantos caracteres se copiaron.");
        System.out.println();
        System.out.println("PISTA: 'int total = 0; while ((linea = br.readLine()) != null) { total += linea.length(); }'");
        System.out.println("// --- TU CODIGO AQUI ---");
    }

    static void mostrarPista(int n) {
        String[][] pistas = {
            {
                "Pista 1: 'BufferedReader br = new BufferedReader(new FileReader(nombre))'",
                "Pista 2: 'while ((linea = br.readLine()) != null) { System.out.println(linea); }'",
                "Pista 3: Captura FileNotFoundException y IOException"
            },
            {
                "Pista 1: 'BufferedWriter bw = new BufferedWriter(new FileWriter(\"notas.txt\"))'",
                "Pista 2: 'bw.write(linea); bw.newLine();'",
                "Pista 3: Bucle while(!linea.equals(\"salir\"))"
            },
            {
                "Pista 1: 'try (BufferedReader br = new BufferedReader(...); BufferedWriter bw = new BufferedWriter(...))'",
                "Pista 2: 'int total = 0; String linea; while ((linea = br.readLine()) != null) { bw.write(linea); bw.newLine(); total += linea.length(); }'",
                "Pista 3: 'System.out.println(\"Copiados \" + total + \" caracteres\");'"
            }
        };
        if (n >= 1 && n <= pistas.length) {
            for (String p : pistas[n - 1]) {
                System.out.println(p);
            }
        }
    }

    static void mostrarSolucion(int n) {
        Soluciones.main(new String[]{String.valueOf(n)});
    }
}
