import random
#ejercicio sobra variables y tipos de datos
#ejercicio1
"""Nombre = "Mateo Montoya Ospina"""
#ejercicio2
"""Edad = 17
Peso = 50,"kg"
Altura = 1.70,"meters"""
#ejercicio3
"""radio = int(input("ingrese el radio del circulo a calcular: "))
areaCirculo = radio*radio
print(f"el area de su circulo es: {areaCirculo} ")"""
#ejercicio4
"""Farenheit = "Farenheit" or "farenheit"
Celsius = "Celsius" or "celsius"
tipo_temperatura = input("ingrese el tipo de temperatura a convertir(Farenheit o Celsius): ")
valor = float(input("ingrese el valor: "))

if tipo_temperatura == Farenheit:
    ecuacion_farenheit_celsius = (valor-32)/(1.8)
    print(f"Este es valor en grados Celsius: {ecuacion_farenheit_celsius}°C")
else:
    ecuacion_celsius_farenheit = (valor*1.8)+32
    print(f"Este es el valor en grados Farenheit: {ecuacion_celsius_farenheit}°F")"""
#ejercicio5
"""hora = int(input("Escriba la hora actual (en formato militar): "))
minuto = int(input("escriba el minuto actual: "))
sol = ((hora in range(6,16))) or (hora == 17 and minuto in range(0,31))
if sol == True:
    print("Aun hay sol, salte de la pc y toca cesped")
else:
    print("Hay luna, no salgas que te asaltan los malandros")"""

#ejercicio6
"""cadena1 = input("Ingrese una palabra u oracion: ")
cadena2 = input("ingrese otra palabra u oracion: ")
union_cadenas = cadena1 + cadena2
print(f"Su nueva oracion es: {union_cadenas}")"""
#ejercicio7
"""num1 =float(input("Escriba un numero cualquiera: "))
num2 = float(input("Escribe otro numero cualquiera: "))
#suma
suma = num1 + num2
print(f"La suma de {num1} y {num2} es: {suma}")
#resta
resta = num1-num2
print(f"La diferencia de {num1} y {num2} es: {resta} ")
#multiplicacion
multiplicacion = num1*num2
print(f"La multiplicacion entre {num1} y {num2} es: {multiplicacion}")
#division
division = num1/num2
residuo = num1%num2
print( f"El resultado de la division entre {num1} y {num2} es: {division}")
print(f"Su residuo fue: {residuo}")"""
#ejercicio8
"""num3 = int(input("Escribe un numero cualquiera: "))
num3 = "No ese :/"
print(num3)"""
#ejercicio9
"""nombre_random = input("Escriba su nombre")"""
#ejercicio10
"""nombres_normales = ["Isabella", "Olivia", "Alexis", "Sofía", "Victoria", "Amelia", "Alexa", "Julia"
"Camila","Alexandra"]
print(nombres_normales[0])"""
#ejercicio11
"""num5 = int(input("Escriba el primer numero: "))
num6 = int(input("Escriba el segundo numero: "))
num7 = int(input("Escriba el tercer numero: "))
promedio = (num5 + num6 + num7)/(3)
print ("El promedio de los tres numeros es: ", promedio)"""
#ejercicio12
"""lista = ["aguacate","tamarindo","masamorra", "bandeja paisa"]
union_elementos_lista = f"{lista[0]}  {lista[1]}  {lista[2]}  {lista[3]}"
print(union_elementos_lista)"""
#ejercicio13
"""tupla_tactica = ('Azul', 'Rojo', 'Verde', 'Amarillo', 'Negro')
print(tupla_tactica[2])"""
#ejercicio14
"""num8 =int(input("Escriba el primer numero a comparar: "))
num9 =int(input("Escriba el segundo numero a comparar: "))
if num8 == num9:
    print("Ambos numeros son iguales")
elif num8<num9:
    print(f"{num8} es menor comparado a {num9}")
else:
    print(f"{num9} es menor comparado a {num8}")"""
#ejercicio15
"""Mi_variable = None
print(type(Mi_variable))"""
#ejercicios para identificar tipos de datos
#ejercicio1
"""nombre = "ejemplo"
print(type(nombre))"""
#ejercicio2
"""lista_numerica = [1,2,3,4,5]
print(type(lista_numerica))"""
#ejercicio3 y ejercicio4
"""lista = [1,1.2,2,2.3]
random_number_choice = random.choice(lista)
random_number= type(random_number_choice)
class_float = random_number==float
class_int = random_number==int
if class_float:
    print("El numero ",random_number_choice, " es decimal o clase float")
elif class_int:
    print("El numero ", random_number_choice, " es entero o clase int")"""

#ejercicio5
"""dato_1 =('aguacate', 1,2,3, 'palta')
choice_dato = type(random.choice(dato_1))
print("Lo que escribiste es un tipo: ",choice_dato)"""
#ejercicio6
"""entrada = input("Hola: ")
if len(entrada) == 0:
   print("No hay texto")
else:
   print("Adios")
#ejercicio7"""

#ejercicio8
"""input_usuario = input(("Decida palta o aguacate: " ))
verificacion_decision = input_usuario== "aguacate" or "Aguacate"==True
print("Su decision es: ", verificacion_decision)"""

#ejercicio9
"""variable_aleatoria = input("Escriba nada: ")
variable_aleatoria = None
print(type(variable_aleatoria))"""
#ejercicio10

#ejercicio11
#ejercicio12
#ejercicio13
#ejercicio14
#ejercicio15
