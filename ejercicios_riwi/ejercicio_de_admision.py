experiencia_laboral = {}
empresas_trabajadas = {}
lenguajes_programacion = {}
idiomas = {}
edad = {}
id = {}
email = {}
color = {}
pais_origen = {}
eleccion = {}

def ingreso():
    print("Bienvenido a la seleccion de candidatos")
    print(" ")
    global Nombre
    Nombre = input("Ingrese su nombre completo: ").lower().capitalize()
    print("****************************")
def experiencia_laboral_():
    años_experiencia = int(input("Por favor ingrese los años de experiencia laboral que posee:"))
    
    experiencia_laboral[Nombre] = años_experiencia
    print("****************************")
def empresas_trabajadas_():
    Bandera = True
    while Bandera==True:
        empresas_laburadas = (input("Por favor ingrese UNA empresa en la cual ha laburado: ")).lower().capitalize()
        empresas_trabajadas[Nombre].append(empresas_laburadas)
        option = input("Desea ingresar mas empresas(si/no): ").lower()
        
        if option == "si":
            empresas_laburadas = (input("Por favor ingrese UNA empresa en la cual ha laburado: "))
            empresas_trabajadas[Nombre].append(empresas_laburadas)
            option = input("Desea ingresar mas empresas(si/no): ").lower()
            
        elif option == "no":
            Bandera=False
        print("*************************")
def lenguajes_programacion_():
    Bandera = True
    while Bandera==True:
        lenguajes_conocidos = (input("Por favor ingrese el nombre de UN lenguaje de programacion que conozca: ")).lower().capitalize()
        lenguajes_programacion[Nombre].append(lenguajes_conocidos)
        option = input("Desea ingresar mas lenguajes(si/no): ").lower()
        
        if option == "si":
            empresas_laburadas = (input("Por favor ingrese el nombre de UN lenguaje de programacion que conozca: ")).lower().capitalize()
            lenguajes_programacion[Nombre].append(lenguajes_conocidos)
            option = input("Desea ingresar mas lenguajes(si/no): ").lower()
            
        elif option == "no":
            Bandera=False
            print("*********************")
def idiomas_():
    Bandera = True
    while Bandera==True:
        idiomas_conocidos = (input("Por favor ingrese UN idioma que conoce: ")).lower().capitalize()
        idiomas[Nombre].append(idiomas_conocidos)
        option = input("Desea ingresar mas idiomas(si/no): ").lower()
        
        if option == "si":
            idiomas_conocidos = (input("Por favor ingrese UN idioma que conoce: ")).lower().capitalize()
            idiomas[Nombre].append(idiomas_conocidos)
            option = input("Desea ingresar mas idiomas(si/no): ").lower()
            
        elif option == "no":
            Bandera=False
        print("******************")  
def edad_():
    edad_actual = int(input("Por favor ingrese su edad:"))
    
    edad[Nombre] = edad_actual
    print("****************************")
def id_():
    ID = int(input("Por favor ingrese su ID:"))
    
    id[Nombre] = ID
    print("****************************")
def email_():
    email_actual = input("Por favor ingrese su email actual:").lower()
    
    email[Nombre] = email_actual
    print("****************************")
def color_():
    color_d = input("Por favor ingrese su color favorito: ").lower().capitalize()
    
    color[Nombre] = color_d
    print("****************************")
def pais_origen_():
    pais = input("Por favor ingrese su pais de origen: ").lower().capitalize()
    
    pais_origen[Nombre] = pais
    print("****************************")   
def eleccion_():   

    print ("Escoja su lenguaje favorito:")
    print("")
    lenguajes = {1: 'python',2: 'java', '3':'c++'}
    print("1.python")
    print("2.c++")
    print("3.JavaScript")
    decision = int(input("Ingrese el numero: "))
    
    eleccion[Nombre]=lenguajes[decision]
    
print("Nombre:", list(experiencia_laboral.keys()[0]), "años de experiencia laboral:", list(experiencia_laboral.values()), "empresas trabajadas: ", 
      list(empresas_trabajadas.values()), "lenguajes de programacion:", list(lenguajes_programacion.values()), "idiomas:" list(idiomas.values()), 
      "edad:", list(idiomas), "id:", list(edad.values()), "id:",list(id.values()), "email:", list(email.values()), "color:" list(color.values()),pais )