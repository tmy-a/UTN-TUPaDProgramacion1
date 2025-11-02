# activida 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

# actividad 2

precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1500,
    'Pera': 2300
}

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

# actividad 3

precios_frutas = {
    'Banana': 1330,
    'Ananá': 2500,
    'Melón': 2800,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1700,
    'Pera': 2300
}

print(list(precios_frutas.keys()))

# actividad 4

def cargar_contactos():
    contactos = {}
    for _ in range(5):
        nombre = input('Ingrese el nombre del contacto: ')
        numero = input(f'Ingrese el numero de {nombre}: ')
        contactos[nombre] = numero
    return contactos

def consultar_contacto(contactos):
    nombre = input('Ingrese el nombre del contacto: ')
    if nombre in contactos:
        print(f'El numero de {nombre} es {contactos[nombre]}')
    else:
        print('El contacto no existe')

contactos = cargar_contactos()
consultar_contacto(contactos)

# actividad 5

def palabras_unicas(frase):
    return set(frase.split())

def recuento_palabras(frase):
    recuento = {}
    palabras = frase.split()
    for palabra in palabras:
        recuento[palabra] = palabras.count(palabra)
    return recuento

frase = input('Ingrese una frase: ')
print(palabras_unicas(frase))
print(recuento_palabras(frase))

# actividad 6

def cargar_alumnos():
    alumnos = {}
    for _ in range(3):
        nombre = input('Ingrese el nombre del alumno: ')
        notas = []
        for nota_idx in range(3):
            notas.append(int(input(f'Ingrese la nota {nota_idx + 1} de {nombre}: ')))
        alumnos[nombre] = notas
    return alumnos

def calcular_promedio(notas):
    return sum(notas) / len(notas)

def mostrar_promedio_alumnos(alumnos):
    for nombre, notas in alumnos.items():
        print(f'El promedio de {nombre} es {calcular_promedio(notas)}')

alumnos = cargar_alumnos()
mostrar_promedio_alumnos(alumnos)

# actividad 7

parcial_1 = {7, 5, 2, 4, 9}
parcial_2 = {1, 5, 3, 7, 8}

print('Los que aprobaron ambos parciales:', parcial_1.intersection(parcial_2))
print('Los que aprobaron solo uno de los dos:', parcial_1.symmetric_difference(parcial_2))
print('La lista total de estudiantes que aprobaron al menos un parcial:', parcial_1.union(parcial_2))

# actividad 8

stock = {
    'Leche': 25,
    'Queso': 15,
    'Yogurt': 27
} # stock de 3 productos lácteos 

def consultar_stock(stock):
    
    producto = input('Ingrese el nombre del producto: ')
    if producto in stock:
        print(f'El stock de {producto} es {stock[producto]}')
    else:
        print('El producto no existe')

def agregar_stock(stock):
    producto = input('Ingrese el nombre del producto: ')
    unidades = int(input(f'Ingrese la cantidad de unidades a agregar: '))
    stock[producto] = stock.get(producto, 0) + unidades
    return stock

def main():
    while True:
        print("""
1. Consultar stock
2. Agregar stock        
3. Salir
""")
        opcion = int(input('Ingrese la opcion: '))
        match opcion:
            case 1:
                consultar_stock(stock)
            case 2:
                agregar_stock(stock)
            case 3:
                break

main()

# actividad 9 

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}

dia = input('Ingrese el dia: ')
hora = input('Ingrese la hora: ')
evento = agenda.get((dia, hora), 'No hay evento en ese dia y hora')
print(evento)

# actividad 10 

original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {}

for pais, capital in original.items():
    invertido[capital] = pais

print(invertido)
