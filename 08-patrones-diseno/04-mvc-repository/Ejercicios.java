/**
 * EJERCICIOS - MVC, Repository e Inyeccion de Dependencias
 * Ejecuta desde raiz: python scripts/runner.py 8 4 [ejercicio]
 */
public class Ejercicios {
    public static void main(String[] args) {
        if (args.length > 0) {
            int num = Integer.parseInt(args[0]);
            switch (num) {
                case 1: ejercicio_1(); break;
                case 2: ejercicio_2(); break;
                case 3: ejercicio_3(); break;
            }
        } else {
            System.out.println("EJERCICIOS:");
            System.out.println("1. MVC - Modelo Usuario, repositorio, controlador");
            System.out.println("2. Vista simple que muestra datos del modelo");
            System.out.println("3. Inyectar dependencia (Repository) en Service");
        }
    }

    static void ejercicio_1() {
        System.out.println(">> EJERCICIO 1: MVC basico");
        System.out.println("-".repeat(40));
        System.out.println("Crea el modelo Usuario (id, nombre, email),");
        System.out.println("un repositorio en memoria y un controlador");
        System.out.println("que permita crear y listar usuarios.");
        System.out.println();
        System.out.println("class Usuario {");
        System.out.println("    private int id;");
        System.out.println("    private String nombre;");
        System.out.println("    private String email;");
        System.out.println("    // ==== ESCRIBE TU RESPUESTA AQUI ====");
        System.out.println("}");
    }

    static void ejercicio_2() {
        System.out.println(">> EJERCICIO 2: Vista simple");
        System.out.println("-".repeat(40));
        System.out.println("Crea una interfaz VistaUsuario que muestre datos");
        System.out.println("del modelo. Implementa VistaConsola que imprime");
        System.out.println("los usuarios en formato simple.");
        System.out.println();
        System.out.println("interface VistaUsuario {");
        System.out.println("    void mostrar(Usuario u);");
        System.out.println("    void mostrarTodos(List<Usuario> lista);");
        System.out.println("    // ==== ESCRIBE TU RESPUESTA AQUI ====");
        System.out.println("}");
    }

    static void ejercicio_3() {
        System.out.println(">> EJERCICIO 3: Inyeccion de Dependencias");
        System.out.println("-".repeat(40));
        System.out.println("Crea un ServicioUsuario que reciba un RepositorioUsuario");
        System.out.println("por constructor (Inyeccion de Dependencias).");
        System.out.println("Demuestra que puedes cambiar la implementacion");
        System.out.println("del repositorio sin cambiar el servicio.");
        System.out.println();
        System.out.println("class ServicioUsuario {");
        System.out.println("    private RepositorioUsuario repo;");
        System.out.println("    public ServicioUsuario(RepositorioUsuario repo) {");
        System.out.println("        this.repo = repo;");
        System.out.println("    }");
        System.out.println("    // ==== ESCRIBE TU RESPUESTA AQUI ====");
        System.out.println("}");
    }
}
