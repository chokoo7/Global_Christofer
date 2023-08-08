from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from funcionQR import *
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import datetime
import locale
locale.setlocale(locale.LC_ALL, '')

ruta = "C:/Users/adanz/OneDrive/Escritorio/ModalidadPython/pruebaFunciones/"

nombreQR = ruta + "miQr.png"
rutaImg= "C:/Users/adanz/OneDrive/Escritorio/ModalidadPython/pruebaFunciones/prueba.png"
rutaImg2 = "C:/Users/adanz/OneDrive/Escritorio/ModalidadPython/pruebaFunciones/shcp.jpg"



def generarPDF(listaNombre, listaEdades):
    fecha_actual = datetime.datetime.now()
    nombreArchivo = ruta + "reporteGlobal"+fecha_actual.strftime('%d_%m_%Y_%H_%M_%S')+".pdf"
    generarQR(nombreQR, "Hola desde funcon")
    c = canvas.Canvas(nombreArchivo,  pagesize=(650,400))
    rutaFuente= "c:/Windows/Fonts/KUNSTLER.TTF"
    pdfmetrics.registerFont(TTFont('Mifuente',rutaFuente))
    c.setFont("Mifuente",12)    
    xInicial = 200
    yInicial = 300
    c.rect(xInicial-200,yInicial-20,300,300)
    c.drawImage(rutaImg, 400, 280, width=150, height=70)
    c.drawImage(rutaImg2, 80, 250, width=190, height=130) 
    c.setFont("Mifuente", 15)
    # c.drawString(xInicial-200, yInicial+ 85," ----------------------------------------------------------------------------------------------------------------------------- ")
    # c.setFont("Helvetica-Bold", 20)
    c.drawString(xInicial - 30 ,yInicial + 60,"Cédula de Identificación Fiscal")
    # c.setFont("Helvetica-Bold", 15)
    # c.drawString(xInicial- 200, yInicial +45," ------------------------------------------------------------------------------------------------------------------------------- ")


    c.setFont("Helvetica-Bold", 20)
    c.drawString(xInicial+150, yInicial-40,"RFC CONTRIBUYENTE 000")

    c.setFont("Helvetica", 12)
    c.drawString(xInicial+150, yInicial-60,"Registro Federal de Contribuyentes")

    c.setFont("Helvetica-Bold", 10)
    c.drawString(xInicial+150,yInicial-160,"Edad")
    c.drawString(xInicial+150,yInicial-140,"NOMBRE CONTRIBUYENTE")
    c.drawImage(nombreQR,xInicial - 150 ,yInicial-300,270,290)
    

    for i in range(len(listaNombre)):
        
        c.setFont("Helvetica", 8)
        yInicial = yInicial - 160
        c.drawString(xInicial,yInicial,listaEdades[i])
        c.drawString(xInicial + 160 ,yInicial-400,listaNombre[i])
    c.save()
    print("Reporte generado------------------")
