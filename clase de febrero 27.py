"""
# Problema 1
#calcular el promedio de una lista de notas mediante el total o la suma de calificacione de calificaciones
calificaciones = [12,33,59,70,86,99]
totalCalificaciones = sum(calificaciones)
numcalificaciones = len(calificaciones)
promedio = totalCalificaciones / numcalificaciones
print("El promedio de estas calificaciones es: ", promedio)
#problema 2
Calcular el numero mas grande


numeros = [12, 55, 89, 90]
numero_mas_grande = numeros[0]

for numero in numeros:
    if numero> numero_mas_grande:
        numero_mas_grande= numero 

print(numero_mas_grande)

#problema 3
#eliminar elementos duplicados en una lista

duplicados = [1,1,4,4,5,5,7,8,9,99,43,23,12,43]
numeroRepetido = duplicados[0]
cont = 0

for numero in duplicados:
    for numero2 in duplicados:
        if numero == numero2:
            cont =cont+1
            if cont >= 2:
                duplicados.remove(numero)
    cont = 0

print(duplicados)

#Problema 4
#calcular la longitud minima de ambas listas entre las dos
lista_1 = [1,2,3,4,5]
lista_2 = ['a', 'b', 'c', 'd', 'e','f']

length_1 = len(lista_1)
length_2 = len(lista_2)

if  length_1 < length_2 :
   print("La longitud minima es: ", length_1)
else:
   print("La longitud minima es: ", length_2)

#otra opcion

lista_1 = [1,2,3,4,5]
lista_2 = ['a', 'b', 'c', 'd', 'e','f']

length_1 = len(lista_1)
length_2 = len(lista_2)


length_lista_minimum = (min(length_1,length_2))
print(f"la longitud menor es {length_lista_minimum}")
"""
#problema 5
"""
nombres = ('pepa', ' micky', 'pinocho')
autores = ('fulanito', 'peranito', 'sultanito')
año = ( 2001, 2019, 2013)
for i in range(len(autores)):
    print  ("Titulo: ", nombres[i], ",Autor: ",autores[i], ",Año: ",año[i],)"""

#lista de cadenas
cadenas = ["manzana", "pera", "banana", "naranja"]
#sort.() ordena una lista en orden alfabetico
cadenas.sort()
#print(cadenas)

cadenas = ["Manzana", "MANZANA", "manZana", "manzana","manzanA", "PERA", "Pera", "pEra", ]
"""sorted(variable) se encarga de organizar una lista teniendo como prioridad lo siguiente:
1.palabras completamente en mayusculas
2.palabras con mayusculas yendo en orden(primero hacia ultimo)
3.palabras con minusculas 
NOTA: Si hay varias palabras con las mismas condiciones se tendera a ir en orden alfabetico
sorted(cadenas)
print(sorted(cadenas))