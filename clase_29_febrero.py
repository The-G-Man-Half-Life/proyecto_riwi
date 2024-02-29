# ingreesar info
#calcular el totla de la factura 
#imprimir info y calculo

name = input("ingresa tu nombre") # name = ju
last_name = input("ingrese su apellido") # last_name = la
credentialsId= input("ingresa tu id") #credentrialId = 3

products={}

def calcular_factura(name, last_name, credentialsId):
    while True:
        print("elige la opcion")
        print("1. añadir producto")
        print("2. generar factura")
        option = input("opcion: ")
        if option == "1":
            #añadir producto
            addProduc= input("add name product")
            addPrice= input("add price product")
            products[addProduc]=int(addPrice)
        elif option == "2":
            #generar factura
            print("MERCADO MATEOS")
            print(f"Nombre : {name}")
            print(f"Apellido :{last_name}")
            print("ID :",credentialsId)
            print("productos: ", products.keys())
            totalNoIva= sum(products.values())
            print("total sin iva", totalNoIva)
            totalSiIva = totalNoIva + totalNoIva*0.19
            print("total con iva", totalSiIva)
            print("products", len(products))
            if  (3<=len(products) < 5):
                subtotal_caso1 = totalSiIva - totalSiIva * 0.05
                print("caso 1", subtotal_caso1)
            elif (5<=len(products) < 7):
                subtotal_caso2 = totalSiIva - totalSiIva*0.10
                print("caso 2", subtotal_caso2)
            elif (7<=len(products)):
                print("obtuviste un bono de 100k")
            break
    return
            
                    
calcular_factura(name, last_name, credentialsId)

#logica de descuentos

    
    
    
  