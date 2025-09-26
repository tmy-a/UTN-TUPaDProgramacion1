#punto 1 - lista de notas
notas = [4, 5, 6, 2, 3, 8, 9, 10, 7.5, 8]
print("las notas de los estudiantes son: ", notas)
promedio = sum (notas)/len(notas)
print("El promedio de todas las notas es de: ", promedio)
print(f"la nota mininma es {min(notas)} y la maxima es{max(notas)}")



#punto 2 - 5 productos en una lista
productos = []
cantidad = 5
for i in range(cantidad):
producto = input(f"ingrese producto({i + 1}): ")
productos.append(producto.title())

productos = sorted(productos)
print("los productos ingresados son:", ', '.join(productos))
prod_eliminar = input("ingrese el producto a eliminar: ").title()
productos.remove(prod_eliminar)
print("los productos ahora son:", ', '.join(productos))



#punto 3 - 
from random import randint

numeros = []
cantidad = 15
pares = []
impares = []

for _ in range(cantidad):
    numeros.append(randint(1, 100))

for idx in range(len(numeros)):
    numero = numeros[idx]
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print('Lista de numeros: ', numeros)
print(f'Pares ({len(pares)}): ', pares)
print(f"Impares ({len(impares)}):" , impares)



#punto 4 - lista valores repetidos
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
nuevos_datos = []

for dato in datos:
    if not (dato in nuevos_datos):
        nuevos_datos.append(dato)

print('Los datos son:', nuevos_datos)



#punto 5 - listas con 8 nombres
estudiantes = ["Tomas", "Ivan", "Axel", "Valentina", "Gino", "Patricio", "Aram", "Tobias"]

print("Los estudiantes de la comision 01 de UTN TUPaD 2025 son:", ', '.join(estudiantes))

operacion = int(input('Queres agregar un nuevo estudiante (1) o eliminar uno existente (2)?: '))

if operacion == 1:
    estudiante = input('Nombre de estudiante nuevo: ')
    estudiantes.append(estudiante)
elif operacion == 2:
    estudiante = input('Nombre de estudiante a eliminar: ')
    if estudiante in estudiantes:
        estudiantes.remove(estudiante)
    else:
        print("No existe el estudiante")
else:
    print("Operacion invalida")

print("Los estudiantes de la comision Z de UTN TUPaD 2025 son:", ', '.join(estudiantes))



#punto 6 - lista con 7 numeros, rotar elementos
numeros = [1, 2, 3, 4, 5, 6, 7]
nuevos_numeros = []
rotacion_cantidad = -1

for idx in range(rotacion_cantidad, len(numeros) + rotacion_cantidad):
   nuevos_numeros.append(numeros[idx])

print('Lista antes:', numeros)
print('Lista despues:', nuevos_numeros)
      


#punto 7 - matriz 7x2 temperatura
temperatura = [
    [10 , 20],
    [12, 22],
    [8, 18],
    [15, 25],
    [11, 19],
    [9, 17],
    [13, 23]
]

minimas = [fila[0] for fila in temperatura]
maximas = [fila[1] for fila in temperatura]

prom_min = sum(minimas)/len(minimas)
prom_max = sum(maximas)/len(maximas)

amplitudes = [fila[1]- fila[0] for fila in temperatura]
dia_mayor_amplitud = amplitudes.index(max(amplitudes))+1
print("el dia con mayor amplitud es: " , dia_mayor_amplitud)



#punto 8 - matriz de notas
notas =[
    [2, 3, 4],
    [6, 5, 7],
    [7, 9, 8],
    [5, 3, 7],
    [1, 2, 7]

]
print("notas de estudiantes: ")
for fila in notas:
    for nota in fila:
        print(nota, end=" ")
    print()

print("promedio de cada estudiante")

for i in range(5):
    suma = 0 
    for j in range(3):
        suma += notas [i][j]
    promedio = suma / 3
    print(f"estudiante{i + 1}: {promedio}")

for j in range(3):
    suma = 0
    for i in range(5):
        suma += notas[i][j]
    promedio = suma / 5
    print(f"promedio materia {j + 1}: {promedio}")



#punto 9 - tablero TaTeTi
tablero = []

for i in range (3):
    fila = []
    for j in range(3):
        fila.append("-")
        tablero.append(fila)

for fila in tablero: 
    for celda in fila:
        print(celda, end= " ")
        prin()

jugador = "X"
jugadas = 0
#sistema de turnos
while jugadas < 9:
    print(f"\nTurno del jugador {jugador}")
    
    fila = int(input("ingrese la fila (0-2): "))
    columna = int(input("ingrese la columna (0-2): "))

    if fila<0 or fila>2 or columna<0 or columna>2:
        print("Posicion fuera de rango. Intenta de nuevo")
        continue
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
        jugadas +=1
    else: 
        print("casilla ocupada. Intente nuevamente.")
        continue

    for fila in tablero: 
    for celda in fila:
        print(celda, end= " ")
        prin()

    if jugador == "x":
        jugador = "O"
    else: 
        jugador = "x"



#punto 10 - registrar ventas
ventas = [
    [40, 50, 30, 10],
    [20, 25, 16, 90],
    [0, 20, 80, 1],
    [90, 3, 4, 6],
    [4, 6, 0, 50],
    [1, 2, 70, 4],
] 

totales_prod = []
for i in range(4):
    total_prod = 0
    for j in range(7):
        total_prod += ventas [i][j]
    totales_prod.append(total_prod)
    print(f"producto {i + 1}: {total_prod}")

#mostrar los dias con mayor ventas
mayor_ventas = 0
dia_mayor = 0

for j in range(7):
    totaldia+ 0 
for i in range(4):
    total_dia += ventas [i][j]
    print(f"total del dia {j +1}: {total_dia}")
    if total_dia > mayor_ventas:
        mayor_ventas = total_dia
        dia_mayor = j
print(f"\nel dia con mayor ventas fue el {dia_mayor+1}, con{mayor_ventas} ventas")

#mas vendido en la semana
mayor_prod = 0
indice_mayor = 0

for i in range(4):
    if totales_prod [i] > mayor_prod:
        mayor_prod = totales_prod [i]
        indice_mayor = i

print(f"\nel producto mas vendido fue el {indice_mayor+1}, con {mayor_prod} ventas en la semana.")