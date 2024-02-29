#Ejercicio 1 - Modulo 1 - Filtro 1

"""Desarrolle un programa que permita a un usuario ingresar informacion sobre varios productos comprados por un cliente.
 El programa debe calcular el total de la factura, aplicar descuentos y mostrar el recibo detallado de la compra."""

#Este funcion se encarga de organizar los datos del usuario y almacenarlos dentro de una lista para luego imprimirlos
def datos (nombre_input, apellidos_input, documentos_input):
    #lista donde se almacenan
    Datos_usuario = []
    #almacenart datos en lista
    Datos_usuario.append(nombre_input)
    Datos_usuario.append(apellidos_input)
    Datos_usuario.append(documentos_input)
    #imprimir datos
    a = print(f"Bienvenido: {Datos_usuario[0]} {Datos_usuario[1]} \nCon documento:{Datos_usuario[2]}")
    return   a

#funcion para mostrar los productos
Lista_productos = {'peluche' : 100000, 'drone' : 250000, 'ak_juguete': 400000 }
def productos (decision):
    
    mostrar = print(Lista_productos.items()) if decision == True  else None 
    return mostrar

#funcion para sumar precio de los productos
productos_del_usuario = []
def sumar_precios_productos ():
     producto_a = input("Ingrese el nombre del producto que desea comprar")
     productos_del_usuario.append(starter)
     decision_2 = input("Desea ingresar mas productos")
     decision_2.lower()

     

#mostrar opciones
def menu_opciones(bool):
    lista_opciones = {'(1)':'Volver a registrar el documento, nombres, apellidos de usted',
                      '(2)':'Registrar un nuevo producto a la factura',
                      '(3)':'Listar productos actuales en la factura',
                      '(4)':'Mostrar factura' }
    if bool ==True:
        print("Que desea hacer")

        lista_opciones = {'(1)':'Volver a registrar el documento, nombres, apellidos del cliente','(2)':'Registrar un nuevo producto a la factura','(3)':'Listar productos actuales en la factura','(4)':'Mostrar factura' }
    
    print(lista_opciones.items())

    decision = int(input("Escriba el numero de la opcion que desee realizar"))
    return decision

print(menu_opciones)




"""if decision == 1:
    nombre = input("ingrese su nombre: ")
    apellido = input("ingrese su apellido: ")
    documento = input("ingrese su documento: ")
    a = datos(nombre, apellido, documento)
    print(a)

elif  decision ==2:
    acceso = True
    print(productos(acceso))

elif decision ==3:"""

"""def caso_1 ():def caso_2 ():def caso_3 ():def caso_4productos"""