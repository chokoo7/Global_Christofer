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

def menuSecundario():
    op = 1
    while( op!=3):
        print("Selecciona el motivo de la cita ")
        #print("1. Atencion al compribuyente")
        print("1. Trámites del RFC")
        print("2. Declaración")
        print("3. Volver")
        print("-----------------------")
        op = int(input("Elige una opcion: "))
        if(op == 1):
            menuRFC()
        elif(op == 2): 
            print("Bienvendio al área Declaración")
            print("-----------------------")
        elif(op == 3):
            pass


def menu():
    op = 1
    while(op!=0):   
        print("Bienvenido al SAT, escoje una de las opciones")
        print("1. Solicitar cita")
        print("2. Cuenta con cita")
        print("3. Soy empleado")
        #print("4. Confirmar cita")
        #print("5.Cambiar cita o tramite")
        #print("6. Generar comprobante") #PDF
        #print("6. Generar QR")
        #print("7. Atencion al cliente")
        print("0. Salir")
        print("----------------")
        op = int(input("Elige una opcion "))
        if(op == 1):
            menuSecundario()
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
            print("--------------------------------")
        elif(op==4):
            imprimirDatos()
            print("--------------------------------")
        elif(op==6):
            generarPDF(listaNombre, listaEdades)
            print("--------------------------------")
        

def menuRFC(): 
     op = 1
     while( op!=3):
        print("Bienvenido al traime del RFC")
        print("1. Sacar RFC")
        print("2. Actualizar RFC")
        print("3. Volver")
        op = int(input("Elige una opcion "))
        print("-----------------------")
        #print("2. Cuento con cita")
        #print("3. Soy empleado")
        if(op == 1):
            pedirDatos()
            print("-------------------------")
        elif(op == 2):
            pedirActualizacionRFC()
            print("-------------------------")
        elif(op ==3):
            pass

def pedirDatos():
    print("Hola buenas tardes")
    print("Mi nombre es ",aleatorio," te voy a ayudar a generar tú RFC")
    print("Empezemos con tu tratime de RCF")
    listaNombre.append(input("Ingresa tu nombre completo (empezando con apellidos) : "))
    listaEdades.append(input("Ingresa tu edad actualmente:  "))
    listaCURP.append(input("Ingresa tu CURP(18 caracteres): "))
    ListaTel.append(input("Ingresa un numero telefonico(10 digitos): "))
    print("Se aguardaron correctamente :)")
    print("--------------------------")
    imprimirDatos()
    menuSecundario()

def imprimirDatos():
    print("Tus datos son: ")
    for i in range(len(listaNombre)):
        print(f"Nombre: {listaNombre[i]} Edad: {listaEdades[i]}  CURP: {listaCURP[i]}   Telefono: {ListaTel[i]}")
    print("Tu RFC es: ")
    print("----------------------------")

def pedirActualizacionRFC():
    print("Bienvendio")
    print("Mi nombre es ",aleatorio," te voy a ayudar a actualizar tú RFC")

def imprimirActualizacionRFC():
    print("Los nuevos datos son: ")



def impimirTrabajadores():
    Trabajadores()

def imprimirClientes():
    Clientes()
