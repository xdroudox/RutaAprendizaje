import java.time.Year;

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
        System.out.println("=== SOLUCION 1: Clase Empleado encapsulada ===");
        System.out.println("class Empleado {");
        System.out.println("    private String nombre;");
        System.out.println("    private double salario;");
        System.out.println("    private String departamento;");
        System.out.println();
        System.out.println("    public String getNombre() { return nombre; }");
        System.out.println("    public void setNombre(String nombre) { this.nombre = nombre; }");
        System.out.println();
        System.out.println("    public double getSalario() { return salario; }");
        System.out.println("    public void setSalario(double salario) {");
        System.out.println("        if (salario >= 0) this.salario = salario;");
        System.out.println("        else System.out.println(\"Salario no puede ser negativo\");");
        System.out.println("    }");
        System.out.println();
        System.out.println("    public String getDepartamento() { return departamento; }");
        System.out.println("    public void setDepartamento(String departamento) {");
        System.out.println("        if (departamento != null && !departamento.isEmpty())");
        System.out.println("            this.departamento = departamento;");
        System.out.println("        else System.out.println(\"Departamento no puede estar vacio\");");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("public class Main {");
        System.out.println("    public static void main(String[] args) {");
        System.out.println("        Empleado e = new Empleado();");
        System.out.println("        e.setNombre(\"Carlos\");");
        System.out.println("        e.setSalario(2500.0);");
        System.out.println("        e.setDepartamento(\"Ventas\");");
        System.out.println("        System.out.println(e.getNombre() + \" - \" + e.getSalario());");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: Los atributos privados solo se acceden mediante getters/setters.");
        System.out.println("Los setters incluyen validacion para mantener el objeto en estado valido.");
    }

    static void solucion_2() {
        System.out.println("=== SOLUCION 2: Clase Libro con validacion ===");
        System.out.println("class Libro {");
        System.out.println("    private String titulo;");
        System.out.println("    private String autor;");
        System.out.println("    private String isbn;");
        System.out.println("    private int anioPublicacion;");
        System.out.println();
        System.out.println("    public String getTitulo() { return titulo; }");
        System.out.println("    public void setTitulo(String titulo) {");
        System.out.println("        if (titulo != null && !titulo.isEmpty()) this.titulo = titulo;");
        System.out.println("    }");
        System.out.println("    public String getAutor() { return autor; }");
        System.out.println("    public void setAutor(String autor) { this.autor = autor; }");
        System.out.println("    public String getIsbn() { return isbn; }");
        System.out.println("    public void setIsbn(String isbn) {");
        System.out.println("        if (isbn.length() == 13) this.isbn = isbn;");
        System.out.println("    }");
        System.out.println("    public int getAnioPublicacion() { return anioPublicacion; }");
        System.out.println("    public void setAnioPublicacion(int anio) {");
        System.out.println("        if (anio <= Year.now().getValue()) this.anioPublicacion = anio;");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: Las validaciones mantienen la integridad de los datos.");
        System.out.println("isbn de 13 caracteres sigue el estandar ISBN-13.");
    }

    static void solucion_3() {
        System.out.println("=== SOLUCION 3: CuentaAhorros JavaBeans ===");
        System.out.println("class CuentaAhorros {");
        System.out.println("    private String numeroCuenta;");
        System.out.println("    private String titular;");
        System.out.println("    private double saldo;");
        System.out.println("    private double tasaInteres;");
        System.out.println();
        System.out.println("    public CuentaAhorros() {}");
        System.out.println();
        System.out.println("    public String getNumeroCuenta() { return numeroCuenta; }");
        System.out.println("    public void setNumeroCuenta(String n) { numeroCuenta = n; }");
        System.out.println("    public String getTitular() { return titular; }");
        System.out.println("    public void setTitular(String t) { titular = t; }");
        System.out.println("    public double getSaldo() { return saldo; }");
        System.out.println("    public void setSaldo(double s) { saldo = s; }");
        System.out.println("    public double getTasaInteres() { return tasaInteres; }");
        System.out.println("    public void setTasaInteres(double t) { tasaInteres = t; }");
        System.out.println();
        System.out.println("    public void aplicarInteres() {");
        System.out.println("        saldo += saldo * tasaInteres / 100;");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: Patron JavaBeans: constructor sin args, atributos privados,");
        System.out.println("getters y setters publicos. aplicarInteres calcula el interes compuesto.");
    }
}
