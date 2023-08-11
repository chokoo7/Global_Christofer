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
    generarQR(nombreQR, "La solicitud fue todo un exito empezaremos con el tramite lo antes posible")
    c = canvas.Canvas(nombreArchivo,  pagesize=(650,400))
    rutaFuente= "c:/Windows/Fonts/KUNSTLER.TTF"
    #Aqui va el for
    if (len(listaNombre)<1):
        print("NO hay datos")
    else:

        for i in range(len(listaNombre)):
            pdfmetrics.registerFont(TTFont('Mifuente',rutaFuente))
            c.setFont("Mifuente",12)    
            xInicial = 200
            yInicial = 300
            
            c.drawImage(rutaImg, 400, 270, width=150, height=70)
            c.drawImage(rutaImg2, 80, 227, width=210, height=130) 

            color = (0,0,0)
            c.setFillColor(color)
        
            c.rect(0,350,700,55,fill=True)
            c.setFillColorRGB(*color)

            c.setFillColorRGB(1, 1, 1)

            c.setFont("Helvetica-Bold", 20)
            c.drawString(xInicial - 30 ,yInicial + 60,"Cédula de Identificación Fiscal")
        

            c.setFillColorRGB(0,0,0)
            c.setFont("Helvetica-Bold", 20)
            c.drawString(xInicial+150, yInicial-50,"RFC CONTRIBUYENTE 00"+str(i+1))

            c.setFont("Helvetica", 12)
            c.drawString(xInicial+150, yInicial-70,"Registro Federal de Contribuyentes ")

            c.setFont("Helvetica-Bold", 13)
            c.drawString(xInicial+150,yInicial-140,"NOMBRE CONTRIBUYENTE")
            c.drawImage(nombreQR,xInicial - 150 ,yInicial-270,270,230)

            c.setFont("Helvetica", 12)
            c.drawString(350,130,listaNombre[i])

            c.setFont("Helvetica-Bold", 13)
            c.drawString(xInicial+150,yInicial-220,"DENOMINACION O RAZON SOCIAL")

        
            #yInicial = yInicial - 160
        
            
            #c.drawString(350,50,listaEdades[i])
            
            #c.drawString(xInicial+160, yInicial-240,"odaaaaa")


            # for i in range(len(listaNombre)):
                
            #     c.setFont("Helvetica", 9)
            #     #yInicial = yInicial - 160
            #     #c.drawString(xInicial,yInicial,listaEdades[i])
            #     c.drawString(xInicial + 160 ,yInicial-160,listaNombre[i])
            #     c.drawString(xInicial+160, yInicial-240,"odaaaaa")
            c.showPage()
        c.save()
        print("Reporte generado")


def generarComprobante(numC, nomClientes,motivo,RFC):
    fecha_actual = datetime.datetime.now()
    nombreArchivo = ruta + "reporte_"+nomClientes[numC]+fecha_actual.strftime('%d_%m_%Y_%H_%M_%S')+".pdf"
    generarQR(nombreQR, "La solicitud fue todo un exito empezaremos con el tramite lo antes posible")
    c = canvas.Canvas(nombreArchivo,  pagesize=(650,400))
    rutaFuente= "c:/Windows/Fonts/KUNSTLER.TTF"
    pdfmetrics.registerFont(TTFont('Mifuente',rutaFuente))
    c.setFont("Mifuente",12)    
    xInicial = 200
    yInicial = 300
    
    c.drawImage(rutaImg, 400, 270, width=150, height=70)
    c.drawImage(rutaImg2, 80, 227, width=210, height=130) 

    color = (0,0,0)
    c.setFillColor(color)
   
    c.rect(0,350,700,55,fill=True)
    c.setFillColorRGB(*color)

    c.setFillColorRGB(1, 1, 1)

    c.setFont("Helvetica-Bold", 20)
    c.drawString(xInicial - 30 ,yInicial + 60,"Cédula de Identificación Fiscal")
    
    c.setFillColorRGB(0,0,0)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(xInicial+140, yInicial-50,"RFC CONTRIBUYENTE "+RFC[numC])

    c.setFont("Helvetica", 12)
    c.drawString(xInicial+150, yInicial-70,"Registro Federal de Contribuyentes")

    c.setFont("Helvetica-Bold", 13)
    c.drawString(xInicial+150,yInicial-140,"NOMBRE CONTRIBUYENTE")
    c.drawImage(nombreQR,xInicial - 150 ,yInicial-270,270,230)

    c.setFont("Helvetica-Bold", 13)
    c.drawString(xInicial+150,yInicial-220,"DENOMINACION O RAZON SOCIAL")


    
    
    c.setFont("Helvetica", 9)
        
    c.drawString(xInicial + 160 ,yInicial-160,nomClientes[numC])
    c.drawString(xInicial+160, yInicial-240,motivo)
    c.save()
    print("Reporte generado")

