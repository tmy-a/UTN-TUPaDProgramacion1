#punto 1
print ("hola mundo")

#punto 2
nombre = input ("Por favor ingrese su nombre: ")
input(f"Hola {nombre}")

#punto 3
nombreyapellido = input("ingrese su nombre y apellido: ")
edad = input( "ahora ingrese su edad por favor: ")
pais = input ("ingrese lugar de residencia: ")
print(f"su nombre y apellido es {nombreyapellido}, tiene {edad} años, y vive en {pais}")

#punto 4
import math
radio = float(input( "ingrese el radio del circulo: "))
area = round(math.pi * (radio)**2, 2)
perimetro = round(2 * math.pi * radio, 2)

print (f"el area del circulo es de {area} y el perimetro es de {perimetro}")

#punto 5
segundos = int(input("ingrese la cantidad de segundos: "))
horas = round(segundos / 3600, 2)
print(f"{segundos} segundos equivale a {horas} horas")

#punto 6
num_mult = int(input("ingrese un numero entero: "))

num0 = num_mult * 0 
num1 = num_mult * 1
num2 = num_mult * 2
num3 = num_mult * 3
num4 = num_mult * 4
num5 = num_mult * 5
num6 = num_mult * 6
num7 = num_mult * 7
num8 = num_mult * 8
num9 = num_mult * 9
num10 = num_mult * 10

print(f"""{num_mult} x 0 = {num0}
{num_mult} x 1 = {num1}
{num_mult} x 2 = {num2}
{num_mult} x 3 = {num3}
{num_mult} x 4 = {num4}
{num_mult} x 5 = {num5}
{num_mult} x 6 = {num6}
{num_mult} x 7 = {num7}
{num_mult} x 8 = {num8}
{num_mult} x 9 = {num9}
{num_mult} x 10 = {num10}
""")

#punto 7
num1 = float(input("ingrese un numero entero distinto a 0: "))
num2 = float(input("ahora ingrese el segundo numero: ")) 

suma = num1 + num2
resta = num1 - num2 
division = num1 / num2
mult = num1 * num2

print(f"""el resultado de ambos numeros si se suman es de {suma}
al restarlos es de {resta}
al dividirlos es de {division} 
al multiplicarlos es de {mult}  """)

#punto 8
peso = float(input("Ingrese su peso en KG: "))
altura = float(input("ingrese su altura en metros: "))

imc = (peso / altura**2, 2)

print(f"su IMC es de: {imc}")

#punto 9 
celsius = float(input("ingrese la temperatura en °C: "))

fahrenheit = round((9/5) * celsius + 32, 2)
print(f"{celsius}°C equivale a {fahrenheit} °F")

#punto 10 
num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el segundo numero: "))
num3 = float(input("ingrese el tercer numero: "))

suma = num1 + num2 + num3
promedio = round(suma / 3, 2)

print(f"el promedio es de: { promedio}")