import pyqrcode

details = "www.shimulit.com"

qrcode = pyqrcode.create(details)

qrcode.svg('details.svg', scale=8)