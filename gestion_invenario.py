#crear carpetas para: nombre producto, precio unitario producto y cantidad disponible en el inventario
nombre_cantidad_producto = {}
precio_unitario_producto = []

#crear funcion para hacer funcionar todo
def agregar_productos ():
    while True:

        #Esta parte muestra las opciones del usuario para que hacer en la lista
        print("Estas son sus opciones: ")
        print("1. Agregar un nuevo producto al inventario")
        print("2. Actualizar la cantidad de producto en el inventario")
        print("3. Eliminar un producto del inventario")
        print("4. listar todos los productos en el inventario")
        print("5. Verificar si hay un producto especifico en el inventario")

        option = int(input("Ingrese el numero de la opcion: "))#Esta opcion recoge la decision como un inr que sera reconocida por los if y elif

        #se recoge la info del elemento a añadir al diccionario(nombre_cantidad_producto) y a la lista (precio_unitario_producto)
        if option ==1:
            print ("Ingrese por favor el nombre de su producto: ")
            nombre_producto = input(": ")

            print ("Ingrese la cantidad de producto")
            cantidad_producto = input(": ")
                
            print("ingrese el precio unitario del producto")
            precio_producto = int(input(": "))

                
            nombre_cantidad_producto[nombre_producto]=cantidad_producto
            precio_unitario_producto.append(precio_producto)

        #se muestran los elemntos en la lista al usuario para que decida cual cantidad de cual producto cambiar
        elif option == 2:
            print(nombre_cantidad_producto.items())
            producto_cambiar_cantidad = input("Ingrese el nombre del producto:" )
            for a in nombre_cantidad_producto.keys():
                if a == producto_cambiar_cantidad:
                    nueva_cantidad = (input("ingrese la nueva cantidad del producto: "))
                    nombre_cantidad_producto[producto_cambiar_cantidad]=nueva_cantidad
                
                #si no esta ese elemento se hace nada
                else:
                    None

        #aqui se pregunta por el producto a eliminar y se elimina de la lista al igual que al valor al cual se compara
        elif option == 3:
            print(nombre_cantidad_producto.keys())
            print(nombre_cantidad_producto.values())
            print(precio_unitario_producto)
            producto_eliminar = input ("Ingrese el nombre del producto a eliminar: ")
            del nombre_cantidad_producto[producto_eliminar]
            precio_eliminar = int(input ("Ingrese el precio del producto(aquel que esta en el mismo orden del objeto) "))
            for n in precio_unitario_producto:
                precio_unitario_producto.pop(precio_eliminar)
            
        #aqui se muestra los elementos de la lista de manera ordenada en formato vertical
        elif option == 4:
            for d in nombre_cantidad_producto:
                print("nombre del producto: ",nombre_cantidad_producto.keys())
                print("cantidad del producto: ",nombre_cantidad_producto.values())
                print("precio del producto en unitario ",precio_unitario_producto)
                break
                        
        #Aqui se verifica elemento por elemento del diccionario de productos para encontrar si esta presente o no
        elif option == 5:
            producto_encontrar = input("Ingrese el nombre del producto que desea encontrar: ")
            for e in nombre_cantidad_producto.keys():
                if e == producto_encontrar:
                    print("El producto: ", producto_encontrar, " esta en la lista")
           
#se llama a la funcion
agregar_productos()