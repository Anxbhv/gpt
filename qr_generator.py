import qrcode


img = qrcode.make("www.google.com")
img.save("jpg.jpg")