/**
 * SOLUCIONES - Encapsulacion (Java)
 * Ejecuta desde raiz: python scripts/runner.py 2 2 [ejercicio] -s
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
            System.out.println("  🟢 1. CuentaBancaria con saldo private y validacion");
            System.out.println("  🟡 2. Producto con precio private y validacion");
            System.out.println("  🔴 3. Estudiante con notas private y promedio()");
        }
    }

    static void solucion_1() {
        System.out.println("=".repeat(50));
        System.out.println("🟢 SOLUCION 1: CuentaBancaria");
        System.out.println("=".repeat(50));
        System.out.println();

        System.out.println("--- CODIGO (Main.java) ---");
        System.out.println("""
class CuentaBancaria {
    private double saldo;

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        if (saldo >= 0) {
            this.saldo = saldo;
        } else {
            System.out.println("Error: saldo no puede ser negativo");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        CuentaBancaria c = new CuentaBancaria();

        c.setSaldo(1000);
        System.out.println(c.getSaldo());  // 1000.0

        c.setSaldo(-50);  // Error: saldo no puede ser negativo
    }
}
""");

        System.out.println("--- EXPLICACION ---");
        System.out.println("""
1. `private double saldo;` — Nadie fuera de CuentaBancaria puede acceder
   a saldo directamente. c.saldo = 5000; daria ERROR de compilacion.

2. `public double getSaldo()` — El GETTER permite LEER el valor.
   Sin el getter, no habria forma de saber el saldo desde fuera.

3. `public void setSaldo(double saldo)` — El SETTER permite MODIFICAR,
   pero con control. `if (saldo >= 0)` solo asigna si es valido.

4. `this.saldo = saldo;` — Solo se ejecuta si saldo >= 0.
   Si es negativo, imprime error y NO modifica el atributo.

5. `c.setSaldo(-50);` — Intenta asignar -50. El setter valida,
   imprime error, y saldo sigue siendo 1000 (no cambio).
""");
    }

    static void solucion_2() {
        System.out.println("=".repeat(50));
        System.out.println("🟡 SOLUCION 2: Producto");
        System.out.println("=".repeat(50));
        System.out.println();

        System.out.println("--- CODIGO (Main.java) ---");
        System.out.println("""
class Producto {
    private String nombre;
    private double precio;

    public Producto(String nombre, double precio) {
        this.nombre = nombre;
        setPrecio(precio);  // Reutiliza la validacion!
    }

    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        if (precio >= 0) {
            this.precio = precio;
        } else {
            System.out.println("Error: precio no puede ser negativo");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Producto p1 = new Producto("Laptop", 1500);
        System.out.println(p1.getPrecio());  // 1500.0

        Producto p2 = new Producto("Mouse", -50);  // Error
    }
}
""");

        System.out.println("--- EXPLICACION ---");
        System.out.println("""
1. `setPrecio(precio);` — En el constructor, usamos el SETTER en vez de
   asignar directamente `this.precio = precio`. Por que? Para REUTILIZAR
   la validacion. Si alguien en el futuro cambia la validacion en
   setPrecio(), el constructor automaticamente la usa.

2. Si hicieramos `this.precio = precio;` en el constructor, estariamos
   SALTANDO la validacion. Un precio negativo pasaria sin problemas.

3. `Producto p2 = new Producto("Mouse", -50);` — El constructor llama a
   setPrecio(-50), la validacion falla, imprime error. El atributo precio
   queda en 0.0 (valor por defecto de double en Java).
""");
    }

    static void solucion_3() {
        System.out.println("=".repeat(50));
        System.out.println("🔴 SOLUCION 3: Estudiante");
        System.out.println("=".repeat(50));
        System.out.println();

        System.out.println("--- CODIGO (Main.java) ---");
        System.out.println("""
class Estudiante {
    private double[] notas;

    public Estudiante(double[] notas) {
        this.notas = notas;
    }

    public double[] getNotas() {
        return notas;
    }

    public void setNotas(double[] notas) {
        this.notas = notas;
    }

    public double promedio() {
        double suma = 0;
        for (double n : notas) {
            suma += n;
        }
        return suma / notas.length;
    }
}

public class Main {
    public static void main(String[] args) {
        double[] notas = {7.5, 8.0, 6.5};
        Estudiante e = new Estudiante(notas);
        System.out.println("Promedio: " + e.promedio());
    }
}
""");

        System.out.println("--- EXPLICACION ---");
        System.out.println("""
1. `private double[] notas;` — El array de notas es privado. Nadie puede
   modificarlo directamente desde fuera.

2. `public double promedio()` — Metodo que CALCULA basado en datos privados.
   - `double suma = 0;` — Acumulador
   - `for (double n : notas)` — For-each: recorre cada elemento del array
   - `suma += n;` — Suma cada nota al acumulador
   - `return suma / notas.length;` — Divide por la cantidad de notas

3. `notas.length` — Propiedad de los arrays en Java que devuelve la
   cantidad de elementos. Para {7.5, 8.0, 6.5}, length = 3.

4. La encapsulacion permite que el metodo promedio() acceda a datos
   privados (notas) mientras que desde fuera solo vemos el resultado.
""");
    }
}
