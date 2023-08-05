from reportlab.pdfgen import canvas
from funcionQR import *
import datetime
import locale
locale.setlocale(locale.LC_ALL, '')

ruta = "C:/Users/adanz/OneDrive/Escritorio/ModalidadPython/pruebaFunciones/"

nombreQR = ruta + "miQr.png"

def generarPDF(listaNombre, listaEdades):
    fecha_actual = datetime.datetime.now()
    nombreArchivo = ruta + "reporteGlobal"+fecha_actual.strftime('%d_%m_%Y_%H_%M_%S')+".pdf"
    generarQR(nombreQR, "Hola desde funcon")
    c = canvas.Canvas(nombreArchivo)
    xInicial = 200
    yInicial = 700
    
    c.setFont("Helvetica-Bold", 20)
    c.drawString(xInicial - 50 ,yInicial + 90,"Cédula de Identificación Fiscal")

    c.setFont("Helvetica", 10)
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
