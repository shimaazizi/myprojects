import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
#creating text for which we want to create the QR code
qrcode = pyqrcode.create('welcom')
#saving the QR code
qrcode.png('welcomqrcode.png',scale=8)
#decoding image
decocdeQR = decode(Image.open('welcomqrcode.png'))
#print data , first data is in binary format so we are changing it into the ASII format
print(decocdeQR[0].data.decode('ascii'))