import os
from PIL import Image

path = os.getcwd()

height = int(input("Enter height of the image: "))
width = int(input("Enter width of the image: "))

ext = (".png",".jpg",".jpeg")

folder = os.path.join(path,"ConvertImage")

if not os.path.isdir(folder):
	os.mkdir(folder)

files = os.listdir(path)

images = [file for file in os.listdir(path) if file.endswith(ext)]

#print(images)

for image in images:
	#print(image)
	#filename, ext = os.path.splitext(image)
	#print(filename, " ", ext)
	img = Image.open(image)
	img1 = img.resize((height,width))
	img1.save(f"{folder}/{image}")
