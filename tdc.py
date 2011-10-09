import Image
import os

im = Image.open("elena.jpg").convert("L")


miau = list(im.getdata())

print(miau)
