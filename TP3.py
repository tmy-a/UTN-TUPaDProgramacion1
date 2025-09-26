#punto 1
edad = int(input("Por favor, ingrese su edad: "))

if edad > 18:
    print ("Es mayor de edad")

#punto 2

nota = float(input("Por favor, ingrese su nota: "))
if nota >= 6:
    print("APROBADO")
elif nota < 6:
    print("DESAPROBADO")

#punto 3

numero = int(input("Ingrese un numero: "))

if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")


#punto 4

edad = int(input("ingrese su edad: "))

if edad < 12:
    print("Pertenece a la categoria: niño/a")

elif edad >= 12 and edad < 18:
    print("Pertenece a la categoria: adolescente")

elif edad >= 18 and edad < 30:
    print("Pertenece a la categoria: adulto joven")

else:
    print("Pertenece a la categoria: adulto")


#punto 5

contraseña = input("ingrese una contraseña: ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#punto 6

import random
import statistics

numeros_aleatorios = [random.rendint(1, 100) for i in range(50)]

media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
moda = statistics.mode(numeros_aleatorios)

print("Lista de numeros: ", numeros_aleatorios)
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

if media > mediana > moda:
    print("La distribucion tiene sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("La distribucion tienen sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("La distribucion no tiene sesgo")
else: 
    print("no se cumple exactamente ninguna de las condiciones de sesgo")


#punto 7

palabra = input("Ingrese una frase o palabra: ")

if palabra [-1].lower() in "a, e, i, o, u":
    palabra += "!"

print( palabra)


#punto 8

nombre = input("ingrese su nombre: ")

opcion = int(input("""ingrese el numero de la opcion que desee
1, Mayusculas
2, Minusculas
3, Primera letra mayusculas
opcion:  """))

if opcion == 1: 
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())

else:
    print("opcion invalida")


#punto 9 

magnitud = float(input("ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5: 
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
else: 
    print("Extremo")


#punto 10

hemisferio = input("en que hesmiferio se encuentra, (norte) o (sur): ").upper()
mes = int(input("ingrese el mes (1-12): "))
dia = int(input("ingrese el dia: "))

fecha = (mes, dia)

if (fecha >= (12, 21)) or (fecha <= (3, 20)):
    estacion = print("Invierno") if hemisferio == "norte" else "Verano"
elif (fecha >= (3, 21)) and (fecha <= (6, 20)):
    estacion = print("Primavera") if hemisferio == "norte" else "Otoño"
elif (fecha >= (6, 21)) and (fecha <= (9, 20)):
    estacion = print("Verano") if hemisferio == "norte" else "Invierno"
else:  # (21 sep - 20 dic)
    estacion = print("Otoño") if hemisferio == "norte" else "Primavera"

print(f"En el hemisferio {hemisferio}, de la fecha {dia}/{mes} es {estacion}.")