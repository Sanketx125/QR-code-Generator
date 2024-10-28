import qrcode as qr

data = input("Enter data for QR code : ")

img = qr.make(data)

title = input("Enter name for QR code : ")
img.save(title +"_QR_code.png")