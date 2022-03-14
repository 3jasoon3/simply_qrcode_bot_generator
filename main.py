import qrcode
def make_qr(message):	
	filename = "readyqr.png"
	img = qrcode.make(message)
	img.save(filename)
