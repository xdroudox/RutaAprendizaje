# 🧩 Lógica de Programación

## ¿Qué es la lógica de programación?

Es la capacidad de **resolver problemas** usando instrucciones secuenciales, igual que una receta de cocina:

```
RECETA: Hacer café ☕
1. Hervir agua
2. Poner café en la taza
3. Verter agua caliente
4. Esperar 3 minutos
5. ¡Disfrutar!
```

Un **algoritmo** es exactamente eso: una secuencia de pasos ordenados para resolver un problema.

## Pseudocódigo

Antes de escribir código real, los programadores usan **pseudocódigo**: lenguaje humano que describe la lógica.

```
ALGORITMO: Calcular el mayor de 2 números
1. LEER numero1
2. LEER numero2
3. SI numero1 > numero2 ENTONCES
4.     MOSTRAR "El mayor es:", numero1
5. SINO
6.     MOSTRAR "El mayor es:", numero2
7. FIN SI
```

## Diagramas de flujo

Los algoritmos también se representan visualmente:

```
    ┌──────────┐
    │  INICIO  │
    └────┬─────┘
         ▼
    ┌──────────┐
    │ LEER a,b │
    └────┬─────┘
         ▼
      ┌─────┐
      │a > b│───SÍ──→ ┌──────────────┐
      └──┬──┘         │ "a es mayor" │
         │ NO         └──────────────┘
         ▼
    ┌──────────────┐
    │ "b es mayor" │
    └──────────────┘
```

## Características de un buen algoritmo

| Característica | ¿Qué significa? |
|---------------|-----------------|
| **Preciso** | Cada paso está claramente definido |
| **Finito** | Tiene un final (no es un loop infinito) |
| **Definido** | Mismos datos de entrada → mismos resultados |
| **Eficiente** | Resuelve el problema con la menor cantidad de pasos |

## Traduciendo a Python

```python
# Algoritmo: saludar al usuario
print("¿Cómo te llamas?")
nombre = input()
print("Hola, " + nombre + "!")

# Algoritmo: calcular el mayor de 2 números
a = int(input("Número 1: "))
b = int(input("Número 2: "))
if a > b:
    print(f"{a} es mayor que {b}")
else:
    print(f"{b} es mayor que {a}")
```

## 🎯 Ejercicios

### 1. Tu primer algoritmo
Escribe un algoritmo (en español) que prepare un sándwich. Luego tradúcelo a Python.

➜ **Ejecuta:** `python ejercicios.py 1`

### 2. El algoritmo del cajero
Crea un algoritmo que calcule cuántos billetes de cada denominación necesita un cajero para dar un vuelto.

➜ **Ejecuta:** `python ejercicios.py 2`

### 3. Número par o impar
Escribe un algoritmo que determine si un número es par o impar.

➜ **Ejecuta:** `python ejercicios.py 3`
