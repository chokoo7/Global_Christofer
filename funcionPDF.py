from reportlab.pdfgen import canvas
from funcionQR import *
ruta = "C:/Users/adanz/OneDrive/Escritorio/ModalidadPython/pruebaFunciones/"
nombreArchivo = ruta + "reporteGlobal.pdf"
nombreQR = ruta + "miQr.png"

def generarPDF(listaNombre, listaEdades):
    generarQR(nombreQR, "Hola desde funcon")
    c = canvas.Canvas(nombreArchivo)
    xInicial = 200
    yInicial = 700
    c.setFont("Helvetica", 20)
    c.drawString(xInicial,yInicial,"Edad")
    c.drawString(xInicial + 120 ,yInicial,"Nombre")
    c.drawImage(nombreQR,200,400,100,100)
    for i in range(len(listaNombre)):
        c.setFont("Helvetica", 18)
        yInicial = yInicial - 20
        c.drawString(xInicial,yInicial,listaEdades[i])
        c.drawString(xInicial + 120 ,yInicial,listaNombre[i])
       
    c.save()
    print("Reporte generado----------------")
