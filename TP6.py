# actividad 1

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

# actividad 2

def saludar_usuario(nombre):
    return f"hola{nombre}"

nombre = input("ingrese su nombre: ")
print(saludar_usuario(nombre))

# actividad 3

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

# actividad 4 

def calcular_area_circulo(radio):
    return pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * pi * radio

radio = float(input("Ingrese el radio del círculo: "))
print(f"El área del círculo es {calcular_area_circulo(radio)} y el perímetro es {calcular_perimetro_circulo(radio)}")

# actividad 5

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese la cantidad de segundos: "))
print(f"La cantidad de horas es {segundos_a_horas(segundos)}")

# actividad 6

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un número: "))
tabla_multiplicar(numero)

# actividad 7 

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
resultado = operaciones_basicas(a, b)
print(f"La suma de {a} y {b} es {resultado[0]}")
print(f"La resta de {a} y {b} es {resultado[1]}")
print(f"La multiplicación de {a} y {b} es {resultado[2]}")
print(f"La división de {a} y {b} es {resultado[3]}")

# actividad 8 

def calcular_imc(peso, altura):
    return peso / altura ** 2

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
print(f"Su índice de masa corporal es {calcular_imc(peso, altura)}")

# actividad 9

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
print(f"La temperatura en grados Fahrenheit es {celsius_a_fahrenheit(celsius)}")

# actividad 10

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))
print(f"El promedio de {a}, {b} y {c} es {calcular_promedio(a, b, c)}")