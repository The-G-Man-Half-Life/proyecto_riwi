DatosUsuario_dict = {}
ListaProductos_dict = {}

def DatosUsuario_input ():
    print ("---Ingrese por favor los siguientes datos: ---")
    Nombre = input ("Ingrese su nombre: \n").lower().capitalize()
    Apellidos = input ("Ingrese un apellido: \n").lower().capitalize()
    Id = int((input("Ingrese su ID: \n")))

    DatosUsuario_dict["Nombre"]= Nombre
    DatosUsuario_dict["Apellidos"]=Apellidos
    DatosUsuario_dict["ID"]=Id
    print("")

    global DatosUsuario
    print(DatosUsuario_dict["Nombre"], DatosUsuario_dict["Apellidos"], "con ID:" ,DatosUsuario_dict["ID"])

    print("")

def MenuOpciones():

    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
    print(DatosUsuario_dict["Nombre"], DatosUsuario_dict["Apellidos"], "con ID:" ,DatosUsuario_dict["ID"])
    print ("Escoja una de las siguientes opciones a ejecutar:\n")
    print("---------------------------------------------------------------------")
    print("\n1. Volver a registrar el nombre, documento y apellido.\n")
    print("2. Registrar un nuevo producto a la factura.\n")
    print("3. Listar productos actuales de la factura\n")
    print("4. Mostrar Factura\n")
    print("5. Apagar el sistema\n")

    global opcion
    opcion =  int(input("Ingrese la opcion deseada: "))
    print(" ")

def RegistrarProductos():
    print("")
    print ("Ingrese el nombre del producto que desea comprar: ")
    NombreProducto = input(": \n").lower().capitalize()
    print ("Ingrese el valor del producto: ")
    ValorProducto = int(input(": \n"))

    ListaProductos_dict[NombreProducto]=ValorProducto
    print(" ")

def ListarProductos():
    print ("\n",DatosUsuario_dict["Nombre"], DatosUsuario_dict["Apellidos"], "con ID:" ,DatosUsuario_dict["ID"])
    print("")
    print("Estos son sus productos: \n")

    for a in range(len(ListaProductos_dict)):
        print(a+1,".", list(ListaProductos_dict.keys())[a],": $",list(ListaProductos_dict.values())[a])

def MostrarFactura():
    global TotalFactura
    TotalFactura = sum(ListaProductos_dict.values())
    global AdicionIva
    AdicionIva = (TotalFactura*0.19) + TotalFactura

    print("----Esta es su factura: ----\n")
    print("Gracias por haber comprado en nuestra tienda")
    print("")
    print("Estos son sus productos: \n")
    ListarProductos()
    print("\n---------------TOTAL-----------------")
    print(f" {TotalFactura}$\n")
    print("-----------TOTAL + IVA -----------\n")
    print(f"+19% :{AdicionIva}$ ")
    print(" ")

def ApagarSistema():
    print("Gracias por haber usado nuestro sistema :)")
    global Bandera
    Bandera = False 
    print(" ")

def Caso1():
    SubtotalCaso1 = (AdicionIva * -0.05)+ (AdicionIva)
    print("\nSe le aplica un 5% de descuento\n")
    print("----------Subtotal-----------")
    print(f"${SubtotalCaso1}$")
    print(" ")

def Caso2():
    SubtotalCaso2 = (AdicionIva * -0.1)+ (AdicionIva)
    print("\nSe le aplica un 10% de descuento\n")
    print("----------Subtotal-----------")
    print(f"${SubtotalCaso2}")
    print(" ")

def Caso3():
    print("\n-----------------")
    print("\n Acaba de obtener un bono de $100000 para su proxima compra" )
    print(" ")

def Caso4():
    print("\nNo se le aplicara IVA a su compra\n")
    print("----------Subtotal-----------")
    print(f"${TotalFactura}")
    print(" ")

Bandera = True
print("---Bienvenido a tiendas ama---")
DatosUsuario_input()

while Bandera ==True:
    MenuOpciones()

    if opcion ==1:
        DatosUsuario_input()
    elif opcion ==2:
        RegistrarProductos()
    elif opcion == 3:
        ListarProductos()
    elif opcion ==4:
        MostrarFactura()

        for e in ListaProductos_dict.values():
            if e >= 500000:
                Caso4()
            else:
                pass
        if 5< len(ListaProductos_dict) <=7:
            Caso3()
        elif 5<= len(ListaProductos_dict) <7:
            Caso2()
        elif 3<=len(ListaProductos_dict)<5:
            Caso1()
        else:
            pass
            

    else:
        ApagarSistema()