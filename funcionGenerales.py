from funcionPDF import *
from DatosEstaticos import *
listaNombre = []
listaEdades = []
listaRFC = []
listaArea = []

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
        print("1. Atencion al compribuyente")
        print("2. Recaudación")
        print("3. Volver")
        op = int(input("Elige una opcion: "))
        if(op == 1):
            print("Bienvenido al área de  Atencion al comrpibuyente")
        elif(op == 2): 
            print("Bienvendio al área Recaudacion")
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
        op = int(input("Elige una opcion "))
        if(op == 1):
            pedirDatos()
           # imprimirClientes()
            print("--------------------------------")
        elif(op == 2):
            numC = int(input("Ingresa tus 2 ultimos digitos del folio: "))
            print(f"Eres {nomClientes[numC-1]} y tu RFC es {RFC[numC-1]}")
            print("--------------------------------")
        elif(op==3):
            #impimirTrabajadores()
            numT = int(input("Cual es tu numero de trabajador? 2 digitos:  "))
            print(f"Eres {nomTrabajadores[numT-1]} y tu numero es {numTrabajadores[numT-1]}")
            print("--------------------------------")
        elif(op==4):
            imprimirDatos()
            print("--------------------------------")
        elif(op==5):
            print("cso 5")
            imprimirClientes()
            print("--------------------------")
        elif(op==6):
            generarPDF(listaNombre, listaEdades)
            print("--------------------------------")
        elif(op==7):
            print("Cso 7")
            print("--------------------------------")

def pedirDatos():
    print("Hola buenas tardes")
    print("Empezemos con tu tratime de cita")
    listaNombre.append(input("Ingresa tu nombre completo (empezando con apellidos) : "))
    listaEdades.append(input("Ingresa tu edad actualmente:  "))
    listaRFC.append(input("Ingresa tu RFC: "))
    menuSecundario()

    print("Guardado")

def imprimirDatos():
    for i in range(len(listaNombre)):
        print(f"Nombre: {listaNombre[i]} Edad: {listaEdades[i]}  RFC: {listaRFC[i]}")

def Cita():
    print("Te gustaria hacer un tramite")
    opcion = int(input("Elige una opcion: "))

def impimirTrabajadores():
    Trabajadores()

def imprimirClientes():
    Clientes()

def contribuyente():
    print("-------------")