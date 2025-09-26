#punto 1 - numeros del 1 al 100
for i in range(101):
    print(i)


#punto 2 - cantidad de digitos de un numero 
num = int(input("ingresa un número entero: "))
print("cantidad de dígitos:", len(str(abs(num))))


#punto 3 - sumar números entre dos valores
a = int(input("lngresa el primer número: "))
b = int(input("lngresa el segundo número: "))
suma = sum(range(min(a, b) + 1, max(a, b)))
print("la suma de los números entre", a, "y", b, "es:", suma)


#punto 4 - números hasta que el usuario ingrese 0
total = 0
while True:
    n = int(input("Ingresa un número (0 para terminar): "))
    if n == 0:
        break
    total += n
print("La suma total es:", total)


#punto 5 - juego de adivinar número
import random
secreto = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el número (0-9): "))
    intentos += 1
    if intento == secreto:
        print(f"¡Correcto! Lo lograste en {intentos} intentos.")
        break


#punto 6 - números pares de 100 a 0 en orden decreciente
for i in range(100, -1, -2):
    print(i)


#punto 7 - suma de 0 hasta un número ingresado
n = int(input("Ingresa un número positivo: "))
suma = sum(range(n + 1))
print("La suma de los números desde 0 hasta", n, "es:", suma)


#punto 8 - pares, impares, negativos y positivos
cantidad = 100 
pares = impares = negativos = positivos = 0

for _ in range(cantidad):
    num = int(input("Ingresa un número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num < 0:
        negativos += 1
    elif num > 0:
        positivos += 1

print("Pares:", pares)
print("Impares:", impares)
print("Negativos:", negativos)
print("Positivos:", positivos)


#punto 9 - calcular la media de 100 números
cantidad = 100  # cambiar este valor para probar con menos
suma = 0
for _ in range(cantidad):
    num = int(input("Ingresa un número: "))
    suma += num
print("La media es:", suma / cantidad)


#punto 10 - invertir los dígitos de un número
num = input("Ingresa un número: ")
print("Número invertido:", num[::-1])