from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('details.png')

d = decode(img)

print(d[0].data.decode())
