
##virtualenv /venv/pillow
##venv/webscraping/scripts/activate.ps1
##pip install pillow

from PIL import Image, ImageFilter
import string
myImage = Image.open
myImage.load


myImage.format
myImage.size
myImage.show()


blur = myImage.filter(ImageFilter(BLUR)).show()
quit()