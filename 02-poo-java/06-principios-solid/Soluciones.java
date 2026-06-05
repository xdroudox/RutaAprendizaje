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
        System.out.println("=== SOLUCION 1: SRP - Refactorizar Pedido ===");
        System.out.println("// Clase 1: Solo datos del pedido");
        System.out.println("class Pedido {");
        System.out.println("    private int id;");
        System.out.println("    private List<Producto> productos;");
        System.out.println("    public double calcularTotal() {");
        System.out.println("        return productos.stream().mapToDouble(Producto::getPrecio).sum();");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("// Clase 2: Persistencia");
        System.out.println("class PedidoDAO {");
        System.out.println("    public void guardar(Pedido p) {");
        System.out.println("        System.out.println(\"Guardando pedido en BD...\");");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("// Clase 3: Facturacion y notificacion");
        System.out.println("class FacturaService {");
        System.out.println("    public void imprimirFactura(Pedido p) {");
        System.out.println("        System.out.println(\"Imprimiendo factura...\");");
        System.out.println("    }");
        System.out.println("    public void enviarEmail(Pedido p) {");
        System.out.println("        System.out.println(\"Enviando email...\");");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: Cada clase tiene una unica responsabilidad.");
        System.out.println("Pedido solo maneja datos, PedidoDAO solo persistencia, FacturaService solo facturacion.");
    }

    static void solucion_2() {
        System.out.println("=== SOLUCION 2: OCP - Sistema de descuentos ===");
        System.out.println("interface Descuento {");
        System.out.println("    double aplicar(double monto);");
        System.out.println("}");
        System.out.println();
        System.out.println("class DescuentoNormal implements Descuento {");
        System.out.println("    @Override");
        System.out.println("    public double aplicar(double monto) { return monto; }");
        System.out.println("}");
        System.out.println();
        System.out.println("class DescuentoPremium implements Descuento {");
        System.out.println("    @Override");
        System.out.println("    public double aplicar(double monto) { return monto * 0.90; }");
        System.out.println("}");
        System.out.println();
        System.out.println("class DescuentoVIP implements Descuento {");
        System.out.println("    @Override");
        System.out.println("    public double aplicar(double monto) { return monto * 0.75; }");
        System.out.println("}");
        System.out.println();
        System.out.println("class CalculadoraDescuento {");
        System.out.println("    public double calcular(Descuento descuento, double monto) {");
        System.out.println("        return descuento.aplicar(monto);");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("Explicacion: Para anadir un nuevo descuento, solo creamos una nueva clase.");
        System.out.println("No modificamos el codigo existente. Abierto a extension, cerrado a modificacion.");
    }

    static void solucion_3() {
        System.out.println("=== SOLUCION 3: DIP - Sistema de notificaciones ===");
        System.out.println("interface Notificador {");
        System.out.println("    void enviar(String mensaje);");
        System.out.println("}");
        System.out.println();
        System.out.println("class EmailNotificador implements Notificador {");
        System.out.println("    @Override");
        System.out.println("    public void enviar(String mensaje) {");
        System.out.println("        System.out.println(\"Enviando email: \" + mensaje);");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("class SMSNotificador implements Notificador {");
        System.out.println("    @Override");
        System.out.println("    public void enviar(String mensaje) {");
        System.out.println("        System.out.println(\"Enviando SMS: \" + mensaje);");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("class ServicioNotificacion {");
        System.out.println("    private Notificador notificador;");
        System.out.println();
        System.out.println("    public ServicioNotificacion(Notificador notificador) {");
        System.out.println("        this.notificador = notificador;");
        System.out.println("    }");
        System.out.println();
        System.out.println("    public void notificar(String mensaje) {");
        System.out.println("        notificador.enviar(mensaje);");
        System.out.println("    }");
        System.out.println("}");
        System.out.println();
        System.out.println("// Uso:");
        System.out.println("// Notificador email = new EmailNotificador();");
        System.out.println("// ServicioNotificacion s = new ServicioNotificacion(email);");
        System.out.println("// s.notificar(\"Hola\");");
        System.out.println();
        System.out.println("Explicacion: ServicioNotificacion depende de la abstraccion Notificador,");
        System.out.println("no de una implementacion concreta. Podemos cambiar el tipo de notificacion facilmente.");
    }
}
