/**
 * SOLUCIONES - Polimorfismo (Java)
 * Ejecuta desde raiz: python scripts/runner.py 2 4 [ejercicio] -s
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
            System.out.println("  🟢 1. Sobrecarga de sumar()");
            System.out.println("  🟡 2. Array polimorfico de Animales");
            System.out.println("  🔴 3. Figura, Circulo y Rectangulo");
        }
    }

    static void solucion_1() {
        System.out.println("=".repeat(50));
        System.out.println("🟢 SOLUCION 1: Sobrecarga de sumar()");
        System.out.println("=".repeat(50));
        System.out.println();

        System.out.println("--- CODIGO (Main.java) ---");
        System.out.println("""
class Calculadora {
    int sumar(int a, int b) {
        return a + b;
    }

    int sumar(int a, int b, int c) {
        return a + b + c;
    }
}

public class Main {
    public static void main(String[] args) {
        Calculadora calc = new Calculadora();
        System.out.println(calc.sumar(3, 4));     // 7
        System.out.println(calc.sumar(3, 4, 5));  // 12
    }
}
""");

        System.out.println("--- EXPLICACION ---");
        System.out.println("""
1. `int sumar(int a, int b)` — Primer metodo. Suma DOS enteros.

2. `int sumar(int a, int b, int c)` — SEGUNDO metodo, MISMO nombre,
   pero DIFERENTE numero de parametros (3 en vez de 2).

3. Esto es OVERLOADING (sobrecarga): el mismo nombre de metodo representa
   operaciones distintas segun los argumentos.

4. `calc.sumar(3, 4)` — Java ve 2 argumentos int → ejecuta la version de 2 params.
   `calc.sumar(3, 4, 5)` — Java ve 3 argumentos int → ejecuta la version de 3 params.

5. La sobrecarga se resuelve en TIEMPO DE COMPILACION. Java sabe exactamente
   que metodo llamar solo con mirar los tipos de los argumentos.
""");
    }

    static void solucion_2() {
        System.out.println("=".repeat(50));
        System.out.println("🟡 SOLUCION 2: Array polimorfico de Animales");
        System.out.println("=".repeat(50));
        System.out.println();

        System.out.println("--- CODIGO (Main.java) ---");
        System.out.println("""
class Animal {
    void hacerSonido() {
        System.out.println("...");
    }
}

class Perro extends Animal {
    @Override
    void hacerSonido() {
        System.out.println("Guau!");
    }
}

class Gato extends Animal {
    @Override
    void hacerSonido() {
        System.out.println("Miau!");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal[] animales = new Animal[2];
        animales[0] = new Perro();
        animales[1] = new Gato();

        for (Animal a : animales) {
            a.hacerSonido();
        }
    }
}
""");

        System.out.println("--- EXPLICACION ---");
        System.out.println("""
1. `Animal[] animales = new Animal[2]` — Array de tipo ANIMAL (la superclase).
   Puede contener CUALQUIER objeto que sea Animal o subclase de Animal.

2. `animales[0] = new Perro()` — Guardamos un Perro. El array es tipo Animal,
   pero el objeto REAL es Perro.
   `animales[1] = new Gato()` — Guardamos un Gato.

3. `for (Animal a : animales)` — Iteramos. EN CADA iteracion, `a` apunta a
   un objeto diferente: primero Perro, luego Gato.

4. `a.hacerSonido()` — DINAMIC DISPATCH:
   - Cuando a apunta a Perro: ejecuta hacerSonido() DE PERRO → "Guau!"
   - Cuando a apunta a Gato: ejecuta hacerSonido() DE GATO → "Miau!"

5. El tipo DECLARADO de `a` es Animal, pero el tipo REAL determina el
   comportamiento. Eso es POLIMORFISMO.
""");
    }

    static void solucion_3() {
        System.out.println("=".repeat(50));
        System.out.println("🔴 SOLUCION 3: Figura, Circulo y Rectangulo");
        System.out.println("=".repeat(50));
        System.out.println();

        System.out.println("--- CODIGO (Main.java) ---");
        System.out.println("""
class Figura {
    double area() {
        return 0.0;
    }
}

class Circulo extends Figura {
    double radio;

    Circulo(double radio) {
        this.radio = radio;
    }

    @Override
    double area() {
        return Math.PI * radio * radio;
    }
}

class Rectangulo extends Figura {
    double base;
    double altura;

    Rectangulo(double base, double altura) {
        this.base = base;
        this.altura = altura;
    }

    @Override
    double area() {
        return base * altura;
    }
}

public class Main {
    public static void main(String[] args) {
        Figura[] figuras = new Figura[2];
        figuras[0] = new Circulo(5);
        figuras[1] = new Rectangulo(4, 6);

        for (Figura f : figuras) {
            System.out.println("Area: " + f.area());
        }
    }
}
""");

        System.out.println("--- EXPLICACION ---");
        System.out.println("""
1. `class Figura { double area() { return 0.0; } }` — Clase BASE.
   area() devuelve 0.0 como valor por defecto. Es la implementacion generica.

2. `class Circulo extends Figura` — Circulo ES-UNA Figura.
   `@Override double area()` — Sobrescribe con la formula del area del circulo:
   PI * radio^2. Para radio=5: 3.14159 * 25 = 78.54

3. `class Rectangulo extends Figura` — Rectangulo ES-UNA Figura.
   `@Override double area()` — base * altura. Para 4x6: 24.0

4. `Figura[] figuras` — Array de tipo FIGURA. Almacena un Circulo y un Rectangulo.

5. `f.area()` — POLIMORFISMO:
   - Circulo.area() usa Math.PI * radio * radio
   - Rectangulo.area() usa base * altura
   - MISMA llamada (f.area()), COMPORTAMIENTO DIFERENTE

6. `Math.PI` — Constante de Java con el valor de PI (3.141592653589793).
""");
    }
}
