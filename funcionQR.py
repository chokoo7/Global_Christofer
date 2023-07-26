import qrcode
def generarQR(nomnbreQR, informacion):
    img = qrcode.make(informacion)
    f = open(nomnbreQR, "wb")
    img.save(f)
    f.close()