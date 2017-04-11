from PIL import Image
from pytesseract import *

# image_file = "inja addresse file akseto bede"

im = Image.open("captcha.jpg")
# im.show()

text = image_to_string(im)
# print(text)
