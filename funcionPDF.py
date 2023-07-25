from reportlab.pdfgen import canvas
ruta = "C:/Users/adanz/OneDrive/Escritorio/ModalidadPython/pruebaFunciones/"
nombreArchivo = ruta + "reporteGlobal.pdf"

def generarPDF(listaNombre,listaEdades):
    c = canvas.Canvas(nombreArchivo)
    xInicial = 200
    yInicial = 700
    for i in range(len(listaNombre)):

        c.drawString(200,600,"Hola desde una funcion")
        yInicial = yInicial -20
    c.save()
    print("Reporte generado----------------")
