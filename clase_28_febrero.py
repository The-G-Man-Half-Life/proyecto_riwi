#ejemplos

"""#ejemplo1
suma_sin_funciones = 3+4
print(suma_sin_funciones)


def sumar_numeros_encapsulados(a,b):
    sumar = a+b
    return sumar

#llamado a la funcion
resultado = sumar_numeros_encapsulados(3,4)
print("El resultado de la suma es : ", resultado)





#ejemplo2
lista_numeros = [1,2,3,4,5]
suma = sum(lista_numeros)

def sumar_numeros_encapsulados(lista):
    resultado = sum(lista)
    return resultado

#Llamado a la funcion
lista_notas = [3,5,4,3,4,5,5]
resultado_lista = sumar_numeros_encapsulados(lista_notas)
print("la suma de la lista es: ", resultado_lista)
"""
#ejemplo3
"""
def calcular_promedio(numeros):
    promedio = sum(numeros)/len(numeros)
    return promedio

#llamado a la funcion
lista_aleatoria = []
peticion = input(str("Desea ingresar mas numeros (si/no):"))
x =peticion.lower()
while x == "si":
    insercion_numeros = int(input("Ingrese un numero entero: "))
    lista_aleatoria.append(insercion_numeros)
    peticion = input("Desea ingresar mas numeros: ")
    x =peticion.lower()
if x == "no":
    promedio_lista_aleatoria = calcular_promedio(lista_aleatoria)
    print("El promedio de la lista aleatoria es:", promedio_lista_aleatoria)
    """
"""
#ejemplo4
def contar_cantidad_palabras(frase):
    palabras= frase.split()
    cantidad_palabras = len(palabras)
    return cantidad_palabras

#Ejempl0 de uso de la funcion
texto = "Esta es una cadena de ejemplo para contar palabras"
cantidad = contar_cantidad_palabras(texto)
print ("La cantidad de palabras en la frase es:", cantidad)

#ejemplo5

lista = ('Mateo Montoya Ospina')

contador = {}
def contar_cantidad_caracteres(nombre):
    for caracter in nombre:
        if caracter not in contador:
            contador[caracter]=1
        else:
            contador[caracter]+=1

#funcion para generar palindromo
def es_palindromo(cadena):
    cadena_inicial = cadena
    cadena = cadena.lower().replace(' ', '') #pasa la cadena a minusculas y elimina los espacios
    decision = print(f"{cadena_inicial}: es palindromo") if cadena ==cadena[::-1] else print(f"{cadena_inicial}: no es palindromo")
    return decision

palabra1 = "Hola world"
palabra2 = "Anita lava la tina"
es_palindromo[palabra1]
es_palindromo[palabra2]

#problema 4
def pedir_documentos(nombre,informacion):
    nombre_1 = nombre
    informacion_1 = informacion
    informacion_documento = []
    informacion_documento.append({nombre_1:informacion_1})
    return print(informacion_documento)

pedir_nombre = input ("dele nombre a su archivo:")
pedir_informacion = input("agrege la informacion a su archivo:")
guardado_informacion_documento = pedir_documentos(pedir_nombre,pedir_informacion)

#sobre los diccionarios


#un diccionario es una estructura de datos que permite almacenar pares clave-valor
mi_diccionario = {'nombre':'juan', 'edad':30, 'ciudad':'Madrid'}

#acceder a un valor utilizando una clave
print(mi_diccionario['nombre'])

#agregar una nueva clave-valor
mi_diccionario['ocupacion'] = 'ingeniero'

#modificar un valor existente
mi_diccionario['edad'] = 31

#eliminar una clave-valor
del mi_diccionario['ciudad']

print(mi_diccionario)

#Metodos de los diccionarios

#dict.items():Devuelve una vista a los  items del diccionario como (pares clave-valor)
#dict.values():Devuelve una vista a los valores del diccionario
#dict.keys():Devuelve una vista de las claves del diccionario
#dict.clear():Elimina todos los elementos del diccionario
#len(dict): devuelve la cantidad de elementos (pares clave-valor) en el diccionario
mi_diccionario = {'nombre':'juan', 'edad':30, 'ciudad':'Madrid'}
print (mi_diccionario.items())
print ( mi_diccionario.values())
print (mi_diccionario.keys())
print (len(mi_diccionario))
print(mi_diccionario.clean())

#agregar cifras decimales
valor = float(30.001)

#problema1: calcular"""