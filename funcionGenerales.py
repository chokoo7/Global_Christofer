from funcionPDF import *
from DatosEstaticos import *
import random
listaNombre = []
listaEdades = []
listaRFC = []
listaCURP= []
ListaTel = []
aleatorio = random.choice(nomTrabajadores)
areaAlet = random.choice(area)



def menu():
    print("MENU PRIMARIO")
    op = 1
    while(op!=0):   
        print("Bienvenido al SAT, escoje una de las opciones")
        print("1. Solicitar cita")
        print("2. Cuenta con cita")
        print("3. Soy empleado")
        print("0. Salir")
        print("----------------")
        op = int(input("Elige una opcion "))
        if(op == 1):
            #menuSecundario()
            menuRFC()
            #pedirDatos()
           # imprimirClientes()
            print("--------------------------------")
        elif(op == 2):
            numC = int(input("Ingresa tus 2 ultimos digitos del folio: "))
            print(f"Eres {nomClientes[numC-1]}  RFC es {RFC[numC-1]}     Telefono: {numTelCliente[numC-1]}")
            print("--------------------------------")
        elif(op==3):
            #impimirTrabajadores()
            numT = int(input("Cual es tu numero de trabajador? 2 digitos:  "))
            print(f"Eres {nomTrabajadores[numT-1]} y tu numero de trabajador : {numTrabajadores[numT-1]}   Area: [{areaAlet}]")
        #     print("--------------------------------")
        # elif(op==4):
        #     imprimirDatos()
        #     print("--------------------------------")
        # elif(op==6):
        #     generarPDF(listaNombre, listaEdades)
        #     print("--------------------------------")


def menuSecundario():
    print("MENU SECUNDARIO")
    op = 1
    while( op!=3):
        print("Selecciona el motivo de la cita ")
        #print("1. Atencion al compribuyente")
        print("1. Trámites del RFC")
        print("2. Declaración")
        print("3. Generar PDF")
        print("4. Volver")
        print("-----------------------")
        op = int(input("Elige una opcion: "))
        if(op == 1):
            menuRFC()
        elif(op == 2): 
            print("Bienvendio al área Declaración")
            print("-----------------------")
        elif(op == 3):
            generarPDF(listaNombre, listaEdades)
            print("--------------------------------")
            
        elif(op == 4):
            menu()
            #pass


def menuRFC(): 
     
     op2 = 1
     while( op2!=5):
        print("Bienvenido al traime de citas")
        print("1. Sacar RFC")
        print("2. Actualizar RFC")
        print("3. Verificar informacion")
        print("4. Generar PDF")
        print("5. Volver")
        op2 = int(input("Elige una opcion para continuar "))
        print("-----------------------")

        if(op2 == 1):
            pedirDatos()
            print("-------------------------")

        elif(op2 == 2):
            pedirActualizacionRFC()
            print("-----------------------------------")
        elif(op2== 3):
           imprimirDatos()
           print("---------------------------")

        elif(op2==4):
            if(listaNombre == 0):
                print("NO HAT DATOS")
            else:
                generarPDF(listaNombre, listaEdades)
                #print("--------------------------------")


# def menuPrincipal(): 
#     op = 1
#     while( op!=3):
#         print("1. Solicitar cita")
#         print("2. Cuento con cita")
#         print("3. Soy empleado")
#         op = int(input("Elige una opcion: "))
#         if(op == 1):
#             menu()
#         elif(op == 2):
#             pass


def pedirDatos():
    
    print("Hola buenas tardes")
    aleatorio = random.choice(nomTrabajadores)
    print("Mi nombre es ",aleatorio," te voy a ayudar a generar tú RFC")
    print("Empezemos con tu tratime de RCF")
    listaNombre.append(input("Ingresa tu nombre completo (empezando con apellidos) : "))
    listaEdades.append(input("Ingresa tu edad actualmente:  "))
    listaCURP.append(input("Ingresa tu CURP(18 caracteres): "))

    ListaTel.append(input("Ingresa un numero telefonico(10 digitos): "))
    print("Se aguardaron correctamente :)")
    #imprimirDatos()
    
def pedirActualizacionRFC():
    print("Bienvendio")
    print("Mi nombre es ",aleatorio," te voy a ayudar a actualizar tú RFC")
    listaNombre.append(input("Ingresa tu nombre completo (empezando con apellidos) : "))
    listaEdades.append(input("Ingresa tu edad actualmente:  "))
    listaCURP.append(input("Ingresa tu CURP(18 caracteres): "))
    ListaTel.append(input("Ingresa un numero telefonico(10 digitos): "))
    listaRFC.append(input("Ingresa tu RFC: "))
    print("Cambio exitoso ")
    print("Tu nuevo RFC es: ")

def imprimirDatos():
    print("Tus datos son: ")
    for i in range(len(listaNombre)):
        print(f"Nombre: {listaNombre[i]} Edad: {listaEdades[i]}  CURP: {listaCURP[i]}   Telefono: {ListaTel[i]}")
    print("Tu RFC es: ")
   






def Declaracion():
    print("Bienvendio")
    print("Mi nombre es ",aleatorio," te voy a ayudar a actualizar tú Declaración")

def imprimirActualizacionRFC():
    print("Los nuevos datos son: ")


def impimirTrabajadores():
    Trabajadores()

def imprimirClientes():
    Clientes()


