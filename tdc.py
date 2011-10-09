import Image
import os
import StringIO
import math

im = Image.open("elena.jpg").convert("L")
im2 = Image.open("elena.jpg").convert("L")
im.copy()

im.show()

for bi in  range(0,32):
	for bj in range(0,32):
		for i in range(0,7):
			for j in range(0,7):
				acumulador = 0
				for m in range(0,7):
					for n in range(0,7):
						indice1 = (((((2*m)+1)*i)*(math.pi))/16)
						indice2 = (((((2*n)+1)*j)*(math.pi))/16)
						acumulador = (acumulador+ ( (im.getpixel((((bi*8)+m),((bj*8)+n))) )*(math.cos(math.radians(indice1)))*(math.cos(math.radians(indice2))) ) )
				im2.putpixel( ( ((bi*8)+i) ,((bj*8)+j) ),(acumulador/64))
im2.show()

