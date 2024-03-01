# ingresar info
print("-----Bienvenido a tiendo D2-----\n")
print("-----Mejor que tiendas D1-----\n")

def  leer_datos():
    print("Ingrese su nombre")
    name = input(": \n") 
    print("ingrese su apellido: ") 
    last_name = input(": \n")
    print("ingresa tu id: ") 
    credentialsId= input(": \n") 
    


products={}

#calcular el total de la factura 
def calcular_factura():
    while True:
        leer_datos()
        print("***Elige una opcion:*** ")
        print("\n1. Cambiar sus datos")
        print("2. Agregar un producto nuevo a la factura")
        print("3. añadir producto")
        print("4. Generar factura")
        print("5. Apagar programa\n")


        option = input("opcion: ")
        if option == "1":
            print("Ingrese su nombre")
            name1 = input(": \n") 
            print("ingrese su apellido: ") 
            last_name1 = input(": \n")
            print("ingresa tu id: ") 
            credentialsId1 = input(": \n") 
            leer_datos(name1,last_name1,id)

        elif option == "2":
            #añadir producto
            print("-----------------------------------------------")
            addProduct= input("\nEscribe el nombre del producto: ")
            addPrice= input("Añade el precio del producto: \n")
            products[addProduct]=int(addPrice)

            
        elif option == "4":

            #checar valor producto para caso 4
            for i in products.values():
                if i == 500000:
                    productoEspecial = True
                else:
                    productoEspecial = False
            #generar factura
            print("------MERCADO MATEOS------")
            print(f"Nombre : {name}")
            print(f"Apellido :{last_name}")
            print("ID :",credentialsId)
            print("productos: ", products.keys())
            totalNoIva= sum(products.values())
            print("total sin iva", totalNoIva)
            totalSiIva = totalNoIva + totalNoIva*0.19
            print("total con iva", totalSiIva)
            print("products", len(products))

            if productoEspecial==True :
                print("El Total de su producto es: ",totalNoIva)

            elif (7<=len(products)):
                print("obtuviste un bono de 100k")

            elif (5<=len(products) < 7):
                subtotal_caso2 = totalSiIva - totalSiIva*0.10
                print("caso 2", subtotal_caso2)

            elif  (3<=len(products) < 5):
                subtotal_caso1 = totalSiIva - totalSiIva * 0.05
                print("caso 1", subtotal_caso1)
            
            break
    return
            
                    

calcular_factura()