import qrcode

website_link = input("What is the link you wish to create a qr code for? ")

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color = 'black', back_color = 'white')
img.save('Python_qr.png')
