/**
 * EJERCICIOS - MVC, Repository e Inyeccion de Dependencias
 * Ejecuta desde raiz: python scripts/runner.py 8 4 [ejercicio] [-p N]
 */
public class Ejercicios {
    public static void main(String[] args) {
        if (args.length > 0 && args[0].matches("\\d+")) {
            int num = Integer.parseInt(args[0]);
            int pista = 0;
            for (int i = 1; i < args.length; i++) {
                if (args[i].equals("-p") && i + 1 < args.length) {
                    pista = Integer.parseInt(args[i + 1]);
                    break;
                }
            }
            switch (num) {
                case 1: ejercicio_1(pista); break;
                case 2: ejercicio_2(pista); break;
                case 3: ejercicio_3(pista); break;
            }
        } else {
            System.out.println("EJERCICIOS:");
            System.out.println("  🟢 Ej 1: MVC - Modelo Usuario, repositorio, controlador");
            System.out.println("  🟡 Ej 2: Vista simple que muestra datos del modelo");
            System.out.println("  🟡 Ej 3: Inyectar dependencia (Repository) en Service");
        }
    }

    static void ejercicio_1(int pista) {
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
        if (pista > 0) {
            System.out.println("\n========================================");
            System.out.println("PISTAS:");
        }
        if (pista >= 1) {
            System.out.println("\n🟢 PISTA 1 (Basica):");
            System.out.println("  - Usuario: atributos privados, constructor con parametros, getters");
            System.out.println("  - Repositorio en memoria: Map<Integer, Usuario> + contador de IDs");
            System.out.println("  - Controlador: metodos crearUsuario() y listarUsuarios()");
        }
        if (pista >= 2) {
            System.out.println("\n🟡 PISTA 2 (Intermedia):");
            System.out.println("  class Usuario {\n" +
                "      private int id; private String nombre; private String email;\n" +
                "      public Usuario(int id, String n, String e) { this.id = id; this.nombre = n; this.email = e; }\n" +
                "      public int getId() { return id; }\n" +
                "      public String getNombre() { return nombre; }\n" +
                "      public String getEmail() { return email; }\n" +
                "      public String toString() { return id + \" - \" + nombre + \" (\" + email + \")\"; }\n" +
                "  }");
            System.out.println("  class RepositorioUsuarios {\n" +
                "      private java.util.Map<Integer, Usuario> datos = new java.util.HashMap<>();\n" +
                "      private int contador = 1;\n" +
                "      public Usuario guardar(String n, String e) {\n" +
                "          Usuario u = new Usuario(contador++, n, e); datos.put(u.getId(), u); return u;\n" +
                "      }\n" +
                "      public java.util.List<Usuario> listar() { return new java.util.ArrayList<>(datos.values()); }\n" +
                "  }");
        }
        if (pista >= 3) {
            System.out.println("\n🔴 PISTA 3 (Avanzada - casi la solucion):");
            System.out.println("  class ControladorUsuario {\n" +
                "      private RepositorioUsuarios repo = new RepositorioUsuarios();\n" +
                "      public void crearUsuario(String n, String e) {\n" +
                "          System.out.println(\"Creado: \" + repo.guardar(n, e));\n" +
                "      }\n" +
                "      public void listarUsuarios() {\n" +
                "          for (Usuario u : repo.listar()) System.out.println(u);\n" +
                "      }\n" +
                "  }\n" +
                "  // Uso: new ControladorUsuario().crearUsuario(\"Ana\", \"ana@test.com\");");
        }
    }

    static void ejercicio_2(int pista) {
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
        if (pista > 0) {
            System.out.println("\n========================================");
            System.out.println("PISTAS:");
        }
        if (pista >= 1) {
            System.out.println("\n🟢 PISTA 1 (Basica):");
            System.out.println("  - VistaUsuario es una interfaz con metodos para mostrar 1 o varios usuarios");
            System.out.println("  - VistaConsola implementa VistaUsuario e imprime en consola");
            System.out.println("  - mostrar(): System.out.println(\"Nombre: \" + u.getNombre()) etc.");
        }
        if (pista >= 2) {
            System.out.println("\n🟡 PISTA 2 (Intermedia):");
            System.out.println("  interface VistaUsuario {\n" +
                "      void mostrar(Usuario u);\n" +
                "      void mostrarTodos(java.util.List<Usuario> lista);\n" +
                "  }");
            System.out.println("  class VistaConsola implements VistaUsuario {\n" +
                "      public void mostrar(Usuario u) {\n" +
                "          System.out.println(\"Nombre: \" + u.getNombre());\n" +
                "          System.out.println(\"Email: \" + u.getEmail());\n" +
                "          System.out.println(\"-\".repeat(20));\n" +
                "      }\n" +
                "      public void mostrarTodos(java.util.List<Usuario> lista) {\n" +
                "          for (Usuario u : lista) mostrar(u);\n" +
                "      }\n" +
                "  }");
        }
        if (pista >= 3) {
            System.out.println("\n🔴 PISTA 3 (Avanzada - casi la solucion):");
            System.out.println("  VistaConsola vista = new VistaConsola();");
            System.out.println("  vista.mostrar(new Usuario(1, \"Maria\", \"maria@test.com\"));");
            System.out.println("  // Muestra: Nombre: Maria, Email: maria@test.com");
        }
    }

    static void ejercicio_3(int pista) {
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
        if (pista > 0) {
            System.out.println("\n========================================");
            System.out.println("PISTAS:");
        }
        if (pista >= 1) {
            System.out.println("\n🟢 PISTA 1 (Basica):");
            System.out.println("  - RepositorioUsuario es una interface con metodos guardar() y listarNombres()");
            System.out.println("  - ServicioUsuario recibe RepositorioUsuario por constructor");
            System.out.println("  - ServicioUsuario llama a repo.guardar() y repo.listarNombres()");
        }
        if (pista >= 2) {
            System.out.println("\n🟡 PISTA 2 (Intermedia):");
            System.out.println("  interface RepositorioUsuario {\n" +
                "      void guardar(String nombre, String email);\n" +
                "      java.util.List<String> listarNombres();\n" +
                "  }");
            System.out.println("  class RepositorioMemoria implements RepositorioUsuario {\n" +
                "      private java.util.List<String> nombres = new java.util.ArrayList<>();\n" +
                "      public void guardar(String n, String e) { nombres.add(n); }\n" +
                "      public java.util.List<String> listarNombres() { return nombres; }\n" +
                "  }");
            System.out.println("  class ServicioUsuario {\n" +
                "      private RepositorioUsuario repo;\n" +
                "      public ServicioUsuario(RepositorioUsuario r) { this.repo = r; }\n" +
                "      public void registrar(String n, String e) {\n" +
                "          repo.guardar(n, e);\n" +
                "          System.out.println(\"Usuario registrado: \" + n);\n" +
                "      }\n" +
                "      public void listar() {\n" +
                "          System.out.println(\"Usuarios: \" + repo.listarNombres());\n" +
                "      }\n" +
                "  }");
        }
        if (pista >= 3) {
            System.out.println("\n🔴 PISTA 3 (Avanzada - casi la solucion):");
            System.out.println("  RepositorioUsuario repo = new RepositorioMemoria();");
            System.out.println("  ServicioUsuario servicio = new ServicioUsuario(repo);");
            System.out.println("  servicio.registrar(\"Carlos\", \"carlos@test.com\");");
            System.out.println("  servicio.registrar(\"Diana\", \"diana@test.com\");");
            System.out.println("  servicio.listar();");
            System.out.println("  // DI funciona: podemos cambiar RepositorioMemoria por otra implementacion");
        }
    }
}
