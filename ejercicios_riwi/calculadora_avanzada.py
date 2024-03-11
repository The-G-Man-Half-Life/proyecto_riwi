#definir la operacion a realizar
#pedir un primer numero en float
#pedir un segundo numero en float


def menu_operaciones():
    print ("Bienvenido a la calculadora avanzada\n")

    print("Estas son sus opciones: ")
    print("1. Suma\n"
          "2. Resta\n"
          "3. Multiplicacion\n"
          "4. Division")

    global opcion
    opcion = int(input("Ingrese la opcion deseada: "))