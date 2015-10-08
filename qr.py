import qrtools
qr = qrtools.QR()
qr.decode('qr2.jpg')
print qr.data