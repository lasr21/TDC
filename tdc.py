import Image
import os
import StringIO

im = Image.open("elena.jpg").convert("L")


miau = list(im.getdata())
print (im.getpixel((2,2)))

for n in  range(0,256):
	for m in range(0,256):
		im.putpixel((n,m),200)
im.show()