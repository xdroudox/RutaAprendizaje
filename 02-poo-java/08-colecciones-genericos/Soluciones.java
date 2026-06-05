import java.util.*;

public class Soluciones {
    public static void main(String[] args) {
        if (args.length > 0) {
            int n = Integer.parseInt(args[0]);
            switch (n) {
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
        System.out.println("=== SOLUCION 1: ArrayList de estudiantes ===");
        System.out.println("class Estudiante {");
        System.out.println("    String nombre;");
        System.out.println("    double nota;");
        System.out.println("    public Estudiante(String nombre, double nota) {");
        System.out.println("        this.nombre = nombre; this.nota = nota;");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("ArrayList<Estudiante> estudiantes = new ArrayList<>();");
        System.out.println("estudiantes.add(new Estudiante(\"Ana\", 8.5));");
        System.out.println("estudiantes.add(new Estudiante(\"Luis\", 7.0));");
        System.out.println("estudiantes.add(new Estudiante(\"Sofia\", 9.2));");
        System.out.println();
        System.out.println("// Listar");
        System.out.println("for (Estudiante e : estudiantes) {");
        System.out.println("    System.out.println(e.nombre + \" - \" + e.nota);");
        System.out.println("}");
        System.out.println();
        System.out.println("// Promedio");
        System.out.println("double suma = 0;");
        System.out.println("for (Estudiante e : estudiantes) suma += e.nota;");
        System.out.println("double promedio = suma / estudiantes.size();");
        System.out.println("System.out.println(\"Promedio: \" + promedio);");
        System.out.println();
        System.out.println("// Mayor nota");
        System.out.println("Estudiante mejor = estudiantes.get(0);");
        System.out.println("for (Estudiante e : estudiantes) {");
        System.out.println("    if (e.nota > mejor.nota) mejor = e;");
        System.out.println("}");
        System.out.println("System.out.println(\"Mejor: \" + mejor.nombre);");
        System.out.println();
        System.out.println("Explicacion: ArrayList permite almacenar objetos y recorrerlos facilmente.");
        System.out.println("Usamos for-each para iterar y metodos de instancia para los calculos.");
    }

    static void solucion_2() {
        System.out.println("=== SOLUCION 2: HashMap de contactos ===");
        System.out.println("HashMap<String, String> agenda = new HashMap<>();");
        System.out.println();
        System.out.println("// Anadir");
        System.out.println("agenda.put(\"Juan\", \"612345678\");");
        System.out.println("agenda.put(\"Ana\", \"698765432\");");
        System.out.println();
        System.out.println("// Buscar");
        System.out.println("String telefono = agenda.get(\"Juan\");");
        System.out.println("System.out.println(\"Telefono de Juan: \" + telefono);");
        System.out.println();
        System.out.println("// Eliminar");
        System.out.println("agenda.remove(\"Ana\");");
        System.out.println();
        System.out.println("// Listar todos");
        System.out.println("for (Map.Entry<String, String> entry : agenda.entrySet()) {");
        System.out.println("    System.out.println(entry.getKey() + \": \" + entry.getValue());");
        System.out.println("}");
        System.out.println();
        System.out.println("// Verificar si existe");
        System.out.println("if (agenda.containsKey(\"Juan\")) {");
        System.out.println("    System.out.println(\"Juan existe en la agenda\");");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: HashMap asocia claves (nombre) con valores (telefono).");
        System.out.println("entrySet() permite iterar sobre pares clave-valor.");
    }

    static void solucion_3() {
        System.out.println("=== SOLUCION 3: Clase generica Par ===");
        System.out.println("class Par<K, V> {");
        System.out.println("    private K clave;");
        System.out.println("    private V valor;");
        System.out.println();
        System.out.println("    public Par(K clave, V valor) {");
        System.out.println("        this.clave = clave;");
        System.out.println("        this.valor = valor;");
        System.out.println("    }");
        System.out.println();
        System.out.println("    public K getClave() { return clave; }");
        System.out.println("    public void setClave(K clave) { this.clave = clave; }");
        System.out.println("    public V getValor() { return valor; }");
        System.out.println("    public void setValor(V valor) { this.valor = valor; }");
        System.out.println("}");
        System.out.println();
        System.out.println("public class Main {");
        System.out.println("    public static void main(String[] args) {");
        System.out.println("        Par<String, Integer> p1 = new Par<>(\"Ana\", 25);");
        System.out.println("        System.out.println(p1.getClave() + \" - \" + p1.getValor());");
        System.out.println();
        System.out.println("        Par<Integer, String> p2 = new Par<>(1, \"Producto A\");");
        System.out.println("        System.out.println(p2.getClave() + \" - \" + p2.getValor());");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: Par<K,V> usa dos parametros de tipo generico.");
        System.out.println("Podemos crear pares con diferentes combinaciones de tipos.");
    }
}
