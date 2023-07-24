listaNombre = []
listaEdades = []

def menu():
    op = 1
    while(op!=0):   
        print("1. Pedir datos")
        print("2. Imprimir datos")
        print("3. Generar PD")
        print("4. Generar QR")
        print("0. Salir")
        op = int(input("Elige una opcion "))
        if(op == 1):
            pedirDatos()
        elif(op == 2):
            imprimirDatos

def pedirDatos():
    listaNombre.append(input("Ingresa un nombre "))
    listaEdades.append(input("Ingresa una edad "))
    print("Guardado")

def imprimirDatos():
    for i in range(len(listaNombre)):
        print(f"Nombre: {listaNombre[i]} Edad: {listaEdades[i]}")