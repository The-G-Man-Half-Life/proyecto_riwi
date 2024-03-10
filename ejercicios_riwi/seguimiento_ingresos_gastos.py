#Definiendo listas a usar
Nombre_Sueldo = {}
Alimento_dict ={}
Transporte_dict = {}
Vivienda_dict = {}
Entretenimiento_dict ={}
GastosAdicionales_dict = {}

def DatosUsuario():
    Nombre = input("Bienvenido. Ingrese su nombre").lower().capitalize()
    Sueldo = int(input("Ingrese su salario mensual Sin puntos ni comas"))

    Nombre_Sueldo["Nombre"] = Nombre
    Nombre_Sueldo["Sueldo"] = Sueldo
    print("****************************")
    return 
    
def Sueldo_AlimentoDict():
    print("Esta es la zona de gastos de alimentacion")
    while True:
        nombreGastoAlimento = input("Diga el nombre especifico del gasto: ").lower().capitalize()
        PrecioGastoAlimento = int(input("Indique el precio de este gasto: "))
        Alimento_dict[nombreGastoAlimento] = PrecioGastoAlimento
        parar = input("¿Desea ingresar mas gastos?(si/no): ").lower()
        if parar == "si":
            pass
        elif parar == "no":
            break


    TotalGastadoAlimentos = sum(Alimento_dict.values())
    print ("Su total gastado en alimentos es:$",TotalGastadoAlimentos )
    global TotalSueldo1
    TotalSueldo1 = Nombre_Sueldo['Sueldo']-TotalGastadoAlimentos
    print("A su sueldo le quedan  $",TotalSueldo1)
    print("****************************")

def Sueldo_TransporteDict():

    print("Esta es la zona de gastos de Transporte")

    
    while True:

        NombreGastoTransporte = input("Diga el nombre especifico del gasto: ").lower().capitalize()
        PrecioGastoTransporte = int(input("Indique el precio de este gasto: "))

        Transporte_dict[NombreGastoTransporte] = PrecioGastoTransporte

        parar = input("¿Desea ingresar mas gastos?(si/no): ").lower()
        if parar == "si":
            pass
        elif parar == "no":
            break
    

    TotalGastadoTransporte = sum(Transporte_dict.values())
    print ("Su total gastado en alimentos es:$",TotalGastadoTransporte )
    global TotalSueldo2
    TotalSueldo2 = TotalSueldo1-TotalGastadoTransporte
    print("A su sueldo le quedan  $",TotalSueldo2)
    print("****************************")

def Sueldo_ViviendaDict():

    print("Esta es la zona de gastos de Vivienda")

    
    while True:

        nombreGastoVivienda = input("Diga el nombre especifico del gasto: ").lower().capitalize()
        PrecioGastoVivienda = int(input("Indique el precio de este gasto: "))

        Vivienda_dict[nombreGastoVivienda] = PrecioGastoVivienda

        parar = input("¿Desea ingresar mas gastos?(si/no): ").lower()
        if parar == "si":
            pass
        elif parar == "no":
            break
    

    TotalGastadoVivienda = sum(Vivienda_dict.values())
    print ("Su total gastado en alimentos es:$",TotalGastadoVivienda )
    global TotalSueldo3
    TotalSueldo3 = TotalSueldo2-TotalGastadoVivienda
    print("A su sueldo le quedan  $",TotalSueldo3)
    print("****************************")

def Sueldo_EntretenimientoDict():

    print("Esta es la zona de gastos de Entretenimiento")

    while True:

        nombreGastoEntretenimiento = input("Diga el nombre especifico del gasto: ").lower().capitalize()
        PrecioGastoEntretenimiento = int(input("Indique el precio de este gasto: "))

        Entretenimiento_dict[nombreGastoEntretenimiento] = PrecioGastoEntretenimiento

        parar = input("¿Desea ingresar mas gastos?(si/no): ").lower()
        if parar == "si":
            pass
        elif parar == "no":
            break
    
    TotalGastadoEntretenimiento = sum(Entretenimiento_dict.values())
    print ("Su total gastado en entretenimiento es:$",TotalGastadoEntretenimiento )
    global TotalSueldo4
    TotalSueldo4 = TotalSueldo3-TotalGastadoEntretenimiento
    print("A su sueldo le quedan  $",TotalSueldo4)
    print("****************************")

def Sueldo_GastosAdicionalesDict():


    print("Esta es la zona de gastos de Adicionales")

    
    while True:

        nombreGastoGastoA = input("Diga el nombre especifico del gasto: ").lower().capitalize()
        PrecioGastoGastoA = int(input("Indique el precio de este gasto: "))

        GastosAdicionales_dict[nombreGastoGastoA] = PrecioGastoGastoA

        parar = input("¿Desea ingresar mas gastos?(si/no): ").lower()
        if parar == "si":
            pass
        elif parar == "no":
            break
            
        

    TotalGastadoGastoA = sum(GastosAdicionales_dict.values())
    print ("Su total en gastos adicionales es:$",TotalGastadoGastoA )
    global TotalSueldo5
    TotalSueldo5 = TotalSueldo4-TotalGastadoGastoA
    print("A su sueldo le quedan  $",TotalSueldo5)
    print("****************************")

#Se llaman a las funciones
apagado = True
while apagado ==True:
    DatosUsuario()
    Sueldo_AlimentoDict()
    Sueldo_TransporteDict()
    Sueldo_ViviendaDict()
    Sueldo_EntretenimientoDict()
    Sueldo_GastosAdicionalesDict()

    if TotalSueldo5 < 0:
        print("Estas gastando mas de lo que ganas")
        print("Te desfalcaste por:",abs(TotalSueldo5))
        apagado =False
    else:
        print("Has hecho un buen manejo de los gastos")
        apagado = False