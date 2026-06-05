/**
 * SOLUCIONES - Principios SOLID
 * Ejecuta: python scripts/runner.py 2 6 [ejercicio] -s
 */
public class Soluciones {

    public static void main(String[] args) {
        if (args.length > 0) {
            int num = Integer.parseInt(args[0]);
            switch (num) {
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
        System.out.println("=== SOLUCION 1: SRP ===");
        System.out.println("class Reporte {");
        System.out.println("    String titulo;");
        System.out.println("    String contenido;");
        System.out.println();
        System.out.println("    Reporte(String titulo, String contenido) {");
        System.out.println("        this.titulo = titulo;");
        System.out.println("        this.contenido = contenido;");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("class Impresora {");
        System.out.println("    static void imprimir(Reporte r) {");
        System.out.println("        System.out.println(r.titulo);");
        System.out.println("        System.out.println(\"---\");");
        System.out.println("        System.out.println(r.contenido);");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("// En el main:");
        System.out.println("Reporte r = new Reporte(\"Ventas\", \"Resumen del mes\");");
        System.out.println("Impresora.imprimir(r);");
        System.out.println();
        System.out.println("Explicacion: Reporte solo almacena datos. Impresora solo imprime. SRP cumplido.");
    }

    static void solucion_2() {
        System.out.println("=== SOLUCION 2: OCP ===");
        System.out.println("interface Descuento {");
        System.out.println("    double aplicar(double precio);");
        System.out.println("}");
        System.out.println();
        System.out.println("class DescuentoPorcentaje implements Descuento {");
        System.out.println("    double porcentaje;");
        System.out.println("    DescuentoPorcentaje(double porcentaje) { this.porcentaje = porcentaje; }");
        System.out.println("    public double aplicar(double precio) { return precio * (1 - porcentaje / 100); }");
        System.out.println("}");
        System.out.println();
        System.out.println("class DescuentoFijo implements Descuento {");
        System.out.println("    double cantidad;");
        System.out.println("    DescuentoFijo(double cantidad) { this.cantidad = cantidad; }");
        System.out.println("    public double aplicar(double precio) { return Math.max(0, precio - cantidad); }");
        System.out.println("}");
        System.out.println();
        System.out.println("class CalculadoraPrecio {");
        System.out.println("    double calcular(double precio, Descuento d) {");
        System.out.println("        return d.aplicar(precio);");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("// En el main:");
        System.out.println("CalculadoraPrecio calc = new CalculadoraPrecio();");
        System.out.println("System.out.println(calc.calcular(100, new DescuentoPorcentaje(10))); // 90.0");
        System.out.println("System.out.println(calc.calcular(100, new DescuentoFijo(15)));      // 85.0");
        System.out.println();
        System.out.println("Explicacion: Para aniadir un nuevo descuento, solo se crea una clase nueva.");
        System.out.println("No se modifica codigo existente. OCP cumplido.");
    }

    static void solucion_3() {
        System.out.println("=== SOLUCION 3: DIP ===");
        System.out.println("interface BaseDatos {");
        System.out.println("    void guardar(String dato);");
        System.out.println("}");
        System.out.println();
        System.out.println("class BaseDatosMySQL implements BaseDatos {");
        System.out.println("    public void guardar(String dato) {");
        System.out.println("        System.out.println(\"Guardado en MySQL: \" + dato);");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("class BaseDatosArchivo implements BaseDatos {");
        System.out.println("    public void guardar(String dato) {");
        System.out.println("        System.out.println(\"Guardado en archivo: \" + dato);");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("class Servicio {");
        System.out.println("    private BaseDatos db;");
        System.out.println("    Servicio(BaseDatos db) { this.db = db; }");
        System.out.println("    void procesar(String dato) { db.guardar(dato); }");
        System.out.println("}");
        System.out.println();
        System.out.println("// En el main:");
        System.out.println("Servicio s1 = new Servicio(new BaseDatosMySQL());");
        System.out.println("Servicio s2 = new Servicio(new BaseDatosArchivo());");
        System.out.println("s1.procesar(\"datos\");");
        System.out.println("s2.procesar(\"datos\");");
        System.out.println();
        System.out.println("Explicacion: Servicio depende de la abstraccion BaseDatos, no de clases concretas.");
    }
}
